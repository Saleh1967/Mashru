# -*- coding: utf-8 -*-
"""hfn_d6.py — محرّك قانون الإيداع بالجملة D6 (أمضاه المالك 2026-10-26).

READ_ONLY على HFN release_v18 و maqayis.db ؛ لا يكتب بايتًا تحتهما. لا كاش ولا بايتكود.
القاعدة الحاكمة: لا رقم ولا معنى يُخترَع ؛ كلُّ حقل يُنسَخ من عمود/صفّ مسمّى أو يبقى فارغًا بسببٍ معلَن.
الأعمدة المستعمَلة مُعلَنة في t4/hfn_map.json بعد قراءة MANIFEST/README.
"""
from __future__ import annotations
import os, csv, json, hashlib, sqlite3, unicodedata
from pathlib import Path

HFN_V18 = Path(os.environ.get("HFN_V18", "/Users/husseinhiyassat/arabic-net/HusseinFrameNet/release/release_v18"))
MAQAYIS = Path(os.environ.get("MAQAYIS_DB", "/Users/husseinhiyassat/arabic-net/Arabic-Mother-language-net/word_tree/maqayis.db"))

# تطبيع الهمزات المعلَن (يوافق t4/dal.py: HAMZA_FORMS و ALIF_MADDA) — لا تطبيع صامت
HAMZA = {'أ': 'ء', 'إ': 'ء', 'ؤ': 'ء', 'ئ': 'ء'}
HARAKAT = set('ًٌٍَُِْ')            # فتحة ضمّة كسرة فتحتان ضمّتان كسرتان سكون
TANWIN_MARKS = set('ًٌٍ')
SHADDA = 'ّ'
STRIP_SILENT = set('ـٰٓ')          # تطويل ، ألف خنجرية ، علامة المدّة (تُزال في المطابقة)

csv.field_size_limit(10 ** 7)


def _nfc(s): return unicodedata.normalize('NFC', s)


def hamza_root(letters):
    """جذر Hokom (قائمة حروف) → سلسلة مطبَّعة الهمزات ، أو None."""
    if not letters:
        return None
    return ''.join(HAMZA.get(c, c) for c in letters)


def _base_units(word):
    """→ [[حرف, [علامات]]] على نقاط الرمز (NFC) ، بإسقاط التطويل والعلامات الصامتة في المطابقة."""
    out = []
    for ch in _nfc(word):
        if ch in STRIP_SILENT:
            continue
        if ch in HARAKAT or ch == SHADDA:
            if out:
                out[-1][1].append(ch)
        else:
            out.append([ch, []])
    return out


def lemma_of(surface):
    """اللِّيمة كما يفعل qari: إسقاط أل والتنوين والحركة الأخيرة (مع فكّ إدغام لام الشمسية) ؛ تبقى الحركات الداخلية.
    يُعاد (lemma_voweled, lemma_norm) حيث lemma_norm مطبَّع الهمزات بلا تطويل/خنجرية/مدّة ؛ تبقى الشدّة والحركات الداخلية."""
    u = _base_units(surface)
    # أل التعريف: ا (بلا حركة) + ل في الأوّل
    if len(u) >= 2 and u[0][0] == 'ا' and not any(m not in (SHADDA,) for m in u[0][1]) and u[1][0] == 'ل' \
            and not any(m in HARAKAT and m not in TANWIN_MARKS for m in u[0][1]):
        # أسقط الألف واللام ؛ وإن كان ما بعدهما شمسيًّا مشدَّدًا فالشدّة لام مدغمة تُحذف
        rest = u[2:]
        if rest and SHADDA in rest[0][1]:
            rest[0][1] = [m for m in rest[0][1] if m != SHADDA]
        u = rest
    # أسقط التنوين دائمًا
    for cu in u:
        cu[1] = [m for m in cu[1] if m not in TANWIN_MARKS]
    # أسقط الحركة الأخيرة (حركة قصيرة أو سكون على آخر حرف)
    if u:
        u[-1][1] = [m for m in u[-1][1] if m == SHADDA]
    voweled = ''.join(c + ''.join(m) for c, m in u)
    norm = ''.join(HAMZA.get(c, c) + ''.join(sorted(ms)) for c, ms in u)   # تبقى الحركات الداخلية والشدّة
    return voweled, norm


