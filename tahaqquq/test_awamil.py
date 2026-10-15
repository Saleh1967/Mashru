"""اختبار مطابقة جدول العوامل (Jisr/AwamilJadwal.lean) لمودَعه (xlsx المالك، مختوم في mudaat/sijill.json).

يُشغَّل حين يحضر المودَع (MUDAA_AWAMIL=<مسار xlsx>، أو MUDAA_DIR فيه awamil_mia.xlsx)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمة المودَع الحاضر هي بصمته في السجلّ (وإلّا رُفض باسمه).
٢. مطابَق: ما يولّده scripts/bina_awamil.py من المودَع هو Jisr/AwamilJadwal.lean بنصّه.
٣. توقّعات مستقلّة عن المولّد (عدٌّ مباشر لأعمدة المودَع، مكتوب باليد من قراءة الجدول): 100 صفًّا؛ «تنصب الاسم وترفع
   الخبر» 6؛ «ترفع الاسم وتنصب الخبر» 13؛ «تنصب مفعولين» 10؛ «أداة شرط جزم فعلين» 10؛ الأسلوب «الاستفهام» 10
   و«النداء» 4؛ وترتيب أسماء الجدول في Lean هو ترتيب العمود الأوّل في المودَع.
التشغيل: python3 -I tahaqquq/test_awamil.py
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول العوامل المئة (جدول المالك؛ «مئة حسب الجرجاني» بتسميته في الجلسة)"

path = os.environ.get("MUDAA_AWAMIL")
if not path:
    d = os.environ.get("MUDAA_DIR")
    if d and os.path.exists(os.path.join(d, "awamil_mia.xlsx")):
        path = os.path.join(d, "awamil_mia.xlsx")
if not path or not os.path.exists(path):
    print("لم يُشغَّل (المودَع غير حاضر؛ عيّن MUDAA_AWAMIL أو MUDAA_DIR)")
    sys.exit(0)

sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["hala"] == "مختوم", m
b = hashlib.sha256(open(path, "rb").read()).hexdigest()
assert b == m["sha256"], f"المودَع تغيّرت بصمته: {b[:16]} ≠ {m['sha256'][:16]}"
ok = 1

with tempfile.TemporaryDirectory() as tmp:
    out = os.path.join(tmp, "AwamilJadwal.lean")
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_awamil.py"), path, out],
                       capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    gen = open(out, encoding="utf-8").read()
lean = open(os.path.join(ROOT, "Jisr", "AwamilJadwal.lean"), encoding="utf-8").read()
assert gen == lean, "Jisr/AwamilJadwal.lean لا يطابق ما يولَّد من المودَع"
ok += 1

try:
    import openpyxl  # noqa: E402
except ImportError:
    sys.exit("المودَع حاضر لكنّ openpyxl غائب: ثبّته (pip install openpyxl) — لا حكم")
rows = [[("" if v is None else str(v)) for v in r]
        for r in openpyxl.load_workbook(path, read_only=True).active.iter_rows(values_only=True)]
hdr, rows = rows[0], rows[1:]
assert hdr[:3] == ["العامل", "الأسلوب النحوي", "الحكم الإعرابي"], hdr[:3]
assert len(rows) == 100, len(rows)
hukm = [r[2] for r in rows]
assert hukm.count("تنصب الاسم وترفع الخبر") == 6
assert hukm.count("ترفع الاسم وتنصب الخبر") == 13
assert hukm.count("تنصب مفعولين") == 10
assert hukm.count("أداة شرط جزم فعلين") == 10
uslub = [r[1] for r in rows]
assert uslub.count("الاستفهام") == 10 and uslub.count("النداء") == 4
import re  # noqa: E402
names = re.findall(r'\n  \("((?:[^"\\]|\\.)*)", \d+, (?:true|false)\)', lean)
assert names == [r[0] for r in rows], "ترتيب الأسماء في Lean ليس ترتيب المودَع"
ok += 1

print(f"{ok}/3")
