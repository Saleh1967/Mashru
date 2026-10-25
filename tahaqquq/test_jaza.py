"""ضابطُ «هذا باب الجزاء» المجمَّد (hawkama/منهج_الضوابط.md §٤، في طلبه).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمةُ المصدر فيه بصمةُ الكتاب.
٢. المولَّد: Jisr/BabJazaDawabit.lean مخرجُ scripts/bina_dawabit_jaza.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله، فتعديلُ سجلٍّ قديمٍ يُكشف. وآخرُها لبصمة Jisr/BabJaza.lean الحاليّة، وأعدادُه (ihsa، bil_fia، akhta)
   هي أعدادُ مبرهنات Jisr/BabJazaQiyas.lean (natija، natija_fia، akhta_sifr)، وحقلُ lean هو LEAN_NATIJA بعينها وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ الحالات والحقول المسؤولة والمتوقَّعات محسوبةٌ من cases.json هنا، لا من Lean، وهي أعدادُ `majal`، وhalat
   وhuqul_masula في آخر سجلّ.
ويفحص، إن حضر المودَع (MUDAA_DIR/sibawayhi.txt ببصمته)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/BabJaza.lean) في أسطرها، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# ») وعلامات
   الصفحات (PageV..P..) والمخطوط (ms..) وتوحيد البياض؛ وكلُّ `sanad.nass` في الحالات في سطره بحذف البادئة وحدها، كما تشترط
   المواصفة؛ ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0.

الطفرات: P492 (بصمة الحالات في tajmid.json، ١)، P493 (بصمة الشفرة في آخر سجلّ، ٣)، P494 (حالةٌ في المولَّد، ٢)،
P495 (عدُّ الصواب في آخر سجلّ، ٣)، P497 (بصمةُ ما قبله في آخر سجلّ، ٣)، P498 (عدٌّ في natija_1.json، ٣)، P499 (halat في آخر سجلّ، ٤)،
P500 (المرساة NATIJA_1 نفسُها، ٣)، P501 (حقلُ lean في آخر سجلّ، ٣)،
P763–P770 (فحوصٌ كانت بلا طفرة: بصمةُ المصدر في tajmid.json ١، وتتالي أرقام السجلّات، وصيغُ natija وnatija_fia، وakhta_sifr،
وكونُ أسماء lean مبرهنات، وhuqul_masula ٤، وصيغةُ majal ٤).
التشغيل: python3 -I tahaqquq/test_jaza.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "jaza"
SHIFRA = JADHR / "Jisr" / "BabJaza.lean"
QIYAS = JADHR / "Jisr" / "BabJazaQiyas.lean"
BASMAT_KITAB = "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625"
NATIJA_1 = "4417cf9f9c1860d4173720d446e0ffd6acbc13ad3e9db023fec46d1b25f02fa1"  # natija_1.json كما أُودع في 68911d9
LEAN_NATIJA = ["Jisr.BabJaza.Qiyas.majal", "Jisr.BabJaza.Qiyas.natija", "Jisr.BabJaza.Qiyas.natija_fia",
               "Jisr.BabJaza.Qiyas.akhta_sifr"]

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


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq(tajmid["masdar"]["sha256"] == BASMAT_KITAB, "بصمةُ المصدر في tajmid.json غيرُ بصمة الكتاب")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(JADHR / "scripts" / "bina_dawabit_jaza.py"), "--check"],
                   capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/BabJazaDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع في 68911d9")
for k, p in enumerate(natayij):
    n = json.loads(p.read_text(encoding="utf-8"))
    tahaqqaq(n["tashghil"] == k + 1, f"{p.name}: رقمُ التشغيل فيه {n['tashghil']}")
    tahaqqaq(n["cases_sha256"] == tajmid["cases_sha256"], f"{p.name}: لغير الحالات المجمَّدة")
    if k > 0:
        qabl = natayij[k - 1]
        tahaqqaq(n.get("qablaha", {}).get(qabl.name) == sha(qabl), f"{p.name} لا يحمل بصمةَ {qabl.name}: سجلٌّ قديمٌ تغيّر")
akhir = json.loads(natayij[-1].read_text(encoding="utf-8")) if natayij else None
if akhir:
    tahaqqaq(akhir["shifra"]["sha256"] == sha(SHIFRA),
             f"{natayij[-1].name} لغير الشفرة الحاليّة: Jisr/BabJaza.lean تغيّر بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa natayij = ⟨(\d+), (\d+), (\d+), (\d+), (\d+), (\d+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/BabJazaQiyas.lean")
    if m:
        ihsa = akhir["ihsa"]
        json_ = [ihsa[k] for k in ("sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtilafDaraja")]
        tahaqqaq([int(x) for x in m.groups()] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?=\s*\[⟨(\d+), 0, 0, 0, 0, 0⟩, ⟨(\d+), 0, 0, 0, 0, 0⟩, ⟨(\d+), 0, 0, 0, 0, 0⟩, ⟨(\d+), 0, 0, 0, 0, 0⟩\]",
                  qiyas, re.S)
    bf = akhir["bil_fia"]
    tahaqqaq(m is not None and [int(x) for x in m.groups()] == [bf["موجب"], bf["حد"], bf["خارج"], bf["عموم"]],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    tahaqqaq(akhir["akhta"] == [] and "theorem akhta_sifr : akhta = []" in qiyas,
             f"{natayij[-1].name}: akhta غيرُ مبرهنة akhta_sifr")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith("Jisr.BabJaza.Qiyas.") and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/BabJazaQiyas.lean")

# ٤. المجال من cases.json وحده
halat = json.loads((D / "cases.json").read_text(encoding="utf-8"))
kalam = [h["kharij"]["kalam"] for h in halat]
shir = [h["kharij"]["shir"] for h in halat]
masul = len(halat) + sum(1 for x in shir if x != "غير_مسؤول")
adad_kalam = [kalam.count(x) for x in ("مقبول", "قبيح", "خطأ", "لا_حكم")]
adad_shir = [shir.count(x) for x in ("مقبول", "قبيح", "خطأ", "لا_حكم", "غير_مسؤول")]
m = re.search(r"theorem majal :\s*halat\.length = (\d+) ∧ natayij\.length = (\d+) ∧.*?= \[(\d+), (\d+), (\d+), (\d+)\] ∧.*?= \[(\d+), (\d+), (\d+), (\d+), (\d+)\]",
              qiyas, re.S)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/BabJazaQiyas.lean")
if m:
    g = [int(x) for x in m.groups()]
    tahaqqaq(g[0] == len(halat) and g[1] == masul and g[2:6] == adad_kalam and g[6:] == adad_shir,
             f"majal {g} غيرُ ما في cases.json {[len(halat), masul] + adad_kalam + adad_shir}")
if akhir:
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == masul,
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")

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
    tahaqqaq(len(asanid) >= 30, f"asanid قليلة: {len(asanid)}")
    for qaida, a, b, nass in asanid:
        a, b = int(a), int(b)
        tahaqqaq(9190 <= a <= b <= 9304, f"سندُ {qaida} خارجَ النطاق: {a}–{b}")
        tahaqqaq(nass in mawsul(a, b), f"سندُ {qaida} ليس في س{a}–{b}: «{nass}»")
    for h in halat:
        for s in h["sanad"]:
            satr = re.sub(r"^(~~|# )", "", sutur[s["satr"] - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في س{s['satr']} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), str(kitab)],
                       capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{sum(len(h['sanad']) for h in halat)} للحالات في أسطرها"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَع غائب)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط باب الجزاء: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط باب الجزاء: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمة الشفرة الحاليّة{ziyada}، وفاحصُ المؤلّف 0" if hadir else
      f"ضابط باب الجزاء: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمة الشفرة الحاليّة{ziyada}")
