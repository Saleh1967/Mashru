# -*- coding: utf-8 -*-
"""T1..T8 — تُشغَّل: python3 -I by-hussein/tabaqat4/tests/test_tabaqat4.py  (من أيّ مكان ؛ MASHRU_ROOT يُكتشف أو يُعيَّن)
كلّ اختبار يطبع اسمه وحالته: PASS / FAIL / NOT_RUN(سبب). لا يُخفَّف شرطٌ ليمرّ."""
import os, sys, json, subprocess, shutil, tempfile, unittest
from pathlib import Path
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; TOOL = HERE.parent
sys.path.insert(0, str(TOOL))
from t4.core import Tabaqat4, sha256_text, AXIOMS_OK      # noqa
from t4.dal import load_hawamil, encode_word              # noqa
from t4.report import write_all                           # noqa


def mashru_root() -> Path:
    env = os.environ.get('MASHRU_ROOT')
    if env: return Path(env)
    for p in TOOL.parents:
        if (p / 'lakefile.toml').exists() and (p / 'Dal' / 'Makharij.lean').exists(): return p
    raise SystemExit('MASHRU_ROOT_NOT_FOUND')


ROOT = mashru_root()
TMP = Path(tempfile.mkdtemp(prefix='tabaqat4_tests_'))


def lean_available() -> str:
    """'' إن كان lake env lean يعمل ومكتبة Jisr.Utur مبنية ، وإلّا السبب."""
    probe = TMP / 'probe.lean'; probe.write_text('import Jisr.Utur\nimport Aql.Isnad\n#eval 1\n', encoding='utf-8')
    try:
        p = subprocess.run(['lake', 'env', 'lean', str(probe)], cwd=str(ROOT), capture_output=True, text=True, timeout=600)
        return '' if p.returncode == 0 else 'LEAN_PROBE_FAILED: ' + (p.stderr or p.stdout).strip().splitlines()[0][:200]
    except FileNotFoundError: return 'LAKE_NOT_FOUND'
    except subprocess.TimeoutExpired: return 'LEAN_PROBE_TIMEOUT'


LEAN_REASON = lean_available()
RESULTS = {}


