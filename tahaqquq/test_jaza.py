"""ضابطُ «هذا باب الجزاء» المجمَّد (hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json.
٢. المولَّد: Jisr/BabJazaDawabit.lean مخرجُ scripts/bina_dawabit_jaza.py على cases.json بايتًا.
٣. النتيجة: آخرُ natija_N.json لبصمة Jisr/BabJaza.lean الحاليّة ولبصمة الحالات المجمَّدة. وأعدادُه هي أعدادُ مبرهنته
   في Jisr/BabJazaQiyas.lean. وكلُّ نتيجةٍ قبله باقيةٌ، وأرقامُها متتالية.
٤. المجال: أعدادُ الحالات والحقول المسؤولة والمتوقَّعات محسوبةٌ من cases.json هنا، لا من Lean. وهي أعدادُ `majal_1`.
ويفحص، إن حضر المودَع (MUDAA_DIR/sibawayhi.txt ببصمته):
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/BabJaza.lean) وكلُّ `sanad.nass` في الحالات حرفيّةٌ في أسطرها، على النصّ موصولَ
   الأسطر بحذف البادئة («~~» أو «# ») وعلامات الصفحات (PageV..P..) والمخطوط (ms..).

الطفرات: P492 (بصمة الحالات في tajmid.json)، P493 (بصمة الشفرة في natija_1.json)، P494 (حالةٌ في المولَّد)،
P495 (عدُّ الصواب في natija_1.json).
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

# ٣. النتيجة
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(arqam == list(range(1, len(arqam) + 1)) and arqam, f"أرقامُ النتائج غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
for p in natayij:
    n = json.loads(p.read_text(encoding="utf-8"))
    tahaqqaq(n["cases_sha256"] == tajmid["cases_sha256"], f"{p.name}: لغير الحالات المجمَّدة")
    m = re.search(r"theorem natija_%d : ihsa natayij = ⟨(\d+), (\d+), (\d+), (\d+), (\d+), (\d+)⟩" % n["tashghil"], qiyas)
    tahaqqaq(m is not None, f"{p.name}: لا مبرهنةَ natija_{n['tashghil']} في Jisr/BabJazaQiyas.lean")
    if m:
        ihsa = n["ihsa"]
        lean = [int(x) for x in m.groups()]
        json_ = [ihsa[k] for k in ("sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtilafDaraja")]
        tahaqqaq(lean == json_, f"{p.name}: أعدادُه {json_} غيرُ أعداد مبرهنته {lean}")
if natayij:
    akhir = json.loads(natayij[-1].read_text(encoding="utf-8"))
    tahaqqaq(akhir["shifra"]["sha256"] == sha(SHIFRA),
             f"{natayij[-1].name} لغير الشفرة الحاليّة: Jisr/BabJaza.lean تغيّر بعد آخر تشغيل")

# ٤. المجال من cases.json وحده
halat = json.loads((D / "cases.json").read_text(encoding="utf-8"))
kalam = [h["kharij"]["kalam"] for h in halat]
shir = [h["kharij"]["shir"] for h in halat]
masul = len(halat) + sum(1 for x in shir if x != "غير_مسؤول")
adad_kalam = [kalam.count(x) for x in ("مقبول", "قبيح", "خطأ", "لا_حكم")]
adad_shir = [shir.count(x) for x in ("مقبول", "قبيح", "خطأ", "لا_حكم", "غير_مسؤول")]
m = re.search(r"halat\.length = (\d+) ∧ natayij\.length = (\d+) ∧.*?= \[(\d+), (\d+), (\d+), (\d+)\] ∧.*?= \[(\d+), (\d+), (\d+), (\d+), (\d+)\]",
              qiyas, re.S)
tahaqqaq(m is not None, "لا مبرهنةَ majal_1 بصيغتها في Jisr/BabJazaQiyas.lean")
if m:
    g = [int(x) for x in m.groups()]
    tahaqqaq(g[0] == len(halat) and g[1] == masul and g[2:6] == adad_kalam and g[6:] == adad_shir,
             f"majal_1 {g} غيرُ ما في cases.json {[len(halat), masul] + adad_kalam + adad_shir}")

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
            tahaqqaq(s["nass"] in nazzif(sutur[s["satr"] - 1]), f"سندُ {h['id']} ليس في س{s['satr']}")
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{sum(len(h['sanad']) for h in halat)} للحالات في أسطرها"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَع غائب)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط باب الجزاء: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط باب الجزاء: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، "
      f"وآخرُ نتيجةٍ natija_{arqam[-1]} لبصمة الشفرة الحاليّة{ziyada}")
