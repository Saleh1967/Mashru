# -*- coding: utf-8 -*-
"""التقرير: JSON (القيم الأصلية كلّها) ، MD (الجداول) ، HTML (الواجهة المفهومة + التفاصيل الفنية قابلة الطيّ)."""
from __future__ import annotations
import html, json
from pathlib import Path
from typing import Any, Dict, List

TABAQA_AR = {0: '٠ — تقدير Hokom', 1: '١ — الدالّ وحده', 2: '٢ — المدلول وحده', 3: '٣ — معًا (الإطار والحكم)', 4: '٤ — العقل (المرساة والإسناد)'}
Q7 = [('started', 'بدأ الاستدعاء؟'), ('completed', 'اكتمل؟'), ('found', 'وجد؟'), ('produced', 'أنتج؟'),
      ('accepted', 'قُبل؟'), ('stored', 'حُفظ؟'), ('consumed_by_next', 'استهلكه التالي؟')]


def _yn(v):
    return {True: 'نعم', False: 'لا', None: '—(لم يُقَس)'}[v]


def _claims_by_tabaqa(rec) -> Dict[int, List[dict]]:
    out: Dict[int, List[dict]] = {}
    for c in rec['claims']: out.setdefault(c['tabaqa'], []).append(c)
    return out


def to_md(rec: Dict[str, Any]) -> str:
    L = []
    inp = rec['input']
    L.append(f"# Tabaqat4 — «{inp['nass_kama_wasal']}»\n")
    L.append('```')
    L.append(f"SCHEMA            = {rec['schema']}")
    L.append(f"TEXT_SHA256       = {inp['sha256']}")
    L.append(f"CODEPOINTS        = {inp['codepoints']} ؛ NFC_EQ_INPUT={inp['nfc_eq_input']}")
    L.append(f"MASHRU_HEAD       = {rec['identity']['mashru_head']} ؛ TREE_CLEAN={rec['identity']['mashru_tree_clean']}")
    L.append(f"LEAN_TOOLCHAIN    = {rec['identity']['lean_toolchain']}")
    L.append(f"QAMUS_SHA256      = {rec['identity']['qamus_sha256'][:16]}…")
    L.append('TABAQAT_STATE     = ' + ' | '.join(f"ط{k}:{v}" for k, v in rec['tabaqat_state'].items()))
    L.append(f"HUKM3             = {rec.get('hukm3')}")
    L.append('WASM_SUMMARY      = ' + ' ، '.join(f"{k}={v}" for k, v in rec['wasm_summary'].items() if v))
    L.append('```\n')
    L.append('## ١. ما الذي عرفه Mashru — طبقةً طبقة\n')
    L.append('| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |')
    L.append('|---|---|---|---|---|')
    for tb, cs in sorted(_claims_by_tabaqa(rec).items()):
        for c in cs:
            L.append(f"| {TABAQA_AR[tb]} | `{c['ism']}` | {c['tarjama']} | {c['rutba'] or '**بلا رتبة**'} | {c['burhan'] or ''} {('— ' + c['sabab_ghiyab']) if c['sabab_ghiyab'] else ''} |")
    L.append('\n## ٢. الفصل الرباعي لكل كلمة\n')
    if rec['tokens']:
        L.append('| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |')
        L.append('|---|---|---|---|---|---|')
        dal = rec['dal'] or []; maani = rec['maani'] or []
        st3 = rec['tabaqat_state'].get(3) or rec['tabaqat_state'].get('3'); st4 = rec['tabaqat_state'].get(4) or rec['tabaqat_state'].get('4')
        for i, t in enumerate(rec['tokens']):
            d = dal[i] if i < len(dal) else None; m = maani[i] if i < len(maani) else None
            dcell = (' '.join(d['cells_human']) + (' ؛ ' + '؛'.join(d['residuals']) if d['residuals'] else '')) if d else '—'
            mcell = (f"`{m['ism']}` {m['ref']}" + (f" ؛ مودَع {m['mudaa']['ism']} {m['mudaa']['sha256'][:8]}" if m.get('mudaa') else ' ؛ بلا مودَع معلَن')) if m else 'NO_SEALED_MADLUL'
            L.append(f"| {t['anchor']} | {t['surface']} | {dcell} | {mcell} | {st3} | {st4} |")
    L.append('\n## ٣. المراحل — الأسئلة السبعة\n')
    L.append('| المرحلة | ' + ' | '.join(q for _, q in Q7) + ' | السبب | البقايا |')
    L.append('|---|' + '---|' * len(Q7) + '---|---|')
    for s in rec['stages']:
        L.append(f"| {s['stage']} | " + ' | '.join(_yn(s[k]) for k, _ in Q7) + f" | {s.get('reason') or ''} | {'؛ '.join(s['residuals'])} |")
    if rec.get('lean'):
        L.append('\n## ٤. البرهان (Lean)\n')
        ln = rec['lean']
        L.append('```')
        L.append(f"PASS1_RC = {ln['pass1']['rc']} ؛ PASS2_RC = {ln['pass2']['rc'] if ln.get('pass2') else None}")
        L.append(f"OBSERVED = {json.dumps(ln.get('observed'), ensure_ascii=False)}")
        for k, v in (ln.get('theorems') or {}).items():
            L.append(f"{k:18s} passed={v['passed']} axioms={v['axioms']}")
        L.append(f"FILES = {json.dumps(ln.get('files'))}")
        L.append('```')
    L.append('\n## ٥. ما لا يُدَّعى\n')
    for x in rec['la_yuddaa']: L.append(f'- {x}')
    L.append('\n## ٦. هوية التشغيل\n```')
    for k, v in rec['identity'].items():
        if k == 'tool_files':
            for f, h in v.items(): L.append(f"  {h[:16]}  {f}")
        else: L.append(f"{k} = {v}")
    L.append(f"timestamp_utc = {rec['timestamp_utc']}")
    L.append('```')
    return '\n'.join(L) + '\n'


