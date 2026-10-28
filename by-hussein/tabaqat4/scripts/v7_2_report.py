#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v7.2 (٤): تقريرٌ مرئيّ للكوربوس. يشغّل run.py لكلّ سطر من corpus/c7.txt ، ويبني _runs_samples/v7_2/index.html.
لا يكتب خارج by-hussein. يُستدعى: python3 -I scripts/v7_2_report.py"""
import os, sys, json, html, subprocess, hashlib
from pathlib import Path
from collections import Counter, defaultdict

TOOL = Path(__file__).resolve().parent.parent
MASHRU = TOOL.parent.parent
sys.path.insert(0, str(TOOL))
from t4 import hfn_d6 as D
import hokom_adapter as HK

OUT = TOOL / '_runs_samples' / 'v7_2'
CORPUS = TOOL / 'corpus' / 'c7.txt'
MUDAAT = TOOL.parent / 'mudaat' / 'mudaat.json'


def sha(p, n=16):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:n]


def tree(root, n=16):
    root = Path(root); L = []
    for p in sorted(root.rglob('*')):
        if p.is_file() and '/.git/' not in str(p):
            L.append(f'{p.relative_to(root)}\t{hashlib.sha256(p.read_bytes()).hexdigest()}\n')
    return hashlib.sha256(''.join(sorted(L)).encode()).hexdigest()[:n]


def b2_table():
    qamus = set(json.loads((TOOL / 't4' / 'qamus.json').read_text(encoding='utf-8'))['kalimat'].keys())
    s = json.loads(MUDAAT.read_text(encoding='utf-8'))['sijill']
    manual = {k for k, e in s.items() if e.get('status') == 'RATIFIED'}
    alam = set(json.loads((TOOL.parent / 'mudaat' / 'alam.json').read_text(encoding='utf-8'))['alam_keys'])
    mw = set(json.loads((TOOL / 't4' / 'mushtaq_awzan.json').read_text(encoding='utf-8'))['mushtaq_hokom_wazn'])
    surf = []
    for line in CORPUS.read_text(encoding='utf-8').splitlines():
        for w in line.split():
            w = w.strip('.،؟!:؛""«»')
            if w and w not in surf:
                surf.append(w)
    hok = HK.taqdir(surf); hfn = D.HFN(); mk = D.build_makhzan_sanad(surf, str(MASHRU))
    cat = Counter(); byc = defaultdict(list)
    for w, h in zip(surf, hok):
        r = D.classify7(w, h, hfn, qamus, manual, alam, mw, makhzan_sanad=mk)
        c = r['category']; key = c.split(':')[0] if c.startswith('D6_PENDING') else c
        cat[key] += 1; byc[key].append(w + (' ⚑' if 'HOKOM_CLASS_SUSPECT' in r['flags'] else ''))
    return cat, byc, len(surf)


def run_line(i, line):
    d = OUT / f'c{i:02d}'
    p = subprocess.run([sys.executable, '-I', str(TOOL / 'run.py'), line, '--hokom',
                        '--mudaat', str(MUDAAT), '--out', str(d)],
                       cwd=str(MASHRU), capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    out = {'line': line, 'dir': d, 'state': '', 'hukm3': '', 'wasm': '', 'madlul': []}
    for ln in p.stdout.splitlines():
        if ln.startswith('TABAQAT_STATE'): out['state'] = ln.split('=', 1)[1].strip()
        elif ln.startswith('HUKM3'): out['hukm3'] = ln.split('=', 1)[1].strip()
        elif ln.startswith('WASM'): out['wasm'] = ln.split('=', 1)[1].strip()
    tj = d / 'taqrir.json'
    if tj.exists():
        dd = json.loads(tj.read_text(encoding='utf-8'))
        for c in dd.get('claims', []):
            if c['ism'].startswith('madlul_'):
                q = c.get('qima')
                out['madlul'].append('OWNER_MUDAA' if isinstance(q, dict) else ('—' if q is None else str(q)))
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lines = [l.strip() for l in CORPUS.read_text(encoding='utf-8').splitlines() if l.strip()]
    runs = [run_line(i + 1, l) for i, l in enumerate(lines)]
    cat, byc, nsurf = b2_table()
    head = subprocess.run(['git', '-C', str(MASHRU), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
    tah = subprocess.run([sys.executable, '-I', str(MASHRU / 'mudaat' / 'idaa.py'), 'tahaqqaq',
                          '/Users/husseinhiyassat/mudaat_mashru'], capture_output=True, text=True).stdout.strip()
    e = html.escape
    H = ['<!doctype html><html lang="ar" dir="rtl"><meta charset="utf-8">',
         '<title>tabaqat4 v7.2 — تقرير الكوربوس</title>',
         '<style>body{font-family:-apple-system,"Segoe UI",sans-serif;margin:2rem;line-height:1.7;font-size:17px}',
         'table{border-collapse:collapse;margin:1rem 0;width:100%}td,th{border:1px solid #bbb;padding:.4rem .6rem;text-align:right}',
         'th{background:#f0f0f0}code{background:#f6f6f6;padding:.1rem .3rem;border-radius:3px}',
         '.d6{background:#e6ffe6}.d7{background:#fff6e6}.harf{background:#eef}.cov{background:#eee}</style>',
         '<h1>tabaqat4 v7.2 — تقرير الكوربوس المرئيّ</h1>',
         '<h2>هويّة الجولة</h2><ul>',
         f'<li>MASHRU_HEAD = <code>{e(head)}</code></li>',
         f'<li>c7.txt sha256 = <code>{e(sha(CORPUS, 64))}</code> ({len(lines)} أسطر)</li>',
         f'<li>HOKOM_TREE = <code>{tree("/Users/husseinhiyassat/hokom")}</code> · HFN_v18 = <code>{tree(D.HFN_V18)}</code> · maqayis.db = <code>{sha(D.MAQAYIS)}</code></li>',
         f'<li>MUDAA_DIR = /Users/husseinhiyassat/mudaat_mashru — idaa.py tahaqqaq: <code>{e(tah.replace(chr(10)," ؛ "))}</code></li>',
         '</ul>']
    # B2
    H.append(f'<h2>جدول B2 ({nsurf} سطحًا متمايزًا)</h2><table><tr><th>الفئة</th><th>العدد</th><th>الأسماء</th></tr>')
    order = ['D6_EVENT', 'D6_MUSHTAQ', 'D6_PENDING', 'D7_JAMID', 'D7_MASDAR', 'D7_ISHARA', 'D7_SUSPECT', 'D7_ALAM',
             'HARF', 'COVERED_BY_MANUAL', 'COVERED_BY_MASHRU_WITNESS']
    for key in order:
        if not cat.get(key):
            continue
        cls = 'd6' if key.startswith('D6') else ('d7' if key.startswith('D7') else ('harf' if key == 'HARF' else 'cov'))
        H.append(f'<tr class="{cls}"><td><code>{e(key)}</code></td><td>{cat[key]}</td><td>{e(" · ".join(byc[key]))}</td></tr>')
    H.append(f'<tr><th>D6_FULL</th><td colspan="2">{cat["D6_EVENT"]+cat["D6_MUSHTAQ"]}</td></tr></table>')
    # per sentence
    H.append('<h2>الجمل الثماني</h2><table><tr><th>#</th><th>الجملة</th><th>TABAQAT_STATE</th><th>HUKM3</th><th>WASM</th><th>المدلول/كلمة</th><th>taqrir</th></tr>')
    for i, r in enumerate(runs, 1):
        rel = f'c{i:02d}/taqrir.html'
        H.append(f'<tr><td>{i}</td><td>{e(r["line"][:60])}{"…" if len(r["line"])>60 else ""}</td>'
                 f'<td>{e(r["state"])}</td><td><code>{e(r["hukm3"])}</code></td><td>{e(r["wasm"])}</td>'
                 f'<td>{e(" ".join(r["madlul"]))}</td><td><a href="{rel}">taqrir.html</a></td></tr>')
    H.append('</table>')
    # ما ينتظر المالك (أ)
    s = json.loads(MUDAAT.read_text(encoding='utf-8'))['sijill']
    jamid = [e2['surface'] for e2 in s.values() if e2.get('sabab_d7') == 'D7_JAMID']
    H.append('<h2>ما ينتظر المالك — القائمة (أ) جوامدُ للإمضاء</h2>')
    H.append('<p>' + e(' · '.join(jamid)) + '</p>')
    H.append('<p>(ب) مشبوهة Hokom في <code>HOKOM_REPAIR_LIST.md</code> · (ج) مصادر/إشارة مؤجَّلة في <code>MUDAAT_IMDA.md</code>)</p>')
    H.append('</html>')
    idx = OUT / 'index.html'
    idx.write_text('\n'.join(H), encoding='utf-8')
    print('INDEX:', idx)
    return idx


if __name__ == '__main__':
    main()