def hfn_lemma_norm(lemma):
    """صورة لِيمة HFN للمطابقة: إسقاط الحركة الأخيرة فقط ، تطبيع الهمزات ، حذف التطويل/الخنجرية/المدّة ،
    وإبقاء الحركات الداخلية والشدّة (فتميّز ذَهَبَ فعل عن ذَهِبَ فعل)."""
    u = _base_units(lemma)
    if u:
        u[-1][1] = [m for m in u[-1][1] if m == SHADDA]
    return ''.join(HAMZA.get(c, c) + ''.join(sorted(ms)) for c, ms in u)


class HFN:
    def __init__(self, root=HFN_V18):
        self.root = Path(root)
        self.event_root = {}        # event_id -> root_K
        for r in csv.DictReader(open(self.root / 'events.csv', encoding='utf-8')):
            self.event_root[r['event_id']] = r['root_K']
        # lexical_units: (root_norm, lemma_norm) -> [ (lu_id, lemma, pos_ar, event_id) ]
        self.by_key = {}
        self.by_lemma_pos = {}      # (lemma_norm, pos) -> set(root_norm) : لتمييز ROOT_MISMATCH عن NO_HFN_UNIT
        self.units = []
        for r in csv.DictReader(open(self.root / 'lexical_units.csv', encoding='utf-8')):
            ev = r['event_id']
            rk = self.event_root.get(ev, '')
            rk_norm = ''.join(HAMZA.get(c, c) for c in rk)
            ln = hfn_lemma_norm(r['lemma'])
            rec = dict(lu_id=r['lu_id'], lemma=r['lemma'], pos=r['pos_ar'], event_id=ev, root_K=rk)
            self._index(rk_norm, ln, rec)

    def _index(self, rk_norm, ln, rec):
        self.units.append(rec)
        self.by_key.setdefault((rk_norm, ln), []).append(rec)
        self.by_lemma_pos.setdefault((ln, rec['pos']), set()).add(rk_norm)

    @classmethod
    def from_records(cls, records):
        """بناءٌ من سجلّات في الذاكرة (للاختبارات بمقتطفات صغيرة). كلّ سجلّ: dict(lu_id, lemma, pos, event_id, root_K)."""
        self = cls.__new__(cls)
        self.root = None; self.event_root = {}; self.by_key = {}; self.by_lemma_pos = {}; self.units = []
        for r in records:
            self.event_root[r['event_id']] = r['root_K']
            rk_norm = ''.join(HAMZA.get(c, c) for c in r['root_K'])
            self._index(rk_norm, hfn_lemma_norm(r['lemma']), dict(r))
        return self

    def match(self, root_norm, lemma_norm):
        return list(self.by_key.get((root_norm, lemma_norm), []))

    def lemma_pos_roots(self, lemma_norm, pos):
        return self.by_lemma_pos.get((lemma_norm, pos), set())


MAKHZAN_SHA = '936c68e0c2c6'   # بصمةُ المخصّص المختوم في makhzan_kamil.tsv (v7.1 B1): سندٌ مختوم يُرسَّم به D6


def build_makhzan_sanad(surfaces, mashru_root):
    """يشغّل qari على السطوح ويُعيد {surface_key: sanad} لكلّ سطحٍ له قولٌ بسندٍ يبدأ ببصمة المخصّص (936c68e0).
    سندٌ مختوم عبر قناة Mashru (qari على mawsua/makhzan_kamil.tsv) — لا يُخترَع ولا يُنسَخ نصّه."""
    from t4 import qari as _q
    from pathlib import Path as _P
    res = _q.run_qari(_P(mashru_root), list(surfaces))
    if res.get('rc') is None:
        return {}
    out = {}
    for w in _q.parse_qari(res['stdout'], list(surfaces)).get('words', []):
        sn = next((e['sanad'] for e in w.get('makhzan_entries', []) if (e.get('sanad') or '').startswith(MAKHZAN_SHA)), None)
        if sn:
            out[surface_key(w['surface'])] = sn
    return out


