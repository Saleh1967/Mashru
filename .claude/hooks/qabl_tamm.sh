#!/bin/bash
# «قبل أن تقول تمّ»: خطّاف Stop. يقرأ مدخل Claude Code (JSON على stdin)، ويشغّل البوّابة.
#   * إن مرّت: خروج 0 (يُسمح بالتوقّف).
#   * إن لم تمرّ: خروج 2 والسبب على stderr، فيُكمل الوكيل العمل بسببها (بروتوكول Claude Code).
#   * حارس الدوران: stop_hook_active=false يعني محاولةَ توقّفٍ جديدة فيبدأ العدّ؛ وtrue يعني أنّ الوكيل
#     يُكمل بسبب حجبٍ سابق فيزيد العدّ. بعد ثلاثة حجوب متتالية يُسمح بالتوقّف مع أمرٍ بإبلاغ المالك بالفشل.
#   * كلّ تشغيلٍ يُسجَّل في .claude/hooks/sijill_khattaf.log (الوقت، stop_hook_active، الجلسة، النتيجة).
#   * عند الفشل يُعاد آخر 40 سطرًا من مخرج البوّابة (التقرير ثمّ الأسباب)؛ كان 15 فسقطت الأسباب لمّا طال التقرير (CI #16).
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0
IN=$(cat)
ACTIVE=$(printf '%s' "$IN" | python3 -I -c 'import json,sys
try:
    d=json.load(sys.stdin); print(str(d.get("stop_hook_active", False)).lower()); print(d.get("session_id","?"))
except Exception: print("?"); print("?")' 2>/dev/null)
ACTIVE_FLAG=$(printf '%s' "$ACTIVE" | sed -n 1p)
SESSION=$(printf '%s' "$ACTIVE" | sed -n 2p)
LOG=".claude/hooks/sijill_khattaf.log"
GUARD=".claude/hooks/.marrat_alhajb"
OUT=$(python3 -I tahaqquq/bawwaba.py 2>&1)
CODE=$?
if [ $CODE -eq 0 ]; then
  rm -f "$GUARD"
  echo "$(date -u +%FT%TZ) stop_hook_active=$ACTIVE_FLAG session=$SESSION gate=pass exit=0" >> "$LOG"
  exit 0
fi
if [ "$ACTIVE_FLAG" = "true" ]; then
  N=$(( $(cat "$GUARD" 2>/dev/null || echo 0) + 1 ))
else
  N=1
fi
echo $N > "$GUARD"
if [ $N -ge 3 ]; then
  rm -f "$GUARD"
  echo "$(date -u +%FT%TZ) stop_hook_active=$ACTIVE_FLAG session=$SESSION gate=fail block=$N exit=0(guard)" >> "$LOG"
  echo "البوّابة فشلت ثلاث مرّات. أبلغ المالك بالفشل باسمه، ولا تقل «تمّ»:" >&2
  echo "$OUT" | tail -n 40 >&2
  exit 0
fi
echo "$(date -u +%FT%TZ) stop_hook_active=$ACTIVE_FLAG session=$SESSION gate=fail block=$N exit=2" >> "$LOG"
echo "لم تمرّ البوّابة؛ أصلح ثم أعد. المخرج:" >&2
echo "$OUT" | tail -n 40 >&2
exit 2
