"""تدقيقُ مكتبة Nabt في Mashru (منقولةٌ من sonaiso/NABT@3dbe335 بنصّها، 2026-10-28؛ AuditNabt.lean تدقيقُها نفسُه هناك).

يفحص:
١. `lake env lean AuditNabt.lean` يخرج 0 ويطبع NABT_AUDIT_OK: كلُّ اسمٍ في القائمة مبرهنةٌ مبنيّة، ومسلّماتُها ومسلّماتُ كلِّ تصريحٍ تحت
   Nabt. من propext وClassical.choice وQuot.sound.
٢. العددُ المطبوع 1592، وهو عددُ أسماء القائمة في AuditNabt.lean عند المنبع 3dbe335 بعدِّ أسطر «``Nabt.» في الجلسة؛ لا يُحسب هنا من الملفّ
   المفحوص، فحذفُ اسمٍ من القائمة يُكشف.
٣. لا اسمَ مكرَّرٌ في القائمة.
٤. جدولُ القانون `jadawil/law.json` هو مخرجُ `qanunJadwal` (Qari/QanunJadwal.lean على Nabt.Law) بايتًا، وبصمتُه 14e32ae2… — بصمةُ
   `src/nabt/data/law.json` في المنبع وفي اللقطة المضمَّنة قبل الاستقلال (قُرئت في الجلسة)، فلم يتغيّر الجدولُ بالنقل.
الطفرات: P1330 (مبرهنةٌ برهانُها sorryAx، ١)، P1331 (اسمٌ محذوفٌ من القائمة، ٢)، P1332 (الجدولُ المودَع غيرُ المخرج، ٤).
التشغيل: python3 -I tahaqquq/test_nabt_tadqiq.py
"""

import os
import re
import hashlib
import subprocess
import sys

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADAD = 1592
FAIL = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


p = subprocess.run(["lake", "env", "lean", "AuditNabt.lean"], cwd=JADHR, capture_output=True, text=True)
out = p.stdout + p.stderr
check("AuditNabt.lean يخرج 0 ويطبع NABT_AUDIT_OK", p.returncode == 0 and "NABT_AUDIT_OK" in out)
m = re.search(r"NABT_THEOREM_COUNT (\d+)", out)
check(f"عددُ القائمة {ADAD}", m is not None and int(m.group(1)) == ADAD)
asma = re.findall(r"^\s*``(\S+?),?$", open(os.path.join(JADHR, "AuditNabt.lean"), encoding="utf-8").read(), re.M)
check("لا اسمَ مكرَّر في القائمة", len(asma) == len(set(asma)) and len(asma) > 0)
LAW_SHA = "14e32ae208ac5ed2f754e83506e72133d0962756ef0c944d12370746febddcdd"
q = subprocess.run([os.path.join(JADHR, ".lake", "build", "bin", "qanunJadwal")], capture_output=True)
mawdu = open(os.path.join(JADHR, "jadawil", "law.json"), "rb").read()
check("jadawil/law.json مخرجُ qanunJadwal بايتًا", q.returncode == 0 and q.stdout == mawdu)
check("بصمةُ law.json هي بصمتُه قبل النقل", hashlib.sha256(mawdu).hexdigest() == LAW_SHA)
print(f"تدقيق Nabt: {'فشل ' + str(len(FAIL)) if FAIL else 'مرّ'} ({m.group(1) if m else '?'} مبرهنة)")
sys.exit(1 if FAIL else 0)
