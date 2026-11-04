"""ضابطُ «الحمل من الجنس» المجمَّد (hawkama/منهج_الضوابط.md §٤؛ المصدرُ أقوالُ المالك في tahaqquq/dawabit/haml_jins/masdar.md).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وmasdar.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json.
٢. المولَّد: Jisr/HamlJinsDawabit.lean مخرجُ scripts/bina_dawabit_haml_jins.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ بعده يحمل
   بصمةَ ما قبله. وآخرُها لبصمة الشفرة الحاليّة (SHIFRA: Jisr/QabiliyyaJins.lean وJisr/HamlJinsDabit.lean)، وأعدادُه (ihsa، bil_fia، akhta)
   أعدادُ مبرهنات Jisr/HamlJinsQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`.
٥. الأسانيد: كلُّ `sanad.nass` في سطره من masdar.md بحذف رقمه والنقطة والمسافة وحدها (المصدرُ في الشجرة، فيُفحص دائمًا)؛ ثمّ فاحصُ المؤلّف
   نفسُه يخرج 0.
التشغيل: python3 -I tahaqquq/test_haml_jins.py
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "haml_jins"
SHIFRA = ["Jisr/QabiliyyaJins.lean", "Jisr/HamlJinsDabit.lean"]
QIYAS = JADHR / "Jisr/HamlJinsQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_haml_jins.py"
NATIJA_1 = "NATIJA_1_PLACEHOLDER"
NS = "Jisr.QabiliyyaJins.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "khata"]
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
AHKAM = ["مرخَّص", "لا_حكم", "ممتنع", "لا_جنس", "لا_مثال"]

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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/HamlJinsQiyas.lean: الحالات؛ ثمّ المتوقَّع: مرخَّص، لا_حكم، ممتنع، لا_جنس، لا_مثال،
    بديلان؛ ثمّ الفئات بترتيب FIAT."""
    hukm = [h["kharij"]["hukm"] for h in halat]
    mj = [len(halat)] + [hukm.count(d) for d in AHKAM] + [sum(1 for x in hukm if isinstance(x, list))]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq(tajmid["masdar"]["sha256"] == sha(D / "masdar.md"), "بصمةُ المصدر في tajmid.json غيرُ بصمة masdar.md")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/HamlJinsDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

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
    shifra_hali = {m: sha(JADHR / m) for m in SHIFRA}
    tahaqqaq(akhir["shifra"] == shifra_hali, f"{natayij[-1].name} لغير الشفرة الحاليّة: {SHIFRA} تغيّرت بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa \(natayij halat\) = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/HamlJinsQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    tahaqqaq(len(tt) == 5 and [sum(t) for t in tt] == [mj[7 + i] for i in range(5)],
             f"مجموعُ الفئات في natija_fia {[sum(t) for t in tt]} غيرُ عددها في cases.json {mj[7:12]}")
    m = re.search(r"theorem (akhta\w*) :\s*akhta \(natayij halat\) = \[(.*?)\] := by", qiyas, re.S)
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
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/HamlJinsQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat), f"{natayij[-1].name}: halat غيرُ ما في cases.json")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/HamlJinsQiyas.lean")
if m:
    g = [int(x) for x in m.group(1).split(",")]
    tahaqqaq(g == mj, f"majal {g} غيرُ ما في cases.json {mj}")

# ٥. الأسانيد على المصدر (في الشجرة)
sutur = {}
for line in (D / "masdar.md").read_text(encoding="utf-8").split("\n"):
    mm = re.match(r"^(\d+)\. (.*)$", line)
    if mm:
        sutur[int(mm.group(1))] = mm.group(2)
tahaqqaq(sorted(sutur) == list(range(1, 19)), f"أسطرُ masdar.md المرقَّمة ليست 1–18: {sorted(sutur)}")
for h in halat:
    for s in h["sanad"]:
        tahaqqaq(s["satr"] in sutur and s["nass"] in sutur[s["satr"]], f"سندُ {h['id']} ليس في س{s['satr']} من masdar.md")
r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), str(D / "masdar.md")],
                   capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])

if fashal:
    print("\n".join(fashal))
    print(f"ضابط الحمل من الجنس: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط الحمل من الجنس: {najah}/{najah} — {len(halat)} حالةً، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمتَي الشفرة الحاليّة؛ "
      f"و{sum(len(h['sanad']) for h in halat)} سندًا في أسطرها من masdar.md، وفاحصُ المؤلّف 0")
