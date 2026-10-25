# -*- coding: utf-8 -*-
"""قارئ Mashru (Qari/Main.lean) شاهدًا ثانيًا للطبقة الأولى ، ومصدرًا للمخزن في الطبقة الثانية.

يُشغَّل `.lake/build/bin/qari mudaat/sijill.tsv mawsua/makhzan_kamil.tsv <الكلمات…>` مرّةً على الجملة كلّها
(القارئ يطبّق الوقف على آخر النصّ ، فتختلف صورةُ الكلمة الأخيرة أحيانًا عن صورة الوصل في Dal.Kalima — يُعلَن لا يُحسَم).
المخرج نصّ ؛ يُقرأ بعلامات ثابتة من Qari/Main.lean ، وما لم يُقرأ يُعلَن QARI_UNPARSED لا يُخمَّن.
"""
from __future__ import annotations
import re, subprocess, os
from pathlib import Path
from typing import Any, Dict, List, Optional


def qari_exe(mashru_root: Path) -> Optional[Path]:
    p = mashru_root / '.lake' / 'build' / 'bin' / 'qari'
    return p if p.exists() else None


def run_qari(mashru_root: Path, words: List[str], timeout: int = 300) -> Dict[str, Any]:
    exe = qari_exe(mashru_root)
    if not exe:
        return {'rc': None, 'stdout': '', 'stderr': 'QARI_EXE_ABSENT: شغّل `lake build qari` في جذر Mashru', 'cmd': None}
    cmd = [str(exe), 'mudaat/sijill.tsv', 'mawsua/makhzan_kamil.tsv', *words]
    env = dict(os.environ); env['PYTHONDONTWRITEBYTECODE'] = '1'
    try:
        p = subprocess.run(cmd, cwd=str(mashru_root), capture_output=True, text=True, timeout=timeout, env=env)
        return {'rc': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr, 'cmd': ' '.join(cmd[:3]) + ' …'}
    except subprocess.TimeoutExpired:
        return {'rc': None, 'stdout': '', 'stderr': 'QARI_TIMEOUT', 'cmd': ' '.join(cmd[:3])}


_CELL = re.compile(r'\((\d+)\)')


def parse_qari(stdout: str, words: List[str]) -> Dict[str, Any]:
    """يقسّم المخرج إلى كتل «الكلمة: …» ثم «الجملة في الوصل» ؛ لكل كلمة: الخلايا ، الرفض ، الملاحظات ، الجذر ، المخزن."""
    out: Dict[str, Any] = {'words': [], 'jumla': None, 'unparsed': []}
    blocks = re.split(r'(?m)^الكلمة: ', stdout)
    head, blocks = blocks[0], blocks[1:]
    jum_idx = None
    for i, b in enumerate(blocks):
        if '\nالجملة في الوصل' in b:
            b, jum = b.split('\nالجملة في الوصل', 1); blocks[i] = b; out['jumla'] = _parse_jumla('الجملة في الوصل' + jum)
    for b in blocks:
        lines = b.splitlines()
        surface = lines[0].strip()
        w: Dict[str, Any] = {'surface': surface, 'khalaya': None, 'rejected': None, 'notes': [], 'root': None,
                             'root_state': None, 'irab_candidate': None, 'sigha_candidates': None,
                             'makhzan_lookup': None, 'makhzan_entries': []}
        for ln in lines[1:]:
            t = ln.strip()
            if t.startswith('الخلايا:'):
                w['khalaya'] = [int(x) for x in _CELL.findall(t)]
            elif t.startswith('مرفوضة باسمها:'):
                w['rejected'] = t.split(':', 1)[1].strip()
            elif t.startswith('ملاحظة:'):
                w['notes'].append(t.split(':', 1)[1].strip())
            elif t.startswith('مرشَّح الجذر:'):
                m = re.search(r'«([^»]+)»', t); w['root'] = m.group(1) if m else None; w['root_state'] = 'مرشَّح'
            elif t.startswith('الجذر: لا حكم'):
                w['root_state'] = 'لا حكم'; w['root_reason'] = t.split('—', 1)[1].strip() if '—' in t else t
            elif 'حال الآخر إعرابًا' in t:
                m = re.search(r':\s*(الرفع|النصب|الجرّ|الجزم)', t); w['irab_candidate'] = m.group(1) if m else None
            elif t.startswith('القراءة (حقولُ العقد):'):
                m = re.search(r'قطر L65\):\s*(.+)$', t); w['sigha_candidates'] = m.group(1).strip() if m else None
            elif t.startswith('المدلول باللفظ'):
                m = re.search(r'«([^»]+)»', t); w['makhzan_lookup'] = m.group(1) if m else None
            elif t.startswith('القول:'):
                m = re.search(r'القول:\s*(.+?)\s+—\s*وسمه المحسوب:\s*(\S+)', t)
                w['makhzan_entries'].append({'qawl': m.group(1) if m else t, 'wasm': m.group(2) if m else None, 'sanad': None})
            elif t.startswith('أصل') and 'سند:' in t and w['makhzan_entries']:
                w['makhzan_entries'][-1]['sanad'] = t.split('سند:', 1)[1].strip()
            elif t.startswith('المنطوق (مطابقة/تضمّن): لا مدخل'):
                w['makhzan_state'] = 'لا مدخل في المخزن — لا حكم'
        if w['makhzan_entries']: w['makhzan_state'] = f"{len(w['makhzan_entries'])} قول"
        out['words'].append(w)
    if len(out['words']) != len(words):
        out['unparsed'].append(f"WORD_COUNT_MISMATCH: qari={len(out['words'])} input={len(words)}")
    return out


