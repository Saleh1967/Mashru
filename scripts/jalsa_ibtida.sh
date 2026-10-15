#!/bin/bash
# خطّاف SessionStart: يضمن lake على PATH ويبني المشروع بناءً تدريجيًّا (فوريٌّ إن كان مبنيًّا).
# لا يُعطّل الجلسة أبدًا: إن غاب Lean طبع تنبيهًا وخرج 0 (التثبيت بـ scripts/tathbit_lean.sh أو سكربت إعداد البيئة).
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" || exit 0
export PATH="$HOME/.elan/bin:$HOME/.lean/lean-4.34.1-linux/bin:$PATH"
if ! command -v lake >/dev/null 2>&1; then
  echo "تنبيه: lake غير موجود؛ شغّل scripts/tathbit_lean.sh أوّلًا (البوّابة لن تمرّ بلا Lean)." >&2
  exit 0
fi
timeout 540 lake build > /tmp/jalsa_ibtida_build.log 2>&1
echo "lake build: خروج $? (السجلّ /tmp/jalsa_ibtida_build.log)"
exit 0
