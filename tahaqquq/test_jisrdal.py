"""اختبار جدول الجسر إلى الدالّ (مرشّح حتّى يُختم) ومطابقة `Jisr/JisrDal.lean` له (الإعراب بالحروف والتقدير وجرّ الممنوع بالفتحة والمجهول).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه jisr_dal.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 18 صفًّا — 12 بابًا، 4 قواعد، 2 شاهدان؛ 54 اقتباسًا من قطر الندى بأسطرها (عدٌّ يدويّ)؛ وكلُّ «…» في عمود الشاهد إمّا
   قراءةُ البنّاء/تعيينه وإمّا على نمط «قطر الندى سN: «…»» موجودٌ في سطره في المودَع الحاضر بلفظه.
٣. Lean من النصّ (لا عبر Lean): `Bab` منشئاتُه الاثنا عشر (بترتيب Lean؛ وأبوابُ الجدول الاثنا عشر بترتيب الجدول — ترتيبان معلَنان)، و`HukmDal` ثلاثيّ
   (muayyan/muhtamal/laHukm)؛ في `hukm`: الأسماء الستّة بالواو رفعًا والألف نصبًا والياء جرًّا، والممنوع فتحتُه محتمَلةٌ نصبًا وجرًّا، والأمثلة بالنون
   رفعًا؛ وفي `majhul`: كسرٌ للماضي وفتحٌ للمضارع، ورفضُ حرف المدّ الساكن.
٤. أرقامُ الحوامل في JisrDal.lean (ا، ي، ن، و) هي مواضعُها في جدول المخارج `Dal/Makharij.hawamil` المقروء نصًّا — توقّعٌ مستقلّ من الملفّ
   الآخر لا من JisrDal نفسه.
٥. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في JisrDal.lean باسمه الكامل (والمنقوطُ منشئٌ في فضاء نوعه).
٦. شواهدُ Lean (`shawahid` تُقرأ نصًّا): 24 شاهدًا، 23 منها بسطرٍ من القطر و1 مبنيّ (السطر 0)؛ وكلُّ شاهدٍ بسطرٍ لفظُه (بلا حركات) في ذلك
   السطر من المودَع الحاضر — توقّعٌ على المودَع لا على Lean.
التشغيل: python3 -I tahaqquq/test_jisrdal.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الجسر إلى الدالّ"

lean = open(os.path.join(ROOT, "Jisr", "JisrDal.lean"), encoding="utf-8").read()
makharij = open(os.path.join(ROOT, "Dal", "Makharij.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def munshiat_of(typ):
    return re.findall(r"\| (\w+)", block(f"inductive {typ}", "deriving"))


def shawahid_lean():
    """(اللفظ، السطر) لكلّ شاهد في `def shawahid` نصًّا."""
    return [(m.group(1), int(m.group(2))) for m in re.finditer(r"⟨\"([^\"]+)\", (\d+), \.", block("def shawahid :", "\n\n"))]


def fahs_lean():
    assert munshiat_of("Bab") == ["mufrad", "filSahih", "maqsur", "manqus", "mudafLiYa", "sitta", "muthanna", "jamMudhakkar", "jamMuannath",
                                  "mamnu", "amthila", "mudariMutall"], munshiat_of("Bab")
    assert munshiat_of("HukmDal") == ["muayyan", "muhtamal", "laHukm"]
    h = block("def hukm ", "\n\n")
    assert "else if harf c == waw then .muayyan .raf else if harf c == alif then .muayyan .nasb" in h
    assert "else if harf c == ya then .muayyan .jarr else .laHukm" in h
    assert "| .mamnu false => match hala c with\n      | 1 => .muayyan .raf | 0 => .muhtamal [.nasb, .jarr] | _ => .laHukm" in h
    assert "| .amthila => if harf c == nun then .muayyan .raf else if maddSakin c then .muhtamal [.nasb, .jazm] else .laHukm" in h
    assert "| .maqsur => if harf c == alif && hala c == 3 then .muhtamal [.raf, .nasb, .jarr] else .laHukm" in h
    mj = block("def majhul ", "\n\n")
    assert "(if madi then 2 else 0)" in mj and "l.any maddSakin = true then none" in mj
    # ٤: الحوامل من جدول المخارج نصًّا
    m = re.search(r"def hawamil : List Char :=\s*\[(.*?)\]", makharij, re.S)
    hawamil = re.findall(r"'(.)'", m.group(1))
    assert len(hawamil) == 29, len(hawamil)
    for name, ch in (("alif", "ا"), ("ya", "ي"), ("nun", "ن"), ("waw", "و")):
        val = int(re.search(rf"^def {name} : Nat := (\d+)", lean, re.M).group(1))
        assert val == hawamil.index(ch), (name, val, hawamil.index(ch))
    for name in ("harf_fakk", "hawamil_huruf", "asliyya_tuqabil", "mufrad_halaIrab", "mufrad_tanwin", "maqsur_la_yuayyin", "mudaf_la_yuayyin",
                 "yayn_la_yufarriq", "manqus_fatha_zahira", "mamnu_fatha", "mamnu_bi_al", "amthila_nun", "sitta_hamil", "farIyaBab_malik",
                 "farIya_kull", "shawahid_hukm", "muwafiq_farIya", "majhul_huruf", "majhul_tul", "majhul_dun_116", "majhul_marfud",
                 "shawahid_majhul", "intilaq_wasl"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name
    # ٦: الشواهد نصًّا
    sh = shawahid_lean()
    assert len(sh) == 24, len(sh)
    assert sum(1 for _, n in sh if n) == 23 and sum(1 for _, n in sh if not n) == 1, sh
    assert [w for w, n in sh if not n] == ["بالزيدين"]
    return sh


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "jisr_dal.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه jisr_dal.tsv)؛ فحص نصّ Lean: الأبواب والحكم الثلاثيّ وقواعد الستّة والممنوع "
          "والأمثلة والمجهول وأرقام الحوامل من جدول المخارج والمبرهنات المسمّاة و24 شاهدًا (23 بسطر) موجودة")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


def segs(cell):
    out, cur, depth, i = [], "", 0, 0
    while i < len(cell):
        c = cell[i]
        if c == "«":
            depth += 1
        elif c == "»":
            depth -= 1
        if depth == 0 and cell.startswith("؛ ", i):
            out.append(cur)
            cur = ""
            i += 2
            continue
        cur += c
        i += 1
    out.append(cur)
    return out


HARAKAT = re.compile("[ً-ْ]")

sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح"), m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
hala = m["hala"]
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 18, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"bab": 12, "qaida": 4, "shahid": 2}, {k: len(v) for k, v in by.items()}
qatr = None
qp = os.path.join(d, "qatr.txt")
if os.path.exists(qp):
    qatr = open(qp, encoding="utf-8").read().split("\n")
pat = re.compile(r"(?:(قطر الندى) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kull = 0
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("قول المالك", "قراءة البنّاء", "تعيين البنّاء")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج النمط فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 == "قطر الندى", (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            if qatr is not None:
                assert q in qatr[int(ln) - 1], (ln, q[:40])
                iqt += 1
assert kull == 54, kull   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا)
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull}" if qatr is not None else "لم تُفحص الاقتباسات (القطر غير حاضر)"
ok += 1

# ٣، ٤
sh = fahs_lean()
babs = [r["ramz"] for r in by["bab"]]
assert babs == ["المفرد المنصرف", "الفعل الصحيح", "الأسماء الستّة", "المثنّى", "جمع المذكر السالم", "جمع المؤنث السالم", "الممنوع من الصرف",
                "الأمثلة الخمسة", "المضارع المعتلّ الآخر", "المقصور", "المنقوص", "المضاف إلى الياء"], babs
ok += 2   # ٣ و٤ كلاهما في fahs_lean

# ٥
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        if ident != "(لم يُبنَ)":
            asma.add(ident)
for ident in asma:
    if "." in ident:
        typ, c = ident.split(".", 1)
        found = (f"inductive {typ}" in lean and c in munshiat_of(typ)) or re.search(rf"^def {re.escape(ident)}\b", lean, re.M)
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M)
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٦: صفّ الشواهد يذكر 14 معيَّنًا و10 محتمَلة = 24، و23 بلفظ القطر؛ وكلّ شاهدٍ بسطرٍ لفظُه في سطره من المودَع
s_row = by["shahid"][0]
assert "المعيَّن 14" in s_row["qima"] and "المحتمَل 10" in s_row["qima"] and "23 بلفظ القطر" in s_row["qima"], s_row["qima"]
fi_satr = 0
if qatr is not None:
    for w, n in sh:
        if n:
            assert HARAKAT.sub("", w) in qatr[n - 1], ("شاهد ليس في سطره", w, n)
            fi_satr += 1
    assert fi_satr == 23
ok += 1
print(f"{ok}/6 — 18/18 صفًّا ({hala})، {iqt_bayan}، الأبواب الاثنا عشر والحكم الثلاثيّ وقواعد الستّة والممنوع والأمثلة والمجهول في Lean مطابقة، "
      f"أرقام الحوامل من جدول المخارج، {len(asma)} اسمًا معرَّفًا، {fi_satr} شاهدًا بلفظ القطر في سطره من 24")
