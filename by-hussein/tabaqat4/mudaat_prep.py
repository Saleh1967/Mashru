#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mudaat_prep.py — يجهّز مودَعات PENDING من taqrir.json (B7/D5).
لكلّ كلمةٍ NO_SEALED في التقرير: الجذر من كتلة Hokom ، القولُ بسنده من ادّعاءات makhzan_* ، tim من القسم (FI3L→true ، ISM→false) ،
ind=false للحرف ؛ haqiqa=null و qabiliyyat/alaqat/khawass=[] — تُترَك للمالك. يدمج في mudaat.json (لا يمسّ RATIFIED) ويطبع ورقة إمضاء.
الاستعمال: python3 mudaat_prep.py <taqrir.json> [--out mudaat.json] [--imda MUDAAT_IMDA.md]
القاعدة: لا يُقترَح haqiqa ولا قابليّة ؛ status يبقى PENDING حتى يُمضي المالك الخانات الثلاث ، وPENDING لا تدخل Lean.
"""
import sys, json, re, argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
MUDAAT = HERE.parent / 'mudaat' / 'mudaat.json'

def _key(surface):
    k = re.sub(r'[ً-ْٰ]', '', surface)
    return k[2:] if k.startswith('ال') else k

def prep(taqrir, existing):
    claims = taqrir.get('claims', [])
    hok = {c['ism'][6:]: c['qima'] for c in claims if c['ism'].startswith('hokom_') and isinstance(c['qima'], dict)}
    out = {}
    for t in taqrir.get('tokens') or []:
        a, surface = t['anchor'], t['surface']
        mad = next((c for c in claims if c['ism'] == f'madlul_{a}'), None)
        if mad and mad.get('qima') is not None: continue          # له مدلول أصلًا
        k = _key(surface)
        if existing.get(k, {}).get('status') == 'RATIFIED': continue   # لا يُمَسّ المُمضى
        h = hok.get(a, {})
        makh = next((c for c in claims if c['ism'] == f'makhzan_{a}' and c.get('qima')), None)
        out[k] = {'surface': surface, 'ism_lean': re.sub(r'\W', '_', k) + '_m', 'status': 'PENDING',
                  'haqiqa': None, 'khawass': [], 'alaqat': [], 'qabiliyyat': [], 'afrad': [],
                  'tim': h.get('word_class') == 'FI3L', 'ind': h.get('word_class') != 'HARF',
                  'jidhr': {'root': h.get('final_root'), 'wazn': h.get('final_wazn'),
                            'pin': h.get('pin'), 'directive': h.get('directive')},
                  'makhzan': {'qawl': (makh['qima'][0] if makh and isinstance(makh['qima'], list) and makh['qima'] else None),
                              'sanad_claim': makh['tarjama'] if makh else None},
                  'imda': {'man': None, 'tarikh': None}}
    return out

def imda_sheet(prepared):
    L = ['# ورقة إمضاء المودَعات — للمالك (D5)', '',
         'لكلّ كلمة: جُهِّز (١) الجذر من Hokom و(٢) القول من المخزن ؛ والمطلوب منك (٣): **haqiqa (≥1000) ، qabiliyyat ، alaqat ، khawass** بإمضائك.',
         'تذكير: إن أمضيتَ «طالب» بلا حقيقة «كتب» في قابليّاته ، فسيُخرج Mashru `laHukm` لـ«كتب الطالب» — قاعدتُه لا الأداة. والأداةُ لا تقترح.',
         '', '| الكلمة | الجذر (Hokom) | directive | القول (المخزن) | المطلوب منك |', '|---|---|---|---|---|']
    for k, e in prepared.items():
        j = e['jidhr']
        L.append(f"| {e['surface']} (`{e['ism_lean']}`) | {j.get('root')} | {j.get('directive')} | "
                 f"{(e['makhzan'] or {}).get('qawl') or '—'} | haqiqa≥1000 ، qabiliyyat ، alaqat ، khawass ، ثمّ status=RATIFIED |")
    return '\n'.join(L) + '\n'

# ================================ D6 (الإيداع بالجملة) ================================
import sys as _sys
_sys.path.insert(0, str(HERE))
from t4 import hfn_d6 as _d6                      # محرّك D6 (READ_ONLY على HFN/maqayis)
from t4 import dal as _dal                        # ترميز الخلايا من Dal/Makharij.lean


def _ism_lean_d6(lu_id):
    """اسمٌ لاتينيّ ثابتٌ متتبَّعٌ إلى وحدة HFN: d6_<lu_id مُعقَّم> (صالح Lean ، بلا اختراع)."""
    return 'd6_' + re.sub(r'\W', '_', lu_id)


def _surfaces_from_text(path):
    """سطوحٌ متمايزةٌ من ملفّ نصّ (سطرٌ لكلّ جملة) ؛ تقطيعٌ على الفراغ وإسقاطُ الترقيم ، بترتيب الورود."""
    out = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        for w in line.split():
            w = w.strip('.،؟!:؛""«»')
            if w and w not in out:
                out.append(w)
    return out


def _surfaces_from_taqrir(taqrir):
    """سطوح الكلمات من tokens التقرير (بلا تكرار ، بترتيب الورود)."""
    out = []
    for t in taqrir.get('tokens') or []:
        s = t.get('surface')
        if s and s not in out:
            out.append(s)
    return out


def prep_d6(surfaces, existing, hfn, imda_sha, imda_date):
    """يطبّق D6 على كلّ سطح. يُعيد (d6_entries, pending_entries, shadowed, coverage_counts).
    لا يمسّ مدخلات RATIFIED اليدوية (status==RATIFIED) ؛ يُعلن D6_SHADOWED_BY_MANUAL حيث تداخلت."""
    import hokom_adapter as _hk
    hok = _hk.taqdir(surfaces)
    seen_haqiqa = {m.get('haqiqa') for m in existing.values() if isinstance(m.get('haqiqa'), int)}
    d6_entries, pending, shadowed = {}, {}, []
    cov = {'SURFACES': len(surfaces), 'FULL': 0, 'PENDING': 0, 'reasons': {}}
    for s, h in zip(surfaces, hok):
        r = _d6.d6_classify(s, h, hfn)
        k = _key(s)
        manual = existing.get(k, {}).get('status') == 'RATIFIED'
        if r['status'] == 'RATIFIED_BY_RULE':
            cov['FULL'] += 1
            if manual:
                shadowed.append(k); continue                      # اليدويّ يغلب (D6_SHADOWED_BY_MANUAL)
            hq = r['haqiqa']
            if hq in seen_haqiqa or (10 <= hq <= 60):
                pending[k] = _pending_entry(s, h, f'D6_HAQIQA_COLLISION:{hq}'); cov['PENDING'] += 1
                cov['reasons']['D6_HAQIQA_COLLISION'] = cov['reasons'].get('D6_HAQIQA_COLLISION', 0) + 1
                continue
            seen_haqiqa.add(hq)
            d6_entries[k] = {
                'surface': s, 'ism_lean': _ism_lean_d6(r['unit']), 'status': 'RATIFIED_BY_RULE',
                'haqiqa': hq, 'khawass': [], 'alaqat': [], 'qabiliyyat': [], 'afrad': [],
                'tim': r['tim'], 'ind': r['ind'],
                'jidhr': {'root': h.get('final_root'), 'wazn': h.get('final_wazn'),
                          'pin': h.get('pin'), 'directive': h.get('directive')},
                'masdar': {'hfn_file': 'lexical_units.csv', 'hfn_row_id': r['unit'],
                           'hfn_event_id': r['event_id'], 'hfn_pos': r['pos'], 'hfn_lemma': r['unit_lemma'],
                           'hfn_sha256': imda_sha,
                           'sanad': {'masdar': 'مقاييس', 'root_display': r['sanad']['root_display'],
                                     'entry_num': r['sanad']['entry_num'], 'page_refs': r['sanad']['page_refs']}},
                'imda': {'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18',
                         'hfn_sha256': imda_sha, 'tarikh': imda_date},
            }
        else:
            cov['PENDING'] += 1
            cov['reasons'][r['reason'].split(':')[0]] = cov['reasons'].get(r['reason'].split(':')[0], 0) + 1
            if not manual:
                pending[k] = _pending_entry(s, h, r['reason'])
    return d6_entries, pending, shadowed, cov


def _pending_entry(surface, h, reason):
    k = _key(surface)
    return {'surface': surface, 'ism_lean': re.sub(r'\W', '_', k) + '_m', 'status': 'PENDING',
            'haqiqa': None, 'khawass': [], 'alaqat': [], 'qabiliyyat': [], 'afrad': [],
            'tim': h.get('word_class') == 'FI3L', 'ind': h.get('word_class') != 'HARF',
            'jidhr': {'root': h.get('final_root'), 'wazn': h.get('final_wazn'),
                      'pin': h.get('pin'), 'directive': h.get('directive')},
            'sabab_d6': reason, 'imda': {'man': None, 'tarikh': None}}


def gen_mudaat_lean(doc, mashru_root):
    """يولّد Mudaat.lean من RATIFIED + RATIFIED_BY_RULE معًا. Kalima = ⟨khalaya, wasl, al⟩ (Dal/Jumla.lean)."""
    hw = _dal.load_hawamil(Path(mashru_root))
    L = ['/- by-hussein/mudaat/Mudaat.lean — مولَّدٌ من مودَعات RATIFIED (D5) و RATIFIED_BY_RULE (D6). يُفحَص قائمًا بذاته. -/',
         'import Jisr.Utur', 'namespace Mudaat', 'open Jisr.Utur SLGE.Awwalan Dal', '']
    for k, e in doc.get('sijill', {}).items():
        if e.get('status') not in ('RATIFIED', 'RATIFIED_BY_RULE'):
            continue
        ism = e['ism_lean']
        b = lambda x: 'true' if x else 'false'
        q = ', '.join(str(x) for x in e.get('qabiliyyat') or [])
        L.append(f"def {ism} : Madlul := {{ haqiqa := {e['haqiqa']}, khawass := [], alaqat := [], "
                 f"qabiliyyat := [{q}], afrad := [], tim := {b(e['tim'])}, ind := {b(e['ind'])} }}"
                 f"   -- {e['surface']} ({e['status']})")
        kd = _dal.encode_word(e['surface'], hw)
        if kd.ok:
            L.append(f"def {ism}K : Kalima := ⟨{kd.khalaya}, {b(kd.wasl)}, {b(kd.al)}⟩")
        else:
            # حدُّ Mashru: جدولُ المخارج لا يرمّز بعض الحروف (ة) ، فتُحذَف خليّةُ الكلمة ويُعلَن ؛ المدلولُ باقٍ
            L.append(f"-- {ism}K: DAL_UNENCODABLE {kd.residuals} — لا ترميزَ خلايا لـ«{e['surface']}» (حدّ Mashru ، لا يُطبَّع السطح)")
    L += ['', 'end Mudaat', '']
    return '\n'.join(L)


# ================================ v7: D6-ب + D7 + قناة الإيداع ================================
def _ajnas_rows():
    p = HERE.parent.parent.parent / 'mawsua' / 'ajnas_mukhassas.tsv'   # mashru/mawsua/
    if not p.exists():
        return []
    return [l.rstrip('\n').split('\t') for l in p.read_text(encoding='utf-8').splitlines()[1:]]


def _mukhassas_sha():
    sj = HERE.parent.parent.parent / 'mudaat' / 'sijill.json'          # mashru/mudaat/sijill.json
    try:
        for e in (json.loads(sj.read_text(encoding='utf-8')).get('sijill') or []):
            if 'مخصص' in e.get('ism', '') or 'مخصّص' in e.get('ism', ''):
                return e.get('sha256')
    except Exception:
        return None
    return None


def _ajnas_ref(surface_key, rows, sha):
    """مرجع المخصّص (لا نصّ): sinf/satr حيث يرد اللفظُ في عنوان ؛ وإلّا None."""
    hits = [(r[0], r[1]) for r in rows if len(r) >= 3 and surface_key in r[2]]
    if not hits:
        return None
    sinf, satr = hits[0]
    return {'masdar': 'مخصص', 'sha': sha, 'sinf': sinf, 'satr': satr, 'count': len(hits)}


def prep_v7(surfaces, existing, hfn, imda_sha, imda_date, mashru_root):
    """التصنيف السباعيّ (sealed) ثمّ كتابة mudaat.json بالمراجع فقط (B2/B3/B4). لا يمسّ RATIFIED اليدويّ.
    يُعيد (doc_sijill, coverage_both_modes, export_rows)."""
    import hokom_adapter as _hk
    from t4 import hfn_d6 as _d6
    qamus = set(json.loads((HERE / 't4' / 'qamus.json').read_text(encoding='utf-8'))['kalimat'].keys())
    manual = {k for k, e in existing.items() if e.get('status') == 'RATIFIED'}
    alam = set(json.loads((HERE.parent / 'mudaat' / 'alam.json').read_text(encoding='utf-8'))['alam_keys'])
    mw = set(json.loads((HERE / 't4' / 'mushtaq_awzan.json').read_text(encoding='utf-8'))['mushtaq_hokom_wazn'])
    rows = _ajnas_rows(); msha = _mukhassas_sha()
    hok = _hk.taqdir(surfaces)
    makhzan = _d6.build_makhzan_sanad(surfaces, mashru_root)   # سند المخصّص عبر qari (936c68e0) — v7.1 B1
    from collections import Counter, OrderedDict
    cov = Counter()
    out = OrderedDict((k, e) for k, e in existing.items() if e.get('status') == 'RATIFIED')   # اليدويّ وحده يُحفَظ
    export = []
    for w, h in zip(surfaces, hok):
        k = _d6.surface_key(w)
        r = _d6.classify7(w, h, hfn, qamus, manual, alam, mw, makhzan_sanad=makhzan)
        cat = r['category']
        cov[cat.split(':')[0] if cat.startswith('D6_PENDING') else cat] += 1
        if k in manual or cat in ('COVERED_BY_MASHRU_WITNESS', 'HARF') or cat.startswith('COVERED'):
            continue
        d6 = r.get('d6', {})
        mref = makhzan.get(k)          # سند المخصّص للكلمة إن وُجد (D7 يُجهَّز به أيضًا)
        if cat in ('D6_EVENT', 'D6_MUSHTAQ'):
            out[k] = {'surface': w, 'ism_lean': _ism_lean_d6(d6['unit']), 'status': 'RATIFIED_BY_RULE',
                      'haqiqa': d6['haqiqa'], 'khawass': [], 'alaqat': [], 'qabiliyyat': [], 'afrad': [],
                      'tim': d6['tim'], 'ind': True, 'qism': d6['qism'],
                      'masdar': {'hfn_file': 'lexical_units.csv', 'hfn_row_id': d6['unit'],
                                 'hfn_event_id': d6['event_id'], 'hfn_sha256': imda_sha, 'sanad': d6['sanad']},
                      'imda': {'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18',
                               'hfn_sha256': imda_sha, 'tarikh': imda_date},
                      'flags': r['flags']}
            export.append(out[k])
        elif cat in ('D7_JAMID', 'D7_ALAM', 'D7_MASDAR', 'D7_ISHARA', 'D7_SUSPECT'):
            out[k] = {'surface': w, 'ism_lean': re.sub(r'\W', '_', k) + '_m', 'status': 'PENDING',
                      'sabab_d7': cat, 'kulli_juzi': ('juzi' if cat == 'D7_ALAM' else 'kulli'),
                      'haqiqa': None, 'khawass': [], 'alaqat': [], 'qabiliyyat': [], 'flags': r['flags'],
                      'jidhr': {'root': h.get('final_root'), 'word_class': h.get('word_class'),
                                'wazn': h.get('final_wazn')},
                      'sanad_makhzan': ({'sha': _d6.MAKHZAN_SHA, 'ref': mref} if mref else None),
                      'mukhassas_ref': _ajnas_ref(k, rows, msha),
                      'imda': {'man': None, 'tarikh': None}}
        else:   # D6_PENDING:*
            out[k] = {'surface': w, 'ism_lean': re.sub(r'\W', '_', k) + '_m', 'status': 'PENDING',
                      'sabab_d6': d6.get('reason'), 'haqiqa': None, 'khawass': [], 'alaqat': [], 'qabiliyyat': [],
                      'flags': r['flags'],
                      'jidhr': {'root': h.get('final_root'), 'word_class': h.get('word_class'),
                                'wazn': h.get('final_wazn')},
                      'imda': {'man': None, 'tarikh': None}}
    return out, cov, export


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('taqrir'); ap.add_argument('--out', default=str(MUDAAT)); ap.add_argument('--imda', default=str(HERE.parent / 'mudaat' / 'MUDAAT_IMDA.md'))
    ap.add_argument('--d6', action='store_true', help='يطبّق قانون D6 (HFN+المقاييس) ؛ يضيف RATIFIED_BY_RULE ولا يمسّ اليدويّ')
    ap.add_argument('--mashru', default=str(HERE.parent.parent), help='جذر Mashru (لتوليد Kalima من Dal/Makharij.lean)')
    ap.add_argument('--lean', help='مسار Mudaat.lean لإعادة توليده (افتراضًا لا يُكتب)')
    ap.add_argument('--coverage', help='مسار D6_COVERAGE.md (مع --d6/--v7)')
    ap.add_argument('--date', default=None, help='tarikh الإمضاء (افتراضًا اليوم)')
    ap.add_argument('--v7', action='store_true', help='D6-ب + D7 (sealed) ؛ يكتب mudaat.json بالمراجع ، وExport ، وMUDAAT_IMDA (D7)')
    ap.add_argument('--export', help='مسار madlulat_export.tsv')
    ap.add_argument('--imda-d7', help='مسار MUDAAT_IMDA.md (D7 فقط)')
    a = ap.parse_args(argv)
    is_txt = str(a.taqrir).endswith('.txt')
    taqrir = {} if is_txt else json.loads(Path(a.taqrir).read_text(encoding='utf-8'))
    doc = json.loads(Path(a.out).read_text(encoding='utf-8')) if Path(a.out).exists() else {'_law': 'D5/D6', 'sijill': {}}
    existing = doc.setdefault('sijill', {})

    if a.v7:
        import datetime, hashlib
        imda_date = a.date or datetime.date.today().isoformat()
        imda_sha = hashlib.sha256((Path(_d6.HFN_V18) / 'MANIFEST.json').read_bytes()).hexdigest()
        hfn = _d6.HFN()
        if is_txt:
            surfaces = _surfaces_from_text(Path(a.taqrir)); note = f"{a.taqrir} ({len(surfaces)} سطحًا متمايزًا)"
        else:
            surfaces = _surfaces_from_taqrir(taqrir); note = f"taqrir ({len(surfaces)} سطحًا)"
        out, cov, export = prep_v7(surfaces, existing, hfn, imda_sha, imda_date, a.mashru)
        doc['sijill'] = dict(out)
        Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
        if a.lean:
            Path(a.lean).write_text(gen_mudaat_lean(doc, a.mashru), encoding='utf-8')
        if a.export:
            Path(a.export).write_text(_export_tsv(doc), encoding='utf-8')
        if a.coverage:
            Path(a.coverage).write_text(_coverage_v7_md(cov, doc, note), encoding='utf-8')
        if a.imda_d7:
            Path(a.imda_d7).write_text(_imda_d7_md(doc), encoding='utf-8')
            Path(a.imda_d7).parent.joinpath('HOKOM_REPAIR_LIST.md').write_text(_repair_list_md(doc), encoding='utf-8')
        print(f"v7.1 (سند المخصّص عبر qari) → {dict(cov)}")
        for k, e in doc['sijill'].items():
            fl = ' '.join(e.get('flags') or [])
            print(f"  {e['status']:16} {k:10} {e.get('sabab_d6') or e.get('sabab_d7') or e.get('imda',{}).get('qanun') or ''} {fl}")
        return 0

    if a.d6:
        import datetime
        imda_date = a.date or datetime.date.today().isoformat()
        man = Path(_d6.HFN_V18) / 'MANIFEST.json'
        import hashlib
        imda_sha = hashlib.sha256(man.read_bytes()).hexdigest()
        hfn = _d6.HFN()
        surfaces = _surfaces_from_taqrir(taqrir)
        d6e, pend, shadowed, cov = prep_d6(surfaces, existing, hfn, imda_sha, imda_date)
        for k, v in d6e.items():
            if existing.get(k, {}).get('status') != 'RATIFIED': existing[k] = v
        for k, v in pend.items():
            if existing.get(k, {}).get('status') not in ('RATIFIED', 'RATIFIED_BY_RULE'): existing[k] = v
        Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
        if a.lean:
            Path(a.lean).write_text(gen_mudaat_lean(doc, a.mashru), encoding='utf-8')
        if a.coverage:
            Path(a.coverage).write_text(_coverage_md(cov, d6e, pend, shadowed), encoding='utf-8')
        print(f"D6 → {a.out} ؛ FULL={cov['FULL']} PENDING={cov['PENDING']} SHADOWED={len(shadowed)} ؛ reasons={cov['reasons']}")
        for k, e in d6e.items(): print('  RATIFIED_BY_RULE:', k, e['haqiqa'], e['ism_lean'])
        for k in shadowed: print('  D6_SHADOWED_BY_MANUAL:', k)
        return 0

    prepared = prep(taqrir, existing)
    for k, v in prepared.items():
        if existing.get(k, {}).get('status') != 'RATIFIED': existing[k] = v
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    Path(a.imda).write_text(imda_sheet({k: existing[k] for k in prepared}), encoding='utf-8')
    print(f'جُهِّز {len(prepared)} مودَعًا PENDING → {a.out} ؛ ورقة الإمضاء → {a.imda}')
    for k in prepared: print('  PENDING:', k, prepared[k]['jidhr'].get('root'))
    return 0


def _coverage_md(cov, d6e, pend, shadowed):
    L = ['# D6_COVERAGE (مولَّد بـ mudaat_prep --d6)', '',
         f"SURFACES_MEASURED = {cov['SURFACES']}", f"D6_FULL = {cov['FULL']}", f"D6_PENDING = {cov['PENDING']}",
         f"reasons = {cov['reasons']}", f"SHADOWED_BY_MANUAL = {shadowed}", '', '## FULL']
    for k, e in d6e.items():
        L.append(f"- {e['surface']} → {e['ism_lean']} haqiqa={e['haqiqa']} tim={e['tim']} sanad(entry_num)={e['masdar']['sanad']['entry_num']}")
    L.append('\n## PENDING')
    for k, e in pend.items():
        L.append(f"- {e['surface']} → {e.get('sabab_d6')}")
    return '\n'.join(L) + '\n'

def _export_tsv(doc):
    """madlulat_export.tsv: RATIFIED + RATIFIED_BY_RULE بأعمدة Madlul + السند + imda (مراجع لا نصّ)."""
    cols = ['key', 'surface', 'ism_lean', 'status', 'haqiqa', 'tim', 'ind', 'qism',
            'qabiliyyat', 'sanad_ref', 'imda']
    L = ['\t'.join(cols)]
    for k, e in doc.get('sijill', {}).items():
        if e.get('status') not in ('RATIFIED', 'RATIFIED_BY_RULE'):
            continue
        sanad = e.get('masdar', {}).get('sanad') or e.get('makhzan') or {}
        L.append('\t'.join(str(x) for x in [
            k, e['surface'], e['ism_lean'], e['status'], e.get('haqiqa'), e.get('tim'), e.get('ind'),
            e.get('qism', ''), ','.join(str(q) for q in e.get('qabiliyyat') or []),
            json.dumps(sanad, ensure_ascii=False), json.dumps(e.get('imda', {}), ensure_ascii=False)]))
    return '\n'.join(L) + '\n'


def _coverage_v7_md(cov, doc, corpus_note=''):
    L = ['# D6_COVERAGE (v7.1) — التصنيف السباعيّ ، سند المخصّص عبر qari', '',
         '**v7.1 (١):** سندُ المخصّص عبر qari على `mawsua/makhzan_kamil.tsv` (يبدأ ببصمة 936c68e0) سندٌ مختوم يُرسَّم به D6 ويُجهَّز به D7.',
         'المقاييس تبقى `D6_NO_SANAD` حتى يحضُر نصّها المختوم (7f71af0d). maqayis.db لا يُرسَّم به.', '',
         f'**الكوربوس:** {corpus_note}', '',
         '## الأعداد (التصنيف السباعيّ)', f"`{dict(cov)}`", '',
         '## سجلّ mudaat.json']
    for k, e in doc.get('sijill', {}).items():
        tag = e.get('imda', {}).get('qanun') or e.get('sabab_d6') or e.get('sabab_d7') or ''
        fl = (' ⚑' + ' '.join(e.get('flags'))) if e.get('flags') else ''
        sn = ' [سند مخصّص]' if e.get('sanad_makhzan') else ''
        L.append(f"- {e['surface']} ({k}) → {e['status']} {tag}{sn}{fl}")
    return '\n'.join(L) + '\n'


def _d7_row(k, e):
    j = e.get('jidhr', {}); ref = e.get('mukhassas_ref'); mk = e.get('sanad_makhzan')
    src = (f"مخصّص@{ref['satr']}({ref['sinf']})" if ref else (f"مخصّص-قول {str((mk or {}).get('ref',''))[:28]}" if mk else '—'))
    return f"| {e['surface']} | {e.get('kulli_juzi')} | {j.get('root')} | {j.get('word_class')}/{j.get('wazn')} | {src} |  |"


def _imda_d7_md(doc):
    """ورقة الإمضاء ثلاثًا (أمر v7.2 ٢): (أ) جوامد للإمضاء ، (ج) مصادر/صفات/إشارة مؤجَّلة. (ب) في HOKOM_REPAIR_LIST.md."""
    s = doc.get('sijill', {})
    jamid = [(k, e) for k, e in s.items() if e.get('sabab_d7') == 'D7_JAMID']
    jeem = [(k, e) for k, e in s.items() if e.get('sabab_d7') in ('D7_MASDAR', 'D7_SIFA', 'D7_ISHARA')]
    alam = [(k, e) for k, e in s.items() if e.get('sabab_d7') == 'D7_ALAM']
    nsus = sum(1 for k, e in s.items() if e.get('sabab_d7') == 'D7_SUSPECT')
    hdr = ['| الكلمة | kulli/juzi | جذر Hokom | صنف/وزن | المصدر (مرجع لا نصّ) | haqiqa (فارغ) |', '|---|---|---|---|---|---|']
    L = ['# ورقة إمضاء D7 — للمالك (ثلاث قوائم ، أمر v7.2 ٢)', '',
         'المطلوب منك في (أ): **haqiqa (≥1000) ، qabiliyyat ، alaqat ، khawass** ثمّ status=RATIFIED. لا يُقترَح رقم (فارغ عمدًا).', '',
         f'## (أ) جوامدُ للإمضاء — {len(jamid)}', *hdr, *[_d7_row(k, e) for k, e in jamid], '',
         f'## (ج) مصادرُ/صفاتٌ/إشارةٌ — قرارُ المالك مؤجَّل — {len(jeem)}',
         '(تُعلَن D7_MASDAR / D7_SIFA / D7_ISHARA ؛ لا تُمضَى حتى يقرّر المالك قسمها)', *hdr,
         *[f"{_d7_row(k, e)[:-3]} ← {e['sabab_d7']} |" for k, e in jeem], '',
         f'## (ب) مشبوهةٌ (HOKOM_CLASS_SUSPECT) — {nsus} — لا تُمضَى ، انظر HOKOM_REPAIR_LIST.md', '',
         f'## أعلام (قائمة alam.json) — {len(alam)}', *hdr, *[_d7_row(k, e) for k, e in alam]]
    return '\n'.join(L) + '\n'


def _repair_list_md(doc):
    """(ب) HOKOM_CLASS_SUSPECT: اسمٌ بجذر null (أكثرُه أفعالٌ قرأها Hokom اسمًا) — تُراجَع ولا تُمضَى."""
    s = doc.get('sijill', {})
    sus = [(k, e) for k, e in s.items() if e.get('sabab_d7') == 'D7_SUSPECT']
    L = ['# HOKOM_REPAIR_LIST — كلماتٌ صنّفها Hokom اسمًا بجذر null (v7.2 ٢ب)', '',
         'تُعرَض كما خرجت من Hokom ، لا تُصلَح ولا تُمضَى ؛ أكثرُها أفعالٌ (جاء/فاز/مات…) قرأها Hokom ISM.', '',
         '| الكلمة (السطح) | صنف Hokom | وزن | بقايا |', '|---|---|---|---|']
    for k, e in sus:
        j = e.get('jidhr', {})
        L.append(f"| {e['surface']} | {j.get('word_class')} | {j.get('wazn')} | root=null |")
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    sys.exit(main())
