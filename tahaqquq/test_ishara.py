"""ضابطُ أسماء الإشارة المجمَّد (قطر الندى س132–135، الألفية س137–144؛ hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md وbina_cases.py هي المسجَّلة في tajmid.json، وبصمتا المصدرين فيه بصمتا
   القطر والألفية.
٢. المولَّد: Jisr/IsharaDawabit.lean مخرجُ scripts/bina_dawabit_ishara.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله. وآخرُها لبصمتَي الشفرة الحاليّة (SHIFRA: الحكمُ والمقارنة)، وأعدادُه (ihsa، bil_fia، akhta، azwaj) هي أعدادُ
   مبرهنات Jisr/IsharaQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat وhuqul_masula في آخر سجلّ،
   ومجموعُ كلّ فئةٍ في natija_fia عددُ حالاتها.
ويفحص، إن حضر المودَعان (MUDAA_DIR/qatr.txt وalfiyya.txt ببصمتيهما)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/Ishara.lean) في أسطرها داخل نطاق مصدرها، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# » أو
   «### | ») وأسطر علامات الصفحات وحدها (PageV..P..) وتوحيد البياض، وبأدنى مدًى؛ وكلُّ `sanad.nass` في الحالات في سطره بحذف البادئة وحدها؛
   ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0.

الطفرات (وقاتلُ كلٍّ منها الفحصُ المسمّى، إلّا ما يُذكر): P931 (بصمةُ الحالات في tajmid.json، ١)، P932 (بصمةُ القطر فيه، ١)، P933 (معرّفُ حالةٍ
بلا زوجٍ في المولَّد، فيُبنى، ٢)، P934 (بصمةُ الشفرة في آخر سجلّ، ٣)، P935 (عدُّ الصواب في آخر سجلّ، ٣)، P936 (qablaha في آخر سجلّ، ٣)، P937 (عدٌّ في
natija_1.json: المرساةُ والسلسلةُ معًا، ٣)، P938 (حقلُ lean في آخر سجلّ، ٣)، P939 (akhta في آخر سجلّ، ٣)، P940 (bil_fia في آخر سجلّ، ٣)، P941
(tashghil في آخر سجلّ، ٣)، P942 (cases_sha256 في آخر سجلّ، ٣)، P943 (halat في آخر سجلّ، ٤)، P944 (azwaj في آخر سجلّ، ٣)؛ وعلى Jisr/IsharaQiyas.lean
وتُبنى: P945 (`majal` بلا أعدادها، ٤)، P946 (`natija` بلا أعدادها، ٣).
**ما لا يُعزل:** P937 تقتلها المرساةُ والسلسلةُ معًا، ونظيرُ المرساة وحدها يغيّر natija_1.json وqablaha في كلّ سجلٍّ بعده، والأداةُ تستبدل موضعًا
واحدًا. وcases.json مجمَّدٌ ببصمته، وأعدادُ `majal` و`natija_fia` تقتلها Lean، وأسماءُ السجلّات لا تطفّرها الأداة.
وطفراتُ الحكم والمقارنة (P912–P928، P930) يقتلها lake build.
التشغيل: python3 -I tahaqquq/test_ishara.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "ishara"
SHIFRA = ["Jisr/Ishara.lean", "Jisr/IsharaDabit.lean"]
QIYAS = JADHR / "Jisr/IsharaQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_ishara.py"
BASMAT = {"قطر": ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d"),
          "ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0")}
NITAQ = {"قطر": (132, 135), "ألفية": (137, 144)}
NATIJA_1 = "e1fe145569aa982a8d8f0851f12e05d9e20672bc9828cfbaa3ca3a0096a1163d"  # natija_1.json كما أُودع في 7a9a064
NS = "Jisr.Ishara.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_sifr", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "khata"]
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]

fashal = []
najah = 0


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def tahaqqaq(shart, risala):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(risala)


def majal_json(halat):
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/IsharaQiyas.lean: الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ، «لا حكم»، بديلان؛ ثمّ ذواتُ
    الزوج؛ ثمّ الفئاتُ بترتيب FIAT."""
    hukm = [h["hukm"] for h in halat]
    mj = [len(halat)] + [hukm.count(d) for d in ("مقبول", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in hukm if isinstance(x, list))]
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"), ("fahs_cases.py", "fahs_cases_sha256"),
                    ("taalif.md", "taalif_sha256"), ("bina_cases.py", "bina_cases_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq({m["milaf"]: m["sha256"] for m in tajmid["masadir"]} == {v[0]: v[1] for v in BASMAT.values()},
         "بصمتا المصدرين في tajmid.json غيرُ بصمتَي القطر والألفية")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/IsharaDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع في 7a9a064")
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
    m = re.search(r"theorem natija : ihsa \(natayij halat\) = ⟨([\d, ]+)⟩ := by", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/IsharaQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    adad_fia = [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    tahaqqaq(len(tt) == 5 and [sum(t) for t in tt] == adad_fia,
             f"مجموعُ الفئات في natija_fia {[sum(t) for t in tt]} غيرُ حالات cases.json {adad_fia}")
    m = re.search(r"theorem (akhta\w*) :\s*akhta \(natayij halat\) = \[(.*?)\] := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ akhta بصيغتها")
    if m:
        lean_akhta = [[x for x in re.findall(r'"(\w+)"|\.(\w+)', t) for x in x if x]
                      for t in re.findall(r"\(([^()]*)\)", m.group(2))]
        tahaqqaq(lean_akhta == akhir["akhta"], f"{natayij[-1].name}: akhta {akhir['akhta']} غيرُ مبرهنة {m.group(1)} {lean_akhta}")
        tahaqqaq(NS + m.group(1) in akhir["lean"], f"{natayij[-1].name}: حقلُ lean لا يسمّي {m.group(1)}")
    m = re.search(r"theorem azwaj_1 :\s*\(azwaj halat\)\.length = (\d+) ∧ \(\(azwaj halat\)\.filter \(·\.2\.2\)\)\.length = (\d+) ∧\s*"
                  r"\(\(azwaj halat\)\.filter fun p => sawab p\.1 && sawab p\.2\.1\)\.length = (\d+) := by", qiyas, re.S)
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj_1 بصيغتها في Jisr/IsharaQiyas.lean")
    if m:
        az = akhir.get("azwaj", {})
        tahaqqaq([int(m.group(1)), int(m.group(2)), int(m.group(3))] == [az.get("jumla"), az.get("taghayyar"), az.get("sawab_maan")],
                 f"{natayij[-1].name}: azwaj {az} غيرُ مبرهنة azwaj_1")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith(NS) and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/IsharaQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == len(halat),
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")
    tahaqqaq(sum(akhir["ihsa"].values()) == akhir["huqul_masula"], f"{natayij[-1].name}: مجموعُ ihsa غيرُ huqul_masula")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\] := by", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/IsharaQiyas.lean")
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
    def nazzif(s):
        s = re.sub(r"^(### \| |~~|# )", "", s)
        s = re.sub(r"^PageV\d+P\d+$", "", s.strip())
        return re.sub(r"\s+", " ", s).strip()

    def mawsul(k, a, b):
        return " ".join(x for x in (nazzif(masadir[k][i - 1]) for i in range(a, b + 1)) if x)

    asanid = re.findall(r'\("(\w+)", "([^"]+)", (\d+), (\d+), "([^"]+)"\)', (JADHR / SHIFRA[0]).read_text(encoding="utf-8"))
    tahaqqaq(len(asanid) >= 10, f"asanid قليلة: {len(asanid)}")
    for qaida, k, a, b, nass in asanid:
        a, b = int(a), int(b)
        tahaqqaq(k in NITAQ and NITAQ[k][0] <= a <= b <= NITAQ[k][1], f"سندُ {qaida} خارجَ نطاق {k}: {a}–{b}")
        if k in masadir:
            tahaqqaq(nass in mawsul(k, a, b), f"سندُ {qaida} ليس في {k} س{a}–{b}: «{nass}»")
            tahaqqaq(a == b or (nass not in mawsul(k, a + 1, b) and nass not in mawsul(k, a, b - 1)),
                     f"سندُ {qaida} أوسعُ من موضعه: س{a}–{b}")
    for h in halat:
        for s in h["sanad"]:
            k, n = s["masdar"], s["satr"]
            tahaqqaq(NITAQ[k][0] <= n <= NITAQ[k][1], f"سندُ {h['id']} خارجَ نطاق {k}: س{n}")
            satr = re.sub(r"^(### \| |~~|# )", "", masadir[k][n - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في {k} س{n} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), mdir], capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{sum(len(h['sanad']) for h in halat)} للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَعان غائبان)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط أسماء الإشارة: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط أسماء الإشارة: {najah}/{najah} — {len(halat)} حالةً، و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمتَي الشفرة الحاليّة"
      f"{ziyada}")
