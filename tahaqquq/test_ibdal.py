"""ضابطُ «الإبدال: الواوُ والياءُ في الكلمة» المجمَّد، من ألفيّة ابن مالك (hawkama/منهج_الضوابط.md §٤؛ Jisr/IbdalAlfiyya.lean).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمتا المصدرين فيه بصمتا الألفيّة والكتاب.
٢. المولَّد: Jisr/IbdalAlfiyyaDawabit.lean مخرجُ scripts/bina_dawabit_ibdal.py على cases.json بايتًا (والكلمةُ خلايا من `qari --khalaya`).
٢ب. والمولِّدُ على كلمةٍ بـ«أل» («الْمُوقِنُ»؛ لا كلمةَ بـ«أل» في الحالات، فلا يكشف ٢ إسقاطَ علامتها): خلاياها وعلامتاها مكتوبةٌ باليد هنا.
٢ج. خلايا شواهد الأبيات (`shawahid` في Jisr/IbdalAlfiyya.lean، منقولةٌ باليد) مخرجُ `qari --khalaya` لكلماتها؛ فحصُ نصٍّ يقرأ القائمةَ من Lean.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله. وآخرُها لبصمات الشفرة الحاليّة (SHIFRA: القواعدُ والمقارنةُ وطبقةُ القواعد والكلمةُ وقارئُها والقانونُ
   وخلاياه)، وأعدادُه (ihsa،
   bil_fia، akhta، azwaj، rafd_qari) هي أعدادُ مبرهنات Jisr/IbdalAlfiyyaQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك،
   ومبرهنةُ akhta مسمّاةٌ فيه.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat في آخر سجلّ، وعددُ حقول
   كلّ فئةٍ في natija_fia يساوي حالاتها (حقلٌ واحدٌ لكلّ حالة).
ويفحص، إن حضر المودَعان (MUDAA_DIR/alfiyya.txt وsibawayhi.txt ببصمتيهما)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ `sanad.nass` في سطره من الألفيّة بحذف البادئة وحدها («# »)، والسطرُ في النطاق؛ ثمّ فاحصُ المؤلّف نفسُه
   (`fahs_cases.py <MUDAA_DIR>`) يخرج 0.

الطفرات وقاتلُها، كلٌّ بفحصها المسمّى وحده إلّا ما يُذكر (وقاتلُ كلٍّ بـtafrat_juz.py على الشجرة المودَعة في طلب الدمج):
- ١: P1189 (بصمةُ المواصفة في tajmid.json)، P1190 (بصمةُ الألفيّة فيه). ٢: P1221 (المولِّد يغيّر رأسَ المولَّد). ٢ب: P1191 (المولِّد يُسقط
  علامة «أل»).
- ٣، على آخر سجلّ (natija_4.json؛ وسجلٌّ بعده يُلزم نقلَها إليه، وإلّا قتلتها السلسلةُ وحدها، إلّا P1193 وP1194 وP1218 فمعها
  فحصُها): P1193 (tashghil)، P1194 (cases_sha256)، P1195 (huqul_masula)، P1196 (ihsa، والمجموعُ باقٍ)، P1197 (bil_fia)، P1198 (akhta)، P1199 (ترتيبُ حقل lean)، P1200 (azwaj)، P1201 (rafd_qari)، P1202 (halat)، P1217 (بصمةُ الشفرة)، P1218 (بصمةُ ما قبله).
- ٣ و٤، على Jisr/IbdalAlfiyyaQiyas.lean وتُبنى: P1203 (مبرهنةُ akhta ثانيةً باسمٍ لا يسمّيه السجلّ)، P1213 (`natija` بلا أعدادها)، P1215
  (`akhta_1` بلا قائمتها)، P1216 (`natija_fia` خاصّة)، P1222 (`azwaj_1` بلا عددها)، P1214 (`majal` بلا أعدادها، ٤).
- البناء: P1204–P1210 وP1212 وP1219 وP1223 على قواعد Jisr/IbdalAlfiyya.lean (`shawahid_hukm`، ومبرهناتُ «حيثما وقع»
  و`madd_la_ghayrMamnu`، ومبرهناتُ Jisr/IbdalAlfiyyaQiyas.lean، و`alif_mayyit`).
**ما لا يُعزل أو يقع على الفحص نفسه:** P1192 (خليّةٌ في شاهدٍ لا تغيّر حكمَه، ٢ج) على Jisr/IbdalAlfiyya.lean، وهو من الشفرة المسجَّلة بصمتُها
(SHIFRA)، فيقتلها فحصُ البصمة في ٣ مع فحصها. وP1211 تطفّر عبارةَ المبرهنة `alif_mayyit` لا الشفرة. وP1220 تطفّر الفحصَ نفسَه (الحسابَ من
cases.json في majal_json، ٤): قتلُها لا يدلّ أنّ الفحص يلتقط عيبًا في المفحوص، ولا نظيرَ له على المفحوص يُبنى (cases.json مجمَّدٌ ببصمته،
وأعدادُ `majal` تقتلها Lean). وبلا طفرة: تتالي أرقام السجلّات (أسماؤها لا تطفّرها الأداة)، والمرساةُ NATIJA_1 وسلسلةُ ما قبل الأخير (طفرةُ
سجلٍّ قديمٍ تقتلها السلسلة، ومعها المرساةُ في natija_1.json)، ومجموعُ حقول الفئات في `natija_fia` (أعدادُها تقتلها Lean،
وcases.json مجمَّد)، وأسماءُ الملفّات في SHIFRA وBASMAT.
التشغيل: python3 -I tahaqquq/test_ibdal.py
"""
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "ibdal"
SHIFRA = ["Jisr/IbdalAlfiyya.lean", "Jisr/IbdalAlfiyyaDabit.lean", "Jisr/TabaqatQawaid.lean", "Dal/Jumla.lean", "Qari/Main.lean",
          "Dal/QiraaTahsil.lean", "Dal/Tahsil.lean", "SLGE/Law.lean", "Dal/Khaliya.lean"]
