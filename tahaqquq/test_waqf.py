"""ضابطُ الوقف على أواخر الكلم المتحرّكة في الوصل المجمَّد (كتاب سيبويه س17782–17859) (hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمةُ المصدر فيه بصمةُ الكتاب.
٢. المولَّد: Dal/WaqfSibawayhiDawabit.lean مخرجُ scripts/bina_dawabit_waqf.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله، فتعديلُ سجلٍّ قديمٍ يُكشف. وآخرُها لبصمة Dal/WaqfSibawayhi.lean الحاليّة، وأعدادُه (ihsa، bil_fia، akhta) هي أعدادُ
   مبرهنات Dal/WaqfSibawayhiQiyas.lean (natija، natija_fia، akhta…)، وحقلُ lean هو LEAN_NATIJA بعينها وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat وhuqul_masula في آخر سجلّ،
   ومجموعُ كلّ فئةٍ في natija_fia عددُ حقولها المسؤولة.
ويفحص، إن حضر المودَع (MUDAA_DIR/sibawayhi.txt ببصمته)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Dal/WaqfSibawayhi.lean) في أسطرها داخل النطاق، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# ») وعلامات
   الصفحات (PageV..P..) والمخطوط (ms..) وتوحيد البياض، وبأدنى مدًى (لا سطرَ زائدًا في طرفيه)؛ وكلُّ `sanad.nass` في الحالات في سطره
   بحذف البادئة وحدها، كما تشترط المواصفة؛ ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0.

الطفرات: P566 (بصمة الحالات في tajmid.json، ١)، P567 (معرّفُ حالةٍ في المولَّد، ٢)، P568 (بصمة الشفرة في آخر سجلّ، ٣)، P569 (عدُّ الصواب في آخر سجلّ، ٣)، P570 (بصمةُ ما قبله في آخر سجلّ، ٣)، P571 (عدٌّ في natija_1.json، ٣)، P572 (المرساة NATIJA_1 نفسُها، ٣)، P573 (حقلُ lean في آخر سجلّ، ٣)، P574 (akhta في آخر سجلّ، ٣)، P575 (عددُ المجال في majal_json، ٤)، P576 (halat في آخر سجلّ، ٤)، P701 (bil_fia في آخر سجلّ، ٣)، P702 (عدُّ الفئات في majal_json، ٤)، P703 (tashghil في آخر سجلّ، ٣)، P704 (cases_sha256 في آخر سجلّ، ٣)، P739–P746 (فحوصُ القالب الثمانية: بصمةُ المصدر في tajmid.json ١، وتتالي أرقام السجلّات، وصيغُ natija وakhta، واسمُ akhta في lean، وكونُ أسماء lean مبرهنات، وhuqul_masula ٤، وصيغةُ majal ٤). وطفراتُ الشفرة P560–P565 وP578–P579 وP705–P707 وP720–P722 وطفرةُ المقارنة P577 يقتلها lake build.
**على أيّ شيءٍ تقع:** P741–P744 وP746 على Dal/WaqfSibawayhiQiyas.lean نفسِه وتُبنى (المبرهنةُ بلا أعدادها: `natija`، `akhta_2`، `majal`؛ ومبرهنةُ `akhta` ثانيةً باسمٍ لا يسمّيه السجلّ؛ و`natija_fia` خاصّة)، فيقتلها الفحصُ المسمّى. وP572 وP575 وP702 وP740 تطفّر الفحصَ نفسَه (المرساةَ، والحسابَ من cases.json،
وتتاليَ الأرقام): قتلُها لا يدلّ أنّ الفحص يلتقط عيبًا في المفحوص. ولا نظيرَ لها على المفحوص يُبنى في موضعٍ واحد: P571 (عدٌّ في natija_1.json) تقتلها المرساةُ والسلسلةُ معًا، ونظيرُ المرساة وحدها يغيّر natija_1.json وqablaha في natija_2.json معًا، والأداةُ تستبدل موضعًا واحدًا؛ و cases.json مجمَّدٌ
ببصمته، وأعدادُ `majal` و`natija_fia` تقتلها Lean، وأسماءُ السجلّات لا تطفّرها الأداة.
التشغيل: python3 -I tahaqquq/test_waqf.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "waqf"
SHIFRA = JADHR / "Dal/WaqfSibawayhi.lean"
QIYAS = JADHR / "Dal/WaqfSibawayhiQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_waqf.py"
BASMAT_KITAB = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
NITAQ = (17782, 17859)
NATIJA_1 = "cdb5b5f0a32ccf7d88a11d6e48d19ad6a600c7486b97b47957c23e662101cb6a"  # natija_1.json كما أُودع في 961bb5d
NS = "Dal.WaqfSibawayhi.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_2"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtilafDaraja", "ikhtiyar", "khata"]
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
    """أعدادُ المجال بترتيب `majalAadad` في Dal/WaqfSibawayhiQiyas.lean، والحقولُ المسؤولة جملةً وبالفئة."""
    kalam = [h["kharij"]["kalam"] for h in halat]
    shir = [h["kharij"]["shir"] for h in halat]
    masul = len(halat) + sum(1 for x in shir if x != "غير_مسؤول")
    mj = [len(halat), masul]
    mj += [kalam.count(d) for d in ("مقبول", "لغة", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in kalam if isinstance(x, list))]
    mj += [shir.count(d) for d in ("مقبول", "لغة", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in shir if isinstance(x, list)), shir.count("غير_مسؤول")]
    fia = {f: 0 for f in FIAT}
    for h in halat:
        fia[h["fia"]] += 1 + (h["kharij"]["shir"] != "غير_مسؤول")
    return mj, masul, fia

# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq(tajmid["masdar"]["sha256"] == BASMAT_KITAB, "بصمةُ المصدر في tajmid.json غيرُ بصمة الكتاب")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Dal/WaqfSibawayhiDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع في 961bb5d")
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
mj, masul, masul_fia = majal_json(halat)
if akhir:
    tahaqqaq(akhir["shifra"]["sha256"] == sha(SHIFRA),
             f"{natayij[-1].name} لغير الشفرة الحاليّة: Dal/WaqfSibawayhi.lean تغيّر بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa natayij = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Dal/WaqfSibawayhiQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    tahaqqaq(len(tt) == 5 and [sum(t) for t in tt] == [masul_fia[f] for f in FIAT],
             f"مجموعُ الفئات في natija_fia {[sum(t) for t in tt]} غيرُ الحقول المسؤولة في cases.json {[masul_fia[f] for f in FIAT]}")
    m = re.search(r"theorem (akhta\w*) :\s*akhta = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ akhta بصيغتها")
    if m:
        lean_akhta = [[x for x in re.findall(r'"(\w+)"|\.(\w+)', t) for x in x if x]
                      for t in re.findall(r"\(([^()]*)\)", m.group(2))]
        tahaqqaq(lean_akhta == akhir["akhta"], f"{natayij[-1].name}: akhta {akhir['akhta']} غيرُ مبرهنة {m.group(1)} {lean_akhta}")
        tahaqqaq(NS + m.group(1) in akhir["lean"], f"{natayij[-1].name}: حقلُ lean لا يسمّي {m.group(1)}")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith(NS) and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Dal/WaqfSibawayhiQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == masul,
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Dal/WaqfSibawayhiQiyas.lean")
if m:
    g = [int(x) for x in m.group(1).split(",")]
    tahaqqaq(g == mj, f"majal {g} غيرُ ما في cases.json {mj}")

# ٥. الأسانيد على المودَع
mdir = os.environ.get("MUDAA_DIR")
kitab = pathlib.Path(mdir) / "sibawayhi.txt" if mdir else None
hadir = bool(kitab and kitab.exists() and sha(kitab) == BASMAT_KITAB)
if hadir:
    sutur = kitab.read_text(encoding="utf-8").split("\n")

    def nazzif(s):
        s = re.sub(r"^(~~|# )", "", s)
        s = re.sub(r"PageV\d+P\d+|ms\d+", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    def mawsul(a, b):
        return " ".join(nazzif(sutur[i - 1]) for i in range(a, b + 1))

    asanid = re.findall(r'\("(\w+)", (\d+), (\d+), "([^"]+)"\)', SHIFRA.read_text(encoding="utf-8"))
    tahaqqaq(len(asanid) >= 15, f"asanid قليلة: {len(asanid)}")
    for qaida, a, b, nass in asanid:
        a, b = int(a), int(b)
        tahaqqaq(NITAQ[0] <= a <= b <= NITAQ[1], f"سندُ {qaida} خارجَ النطاق: {a}–{b}")
        tahaqqaq(nass in mawsul(a, b), f"سندُ {qaida} ليس في س{a}–{b}: «{nass}»")
        tahaqqaq(a == b or (nass not in mawsul(a + 1, b) and nass not in mawsul(a, b - 1)),
                 f"سندُ {qaida} أوسعُ من موضعه: س{a}–{b}")
    for h in halat:
        for s in h["sanad"]:
            satr = re.sub(r"^(~~|# )", "", sutur[s["satr"] - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في س{s['satr']} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), str(kitab)],
                       capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{sum(len(h['sanad']) for h in halat)} للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَع غائب)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط الوقف: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط الوقف: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمة الشفرة الحاليّة{ziyada}")
