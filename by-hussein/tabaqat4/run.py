#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tabaqat4 — جملة مشكولة ← Mashru (كما هو) ← تقرير الطبقات الأربع.

الاستعمال (من جذر مستودع Mashru أو من أيّ مكان):
    python3 by-hussein/tabaqat4/run.py "ذَهَبَ الْوَلَدُ"
    python3 by-hussein/tabaqat4/run.py "ذَهَبَ الْوَلَدُ" --hokom --out /tmp/x --an 0 --izaha -1
    python3 by-hussein/tabaqat4/run.py "..." --no-lean          (بلا برهان ؛ للفحص السريع)

لا يكتب خارج by-hussein/tabaqat4/ (أو --out) ؛ لا يُعدّل Mashru ؛ Lean يُستدعى بـ `lake env lean` من جذر Mashru.
"""
import os, sys, argparse, json
from pathlib import Path
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from t4.core import Tabaqat4, TOOL_ROOT   # noqa: E402
from t4.report import write_all           # noqa: E402


def find_mashru_root() -> Path:
    env = os.environ.get('MASHRU_ROOT')
    if env: return Path(env)
    for p in [HERE.parent.parent, *HERE.parents]:
        if (p / 'lakefile.toml').exists() and (p / 'Dal' / 'Makharij.lean').exists():
            return p
    raise SystemExit('MASHRU_ROOT_NOT_FOUND: ضع الأداة في <mashru>/by-hussein/tabaqat4/ أو عيّن MASHRU_ROOT')


def main(argv=None):
    ap = argparse.ArgumentParser(description='tabaqat4')
    ap.add_argument('jumla', help='الجملة مشكولةً بين علامتَي تنصيص')
    ap.add_argument('--out', help='مجلد المخرجات (افتراضًا tabaqat4/_runs/<sha8>/)')
    ap.add_argument('--hokom', action='store_true', help='أضف تقدير Hokom عبر hokom_adapter.py (يُعرَض ولا يُستهلك)')
    ap.add_argument('--no-lean', action='store_true', help='لا تشغّل Lean (S7 يُعلَن NOT_RUN)')
    ap.add_argument('--an', type=int, default=0, help='الآن على المرساة (افتراض الشاهد 0)')
    ap.add_argument('--izaha', type=int, default=-1, help='إزاحة الحدث بالساعات (افتراض الشاهد −1)')
    ap.add_argument('--mashru', help='جذر Mashru (افتراضًا يُكتشف من موضع الأداة)')
    ap.add_argument('--forms', nargs='*', default=[], help='باب الجزاء: shart=<صورة> jawab=<صورة> [lam=true] — صيغٌ معلَنة من المالك ، رتبتها رأي')
    a = ap.parse_args(argv)
    root = Path(a.mashru) if a.mashru else find_mashru_root()
    forms = dict(kv.split('=', 1) for kv in a.forms if '=' in kv)
    t = Tabaqat4(root, out_dir=Path(a.out) if a.out else None, use_hokom=a.hokom, run_lean=not a.no_lean,
                 mirsat_an=a.an, arad_izaha=a.izaha, forms=forms)
    rec = t.run(a.jumla)
    out = Path(rec['run_dir'])
    shas = write_all(rec, out)
    print(f"TEXT_SHA256   = {rec['input']['sha256']}")
    print('TABAQAT_STATE = ' + ' | '.join(f"ط{k}:{v}" for k, v in rec['tabaqat_state'].items()))
    print(f"HUKM3         = {rec.get('hukm3')}")
    print('WASM          = ' + ' ، '.join(f"{k}={v}" for k, v in rec['wasm_summary'].items() if v))
    for s in rec['stages']:
        if s.get('reason'): print(f"  {s['stage']}: {s['reason']}")
    print(f"OUT           = {out}")
    for n, h in shas.items(): print(f"  {h[:16]}  {n}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
