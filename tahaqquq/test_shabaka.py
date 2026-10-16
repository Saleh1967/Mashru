"""اختبار جدول العلاقات المودَع (شبكة الأجناس والأفعال والصفات) ومطابقة `Madlul/Shabaka.lean` له (الشبكة `shabaka`/`shabaka'`، وأسماء
التحويلات والقوانين).

يُشغَّل حين يحضر المودَع (MUDAA_DIR وفيه alaqat.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ المودَع هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه «مختوم».
٢. توقّعاتٌ مستقلّة: 23 صفًّا — 9 أصول (قابليّتان، مفعولية، سببية، 3 حالات، تسمية، قانون معجميّ)، 8 أساليب (لازم، متعدٍّ، مطاوعة،
   تعديتان، مشاركة، طلب، مجهول)، 6 قوانين (ش0–ش5)؛ الحالاتُ الثلاث تطابق عمود hala في القطعة الثانية (إن حضرت)؛ القابليّتان
   تطابقان عمود qabiliyyat في القطعة الأولى (إن حضرت: «شرب» فيهما)؛ وكلُّ اقتباسٍ «…» بسطره من لسان العرب/المخصّص/الكتاب/الألفية
   موجودٌ في سطره في المودَع الحاضر بلفظه (والمصدرُ محمولٌ على ما بعده بـ «؛ س…»؛ وما كان من ج3 — مرشّح — لا يُفحص هنا).
٣. Lean من النصّ (لا عبر Lean): قوائمُ `shabaka` (qabiliyyat، mafooliyyat، sababiyyat، halat، tasmiyat) و`shabaka'.qawaninMujam`
   تُقرأ من Madlul/Shabaka.lean وتطابق صفوفَ الأصول زوجًا زوجًا بترتيبها.
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر، أو منشئٌ معلَن
   `Luzum.lazim`/`Luzum.mutaaddi`) في Madlul/Shabaka.lean؛ وما بدأ بـ `shabaka.`/`shabaka'.` لا يُقبل إلّا حقلًا من حقول `Shabaka`.
٥. قرارُ «السائل شراب» من بنية الجدول وحدها (لا من غياب شاهدٍ مضادّ — م13): القانونُ الوحيد الذي نتيجتُه «ذو الحالة موصوف» هو ش5
   ومقدّمتُه قانونٌ معجميّ، والقانونُ المعجميّ مرآتُه الشبكةُ المعجمية `shabaka'` وحدها — فبلا إيداعه «لا حكم» ومعه مرخَّص؛ ويُطابَق
   بوجود `jinsSifa_la_yurakhkhas`/`sail_sharab_marfud`/`sail_sharab_bil_mujam` في Lean.
التشغيل: python3 -I tahaqquq/test_shabaka.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول العلاقات"

d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "alaqat.tsv") if d else None
if not p or not os.path.exists(p):
    print("لم يُشغَّل (المودَع غير حاضر؛ عيّن MUDAA_DIR وفيه alaqat.tsv)")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["hala"] == "مختوم" and m["naw"] == "معلومات-سابقة", m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 23, len(rows)
asl = [r for r in rows if r["naw"] == "asl"]
usl = [r for r in rows if r["naw"] == "uslub"]
qan = [r for r in rows if r["naw"] == "qanun"]
assert (len(asl), len(usl), len(qan)) == (9, 8, 6), (len(asl), len(usl), len(qan))
assert [r["ramz"] for r in asl] == ["قابلية", "قابلية", "مفعولية", "سببية", "حالة", "حالة", "حالة", "تسمية", "قانون-معجمي"]
assert [r["ramz"] for r in usl] == ["لازم", "متعدٍّ", "مطاوعة", "تعدية", "تعدية", "مشاركة", "طلب", "مجهول"]
assert sorted(r["ramz"] for r in qan) == ["ش0", "ش1", "ش2", "ش3", "ش4", "ش5"]
for r in usl:
    assert r["luzum"] in ("لازم", "متعدٍّ") and r["uslub"] in ("مجرّد", "مطاوعة", "تعدية", "مشاركة", "طلب", "مجهول"), r["ramz"]
halat = [(r["taraf1"], r["taraf2"]) for r in asl if r["ramz"] == "حالة"]
assert halat == [("الماء", "سائل"), ("الزئبق", "سائل"), ("الحديد", "جامد")]
p2 = os.path.join(d, "ajnas_jamad.tsv")
if os.path.exists(p2):
    h2 = {r["jins"]: r["hala"] for r in tsv(p2)}
    for j, h in halat:
        assert h2[j[2:]] == h, (j, h, h2.get(j[2:]))
p1 = os.path.join(d, "ajnas.tsv")
if os.path.exists(p1):
    q1 = {r["jins"]: r["qabiliyyat"].split("؛") for r in tsv(p1)}
    for r in asl:
        if r["ramz"] == "قابلية":
            assert r["taraf2"] in q1[r["taraf1"][2:]], (r["taraf1"], r["taraf2"])

src = {"لسان العرب": "lisan.txt", "المخصّص": "mukhassas.txt", "الكتاب": "sibawayhi.txt", "الألفية": "alfiyya.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(لسان العرب|المخصّص|الكتاب|الألفية|ج3) )?س(\d+)(?:–\d+)?: «([^»]+)»")
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
iqt_bayan = f"{iqt} اقتباسًا في سطره" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣
lean = open(os.path.join(ROOT, "Madlul", "Shabaka.lean"), encoding="utf-8").read()
blk = lean[lean.index("def shabaka : Shabaka :="):lean.index("def shabaka' : Shabaka :=")]
lists = {k: re.findall(r'\("([^"]+)", "([^"]+)"\)', re.search(rf"{k} := (\[[^\]]*\])", blk).group(1))
         for k in ("qabiliyyat", "mafooliyyat", "sababiyyat", "halat", "tasmiyat")}
blk2 = lean[lean.index("def shabaka' : Shabaka :="):lean.index("def qaida : Qaida Qawl")]
lists["qawaninMujam"] = re.findall(r'\("([^"]+)", "([^"]+)"\)', re.search(r"qawaninMujam := (\[[^\]]*\])", blk2).group(1))
ramzOf = {"قابلية": "qabiliyyat", "مفعولية": "mafooliyyat", "سببية": "sababiyyat", "حالة": "halat", "تسمية": "tasmiyat",
          "قانون-معجمي": "qawaninMujam"}
expected = {}
for r in asl:
    expected.setdefault(ramzOf[r["ramz"]], []).append((r["taraf1"], r["taraf2"]))
assert expected == lists, (expected, lists)
ok += 1

# ٤
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        asma.add(ident)
fields = set(re.findall(r"^\s+(\w+) : List \(String × String\)", lean, re.M))
for ident in asma:
    if ident.startswith(("shabaka.", "shabaka'.")):
        # لا يُقصّ الاسمُ إلّا إلى حقلٍ من حقول Shabaka (قوائم الأصول)
        found = ident.split(".", 1)[1] in fields
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M) or \
            ident in ("Luzum.lazim", "Luzum.mutaaddi")
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
assert len(asma) >= 20, len(asma)
ok += 1

# ٥ — قرار «السائل شراب» من بنية الجدول وحدها (لا من غياب شاهد): القانونُ الوحيد الذي نتيجتُه «ذو الحالة موصوف» هو ش5 ومقدّمتُه
# «قانون-معجمي»؛ والقانونُ المعجميّ الوحيد مرآتُه shabaka'.qawaninMujam (لا shabaka) — فبلا إيداعه «لا حكم»، ومعه مرخَّص.
qm_rows = [r for r in asl if r["ramz"] == "قانون-معجمي"]
assert qm_rows and all(r["mirat_lean"] == "shabaka'.qawaninMujam" for r in qm_rows), "القانون المعجميّ في الشبكة المعجمية وحدها"
assert lists["qawaninMujam"] == [(r["taraf1"], r["taraf2"]) for r in qm_rows] and "qawaninMujam" not in blk, "shabaka بلا قانون معجميّ"
sh5 = [r for r in qan if r["ramz"] == "ش5"]
assert len(sh5) == 1 and sh5[0]["taraf1"] == "قانون-معجمي" and "ذو الحالة" in sh5[0]["bayan"], sh5
assert all("ذو الحالة" not in r["bayan"] or r["ramz"] in ("ش5", "ش0") for r in qan), "لا قانون آخر نتيجته ذو الحالة"
sh0 = [r for r in qan if r["ramz"] == "ش0"]
assert len(sh0) == 1 and "لا قانونَ" in sh0[0]["bayan"]
assert re.search(r"^theorem jinsSifa_la_yurakhkhas\b", lean, re.M) and re.search(r"^theorem sail_sharab_marfud\b", lean, re.M) and \
    re.search(r"^theorem sail_sharab_bil_mujam\b", lean, re.M)
ok += 1
print(f"{ok}/5 — 23/23 صفًّا، {iqt_bayan}، الشبكة في Lean مطابقة للأصول، {len(asma)} اسمًا معرَّفًا، قرار «السائل شراب»: لا حكم بلا قانون معجميّ مودَع ومرخَّص معه")
