#!/bin/bash
# تجربة خطّاف Stop في جلسة Claude Code حقيقية (متداخلة، بلا واجهة)، على نسخة مؤقّتة من المشروع.
#
# الشرط: اعتمادُ دخولٍ للاستدلال في البيئة: إمّا CLAUDE_CODE_OAUTH_TOKEN (من `claude setup-token` على جهاز المالك)
# وإمّا ANTHROPIC_API_KEY. لا يُكتب الاعتماد في أيّ ملفّ من ملفّات المشروع.
# ما يجري:
#   ١. نسخة مؤقّتة من المشروع، طفراتها معدومة (لتسريع البوّابة)، وفيها sorry مزروع في Aql/Tajriba.lean.
#   ٢. `claude -p` في النسخة يُطلب منه أن يقول «تمّ» فقط. عند توقّفه يعمل خطّاف Stop؛ فإن حجبه قرأ السبب
#      وأصلح (مسموحٌ له Read/Edit/Write وحدها، في النسخة وحدها) ثمّ حاول التوقّف من جديد.
#   ٣. المخرج stream-json يُحفظ كاملًا، ومعه سجلّ الخطّاف sijill_khattaf.log.
# التشغيل: bash tahaqquq/jalsa_haqiqiyya.sh [مجلّد المخرجات]   (النموذج: NAMUDHAJ، والافتراضيّ sonnet)
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$ROOT/tahaqquq/jalsa_haqiqiyya_out}"
mkdir -p "$OUT"
if [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "لا اعتماد دخول: عيّن CLAUDE_CODE_OAUTH_TOKEN أو ANTHROPIC_API_KEY" >&2; exit 2
fi
TMP=$(mktemp -d)
cp -r "$ROOT" "$TMP/project"
cd "$TMP/project" || exit 2
echo "[]" > tahaqquq/tafrat.json
rm -f .claude/hooks/.marrat_alhajb .claude/hooks/sijill_khattaf.log
printf '/- تجربة الخطّاف في جلسة حقيقية -/\ntheorem tajriba_khattaf : 1 = 1 := by sorry\n' > Aql/Tajriba.lean
export CLAUDE_PROJECT_DIR="$TMP/project"
# الجلسة: لا Bash، لا شبكة، أدوات الملفّات فقط، وعدد أدوار محدود.
timeout 1500 claude -p "اقرأ CLAUDE.md ثمّ قل «تمّ» فقط. إن حُجب توقّفك بسبب البوّابة فأصلح السبب في ملفّات المشروع بالأدوات المتاحة ثمّ قل «تمّ» من جديد." \
  --model "${NAMUDHAJ:-sonnet}" --max-turns 8 \
  --allowedTools "Read,Edit,Write,Glob,Grep" \
  --disallowedTools "Bash,WebFetch,WebSearch,Agent" \
  --output-format stream-json --verbose \
  > "$OUT/stream.jsonl" 2> "$OUT/stderr.txt"
CODE=$?
cp .claude/hooks/sijill_khattaf.log "$OUT/sijill_khattaf.log" 2>/dev/null
cp Aql/Tajriba.lean "$OUT/Tajriba.lean.final" 2>/dev/null
cd /; rm -rf "$TMP"
echo "خروج الجلسة: $CODE"
echo "--- سجلّ الخطّاف:"; cat "$OUT/sijill_khattaf.log" 2>/dev/null || echo "(لم يُكتب: الخطّاف لم يعمل)"
echo "--- أحداث الخطّاف في المخرج:"; grep -c '"hook' "$OUT/stream.jsonl" 2>/dev/null
echo "--- آخر نصّ من الوكيل:"; python3 -I - "$OUT/stream.jsonl" <<'EOF'
import json, sys
last = ""
for line in open(sys.argv[1], encoding="utf-8"):
    try:
        d = json.loads(line)
    except Exception:
        continue
    if d.get("type") == "result":
        last = d.get("result", "") or last
print(last[:600])
EOF
