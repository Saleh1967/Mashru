#!/bin/bash
# سكربت إعداد البيئة السحابية (يُلصق في خانة Setup script في إعدادات البيئة على claude.ai/code).
# يثبّت Lean 4.34.1 ثمّ يبني ما يسعه في حدود الدقائق الخمس (شرط التخزين المؤقّت للبيئة)؛
# وما بقي يكمله خطّاف SessionStart (scripts/jalsa_ibtida.sh) بناءً تدريجيًّا.
set -u
# حين يُشغَّل من ملفّه: جذر المستودع فوق .claude/؛ وحين يُلصق نصًّا: المجلّد الحاليّ هو الجذر أصلًا.
[ -f "$(dirname "$0")/../scripts/tathbit_lean.sh" ] && cd "$(dirname "$0")/.."
[ -f scripts/tathbit_lean.sh ] || { echo "cloud-setup: شغِّلني من جذر المستودع (لا scripts/tathbit_lean.sh هنا: $PWD)" >&2; exit 1; }
bash scripts/tathbit_lean.sh || exit 1
export PATH="$HOME/.elan/bin:$HOME/.lean/lean-4.34.1-linux/bin:$PATH"
timeout 200 lake build SLGE || true
exit 0
