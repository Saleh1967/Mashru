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

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('taqrir'); ap.add_argument('--out', default=str(MUDAAT)); ap.add_argument('--imda', default=str(HERE.parent / 'mudaat' / 'MUDAAT_IMDA.md'))
    a = ap.parse_args(argv)
    taqrir = json.loads(Path(a.taqrir).read_text(encoding='utf-8'))
    doc = json.loads(Path(a.out).read_text(encoding='utf-8')) if Path(a.out).exists() else {'_law': 'D5', 'sijill': {}}
    existing = doc.setdefault('sijill', {})
    prepared = prep(taqrir, existing)
    for k, v in prepared.items():
        if existing.get(k, {}).get('status') != 'RATIFIED': existing[k] = v
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
    Path(a.imda).write_text(imda_sheet({k: existing[k] for k in prepared}), encoding='utf-8')
    print(f'جُهِّز {len(prepared)} مودَعًا PENDING → {a.out} ؛ ورقة الإمضاء → {a.imda}')
    for k in prepared: print('  PENDING:', k, prepared[k]['jidhr'].get('root'))
    return 0

if __name__ == '__main__':
    sys.exit(main())
