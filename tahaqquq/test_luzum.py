"""اختبارُ جدول اللزوم من شبكة المعاجم: `shabaka/jadwal_luzum.py` و`Madlul/JadwalLuzumData.lean` و`Madlul/JadwalLuzum.lean`.

١. نصُّ Lean (دائمًا): منشئاتُ `Naw` الخمسة؛ عددُ الصفوف في الترويسة = عددُها؛ مبرهناتُ الملفّ السبعَ عشرةَ بأسمائها في Audit.lean؛
   وقائلا `Madlul/JadwalLuzumNaql.lean` اسما `lisan.txt` و`maqayis.txt` المختومين في `mudaat/sijill.json` (طفرتُه P830)، ومبرهناتُه الخمسَ عشرةَ مدقّقة؛
   وبالمودَع: سنةُ وفاة صاحب كلّ معجمٍ في `wafat` هي `011.AuthorDIED` في رأس مودَعه (فحصٌ بالمودَع بلا طفرةٍ تخصّه: P831 يقتلها البناء).
٢. عيّنةٌ مضمَّنة (دائمًا، بلا مودَع): أسطرٌ حقيقيّةٌ منقولةٌ من اللسان والمقاييس بصيغة OpenITI، والمتوقَّعُ مكتوبٌ يدويًّا من قراءتها
   لا من المخرج: «الفهم: معرفتك الشيء بالقلب» جزءان (عرف، قلب)؛ «فهمت الشيء: عقلته وعرفته» مترادفان لا جزءان (R3-ب)؛
   «وبنو كتب: بطن، والله أعلم» بلا «علم» (FORMULA؛ و«أعلم» صيغةٌ لـ«علم» بسطر اللسان س235062 في العيّنة)؛ «لأن كتاب الله أمر…» بلا لزوم (TASMIYA؛ و«أمر» جذرٌ بأوّل مادّته س72211 في العيّنة)؛ «وسميت عقالا لأنها تعقل عن صاحبها الطلب»
   لزومٌ لـ«طلب» من «عقالا»؛ «الفاء والهاء والميم علم الشيء» أصلٌ «علم». تُقتل بها طفراتُ المستخرِج في CI بلا مودَع.
٣. المودَعان (إن حضرا في MUDAA_DIR ببصمتيهما المختومتين): الجدولُ كاملًا من المستخرِج؛ والصفوفُ المقروءةُ يدويًّا في هذه الجلسة
   بأسطرها حاضرة (EXPECT)، والمنفيّةُ غائبة (ABSENT)؛ وجدولُ Lean هو اختيارُ المولِّد من الجدول كاملًا بعينه (مطابَق)؛
   واختيارُ (A وB من الشبكة) تامّ فلا صلةَ بين جذرين من الشبكة خارج Lean (فـ`talab_la_mubashir` على الجدول كلّه)؛
   ولفظُ كلّ صفٍّ (غير الأصل) في سطره بعينه.
التشغيل: python3 -I tahaqquq/test_luzum.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "shabaka"))
import jadwal_luzum as J  # noqa: E402
import bina_luzum_lean as G  # noqa: E402
import hiss as H  # noqa: E402
import naht as N  # noqa: E402
import tarjih as T  # noqa: E402
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import tahwil_docx as TD  # noqa: E402

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


# ---------- ١. نصّ Lean ----------
naw_src = open(os.path.join(ROOT, "Madlul", "JadwalLuzumNaw.lean"), encoding="utf-8").read()
data_src = open(os.path.join(ROOT, "Madlul", "JadwalLuzumData.lean"), encoding="utf-8").read()
main_src = open(os.path.join(ROOT, "Madlul", "JadwalLuzum.lean"), encoding="utf-8").read()
audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
check(re.search(r"inductive Naw \| juz \| taraduf \| luzum \| kharij \| asl", naw_src), "منشئات Naw ليست الخمسة بترتيبها")
ROW = re.compile(r'⟨\.(\w+), "([^"]+)", "([^"]+)", \.(\w+), "([^"]+)", (\d+)⟩')
lean_rows = [(m, a, w, n, b, str(s)) for m, a, w, n, b, s in ROW.findall(data_src)]
mh = re.search(r"/-- (\d+) صفًّا", data_src)
check(mh and int(mh.group(1)) == len(lean_rows), "عدد الصفوف في الترويسة لا يطابق عددها")
THEOREMS = ["qawaninOf_shakl", "qaidaOf_shakl", "qaidaOf_mutadarrija", "asl_rutba_sifr", "luzum_min_taalil", "juz_min_hadd",
            "aslB_iff", "iltizam_min_taalil", "tadammun_min_juz", "la_iltizam_bila_taalil", "fahm_marifa_tadammun",
            "fahm_qalb_tadammun", "fahm_ilm_mutabaqa", "iqal_talab_iltizam", "fahm_la_iltizam", "silat_sitt", "talab_la_mubashir"]
for t in THEOREMS:
    check(f"theorem {t}" in main_src, f"المبرهنة {t} غائبة عن JadwalLuzum.lean")
    check(f"#print axioms JadwalLuzum.{t}\n" in audit, f"المبرهنة {t} غير مدقّقة في Audit.lean")
naht_src = open(os.path.join(ROOT, "Madlul", "Naht.lean"), encoding="utf-8").read()
isht_src = open(os.path.join(ROOT, "Madlul", "Ishtirak.lean"), encoding="utf-8").read()
for ns, src, ts in (("Naht", naht_src, "aakhidha_bihazz farid_nodup manhut_ithnan amthila_manhuta bulum_yukhalif"),
                    ("Ishtirak", isht_src, "ishtirak_iff taraduf_iff alaqa_tanazur alaqa_hasira shawahid_sibawayhi isqat_yahfaz "
                     "silat_malik_arba isqat_khams dars_la_yasil katiba_laysat_kitaba")):
    for t in ts.split():
        check(f"theorem {t}" in src, f"المبرهنة {t} غائبة عن {ns}.lean")
        check(f"#print axioms {ns}.{t}\n" in audit, f"المبرهنة {ns}.{t} غير مدقّقة في Audit.lean")
# النقلُ لصفوف الجدول (Madlul/JadwalLuzumNaql.lean): القائلُ اسمُ المعجم في سجلّ المودَعات بعينه، والمبرهناتُ مدقّقة.
naql_src = open(os.path.join(ROOT, "Madlul", "JadwalLuzumNaql.lean"), encoding="utf-8").read()
SIJILL = {x["milaf"]: x for x in json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]}
for mujam, milaf in (("lisan", "lisan.txt"), ("maqayis", "maqayis.txt")):
    mq = re.search(r'^  \| \.' + mujam + r' => "([^"]+)"$', naql_src, flags=re.M)
    check(mq and mq.group(1) == SIJILL[milaf]["ism"] and SIJILL[milaf]["hala"] == "مختوم",
          f"قائلُ {mujam} في JadwalLuzumNaql.lean ليس اسمَ {milaf} المختوم في mudaat/sijill.json")
for t in ("la_mutawatir mutadhafir_iff yashhad_saff la_daraja_bila_saff daraja_jisr yasluh_iff naw_hadd naw_ithnan iltizam_saff "
          "shahid_luzum_maqayis iltizam_jadwal shahid_hadd shahid_daraja shahid_qiraat shahid_fahm_juz_lisan").split():
    check(f"theorem {t}" in naql_src, f"المبرهنة {t} غائبة عن JadwalLuzumNaql.lean")
    check(f"#print axioms JadwalLuzum.{t}\n" in audit, f"المبرهنة JadwalLuzum.{t} غير مدقّقة في Audit.lean")

# ---------- ٢. العيّنة المضمَّنة ----------
LISAN_AYYINA = """### $ فهم: الفهم: معرفتك الشيء بالقلب. فهمه فهما وفهما وفهامة: علمه؛ الأخيرة
~~عن سيبويه. وفهمت الشيء: عقلته وعرفته.
### $ عرف: العرفان: العلم. والمعرفة: العرفان.
### $ قلب: القلب: الفؤاد.
### $ علم: العلم: نقيض الجهل.
~~بالعلم أي كان أعلم منه. وحكى اللحياني: ما كنت أراني أن أعلمه؛ قال
### $ أمر: الأمر: معروف، نقيض النهي. أمره به وأمره؛ الأخيرة عن كراع؛ وأمره
### $ جهل: الجهل: نقيض العلم.
### $ عقل: العقل: الحجر والنهى ضد الحمق. وعقل الشيء يعقله عقلا: فهمه.
### $ كتب: الكتاب: معروف. وبنو كتب: بطن، والله أعلم. ولا على موجب قضاء كتابه، لأن كتاب الله أمر بطاعة الرسول.
### $ بطن: البطن: خلاف الظهر.
### $ طلب: الطلب: محاولة وجدان الشيء وأخذه.""".split("\n")
MAQAYIS_AYYINA = """### | (فهم)
# الفاء والهاء والميم علم الشيء، كذا يقولون أهل اللغة.
### | (عقل)
# العين والقاف واللام أصل واحد منقاس مطرد، يدل عظمه على حبسة في الشيء.
# وأهل اللغة يقولون: إن الصدقة كلها عقال. يقال: استعمل فلان على عقال بني
~~فلان، أي على صدقاتهم. قالوا: وسميت عقالا لأنها تعقل عن صاحبها الطلب بها""".split("\n")