def _lookup_makhzan(makhzan_sanad, surface, lem_n, root):
    """سندُ المخصّص للكلمة من القاموس المبنيّ (بالسطح ثمّ اللِّيمة ثمّ الجذر). None إن غاب."""
    if not makhzan_sanad:
        return None
    for key in (surface_key(surface), lem_n, root):
        if key in makhzan_sanad:
            return {'masdar': 'مخصص-makhzan', 'sha': MAKHZAN_SHA, 'ref': makhzan_sanad[key]}
    return None


def haqiqa_of(unit):
    """D6 (B11): لا معرّف عدديّ ثابت في release_v18 (المعرّفات سلاسل HFN-E-<hex>) ⇒ الفرع الثاني مُعلَنًا:
    haqiqa = 100000 + (int(sha256("release_v18:"+pos+":"+lu_id),16) % 1000000). التصادم داخل النطاق يُرفَض.
    (محفوظ للتوافق ؛ v7 يستعمل haqiqa_event فالفعل ومشتقّه يتشاركان حقيقة حدثهما — نسق Mashru Utur.lean:938.)"""
    key = "release_v18:" + unit['pos'] + ":" + unit['lu_id']
    h = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % 1000000
    return 100000 + h


def haqiqa_event(event_id):
    """D6-ب (v7): حقيقةُ الوحدة = حقيقةُ حدثها ، فالفعلُ ومشتقّه واحد (dhahib=dhahab=10 ، Utur.lean:938).
    لا معرّف عدديّ ثابت ⇒ SHA256_DERIVED على معرّف الحدث: 100000 + int(sha256("release_v18:event:"+event_id))%10^6."""
    h = int(hashlib.sha256(("release_v18:event:" + event_id).encode('utf-8')).hexdigest(), 16) % 1000000
    return 100000 + h


# النصّ المختوم للمقاييس (7f71af0d) بدل maqayis.db (B4). السندُ من موضع الجذر في النصّ المختوم ؛ غيابُه ⇒ D6_NO_SANAD (لا db).
SEALED_MAQAYIS_SHA = '7f71af0dfe056cb84e7da24657fa13edc6e8061c'
_SEALED_MAQAYIS_PATHS = [
    Path(os.environ['MUDAA_DIR']) / 'maqayis.txt' if os.environ.get('MUDAA_DIR') else None,
    Path('/Users/husseinhiyassat/mudaat_mashru/maqayis.txt'),
    Path('/Users/husseinhiyassat/mudaa_dir/maqayis.txt'),
]


def _sealed_maqayis_path():
    return next((p for p in _SEALED_MAQAYIS_PATHS if p and p.exists()), None)


def sealed_maqayis_present():
    return _sealed_maqayis_path() is not None


_MAQAYIS_ROOT_LINES = None


def sealed_maqayis_sanad(root_display):
    """سندُ الجذر من النصّ المختوم للمقاييس (معجم الجذور): موضعُ عنوان «### | (جذر)» ؛ None إن غاب النصّ أو الجذر.
    المرجعُ موضعٌ (رقم سطر) لا نصٌّ منقول — السند = 7f71af0d@line:N/(جذر)."""
    global _MAQAYIS_ROOT_LINES
    p = _sealed_maqayis_path()
    if not p:
        return None
    if _MAQAYIS_ROOT_LINES is None:
        idx = {}
        for i, ln in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            m = _re.match(r'###\s*\|\s*\(([^)]+)\)', ln)
            if m and m.group(1) not in idx:
                idx[m.group(1)] = i
        _MAQAYIS_ROOT_LINES = idx
    n = _MAQAYIS_ROOT_LINES.get(root_display)
    if n is None:
        return None
    return {'masdar': 'مقاييس-مختوم', 'sha': SEALED_MAQAYIS_SHA, 'ref': f'{SEALED_MAQAYIS_SHA[:12]}@line:{n}/({root_display})'}


