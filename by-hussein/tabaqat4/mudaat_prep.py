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
        kd = _dal.encode_word(e['surface'], hw)
        if not kd.ok:
            raise RuntimeError(f'MUDAA_DAL_UNENCODABLE:{k}:{kd.residuals}')
        b = lambda x: 'true' if x else 'false'
        q = ', '.join(str(x) for x in e.get('qabiliyyat') or [])
        L.append(f"def {ism} : Madlul := {{ haqiqa := {e['haqiqa']}, khawass := [], alaqat := [], "
                 f"qabiliyyat := [{q}], afrad := [], tim := {b(e['tim'])}, ind := {b(e['ind'])} }}"
                 f"   -- {e['surface']} ({e['status']})")
        L.append(f"def {ism}K : Kalima := ⟨{kd.khalaya}, {b(kd.wasl)}, {b(kd.al)}⟩")
    L += ['', 'end Mudaat', '']
    return '\n'.join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('taqrir'); ap.add_argument('--out', default=str(MUDAAT)); ap.add_argument('--imda', default=str(HERE.parent / 'mudaat' / 'MUDAAT_IMDA.md'))
    ap.add_argument('--d6', action='store_true', help='يطبّق قانون D6 (HFN+المقاييس) ؛ يضيف RATIFIED_BY_RULE ولا يمسّ اليدويّ')
    ap.add_argument('--mashru', default=str(HERE.parent.parent), help='جذر Mashru (لتوليد Kalima من Dal/Makharij.lean)')
    ap.add_argument('--lean', help='مسار Mudaat.lean لإعادة توليده (افتراضًا لا يُكتب)')
    ap.add_argument('--coverage', help='مسار D6_COVERAGE.md (مع --d6)')
    ap.add_argument('--date', default=None, help='tarikh الإمضاء (افتراضًا اليوم)')
    a = ap.parse_args(argv)
    taqrir = json.loads(Path(a.taqrir).read_text(encoding='utf-8'))
    doc = json.loads(Path(a.out).read_text(encoding='utf-8')) if Path(a.out).exists() else {'_law': 'D5/D6', 'sijill': {}}
    existing = doc.setdefault('sijill', {})

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

if __name__ == '__main__':
    sys.exit(main())
