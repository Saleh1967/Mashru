"""اختبار جدول الرابطة الإسنادية (مرشّح حتّى يُختم) ومطابقة `Aql/Isnad.lean` له (الأنماط الثلاثة، الرابط «من سببه»، المستقرّ، الجملة على المرساة).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه isnad.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها (منشئات الجملة، قاعدة الكبرى، زمن الوصف، موضع الصغرى،
أسماء المبرهنات) وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 21 صفًّا — 3 أنماط (الصغرى، الكبرى، الظرفية)، 2 رتبة، 3 قواعد، 10 شواهد، 3 فحص لجدول المالك؛ 72 اقتباسًا (الكتاب 63، مغني
   اللبيب 3، قطر الندى 4، لسان العرب 2) بعدٍّ يدويّ؛ وكلُّ «…» في عمود الشاهد إمّا قولُ المالك/قراءة البنّاء/تعيينه وإمّا على نمط «المصدر سN: «…»»
   موجودٌ في سطره في المودَع الحاضر بلفظه.
٣. Lean من النصّ (لا عبر Lean): `Jumla` منشئاتُه الأربعة sughra/kubra/zarfiyya/mansukha؛ `Juz` أربعة؛ `Arad` فعلٌ بمفعولٍ ووصفٌ بفاعل؛ قاعدةُ الكبرى
   في `yastaghni`: «الخبر كلامٌ ومن سببه» (`yastaghni j && (sabab j).contains d.ramz`)، والوصفُ بفاعلٍ في `sababWasf` (`f.damir == some d.ramz`)؛
   `zamanArad` للوصف `none`؛ `mawdiInda` للصغرى `r.huna`؛ `Rutba` hakim/mahkum.
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Isnad.lean باسمه الكامل، والمنقوطُ منشئٌ في فضاء نوعه أو تعريفٌ منقوط (`Arad.naql`)؛ و«(لم يُبنَ)»
   يُقبل إعلانًا.
٥. ادّعاءاتُ الغياب والأعداد تُفحص على مادّة المودَعات الحاضرة كلّها **موصولةَ الأسطر**: في الكتاب «بظرفه» 0، «ومستقره» 0، «إخبار عن الاسم» 0،
   «زيد ضربت أخاه» 0، و«زيد أبوه منطلق» 1 موصولًا و0 على الأسطر (مقطوع بين س9929 وس9930)، و«من سببه» 33 موضعًا في 24 سطرًا، و«ملتبس به» في س653
   وس1161، و«زيد أخوك» في ستّة أسطر بعينها و7 مواضع موصولًا (السابع س1446 مقطوع بعلامة مخطوط)؛ وأعدادُ الثلاث في القطر والمغني والألفية والجنى الداني والمخصّص واللسان والتاج والمقاييس كما في
   صفّ الفحص الثالث؛ وعلامتا الصفحتين 23 و61 في س240 وس662؛ و«ههنا عمرو» في س5731؛ وصفوفُ الفحص الثلاثة تذكر ذلك.
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
    assert munshiat_of("Juz") == ["ilayh", "arad", "khabar", "mustaqarr"], munshiat_of("Juz")
    assert "| fiil (ramz : Nat) (t : Int) (u : Wahda) (maful : Option Dhat)" in lean and "| wasf (ramz : Nat) (fail : Option Dhat)" in lean
    assert "| .kubra d j => yastaghni j && (sabab j).contains d.ramz" in block("def yastaghni", "\n\n")
    assert "| .wasf _ (some f) => f.damir == some d.ramz" in block("def sababWasf", "\n\n")
    assert "| .wasf _ _ => none" in block("def zamanArad", "\n\n")
    assert "| .sughra _ _ => r.huna" in block("def mawdiInda", "\n\n")
    assert re.search(r"^inductive Rutba \| hakim \| mahkum", lean, re.M)
    for name in ("ajza_ithnan", "hakim_mahkum", "sughra_kalam", "wasf_bi_fail", "zarfiyya_kalam", "nasikh_yahfaz", "kubra_kalam",
                 "kubra_bila_sabab_la_kalam", "khabar_kalam", "wasf_la_zaman", "sughra_huna", "thabat_naql_arad", "thabat_naql_mawdi",
                 "mustaqarr_jiha", "shawahid_kalam", "sabab_yufarriq", "hahuna_la_jiha", "thamma_dhaka"):
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
assert len(rows) == 21, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"namat": 3, "rutba": 2, "qaida": 3, "shahid": 10, "fahs": 3}, {k: len(v) for k, v in by.items()}
assert [r["ramz"] for r in by["namat"]] == ["الصغرى", "الكبرى", "الظرفية"] and [r["ramz"] for r in by["rutba"]] == ["الحاكم", "المحكوم"]
src = {"الكتاب": "sibawayhi.txt", "لسان العرب": "lisan.txt", "مغني اللبيب": "mughni.txt", "قطر الندى": "qatr.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(الكتاب|لسان العرب|مغني اللبيب|قطر الندى) )?س(\d+)(?:–\d+)?: «([^»]+)»")
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
assert kull == 72 and bimasdar == {"الكتاب": 63, "مغني اللبيب": 3, "قطر الندى": 4, "لسان العرب": 2}, (kull, bimasdar)   # توقّع مستقلّ (عدٌّ يدويّ)
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
assert "ص23" in f1["qima"] and "س240" in f1["shahid"] and "PageV01P023" in f1["shahid"] and "7 مواضع موصولًا" in f1["shahid"]
assert "س9929" in f2["qima"] and "0 على السطر" in f2["qima"] and "1 على النصّ الموصول" in f2["qima"] and "«زيد ضربت أخاه» 0" in f2["qima"]
assert "بتمامها 0" in f3["qima"] and "و4 في التاج" in f3["shahid"] and "و2 في المخصّص و3 في اللسان و2 في التاج و2 في المقاييس" in f3["shahid"]
assert by["shahid"][5]["ramz"] == "زيد ضربت أخاه" and "قراءة مثال المالك بالرفع" in by["shahid"][5]["qima"], "«زيد ضربت أخاه» قراءة معلَنة بالرفع"
ghiyab = "لم يُفحص (الكتاب غير حاضر)"
if "الكتاب" in nusus:
    k = nusus["الكتاب"]
    kk = mawsul(k)
    for ibara in ("بظرفه", "ومستقره", "إخبار عن الاسم", "زيد ضربت أخاه", "زيد أخوك وضرب"):
        assert kk.count(ibara) == 0, (ibara, kk.count(ibara))
    assert kk.count("زيد أبوه منطلق") == 1 and sum(l.count("زيد أبوه منطلق") for l in k) == 0
    assert "كان زيد" in k[9929 - 1] and k[9930 - 1].startswith("~~أبوه منطلق")
    assert kk.count("من سببه") == 33 and sum(1 for l in k if "من سببه" in l) == 24
    assert [i + 1 for i, l in enumerate(k) if "ملتبس به" in l] == [653, 1161]
    assert [i + 1 for i, l in enumerate(k) if "زيد أخوك" in l] == [3653, 4000, 5738, 5739, 11938, 11945] and kk.count("زيد أخوك") == 7
    assert "زيد ضربته فلزمته الهاء" in k[841 - 1] and "وأعبد الله" in k[1139 - 1] and k[1140 - 1].startswith("~~ضربت أخاه")
    assert "PageV01P023" in k[240 - 1] and "PageV01P061" in k[662 - 1] and "PageV01P060" in k[647 - 1] and "PageV01P022" in k[227 - 1]
    assert "هذا باب المسند والمسند إليه" in k[234 - 1] and "ومثله ثم زيد وههنا عمرو" in k[5731 - 1]
    assert "هذا باب ما أجرى مجرى ليس" in k[607 - 1] and "هذا باب إنما وأنما" in k[9907 - 1]
    # أعداد الثلاث في سائر المودَعات الحاضرة، موصولةَ الأسطر — توقّع مستقلّ (عُدّت بأداة في الجلسة)
    mutawaqqa = {"qatr": (0, 0, 0), "mughni": (0, 0, 0), "alfiyya": (0, 0, 0), "janadani": (0, 0, 0), "mukhassas": (0, 2, 0),
                 "lisan": (0, 3, 0), "taj": (4, 2, 2), "maqayis": (0, 2, 0)}
    ghaib = []
    for f, (a, b, c) in mutawaqqa.items():
        fp = os.path.join(d, f + ".txt")
        if not os.path.exists(fp):
            ghaib.append(f)
        else:
            jj = mawsul(open(fp, encoding="utf-8").read().split("\n"))
            assert (jj.count("بظرفه"), jj.count("ومستقره"), jj.count("إخبار عن الاسم")) == (a, b, c), (f, jj.count("بظرفه"), jj.count("ومستقره"), jj.count("إخبار عن الاسم"))
            assert jj.count("إخبار عن الاسم بظرفه ومستقره") == 0
    ghiyab = ("ادّعاءات الغياب والأعداد مفحوصة على الكتاب وسائر المودَعات الحاضرة موصولة الأسطر"
              + (f" (غابت: {'، '.join(ghaib)})" if ghaib else "") + "، و«زيد أبوه منطلق» 1 موصولًا (س9929–9930)، وعلامتا ص23 وص61 في سطريهما")
ok += 1
print(f"{ok}/5 — 21/21 صفًّا ({hala})، {iqt_bayan}، منشئات الجملة وقاعدة الكبرى وزمن الوصف وموضع الصغرى في Lean مطابقة، {len(asma)} اسمًا "
      f"معرَّفًا، {ghiyab}")