class T(unittest.TestCase):
    def rec(self, text, lean=True, **kw):
        # مجلّدٌ فريدٌ بالنصّ والوسائط كي لا تتشارك اختباراتٌ على الجملة نفسها (بمودَع/بلا) مجلّدًا واحدًا
        kw.setdefault('load_default_mudaat', False)   # الاختبارات محصّنةٌ عن المعجم الحيّ (المودَعات RATIFIED) ؛ كلٌّ يعلن مودَعه
        key = text + '|lean=' + str(lean) + '|' + json.dumps({k: str(v) for k, v in sorted(kw.items())}, ensure_ascii=False)
        t = Tabaqat4(ROOT, out_dir=TMP / sha256_text(key)[:10], run_lean=lean and not LEAN_REASON, **kw)
        return t.run(text)

    def test_T1_shahid_four_layers(self):
        """T1 ذَهَبَ الْوَلَدُ → الأربع «مبرهن على الشاهد» ، النظريات تطابق Shahid_Ahmad.lean ، axioms ⊆ الثلاث"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        r = self.rec('ذَهَبَ الْوَلَدُ')
        self.assertEqual(r['dal'][0]['khalaya'], [92, 4, 104]); self.assertEqual(r['dal'][1]['khalaya'], [55, 112, 52, 69])
        th = r['lean']['theorems']
        self.assertTrue(all(v['passed'] for v in th.values()), th)
        self.assertEqual(r['lean']['observed']['hukm3'], '.murakhkhas')
        self.assertEqual(r['lean']['observed']['zaman'], 'some .madi')
        for k in (1, 2, 3, 4): self.assertEqual(r['tabaqat_state'][k], 'مبرهن على الشاهد', (k, r['tabaqat_state']))
        for v in th.values(): self.assertTrue(set(v['axioms']) <= AXIOMS_OK)

    def test_T2_no_sealed_madlul(self):
        """T2 كَتَبَ الطَّالِبُ الدَّرْسَ → S2 كامل ، S4 NO_SEALED_MADLUL ، S5 متوقّف مُعلَن ، لا ملف Lean"""
        r = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ')
        self.assertTrue(all(not d['residuals'] for d in r['dal']))
        s4 = [s for s in r['stages'] if s['stage'] == 'S4_MADLUL'][0]
        self.assertEqual(sum('NO_SEALED_MADLUL' in x for x in s4['residuals']), 3)
        self.assertIsNone(r['plan']); self.assertIsNone(r['lean'])
        self.assertFalse((Path(r['run_dir']) / 'Jumla.lean').exists())

    def test_T3_out_of_executed_path(self):
        """T3 الْعِلْمُ نُورٌ → OUT_OF_EXECUTED_PATH:جملة اسمية ؛ S2 يتمّ ؛ لا hukm3"""
        r = self.rec('الْعِلْمُ نُورٌ')
        self.assertTrue(all(not d['residuals'] for d in r['dal']), r['dal'])
        s5 = [s for s in r['stages'] if s['stage'] == 'S5_MAAN_ITAR'][0]
        self.assertIn('OUT_OF_EXECUTED_PATH:جملة اسمية', s5['reason']); self.assertIsNone(r['lean'])

    def test_T4_unvocalized_refused(self):
        """T4 نصّ غير مشكول → يُرفَض في S0 بسبب مُعلَن ، لا تطبيع صامت"""
        r = self.rec('ذهب الولد')
        self.assertFalse(r['stages'][0]['accepted']); self.assertIn('NASS_GHAYR_MASHKUL', r['stages'][0]['reason'])
        self.assertIsNone(r['tokens'])

    def test_T5_corrupt_cell_changes_verdict(self):
        """T5 إفساد خلية واحدة (دُ→دَ ، 69→68) في الكلمة الثانية → hukm3 يتغيّر عن مرخَّص (Utur.lean:958 يتوقّع mumtani) ، ولا يُخفى"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        good = self.rec('ذَهَبَ الْوَلَدُ'); bad = self.rec('ذَهَبَ الْوَلَدَ')
        self.assertEqual(bad['dal'][1]['khalaya'], [55, 112, 52, 68])
        self.assertEqual(good['lean']['observed']['hukm3'], '.murakhkhas')
        self.assertNotEqual(bad['lean']['observed']['hukm3'], '.murakhkhas')
        self.assertIn('ممتنع' if bad['lean']['observed']['hukm3'] == '.mumtani' else 'لا حكم', json.dumps(bad['claims'], ensure_ascii=False))

    def test_T6_unknown_madlul_refused(self):
        """T6 كلمة ليست في qamus (ببصمة/مدلول غير معرَّف) → S4 يرفض بناءها ولا يُولَّد لها Itar3"""
        r = self.rec('ذَهَبَ الرَّجُلُ')
        self.assertIsNone(r['maani'][1]); self.assertIsNone(r['plan'])

    def test_T7_determinism(self):
        """T7 تشغيلان للنصّ نفسه → JSON متطابق خارج حقل الطابع الزمني وهوية المجلد"""
        a = self.rec('ذَهَبَ الْوَلَدُ', lean=False); b = self.rec('ذَهَبَ الْوَلَدُ', lean=False)
        for r in (a, b): r.pop('timestamp_utc'); r.pop('run_dir'); r['identity'].pop('mashru_status_porcelain', None)
        self.assertEqual(json.dumps(a, ensure_ascii=False, sort_keys=True), json.dumps(b, ensure_ascii=False, sort_keys=True))

    def test_T8_mashru_untouched(self):
        """T8 شجرة Mashru: git status --porcelain قبل = بعد ، ولا ملف جديد خارج TOOL_ROOT/_runs أو --out"""
        def st(): return subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain', '--untracked-files=all'], capture_output=True, text=True).stdout
        before = st(); self.rec('ذَهَبَ الْوَلَدُ'); after = st()
        self.assertEqual(before, after, 'MASHRU_TREE_CHANGED')


    def test_T9_jaza_maqbul_proven(self):
        """T9 إِنْ تَجْتَهِدْ تَنْجَحْ + --forms shart=mudariMajzum jawab=mudariMajzum → hukm=⟨maqbul,maqbul⟩ مبرهنًا (مشروطًا بالصيغ) ؛ ط4 NOT_APPLICABLE"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        r = self.rec('إِنْ تَجْتَهِدْ تَنْجَحْ', forms={'shart': 'mudariMajzum', 'jawab': 'mudariMajzum'})
        self.assertEqual(r['plan']['kind'], 'jaza'); self.assertEqual(r['lean']['observed'], {'kalam': '.maqbul', 'shir': '.maqbul', 'sinf': '.jaza'})
        self.assertTrue(all(v['passed'] for v in r['lean']['theorems'].values()))
        self.assertEqual(r['tabaqat_state'][3], 'مبرهن على الشاهد'); self.assertEqual(r['tabaqat_state'][4], 'NOT_APPLICABLE')
        self.assertTrue(any('CONDITIONAL_ON_SUPPLIED_FORMS' in x for s in r['stages'] for x in s['residuals']))

    def test_T10_jaza_qabih_J16(self):
        """T10 إِنْ تَجْتَهِدْ تَنْجَحُ (جواب مرفوع بعد مجزوم) → J16: الكلام قبيح ، الشعر مقبول — مبرهنًا"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        r = self.rec('إِنْ تَجْتَهِدْ تَنْجَحُ', forms={'shart': 'mudariMajzum', 'jawab': 'mudariMarfu'})
        self.assertEqual(r['lean']['observed']['kalam'], '.qabih'); self.assertEqual(r['lean']['observed']['shir'], '.maqbul')
        self.assertTrue(r['lean']['theorems']['jaza_hukm']['passed'])

    def test_T11_jaza_forms_undeclared(self):
        """T11 جملة شرطية بلا --forms → JAZA_FORMS_UNDECLARED ، لا Lean ، لا حكم"""
        r = self.rec('إِنْ تَجْتَهِدْ تَنْجَحْ')
        s5 = [s for s in r['stages'] if s['stage'] == 'S5_MAAN_ITAR'][0]
        self.assertIn('JAZA_FORMS_UNDECLARED', s5['reason']); self.assertIsNone(r['lean']); self.assertIsNone(r['hukm3'])

    def test_T12_qari_witness(self):
        """T12 قارئ Mashru شاهدًا ثانيًا: AGREE على ذَهَبَ الْوَلَدُ (بعد إسقاط همزة الابتداء) ؛ DISAGREE مسمًّى WAQF_VS_WASL على وَلَدٌ الأخيرة"""
        from t4.qari import qari_exe
        if not qari_exe(ROOT): self.skipTest('NOT_RUN: QARI_EXE_ABSENT (lake build qari)')
        a = self.rec('ذَهَبَ الْوَلَدُ', lean=False)
        self.assertEqual([d['qari']['reconcile']['state'] for d in a['dal']], ['AGREE', 'AGREE'])
        self.assertEqual(a['dal'][1]['qari']['khalaya'], [0, 55, 112, 52, 69])
        f = self.rec('ذَهَبَ وَلَدٌ', lean=False)
        rc = f['dal'][1]['qari']['reconcile']; self.assertEqual(rc['state'], 'DISAGREE'); self.assertIn('WAQF_VS_WASL', rc['reason'])
        self.assertTrue(any(c['ism'].startswith('makhzan_') and c['rutba'] == 'تقدير' for c in a['claims']))


    # ───────────────── الإصدار 4: Hokom تقديرًا + صورة الجزاء + split-punct ─────────────────
    def _hokom_ok(self):
        import os as _os
        if not (TOOL / 'hokom_adapter.py').exists(): return 'HOKOM_ADAPTER_ABSENT'
        if not _os.path.exists('/Users/husseinhiyassat/hokom/.venv-taaqol/bin/python'): return 'HOKOM_VENV_ABSENT'
        return None

    def test_T13_jaza_forms_from_hokom(self):
        """T13 --hokom بلا --forms على «إِنْ تَجْتَهِدْ تَنْجَحْ» → الصيغتان من Hokom (HOKOM_TAQDIR، رتبة تقدير) ، hukm=⟨maqbul,maqbul⟩ مبرهنًا"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        hr = self._hokom_ok()
        if hr: self.skipTest('NOT_RUN: ' + hr)
        r = self.rec('إِنْ تَجْتَهِدْ تَنْجَحْ', use_hokom=True)
        self.assertEqual(r['plan']['kind'], 'jaza')
        self.assertEqual(r['plan']['shart'], '.mudariMajzum'); self.assertEqual(r['plan']['jawab'], '.mudariMajzum')
        self.assertIn('HOKOM_TAQDIR', r['plan']['premise_source']); self.assertEqual(r['plan']['premise_rank'], 'تقدير')
        self.assertEqual(r['lean']['observed'], {'kalam': '.maqbul', 'shir': '.maqbul', 'sinf': '.jaza'})
        self.assertTrue(all(v['passed'] for v in r['lean']['theorems'].values()))

    def test_T14_forms_conflict_owner_wins(self):
        """T14 --hokom مع --forms متعارضَين → FORMS_CONFLICT_OWNER_VS_HOKOM مُعلَن ، والمعتمَد صيغة المالك"""
        hr = self._hokom_ok()
        if hr: self.skipTest('NOT_RUN: ' + hr)
        r = self.rec('إِنْ تَجْتَهِدْ تَنْجَحْ', lean=False, use_hokom=True,
                     forms={'shart': 'mudariMarfu', 'jawab': 'mudariMajzum'})
        self.assertIsNotNone(r['plan']['forms_conflict'])
        self.assertIn('FORMS_CONFLICT_OWNER_VS_HOKOM', r['plan']['forms_conflict'])
        self.assertEqual(r['plan']['shart'], '.mudariMarfu')   # المالك يغلب

    def test_T15_hokom_shown_not_consumed(self):
        """T15 --hokom على «ذَهَبَ الْوَلَدُ» → كتلة Hokom حاضرة ، ولا أثر على hukm3/النظريات (طبقتا 3/4 كتشغيلٍ بلا --hokom)"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        hr = self._hokom_ok()
        if hr: self.skipTest('NOT_RUN: ' + hr)
        base = self.rec('ذَهَبَ الْوَلَدُ'); withh = self.rec('ذَهَبَ الْوَلَدُ', use_hokom=True)
        hc = [c for c in withh['claims'] if c['ism'].startswith('hokom_')]
        self.assertEqual(len(hc), 2); self.assertTrue(all(c['rutba'] == 'تقدير' for c in hc))
        self.assertEqual(hc[0]['qima']['final_root'], ['ذ', 'ه', 'ب'])   # ذهب كما يُخرجه Hokom
        # لا أثر على الحكم ولا النظريات
        self.assertEqual(base['lean']['observed'], withh['lean']['observed'])
        self.assertEqual({k: v['passed'] for k, v in base['lean']['theorems'].items()},
                         {k: v['passed'] for k, v in withh['lean']['theorems'].items()})

    def test_T16_hokom_unreadable_named(self):
        """T16 Hokom غير قابل للقراءة (مسار خاطئ) → HOKOM_ADAPTER_FAILED باسمه ، وبقية المراحل تكتمل"""
        import os as _os
        old = _os.environ.get('HOKOM_ROOT')
        _os.environ['HOKOM_ROOT'] = '/nonexistent/hokom_path_xyz'
        try:
            r = self.rec('ذَهَبَ الْوَلَدُ', lean=False, use_hokom=True)
        finally:
            if old is None: _os.environ.pop('HOKOM_ROOT', None)
            else: _os.environ['HOKOM_ROOT'] = old
        s3 = [s for s in r['stages'] if s['stage'].startswith('S3')][0]
        self.assertFalse(s3.get('completed')); self.assertIn('FAILED', s3['reason'])
        # بقية المراحل اكتملت (S4 وصل ، والدالّ تمّ)
        self.assertTrue(any(s['stage'] == 'S4_MADLUL' and s['completed'] for s in r['stages']))
        self.assertEqual(r['dal'][0]['khalaya'], [92, 4, 104])

    def test_T17_split_punct(self):
        """T17 --split-punct على نصّ من جملتَين → تقريران مستقلّان ؛ وبلا الخيار → OUT_OF_EXECUTED_PATH"""
        import os as _os
        run_py = str(TOOL / 'run.py')
        env = dict(_os.environ, PYTHONDONTWRITEBYTECODE='1')
        o = TMP / 'split'
        p = subprocess.run([sys.executable, '-I', run_py, 'ذَهَبَ الْوَلَدُ. ذَهَبَ وَلَدٌ', '--split-punct', '--no-lean', '--out', str(o)],
                           capture_output=True, text=True, env=env, timeout=600)
        self.assertIn('SPLIT_ON_PUNCT_OWNER_OPTION = 2', p.stdout)
        self.assertTrue((o / 's1' / 'taqrir.json').exists() and (o / 's2' / 'taqrir.json').exists())
        s1 = json.loads((o / 's1' / 'taqrir.json').read_text(encoding='utf-8'))
        s2 = json.loads((o / 's2' / 'taqrir.json').read_text(encoding='utf-8'))
        self.assertNotEqual(s1['input']['sha256'], s2['input']['sha256'])
        # بلا الخيار: جملتان في مدخلٍ واحد → OUT_OF_EXECUTED_PATH
        r = self.rec('ذَهَبَ الْوَلَدُ ذَهَبَ وَلَدٌ', lean=False)
        self.assertIsNone(r['plan'])

    def test_T18_both_trees_untouched(self):
        """T18 شجرتا Mashru وHokom لم تُمَسّا (git status قبل/بعد) ولا بايتكود كُتب خارج TOOL_ROOT"""
        import os as _os, glob as _glob
        def st(root): return subprocess.run(['git', '-C', root, 'status', '--porcelain', '--untracked-files=all'], capture_output=True, text=True).stdout
        hk = '/Users/husseinhiyassat/hokom'
        b_m, b_h = st(str(ROOT)), st(hk)
        self.rec('إِنْ تَجْتَهِدْ تَنْجَحْ', lean=False, use_hokom=True) if not self._hokom_ok() else self.rec('ذَهَبَ الْوَلَدُ', lean=False)
        a_m, a_h = st(str(ROOT)), st(hk)
        self.assertEqual(b_m, a_m, 'MASHRU_TREE_CHANGED')
        self.assertEqual(b_h, a_h, 'HOKOM_TREE_CHANGED')
        # لا بايتكود في شجرة Hokom
        self.assertEqual(_glob.glob(hk + '/**/__pycache__/*tabaqat*', recursive=True), [])


    # ───────────────── الإصدار 5: مودَعات المالك + اختيار الإطار ─────────────────
    FX = HERE / 'fixtures'

    def test_T20_mudaat_ratified_daraba_proven(self):
        """T20 كَتَبَ الطَّالِبُ الدَّرْسَ بمودَعات RATIFIED → إطار daraba مختار ، hukm3 مبرهَن ، الطبقة ٤ مبرهَنة ، axioms⊆المسموح ؛ وبلا مودَعات NO_SEALED"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        r = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', mudaat_path=self.FX / 'mudaat_test.json')
        self.assertEqual(r['plan']['ud'], 'Jisr.Mulhaqat.daraba'); self.assertTrue(r['plan']['maful'])
        self.assertIn('darabaFata', r['plan']['shahid_mashru'])   # G4: شاهد daraba الصحيح (لا bimafulayn)
        self.assertIn('CONDITIONAL_ON_SELECTED_ITAR', json.dumps(r['la_yuddaa'], ensure_ascii=False))
        th = r['lean']['theorems']; self.assertTrue(all(v['passed'] for v in th.values()), th)
        for v in th.values(): self.assertTrue(set(v['axioms']) <= AXIOMS_OK)
        self.assertEqual(r['lean']['observed']['hukm3'], '.murakhkhas')
        for k in (1, 2, 3, 4): self.assertEqual(r['tabaqat_state'][k], 'مبرهن على الشاهد', (k, r['tabaqat_state']))
        self.assertIsNone(self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False)['plan'])   # بلا مودَعات: كما اليوم

    def test_T21_mudaa_without_qabiliyya_laHukm(self):
        """T21 الطالب مودَع بلا قابليّة «كتب» → hukm3 = laHukm (قاعدة Mashru لا الأداة)"""
        if LEAN_REASON: self.skipTest('NOT_RUN: ' + LEAN_REASON)
        r = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', mudaat_path=self.FX / 'mudaat_t21.json')
        self.assertEqual(r['lean']['observed']['hukm3'], '.laHukm')

    def test_T22_hokom_tree_sha_before_eq_after(self):
        """T22 شرط المالك: sha256 **المحتوى** لكلّ ملفّ في HOKOM_ROOT (لا الميتاداتا) قبل=بعد ؛ Mashru نظيف ؛ لا كتابة خارج by-hussein.
        الخوارزم: HOKOM_TREE_SHA = sha256 لنصّ القائمة المرتّبة «<مسار نسبي>\\t<sha256 المحتوى>\\n» ؛ باستثناء .git/ (مُعلَن)."""
        import hashlib as _h
        hk = Path('/Users/husseinhiyassat/hokom')
        def tree_sha():
            lines = []
            for p in sorted(hk.rglob('*')):
                if p.is_file() and '/.git/' not in str(p):
                    try: hh = _h.sha256(p.read_bytes()).hexdigest()
                    except Exception as e: self.fail(f'HOKOM_FILE_UNREADABLE:{p}:{e}')  # يفشل باسم الملف ، لا يتجاوزه
                    lines.append(f'{p.relative_to(hk)}\t{hh}\n')
            return _h.sha256(''.join(sorted(lines)).encode()).hexdigest()
        before = tree_sha()
        self.rec('ذَهَبَ الْوَلَدُ', lean=False, use_hokom=not self._hokom_ok())
        after = tree_sha()
        self.assertEqual(before, after, 'HOKOM_TREE_CHANGED (sha256 المحتوى)')
        m = subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain', '--untracked-files=all'], capture_output=True, text=True).stdout
        outside = [l for l in m.splitlines() if not (l[3:].startswith('by-hussein/') or l[3:] in ('audit.txt', 'build.log', 'jumla_kamila.json'))]
        self.assertEqual(outside, [], outside)

    def test_T23_pending_not_in_lean(self):
        """T23 مودَع PENDING لا يدخل ، والكلمة تبقى NO_SEALED_MADLUL"""
        r = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False, mudaat_path=self.FX / 'mudaat_pending.json')
        self.assertIsNone(r['maani'][1]); self.assertIsNone(r['plan'])   # الطالب PENDING ⇒ لا إطار

    def test_T24_haqiqa_collision_rejected(self):
        """T24 haqiqa مصادِمة → MUDAA_HAQIQA_COLLISION ورفض الإدخال"""
        t = Tabaqat4(ROOT, out_dir=TMP / 't24', mudaat_path=self.FX / 'mudaat_collision.json')
        self.assertTrue(any('MUDAA_HAQIQA_COLLISION' in x for x in t.mudaat_residuals), t.mudaat_residuals)

    def test_T25_itar_unmapped(self):
        """T25 نمطٌ لا في itar_map (اسمان مرفوعان) → ITAR_UNMAPPED باسم النمط المقروء"""
        r = self.rec('الطَّالِبُ الدَّرْسُ', lean=False, mudaat_path=self.FX / 'mudaat_2noun.json')
        s5 = [s for s in r['stages'] if s['stage'] == 'S5_MAAN_ITAR'][0]
        self.assertIn('ITAR_UNMAPPED', s5['reason']); self.assertIsNone(r['plan'])

    def test_T26_taaqol_source_and_conflict(self):
        """T26 --taaqol: المصدر TAAQOL_P8 معلَن ؛ ومع Hokom متعارض → ITAR_SOURCE_CONFLICT والمُعتمَد Hokom"""
        r = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False, mudaat_path=self.FX / 'mudaat_test.json', taaqol_path=self.FX / 'taaqol_c02.json')
        self.assertIn('TAAQOL_P8', r['plan']['itar_source'])
        if not self._hokom_ok():
            c = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False, use_hokom=True,
                         mudaat_path=self.FX / 'mudaat_test.json', taaqol_path=self.FX / 'taaqol_conflict.json')
            self.assertIsNotNone(c['plan']['itar_conflict']); self.assertIn('ITAR_SOURCE_CONFLICT', c['plan']['itar_conflict'])
            self.assertEqual(c['plan']['ud'], 'Jisr.Mulhaqat.daraba')   # Hokom (fiil) غلب

    def test_T27_determinism_with_mudaat(self):
        """T27 تشغيلان لنفس الجملة والمودَعات → JSON متطابق خارج الطابع الزمني والمجلّد"""
        a = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False, mudaat_path=self.FX / 'mudaat_test.json')
        b = self.rec('كَتَبَ الطَّالِبُ الدَّرْسَ', lean=False, mudaat_path=self.FX / 'mudaat_test.json')
        for r in (a, b): r.pop('timestamp_utc'); r.pop('run_dir'); r['identity'].pop('mashru_status_porcelain', None)
        self.assertEqual(json.dumps(a, ensure_ascii=False, sort_keys=True), json.dumps(b, ensure_ascii=False, sort_keys=True))


class Reporter(unittest.TextTestResult):
    def addSuccess(self, t): super().addSuccess(t); RESULTS[t._testMethodName] = 'PASS'
    def addFailure(self, t, e): super().addFailure(t, e); RESULTS[t._testMethodName] = 'FAIL'
    def addError(self, t, e): super().addError(t, e); RESULTS[t._testMethodName] = 'ERROR'
    def addSkip(self, t, r): super().addSkip(t, r); RESULTS[t._testMethodName] = r


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2, resultclass=Reporter)
    res = runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print('\n```')
    print(f'LEAN_AVAILABLE = {"YES" if not LEAN_REASON else "NO (" + LEAN_REASON + ")"}')
    for k in sorted(RESULTS): print(f'{k:36s} = {RESULTS[k]}')
    ran = [k for k, v in RESULTS.items() if v in ('PASS', 'FAIL', 'ERROR')]
    print(f'TABAQAT4_SCOPE_TESTS_PASS = {"YES" if all(RESULTS[k] == "PASS" for k in ran) else "NO"} ({sum(RESULTS[k]=="PASS" for k in ran)}/{len(ran)} ran ؛ {len(RESULTS)-len(ran)} NOT_RUN)')
    print('```')
    shutil.rmtree(TMP, ignore_errors=True)
    sys.exit(0 if res.wasSuccessful() else 1)
