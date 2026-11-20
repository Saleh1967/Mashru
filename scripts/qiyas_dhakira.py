"""ذروةُ الذاكرة لكلّ ملفّ Lean وحده (`lake env lean <ملفّ>` على خيطٍ واحد)، بمراقبة ru_maxrss للابن.

التشغيل: python3 -I scripts/qiyas_dhakira.py <وحدة>... — يطبع «وحدة⇥ذروة م.ب⇥ثوانٍ⇥خروج». قياسُ البيئة التي يُشغَّل فيها (بلا وسم).
"""
import os
import resource
import subprocess
import sys
import time

for m in sys.argv[1:]:
    f = m.replace(".", "/") + ".lean"
    t = time.time()
    p = subprocess.run(["lake", "env", "lean", f], capture_output=True, env=dict(os.environ, LEAN_NUM_THREADS="1"))
    r = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    print(f"{m}\t{r // 1024}\t{time.time() - t:.0f}\t{p.returncode}", flush=True)