QIYAS = JADHR / "Jisr/IbdalAlfiyyaQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_ibdal.py"
QARI = JADHR / ".lake" / "build" / "bin" / "qari"
BASMAT = {"ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0"),
          "كتاب": ("sibawayhi.txt", "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625")}
NITAQ = [(1216, 1217), (1222, 1222), (1224, 1224), (1225, 1226), (1238, 1239)]
NATIJA_1 = "59dfa8c564903a8d7d5831b98d73bfac59d239bea71940af8d9cf402cff88fc9"  # natija_1.json كما أُودع أوّلًا
NS = "Jisr.IbdalAlfiyya.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_1", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "rafdQari", "khata"]
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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/IbdalAlfiyyaQiyas.lean: الحالات؛ ثمّ المتوقَّع: ممنوع، غير ممنوع، «لا حكم»، بديلان؛
    ثمّ ذواتُ الزوج؛ ثمّ الفئاتُ بترتيب FIAT."""
    hukm = [h["hukm"] for h in halat]
    mj = [len(halat)] + [hukm.count(d) for d in ("ممنوع", "غير_ممنوع", "لا_حكم")]
    mj += [sum(1 for x in hukm if isinstance(x, list))]
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq([(m["milaf"], m["sha256"]) for m in tajmid["masadir"]] == [BASMAT["ألفية"], BASMAT["كتاب"]],
         "بصمتا المصدرين في tajmid.json غيرُ بصمتي الألفيّة والكتاب")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/IbdalAlfiyyaDawabit.lean ليس مخرجَ المولِّد: " + (r.stdout + r.stderr).strip()[-300:])

# ٢ب. المولِّدُ على «الْمُوقِنُ»، والخلايا باليد من جدول الحوامل (Dal/Makharij.lean: ق 7، ل 13، ن 14، م 27، و 28) والخليّةُ 4×الحامل+الحالة
#     (فتحة 0، ضمّة 1، كسرة 2، سكون 3): لْ 55، مُ 109، وْ 115، قِ 30، نُ 57؛ وهمزةُ الوصل ليست خليّة، فالعلامتان (الوصل، أل) صادقتان.
if QARI.exists():
    spec = importlib.util.spec_from_file_location("bina_dawabit_ibdal", BINA)
    bina = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bina)
    natija_al = bina.khalaya([{"id": "T1", "kalima": "الْمُوقِنُ"}])
    tahaqqaq(natija_al == {"T1": "some ⟨[55, 109, 115, 30, 57], true, true⟩"},
             f"المولِّدُ على «الْمُوقِنُ»: {natija_al}")
else:
    tahaqqaq(False, "القارئ غيرُ مبنيّ (lake build qari)")

# ٢ج. خلايا شواهد الأبيات في Jisr/IbdalAlfiyya.lean منقولةٌ باليد: هي مخرجُ `qari --khalaya` لكلماتها، بترتيبها.
nass_qawaid = (JADHR / "Jisr/IbdalAlfiyya.lean").read_text(encoding="utf-8")
m = re.search(r"def shawahid : List \(String × List Nat × Hukm\) := \[(.*?)\]\n\n", nass_qawaid, re.S)
shawahid = re.findall(r'\("([^"]+)", \[([\d, ]+)\],', m.group(1)) if m else []
if shawahid and QARI.exists():
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "s.tsv"
        p.write_text("".join(f"{i}\t{w}\n" for i, (w, _) in enumerate(shawahid)), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(p)], capture_output=True, text=True)
    qari = []
    for satr in r.stdout.splitlines():
        ajza = satr.split("\t")
        qari.append([int(x) for x in ajza[2].split(";")[0].split(",")] if len(ajza) == 3 and ajza[1] == "QABUL" else None)
    lean = [[int(x) for x in c.split(",")] for _, c in shawahid]
    tahaqqaq(r.returncode == 0 and lean == qari, f"خلايا `shawahid` غيرُ مخرج qari --khalaya: {lean} مقابل {qari}")
else:
    tahaqqaq(False, "لا قائمةَ `shawahid` في Jisr/IbdalAlfiyya.lean أو القارئ غيرُ مبنيّ")

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
        tahaqqaq(n.get("qablaha", {}).get(qabl.name) == sha(qabl), f"{p.name} لا يحمل بصمةَ {qabl.name}: سجلٌّ قديمٌ تغيّر")


def tuples(nass):
    return [[int(x) for x in t.split(",")] for t in re.findall(r"⟨([\d, ]+)⟩", nass)]


akhir = json.loads(natayij[-1].read_text(encoding="utf-8")) if natayij else None
halat = json.loads((D / "cases.json").read_text(encoding="utf-8"))
mj = majal_json(halat)
if akhir:
    tahaqqaq({m: x["sha256"] for m, x in akhir["shifra"].items()} == {m: sha(JADHR / m) for m in SHIFRA},
             f"{natayij[-1].name} لغير الشفرة الحاليّة: تغيّر ملفٌّ من {SHIFRA} بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa \(natayij halat\) = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/IbdalAlfiyyaQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    adad_fia = [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    tahaqqaq(len(tt) == 5 and [sum(t) for t in tt] == adad_fia,
             f"حقولُ الفئات في natija_fia {[sum(t) for t in tt]} غيرُ حالات cases.json {adad_fia}")
    m = re.search(r"theorem (akhta\w*) :\s*akhta \(natayij halat\) = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ akhta بصيغتها")
    if m:
        lean_akhta = [[x for x in re.findall(r'"(\w+)"|\.(\w+)', t) for x in x if x]
                      for t in re.findall(r"\(([^()]*)\)", m.group(2))]
        tahaqqaq(lean_akhta == akhir["akhta"], f"{natayij[-1].name}: akhta {akhir['akhta']} غيرُ مبرهنة {m.group(1)} {lean_akhta}")
        tahaqqaq(NS + m.group(1) in akhir["lean"], f"{natayij[-1].name}: حقلُ lean لا يسمّي {m.group(1)}")
    m = re.search(r"theorem azwaj_1 :\s*\(azwaj halat\)\.length = (\d+) ∧ \(\(azwaj halat\)\.filter \(·\.2\.2\)\)\.length = (\d+) ∧\s*"
                  r"\(azwaj halat\)\.filter \(!·\.2\.2\) = \[(.*?)\] ∧\s*"
                  r"\(\(azwaj halat\)\.filter fun p => sawabHukm p\.1 && sawabHukm p\.2\.1\)\.length = (\d+) ∧ rafd halat = \[(.*?)\] := by",
                  qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj_1 بصيغتها في Jisr/IbdalAlfiyyaQiyas.lean")
    if m:
        lam = [list(t) for t in re.findall(r'\("(\w+)", "(\w+)", false\)', m.group(3))]
        az = akhir.get("azwaj", {})
        tahaqqaq([int(m.group(1)), int(m.group(2)), lam, int(m.group(4))] ==
                 [az.get("jumla"), az.get("taghayyar"), az.get("lam_yataghayyar"), az.get("asaba_tarafan")],
                 f"{natayij[-1].name}: azwaj {az} غيرُ مبرهنة azwaj_1")
        tahaqqaq(re.findall(r'"(\w+)"', m.group(5)) == akhir.get("rafd_qari"),
                 f"{natayij[-1].name}: rafd_qari {akhir.get('rafd_qari')} غيرُ مبرهنة azwaj_1")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith(NS) and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/IbdalAlfiyyaQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat), f"{natayij[-1].name}: halat غيرُ ما في cases.json")
    tahaqqaq(sum(akhir["ihsa"].values()) == akhir["huqul_masula"] == len(halat),
             f"{natayij[-1].name}: مجموعُ ihsa أو huqul_masula غيرُ عدد الحالات")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/IbdalAlfiyyaQiyas.lean")
if m:
    g = [int(x) for x in m.group(1).split(",")]
    tahaqqaq(g == mj, f"majal {g} غيرُ ما في cases.json {mj}")

# ٥. الأسانيد على المودَعين
mdir = os.environ.get("MUDAA_DIR")
masadir = {}
for k, (milaf, basma) in BASMAT.items():
    p = pathlib.Path(mdir) / milaf if mdir else None
    if p and p.exists() and sha(p) == basma:
        masadir[k] = p.read_text(encoding="utf-8").split("\n")
if len(masadir) == 2:
    for h in halat:
        for s in h["sanad"]:
            n = s["satr"]
            tahaqqaq(s["masdar"] == "ألفية" and any(a <= n <= b for a, b in NITAQ), f"سندُ {h['id']} خارجَ النطاق: {s['masdar']} س{n}")
            satr = re.sub(r"^# ", "", masadir["ألفية"][n - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في الألفيّة س{n} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), mdir], capture_output=True, text=True, cwd=str(D))
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{sum(len(h['sanad']) for h in halat)} سندًا للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَعان غائبان)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط الإبدال: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط الإبدال: {najah}/{najah} — {len(halat)} حالةً و{akhir['huqul_masula']} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمات الشفرة الحاليّة{ziyada}")
