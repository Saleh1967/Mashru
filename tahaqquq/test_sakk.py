"""ضابطُ «صكّ الجملة» المجمَّد: القوّةُ والسببُ المذكورُ والمرجع (hawkama/منهج_الضوابط.md §٤)، وتشخيصُ NABT.

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصماتُ المصادر فيه بصماتُ المودَعات.
٢. المولَّد: Jisr/SakkJumlaDawabit.lean مخرجُ scripts/bina_dawabit_sakk.py على cases.json بايتًا.
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله. وآخرُها لبصمة Jisr/SakkJumla.lean الحاليّة، وأعدادُه (ihsa، bil_fia، akhta) هي أعدادُ مبرهنات
   Jisr/SakkJumlaQiyas.lean (natija، natija_fia، akhta…)، وحقلُ lean هو LEAN_NATIJA بعينها وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال بالقيم محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat وhuqul_masula في آخر سجلّ،
   ومجموعُ كلّ فئةٍ في natija_fia عددُ حقولها المسؤولة.
٥. NABT: ذهبُ الحالات الخمس والعشرين منقولٌ هنا يدويًّا (DHAHAB) من reference.json في sonaiso/nabt (`b64401f`)، ويُقارَن بـ`dhahab25` في
   Jisr/SakkJumla.lean سطرًا سطرًا؛ ويُفحص أنّ `mukhraj25` مخرجُ الشفرة على `nabt25`، وأنّ المبرهنات `nabt_quwwa` و`nabt_marji` و`nabt_marji_C05`
   و`nabt_la_tarqiya` بصيغتها تقارنه بـ`dhahab25`. وإن حضر مستودعُ NABT (NABT_DIR، أو /home/claude/sonaiso/nabt) قورن DHAHAB بالملفّ نفسِه ببصمته.
ويفحص، إن حضرت المودَعات (MUDAA_DIR) ببصماتها، ولا طفرةَ له لأنّ CI بلا مودَع:
٦. الأسانيد: كلُّ قطعةٍ في `asanid` (Jisr/SakkJumla.lean) في أسطرها من ملفّها، على النصّ موصولَ الأسطر بحذف البادئة («~~» أو «# » أو
   «### | ») وعلامات الصفحات (PageV..P..) والمخطوط (ms..) وتوحيد البياض، وبأدنى مدًى؛ وكلُّ `sanad.nass` في الحالات في سطره بحذف البادئة
   وحدها، وسطرُه في نطاق نوع حالته كما تشترط المواصفة؛ ثمّ فاحصُ المؤلّف نفسُه (fahs_cases.py) يخرج 0.

الطفرات: P869 (بصمةُ الحالات في tajmid.json، ١)، P870 (اسمُ حالةٍ في المولَّد، ٢)، P874 (جدولُ «adaa» في المولِّد، ٢)، P871 (عدُّ الصواب في
natija_1.json، ٣)، P875 (اسمُ مبرهنة akhta، ٣)، P872 (صيغةُ مبرهنة majal، ٤)، P873 (مرجعُ N01 في dhahab25، ٥).
**على أيّ شيءٍ تقع:** كلُّها على المفحوص لا على نصّ الفحص. وأربعٌ منها تُبنى (P870 وP872 وP873 وP875)، فلا يقتلها البناء بل الاختبار.
**وثلاثٌ يقتلها فحصان:**
- P873 على Jisr/SakkJumla.lean: الفحصُ ٥ وبصمةُ الشفرة في آخر سجلّ (٣).
- P871 على natija_1.json: المرساةُ NATIJA_1 وبصمتُه في qablaha في natija_2.json (٣)، وعددُ ihsa.
- P869 على tajmid.json: بصمةُ cases.json (١) ومطابقةُ cases_sha256 في السجلّات (٣).
ومرجعُ الحالات غيرِ C في dhahab25 لا تقارنه مبرهنةٌ (`nabt_marji` على C01–C04 و`nabt_marji_C05` على C05 وحدها)، فلا يحرسه في Lean شيءٌ، ويحرسه الفحصُ ٥. ولا طفرةَ
للبند ٦ (CI بلا مودَع)، ولا لمقارنة DHAHAB بملفّ NABT (المستودعُ خارجيّ).
التشغيل: python3 -I tahaqquq/test_sakk.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "sakk"
SHIFRA = JADHR / "Jisr/SakkJumla.lean"
QIYAS = JADHR / "Jisr/SakkJumlaQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_sakk.py"
MASADIR = {
    "qatr.txt": "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
    "alfiyya.txt": "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
    "mughni.txt": "f37ac2bb4b273f59169053dd0ac2abf50a52846a7e87ddf689ee5c0b87f77e7d",
    "sibawayhi.txt": "a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625",
    "a1.txt": "25a91560a646adb6ce0eb2a1bd9d6f2d1f8fd129c535a86fd5a3da34f12162c9",
    "a2.txt": "8252ca521c91c285b0344b74ab5fc956f088447c8c7811fd5c95c6c2717b8401",
}
# «التفكير»: للأسانيد وحدها، لا للحالات (ليس في جدول المواصفة).
MASADIR_SHIFRA = dict(MASADIR, **{"a3.txt": "659db78321fa3560893e8d0f5032946783ce9101d99abfe8dafa91f354c91fe0"})
# نطاقُ كلّ نوعٍ في المواصفة (wasf.md، «المصادر والنطاق»).
NITAQ = {
    "قوة": {"sibawayhi.txt": [(1268, 1294), (1522, 1525), (9190, 9304), (9544, 9652), (9782, 9787), (10022, 10041)],
            "mughni.txt": [(2217, 2239), (5901, 5919), (6109, 6116), (6400, 6405), (6483, 6486), (9567, 9589), (9620, 9668)],
            "qatr.txt": [(108, 122), (194, 197)],
            "alfiyya.txt": [(250, 256), (296, 302), (905, 912)],
            "a2.txt": [(767, 767), (896, 896)]},
    "سبب": {"sibawayhi.txt": [(3659, 3692), (4196, 4202), (8791, 8913), (8914, 9049), (9592, 9594), (9824, 9865),
                              (10143, 10221), (11484, 11574), (18400, 18405)],
            "mughni.txt": [(643, 687), (709, 712), (2748, 2848), (3660, 3697), (4158, 4163), (4781, 4802), (7555, 7608),
                           (11032, 11040), (12964, 13006)],
            "qatr.txt": [(50, 51), (97, 97), (108, 109), (293, 298)],
            "alfiyya.txt": [(399, 401), (491, 491), (534, 534), (895, 895)],
            "a1.txt": [(269, 271)], "a2.txt": [(1040, 1040)]},
    "مرجع": {"qatr.txt": [(123, 133)], "alfiyya.txt": [(105, 105), (138, 140)],
             "sibawayhi.txt": [(4434, 4551), (5203, 5248)], "a2.txt": [(749, 749), (918, 918), (1419, 1419)]},
}
NATIJA_1 = "64bb617f91fd1d1f04c1883df3dbffa5d1b52c70855e1c8c67ec49c7cb43c246"  # natija_1.json كما أُودع أوّلًا
NS = "Jisr.SakkJumla.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_3"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "ikhtiyar", "khata"]
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
NABT_REF = "evidence/semantic_axes_v1/revision_2/reference.json"
NABT_SHA = "9787e4496118a80a4f352ef19193e1e37976eb282eaf96caaad511ce77ffa431"
# ذهبُ NABT منقولًا يدويًّا من reference.json: (القوّةُ الأولى، قوىُ الثانية، الدافع، المرجع، الواقع).
A = ("assertPos", [], "underdetermined", "notApplicable", "notEstablished")
DHAHAB = {f"{x}0{n}": A for x in "NVT" for n in range(1, 6)}
DHAHAB.update({
    "C01": (A[0], [], A[2], "resolved", A[4]), "C02": (A[0], [], A[2], "resolved", A[4]),
    "C03": (A[0], [], A[2], "resolved", A[4]), "C04": (A[0], [], A[2], "resolved", A[4]),
    "C05": (A[0], [], A[2], "ambiguous", A[4]),
    "Q01": ("assertNeg", [], A[2], A[3], A[4]),
    "Q02": ("hypothetical", ["hypothetical"], A[2], A[3], A[4]),
    "Q03": ("assertPos", ["quoted"], A[2], A[3], A[4]),
    "Q04": ("assertNeg", ["quoted"], A[2], A[3], A[4]),
    "Q05": ("hypothetical", ["hypothetical"], A[2], A[3], A[4]),
})
TARTIB = [f"{x}0{n}" for x in "NVTCQ" for n in range(1, 6)]

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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/SakkJumlaQiyas.lean، والحقولُ المسؤولة جملةً وبالفئة."""
    q = [h for h in halat if h["naw"] == "قوة"]
    s = [h for h in halat if h["naw"] == "سبب"]
    m = [h for h in halat if h["naw"] == "مرجع"]

    def bil_qiyam(qiyam, l):
        l = [qaima(x) for x in l]
        return [sum(1 for x in l if x == [v]) for v in qiyam] + [sum(1 for x in l if len(x) >= 2)]

    masul = 2 * len(q) + len(s) + len(m)
    mj = [len(q), len(s), len(m), masul]
    mj += bil_qiyam(["إثبات", "نفي", "تعليق", "إنشاء", "لا_حكم"], [h["kharij"]["awwal"] for h in q])
    mj += bil_qiyam(["إثبات", "نفي", "تعليق", "حكاية", "ظن", "لا_ثاني", "لا_حكم"], [h["kharij"]["thani"] for h in q])
    mj += bil_qiyam(["علة", "سببية", "غير_مذكور", "لا_حكم"], [h["kharij"]["sabab"] for h in s])
    mj += bil_qiyam(["معين", "محتمل", "لا_حكم"], [h["kharij"]["marji"] for h in m])
    fia = {f: 0 for f in FIAT}
    for h in halat:
        fia[h["fia"]] += 2 if h["naw"] == "قوة" else 1
    return mj, masul, fia


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq({x["milaf"]: x["sha256"] for x in tajmid["masadir"]} == MASADIR and len(tajmid["masadir"]) == len(MASADIR),
         "بصماتُ المصادر في tajmid.json غيرُ بصمات المودَعات")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/SakkJumlaDawabit.lean ليس مخرجَ المولِّد: " + r.stdout.strip())

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
mj, masul, masul_fia = majal_json(halat)
if akhir:
    tahaqqaq(akhir["shifra"]["sha256"] == sha(SHIFRA),
             f"{natayij[-1].name} لغير الشفرة الحاليّة: Jisr/SakkJumla.lean تغيّر بعد آخر تشغيل")
    m = re.search(r"theorem natija : ihsa natayij = ⟨([\d, ]+)⟩", qiyas)
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/SakkJumlaQiyas.lean")
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
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/SakkJumlaQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat) and akhir["huqul_masula"] == masul,
             f"{natayij[-1].name}: halat/huqul_masula غيرُ ما في cases.json")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/SakkJumlaQiyas.lean")
