"""تشغيل طفراتٍ مسمّاة وحدها بإجراء tahaqquq/bawwaba.py نفسِه (نسخ الشجرة مع .lake، استبدال أوّل ظهور، lake build ثمّ
اختبارات البوّابة بترتيبها، تُقرأ قائمتُها من bawwaba.py نفسِه فلا تفترق عنه). للفحص المحلّيّ لما تغيّر من الطفرات، لأنّ
المسح الكامل يتجاوز سقف البيئة المحلّيّة؛ والمسح الكامل على CI. يخرج 1 إن عاشت طفرة.
التشغيل: python3 -I tahaqquq/tafrat_juz.py <جذر المستودع> <اسم طفرة>...
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

root, names = sys.argv[1], sys.argv[2:]
src = open(os.path.join(root, "tahaqquq", "bawwaba.py"), encoding="utf-8").read()
# قائمة الاختبارات تُقرأ من البوّابة نفسِها لا تُكتب هنا، فلا تفترق عنها
tests = re.findall(r'run\(\[sys\.executable, "-I", "([^"]+)"\], cwd=dst\)', src)
tafrat = {t["ism"]: t for t in json.load(open(os.path.join(root, "tahaqquq", "tafrat.json"), encoding="utf-8"))}
print("الاختبارات:", len(tests), flush=True)
alive = []
for n in names:
    t = tafrat[n]
    tmp = tempfile.mkdtemp()
    dst = os.path.join(tmp, "p")
    shutil.copytree(root, dst, ignore=shutil.ignore_patterns("__pycache__", "mustakshif", "jalsa_haqiqiyya_out"))
    path = os.path.join(dst, t["milaf"])
    s = open(path, encoding="utf-8").read()
    if t["min"] not in s:
        print(n, "— الاقتباس غائب", flush=True)
        alive.append(n)
        shutil.rmtree(tmp)
        continue
    open(path, "w", encoding="utf-8").write(s.replace(t["min"], t["ila"], 1))
    p = subprocess.run(["lake", "build"], cwd=dst, capture_output=True, text=True)
    why = "lake build" if p.returncode != 0 else None
    if why is None:
        for x in tests:
            p = subprocess.run([sys.executable, "-I", x], cwd=dst, capture_output=True, text=True)
            if p.returncode != 0:
                why = x
                break
    print(n, "— قُتلت بـ" + why if why else "— عاشت", flush=True)
    if not why:
        alive.append(n)
    shutil.rmtree(tmp)
print(f"قُتلت {len(names) - len(alive)} من {len(names)}" + (f"؛ عاشت: {alive}" if alive else ""))
sys.exit(1 if alive else 0)