def maqayis_sanad(root_display):
    """سندٌ من المقاييس: أوّل صفّ entries بجذرٍ مطابق (root_display) ← (entry_id, entry_num, موضع)."""
    con = sqlite3.connect(f"file:{MAQAYIS}?mode=ro", uri=True)
    try:
        cur = con.execute(
            "SELECT id, entry_num, root_display, page_refs FROM entries "
            "WHERE root_display = ? AND is_lexical_entry = 1 ORDER BY entry_num LIMIT 1", (root_display,))
        row = cur.fetchone()
        if not row:
            return None
        return dict(entry_id=row[0], entry_num=row[1], root_display=row[2], page_refs=row[3])
    finally:
        con.close()


import re as _re


def surface_key(surface):
    """مفتاح الكلمة كـ mudaat_prep._key: حذف التشكيل ثمّ إسقاط «ال» الأولى."""
    k = _re.sub(r'[ً-ْٰ]', '', _nfc(surface))
    return k[2:] if k.startswith('ال') else k


def classify7(surface, hok, hfn, qamus_surfaces, manual_keys, alam_keys, mushtaq_wazn, makhzan_sanad=None):
    """التصنيف السباعيّ (B2): COVERED_BY_MANUAL / COVERED_BY_MASHRU_WITNESS / HARF /
    D6_EVENT / D6_MUSHTAQ / D6_PENDING:<سبب> / D7_ALAM / D7_JAMID. لا ترجيح.
    يُعيد dict(category, flags, d6)."""
    k = surface_key(surface)
    flags = []
    if k in manual_keys:
        return dict(category='COVERED_BY_MANUAL', flags=flags)
    if _nfc(surface) in qamus_surfaces:
        return dict(category='COVERED_BY_MASHRU_WITNESS', flags=flags)
    if hok.get('word_class') == 'HARF':
        return dict(category='HARF', flags=flags)
    d6 = d6_classify(surface, hok, hfn, makhzan_sanad=makhzan_sanad)
    if d6['status'] == 'RATIFIED_BY_RULE':
        if k in alam_keys:
            flags.append('D7_ALAM_READING_POSSIBLE')      # مشتقّ يرد في قائمة الأعلام (مالك) — لا ترجيح
        return dict(category=d6['d6_kind'], flags=flags, d6=d6)
    # (٣) Hokom صنّف اسمًا جذرُه null (كـ«مَاتَ» الأجوف) ⇒ يُبقى كما خرج ويُعلَن HOKOM_CLASS_SUSPECT لا يُصلَح
    if hok.get('word_class') == 'ISM' and hok.get('final_root') is None:
        flags.append('HOKOM_CLASS_SUSPECT')
    # PENDING: علمٌ مقدَّمٌ ، ثمّ جامدٌ (اسمٌ ليس على وزن مشتقّ) ، وإلّا سبب D6
    if k in alam_keys:
        return dict(category='D7_ALAM', flags=flags, d6=d6)
    if hok.get('word_class') == 'ISM' and hok.get('final_wazn') not in mushtaq_wazn:
        return dict(category='D7_JAMID', flags=flags, d6=d6)
    return dict(category='D6_PENDING:' + d6['reason'], flags=flags, d6=d6)


# أصناف الوحدة → (tim, ind) : حدث(فعل) true/true ، مصدر/مشتق(ذات/مفهوم) false/true ، حرف -/false
POS_TIM = {'فعل': True, 'مصدر': False, 'اسم فاعل': False, 'اسم مفعول': False}
# صنف Hokom ↔ أقسام HFN المقبولة (condition 4): FI3L حدثٌ=فعل ، ISM ذاتٌ/مفهوم=مصدر/مشتق ، HARF لا وحدة
CLASS_POS = {'FI3L': {'فعل'}, 'ISM': {'مصدر', 'اسم فاعل', 'اسم مفعول'}}