if m:
    g = [int(x) for x in m.group(1).split(",")]
    tahaqqaq(g == mj, f"majal {g} غيرُ ما في cases.json {mj}")

# ٥. NABT
shifra = SHIFRA.read_text(encoding="utf-8")
m = re.search(r"def dhahab25 : List \(String × MukhrajNabt\) := \[\n(.*?)\]\n\n", shifra, re.S)
tahaqqaq(m is not None, "لا dhahab25 بصيغتها في Jisr/SakkJumla.lean")
if m:
    sutur = re.findall(r'\("(\w\d\d)", ⟨\.(\w+), \[([^\]]*)\], \.(\w+), \.(\w+), \.(\w+)⟩\)', m.group(1))
    lean_dh = {i: (a, [x.strip().lstrip(".") for x in t.split(",") if x.strip()], d, r_, w) for i, a, t, d, r_, w in sutur}
    tahaqqaq([s[0] for s in sutur] == TARTIB, f"حالاتُ dhahab25 غيرُ الخمس والعشرين بترتيبها: {[s[0] for s in sutur]}")
    for i in TARTIB:
        tahaqqaq(lean_dh.get(i) == DHAHAB[i], f"dhahab25 في {i}: {lean_dh.get(i)} غيرُ المنقول {DHAHAB[i]}")
