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
sys.path.insert(0, os.path.join(os.path.abspath(root), "tahaqquq"))
import bawwaba  # noqa: E402 — عيوبُ النصّ (٤ب) بدالّة البوّابة نفسِها
print("الاختبارات:", len(tests), flush=True)


def sabab(out, namat):
    """موضعُ القتل من المخرج: ملفُّ أوّل خطأ بناءٍ في Lean، أو أوّلُ اختبار unittest فشل — ليُرى أنّ الطفرة قُتلت لسببها."""
    m = sorted(set(re.findall(namat, out, re.M)))
    return f" ({'، '.join(m[:4])})" if m else ""

alive = []
for n in names:
    t = tafrat[n]
    tmp = tempfile.mkdtemp()
    dst = os.path.join(tmp, "p")
    shutil.copytree(root, dst, ignore=shutil.ignore_patterns("__pycache__", "mustakshif", "jalsa_haqiqiyya_out"))
    ayb = bawwaba.ayb_tafra(t, dst)   # لا كتابةَ بطفرةٍ معيبة (خارج النسخة، في تعليق، نصٌّ مكرَّر أو غائب)
    if ayb:
        print(n, "— معيبة (٤ب):", ayb, flush=True)
        alive.append(n)
        shutil.rmtree(tmp)
        continue
    path = bawwaba.masar_tafra(t, dst)
    s = open(path, encoding="utf-8").read()
    open(path, "w", encoding="utf-8").write(s.replace(t["min"], t["ila"], 1))
    p = subprocess.run(["lake", "build"], cwd=dst, capture_output=True, text=True)
    why = "lake build" + sabab(p.stdout + p.stderr, r"^error: (\S+?):\d+") if p.returncode != 0 else None
    if why is None:
        for x in tests:
            p = subprocess.run([sys.executable, "-I", x], cwd=dst, capture_output=True, text=True)
            if p.returncode != 0:
                why = x + sabab(p.stdout + p.stderr, r"^(?:FAIL|ERROR): (\S+)")
                break
    print(n, "— قُتلت بـ" + why if why else "— عاشت", flush=True)
    if not why:
        alive.append(n)
    shutil.rmtree(tmp)
print(f"قُتلت {len(names) - len(alive)} من {len(names)}" + (f"؛ عاشت: {alive}" if alive else ""))
sys.exit(1 if alive else 0)
