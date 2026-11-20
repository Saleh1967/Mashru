#!/usr/bin/env bash
# بناءٌ آمنٌ على الذاكرة (أمرُ المالك 2026-11-20، 03:10: «find solutions for memory»):
# - يطبع أقصى ذاكرةٍ مقيمةٍ لأكبر عمليّةٍ في البناء (GNU time، ru_maxrss للأبناء) — فالذروةُ على CI تُقاس لا تُفترض؛
# - ويعيد `lake build` إن قُتلت عمليّةٌ بنفاد الذاكرة (137 / Killed) حتّى ‎BINA_MUHAWALAT‎ مرّة (افتراضًا 6): ما بُني يبقى في .lake،
#   فالإعادةُ تكمل لا تبدأ؛ وأيُّ خطأٍ آخر (خطأُ Lean) يُعاد رمزُه فورًا بلا إعادة.
set -u
N="${BINA_MUHAWALAT:-6}"
T="$(mktemp)"
for i in $(seq 1 "$N"); do
  if [ -x /usr/bin/time ]; then
    /usr/bin/time -v -o "$T" lake build "$@" > "$T.out" 2>&1; c=$?
    m=$(grep "Maximum resident set size" "$T" | awk '{print $NF}')
    echo "bina_amin: المحاولة $i، الخروج $c، أقصى ذاكرةٍ مقيمة ${m:-?} ك.ب"
  else
    lake build "$@" > "$T.out" 2>&1; c=$?
    echo "bina_amin: المحاولة $i، الخروج $c (بلا /usr/bin/time)"
  fi
  tail -n 3 "$T.out"
  [ "$c" -eq 0 ] && { rm -f "$T" "$T.out"; exit 0; }
  if ! grep -qE "exit code 137|Killed|signal 9|out of memory" "$T.out"; then
    cat "$T.out" | tail -n 60; rm -f "$T" "$T.out"; exit "$c"
  fi
  echo "bina_amin: قُتلت عمليّةٌ بنفاد الذاكرة؛ إعادة"
done
rm -f "$T" "$T.out"
exit 137