def d6_classify(surface, hok, hfn, makhzan_sanad=None):
    """يطبّق D6 على سطحٍ واحد بتقدير Hokom (hok) ومعجم HFN (hfn).
    يُعيد dict: status (RATIFIED_BY_RULE|PENDING) ، reason (عند PENDING) ، وحقول المودَع عند الاكتمال.
    الترتيب في فحص الغياب يحدّد «السبب الأوّل»."""
    wc = hok.get('word_class'); dr = hok.get('directive'); sub = hok.get('word_class_subclass')
    res = dict(surface=surface, word_class=wc, word_class_subclass=sub, directive=dr, hokom_root=hok.get('final_root'))
    # (١-أ) directive=ACCEPT
    if dr != 'ACCEPT':
        res.update(status='PENDING', reason=f'D6_HOKOM_NOT_ACCEPT:{dr}'); return res
    # حرف: لا جذر ولا وحدة معجمية (ind=false)
    if wc == 'HARF':
        res.update(status='PENDING', reason='D6_NO_HFN_UNIT:حرف', ind=False); return res
    # (١-ب) جذر Hokom حاضر
    root = hamza_root(hok.get('final_root'))
    if not root:
        res.update(status='PENDING', reason='D6_HOKOM_ROOT_NULL'); return res
    # اللِّيمة: المضارع بلِيمة Hokom الماضية (B2) ؛ غيرُه من السطح (إسقاط أل/تنوين/الحركة الأخيرة)
    if wc == 'FI3L' and sub == 'VERBAL_IMPERFECT':
        ls = hok.get('lemma_surface')
        if not ls:
            res.update(status='PENDING', reason='D6_LEMMA_ABSENT'); return res
        lem_v, lem_n = ls, hfn_lemma_norm(ls); res['lemma_source'] = 'HOKOM_LEMMA'
    else:
        lem_v, lem_n = lemma_of(surface); res['lemma_source'] = 'SURFACE'
    res['lemma'] = lem_v
    # وحدة HFN بالجذر + اللِّيمة + قسمٌ يوافق صنف Hokom
    allowed = CLASS_POS.get(wc, set())
    cands = [u for u in hfn.match(root, lem_n) if u['pos'] in allowed]
    if len(cands) == 0:
        # لِيمة موجودة بقسمٍ موافق لكن تحت جذرٍ آخر ⇒ عدم تطابق الجذر (الشرط ١)، لا غياب وحدة
        other_roots = set()
        for p in allowed:
            other_roots |= hfn.lemma_pos_roots(lem_n, p)
        if other_roots:
            res.update(status='PENDING', reason='D6_ROOT_MISMATCH',
                       hfn_roots=sorted(other_roots)); return res
        res.update(status='PENDING', reason='D6_NO_HFN_UNIT'); return res
    if len(cands) > 1:
        res.update(status='PENDING', reason=f'D6_AMBIGUOUS_UNIT:{len(cands)}',
                   units=[u['lu_id'] for u in cands]); return res
    unit = cands[0]
    # (٢) سند مختوم — مصدران طبيعيّان (أمر v7.1): المخصّص (معجم الأعيان ، عبر qari على makhzan_kamil.tsv ، 936c68e0)
    #   أو المقاييس (معجم الجذور ، موضعُ الجذر في النصّ المختوم 7f71af0d). أيُّهما حضر رسَّم D6 ؛ وإلّا D6_NO_SANAD.
    root_display = unit['root_K'] or root
    sanad = _lookup_makhzan(makhzan_sanad, surface, lem_n, root) or sealed_maqayis_sanad(root_display)
    if not sanad:
        res.update(status='PENDING', reason='D6_NO_SANAD', unit=unit['lu_id']); return res
    pos = unit['pos']
    mushtaq = pos in ('اسم فاعل', 'اسم مفعول')
    qism = 'ism_mushtaq' if mushtaq else ('fil' if pos == 'فعل' else 'masdar')
    # اكتمل: الحقول من أعمدة مسمّاة ؛ haqiqa = حقيقة الحدث (الفعلُ ومشتقّه واحد)
    res.update(status='RATIFIED_BY_RULE', d6_kind=('D6_MUSHTAQ' if mushtaq else 'D6_EVENT'),
               unit=unit['lu_id'], unit_lemma=unit['lemma'], pos=pos, qism=qism,
               event_id=unit['event_id'], root_K=unit['root_K'],
               haqiqa=haqiqa_event(unit['event_id']), tim=(pos == 'فعل'), ind=True, sanad=sanad)
    return res