def _parse_jumla(txt: str) -> Dict[str, Any]:
    j: Dict[str, Any] = {'silsila': None, 'qanun': None, 'wasl_notes': []}
    for ln in txt.splitlines():
        t = ln.strip()
        if t.startswith('السلسلة:'):
            j['silsila'] = [int(x) if x != '|' else 116 for x in re.findall(r'\((\d+)\)|(\|)', t) for x in [x[0] or x[1]]]
        elif t.startswith('القانون (آلة الجملة'):
            j['qanun'] = t.split(':', 1)[1].strip()
        elif t.startswith('الوصل عند الكلمة'):
            j['wasl_notes'].append(t)
    return j


def reconcile(my_cells: List[int], my_al: bool, my_wasl: bool, q: Dict[str, Any], is_last: bool) -> Dict[str, Any]:
    """يقارن خلايا الجدول بخلايا القارئ بعد إعلان التحويلات ؛ لا يحسم الاختلاف ، يسمّيه."""
    qc = q.get('khalaya')
    if qc is None:
        return {'state': 'QARI_NO_CELLS', 'reason': q.get('rejected') or 'لا سطر خلايا'}
    transforms = []
    qn = list(qc)
    if (my_al or my_wasl) and qn and qn[0] < 4:          # همزة الوصل المُصلَحة بـ ibtidaForm (حامل 0 = ء)
        qn = qn[1:]; transforms.append('QARI_IBTIDA_HAMZA_DROPPED→Kalima.al/wasl')
    if qn == my_cells:
        return {'state': 'AGREE', 'transforms': transforms}
    reason = None
    if is_last and my_cells[:-2] == qn[:-1] and my_cells[-1] == 59:
        reason = 'WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة)'
    elif is_last and any(n in ('الوقف على التاء المربوطة' in x) for n in [True] for x in q.get('notes', [])):
        reason = 'WAQF_TA_MARBUTA: القارئ يقرأ ة هاءً ساكنة في الوقف ؛ الجدول لا يرمّز ة'
    elif q.get('notes'):
        reason = 'QARI_NOTE: ' + ' ؛ '.join(q['notes'])
    return {'state': 'DISAGREE', 'transforms': transforms, 'qari': qc, 'jadwal': my_cells, 'reason': reason or 'UNEXPLAINED'}