tahaqqaq(re.search(r"^def mukhraj25 : List \(String × MukhrajNabt\) := nabt25\.map \(fun p => \(p\.1, sakkNabt \.laHukm p\.2\)\)$",
                   shifra, re.M) is not None, "لا mukhraj25 بصيغتها")
for ism in ("nabt_quwwa", "nabt_marji", "nabt_marji_C05", "nabt_la_tarqiya"):
    m = re.search(r"^theorem %s :(.*?):= by\n  decide$" % ism, shifra, re.M | re.S)
    tahaqqaq(m is not None and "mukhraj25" in m.group(1) and "dhahab25" in m.group(1),
             f"لا مبرهنةَ {ism} بصيغتها (mukhraj25 مقابل dhahab25)")
nabt_dir = pathlib.Path(os.environ.get("NABT_DIR", "/home/claude/sonaiso/nabt"))
nabt_nass = ""
if (nabt_dir / ".git").exists():
    r = subprocess.run(["git", "-C", str(nabt_dir), "show", f"b64401f:{NABT_REF}"], capture_output=True)
    if r.returncode == 0 and hashlib.sha256(r.stdout).hexdigest() == NABT_SHA:
        ref = json.loads(r.stdout.decode("utf-8"))
        QUWWA = {("ASSERT", True): "assertPos", ("ASSERT", False): "assertNeg", ("HYPOTHETICAL", True): "hypothetical",
                 ("QUOTED", True): "quoted"}
        MARJI = {"resolved": "resolved", "ambiguous": "ambiguous", "unresolved": "unresolved",
                 "not_applicable": "notApplicable"}
        for c in ref["cases"]:
            e = c["expected"]
            qq = [QUWWA.get((x["force"], x["positive"]), "?") for x in e["readings"]["required"]]
            min_al_milaf = (qq[0], qq[1:], e["motive"]["status"], MARJI.get(e["reference"]["status"], "?"),
                            {"not_established": "notEstablished"}.get(e["world"]["status"], "?"))
            tahaqqaq(DHAHAB.get(c["id"]) == min_al_milaf, f"DHAHAB في {c['id']} غيرُ reference.json: {min_al_milaf}")
        tahaqqaq([c["id"] for c in ref["cases"]] == TARTIB, "حالاتُ reference.json غيرُ الخمس والعشرين بترتيبها")
        nabt_nass = "، وDHAHAB بملفّ NABT نفسِه"

