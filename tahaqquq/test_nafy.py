"""ضابطُ «نفي الفعل» وحروفِ الفعل المجمَّد (كتاب سيبويه س9755–9787) (hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمةُ المصدر فيه بصمةُ الكتاب.
٢. المولَّد: Jisr/NafyFilDawabit.lean مخرجُ scripts/bina_dawabit_nafy.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله، فتعديلُ سجلٍّ قديمٍ يُكشف. وآخرُها لبصمة Jisr/NafyFil.lean الحاليّة، وأعدادُه (ihsa، bil_fia، akhta) هي أعدادُ
   مبرهنات Jisr/NafyFilQiyas.lean (natija، natija_fia، akhta…)، وحقلُ lean هو LEAN_NATIJA بعينها وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat وhuqul_masula في آخر سجلّ،
   ومجموعُ كلّ فئةٍ في natija_fia عددُ حقولها المسؤولة.
ويفحص، إن حضر المودَع (MUDAA_DIR/sibawayhi.txt ببصمته)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/NafyFil.lean) في أسطرها داخل النطاق، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# ») وعلامات
   الصفحات (PageV..P..) والمخطوط (ms..) وتوحيد البياض، وبأدنى مدًى (لا سطرَ زائدًا في طرفيه)؛ وكلُّ `sanad.nass` في الحالات في سطره
   بحذف البادئة وحدها، كما تشترط المواصفة؛ ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0.

الطفرات: P508 (بصمة الحالات في tajmid.json، ١)، P509 (حالةٌ في المولَّد، ٢)، P510 (بصمة الشفرة في آخر سجلّ، ٣)، P511 (عدُّ الصواب في آخر سجلّ، ٣)، P512 (بصمةُ ما قبله في آخر سجلّ، ٣)، P513 (عدٌّ في natija_1.json، ٣)، P514 (المرساة NATIJA_1 نفسُها، ٣)، P515 (حقلُ lean في آخر سجلّ، ٣)، P516 (akhta في آخر سجلّ، ٣)، P517 (عددُ المجال في majal_json، ٤)، P518 (halat في آخر سجلّ، ٤)، P716 (bil_fia في آخر سجلّ، ٣)، P717 (عدُّ الفئات في majal_json، ٤)، P718 (tashghil في آخر سجلّ، ٣)، P719 (cases_sha256 في آخر سجلّ، ٣)، P723–P730 (فحوصُ القالب الثمانية: بصمةُ المصدر في tajmid.json ١، وتتالي أرقام السجلّات، وصيغُ natija وakhta، واسمُ akhta في lean، وكونُ أسماء lean مبرهنات، وhuqul_masula ٤، وصيغةُ majal ٤).
التشغيل: python3 -I tahaqquq/test_nafy.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "nafy"
SHIFRA = JADHR / "Jisr/NafyFil.lean"
QIYAS = JADHR / "Jisr/NafyFilQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_nafy.py"
BASMAT_KITAB = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
NITAQ = (9755, 9787)
NATIJA_1 = "01d9b02399def4ac160030e75fbb74e2453e68eff869dde2c7e7c25f6d207129"  # natija_1.json كما أُودع في 5cb531f
NS = "Jisr.NafyFil.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_sifr"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "ikhtiyar", "khata", "qabulKhati", "raddKhati", "ikhtilafDaraja"]
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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/NafyFilQiyas.lean، والحقولُ المسؤولة جملةً وبالفئة."""
    nafy = [h for h in halat if h["naw"] == "نفي"]
    wali = [h for h in halat if h["naw"] == "ولي"]
    suwar = [h["kharij"]["suwar"] for h in nafy]
    kalam = [h["kharij"]["kalam"] for h in wali]
    shir = [h["kharij"]["shir"] for h in wali]
    masul = len(nafy) + len(wali) + sum(1 for x in shir if x != "غير_مسؤول")
    mj = [len(nafy), len(wali), masul,
          sum(1 for x in suwar if x == "لا_حكم"),
          sum(1 for x in suwar if isinstance(x, list) and len(x) == 1),
          sum(1 for x in suwar if isinstance(x, list) and len(x) >= 2)]
    mj += [kalam.count(d) for d in ("مقبول", "مرجوح", "قبيح", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in kalam if isinstance(x, list))]
    mj += [shir.count(d) for d in ("مقبول", "مرجوح", "قبيح", "خطأ", "لا_حكم", "غير_مسؤول")]
    fia = {f: 0 for f in FIAT}
    for h in nafy:
        fia[h["fia"]] += 1
    for h in wali:
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
tahaqqaq(r.returncode == 0, "Jisr/NafyFilDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع في 5cb531f")
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
             f"{natayij[-1].name} لغير الشفرة الحاليّة: Jisr/NafyFil.lean تغيّر بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa natayij = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/NafyFilQiyas.lean")
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
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/NafyFilQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == masul,
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/NafyFilQiyas.lean")
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
    tahaqqaq(len(asanid) >= 20, f"asanid قليلة: {len(asanid)}")
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
    print(f"ضابط نفي الفعل: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط نفي الفعل: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمة الشفرة الحاليّة{ziyada}")
