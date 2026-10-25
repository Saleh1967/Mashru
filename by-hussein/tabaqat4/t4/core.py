# -*- coding: utf-8 -*-
"""المراحل S0–S8: جملة ← سجلّ الطبقات الأربع. Mashru يُقرأ ولا يُمَسّ.

الأسئلة السبعة لكل مرحلة (أمر المالك R26 §7): started / completed / found / produced / accepted / stored / consumed.
"""
from __future__ import annotations
import hashlib, json, os, re, subprocess, unicodedata, datetime
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from .dal import load_hawamil, tokenize, encode_word, KalimaDal
from .qari import run_qari, parse_qari, reconcile

HERE = Path(__file__).resolve().parent
TOOL_ROOT = HERE.parent

WASM = ['مبرهن', 'مبرهن على الشاهد', 'مطابَق', 'مفحوص', 'مقيس', 'تقدير', 'رأي']   # سلّم Mashru ، بترتيبه ، لا يُعاد تسميته
AXIOMS_OK = {'propext', 'Classical.choice', 'Quot.sound'}


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def stage(name: str) -> Dict[str, Any]:
    return {'stage': name, 'started': False, 'completed': None, 'found': None, 'produced': None,
            'accepted': None, 'stored': None, 'consumed_by_next': None, 'reason': None, 'residuals': []}


@dataclass
class Claim:
    """ادّعاءٌ واحد بقيمته ورتبته وبرهانه."""
    tabaqa: int
    ism: str                    # اسم الادّعاء (اسم النظرية إن بُرهن)
    qima: Any                   # القيمة
    tarjama: str                # عربية مفهومة
    rutba: Optional[str]        # من WASM أو None
    burhan: Optional[str] = None   # نتيجة lean / #print axioms
    sabab_ghiyab: Optional[str] = None
    def to_dict(self): return asdict(self)


