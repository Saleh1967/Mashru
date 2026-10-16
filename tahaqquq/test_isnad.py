"""اختبار جدول الرابطة الإسنادية (مرشّح حتّى يُختم) ومطابقة `Aql/Isnad.lean` له (الأنماط الثلاثة، الرابط «من سببه»، المستقرّ، الجملة على المرساة).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه isnad.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها (منشئات الجملة، قاعدة الكبرى، زمن الوصف، موضع الصغرى،
أسماء المبرهنات) وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 18 صفًّا — 3 أنماط (الصغرى، الكبرى، الظرفية)، 2 رتبة، 3 قواعد، 7 شواهد، 3 فحص لجدول المالك؛ 48 اقتباسًا (الكتاب 46، لسان
   العرب 2) بعدٍّ يدويّ؛ وكلُّ «…» في عمود الشاهد إمّا قولُ المالك/قراءة البنّاء/تعيينه وإمّا على نمط «المصدر سN: «…»» موجودٌ في سطره في المودَع
   الحاضر بلفظه.
٣. Lean من النصّ (لا عبر Lean): `Jumla` منشئاتُه الأربعة sughra/kubra/zarfiyya/mansukha؛ قاعدةُ الكبرى في `yastaghni`: «الخبر كلامٌ ومن سببه»
   (`yastaghni j && (sabab j).contains d.ramz`)؛ `zamanArad` للوصف `none`؛ `mawdiInda` للصغرى `r.huna`؛ `Rutba` hakim/mahkum.
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Isnad.lean باسمه الكامل، والمنقوطُ منشئٌ في فضاء نوعه أو تعريفٌ منقوط (`Arad.naql`)؛ و«(لم يُبنَ)»
   يُقبل إعلانًا.
٥. ادّعاءاتُ الغياب تُفحص على مادّة الكتاب الحاضر كلّها **موصولةَ الأسطر** (لا على الأسطر وحدها): «بظرفه» 0، «ومستقره» 0، «إخبار عن الاسم» 0،
   «زيد ضربت أخاه» 0؛ و«زيد أبوه منطلق» 1 موصولًا و0 على الأسطر (مقطوع بين س9929 وس9930)؛ وعلامتا الصفحتين 23 و61 في س240 وس662؛ و«ههنا عمرو»
   في س5731؛ وصفوفُ الفحص الثلاثة تذكر ذلك.
التشغيل: python3 -I tahaqquq/test_isnad.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الرابطة الإسنادية"

lean = open(os.path.join(ROOT, "Aql", "Isnad.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def munshiat_of(typ):
    return re.findall(r"\| (\w+)", block(f"inductive {typ}", "deriving"))


def fahs_lean():
    assert munshiat_of("Jumla") == ["sughra", "kubra", "zarfiyya", "mansukha"], munshiat_of("Jumla")
    assert "| .kubra d j => yastaghni j && (sabab j).contains d.ramz" in block("def yastaghni", "\n\n")
    assert "| .wasf _ => none" in block("def zamanArad", "\n\n")
    assert "| .sughra _ _ => r.huna" in block("def mawdiInda", "\n\n")
    assert re.search(r"^inductive Rutba \| hakim \| mahkum", lean, re.M)
    for name in ("hakim_mahkum", "shatr_laysa_kalaman", "sughra_kalam", "zarfiyya_kalam", "nasikh_yahfaz", "kubra_bila_sabab_la_kalam",
                 "kubra_kalam", "khabar_kalam", "wasf_la_zaman", "sughra_huna", "thabat_naql_arad", "thabat_naql_mawdi", "mustaqarr_jiha",
                 "shawahid_kalam", "sabab_yufarriq", "hahuna_la_jiha", "thamma_dhaka"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "isnad.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه isnad.tsv)؛ فحص نصّ Lean: منشئات الجملة وقاعدة الكبرى وزمن الوصف وموضع الصغرى "
          "والمبرهنات المسمّاة موجودة")
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


def mawsul(lines):
    """نصُّ المودَع موصولَ الأسطر: تُحذف بادئات OpenITI وعلاماتُ الصفحات والمخطوط، وتُوصل الأسطر بمسافة."""
    out = []
    for l in lines:
        l = re.sub(r"^(~~|# \| |# |### \|+ ?)", "", l)
        l = re.sub(r"PageV\d+P\d+|ms\d+", "", l)
        out.append(l.strip())
    return re.sub(r"\s+", " ", " ".join(out))


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
assert {k: len(v) for k, v in by.items()} == {"namat": 3, "rutba": 2, "qaida": 3, "shahid": 7, "fahs": 3}, {k: len(v) for k, v in by.items()}
assert [r["ramz"] for r in by["namat"]] == ["الصغرى", "الكبرى", "الظرفية"] and [r["ramz"] for r in by["rutba"]] == ["الحاكم", "المحكوم"]
src = {"الكتاب": "sibawayhi.txt", "لسان العرب": "lisan.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(الكتاب|لسان العرب) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kull = 0
bimasdar = {}
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
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            bimasdar[s0] = bimasdar.get(s0, 0) + 1
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
assert kull == 48 and bimasdar == {"الكتاب": 46, "لسان العرب": 2}, (kull, bimasdar)   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا)
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull}" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣
fahs_lean()
assert "Jumla.sughra" in by["namat"][0]["mirat_lean"] and "Jumla.kubra" in by["namat"][1]["mirat_lean"] and \
    "Jumla.zarfiyya" in by["namat"][2]["mirat_lean"]
assert "Rutba.hakim" in by["rutba"][0]["mirat_lean"] and "Rutba.mahkum" in by["rutba"][1]["mirat_lean"]
ok += 1

# ٤
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

# ٥
f1, f2, f3 = by["fahs"]
assert "ص23" in f1["qima"] and "س240" in f1["shahid"] and "PageV01P023" in f1["shahid"]
assert "س9929" in f2["qima"] and "0 على السطر" in f2["qima"] and "1 على النصّ الموصول" in f2["qima"] and "«زيد ضربت أخاه» 0" in f2["qima"]
assert "«إخبار عن الاسم بظرفه ومستقره» 0" in f3["qima"] and "«بظرفه» 0" in f3["shahid"] and "«ومستقره» 0" in f3["shahid"]
ghiyab = "لم يُفحص (الكتاب غير حاضر)"
if "الكتاب" in nusus:
    k = nusus["الكتاب"]
    kk = mawsul(k)
    for ibara in ("بظرفه", "ومستقره", "إخبار عن الاسم", "زيد ضربت أخاه"):
        assert kk.count(ibara) == 0, (ibara, kk.count(ibara))
    assert kk.count("زيد أبوه منطلق") == 1 and sum(l.count("زيد أبوه منطلق") for l in k) == 0
    assert "كان زيد" in k[9929 - 1] and k[9930 - 1].startswith("~~أبوه منطلق")
    assert "PageV01P023" in k[240 - 1] and "PageV01P061" in k[662 - 1] and "PageV01P060" in k[647 - 1]
    assert "هذا باب المسند والمسند إليه" in k[234 - 1] and "ومثله ثم زيد وههنا عمرو" in k[5731 - 1]
    ghiyab = "ادّعاءات الغياب الأربعة مفحوصة على الكتاب موصول الأسطر، و«زيد أبوه منطلق» 1 موصولًا (س9929–9930)، وعلامتا ص23 وص61 في سطريهما"
ok += 1
print(f"{ok}/5 — 18/18 صفًّا ({hala})، {iqt_bayan}، منشئات الجملة وقاعدة الكبرى وزمن الوصف وموضع الصغرى في Lean مطابقة، {len(asma)} اسمًا "
      f"معرَّفًا، {ghiyab}")