ml = J.mawadd_lisan(LISAN_AYYINA)
mq, _ = J.mawadd_maqayis(MAQAYIS_AYYINA)
Jd = J.Jadhr(ml + [[r, 0, []] for r in ("حبس",)] + mq)  # وورودُ «عقالا» من مادّة المقاييس نفسِها (المقاييس س26424–26425)
rl, _ = J.lisan_qadaya(Jd, ml)
rq, _ = J.maqayis_qadaya(Jd, mq)
got = {(r[0], r[1], r[2], r[3], r[4], str(r[5])) for r in rl + rq}
EXPECT_AYYINA = [
    ("lisan", "فهم", "الفهم", "juz", "عرف", "1"), ("lisan", "فهم", "الفهم", "juz", "قلب", "1"),
    ("lisan", "فهم", "وفهما", "taraduf", "علم", "1"),
    ("lisan", "فهم", "وفهمت", "taraduf", "عقل", "2"), ("lisan", "فهم", "وفهمت", "taraduf", "عرف", "2"),
    ("lisan", "علم", "العلم", "kharij", "جهل", "5"), ("lisan", "عقل", "يعقله", "taraduf", "فهم", "9"),
    ("maqayis", "فهم", "فهم", "asl", "علم", "2"), ("maqayis", "عقل", "عقالا", "luzum", "طلب", "6"),
]
for e in EXPECT_AYYINA:
    check(e in got, f"العيّنة: الصفّ المتوقَّع غائب {e}")