class Tabaqat4:
    def __init__(self, mashru_root: Path, out_dir: Optional[Path] = None, use_hokom: bool = False,
                 run_lean: bool = True, mirsat_an: int = 0, arad_izaha: int = -1, forms: Optional[Dict[str, str]] = None):
        self.mashru_root = Path(mashru_root).resolve()
        self.forms = forms or {}          # صيغ باب الجزاء المعلَنة من المالك: shart=, jawab=, lam=
        self.out_dir = out_dir
        self.use_hokom = use_hokom
        self.run_lean = run_lean
        self.mirsat_an = mirsat_an
        self.arad_izaha = arad_izaha
        self.qamus = json.loads((HERE / 'qamus.json').read_text(encoding='utf-8'))
        self.forms_map = json.loads((HERE / 'forms_map.json').read_text(encoding='utf-8')).get('map', {})
        self.hokom = None                 # مخرج S3 (تقدير) ؛ يُعرَض ولا يُستهلك إلّا لاشتقاق صورة باب الجزاء بوسمها «تقدير»
        self.stages: List[Dict[str, Any]] = []
        self.claims: List[Claim] = []
        self.la_yuddaa: List[str] = [
            'لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.',
            'المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.',
            'أنواع الجمل المنفَّذة في هذه الأداة: [فعل ماضٍ + فاعل معرَّف بأل] و [فعل ماضٍ + فاعل منوَّن] فقط ؛ ما عداها OUT_OF_EXECUTED_PATH.',
            'المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.',
            'الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.',
            'رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.',
        ]

    # ---------------------------------------------------------------- S0..S2
    def _s0(self, text: str) -> Dict[str, Any]:
        st = stage('S0_HAWIYYA'); st['started'] = True
        nfc = unicodedata.normalize('NFC', text)
        st['found'] = True; st['produced'] = True; st['completed'] = True; st['accepted'] = True; st['stored'] = True
        rec = {'nass_kama_wasal': text, 'nfc': nfc, 'nfc_eq_input': nfc == text, 'sha256': sha256_text(nfc),
               'codepoints': len(nfc), 'tahwil': [] if nfc == text else ['NFC_APPLIED']}
        if not re.search(r'[ً-ْ]', nfc):
            st['accepted'] = False; st['reason'] = 'NASS_GHAYR_MASHKUL: Mashru دالُّه خلايا بحركاتها ؛ لا تطبيع صامت ولا تشكيل آلي'
        self.stages.append(st); return rec

    def _s1(self, nfc: str) -> List[Dict[str, Any]]:
        st = stage('S1_TAQTI'); st['started'] = True
        punct = '.،؛:!؟«»()'
        words, dropped = [], []
        for w in tokenize(nfc):
            w2 = w.strip(punct)
            if w2 != w: dropped.append(w.replace(w2, ''))
            if w2: words.append(w2)
        sha8 = sha256_text(nfc)[:8]
        toks = [{'idx': i, 'anchor': f'W-{sha8}-{i:03d}', 'surface': w} for i, w in enumerate(words)]
        st.update(completed=True, found=bool(toks), produced=True, accepted=True, stored=True, consumed_by_next=True)
        if dropped: st['residuals'].append('PUNCT_DROPPED_DECLARED:' + ''.join(dropped))
        self.stages.append(st); return toks

    def _s2(self, toks: List[Dict[str, Any]]) -> List[KalimaDal]:
        st = stage('S2_DAL'); st['started'] = True
        try:
            hawamil = load_hawamil(self.mashru_root)
        except Exception as e:
            st['completed'] = False; st['reason'] = str(e); self.stages.append(st); return []
        out = []
        for t in toks:
            k = encode_word(t['surface'], hawamil)
            out.append(k)
            for r in k.residuals: st['residuals'].append(f"{t['anchor']}:{r}")
            self.claims.append(Claim(1, f"dal_{t['anchor']}", k.khalaya,
                                     f"«{t['surface']}»: {len(k.khalaya)} خلية [{', '.join(k.cells_human)}]"
                                     + (' ، بأل التعريف (همزة وصل)' if k.al else ''),
                                     'مطابَق' if k.ok else None,
                                     burhan='ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7',
                                     sabab_ghiyab=None if k.ok else ';'.join(k.residuals)))
        st.update(completed=True, found=True, produced=True, accepted=all(k.ok for k in out), stored=True,
                  consumed_by_next=all(k.ok for k in out))
        st['hawamil_source'] = 'Dal/Makharij.lean:def hawamil (قُرئ وقت التشغيل ، 29 حاملًا)'
        # الشاهد الثاني: قارئ Mashru نفسه (Qari/Main.lean) على الجملة كلّها
        self.qari = None
        q = run_qari(self.mashru_root, [t['surface'] for t in toks])
        st['qari'] = {'cmd': q['cmd'], 'rc': q['rc']}
        if q['rc'] != 0:
            st['qari']['reason'] = (q['stderr'] or q['stdout'])[:300] or 'QARI_FAILED'
            st['residuals'].append('QARI_WITNESS_ABSENT: ' + st['qari']['reason'].splitlines()[0][:120])
        else:
            self.qari = parse_qari(q['stdout'], [t['surface'] for t in toks])
            for u in self.qari['unparsed']: st['residuals'].append('QARI_UNPARSED: ' + u)
            for i, (t, k) in enumerate(zip(toks, out)):
                qw = self.qari['words'][i] if i < len(self.qari['words']) else {}
                if not k.ok:
                    rec = {'state': 'QARI_ONLY' if qw.get('khalaya') else 'BOTH_REJECTED', 'qari': qw.get('khalaya'), 'reason': ' ؛ '.join(qw.get('notes', [])) or qw.get('rejected')}
                else:
                    rec = reconcile(k.khalaya, k.al, k.wasl, qw, i == len(toks) - 1)
                k.transforms.append('QARI_WITNESS:' + rec['state'])
                setattr(k, 'qari', {'khalaya': qw.get('khalaya'), 'notes': qw.get('notes', []), 'rejected': qw.get('rejected'), 'reconcile': rec})
                if rec['state'] == 'DISAGREE':
                    st['residuals'].append(f"{t['anchor']}:QARI_DISAGREE:{rec.get('reason')}")
                    self.claims.append(Claim(1, f"qari_{t['anchor']}", qw.get('khalaya'), f"قارئ Mashru يقرأ «{t['surface']}» = {qw.get('khalaya')} ≠ الجدول {k.khalaya} — {rec.get('reason')}", 'مفحوص',
                                             burhan='مخرج qari (تنفيذ Mashru) ؛ الاختلاف يُعرَض ولا يُحسَم'))
                elif rec['state'] == 'QARI_ONLY':
                    self.claims.append(Claim(1, f"qari_{t['anchor']}", qw.get('khalaya'), f"قارئ Mashru يقرأ «{t['surface']}» = {qw.get('khalaya')} حيث رفضها الجدول ({';'.join(k.residuals)}) — {rec.get('reason')}", 'مفحوص',
                                             burhan='مخرج qari بقراراته المودَعة (قطر الندى/الألفية كما يذكرها)'))
            if self.qari.get('jumla') and self.qari['jumla'].get('qanun'):
                self.claims.append(Claim(1, 'qari_jumla', self.qari['jumla']['silsila'], f"الجملة في الوصل عند قارئ Mashru: {self.qari['jumla']['qanun']} ؛ السلسلة {self.qari['jumla']['silsila']}", 'مفحوص',
                                         burhan='آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)'))
        self.stages.append(st); return out

    # ---------------------------------------------------------------- S3 Hokom (تقدير)
    def _s3(self, toks):
        st = stage('S3_HOKOM_TAQDIR'); st['started'] = self.use_hokom
        if not self.use_hokom:
            st['reason'] = 'NOT_REQUESTED (--hokom غير مطلوب)'; self.stages.append(st); return None
        adapter = TOOL_ROOT / 'hokom_adapter.py'
        if not adapter.exists():
            st['completed'] = False
            st['reason'] = ('HOKOM_ADAPTER_ABSENT: ضع by-hussein/tabaqat4/hokom_adapter.py يعرّف '
                            'def taqdir(surfaces: list[str]) -> list[dict] يقرأ Hokom بالـpin قراءةً فقط ؛ '
                            'المخرج يُعرَض برتبة «تقدير» ولا يُستهلك')
            self.stages.append(st); return None
        import importlib.util
        spec = importlib.util.spec_from_file_location('hokom_adapter', adapter)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        try:
            res = mod.taqdir([t['surface'] for t in toks])
            st.update(completed=True, found=True, produced=True, accepted=True, stored=True, consumed_by_next=False)
            st['reason'] = 'رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7'
            for t, r in zip(toks, res):
                self.claims.append(Claim(0, f"hokom_{t['anchor']}", r, f"تقدير Hokom لـ«{t['surface']}»: {r}", 'تقدير',
                                         burhan=f"pin={r.get('pin','?')}"))
        except Exception as e:
            st['completed'] = False; st['reason'] = f'HOKOM_ADAPTER_FAILED:{e}'; res = None
        self.stages.append(st); return res

    # ---------------------------------------------------------------- S4 المدلول
    def _s4(self, toks):
        st = stage('S4_MADLUL'); st['started'] = True
        found = []
        for i, t in enumerate(toks):
            qw = (self.qari['words'][i] if getattr(self, 'qari', None) and i < len(self.qari['words']) else {}) or {}
            if qw:
                ents = qw.get('makhzan_entries') or []
                if ents:
                    self.claims.append(Claim(2, f"makhzan_{t['anchor']}", [e_['qawl'] for e_ in ents],
                                             f"المخزن (Mashru) باللفظ «{qw.get('makhzan_lookup')}»: {len(ents)} قول ؛ الأوّل: {ents[0]['qawl']} — سند {ents[0].get('sanad')}",
                                             'تقدير', burhan='وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي'))
                elif qw.get('makhzan_lookup'):
                    self.claims.append(Claim(2, f"makhzan_{t['anchor']}", None, f"المخزن باللفظ «{qw.get('makhzan_lookup')}»: لا مدخل — لا حكم (الغياب ليس امتناعًا)", None,
                                             sabab_ghiyab='MAKHZAN_NO_ENTRY'))
                if qw.get('root'):
                    self.claims.append(Claim(2, f"jidhr_{t['anchor']}", qw['root'], f"مرشَّح الجذر عند قارئ Mashru: «{qw['root']}» (مرشَّح لا هويّة ؛ المزيد والأدوات لا تُميَّز بعد)", 'مقيس',
                                             burhan='qari: fakk_ramz على ثلاث خانات حواملها سالمة — نطاق معلَن'))
            e = self.qamus['kalimat'].get(t['surface'])
            if not e:
                found.append(None)
                st['residuals'].append(f"{t['anchor']}:NO_SEALED_MADLUL")
                self.claims.append(Claim(2, f"madlul_{t['anchor']}", None,
                                         f"«{t['surface']}»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد)", None,
                                         sabab_ghiyab='NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به)'))
                continue
            m = dict(self.qamus['madlulat'][e['madlul']]); m['ism'] = e['madlul']; m['shahid'] = e.get('shahid')
            found.append(m)
            res = [] if m.get('mudaa') else ['MADLUL_SOURCE_UNDECLARED_IN_MASHRU']
            self.claims.append(Claim(2, f"madlul_{t['anchor']}", m['ism'],
                                     f"«{t['surface']}» ↔ مدلول Mashru `{m['ism']}` ({m['wasf']}) — {m['ref']}"
                                     + (f" ؛ مودَع: {m['mudaa']['ism']} {m['mudaa']['sha256'][:12]}… {m['mudaa'].get('mawdi','')}" if m.get('mudaa') else ' ؛ بلا مودَع معجمي معلَن'),
                                     'مطابَق', burhan='مطابقة اسمية بين السطح وتعريف Mashru ؛ حقوله تُبرهَن في S7',
                                     sabab_ghiyab=None))
            for r in res: st['residuals'].append(f"{t['anchor']}:{r}")
        st.update(completed=True, found=any(found), produced=True, accepted=all(found), stored=True,
                  consumed_by_next=all(found))
        if not all(found):
            is_jaza = bool(toks) and self._strip(toks[0]['surface']) in self.ADAWAT_JAZA
            st['reason'] = ('لا مدلول بنيويّ لكلمة أو أكثر ؛ لا يمنع باب الجزاء (S5-ج يحكم على صورة الجملة لا على المدلول)'
                            if is_jaza else 'كلمة أو أكثر بلا مدلول ← المسار الإسناديّ (S5) لا يُبنى')
        self.stages.append(st); return found

    # ---------------------------------------------------------------- S5 معًا (النوع والإطار)
    def _s5(self, toks, dal: List[KalimaDal], maani):
        st = stage('S5_MAAN_ITAR'); st['started'] = True
        plan = None
        n = len(toks)
        jaza = self._s5_jaza(toks, dal, st)
        if jaza is not None:
            self.stages.append(st); return jaza
        if not maani or not all(maani) or not all(k.ok for k in dal):
            st['completed'] = True; st['found'] = False; st['produced'] = False
            # تقدير النوع من السطح وحده (لا من مدلول) كي يُعلَن الخروج عن المسار باسمه
            if dal and (dal[0].al or dal[0].tanwin):
                st['reason'] = 'OUT_OF_EXECUTED_PATH:جملة اسمية (تقديرًا من السطح: أوّلها اسمٌ بأل أو تنوين) + PREREQ_MISSING: مدلولٌ أو خلايا ناقصة'
                st['residuals'].append('OUT_OF_EXECUTED_PATH')
            elif n != 2:
                st['reason'] = f'OUT_OF_EXECUTED_PATH:جملة من {n} كلمات (المغلَّف: كلمتان) + PREREQ_MISSING: مدلولٌ أو خلايا ناقصة'
                st['residuals'].append('OUT_OF_EXECUTED_PATH')
            else:
                st['reason'] = 'PREREQ_MISSING: مدلولٌ أو خلايا ناقصة ؛ نوع الجملة لم يُقدَّر'
            self.stages.append(st); return None
        q0 = maani[0]['qism']
        if n == 2 and q0 == 'fiil' and maani[1]['qism'] == 'ism' and dal[1].al:
            plan = {'naw': 'فعل ماضٍ + فاعل معرَّف بأل', 'ud': 'Jisr.Mulhaqat.darabaZayd', 'shahid_mashru': 'dhahabaAlWalad (Jisr/Utur.lean:914)'}
        elif n == 2 and q0 == 'fiil' and maani[1]['qism'] == 'ism' and dal[1].tanwin:
            plan = {'naw': 'فعل ماضٍ + فاعل منوَّن', 'ud': 'Jisr.Mulhaqat.jaaRajul', 'shahid_mashru': 'dhahabaWaladun (Jisr/Utur.lean:918)'}
        else:
            guess = 'جملة اسمية' if q0 == 'ism' else ('شبه جملة' if q0 == 'harf' else f'فعلية من {n} كلمات')
            st['completed'] = True; st['found'] = False; st['produced'] = False
            st['reason'] = f'OUT_OF_EXECUTED_PATH:{guess} — ليس من النوعَين المغلَّفَين ؛ إطار Mashru له (إن وُجد) لم يُغلَّف'
            st['residuals'].append('OUT_OF_EXECUTED_PATH'); self.stages.append(st); return None
        plan['isnad'] = {'mawdu': maani[1]['ism'], 'mahmul': f".qabiliyya {maani[0]['haqiqa']}", 'nisba': '.isnadiyya',
                         'qaida': 'ISNAD_RULE_FIIL_FAIL (موروثة من الشاهد): الفاعل موضوعٌ ، والفعل قابليّةٌ بحقيقته'}
        st.update(completed=True, found=True, produced=True, accepted=True, stored=True, consumed_by_next=True)
        self.claims.append(Claim(3, 'naw_jumla', plan['naw'], f"نوع الجملة: {plan['naw']} ← إطار {plan['ud']} (شاهد Mashru: {plan['shahid_mashru']})",
                                 'مقيس', burhan='اختيار الإطار بشروط سطحية (قسم المدلول الأوّل ، أل/تنوين الثاني) — حكمه يُبرهَن في S7'))
        self.stages.append(st); return plan


    # ---------------------------------------------------------------- S5-ج باب الجزاء (Jisr/BabJaza.lean ، PR #80)
    ADAWAT_JAZA = ["من", "ما", "أيهم", "أي", "متى", "أين", "أنى", "حيثما", "إن", "إذما", "مهما", "إما", "أينما", "أياما",
                   "حيث", "إذ", "كيف", "إذا", "لو", "كلما", "أيان", "كيفما", "حينما"]   # = adawatJaza + ما يحكم فيه sinfOf بـ«لا حكم» ؛ قائمة حاصرة
    SHART_FORMS = ("mudariMajzum", "mudariMarfu", "madi")
    JAWAB_FORMS = ("mudariMajzum", "mudariMarfu", "madi", "faIsmiyya", "faMudariMarfu", "faMudariMajzum", "faGhayr",
                   "idhaIsmiyya", "faIdha", "ismiyya", "waw", "thumma", "lamQasam")

    @staticmethod
    def _strip(w: str) -> str:
        return re.sub(r'[\u064b-\u0652\u0670]', '', w)

    def _s5_jaza(self, toks, dal, st):
        """يعود بخطّة باب الجزاء إن كانت الكلمة الأولى أداةَ جزاء ؛ وإلّا None (لا يمسّ st)."""
        if not toks: return None
        adat = self._strip(toks[0]['surface'])
        if adat not in self.ADAWAT_JAZA: return None
        n = len(toks)
        base = {'naw': 'جملة شرطية (باب الجزاء)', 'adat': adat, 'tartib': '.shartAwwalan',
                'shahid_mashru': 'Jisr/BabJaza.lean hukm ؛ الضابط المجمَّد BabJazaDawabit (39 حالة)'}
        if n != 3:
            st['completed'] = True; st['found'] = True; st['produced'] = False
            st['reason'] = f'OUT_OF_EXECUTED_PATH:جملة شرطية من {n} كلمات (المغلَّف: أداة + فعل الشرط + الجواب = 3) — الأداة «{adat}» معروفة لـ BabJaza'
            st['residuals'].append('OUT_OF_EXECUTED_PATH'); return {'blocked': True, **base}
        own_sh, own_jw = self.forms.get('shart'), self.forms.get('jawab')
        lam = self.forms.get('lam', 'false')
        hok_sh, hok_jw, hok_res = self._forms_from_hokom(toks)
        # المالك يغلب عند الحضور ؛ وإلّا تقدير Hokom ؛ وإلّا لا شيء
        sh = own_sh or hok_sh
        jw = own_jw or hok_jw
        src, rank = [], 'رأي'
        if own_sh or own_jw: src.append('OWNER_DECLARED_FORMS (--forms)')
        used_hokom = (not own_sh and hok_sh) or (not own_jw and hok_jw)
        if used_hokom: src.append('HOKOM_TAQDIR'); rank = 'تقدير' if not (own_sh or own_jw) else 'رأي+تقدير'
        conflict = None
        if own_sh and hok_sh and own_sh != hok_sh or own_jw and hok_jw and own_jw != hok_jw:
            conflict = (f"FORMS_CONFLICT_OWNER_VS_HOKOM: المالك (شرط={own_sh} ، جواب={own_jw}) ≠ "
                        f"Hokom (شرط={hok_sh} ، جواب={hok_jw}) ؛ المعتمَد: صيغة المالك")
        unmapped = [r for r in hok_res if r.startswith('FORMS_UNMAPPED')]
        if (sh is None or jw is None) and unmapped and not (own_sh and own_jw):
            st['completed'] = True; st['found'] = True; st['produced'] = False
            st['reason'] = 'FORMS_UNMAPPED من تقدير Hokom: ' + ' ؛ '.join(unmapped) + ' — أضِفه إلى forms_map.json أو أعلِن --forms'
            st['residuals'].append('FORMS_UNMAPPED'); return {'blocked': True, **base}
        if sh not in self.SHART_FORMS or jw not in self.JAWAB_FORMS or lam not in ('true', 'false'):
            st['completed'] = True; st['found'] = True; st['produced'] = False
            st['reason'] = ('JAZA_FORMS_UNDECLARED: BabJaza.Jumla يحتاج صورةَ فعل الشرط والجواب «كما كُتبت» ؛ أعلِنها '
                            '--forms shart=<' + '|'.join(self.SHART_FORMS) + '> jawab=<' + '|'.join(self.JAWAB_FORMS) + '> [lam=true]'
                            + (' أو شغّل --hokom لتقديرها' if not self.use_hokom else ''))
            st['residuals'].append('JAZA_FORMS_UNDECLARED'); return {'blocked': True, **base}
        plan = {**base, 'shart': '.' + sh, 'jawab': '.' + jw, 'lamQasam': lam, 'kind': 'jaza',
                'premise_rank': rank, 'premise_source': ' + '.join(src) or 'OWNER_DECLARED_FORMS (--forms)',
                'forms_conflict': conflict}
        st.update(completed=True, found=True, produced=True, accepted=True, stored=True, consumed_by_next=True)
        st['residuals'].append('FORMS_SOURCE:' + (' + '.join(src) or 'OWNER'))
        if used_hokom: st['residuals'].append('FORMS_FROM_HOKOM_TAQDIR: صورتا الفعلَين تقديرٌ من Hokom (لا يُستهلَك إلّا هنا مقعدًا معلَنًا) ؛ la_yuddaa')
        if conflict: st['residuals'].append(conflict)
        self.claims.append(Claim(3, 'naw_jumla', plan['naw'],
                                 f"نوع الجملة: شرطية ، الأداة «{adat}» ، الشرط أوّلًا ؛ الصيغتان: شرط={sh} ، جواب={jw} ، لام القسم={lam}"
                                 + (f" ({conflict})" if conflict else ''),
                                 'مقيس', burhan=f"الأداة من قائمة BabJaza الحاصرة (مقيس) ؛ مصدر الصيغتين: {' + '.join(src) or 'OWNER'} (رتبتها {rank}) ؛ الحكم يُبرهَن في S7 مشروطًا بهما"))
        return plan

    def _forms_from_hokom(self, toks):
        """صورتا الشرط (توكن 1) والجواب (توكن 2) من تقدير Hokom عبر forms_map.json ؛ أو (None, None, [أسباب])."""
        if not (self.use_hokom and self.hokom and len(self.hokom) >= 3):
            return None, None, ['HOKOM_NOT_AVAILABLE_FOR_FORMS']
        def form_of(idx):
            r = self.hokom[idx] if idx < len(self.hokom) else {}
            sub = r.get('word_class_subclass') or ''; mood = r.get('mood')
            keys = ([f"{sub}+{mood}"] if mood and mood != 'NOT_APPLICABLE' else []) + [sub]
            for k in keys:
                if k in self.forms_map: return self.forms_map[k], None
            return None, f"FORMS_UNMAPPED:{sub}+{mood}"
        sh, e1 = form_of(1); jw, e2 = form_of(2)
        return sh, jw, [x for x in (e1, e2) if x]

    # ---------------------------------------------------------------- S6/S7 Lean
    def _lean_file(self, toks, dal, maani, plan, pass_no: int, observed: Optional[Dict[str, str]] = None) -> str:
        v, s = maani[0], maani[1]
        kal = ', '.join(f"⟨{k.khalaya}, {str(k.wasl).lower()}, {str(k.al).lower()}⟩" for k in dal)
        an, iz = self.mirsat_an, self.arad_izaha
        L = []
        L.append(f"/- Tabaqat4 — مولَّد آليًّا لـ «{' '.join(t['surface'] for t in toks)}» ؛ قالب Shahid_Ahmad.lean ؛ pass {pass_no}. Mashru يُستورَد ولا يُعدَّل. -/")
        L.append("import Jisr.Utur\nimport Aql.Isnad\n\nnamespace Tabaqat4\nopen Jisr.Utur Aql.Isnad Aql.Mirsat Aql.Azmina Aql.Makan\n")
        L.append(f"def jumla3 : Itar3 :=\n  {{ jisr := {{ ud := {plan['ud']} }}, kalimat := [{kal}], maani := [{v['ism']}, {s['ism']}],\n    isnad := ⟨{s['ism']}, .qabiliyya {v['haqiqa']}, .isnadiyya⟩ }}\n")
        L.append(f"def mirsat : Mirsat := ⟨{an}, ⟨0, 0, 0⟩⟩")
        L.append(f"def dhat : Dhat := ⟨{s['haqiqa']}, none⟩")
        L.append(f"def arad : Arad := .fiil {v['haqiqa']} ({iz}) .saa none")
        L.append("def jumla4 : Jumla := .sughra dhat arad\n")
        if pass_no == 1:
            L.append('#eval hukm3 jumla3')
            L.append('#eval ibtida3 jumla3')
            L.append('#eval (Dal.rakkib jumla3.kalimat).silsila')
            L.append('#eval (ajza jumla4).map rutba')
            L.append('#eval yastaghni jumla4')
            L.append('#eval zamanArad mirsat arad')
            L.append('#eval mawdiInda mirsat jumla4')
        else:
            o = observed
            L.append(f"theorem tabaqa1_kalimat : jumla3.kalimat = [{kal}] := by decide")
            L.append(f"theorem tabaqa2_maani : jumla3.maani = [{v['ism']}, {s['ism']}] ∧ {v['ism']}.tim = true := by decide")
            L.append(f"theorem tabaqa3_hukm : hukm3 jumla3 = {o['hukm3']} := by decide +kernel")
            L.append(f"theorem tabaqa3_isnad : jumla3.isnad = ⟨{s['ism']}, .qabiliyya {v['haqiqa']}, .isnadiyya⟩ := by decide")
            L.append(f"theorem tabaqa4_ajza : (ajza jumla4).map rutba = {o['ajza']} := by decide")
            L.append(f"theorem tabaqa4_kalam : yastaghni jumla4 = {o['yastaghni']} := by decide")
            L.append(f"theorem tabaqa4_zaman : zamanArad mirsat arad = {o['zaman']} := by decide")
            L.append(f"theorem tabaqa4_mawdi : mawdiInda mirsat jumla4 = {o['mawdi']} := by decide")
            L.append("theorem tabaqa4_thabat : zamanArad ⟨mirsat.an + 5, mirsat.huna⟩ (arad.naql 5) = zamanArad mirsat arad :=\n  thabat_naql_arad mirsat 5 ⟨0, 0, 0⟩ arad")
            for th in ['tabaqa1_kalimat', 'tabaqa2_maani', 'tabaqa3_hukm', 'tabaqa3_isnad', 'tabaqa4_ajza', 'tabaqa4_kalam', 'tabaqa4_zaman', 'tabaqa4_mawdi', 'tabaqa4_thabat']:
                L.append(f'#print axioms Tabaqat4.{th}')
        L.append('\nend Tabaqat4')
        return '\n'.join(L) + '\n'

    def _run_lean(self, lean_path: Path) -> Dict[str, Any]:
        env = dict(os.environ); env['PYTHONDONTWRITEBYTECODE'] = '1'
        import shutil
        lake = shutil.which('lake')
        if not lake:   # elan غير مُحمَّل في الصدفة: ابحث في موضعه المعتاد وأعلن ذلك
            cand = Path.home() / '.elan' / 'bin' / 'lake'
            if cand.exists():
                lake = str(cand); env['PATH'] = str(cand.parent) + os.pathsep + env.get('PATH', '')
        cmd = [lake or 'lake', 'env', 'lean', str(lean_path)]
        try:
            p = subprocess.run(cmd, cwd=str(self.mashru_root), capture_output=True, text=True, timeout=600, env=env)
            return {'cmd': ' '.join(cmd), 'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}
        except FileNotFoundError:
            return {'cmd': ' '.join(cmd), 'rc': None, 'stdout': '', 'stderr': 'LAKE_NOT_FOUND: لا lake في PATH ولا في ~/.elan/bin ؛ شغّل `source ~/.elan/env`'}
        except subprocess.TimeoutExpired:
            return {'cmd': ' '.join(cmd), 'rc': None, 'stdout': '', 'stderr': 'LEAN_TIMEOUT_600S'}

    @staticmethod
    def _parse_eval(stdout: str) -> Optional[Dict[str, str]]:
        lines = [l.strip() for l in stdout.splitlines() if l.strip()]
        if len(lines) < 7: return None
        h = lines[0]
        hukm = '.murakhkhas' if 'murakhkhas' in h else ('.laHukm' if 'laHukm' in h else ('.mumtani' if 'mumtani' in h else None))
        if hukm is None: return None
        ajza = '[' + ', '.join('.' + x for x in re.findall(r'(hakim|mahkum)', lines[3])) + ']'
        zam = lines[5]
        zaman = 'none' if zam.startswith('none') else ('some .' + re.search(r'(madi|hal|mustaqbal)', zam).group(1) if re.search(r'(madi|hal|mustaqbal)', zam) else None)
        mawdi = re.search(r'(\{.*\}|⟨.*⟩|\(.*\))', lines[6])
        nums = re.findall(r'-?\d+', lines[6])
        return {'hukm3': hukm, 'ibtida3': lines[1], 'silsila': lines[2], 'ajza': ajza, 'yastaghni': lines[4],
                'zaman': zaman, 'mawdi': f"⟨{', '.join(nums[:3])}⟩" if len(nums) >= 3 else lines[6]}

    def _lean_jaza(self, plan, pass_no: int, observed=None) -> str:
        L = [f"/- Tabaqat4 — باب الجزاء ؛ مولَّد آليًّا ؛ pass {pass_no}. Mashru يُستورَد ولا يُعدَّل. -/",
             "import Jisr.BabJaza\n\nnamespace Tabaqat4\nopen Jisr.BabJaza\n",
             f"def j : Jumla := ⟨\"{plan['adat']}\", {plan['tartib']}, {plan['lamQasam']}, {plan['shart']}, {plan['jawab']}⟩\n"]
        if pass_no == 1:
            L.append('#eval (hukm j).kalam'); L.append('#eval (hukm j).shir'); L.append('#eval sinfOf j.adat')
        else:
            L.append(f"theorem jaza_hukm : hukm j = ⟨{observed['kalam']}, {observed['shir']}⟩ := by decide")
            L.append(f"theorem jaza_sinf : sinfOf j.adat = {observed['sinf']} := by decide")
            L.append('#print axioms Tabaqat4.jaza_hukm'); L.append('#print axioms Tabaqat4.jaza_sinf')
        L.append('\nend Tabaqat4'); return '\n'.join(L) + '\n'

    def _s7_jaza(self, plan, run_dir: Path):
        st6 = stage('S6_AQL'); st7 = stage('S7_BURHAN')
        st6['reason'] = 'NOT_APPLICABLE: باب الجزاء يحكم على صورة الجملة (كلام/شعر) ولا يبني Itar3 ولا Aql.Jumla ؛ لا طبقة رابعة له في Mashru'
        st6['residuals'].append('AQL_NOT_DEFINED_FOR_JAZA'); self.stages.append(st6)
        st7['started'] = self.run_lean
        if not self.run_lean:
            st7['reason'] = 'NOT_RUN (--no-lean)'; self.stages.append(st7); return None
        run_dir.mkdir(parents=True, exist_ok=True)
        p1 = run_dir / 'Jumla_pass1.lean'; p1.write_text(self._lean_jaza(plan, 1), encoding='utf-8')
        r1 = self._run_lean(p1); (run_dir / 'lean_pass1_stdout.txt').write_text(r1['stdout'] + '\n--- stderr ---\n' + r1['stderr'], encoding='utf-8')
        res = {'pass1': r1, 'pass2': None, 'observed': None, 'theorems': {}, 'files': {'pass1': sha256_file(p1)}, 'kind': 'jaza'}
        if r1['rc'] != 0:
            st7['completed'] = False; st7['reason'] = 'LEAN_PASS1_FAILED: ' + (r1['stderr'] or r1['stdout'])[:400]; self.stages.append(st7); return res
        lines = [l.strip() for l in r1['stdout'].splitlines() if l.strip()]
        def dar(x):
            m = re.search(r'(maqbul|qabih|khata|laHukm)', x); return '.' + m.group(1) if m else None
        def sinf(x):
            m = re.search(r'(jaza|haythuIdh|kayfa|idha|ghayr)', x); return '.' + m.group(1) if m else None
        if len(lines) < 3 or not dar(lines[0]) or not dar(lines[1]) or not sinf(lines[2]):
            st7['completed'] = False; st7['reason'] = 'LEAN_PASS1_UNPARSED'; self.stages.append(st7); return res
        obs = {'kalam': dar(lines[0]), 'shir': dar(lines[1]), 'sinf': sinf(lines[2])}; res['observed'] = obs
        p2 = run_dir / 'Jumla.lean'; p2.write_text(self._lean_jaza(plan, 2, obs), encoding='utf-8')
        r2 = self._run_lean(p2); (run_dir / 'lean_stdout.txt').write_text(r2['stdout'] + '\n--- stderr ---\n' + r2['stderr'], encoding='utf-8')
        res['pass2'] = r2; res['files']['pass2'] = sha256_file(p2)
        ax = {m.group(1): [a.strip() for a in m.group(2).split(',') if a.strip()] for m in re.finditer(r"'Tabaqat4\.(\w+)' depends on axioms: \[(.*?)\]", r2['stdout'])}
        for m in re.finditer(r"'Tabaqat4\.(\w+)' does not depend on any axioms", r2['stdout']): ax[m.group(1)] = []
        ok2 = r2['rc'] == 0
        for nme in ('jaza_hukm', 'jaza_sinf'):
            a = ax.get(nme); res['theorems'][nme] = {'passed': ok2 and a is not None and set(a) <= AXIOMS_OK, 'axioms': a}
        st7.update(completed=True, found=ok2, produced=True, accepted=all(t['passed'] for t in res['theorems'].values()), stored=True)
        if not ok2: st7['reason'] = 'LEAN_PASS2_FAILED: ' + (r2['stderr'] or r2['stdout'])[-600:]
        st7['residuals'].append('CONDITIONAL_ON_SUPPLIED_FORMS: البرهان على الحكم مشروطٌ بصيغتَي الشرط والجواب المعطاتَين')
        self.stages.append(st7)
        DAR = {'.maqbul': 'مقبول', '.qabih': 'قبيح', '.khata': 'خطأ', '.laHukm': 'لا حكم'}
        rk = lambda n: 'مبرهن على الشاهد' if res['theorems'][n]['passed'] else 'مفحوص'
        br = lambda n: f"lean rc={r2['rc']} ؛ axioms={res['theorems'][n]['axioms']} ؛ مشروط بالصيغ المعطاة"
        self.claims.append(Claim(3, 'jaza_sinf', obs['sinf'], f"صنف الأداة «{plan['adat']}» عند سيبويه (sinfOf): {obs['sinf']}", rk('jaza_sinf'), br('jaza_sinf')))
        self.claims.append(Claim(3, 'jaza_hukm', obs, f"حكم باب الجزاء: في الكلام {DAR[obs['kalam']]} ، في الشعر {DAR[obs['shir']]} — على الصيغتَين المعطاتَين", rk('jaza_hukm'), br('jaza_hukm')))
        self.la_yuddaa.append('في باب الجزاء: صورتا فعل الشرط والجواب مُعطاتان من المالك (--forms) لا مقروءتان من السطح ؛ البرهان مشروط بهما ، وقراءة الصورة من السطح تنتظر مُنتِجًا (Hokom) برتبة تقدير.')
        return res

    def _s6_s7(self, toks, dal, maani, plan, run_dir: Path):
        st6 = stage('S6_AQL'); st7 = stage('S7_BURHAN')
        if plan is not None and plan.get('blocked'):
            st6['reason'] = st7['reason'] = 'PREREQ_MISSING (S5 أعلن توقّفًا)'; self.stages += [st6, st7]; return None
        if plan is not None and plan.get('kind') == 'jaza':
            return self._s7_jaza(plan, run_dir)
        if plan is None:
            st6['reason'] = st7['reason'] = 'PREREQ_MISSING (S5 لم يُنتج إطارًا)'; self.stages += [st6, st7]; return None
        st6['started'] = True
        st6.update(completed=True, found=True, produced=True, accepted=True, stored=True, consumed_by_next=True)
        st6['reason'] = f'Mirsat ⟨{self.mirsat_an}, ⟨0,0,0⟩⟩ و Arad .fiil {maani[0]["haqiqa"]} ({self.arad_izaha}) .saa none — افتراضات معلَنة (ت3/ت4/ت5 من الشاهد)'
        st6['residuals'] += ['MIRSAT_DEFAULT_ASSUMED', 'ARAD_IZAHA_DEFAULT_ASSUMED', 'LAZIM_BY_FRAME_NOT_BY_TEXT']
        self.stages.append(st6)
        st7['started'] = self.run_lean
        if not self.run_lean:
            st7['reason'] = 'NOT_RUN (--no-lean)'; self.stages.append(st7); return None
        run_dir.mkdir(parents=True, exist_ok=True)
        p1 = run_dir / 'Jumla_pass1.lean'; p1.write_text(self._lean_file(toks, dal, maani, plan, 1), encoding='utf-8')
        r1 = self._run_lean(p1); (run_dir / 'lean_pass1_stdout.txt').write_text(r1['stdout'] + '\n--- stderr ---\n' + r1['stderr'], encoding='utf-8')
        res = {'pass1': r1, 'pass2': None, 'observed': None, 'theorems': {}, 'files': {'pass1': sha256_file(p1)}}
        if r1['rc'] != 0:
            st7['completed'] = False; st7['reason'] = 'LEAN_PASS1_FAILED: ' + (r1['stderr'] or r1['stdout'])[:400]
            self.stages.append(st7); return res
        obs = self._parse_eval(r1['stdout'])
        res['observed'] = obs
        if not obs:
            st7['completed'] = False; st7['reason'] = 'LEAN_PASS1_UNPARSED'; self.stages.append(st7); return res
        hukm_ar = {'.murakhkhas': 'مرخَّص', '.laHukm': 'لا حكم (غياب شاهد لا امتناع)', '.mumtani': 'ممتنع'}[obs['hukm3']]
        if obs['hukm3'] != '.murakhkhas':
            st7['residuals'].append(f"HUKM3_NOT_MURAKHKHAS:{obs['hukm3']} — الطبقة الرابعة محسوبة على مدلولات الكلمات ، لا على جملة مرخَّصة ؛ لا يُبنى عليها")
            self.la_yuddaa.append(f"هذه الجملة {hukm_ar} في الطبقة الثالثة (hukm3={obs['hukm3']}) ؛ نظريات الطبقة الرابعة صحيحة على مدلولاتها لكنها لا تُقرأ حكمًا على الجملة.")
        p2 = run_dir / 'Jumla.lean'; p2.write_text(self._lean_file(toks, dal, maani, plan, 2, obs), encoding='utf-8')
        r2 = self._run_lean(p2); (run_dir / 'lean_stdout.txt').write_text(r2['stdout'] + '\n--- stderr ---\n' + r2['stderr'], encoding='utf-8')
        res['pass2'] = r2; res['files']['pass2'] = sha256_file(p2)
        # axioms per theorem
        ax = {}
        for m in re.finditer(r"'Tabaqat4\.(\w+)' depends on axioms: \[(.*?)\]", r2['stdout']):
            ax[m.group(1)] = [a.strip() for a in m.group(2).split(',') if a.strip()]
        for m in re.finditer(r"'Tabaqat4\.(\w+)' does not depend on any axioms", r2['stdout']):
            ax[m.group(1)] = []
        ok2 = r2['rc'] == 0
        names = ['tabaqa1_kalimat', 'tabaqa2_maani', 'tabaqa3_hukm', 'tabaqa3_isnad', 'tabaqa4_ajza', 'tabaqa4_kalam', 'tabaqa4_zaman', 'tabaqa4_mawdi', 'tabaqa4_thabat']
        for nme in names:
            a = ax.get(nme)
            passed = ok2 and a is not None and set(a) <= AXIOMS_OK
            res['theorems'][nme] = {'passed': passed, 'axioms': a}
        st7.update(completed=True, found=ok2, produced=True, accepted=all(t['passed'] for t in res['theorems'].values()), stored=True)
        if not ok2: st7['reason'] = 'LEAN_PASS2_FAILED: ' + (r2['stderr'] or r2['stdout'])[-600:]
        self.stages.append(st7)
        # claims
        def rk(nme): return 'مبرهن على الشاهد' if res['theorems'][nme]['passed'] else ('مفحوص' if r1['rc'] == 0 else None)
        def br(nme):
            t = res['theorems'][nme]; return f"lean rc={r2['rc']} ؛ axioms={t['axioms']}" if t['axioms'] is not None else f"lean rc={r2['rc']} ؛ axioms غير ملتقطة"
        self.claims.append(Claim(1, 'tabaqa1_kalimat', [k.khalaya for k in dal], 'خلايا الكلمتَين كما بناها Mashru في الإطار الثلاثي (مطابقة البناء)', rk('tabaqa1_kalimat'), br('tabaqa1_kalimat')))
        self.claims.append(Claim(2, 'tabaqa2_maani', [maani[0]['ism'], maani[1]['ism']], f"المدلولان في الإطار ، و`{maani[0]['ism']}.tim = true` (عَرَضٌ له زمان)", rk('tabaqa2_maani'), br('tabaqa2_maani')))
        self.claims.append(Claim(3, 'tabaqa3_hukm', obs['hukm3'], f"حكم الإطار الثلاثي hukm3 = {hukm_ar} ({obs['hukm3']}) ؛ ibtida3={obs['ibtida3']} ؛ سلسلة الوصل {obs['silsila']}", rk('tabaqa3_hukm'), br('tabaqa3_hukm')))
        self.claims.append(Claim(3, 'tabaqa3_isnad', plan['isnad'], f"الإسناد الدلالي: {maani[1]['ism']} موضوعٌ ، قابليّة {maani[0]['haqiqa']} محمولٌ ، نسبة إسنادية", rk('tabaqa3_isnad'), br('tabaqa3_isnad')))
        self.claims.append(Claim(4, 'tabaqa4_ajza', obs['ajza'], f"أجزاء الجملة الصغرى بالرتبة: {obs['ajza']} (محكوم ثمّ حاكم)", rk('tabaqa4_ajza'), br('tabaqa4_ajza')))
        self.claims.append(Claim(4, 'tabaqa4_kalam', obs['yastaghni'], f"كلامٌ يُستغنى به بالسكوت: {obs['yastaghni']}", rk('tabaqa4_kalam'), br('tabaqa4_kalam')))
        self.claims.append(Claim(4, 'tabaqa4_zaman', obs['zaman'], f"زمن الحدث عند المرساة: {obs['zaman']} (بإزاحة {self.arad_izaha} ساعة معلَنة)", rk('tabaqa4_zaman'), br('tabaqa4_zaman')))
        self.claims.append(Claim(4, 'tabaqa4_mawdi', obs['mawdi'], f"موضع الجملة نسبةً إلى «هنا»: {obs['mawdi']}", rk('tabaqa4_mawdi'), br('tabaqa4_mawdi')))
        self.claims.append(Claim(4, 'tabaqa4_thabat', True, 'نقل المرساة والحدث معًا بساعة لا يغيّر الزمن (thabat_naql_arad)', 'مبرهن' if res['theorems']['tabaqa4_thabat']['passed'] else None, br('tabaqa4_thabat'),
                                 sabab_ghiyab=None if res['theorems']['tabaqa4_thabat']['passed'] else 'نظرية عامّة من Mashru لم تُطبَّق هنا'))
        return res

    # ---------------------------------------------------------------- تشغيل كامل
    def run(self, text: str) -> Dict[str, Any]:
        t0 = datetime.datetime.now(datetime.timezone.utc).isoformat()
        s0 = self._s0(text)
        sha8 = s0['sha256'][:8]
        run_dir = (self.out_dir or (TOOL_ROOT / '_runs' / sha8))
        toks = dal = maani = plan = lean = None
        if self.stages[-1]['accepted']:
            toks = self._s1(s0['nfc'])
            dal = self._s2(toks)
            self.hokom = self._s3(toks)
            maani = self._s4(toks)
            plan = self._s5(toks, dal, maani)
            lean = self._s6_s7(toks, dal, maani, plan, run_dir)
        # S8 الوسم: ملخّص الرتب
        wasm_summary = {w: sum(1 for c in self.claims if c.rutba == w) for w in WASM}
        wasm_summary['بلا رتبة'] = sum(1 for c in self.claims if c.rutba is None)
        tabaqat_state = {}
        for tb in (1, 2, 3, 4):
            cs = [c for c in self.claims if c.tabaqa == tb]
            if tb == 4 and plan and plan.get('kind') == 'jaza': tabaqat_state[tb] = 'NOT_APPLICABLE'; continue
            if not cs: tabaqat_state[tb] = 'NOT_REACHED'
            elif all(c.rutba in ('مبرهن', 'مبرهن على الشاهد') for c in cs if c.ism.startswith(('tabaqa', 'jaza_'))) and any(c.ism.startswith(('tabaqa', 'jaza_')) for c in cs): tabaqat_state[tb] = 'مبرهن على الشاهد'
            elif any(c.rutba is None for c in cs): tabaqat_state[tb] = 'PARTIAL_OR_BLOCKED'
            else: tabaqat_state[tb] = max((c.rutba for c in cs if c.rutba), key=lambda r: -WASM.index(r))
        ident = self._identity()
        rec = {'schema': 'Tabaqat4Record:v1', 'timestamp_utc': t0, 'input': s0, 'tokens': toks,
               'dal': [k.to_dict() for k in dal] if dal else None, 'maani': maani, 'plan': plan,
               'lean': lean, 'stages': self.stages, 'claims': [c.to_dict() for c in self.claims],
               'wasm_summary': wasm_summary, 'tabaqat_state': tabaqat_state, 'hukm3': ((lean.get('observed') or {}).get('hukm3') or (lean.get('observed') or {}).get('kalam')) if lean else None, 'la_yuddaa': self.la_yuddaa, 'identity': ident,
               'run_dir': str(run_dir)}
        return rec

    def _identity(self) -> Dict[str, Any]:
        def git(*a):
            try: return subprocess.run(['git', '-C', str(self.mashru_root), *a], capture_output=True, text=True, timeout=30).stdout.strip()
            except Exception as e: return f'GIT_UNAVAILABLE:{e}'
        tool_files = sorted(p for p in TOOL_ROOT.rglob('*') if p.is_file() and '_runs' not in p.parts and '__pycache__' not in p.parts and p.suffix in ('.py', '.json', '.md'))
        return {'mashru_root': str(self.mashru_root), 'mashru_head': git('rev-parse', 'HEAD'),
                'mashru_tree_clean': git('status', '--porcelain') == '', 'mashru_status_porcelain': git('status', '--porcelain')[:2000],
                'lean_toolchain': (self.mashru_root / 'lean-toolchain').read_text(encoding='utf-8').strip() if (self.mashru_root / 'lean-toolchain').exists() else None,
                'qamus_sha256': sha256_file(HERE / 'qamus.json'),
                'tool_files': {str(p.relative_to(TOOL_ROOT)): sha256_file(p) for p in tool_files}}
