"""ضابطُ الخبر المجمَّد (قطر الندى س157–162، الألفية س177–188؛ hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md وbina_cases.py وsana_tafrat.py هي المسجَّلة في tajmid.json، وبصمتا المصدرين
   فيه بصمتا القطر والألفية.
٢. المولَّد: Jisr/KhabarDawabit.lean مخرجُ scripts/bina_dawabit_khabar.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله. وآخرُها لبصمتَي الشفرة الحاليّة (SHIFRA: الحكمُ والمقارنة)، وأعدادُه (ihsa، bil_fia، akhta، azwaj) هي أعدادُ
   مبرهنات Jisr/KhabarQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك؛ وhalat وhuqul_masula فيه عددُ الحالات وعددُ الحقول
   المسؤولة (حكمٌ لكلّ حالة، ودرجةٌ لما متوقَّعُه «مقبول» وحده) من cases.json، ومجموعُ ihsa هو huqul_masula، ومجموعُ كلّ فئةٍ في natija_fia
   عددُ حقولها.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`.
ويفحص، إن حضر المودَعان (MUDAA_DIR/qatr.txt وalfiyya.txt ببصمتيهما)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/Khabar.lean) في أسطرها داخل نطاق مصدرها، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# » أو
   «### | ») وأسطر علامات الصفحات وحدها (PageV..P..) وتوحيد البياض، وبأدنى مدًى؛ وفي السطر 162 من القطر قبل «وقد يتعدد» (حدُّ النطاق)؛ وكلُّ
   `sanad.nass` في الحالات في سطره بحذف البادئة وحدها، وكذلك قبل «وقد يتعدد»؛ ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0، وbina_cases.py على
   المصدرين يعيد cases.json بايتًا.

الطفرات (وقاتلُ كلٍّ منها الفحصُ المسمّى وحده، إلّا ما يُذكر؛ وعُزل كلٌّ بتشغيل الاختبار على نسخةٍ مطفَّرةٍ مؤقّتة): P1119 (بصمةُ المواصفة في
tajmid.json، ١)، P1120 (بصمةُ القطر فيه، ١)، P1121 (بصمةُ bina_cases.py فيه، ١)، P1122 (بصمةُ sana_tafrat.py فيه، ١)، P1123 (معرّفُ حالةٍ بلا زوجٍ
في المولَّد، فيُبنى، ٢)، P1124 (بصمةُ الشفرة في آخر سجلّ، ٣)، P1125 (الصوابُ ونقصُ التغطية في آخر سجلّ، بمجموعٍ ثابت، ٣: مبرهنةُ natija)، P1126
(qablaha في آخر سجلّ، ٣)، P1128 (مبرهنةٌ ثانيةٌ للإخفاقات باسمٍ لا يسمّيه السجلّ، فتُبنى، ٣)، P1129 (اسمٌ ناقصٌ من حقل lean، ٣)، P1130 (akhta في
آخر سجلّ، ٣)، P1131 (bil_fia في آخر سجلّ، ٣)، P1132 (tashghil في آخر سجلّ، ٣)، P1133 (cases_sha256 في آخر سجلّ، ٣)، P1134 (halat في آخر سجلّ، ٣)،
P1135 (azwaj في آخر سجلّ، ٣)؛ وعلى Jisr/KhabarQiyas.lean وتُبنى: P1136 (`majal` بلا أعدادها، ٤)، P1137 (`natija` بلا أعدادها، ٣)، P1138 (`akhta_sifr`
بلا صيغتها، ٣)، P1139 (`natija_fia` خاصّةً فلا يجدها فحصُ الأسماء `^theorem`، ٣)، P1140 (`azwaj_1` بلا صيغتها، ٣).
**ما لا يُعزل:** P1127 (عدٌّ في natija_1.json) تقتلها المرساةُ والسلسلةُ معًا: نظيرُ المرساة وحدها يغيّر natija_1.json وqablaha في كلّ سجلٍّ بعده،
والأداةُ تستبدل موضعًا واحدًا. وP1141 (huqul_masula في آخر سجلّ) يقتلها فحصان (halat/huqul_masula ومجموعُ ihsa). وبصمةُ الحالات في tajmid.json
تقارنها ١ و٣ معًا (cases_sha256 في كلّ سجلّ)، فلا طفرةَ لها وحدها؛ وcases.json مجمَّدٌ ببصمته، وأعدادُ `majal` و`natija_fia` تقتلها Lean، وأسماءُ
السجلّات لا تطفّرها الأداة، وتتالي أرقامها فحصٌ لا نظيرَ له على المفحوص.
وطفراتُ الحكم والمقارنة (P1080–P1101، P1118، P1147، P1148) يقتلها البناء (أُفشل بكلٍّ تجميعُ الملفّ المطفَّر بـ lake env lean؛ وتشغيلُها بـ tafrat_juz.py في
وصف طلب الدمج).
التشغيل: python3 -I tahaqquq/test_khabar.py
"""
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "khabar"
SHIFRA = ["Jisr/Khabar.lean", "Jisr/KhabarDabit.lean"]
QIYAS = JADHR / "Jisr/KhabarQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_khabar.py"
BASMAT = {"قطر": ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d"),
          "ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0")}
