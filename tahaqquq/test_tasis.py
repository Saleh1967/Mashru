"""اختبارُ شبكة الدلالة: `Madlul/TasisDalala.lean` (الدورُ والتأسيس).

١. دائمًا، بلا مودَع: يقرأ صفوفَ `Madlul/JadwalLuzumData.lean`، ويحسب بنفسه بتنفيذٍ مستقلٍّ عن Lean معرِّفاتِ الجذر (صفوفُه غيرُ
   صفوف التعليل) والإغلاقَ بالتعريف (يُعرَّف المدخلُ إذا عُرفت معرِّفاتُه كلُّها):
   - من «كتب» وحده لا يُعرَّف إلّا «كتب» (`min_kataba`).
   - {فهم، عقل} دور: لكلٍّ منهما معرِّفٌ من الآخر (`dawr_fahm_aql`).
   - `awraq` في Lean = ألفاظُ الشبكة التي لا مدخلَ لها (بلا ترتيب)، و`asasAdna` = `awraq` ثمّ «عقل»، ويعرّف كلَّ الألفاظ، ولا يكفي إن
     نقص منه عضو.
   ومبرهناتُ الملفّ بأسمائها في Audit.lean.
   هذه الفحوصُ على Lean كاشفةٌ مع البناء لا قاتلةٌ وحدها: طفراتُ Lean (P841–P845، P853، P854) يقتلها البناءُ قبلها، ولا طفرةَ تخصّها.
   ومرآةُ الجدول الكامل `shabaka/tasis_dalala.py`، بتوقّعاتٍ مكتوبةٍ باليد على الصفوف الثلاثين: العقدُ (`uqad`) ألفاظُ الشبكة (P849)،
   والمعرِّفاتُ (T1) والإغلاقُ (T3) هما هما (P846، P848)، والبالغُ إلى «كتب» (T4) كتب ودرس وقلم (P850)، والنواةُ (T5) ثلاث عشرة (P851)،
   والأساسُ الجشع (T6) يعرّف العقدَ كلَّها ويضمّ ما أُعطي ولا ينقص عن 18 (P852)، وبحرف المقال (T3م) يعرّف «عقل» وحده العقدَ كلَّها
   ولا يعرّف الأساسُ الفارغ إلّا ما سوى فهم وعقل (P855)؛ وأساسُ «معروف» (T2) على عناوين مصنوعة: يُقبل «معروف»
   قبل «،» وعلى سطرين، ويُردّ غيرُه (P847).
٢. بالمودَع (إن حضر MUDAA_DIR فيه lisan.txt وmaqayis.txt وa2.txt وa3.txt ببصماتها في السجلّ؛ والنصّان المحوَّلان ببصمة `nass_muhawwal`):
   الاقتباساتُ الموسومة {{ملفّ:سطر}} في الملفّ في أسطرها. فحصٌ بالمودَع بلا طفرةٍ تخصّه.
التشغيل: python3 -I tahaqquq/test_tasis.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


data = open(os.path.join(ROOT, "Madlul", "JadwalLuzumData.lean"), encoding="utf-8").read()
src = open(os.path.join(ROOT, "Madlul", "TasisDalala.lean"), encoding="utf-8").read()
audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
ROW = re.compile(r'⟨\.(\w+), "([^"]+)", "([^"]+)", \.(\w+), "([^"]+)", (\d+)⟩')
rows = ROW.findall(data)
check(len(rows) == 30, f"صفوف الجدول {len(rows)} لا 30")

# معرِّفاتُ الجذر: الجذورُ الأخرى في صفوفه غيرِ صفوف التعليل
DEF = {}
for m, a, w, n, b, s in rows:
    if n != "luzum":
        DEF.setdefault(a, []).append(b)
madakhil = [a for m, a, w, n, b, s in rows]
kalimat = madakhil + [b for m, a, w, n, b, s in rows if n != "luzum"]


def iqfal(G):
    K = list(G)
    while True:
        new = [v for v in madakhil if v not in K and v in DEF and all(d in K for d in DEF[v])]
        new = list(dict.fromkeys(new))
        if not new:
            return K
        K += new


check(iqfal(["كتب"]) == ["كتب"], f"الإغلاقُ من «كتب» {iqfal(['كتب'])}")
check(all(any(d in ("فهم", "عقل") for d in DEF[v]) for v in ("فهم", "عقل")), "{فهم، عقل} ليس دورًا في الجدول")

m = re.search(r"def awraq : List String :=\s*\[([^\]]*)\]", src)
awraq_lean = re.findall(r'"([^"]+)"', m.group(1)) if m else []
check(re.search(r'def asasAdna : List String := awraq \+\+ \["عقل"\]', src) is not None, "asasAdna ليس awraq ثمّ «عقل»")
asas = awraq_lean + ["عقل"]
awraq = list(dict.fromkeys(b for v in madakhil for b in DEF.get(v, []) if b not in DEF))
check(sorted(awraq_lean) == sorted(awraq) and len(set(asas)) == len(asas), f"awraq في Lean ليس أوراقَ الشبكة: {awraq_lean}")
K = iqfal(asas)
check(all(x in K for x in kalimat), "asasAdna لا يعرّف كلَّ الألفاظ")
for g in asas:
    rest = [x for x in asas if x != g]
    check(g not in iqfal(rest), f"asasAdna ليس أدنى: يكفي بلا {g}")

NAMES = ("dawr_mawqufa mawqufa_la_yuarraf dawr_la_yuarraf ghayr_muarraf_mawqufa muarraf_iff la_tarif_bila_asl bila_madkhal "
         "asl_kafin_iff iqfal_sahih asl_fi_iqfal thabit_tamm iqfal_iff dawrB_sahih kharij_thabit").split()
for t in NAMES:
    check(f"theorem {t}" in src and f"#print axioms TasisDalala.{t}\n" in audit, f"المبرهنة {t} غائبة أو غيرُ مدقّقة")
for t in ("defJ_madakhil defJ_ghayr_farigh la_tarif_bila_asl_defJ dawr_fahm_aql fahm_aql_la_yuarraf min_kataba "
          "kafin_yahwi asasAdna_kafin asasAdna_asghar asasAdna_adna maqal_aql_kafin maqal_dawr").split():
    check(f"theorem {t}" in src and f"#print axioms TasisDalala.Jadwal.{t}\n" in audit, f"المبرهنة {t} غائبة أو غيرُ مدقّقة")

# مرآةُ الجدول الكامل
sys.path.insert(0, os.path.join(ROOT, "shabaka"))
import tasis_dalala as td  # noqa: E402

Dm = td.muarrifat([(a, n, b) for m, a, w, n, b, s in rows])
check(Dm == {k: set(v) for k, v in DEF.items()}, "مرآةُ المعرِّفات (T1) لا تطابق")
for G in (["كتب"], asas, ["عقل"], []):
    check(td.iqfal(Dm, set(G)) == set(iqfal(G)), f"مرآةُ الإغلاق (T3) من {G} لا تطابق")
R30 = [(a, n, b) for m, a, w, n, b, s in rows]
N30 = td.uqad(R30)
check(N30 == set(kalimat) and len(N30) == 23, f"عقدُ المرآة {len(N30)} ليست ألفاظَ الشبكة")
check(td.bulugh(Dm, {"كتب"}) == {"كتب", "درس", "قلم"}, f"البالغُ إلى «كتب»: {td.bulugh(Dm, {'كتب'})}")
NAWAT = {"عقل", "فهم", "علم", "حبس", "قرب", "عرف", "قلب", "بعد", "جعل", "سءل", "قبل", "ءثر", "ميز"}
check(td.nawat(Dm, N30) == NAWAT, f"النواة: {td.nawat(Dm, N30)}")
check(td.iqfal_maqal(Dm, N30, {"عقل"}) == N30 and td.iqfal_maqal(Dm, N30, set()) == N30 - {"فهم", "عقل"},
      f"بحرف المقال: {td.iqfal_maqal(Dm, N30, set())}")
for G in (set(), {"عقل"}, {"كتب", "درس"}):
    B = td.jashi(Dm, N30, G)
    check(N30 <= td.iqfal(Dm, B) and G <= B and len(B) >= 18, f"الأساسُ الجشع من {G}: {B}")
HEADS = ["### $ كتب: الكتاب: معروف، والجمع كتب.",
         "### $ فهم: الفهم: معرفتك الشيء بالقلب.",
         "### $ شيب: الشيب:",
         "~~معروفٌ، قليله وكثيره.",
         "### $ درب: الدرب: معروف عند العرب.",
         "### $ ءرض: الأرض: التي عليها الناس، معروف."]
check(td.asas_maruf(HEADS) == [("كتب", 1), ("شيب", 3)], f"أساسُ «معروف» (T2) على العناوين المصنوعة: {td.asas_maruf(HEADS)}")

# ٢. الاقتباساتُ في أسطرها
hadir = False
D = os.environ.get("MUDAA_DIR")
if D:
    BASMA = {}
    for x in json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]:
        BASMA[x["milaf"]] = x["sha256"]
        if "nass_muhawwal" in x:
            BASMA[x["nass_muhawwal"]["milaf"]] = x["nass_muhawwal"]["sha256"]

    def basma(p):
        return hashlib.sha256(open(p, "rb").read()).hexdigest()
    MILAFAT = ("lisan.txt", "maqayis.txt", "a2.txt", "a3.txt")
    paths = {f: os.path.join(D, f) for f in MILAFAT}
    if all(os.path.exists(p) for p in paths.values()):
        ok = all(basma(p) == BASMA[f] for f, p in paths.items())
        check(ok, "مودَعٌ حاضرٌ بصمتُه لا تطابق السجلّ")
        if ok:
            hadir = True
            satr = {f: open(p, encoding="utf-8").read().split("\n") for f, p in paths.items()}
            wasm = re.findall(r"\{\{([\w.]+):(\d+)\}\} «([^»]+)»", src)
            check(len(wasm) >= 10, f"الاقتباساتُ الموسومة {len(wasm)}")
            for f, n, q in wasm:
                check(f in satr and q in satr[f][int(n) - 1], f"«{q}» ليس في {f} س{n}")

if fails:
    print("\n".join(fails))
    print(f"شبكة الدلالة: {len(fails)} خلل")
    sys.exit(1)
print(f"شبكة الدلالة: مرّ (30 صفًّا، الأساسُ الأدنى {len(asas)}، المودَع {'حاضر' if hadir else 'غائب'})")