check(not any(r[1] == "فهم" and r[2] == "وفهمت" and r[3] == "juz" for r in got), "العيّنة: «عقلته وعرفته» قُرئ أجزاءً لا مترادفات (R3-ب)")
check(not any(r[1] == "كتب" and r[4] == "علم" for r in got), "العيّنة: «والله أعلم» دخل التفسير (FORMULA)")
check(not any(r[1] == "كتب" and r[3] == "luzum" for r in got), "العيّنة: «لأن» احتجاجٍ قُرئ لزومًا (TASMIYA)")

# الترجيح (Madlul/Tarjih.lean): نصُّ Lean، ومرآةُ بايثون على حالاتٍ مكتوبةٍ يدويًّا من ج3 س421–422 وس487
tarjih_src = open(os.path.join(ROOT, "Madlul", "Tarjih.lean"), encoding="utf-8").read()
for t in ("ashara_awjuh kull_zawj_marra khayr_min_khayr awla_la_yaksis bila_qarina_haqiqa qarina_tusrif la_ishtirak_maa_alaqa "
          "mushtarak_bila_qarina dars_dirasa dars_bila_siyaq sibawayhi_nabhani dars_laysa_mushtarak").split():
    check(f"theorem {t}" in tarjih_src, f"المبرهنة {t} غائبة عن Tarjih.lean")
    check(f"#print axioms Tarjih.{t}\n" in audit, f"المبرهنة Tarjih.{t} غير مدقّقة في Audit.lean")
