"""ضابطُ «أثر العُقَد» المجمَّد: قوّةُ الجملة وقيدُ المخالفة في لفظها (hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصماتُ المصادر فيه بصماتُ المودَعات.
٢. المولَّد: Nizam/AtharDawabit.lean مخرجُ scripts/bina_dawabit_athar.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ بعده يحمل
   بصمةَ ما قبله. وآخرُها لبصمات الشفرة الحاليّة (SHIFRA)، وأعدادُه (ihsa، bil_fia، akhta، azwaj) هي أعدادُ مبرهنات Nizam/AtharQiyas.lean،
   وحقلُ lean هو LEAN_NATIJA بعينها وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال بالقيم محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat في آخر سجلّ، ومجموعُ كلّ
   فئةٍ في natija_fia عددُ حالاتها.
ويفحص، إن حضرت المودَعات (MUDAA_DIR) ببصماتها، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. كلُّ `sanad.nass` في الحالات في سطره بحذف البادئة وحدها، وسطرُه في نطاق نوع حالته كما تشترط المواصفة؛ ثمّ فاحصُ المؤلّف نفسُه يخرج 0.

الطفرات وقاتلُها (شُغّلت بـtafrat_juz.py على 08a3ba1، 21 من 21، وأُعيدت P1430–P1439 على natija_3.json بعده؛ وعُزل الفحصُ القاتل بتشغيل الاختبار
تحت كلّ طفرة): على المقارنة يقتلها البناء —
P1419 (`qarin`: «لا حكم» تجاوز، `qarin_shawahid`)، P1428 (لا ردَّ من القارئ، `rafd_shahid`)؛ وعلى المفحوص يقتلها الفحصُ المسمّى وحده: P1420 (بصمةُ
المواصفة في tajmid.json، ١)، P1421 (بصمةُ مصدرٍ فيه، ١)، P1422 (جملةُ حالةٍ في المولَّد، ٢)، P1423 (جدولُ القوّة في المولِّد، ٢)، P1425 (`natija` بلا أعدادها،
٣)، P1427 (`azwaj_1` بغير صيغتها، ٣)، P1429 (`akhta_1` بغير صيغتها، ٣)، P1430 (tashghil، ٣)، P1431 (cases_sha256، ٣)، P1432 (بصمةُ ملفٍّ من الشفرة،
٣)، P1433 (bil_fia، ٣)، P1434 (akhta، ٣)، P1435 (azwaj، ٣)، P1436 (حقلُ lean، ٣)، P1437 (halat، ٣)، P1438 (qablaha، ٣)، P1439 (ihsa، ٣)، P1426 (`majal`
بلا أعدادها، ٤). وP1430–P1439 على natija_3.json (آخرِ سجلّ).
**أثرُ بصمة الشفرة على غيره:** تشمل ملفّاتٍ لا يبصمها اختبارُ ضابطٍ قبله (منها Jisr/QaydMafhum.lean وJisr/MantuqMafhum.lean وJisr/AqsamAwamil.lean
وJisr/Awamil.lean وNizam/Silsila.lean)، فكلُّ طفرةٍ مقبلةٍ فيها تنجو من الاختبارات قبله يقتلها فحصُ البصمة في ٣، وهو لا يدلّ على عيبٍ سلوكيّ. وقاتلُ
طفرةٍ قائمة في ملفّات البصمة قد يتغيّر: إن كان اختبارًا بعد هذا في IKHTIBARAT_TAFRAT (tahaqquq/bawwaba.py)، أو قتلها البناءُ (natayij_1 وشواهدُ
Nizam/Athar.lean) قبل قاتلها المعلَن؛ ويُرى ذلك في تشغيل الطفرات الكامل على CI.
**ما لا يُعزل:** P1424 (عدٌّ في natija_1.json) يقتلها فحصان: المرساة NATIJA_1، وqablaha في natija_2.json (٣). ولا طفرةَ على: موازنة أعداد `majal` بما
في cases.json، ومجموعِ كلّ فئةٍ في `natija_fia` (تغييرُ أعداد المبرهنة يقتله البناء، وcases.json مجمَّدٌ ببصمته)؛ ووجودِ أسماء حقل lean مبرهناتٍ (لم تُبنَ
طفرتُه: إعادةُ تسمية مبرهنةٍ تُبقي سطرَها في Audit.lean بلا تصريح)؛ وتتالي أرقام السجلّات؛ وفحوصِ ٥ (CI بلا مودَع).
التشغيل: python3 -I tahaqquq/test_athar_dabit.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "athar"
# بصمةُ الشفرة: ملفّاتُ ما يحسب الحقلين مباشرةً (القوّة والقيد وقراءةُ الجملة وإطارُها وحكمُه)، لا كلُّ ما تستورده. وفي natija_1.json خمسةٌ منها
# (الشفرةُ المجمَّدة)، وثلاثةَ عشرَ في natija_2.json، وخمسةَ عشرَ منذ natija_3.json (زيد Jisr/QawaidSitta.lean وJisr/QawaidJadwal.lean).
SHIFRA = ["Nizam/Athar.lean", "Nizam/AtharDabit.lean", "Nizam/Silsila.lean", "Jisr/NassItar.lean", "Dal/QiraaTahsil.lean",
          "Dal/Tahsil.lean", "Jisr/Utur.lean", "Jisr/SakkJumla.lean", "Jisr/Awamil.lean", "Jisr/AwamilJadwal.lean",
          "Jisr/AqsamAwamil.lean", "Jisr/MantuqMafhum.lean", "Jisr/QaydMafhum.lean", "Jisr/QawaidSitta.lean",
          "Jisr/QawaidJadwal.lean"]
QIYAS = JADHR / "Nizam/AtharQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_athar.py"
MASADIR = {
    "qatr.txt": "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
    "mughni.txt": "f37ac2bb4b273f59169053dd0ac2abf50a52846a7e87ddf689ee5c0b87f77e7d",
    "sibawayhi.txt": "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625",
    "a2.txt": "8252ca521c91c285b0344b74ab5fc956f088447c8c7811fd5c95c6c2717b8401",
}
# نطاقُ كلّ نوعٍ في المواصفة (wasf.md، «المصادر والنطاق»).
NITAQ = {
    "قوة": {"sibawayhi.txt": [(1268, 1294), (1522, 1525), (9190, 9304), (9544, 9652), (9782, 9787), (10022, 10041)],
            "mughni.txt": [(129, 134), (2217, 2239), (5901, 5919), (6109, 6116), (6400, 6405), (6483, 6486), (8094, 8116),
                           (9567, 9589), (9620, 9668)],
            "qatr.txt": [(108, 122), (194, 197)],
            "alfiyya.txt": [(250, 256), (296, 302), (905, 912)],
            "a2.txt": [(767, 767), (896, 896)]},
    "قيد": {"a2.txt": [(1062, 1106)]},
}
NATIJA_1 = "562bf2462de408048f96c4695d7505e08e4d60f4041be8d183b04674d33f0b21"  # natija_1.json كما أُودع أوّلًا
NS = "Nizam.Athar.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natayij_1", "natija", "natija_fia", "akhta_1", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "ikhtiyar", "khata", "rafdQari"]
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


def qaima(v):
    return v if isinstance(v, list) else [v]


def majal_json(halat):
    """أعدادُ المجال بترتيب `majalAadad` في Nizam/AtharDabit.lean، والحالاتُ بالفئة."""
    q = [h for h in halat if h["naw"] == "قوة"]
    d = [h for h in halat if h["naw"] == "قيد"]

    def bil_qiyam(qiyam, l):
        l = [qaima(x) for x in l]
        return [sum(1 for x in l if x == [v]) for v in qiyam] + [sum(1 for x in l if len(x) >= 2)]

    mj = [len(halat), len(q), len(d)]
    mj += bil_qiyam(["إثبات", "نفي", "تعليق", "إنشاء", "لا_حكم"], [h["kharij"]["quwwa"] for h in q])
    mj += bil_qiyam(["صفة", "شرط", "غاية", "عدد", "لا_قيد", "لا_حكم"], [h["kharij"]["qayd"] for h in d])
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj, {f: sum(1 for h in halat if h["fia"] == f) for f in FIAT}


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq({x["milaf"]: x["sha256"] for x in tajmid["masadir"]} == MASADIR and len(tajmid["masadir"]) == len(MASADIR),
         "بصماتُ المصادر في tajmid.json غيرُ بصمات المودَعات")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Nizam/AtharDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

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
mj, bil_fia_json = majal_json(halat)
if akhir:
    tahaqqaq({m: x["sha256"] for m, x in akhir["shifra"].items()} == {m: sha(JADHR / m) for m in SHIFRA},
             f"{natayij[-1].name} لغير الشفرة الحاليّة: تغيّر ملفٌّ من {SHIFRA} بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa \(natayij halat\) = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Nizam/AtharQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    tahaqqaq(len(tt) == 5 and [sum(t) for t in tt] == [bil_fia_json[f] for f in FIAT],
             f"مجموعُ الفئات في natija_fia {[sum(t) for t in tt]} غيرُ الحالات في cases.json {[bil_fia_json[f] for f in FIAT]}")
    m = re.search(r"theorem (akhta_\d+) :\s*akhta \(natayij halat\) = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ akhta بصيغتها")
    if m:
        lean_akhta = [[x for x in re.findall(r'"(\w+)"|\.(\w+)', t) for x in x if x]
                      for t in re.findall(r"\(([^()]*)\)", m.group(2))]
        tahaqqaq(lean_akhta == akhir["akhta"], f"{natayij[-1].name}: akhta {akhir['akhta']} غيرُ مبرهنة {m.group(1)} {lean_akhta}")
    m = re.search(r"theorem (azwaj_\d+) :\s*azwaj halat = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj بصيغتها")
    if m:
        lean_azwaj = [[a, b, c == "true"] for a, b, c in re.findall(r'\("(\w+)", "(\w+)", (true|false)\)', m.group(2))]
        tahaqqaq(lean_azwaj == akhir["azwaj"], f"{natayij[-1].name}: azwaj {akhir['azwaj']} غيرُ مبرهنة {m.group(1)}")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith(NS) and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Nizam/AtharQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat), f"{natayij[-1].name}: halat غيرُ ما في cases.json")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad halat = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Nizam/AtharQiyas.lean")
if m:
    g = [int(x) for x in m.group(1).split(",")]
    tahaqqaq(g == mj, f"majal {g} غيرُ ما في cases.json {mj}")

# ٥. السندُ على المودَع
mdir = os.environ.get("MUDAA_DIR")
hadir = bool(mdir) and all((pathlib.Path(mdir) / f).exists() and sha(pathlib.Path(mdir) / f) == b for f, b in MASADIR.items())
if hadir:
    cache = {}

    def sutur_milaf(f):
        if f not in cache:
            cache[f] = (pathlib.Path(mdir) / f).read_text(encoding="utf-8").split("\n")
        return cache[f]

    nh = 0
    for h in halat:
        for s in h["sanad"]:
            nh += 1
            satr = re.sub(r"^(~~|# |### \| )", "", sutur_milaf(s["milaf"])[s["satr"] - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في {s['milaf']} س{s['satr']} بحذف البادئة وحدها")
            tahaqqaq(any(a <= s["satr"] <= b for a, b in NITAQ[h["naw"]].get(s["milaf"], [])),
                     f"سندُ {h['id']} خارجَ نطاق نوعه: {s['milaf']} س{s['satr']}")
    # فاحصُ المؤلّف يقرأ المصادرَ من /home/claude/mudaa_dir مكتوبًا فيه، ويأخذ مسارَ الحالات.
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json")], capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{nh} سندًا للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ السندُ لم يُفحص (المودَعات غائبة)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط أثر العقد: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط أثر العقد: {najah}/{najah} — {len(halat)} حالةً، و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمات الشفرة الحاليّة{ziyada}")
