"""اختبار جدول الأجناس المودَع (القطعة الأولى) ومطابقة جدول Lean له (`Madlul/Tayin.lean`: `fusul`، `ramzQism`).

يُشغَّل حين يحضر المودَع (MUDAA_DIR وفيه ajnas.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ المودَع الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه «مختوم».
٢. توقّعاتٌ مستقلّة عن Lean: أربعةُ صفوف بأسمائها (جماد، نبات، حيوان، إنسان) وحقائقها 1–4، وكلُّ قيمةٍ من الخواصّ الخمس من الثلاث
   (نعم/لا/لا حكم)، وكلُّ صفٍّ له بصمةُ مودَعٍ مختوم في عمود basma وعددُ شهودٍ ≥ 1.
٣. جدولُ Lean يُقرأ من الملفّ بالنصّ (لا عبر Lean): `fusul` (الخواصّ الخمس لكلّ قسم؛ الغائبُ = لا حكم) و`ramzQism` (الحقائق)
   و`qab` (قابليّات الحركة) — فيُطابَق بالمودَع: الخواصُّ سواء، والحقائقُ سواء، وقابليّاتُ Lean جزءٌ من قابليّات المودَع.
٤. شجرةُ الأجناس الأعلى `mawsua/ajnas_mukhassas.tsv` تُعاد من المخصّص المختوم الحاضر بـ `scripts/bina_ajnas_mukhassas.py` وتطابق المخزون
   بايتًا؛ وتوقّعاتٌ مستقلّة: 18 عنوانًا بلفظ «كتاب» و310 بلفظ «باب» و3 ختام و2 تالٍ، وأوّلُها «كتاب خلق الإنسان» س383.
التشغيل: python3 -I tahaqquq/test_ajnas.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الأجناس — القطعة الأولى"
ASMA = {"jamad": "جماد", "nabat": "نبات", "hayawan": "حيوان", "insan": "إنسان"}
QIYAM = {"naam": "نعم", "la": "لا", "laHukm": "لا حكم"}
QAB = {"sayr": "السير", "rakd": "الركض", "jary": "الجري", "zahf": "الزحف", "qafz": "القفز"}
KHAWASS = ["taghadhdhi", "numuw", "mawt", "intiqal", "aql"]

d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "ajnas.tsv") if d else None
if not p or not os.path.exists(p):
    print("لم يُشغَّل (المودَع غير حاضر؛ عيّن MUDAA_DIR وفيه ajnas.tsv)")
    sys.exit(0)

sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["hala"] == "مختوم" and m["naw"] == "معلومات-سابقة", m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
makhtuma = {x["sha256"] for x in sijill if x["hala"] == "مختوم"}
ok = 1

lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
hdr = lines[0].split("\t")
rows = [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]
assert [r["jins"] for r in rows] == ["جماد", "نبات", "حيوان", "إنسان"], [r["jins"] for r in rows]
assert [r["haqiqa"] for r in rows] == ["1", "2", "3", "4"]
for r in rows:
    for k in KHAWASS:
        assert r[k] in ("نعم", "لا", "لا حكم"), (r["jins"], k, r[k])
    assert r["basma"] in makhtuma, (r["jins"], r["basma"][:16])
    assert int(r["adad_shuhud"]) >= 1, r["jins"]
ok += 1

lean = open(os.path.join(ROOT, "Madlul", "Tayin.lean"), encoding="utf-8").read()
fus = lean[lean.index("def fusul : Qism → Khawass"):]
fus = fus[:fus.index("\n\n")]
lean_rows = {}
for q, body in re.findall(r"\| \.(\w+) => \{([^}]*)\}", fus, re.S):
    vals = dict(re.findall(r"(\w+) := \.(\w+)", body))
    qab = re.findall(r"\.(sayr|rakd|jary|zahf|qafz)", body)
    lean_rows[q] = ({k: QIYAM[vals.get(k, "laHukm")] for k in KHAWASS}, [QAB[x] for x in qab])
assert set(lean_rows) == set(ASMA), set(lean_rows)
ramz = dict(re.findall(r"\| \.(\w+) => (\d+)", lean[lean.index("def ramzQism"):lean.index("def ramzQab")]))
ghalat = []
for q, ism in ASMA.items():
    r = next(x for x in rows if x["jins"] == ism)
    kh, qab = lean_rows[q]
    for k in KHAWASS:
        if kh[k] != r[k]:
            ghalat.append((ism, k, kh[k], r[k]))
    if ramz[q] != r["haqiqa"]:
        ghalat.append((ism, "haqiqa", ramz[q], r["haqiqa"]))
    mudaa_qab = [x for x in r["qabiliyyat"].split("؛") if x]
    for x in qab:
        if x not in mudaa_qab:
            ghalat.append((ism, "qab", x, mudaa_qab))
    if not qab and mudaa_qab and ism in ("حيوان", "إنسان"):
        ghalat.append((ism, "qab", "فارغ في Lean", mudaa_qab))
assert not ghalat, ghalat
ok += 1

mk = os.path.join(d, "mukhassas.txt")
if os.path.exists(mk):
    mm = next(x for x in sijill if x["ism"] == "المخصص")
    assert hashlib.sha256(open(mk, "rb").read()).hexdigest() == mm["sha256"], "المخصّص: تغيّرت بصمته"
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import bina_ajnas_mukhassas
    muwallad = bina_ajnas_mukhassas.bina(mk)
    makhzun = open(os.path.join(ROOT, "mawsua", "ajnas_mukhassas.tsv"), encoding="utf-8").read()
    assert muwallad == makhzun, "شجرة الأجناس لا تطابق المولَّد من المخصّص"
    asnaf = [l.split("\t")[0] for l in muwallad.split("\n")[1:] if l]
    assert (asnaf.count("كتاب"), asnaf.count("باب"), asnaf.count("كتاب-ختام"), asnaf.count("كتاب-تالٍ")) == (18, 310, 3, 2), \
        (asnaf.count("كتاب"), asnaf.count("باب"))
    assert muwallad.split("\n")[1] == "كتاب\t383\tكتاب خلق الإنسان"
    ok += 1
    print(f"{ok}/4 — {len(rows)}/4 صفوف مطابقة لجدول Lean، وشجرة المخصّص {len(asnaf)} عنوانًا مطابقة")
else:
    print(f"{ok}/3 — {len(rows)}/4 صفوف مطابقة لجدول Lean (الخواصّ الخمس والحقائق والقابليّات)؛ شجرة المخصّص لم تُفحص (المودَع غير حاضر)")