NITAQ = {"قطر": (157, 162), "ألفية": (177, 188)}
MASDAR = {"qatr": "قطر", "alfiyya": "ألفية"}
NATIJA_1 = "647683a041f548265228411bb4518628e0f650aa916b45013c3a20bd7df5e7c3"  # natija_1.json كما أُودع في b39dc59
NS = "Jisr.Khabar.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_sifr", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "khata", "khataDaraja"]
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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/KhabarQiyas.lean: الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ، «لا حكم»، بديلان؛ ثمّ الدرجةُ
    المتوقَّعة لما متوقَّعُه «مقبول»: قليل، بتأويل، بلا درجة، بديلان؛ ثمّ ذواتُ الزوج؛ ثمّ الفئاتُ بترتيب FIAT."""
    hukm = [h["hukm"] for h in halat]
    maq = [h["daraja"] for h in halat if h["hukm"] == "مقبول"]
    mj = [len(halat)] + [hukm.count(d) for d in ("مقبول", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in hukm if isinstance(x, list))]
    mj += [maq.count(d) for d in ("قليل", "بتأويل", "بلا_درجة")] + [sum(1 for x in maq if isinstance(x, list))]
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


def huqul(halat, fia=None):
    """عددُ الحقول المسؤولة: حكمٌ لكلّ حالة، ودرجةٌ لما متوقَّعُه «مقبول»."""
    return sum(1 + (h["hukm"] == "مقبول") for h in halat if fia is None or h["fia"] == fia)


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"), ("fahs_cases.py", "fahs_cases_sha256"),
                    ("taalif.md", "taalif_sha256"), ("bina_cases.py", "bina_cases_sha256"), ("sana_tafrat.py", "sana_tafrat_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq({m["milaf"]: m["sha256"] for m in tajmid["masadir"]} == {v[0]: v[1] for v in BASMAT.values()},
         "بصمتا المصدرين في tajmid.json غيرُ بصمتَي القطر والألفية")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/KhabarDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع في b39dc59")
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
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/KhabarQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    adad_fia = [huqul(halat, f) for f in FIAT]
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
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj_1 بصيغتها في Jisr/KhabarQiyas.lean")
    if m:
        az = akhir.get("azwaj", {})
        tahaqqaq([int(m.group(1)), int(m.group(2)), int(m.group(3))] == [az.get("jumla"), az.get("taghayyar"), az.get("sawab_maan")],
                 f"{natayij[-1].name}: azwaj {az} غيرُ مبرهنة azwaj_1")
    tahaqqaq(akhir["lean"] == LEAN_NATIJA, f"{natayij[-1].name}: حقلُ lean غيرُ القائمة المتوقَّعة LEAN_NATIJA")
    for ism in akhir["lean"]:
        qasir = ism.rsplit(".", 1)[-1]
        tahaqqaq(ism.startswith(NS) and re.search(r"^theorem %s\b" % re.escape(qasir), qiyas, re.M) is not None,
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/KhabarQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == huqul(halat),
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")
    tahaqqaq(sum(akhir["ihsa"].values()) == akhir["huqul_masula"], f"{natayij[-1].name}: مجموعُ ihsa غيرُ huqul_masula")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\] := by", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/KhabarQiyas.lean")
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

    asanid = [(q, MASDAR.get(k, k), a, b, n.replace('\\"', '"')) for q, k, a, b, n in
              re.findall(r'\("(\w+)", "(\w+)", (\d+), (\d+), "((?:[^"\\]|\\.)+)"\)', (JADHR / SHIFRA[0]).read_text(encoding="utf-8"))]
    tahaqqaq(len(asanid) >= 10, f"asanid قليلة: {len(asanid)}")
    for qaida, k, a, b, nass in asanid:
        a, b = int(a), int(b)
        tahaqqaq(k in NITAQ and NITAQ[k][0] <= a <= b <= NITAQ[k][1], f"سندُ {qaida} خارجَ نطاق {k}: {a}–{b}")
        if k in masadir:
            matn = mawsul(k, a, b)
            if k == "قطر" and b == 162:
                matn = matn.split("وقد يتعدد")[0]
            tahaqqaq(nass in matn, f"سندُ {qaida} ليس في {k} س{a}–{b}: «{nass}»")
            tahaqqaq(a == b or (nass not in mawsul(k, a + 1, b) and nass not in mawsul(k, a, b - 1)),
                     f"سندُ {qaida} أوسعُ من موضعه: س{a}–{b}")
    for h in halat:
        for s in h["sanad"]:
            k, n = s["masdar"], s["satr"]
            tahaqqaq(NITAQ[k][0] <= n <= NITAQ[k][1], f"سندُ {h['id']} خارجَ نطاق {k}: س{n}")
            satr = re.sub(r"^(### \| |~~|# )", "", masadir[k][n - 1])
            if k == "قطر" and n == 162:
                satr = satr.split("وقد يتعدد")[0]
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في {k} س{n} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), mdir], capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    with tempfile.TemporaryDirectory() as t:
        r = subprocess.run([sys.executable, "-I", str(D / "bina_cases.py"), mdir, str(pathlib.Path(t) / "cases.json")],
                           capture_output=True, text=True)
        tahaqqaq(r.returncode == 0 and (pathlib.Path(t) / "cases.json").read_bytes() == (D / "cases.json").read_bytes(),
                 "bina_cases.py لا يعيد cases.json بايتًا من المصدرين")
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{sum(len(h['sanad']) for h in halat)} للحالات في أسطرها، وفاحصُ المؤلّف 0، وbina_cases.py يعيد الحالات"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَعان غائبان)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط الخبر: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط الخبر: {najah}/{najah} — {len(halat)} حالةً، و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمتَي الشفرة الحاليّة"
      f"{ziyada}")
