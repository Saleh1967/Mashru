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
        t = Tabaqat4(ROOT, out_dir=TMP / sha256_text(text)[:8], run_lean=lean and not LEAN_REASON, **kw)
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
