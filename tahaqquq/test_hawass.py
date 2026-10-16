"""اختبار جدول الحواسّ الخمس (مرشّح حتّى يُختم) ومطابقة `Madlul/Hawass.lean` له (المعجم `mujam`، خبرات المالك `khibrat`، الأبعاد `abad`،
وأسماء الرخصة والصيغ).

يُشغَّل حين يحضر الجدول (MUDAA_DIR وفيه hawass.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 29 صفًّا — 5 حواسّ بأدواتها ومحسوساتها (العين/مرئيّ، الأذن/مسموع، الفم/مذوق، اليد/ملموس، الأنف/مشموم)، 5 أبعاد،
   8 تسميات، 6 خبرات للمالك، رخصة، 4 صيغ؛ وكلُّ اقتباسٍ «…» بسطره (لسان العرب/قطر الندى) موجودٌ في سطره في المودَع الحاضر بلفظه.
٣. Lean من النصّ (لا عبر Lean): `mujam` (الاسم، البُعد) يطابق صفوفَ التسمية زوجًا زوجًا بترتيبها؛ `khibrat` (الحاسّة، الجنس، البُعد،
   الاسم) يطابق خبراتِ المالك 1–5 بترتيبها؛ `abad` يطابق صفوفَ الأبعاد بأسمائها وحواسّها؛ `adat`/`mahsus` يطابقان صفوفَ الحواسّ.
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Hawass.lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر، أو منشئٌ من
   `Hassa.*`/`Thubut.*`).
٥. قرارُ الرخصة من بنية الجدول وحدها: خبراتُ المالك شاهدُها قولُه (ليس مودَعًا من نوع «واقع-مختوم» في السجلّ) — فكلُّها «معلومة» إن
   طابق اسمُها تسميةً في الجدول، ولا مفهومَ ما لم يحضر في السجلّ مودَعٌ «واقع-مختوم» (يُطابَق بـ `shawahid_malik`/`la_mafhum_bila_waqi`).
التشغيل: python3 -I tahaqquq/test_hawass.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الحواسّ الخمس"
HASSA = {"بصر": "basar", "سمع": "sam", "ذوق": "dhawq", "لمس": "lams", "شم": "shamm"}

d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "hawass.tsv") if d else None
if not p or not os.path.exists(p):
    print("لم يُشغَّل (الجدول غير حاضر؛ عيّن MUDAA_DIR وفيه hawass.tsv)")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح"), m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
hala = m["hala"]
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 29, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"hassa": 5, "bud": 5, "tasmiya": 8, "khibra": 6, "rukhsa": 1, "sigha": 4}, {k: len(v) for k, v in by.items()}
assert [(r["ramz"], r["taraf1"], r["taraf2"]) for r in by["hassa"]] == \
    [("بصر", "العين", "مرئيّ"), ("سمع", "الأذن", "مسموع"), ("ذوق", "الفم", "مذوق"), ("لمس", "اليد", "ملموس"), ("شم", "الأنف", "مشموم")]
assert [r["ramz"] for r in by["bud"]] == ["حرارة", "صلابة", "قوام", "شدّة الصوت", "حجم"]
for r in by["khibra"][:5]:
    assert r["hassa"] in HASSA and r["qima"] and r["taraf2"] in [x["ramz"] for x in by["bud"]], r["ramz"]
assert [r["ramz"] for r in by["sigha"]] == ["صفة مشبّهة", "حال", "تمييز", "اسم تفضيل"]

src = {"لسان العرب": "lisan.txt", "قطر الندى": "qatr.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(لسان العرب|قطر الندى) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = 0
for line in open(p, encoding="utf-8"):
    for cell in line.rstrip("\n").split("\t"):
        s0 = None
        for s, ln, q in pat.findall(cell):
            if s:
                s0 = s
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
iqt_bayan = f"{iqt} اقتباسًا في سطره" if nusus else "لم تُفحص الاقتباسات (لسان العرب وقطر الندى غير حاضرين)"
ok += 1

# ٣
lean = open(os.path.join(ROOT, "Madlul", "Hawass.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


mujam = re.findall(r'⟨"([^"]+)", "([^"]+)"⟩', block("def mujam : List Tasmiya :=", "/-- شاهدُ قول المالك"))
assert mujam == [(r["ramz"], r["taraf1"]) for r in by["tasmiya"]], (mujam, [(r["ramz"], r["taraf1"]) for r in by["tasmiya"]])
khib = re.findall(r'⟨qawlMalik (\d+), \.(\w+), "([^"]+)", "([^"]+)", "([^"]+)"⟩', block("def khibrat : List Khibra :=", "/-- سجلٌّ"))
assert khib == [(r["ramz"], HASSA[r["hassa"]], r["taraf1"], r["taraf2"], r["qima"]) for r in by["khibra"][:5]], khib
abad = re.findall(r'⟨"([^"]+)", \[([^\]]*)\]⟩', block("def abad : List Bud :=", "theorem hajm_malmus_mari"))
abad = [(n, [x.strip(". ") for x in hs.split(",")]) for n, hs in abad]
assert abad == [(r["ramz"], [HASSA[h] for h in r["hassa"].split("؛")]) for r in by["bud"]], abad
adat = dict(re.findall(r'\| \.(\w+) => "([^"]+)"', block("def adat : Hassa → String", "theorem sawt_masmu")))
mahsus = dict(re.findall(r'\| \.(\w+) => "([^"]+)"', block("def mahsus : Hassa → String", "/-- أداةُ الحاسّة")))
for r in by["hassa"]:
    assert adat[HASSA[r["ramz"]]] == r["taraf1"] and mahsus[HASSA[r["ramz"]]] == r["taraf2"], r["ramz"]
ok += 1

# ٤
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        asma.add(ident)
for ident in asma:
    found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M) or \
        (ident.startswith(("Hassa.", "Thubut.")) and re.search(rf"\| {re.escape(ident.split('.', 1)[1])}\b", lean))
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٥ — الرخصة من بنية الجدول: لا «واقع-مختوم» في السجلّ ← لا مفهوم؛ خبرات المالك مطابقة للتسميات ← معلومة
waqi = [x for x in sijill if x["naw"] == "واقع-مختوم"]
tasmiyat = {(r["ramz"], r["taraf1"]) for r in by["tasmiya"]}
for r in by["khibra"][:5]:
    assert (r["qima"], r["taraf2"]) in tasmiyat, (r["ramz"], r["qima"], r["taraf2"])
    assert "معلومة" in r["bayan"], r["ramz"]
assert not waqi, "ظهر مودَع «واقع-مختوم» في السجلّ: يجب مراجعة حكم «معلومة» في الجدول وفي shawahid_malik"
assert re.search(r"^theorem shawahid_malik\b", lean, re.M) and re.search(r"^theorem la_mafhum_bila_waqi\b", lean, re.M)
ok += 1
print(f"{ok}/5 — 29/29 صفًّا ({hala})، {iqt_bayan}، المعجم والخبرات والأبعاد والحواسّ في Lean مطابقة، {len(asma)} اسمًا معرَّفًا، "
      f"خبرات المالك «معلومة» (لا واقع مختوم في السجلّ)")
