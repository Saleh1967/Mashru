"""اختبار القطعة الثانية من جدول الأجناس (عُقَد الآباء والجماد) وجدولَي نظام الفيزياء ونظام الرياضيات المودَعة، ومطابقة Lean لها
(`Madlul/Wiratha.lean`: شجرة `shajara` بفصولها؛ `Madlul/Jamad.lean`: ثوابت المواد `ma`…`milh` وقوانين الجدولين بأسمائها).

يُشغَّل حين تحضر المودَعات الثلاثة في MUDAA_DIR (ajnas_jamad.tsv، nizam_fizya.tsv، nizam_riyadiyyat.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصماتُ المودَعات الثلاثة هي بصماتُها في mudaat/sijill.json (وإلّا رُفض المودَع باسمه)، ونوعُها «معلومات-سابقة»، وحالتُها «مختوم».
٢. توقّعاتٌ مستقلّة لجدول الأجناس: 17 صفًّا بأسمائها؛ الحقائقُ: الآباء 0/5/6، الجوهر 10، المواد 11–18، الأجسام 21–23؛ الثلجُ والبخارُ
   بحقيقة الماء (قانون التعيين)؛ الأبُ جنسٌ في الجدول (أو الجماد من القطعة الأولى) والجذرُ الموجود وحدَه ولا دور؛ كلُّ صفّ تحت الجماد
   بخواصّه الخمس الموروثة (لا/لا/لا حكم/لا/لا حكم)؛ القيمُ من الثلاث؛ الوحدةُ من {معدود، مقيس، لا حكم}؛ الحالةُ من {جامد، سائل، بخار، فارغ}؛
   البصمةُ من مودَعٍ مختوم؛ الشهودُ ≥ 1؛ وكلُّ اقتباسٍ «…» بسطره (لسان العرب/المخصّص؛ والمصدرُ محمولٌ على ما بعده بـ «؛ س…») موجودٌ
   في سطره في المودَع الحاضر بلفظه — وإن غاب المعجمان أُعلن «لم تُفحص الاقتباسات».
٣. Lean من النصّ (لا عبر Lean): فصولُ `shajara` في Wiratha.lean تُقرأ، وتُورَّث بمرآةٍ مستقلّة هنا (ما بتّه الأب يبقى وما تُرك يبتّه
   الفصل) فتطابق صفوفَ الآباء الثلاثة في المودَع وصفوفَ القطعة الأولى (ajnas.tsv إن حضر)، وأضلاعُ الشجرة تطابق عمود jins_ala
   (بتعيينٍ معلَن لأسماء القطعة الأولى الوصفية — أبًا أو جدًّا، لأنّها سبقت عُقَدَ الآباء)؛ وثوابتُ `Madda` في Jamad.lean (ma، hadid،
   dhahab، rasas، zibaq، milh) تطابق صفوفَ «ثابت» في نظام الفيزياء قيمةً قيمة (mirat_lean ↔ الحقل)، وحقائقُها حقائقَ الجدول.
٤. كلُّ اسمٍ في عمود mirat_lean في جدولَي القوانين معرَّفٌ في Lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر) في
   Wiratha.lean أو Jamad.lean أو SLGE/MadlulAwwalan.lean — لا يُقبل اسمٌ بمقطعه الأخير وحده.
٥. الحالةُ المرجعية (ف4) تُحسب هنا من العتبات عند 25°م لكلّ مادّة حاضرة العتبتين وتطابق عمود hala في جدول الأجناس؛ والعتباتُ متّسقة (ف3).
التشغيل: python3 -I tahaqquq/test_jamad.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASMA = {"ajnas_jamad.tsv": "جدول الأجناس — القطعة الثانية", "nizam_fizya.tsv": "نظام الفيزياء", "nizam_riyadiyyat.tsv": "نظام الرياضيات"}
KH = ["taghadhdhi", "numuw", "mawt", "intiqal", "aql"]
QIYAM = {"naam": "نعم", "la": "لا", "laHukm": "لا حكم"}

d = os.environ.get("MUDAA_DIR")
if not d or any(not os.path.exists(os.path.join(d, f)) for f in ASMA):
    print("لم يُشغَّل (المودَعات غير حاضرة؛ عيّن MUDAA_DIR وفيه ajnas_jamad.tsv وnizam_fizya.tsv وnizam_riyadiyyat.tsv)")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
makhtuma = {x["sha256"]: x for x in sijill if x["hala"] == "مختوم"}
for f, ism in ASMA.items():
    m = next(x for x in sijill if x["ism"] == ism)
    assert m["hala"] == "مختوم" and m["naw"] == "معلومات-سابقة", m
    b = hashlib.sha256(open(os.path.join(d, f), "rb").read()).hexdigest()
    assert b == m["sha256"], f"{ism}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
ok = 1

# ٢
rows = tsv(os.path.join(d, "ajnas_jamad.tsv"))
asma = [r["jins"] for r in rows]
assert asma == ["موجود", "حيّ", "حيوان (الجنس)", "جوهر", "ماء", "ثلج", "بخار", "حديد", "ذهب", "رصاص", "زئبق", "ملح", "تراب", "رمل",
                "حجر", "صخرة", "جبل"], asma
haq = {r["jins"]: r["haqiqa"] for r in rows}
assert haq["موجود"] == "0" and haq["حيّ"] == "5" and haq["حيوان (الجنس)"] == "6" and haq["جوهر"] == "10"
assert [haq[x] for x in ["ماء", "حديد", "ذهب", "رصاص", "زئبق", "ملح", "تراب", "رمل"]] == ["11", "12", "13", "14", "15", "16", "17", "18"]
assert [haq[x] for x in ["حجر", "صخرة", "جبل"]] == ["21", "22", "23"]
assert haq["ثلج"] == haq["ماء"] == haq["بخار"], "قانون التعيين: الثلج والبخار بحقيقة الماء"
ab = {r["jins"]: r["jins_ala"] for r in rows}
assert ab["موجود"] == "" and all(v != "" for k, v in ab.items() if k != "موجود")
for k, v in ab.items():
    assert v == "" or v in asma or v == "جماد", (k, v)
    seen, x = {k}, v
    while x and x != "جماد":
        assert x not in seen, f"دور في الشجرة عند {k}"
        seen.add(x)
        x = ab[x]
tahtJamad = [r for r in rows if r["jins"] not in ("موجود", "حيّ", "حيوان (الجنس)")]
for r in tahtJamad:
    assert [r[k] for k in KH] == ["لا", "لا", "لا حكم", "لا", "لا حكم"], (r["jins"], [r[k] for k in KH])
for r in rows:
    for k in KH:
        assert r[k] in ("نعم", "لا", "لا حكم"), (r["jins"], k)
    assert r["wahda"] in ("معدود", "مقيس", "لا حكم") and r["ta_wahda"] in ("نعم", "لا", "لا حكم"), r["jins"]
    assert r["hala"] in ("جامد", "سائل", "بخار", ""), r["jins"]
    assert r["basma"] in makhtuma and int(r["adad_shuhud"]) >= 1, r["jins"]
assert [r[k] for r in rows if r["jins"] == "حيّ" for k in KH] == ["نعم", "نعم", "نعم", "لا حكم", "لا حكم"]
assert [r[k] for r in rows if r["jins"] == "حيوان (الجنس)" for k in KH] == ["نعم", "نعم", "نعم", "نعم", "لا حكم"]
assert [r[k] for r in rows if r["jins"] == "موجود" for k in KH] == ["لا حكم"] * 5

nusus = {}
for f, ism in (("lisan.txt", "لسان العرب"), ("mukhassas.txt", "المخصّص")):
    p = os.path.join(d, f)
    if os.path.exists(p):
        nusus[ism] = open(p, encoding="utf-8").read().split("\n")
pat = re.compile(r"(?:(لسان العرب|لسان|المخصّص) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = 0
for f in ASMA:
    for line in open(os.path.join(d, f), encoding="utf-8"):
        for cell in line.rstrip("\n").split("\t"):
            src = None
            for s0, ln, q in pat.findall(cell):
                if s0:
                    src = "لسان العرب" if s0 == "لسان" else s0
                assert src is not None, (f, ln, q[:40], "اقتباس بلا مصدر")
                if src in nusus:
                    assert q in nusus[src][int(ln) - 1], (f, src, ln, q[:40])
                    iqt += 1
iqt_bayan = f"{iqt} اقتباسًا في سطره" if nusus else "لم تُفحص الاقتباسات (لسان العرب والمخصّص غير حاضرين)"
ok += 1

# ٣ — مرآةٌ مستقلّة للتوريث: ما بتّه الأب يبقى، وما تُرك «لا حكم» يبتّه الفصل
wir = open(os.path.join(ROOT, "Madlul", "Wiratha.lean"), encoding="utf-8").read()
blk = wir[wir.index("fasl := fun"):]
blk = blk[:blk.index("}\n\n")]
fasl, parent = {}, {}
for n, body in re.findall(r"\| \.(\w+) => \{([^}]*)\}", blk):
    vals = dict(re.findall(r"(\w+) := \.(\w+)", body))
    fasl[n] = {k: vals.get(k, "laHukm") for k in KH}
abblk = wir[wir.index("ab := fun"):wir.index("fasl := fun")]
for n, p in re.findall(r"\| \.(\w+) => (?:some \.(\w+)|none)", abblk):
    parent[n] = p or None
assert set(fasl) == set(parent) == {"mawjud", "hayy", "jamad", "nabat", "hayawanJins", "hayawan", "insan"}, set(fasl)
# أضلاع الشجرة ↔ عمود jins_ala: القطعة الثانية تسمّي الآباء بأسماء صفوفها؛ والقطعة الأولى تسمّيهم وصفًا («الموجود غير الحيّ» للجذر،
# «الحيّ»، «الحيوان» للجنس لا للنوع) — التعيين معلَن هنا.
ismUqda = {"موجود": "mawjud", "حيّ": "hayy", "حيوان (الجنس)": "hayawanJins", "": None,
           "الموجود غير الحيّ": "mawjud", "الحيّ": "hayy", "الحيوان": "hayawanJins"}
for n, ism in (("mawjud", "موجود"), ("hayy", "حيّ"), ("hayawanJins", "حيوان (الجنس)")):
    assert parent[n] == ismUqda[ab[ism]], (ism, ab[ism], parent[n])


def khawass(n):
    f = fasl[n]
    if parent[n] is None:
        return dict(f)
    p = khawass(parent[n])
    return {k: (f[k] if p[k] == "laHukm" else p[k]) for k in KH}


lean_rows = {n: {k: QIYAM[v] for k, v in khawass(n).items()} for n in fasl}
for n, ism in (("mawjud", "موجود"), ("hayy", "حيّ"), ("hayawanJins", "حيوان (الجنس)")):
    r = next(x for x in rows if x["jins"] == ism)
    assert all(lean_rows[n][k] == r[k] for k in KH), (ism, lean_rows[n], [r[k] for k in KH])
for r in tahtJamad:
    assert all(lean_rows["jamad"][k] == r[k] for k in KH), (r["jins"], lean_rows["jamad"])
p1 = os.path.join(d, "ajnas.tsv")
if os.path.exists(p1):
    for r in tsv(p1):
        n = {"جماد": "jamad", "نبات": "nabat", "حيوان": "hayawan", "إنسان": "insan"}[r["jins"]]
        assert all(lean_rows[n][k] == r[k] for k in KH), (r["jins"], lean_rows[n])
        # القطعةُ الأولى سبقت عُقَدَ الآباء، فجنسُها الأعلى المسمّى أصلٌ في الشجرة (أبٌ أو جدّ: «الحيّ» للحيوان-النوع صار جدًّا)
        aslaf, x = [], parent[n]
        while x:
            aslaf.append(x)
            x = parent[x]
        assert ismUqda[r["jins_ala"]] in aslaf, (r["jins"], r["jins_ala"], aslaf)

jam = open(os.path.join(ROOT, "Madlul", "Jamad.lean"), encoding="utf-8").read()
madda = {}
for n, body in re.findall(r"def (\w+) : Madda := \{([^}]*)\}", jam):
    madda[n] = {}
    for k, a, b in re.findall(r"(\w+) := (?:some \(?(-?\d+)\)?|(\d+))", body):
        madda[n][k] = a or b
assert set(madda) == {"ma", "hadid", "dhahab", "rasas", "zibaq", "milh"}, set(madda)
fiz = tsv(os.path.join(d, "nizam_fizya.tsv"))
thabit = [r for r in fiz if r["naw"] == "thabit"]
assert len(thabit) == 20, len(thabit)
for r in thabit:
    n, fld = r["mirat_lean"].split(".")
    if r["qima"] == "":
        assert fld not in madda[n], (n, fld, "لا حكم في المودَع وقيمة في Lean")
    else:
        assert madda[n].get(fld) == r["qima"], (n, fld, madda[n].get(fld), r["qima"])
for r in rows:
    if r["lean"].startswith("Jamad.") and r["lean"][6:] in madda:
        assert madda[r["lean"][6:]]["haqiqa"] == r["haqiqa"], (r["jins"], r["haqiqa"])
ok += 1

# ٤
awwalan = open(os.path.join(ROOT, "SLGE", "MadlulAwwalan.lean"), encoding="utf-8").read()
src = wir + jam + awwalan
riy = tsv(os.path.join(d, "nizam_riyadiyyat.tsv"))
asmaLean = set()
for r in [x for x in fiz if x["naw"] == "qanun"] + riy:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        asmaLean.add(ident)
for ident in asmaLean:
    full = ident
    for pre in ("SLGE.Awwalan.", "Jamad.", "Wiratha."):
        if full.startswith(pre):
            full = full[len(pre):]
    assert re.search(rf"^(def|theorem|structure|inductive) {re.escape(full)}\b", src, re.M), \
        f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
assert len(asmaLean) >= 30, len(asmaLean)
ok += 1

# ٥ — الحالة المرجعية من العتبات (حساب مستقلّ) واتّساقها
by = {}
for r in thabit:
    n, fld = r["mirat_lean"].split(".")
    if r["qima"] != "":
        by.setdefault(n, {})[fld] = int(r["qima"])
jinsOf = {"ma": "ماء", "hadid": "حديد", "dhahab": "ذهب", "rasas": "رصاص", "zibaq": "زئبق", "milh": "ملح"}
for n, v in by.items():
    assert v["dhawb"] < v["ghalayan"], (n, "ف3")
    hala = "جامد" if 25 < v["dhawb"] else ("سائل" if 25 < v["ghalayan"] else "بخار")
    r = next(x for x in rows if x["jins"] == jinsOf[n])
    assert r["hala"] == hala, (n, r["hala"], hala)
assert sorted(by) == sorted(jinsOf)
ok += 1
print(f"{ok}/5 — {len(rows)}/17 صفًّا، {iqt_bayan}، {len(thabit)} ثابتًا مطابقًا لـ Lean، {len(asmaLean)} اسمًا معرَّفًا، 6/6 حالات مرجعية من العتبات")