HALAT = [  # (المعاني: اسم، أوّل، علاقة، قرينة) → المتوقَّع بنصّ النبهاني
    ([("ع", 1, 0, 0), ("د", 0, 1, 1)], ("mana", "د")),           # «إن كان معه قرينة … أعملناه فيه»
    ([("ع", 1, 0, 0), ("د", 0, 1, 0)], ("mana", "ع")),           # «وإلا أعملناه في الحقيقة»
    ([("ع", 1, 0, 0), ("ج", 1, 0, 0)], ("mushtarak", ["ع", "ج"])),  # المشترك «مفتقراً إلى قرينة»
    ([("ع", 1, 0, 1), ("ج", 1, 0, 0)], ("mana", "ع")),           # قرينةٌ تعيّن أحدَ معاني المشترك
    ([], ("laHukm", None)),
]
for ms, want in HALAT:
    check(T.tarjih([(a, bool(b), bool(c), bool(d)) for a, b, c, d in ms]) == want, f"مرآة الترجيح تخالف النصّ: {ms}")

# العيّنةُ لفصل المعاني (H1): صيغُ «فهمه فهما وفهما وفهامة: علمه» حدٌّ واحد فعقدةٌ واحدة؛ و«الفهم:» حدٌّ غيرُه
hs_a = []
J.lisan_qadaya(Jd, ml, hiss=hs_a)
U_a, uq_a, sil_a = H.bina(hs_a)
check(uq_a("فهم", J.qanun_sigha("فهما", "فهم")) == uq_a("فهم", J.qanun_sigha("وفهامة", "فهم")),
      "العيّنة: صيغُ الحدّ الواحد لم تتّحد عقدةً (H1)")
check(any(a == uq_a("فهم", "فهما") and b[0] == "علم" for a, _, b, _ in sil_a), "العيّنة: صلةُ «فهما ← علم» على العُقَد غائبة (H2)")
# النحت (N1) على عيّنةٍ مبنيّة: «بحتر» بثلاثيّين مختلفين منحوت، وبثلاثيٍّ واحدٍ غير منحوت
check(N.sannif("بحتر", {"بتر", "حتر"})[0] == "manhut" and N.sannif("بحتر", {"بتر"})[0] != "manhut", "العيّنة: معيار النحت N1 خطأ")

# ---------- ٣. المودَعان ----------
D = os.environ.get("MUDAA_DIR")
hadir = False
if D and all(os.path.exists(os.path.join(D, f)) for f in ("lisan.txt", "maqayis.txt")):
    S = J.sijill()
    hadir = all(J.basma(os.path.join(D, f)) == S[f]["sha256"] for f in ("lisan.txt", "maqayis.txt"))
    check(hadir, "مودَعٌ حاضرٌ بصمتُه لا تطابق السجلّ")
