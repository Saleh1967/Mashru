"""ضابطُ «قراءة الجملة بالعوامل» المجمَّد (Jisr/Tahlil.lean؛ القطر في المجال المعلن في wasf.md؛ hawkama/منهج_الضوابط.md §٤)، والسلسلةُ
فوقه (Nizam/Rabt.lean والأداتان tarkib وrabt).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمةُ المصدر فيه بصمةُ القطر.
٢. المولَّد: Jisr/TahlilDawabit.lean مخرجُ scripts/bina_dawabit_tahlil.py على cases.json بايتًا (والكلماتُ خلايا من `qari --khalaya`).
   ٢ب. الأداة `tarkib` على جملٍ بتوقّعٍ يدويّ لحكم الجملة وقراءتها، كلٌّ بسطره من القطر والألفية.
   ٢ج. الأداة `rabt` (بجدول لزومٍ فارغ) على جملٍ بتوقّعٍ يدويّ، كلٌّ بسطره: عاملُ الوحدة وحالتُها، والإسنادُ (ظاهرًا أو بارزًا أو مستترًا
       وجوبًا)، وقوّةُ الجملة، والإحالةُ إلى الحضور، ومفهومُ الغاية.
   ٢د. الأداة `rabt` على جدول لزومٍ مصنوع: اتّساقٌ لا توقّعٌ مستقلّ — أنواعُ الصفوف تُطبع تحت أسماء دلالاتها كما يعيّنها `Nizam.Rabt.iddiaOf`،
       ومرشَّحُ الجذر من خلايا الفعل، ولا يظهر صفُّ جذرٍ آخر.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ بعده
   يحمل بصمةَ ما قبله (qablaha). وآخرُها لبصمات الشفرة الحاليّة (SHIFRA)، وأعدادُه (ihsa، bil_fia، akhta، azwaj، rafd_qari) أعدادُ مبرهنات
   Jisr/TahlilQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`.
ويفحص، إن حضر القطرُ ببصمته في MUDAA_DIR (ولا طفرةَ له لأنّ CI بلا مودَع):
٥. الأسانيد: كلُّ `sanad.nass` في سطره بحذف البادئة وحدها، والسطرُ في النطاق؛ ثمّ فاحصُ المؤلّف نفسُه يخرج 0.

**بصمةُ الشفرة:** SHIFRA قائمةٌ ثابتةٌ من خمسة ملفّات (لا الإغلاقُ الذي يبلغه الحساب كما في test_athar_dabit.py)، و`Jisr/Tahlil.lean` منها؛
فكلُّ طفرةٍ فيه يقتلها فحصُ البصمة في ٣ أيًّا كانت إن لم يقتلها البناء. فطفراتُه (P1447–P1457) لا يُعدّ قتلُها بهذا الاختبار شاهدًا: والشاهدُ
قتلُها بالبناء (شواهدُ `Jisr/Tahlil.lean` ومبرهناتُ `Jisr/TahlilQiyas.lean`)، أو بفحصٍ في ٢ب أو ٢ج يسمّيه وصفُ طلب الدمج.
التشغيل: python3 -I tahaqquq/test_tahlil.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "tahlil"
SHIFRA = ["Jisr/Tahlil.lean", "Jisr/TahlilDabit.lean", "Qari/Main.lean", "Dal/QiraaTahsil.lean", "Dal/Tahsil.lean"]
QIYAS = JADHR / "Jisr/TahlilQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_tahlil.py"
BIN = JADHR / ".lake" / "build" / "bin"
QATR = ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d")
NITAQ = [(53, 67), (75, 78), (82, 85), (88, 90), (96, 100), (110, 114), (123, 126), (152, 158), (219, 224), (267, 268), (337, 343)]
NATIJA_1 = "46ca7c561d20c83d94c616e157c128e5de37203256f21a599ca8e9b812718025"  # natija_1.json كما أُودع أوّلًا (5c91dad)
NS = "Jisr.Tahlil.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_1", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "khataAdwar", "rafdQari", "khata"]
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]

fashal = []
najah = 0


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tahaqqaq(shart, risala):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(risala)


def majal_json(halat):
    """أعدادُ المجال بترتيب `majalAadad`: الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ، «لا حكم»، بديلان؛ ثمّ القراءاتُ البديلة؛ ثمّ ذواتُ
    الزوج؛ ثمّ الفئاتُ بترتيب FIAT."""
    hukm = [h["hukm"] for h in halat]
    mj = [len(halat)] + [hukm.count(d) for d in ("مقبول", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in hukm if isinstance(x, list))]
    mj += [sum(1 for h in halat if h["adwar"] and isinstance(h["adwar"][0], list))]
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


def shaghghil(ism, args, jumal, luzum=()):
    """يشغّل الأداة على ملفّ «مفتاح⇥جملة» ويُرجع (الرمز، الأسطر)؛ و`@luzum` جدولُ لزومٍ مصنوعٌ من صفوف `luzum`."""
    exe = BIN / ism
    if not exe.exists():
        return None, []
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "j.tsv"
        p.write_text("".join(f"{i}\t{s}\n" for i, s in enumerate(jumal)), encoding="utf-8")
        f = pathlib.Path(d) / "luzum.tsv"
        f.write_text("mujam\tA\tW\tqadiyya\tB\tsatr\tnass\n" + "".join("\t".join(r) + "\n" for r in luzum), encoding="utf-8")
        r = subprocess.run([str(exe)] + [str(f) if a == "@luzum" else a for a in args] + [str(p)], capture_output=True, text=True)
    return r.returncode, r.stdout.splitlines()


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq([(m["milaf"], m["sha256"]) for m in tajmid["masadir"]] == [QATR], "بصمةُ المصدر في tajmid.json غيرُ بصمة القطر")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/TahlilDawabit.lean ليس مخرجَ المولِّد: " + (r.stdout + r.stderr).strip()[-300:])

# ٢ب. الأداة tarkib: حكمُ الجملة وقراءتُها، والتوقّعاتُ يدويّةٌ من القطر: «ويجزم أيضا بلم» (L112)، والفاعلُ مرفوع (L219)، والمضارعُ
#     يُرفع خاليًا من ناصبٍ وجازم (L96)، و«ولا تلحقه علامة تثنية ولا جمع» (L220–221)، والمبتدأُ والخبرُ مرفوعان (L152)؛ ومثالُ القطر
#     للفاعل «ك"قام زيد" و "مات عمرو"» (L220؛ وواوُ «عمرو» لم تُبنَ، فـ«مَاتَ زَيْدٌ» مكانَه)، و«وذو تمام ما برفع يكتفي» (الألفية L217) فـ«كَانَ زَيْدٌ»
#     تامّة، و«وينصب ب"لن"» (القطر L96).
TARKIB = [("لَمْ يَكْتُبْ زَيْدٌ", "مقبول", "جازم فعل فاعل"), ("لَمْ يَكْتُبُ زَيْدٌ", "خطأ", ""),
          ("يَكْتُبُ زَيْدٌ", "مقبول", "فعل فاعل"), ("قَامُوا الرِّجَالُ", "خطأ", ""),
          ("الْوَلَدُ قَائِمٌ", "مقبول", "مبتدأ خبر"), ("الْوَلَدُ قَائِمًا", "خطأ", ""),
          ("مَاتَ زَيْدٌ", "مقبول", "فعل فاعل"), ("كَانَ زَيْدٌ", "مقبول", "فعل فاعل"), ("لَنْ يَصُونَ", "مقبول", "ناصب فعل")]
code, sutur = shaghghil("tarkib", [], [j for j, _, _ in TARKIB])
tahaqqaq(code == 0 and [s.split("\t") for s in sutur] == [[str(i), h, q] for i, (_, h, q) in enumerate(TARKIB)],
         f"tarkib: {sutur} غيرُ المتوقَّع اليدويّ")

# ٢ج. الأداة rabt: عاملُ الفعل بعد «لم» «لم» (القطر L112)، وصفُّها 58 في جدول العوامل المختوم؛ وعاملُ الفاعل الفعل (القطر L220 «ولا يتأخر
#     عامله عنه»)، وقوّةُ «لم» نفي، والمضارعُ بلا ناصبٍ ولا جازم مرفوعٌ بالتجرّد (L96)، ومفهومُ الغاية من «إلى» (الشخصيّة ج3، a2.txt س1088:
#     «فإذا قيد الحـكم بغـاية فإنه يدل على نفي الحكم فيما بعد الغاية»)، وضميرُ المخاطب
#     يحيل إلى الحضور (القطر L124).
code, sutur = shaghghil("rabt", ["@luzum"], ["لَمْ يَكْتُبْ زَيْدٌ", "يَكْتُبُ زَيْدٌ", "ذَهَبَ زَيْدٌ إِلَى الدَّارِ", "أَكْرَمَكَ"])
nass = "\n".join(sutur)
for juz in ["يَكْتُبْ\tفعل\tجزم\tالعامل: «لم» (صفّ 58 من جدول العوامل)",
            "زَيْدٌ\tفاعل\tرفع\tالعامل: الفعل «يَكْتُبْ»",
            "القوّة: خبرٌ منفيّ",
            "يَكْتُبُ\tفعل\tرفع\tالعامل: التجرّد من الناصب والجازم",
            "المفهوم (على الودائع المرشَّحة — تحتاج ختمًا): مخالفةُ الغاية «إِلَى الدَّارِ»",
            "فنفيُ الحكم فيما بعد الغاية (س1088)",
            "← الحضور"]:
    tahaqqaq(code == 0 and juz in nass, f"rabt: لا «{juz}» في مخرجه")
# و«وينصب ب"لن"» (L96)، و«وباللام ولا الطلبيتين» (L113) فقوّتُها طلب، و«يخفض الاسم … بإضافة إلى اسم» (L337–339)، والألفية L109
# «وكل مضمر له البنا يجب»؛ و«ويسكن آخره مع نون النسوة» (القطر L67)، و«مستتر كالمقدر وجوبا في نحو "أقوم"» (L124–125) فـ«نَكْتُبُ»
# للمتكلّم مثلُه، و«تقدر جميع الحركات في نحو "غلامي والفتى"» (L92).
code, sutur = shaghghil("rabt", ["@luzum"], ["لَنْ يَكْتُبَ زَيْدٌ", "لَا تَكْتُبْ", "كِتَابِي جَدِيدٌ", "يَكْتُبْنَ", "نَكْتُبُ"])
nass = "\n".join(sutur)
for juz in ["يَكْتُبَ\tفعل\tنصب\tالعامل: «لن» (صفّ 63 من جدول العوامل)",
            "تَكْتُبْ\tفعل\tجزم\tالعامل: «لا الناهية» (صفّ 60 من جدول العوامل)",
            "القوّة: إنشاء",
            "يْ\tمضاف_إليه\tمبنيّ في محلّ جرّ\tالعامل: إضافةُ «كِتَاْبِ» إليه",
            "جَدِيدٌ\tخبر\tرفع\tالعامل: المبتدأ «كِتَاْبِ»",
            "كِتَاْبِ\tمبتدأ\tرفع مقدَّرًا",
            "القوّة: خبرٌ منفيّ — «لن»",
            "يَكْتُبْنَ\tفعل\tمبنيّ في محلّ رفع",
            "والمسند إليه ضميرٌ مستتر (متكلّم مذكّر جمع) وجوبًا"]:
    tahaqqaq(code == 0 and juz in nass, f"rabt: لا «{juz}» في مخرجه")
# و«لا يفعل» نفيُ «يفعل» (الكتاب س9786)، والأمرُ «ويعرف بدلالته على الطلب» (القطر L59)، والضميرُ البارزُ المتّصل «ك"تاء" "قمت"» (L125–126)،
# والألفية L181 «ورفعوا مبتدأ بالابتدا ... كذاك رفع خبر بالمبتدا».
code, sutur = shaghghil("rabt", ["@luzum"], ["لَا يَكْتُبُ زَيْدٌ", "اكْتُبْ", "كَتَبْتُ", "الْوَلَدُ قَائِمٌ"])
nass = "\n".join(sutur)
for juz in ["القوّة: خبرٌ منفيّ — «لا» نافيةً",
            "القوّة: إنشاء — الأمرُ",
            "والمسند إليه ضميرٌ بارزٌ متّصل (متكلّم",
            "الْوَلَدُ\tمبتدأ\tرفع\tالعامل: الابتداء",
            "قَائِمٌ\tخبر\tرفع\tالعامل: المبتدأ «الْوَلَدُ»"]:
    tahaqqaq(code == 0 and juz in nass, f"rabt: لا «{juz}» في مخرجه")

# ٢د. الدلالةُ على جدول لزومٍ مصنوع — اتّساقٌ لا توقّعٌ مستقلّ: الترادفُ مطابقة، والأصلُ تضمّن، والتعليلُ التزام كما يعيّنها `Nizam.Rabt.iddiaOf`
#     (و`Madlul/JadwalLuzum.lean` `iltizam_min_taalil`)، والجذرُ «كتب» من «يَكْتُبْ» بلا سابقته (القطر L65–66).
LUZUM = [("lisan", "كتب", "الكتاب", "taraduf", "نسخ", "11", "-"), ("maqayis", "كتب", "كتب", "asl", "جمع", "22", "-"),
         ("lisan", "كتب", "كاتب", "luzum", "علم", "33", "-"), ("lisan", "قلم", "قلم", "luzum", "كتب", "44", "-")]
code, sutur = shaghghil("rabt", ["@luzum"], ["لَمْ يَكْتُبْ زَيْدٌ"], LUZUM)
nass = "\n".join(sutur)
for juz in ["الدلالة: «يَكْتُبْ» مرشَّحُ جذره كتب", "    مطابقة: نسخ (اللسان س11)", "    تضمّن: جمع (المقاييس س22)",
            "    التزام: علم (اللسان س33)"]:
    tahaqqaq(code == 0 and juz in nass, f"rabt: لا «{juz}» في مخرجه على الجدول المصنوع")
tahaqqaq("كتب (اللسان س44)" not in nass, "rabt: صفُّ «قلم» ظهر في دلالة «كتب»")

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع أوّلًا")
for k, p in enumerate(natayij):
    n = json.loads(p.read_text(encoding="utf-8"))
    tahaqqaq(n["tashghil"] == k + 1, f"{p.name}: رقمُ التشغيل فيه {n['tashghil']}")
    tahaqqaq(n["cases_sha256"] == tajmid["cases_sha256"], f"{p.name}: لغير الحالات المجمَّدة")
    if k > 0:
        qabl = natayij[k - 1]
        q = n.get("qablaha", {})
        tahaqqaq(q.get("milaf") == qabl.name and q.get("sha256") == sha(qabl), f"{p.name} لا يحمل بصمةَ {qabl.name}")


def tuples(nass):
    return [[int(x) for x in t.split(",")] for t in re.findall(r"⟨([\d, ]+)⟩", nass)]


akhir = json.loads(natayij[-1].read_text(encoding="utf-8")) if natayij else None
halat = json.loads((D / "cases.json").read_text(encoding="utf-8"))
if akhir:
    tahaqqaq({m: x["sha256"] for m, x in akhir["shifra"].items()} == {m: sha(JADHR / m) for m in SHIFRA},
             f"{natayij[-1].name} لغير الشفرة الحاليّة: تغيّر ملفٌّ من {SHIFRA} بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa \(natayij halat\) = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/TahlilQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    m = re.search(r"theorem (akhta\w*) :\s*akhta \(natayij halat\) = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ akhta بصيغتها")
    if m:
        lean_akhta = [[x for x in re.findall(r'"(\w+)"|\.(\w+)', t) for x in x if x]
                      for t in re.findall(r"\(([^()]*)\)", m.group(2))]
        tahaqqaq(lean_akhta == akhir["akhta"], f"{natayij[-1].name}: akhta {akhir['akhta']} غيرُ مبرهنة {m.group(1)} {lean_akhta}")
        tahaqqaq(NS + m.group(1) in akhir["lean"], f"مبرهنةُ الإخفاقات {m.group(1)} ليست في حقل lean من {natayij[-1].name}")
    m = re.search(r"theorem azwaj_1 :\s*\(azwaj halat\)\.length = (\d+) ∧ \(\(azwaj halat\)\.filter \(·\.2\.2\)\)\.length = (\d+) ∧\s*"
                  r"\(azwaj halat\)\.filter \(!·\.2\.2\) = \[(.*?)\] ∧\s*"
                  r"\(\(azwaj halat\)\.filter fun p => sawabHukm p\.1 && sawabHukm p\.2\.1\)\.length = (\d+) ∧ rafd halat = \[(.*?)\] := by",
                  qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj_1 بصيغتها في Jisr/TahlilQiyas.lean")
    if m:
        lam = [list(t) for t in re.findall(r'\("(\w+)", "(\w+)", false\)', m.group(3))]
        az = akhir.get("azwaj", {})
        tahaqqaq([int(m.group(1)), int(m.group(2)), lam, int(m.group(4))] ==
                 [az.get("jumla"), az.get("taghayyar"), az.get("lam_yataghayyar"), az.get("sawab_tarafayn")],
                 f"{natayij[-1].name}: azwaj {az} غيرُ مبرهنة azwaj_1")
        tahaqqaq(re.findall(r'"(\w+)"', m.group(5)) == akhir.get("rafd_qari"),
                 f"{natayij[-1].name}: rafd_qari غيرُ مبرهنة azwaj_1")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/TahlilQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat), f"{natayij[-1].name}: halat غيرُ ما في cases.json")
    tahaqqaq(sum(akhir["ihsa"].values()) == akhir["huqul_masula"], f"{natayij[-1].name}: مجموعُ ihsa غيرُ huqul_masula")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/TahlilQiyas.lean")
if m:
    tahaqqaq([int(x) for x in m.group(1).split(",")] == majal_json(halat), f"majal غيرُ ما في cases.json {majal_json(halat)}")

# ٥. الأسانيد على القطر
mdir = os.environ.get("MUDAA_DIR")
p = pathlib.Path(mdir) / QATR[0] if mdir else None
if p and p.exists() and sha(p) == QATR[1]:
    qatr = p.read_text(encoding="utf-8").split("\n")
    for h in halat:
        for s in h["sanad"]:
            n = s["satr"]
            tahaqqaq(any(a <= n <= b for a, b in NITAQ), f"سندُ {h['id']} خارجَ النطاق: س{n}")
            satr = re.sub(r"^(### \| |~~|# )", "", qatr[n - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في القطر س{n} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), str(p)], capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{sum(len(h['sanad']) for h in halat)} سندًا في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (القطرُ غائب)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط قراءة الجملة بالعوامل: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط قراءة الجملة بالعوامل والسلسلة: {najah}/{najah} — {len(halat)} حالةً و{akhir['huqul_masula']} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمات الشفرة الحاليّة{ziyada}")
