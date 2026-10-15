#!/bin/bash
# سكربت إعداد البيئة السحابية (يُلصق في خانة Setup script في إعدادات البيئة على claude.ai/code).
# يثبّت Lean 4.34.1 ثمّ يبني ما يسعه في حدود الدقائق الخمس (شرط التخزين المؤقّت للبيئة)؛
# وما بقي يكمله خطّاف SessionStart (scripts/jalsa_ibtida.sh) بناءً تدريجيًّا.
set -u
cd "$(dirname "$0")/.." 2>/dev/null || true
bash scripts/tathbit_lean.sh || exit 1
export PATH="$HOME/.elan/bin:$HOME/.lean/lean-4.34.1-linux/bin:$PATH"
timeout 200 lake build SLGE || true
exit 0