if hadir:
    L = open(os.path.join(D, "lisan.txt"), encoding="utf-8").read().split("\n")
    M = open(os.path.join(D, "maqayis.txt"), encoding="utf-8").read().split("\n")
    for mujam, src in (("lisan", L), ("maqayis", M)):
        mw = re.search(r'^  \| \.' + mujam + r' => (\d+)$', naql_src, flags=re.M)
        md = [x for x in src[:40] if x.startswith("#META# 011.AuthorDIED")]
        check(mw and len(md) == 1 and md[0].split("::")[1].strip() == mw.group(1),
              f"wafat {mujam} في JadwalLuzumNaql.lean ليست 011.AuthorDIED في رأس مودَعه")
    mlf = J.mawadd_lisan(L)
    mqf, _ = J.mawadd_maqayis(M)
    Jf = J.Jadhr(mlf)
    rows = J.lisan_qadaya(Jf, mlf)[0] + J.maqayis_qadaya(Jf, mqf)[0]
    full = {(r[0], r[1], r[2], r[3], r[4], str(r[5])) for r in rows}
    # مقروءةٌ يدويًّا في الجلسة (sed على الأسطر): اللسان س236711–236712، س209627، س24031، س115082؛ المقاييس س32736، س36420، س26425
    EXPECT = [
        ("lisan", "فهم", "الفهم", "juz", "عرف", "236711"), ("lisan", "فهم", "الفهم", "juz", "قلب", "236711"),
        ("lisan", "فهم", "وفهمت", "taraduf", "عقل", "236712"), ("lisan", "فهم", "وفهمت", "taraduf", "عرف", "236712"),
        ("lisan", "عقل", "يعقله", "taraduf", "فهم", "209627"), ("lisan", "كتب", "والمكتب", "taraduf", "علم", "24031"),
        ("lisan", "درس", "والمدارس", "juz", "كتب", "115082"), ("maqayis", "فهم", "فهم", "asl", "علم", "32736"),
        ("maqayis", "كتب", "كتب", "asl", "جمع", "36420"), ("maqayis", "عقل", "عقالا", "luzum", "طلب", "26425"),
    ]
    for e in EXPECT:
        check(e in full, f"المودَع: الصفّ المقروء يدويًّا غائب {e}")
    ABSENT = [lambda r: r[1] == "كتب" and r[4] == "علم" and r[5] == "24132", lambda r: r[1] == "كتب" and r[3] == "luzum" and r[5] == "24068"]
    for i, f in enumerate(ABSENT):
        check(not any(f(r) for r in full), f"المودَع: صفٌّ منفيّ حاضر (ABSENT[{i}])")
    sel = G.ikhtiyar([[str(x) for x in r[:6]] for r in rows])
    check([tuple(x) for x in sel] == lean_rows, "جدول Lean ليس اختيارَ المولِّد من الجدول كاملًا بعينه")
    shabaka = set(G.SHABAKA)
    kharij_lean = [r for r in full if r[1] in shabaka and r[4] in shabaka and r[1] != r[4] and r not in set(lean_rows)]
    check(not kharij_lean, f"صلةٌ بين جذرين من الشبكة خارج Lean: {kharij_lean[:3]}")
    # الجدولُ المشتقّ مسجَّلٌ «مرشّحًا»: إن حضر فبصمتُه بصمتُه في السجلّ (تُحدَّث ما دام مرشّحًا)
    tp = os.path.join(D, "luzum_mujam.tsv")
    if os.path.exists(tp):
        check(J.basma(tp) == S["luzum_mujam.tsv"]["sha256"] and S["luzum_mujam.tsv"]["hala"] in ("مرشح", "مختوم"),
              "luzum_mujam.tsv الحاضر بصمتُه غيرُ بصمته في السجلّ")
    # فصلُ المعاني على اللسان: IshtirakData.lean مطابقٌ لإعادة البناء، وصلاتٌ مقروءةٌ يدويًّا حاضرة
    hs_f = []
    J.lisan_qadaya(Jf, mlf, hiss=hs_f)
    Uf, uqf, silf = H.bina(hs_f)
    idata = open(os.path.join(ROOT, "Madlul", "IshtirakData.lean"), encoding="utf-8").read()
    silat_lean = re.findall(r'\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", (\d+)\)', idata)
    R7 = ["كتب", "درس", "قلم", "علم", "فهم", "طلب", "عقل"]
    seen, regen = set(), []
    for a, _, b, satr in silf:
        if a[0] in R7 and b[0] in R7 and a[0] != b[0] and (a, b) not in seen:
            seen.add((a, b))
            regen.append((a[0], a[1], b[0], b[1], str(satr)))
    check(regen == silat_lean, "IshtirakData.lean ليس إعادةَ البناء من اللسان بعينها")
    for satr, (ra, rb) in (("237932", ("قلم", "كتب")), ("237970", ("قلم", "كتب")), ("115082", ("درس", "كتب"))):
        check(any(x[4] == satr and x[0] == ra and x[2] == rb for x in silat_lean), f"صلةُ اللسان س{satr} غائبة عن IshtirakData")
    # النحت: ثلاثيّاتُ NahtData كلُّ ما في اللسان من إسقاطات الأمثلة، وكلمتا ابن فارس (مقروءتان يدويًّا: المقاييس س5289–5302) بينها
    ndata = open(os.path.join(ROOT, "Madlul", "NahtData.lean"), encoding="utf-8").read()
    th_lean = re.findall(r'"([^"]+)"', ndata.split("def thulathiyyat")[1].split("]")[0])
    T3f = {r for r, _, _ in mlf if len(r) == 3}
    th_regen = sorted({t for q in ("بحتر", "بحثر", "بعثق", "بلعم") for _, t in N.isqatat(q) if t in T3f})
    check(th_lean == th_regen, "NahtData.thulathiyyat ليس إسقاطاتِ الأمثلة المشهودةَ في اللسان بعينها")
    for t in ("بتر", "حتر", "بحث", "بثر", "بعق", "بثق", "بلع"):
        check(t in th_lean, f"ثلاثيُّ ابن فارس {t} غائبٌ عن NahtData")
    # شواهدُ «درس» في Tarjih.lean بأسطرها (مقروءةٌ يدويًّا)، وأسطرُ ج3 المستشهَد بها إن حضر a2.docx
    for src, satr, nass in ((M, 12989, "أصل واحد يدل على خفاء وخفض وعفاء"), (M, 12997, "ومن الباب درست القرآن"),
                            (L, 115033, "يدرس دروسا: عفا"), (L, 115055, "درسا ودراسة ودارسه، من ذلك، كأنه"),
                            (L, 115071, "ذللته بكثرة القراءة")):
        check(nass in src[satr - 1], f"شاهدُ «درس» ليس في سطره: {satr} «{nass}»")
    a2 = os.path.join(D, "a2.docx")
    if os.path.exists(a2) and J.basma(a2) == S["a2.docx"]["sha256"]:
        A2 = TD.fakra(a2).split("\n")
        for satr, nass in ((417, "إلى سبعة أقسام"), (421, "الأصل عدم الاشتراك"), (422, "يجوز استعمال المشترك في جميع معانيه"),
                           (434, "المشابهة"), (484, "احتمالات خمسة"), (485, "يؤخذ كل واحد مع ما بعده"),
                           (486, "النقل أولى من الاشتراك"), (487, "المجاز أولى من الاشتراك"), (493, "الإضمار مثل المجاز"),
                           (495, "التخصيص أولى من الإضمار"), (548, "ثم المعنى العرفي، ثم المعنى اللغوي")):
            check(nass in A2[satr - 1], f"ج3 س{satr} لا يحمل «{nass}»")
    for m, a, w, n, b, s in lean_rows:
        if n != "asl":
            src = L if m == "lisan" else M
            check(w in J.norm(J.satr(src[int(s) - 1])), f"لفظ الصفّ ليس في سطره: {(m, a, w, n, b, s)}")

if fails:
    print("\n".join(fails))
    print(f"جدول اللزوم: {len(fails)} خلل")
    sys.exit(1)
print(f"جدول اللزوم: مرّ (Lean {len(lean_rows)} صفًّا، العيّنة {len(EXPECT_AYYINA)} متوقَّعًا، المودَع {'حاضر' if hadir else 'غائب'})")