# ٦. الأسانيد على المودَع
mdir = os.environ.get("MUDAA_DIR")
hadir = bool(mdir) and all((pathlib.Path(mdir) / f).exists() and sha(pathlib.Path(mdir) / f) == b
                           for f, b in MASADIR_SHIFRA.items())
if hadir:
    cache = {}

    def sutur_milaf(f):
        if f not in cache:
            cache[f] = (pathlib.Path(mdir) / f).read_text(encoding="utf-8").split("\n")
        return cache[f]

    def nazzif(s):
        s = re.sub(r"^(~~|# |### \| )", "", s)
        s = re.sub(r"PageV\d+P\d+|ms\d+", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    def mawsul(f, a, b):
        # سطرُ علامة الصفحة وحدها يصير فارغًا فلا يُدخل بياضًا ثانيًا (توحيدُ البياض)
        return " ".join(x for x in (nazzif(sutur_milaf(f)[i - 1]) for i in range(a, b + 1)) if x)

    asanid = re.findall(r'\("(\w+)", "([\w.]+)", (\d+), (\d+), "([^"]+)"\)', shifra)
    tahaqqaq(len(asanid) >= 40, f"asanid قليلة: {len(asanid)}")
    tahaqqaq(len({x[0] for x in asanid}) == len(asanid), "أسماءٌ مكرّرة في asanid")
    for qaida, f, a, b, nass in asanid:
        a, b = int(a), int(b)
        tahaqqaq(f in MASADIR_SHIFRA, f"سندُ {qaida} من ملفٍّ غير معلن: {f}")
        if f not in MASADIR_SHIFRA:
            continue
        tahaqqaq(nass in mawsul(f, a, b), f"سندُ {qaida} ليس في {f} س{a}–{b}: «{nass}»")
        tahaqqaq(a == b or (nass not in mawsul(f, a + 1, b) and nass not in mawsul(f, a, b - 1)),
                 f"سندُ {qaida} أوسعُ من موضعه: {f} س{a}–{b}")
    nh = 0
    for h in halat:
        for s in h["sanad"]:
            nh += 1
            satr = re.sub(r"^(~~|# |### \| )", "", sutur_milaf(s["milaf"])[s["satr"] - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في {s['milaf']} س{s['satr']} بحذف البادئة وحدها")
            tahaqqaq(any(a <= s["satr"] <= b for a, b in NITAQ[h["naw"]].get(s["milaf"], [])),
                     f"سندُ {h['id']} خارجَ نطاق نوعه: {s['milaf']} س{s['satr']}")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py"), str(D / "cases.json"), "--src", mdir,
                        "--wasf", str(D / "wasf.md")], capture_output=True, text=True)
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{len(asanid)} سندًا للشفرة و{nh} للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَعات غائبة)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط صكّ الجملة: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط صكّ الجملة: {najah}/{najah} — {len(halat)} حالةً و{masul} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمة الشفرة الحاليّة؛ وذهبُ NABT الخمسُ والعشرون{nabt_nass}{ziyada}")