def to_html(rec: Dict[str, Any], md_text: str) -> str:
    inp = rec['input']; e = html.escape
    states = rec['tabaqat_state']
    def badge(v):
        col = {'مبرهن على الشاهد': '#1b7f3b', 'مبرهن': '#0b5d2a', 'NOT_REACHED': '#777', 'PARTIAL_OR_BLOCKED': '#b3261e'}.get(v, '#8a6d00')
        return f'<span style="background:{col};color:#fff;padding:2px 8px;border-radius:10px">{e(str(v))}</span>'
    rows = []
    for tb, cs in sorted(_claims_by_tabaqa(rec).items()):
        for c in cs:
            rows.append(f"<tr><td>{e(TABAQA_AR[tb])}</td><td>{e(c['tarjama'])}</td><td>{badge(c['rutba'] or 'بلا رتبة')}</td>"
                        f"<td><small>{e(c['burhan'] or '')} {e(c['sabab_ghiyab'] or '')}</small></td></tr>")
    stg = []
    for s in rec['stages']:
        stg.append('<tr><td>' + e(s['stage']) + '</td>' + ''.join(f'<td>{_yn(s[k])}</td>' for k, _ in Q7) +
                   f"<td>{e(s.get('reason') or '')}</td><td>{e('؛ '.join(s['residuals']))}</td></tr>")
    unresolved = [f"{s['stage']}: {s['reason']}" for s in rec['stages'] if s.get('reason') and (s['accepted'] is False or s['completed'] is False or s['found'] is False)]
    unresolved += [f"{s['stage']}: {r}" for s in rec['stages'] for r in s['residuals']]
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>Tabaqat4 — {e(inp['nass_kama_wasal'])}</title>
<style>body{{font-family:-apple-system,"Segoe UI",Tahoma,sans-serif;margin:24px;max-width:1200px;background:#fafafa;color:#222}}
table{{border-collapse:collapse;width:100%;margin:8px 0}}td,th{{border:1px solid #ddd;padding:6px 8px;vertical-align:top}}th{{background:#eee}}
code,pre{{font-family:Menlo,monospace;font-size:12px}}pre{{background:#f0f0f0;padding:10px;overflow:auto}}details{{margin:10px 0}}summary{{cursor:pointer;font-weight:bold}}
.k{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.k div{{background:#fff;border:1px solid #ddd;padding:10px;border-radius:8px}}</style></head><body>
<h1>الطبقات الأربع — «{e(inp['nass_kama_wasal'])}»</h1>
<p><code>sha256 {e(inp['sha256'])}</code> · Mashru HEAD <code>{e(str(rec['identity']['mashru_head']))}</code> · شجرة Mashru نظيفة: {_yn(rec['identity']['mashru_tree_clean'])}</p>
<div class="k">{''.join(f'<div><b>{e(TABAQA_AR[int(k)])}</b><br>{badge(v)}</div>' for k, v in states.items())}</div>
<h2>١. ما الذي عرفه Mashru؟</h2>
<table><tr><th>الطبقة</th><th>القيمة مترجمة</th><th>الرتبة (سلّم Mashru)</th><th>البرهان / سبب الغياب</th></tr>{''.join(rows)}</table>
<h2>٢. ما الذي بقي غير محسوم — وسببه</h2>
{'<ul>' + ''.join(f'<li>{e(u)}</li>' for u in unresolved) + '</ul>' if unresolved else '<p>لا شيء مفتوح في هذا التشغيل داخل نطاق الأداة.</p>'}
<h2>٣. حدود النتيجة — ما لا يُدَّعى</h2><ul>{''.join(f'<li>{e(x)}</li>' for x in rec['la_yuddaa'])}</ul>
<details><summary>المراحل — الأسئلة السبعة</summary><table><tr><th>المرحلة</th>{''.join(f'<th>{q}</th>' for _, q in Q7)}<th>السبب</th><th>البقايا</th></tr>{''.join(stg)}</table></details>
<details><summary>التفاصيل الفنية الكاملة (MD)</summary><pre>{e(md_text)}</pre></details>
<details><summary>JSON</summary><pre>{e(json.dumps(rec, ensure_ascii=False, indent=1))}</pre></details>
</body></html>"""


def write_all(rec: Dict[str, Any], out_dir: Path) -> Dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    md = to_md(rec)
    (out_dir / 'taqrir.md').write_text(md, encoding='utf-8')
    (out_dir / 'taqrir.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8')
    (out_dir / 'taqrir.html').write_text(to_html(rec, md), encoding='utf-8')
    import hashlib
    return {n: hashlib.sha256((out_dir / n).read_bytes()).hexdigest() for n in ('taqrir.md', 'taqrir.json', 'taqrir.html')}
