"""ضابطُ «من النصّ إلى الإطار» في ل1 المجمَّد: الأسماءُ الستّة في الجملة (الحزمة P4؛ hawkama/منهج_الضوابط.md §٤).

يفحص، بلا مودَع:
١. التجميد: بصماتُ wasf.md وcases.json وfahs_cases.py وtaalif.md هي المسجَّلة في tajmid.json، وبصمتا المصدرين فيه بصمتا القطر والألفية.
٢. المولَّد: Jisr/NassItarDawabit.lean مخرجُ scripts/bina_dawabit_nass.py على cases.json بايتًا (والكلماتُ خلايا من `qari --khalaya`).
   ووضعُ الإطار في القارئ (`qari --itar`) على أربع جملٍ بتوقّعٍ يدويّ لحكم الجملة (٢ب). وخلايا شاهد الحدّ `haykal_fil_la_itar` في
   Jisr/NassItar.lean (منقولةٌ باليد) مخرجُ `qari --khalaya` لجمله الثلاث (٢ج؛ فحصُ نصٍّ يقرأ قوائمَ المبرهنة وأسماءَها من Lean).
٣. السجلّات: natija_1.json … natija_N.json متتالية، كلٌّ للحالات المجمَّدة. وبصمةُ natija_1.json ثابتةٌ هنا (NATIJA_1)، وكلُّ سجلٍّ
   بعده يحمل بصمةَ ما قبله. وآخرُها لبصمات الشفرة الحاليّة (SHIFRA: القراءةُ والمقارنةُ والقارئ)، وأعدادُه (ihsa، bil_fia، akhta، azwaj، rafd_qari)
   هي أعدادُ مبرهنات Jisr/NassItarQiyas.lean، وحقلُ lean هو LEAN_NATIJA وكلُّ اسمٍ فيه مبرهنةٌ هناك.
٤. المجال: أعدادُ المجال محسوبةٌ من cases.json هنا (majal_json)، لا من Lean، وهي قائمةُ مبرهنة `majal`؛ وhalat في آخر سجلّ، وعددُ حقول
   كلّ فئةٍ في natija_fia لا يقلّ عن حالاتها ولا يزيد على ضعفها.
ويفحص، إن حضر المودَعان (MUDAA_DIR/qatr.txt وalfiyya.txt ببصمتيهما)، ولا طفرةَ له لأنّ CI بلا مودَع:
٥. الأسانيد: كلُّ `sanad.nass` في سطره بحذف البادئة وحدها («~~» أو «# » أو «### | »)، والسطرُ في نطاق مصدره؛ ثمّ فاحصُ المؤلّف
   نفسُه (fahs_cases.py) يخرج 0.

الطفرات (وقاتلُ كلٍّ منها الفحصُ المسمّى وحده، إلّا ما يُذكر): P791 (بصمةُ المواصفة في tajmid.json، ١)، P800 (بصمةُ القطر فيه، ١)، P792 (حالةٌ في المولَّد
باسمٍ لا يقرؤه زوجٌ ولا إخفاق، فيُبنى، ٢)، P799 (القارئُ يحكم على الجملة مقلوبةً، ٢ب)، P795 (القارئُ يقرأ في الوقف، ٢)، P793 (عدٌّ في natija_1.json:
المرساةُ والسلسلةُ معًا، ٣)، P797 (qablaha في آخر سجلّ، ٣)، P801 (tashghil، ٣)، P802 (cases_sha256، ٣)، P803 (بصمةُ الشفرة، ٣)، P794 (ihsa بمجموعه، ٣)،
P805 (bil_fia، ٣)، P807 (akhta، ٣)، P808 (حقلُ lean، ٣)، P816 (azwaj، ٣)، P817 (rafd_qari، ٣)، P810 (halat، ٤)، P811 (huqul_masula، ٤)؛ وعلى Jisr/NassItarQiyas.lean وتُبنى: P804 (`natija` بلا
أعدادها، ٣)، P806 (`akhta` بغير صيغتها، ٣)، P796 (مبرهنةُ `akhta` ثانيةً باسمٍ لا يسمّيه السجلّ، ٣)، P809 (`natija_fia` خاصّة، ٣)، P818 (`azwaj_1` بغير صيغتها، ٣)، P798 (`majal` بلا أعدادها، ٤).
**ما لا يُعزل:** P799 وP795 على Qari/Main.lean، وP819 (خليّةٌ في شاهد الحدّ، ٢ج) على Jisr/NassItar.lean، وكلاهما من الشفرة المسجَّلة
بصمتُها (SHIFRA)، فيقتلها فحصُ البصمة في ٣ مع فحصها — ولا طفرةَ عليهما لا يقتلها فحصُ البصمة. وP812 وP813 وP814 وP815 تطفّر الفحصَ نفسَه (حدَّ الفئات، والحسابَ من cases.json، وتتاليَ الأرقام، والمرساة):
قتلُها لا يدلّ أنّ الفحص يلتقط عيبًا في المفحوص؛ ونظيرُها على المفحوص لا يُبنى في موضعٍ واحد: cases.json مجمَّدٌ ببصمته، وأعدادُ `majal`
و`natija_fia` تقتلها Lean، وأسماءُ السجلّات لا تطفّرها الأداة، وnatija_1.json تقتله المرساةُ والسلسلةُ معًا (P793).
التشغيل: python3 -I tahaqquq/test_nass.py
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "nass"
SHIFRA = ["Jisr/NassItar.lean", "Jisr/NassItarDabit.lean", "Qari/Main.lean"]
QIYAS = JADHR / "Jisr/NassItarQiyas.lean"
BINA = JADHR / "scripts/bina_dawabit_nass.py"
BASMAT = {"قطر": ("qatr.txt", "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d"),
          "ألفية": ("alfiyya.txt", "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0")}
NITAQ = {"قطر": [(75, 80), (219, 220), (267, 268), (337, 345)], "ألفية": [(75, 79)]}
NATIJA_1 = "09613ffd9005cb1511033e421440303a12ba4600f7e4647a07c75fa98c03ff6e"  # natija_1.json كما أُودع أوّلًا
NS = "Jisr.NassItar.Qiyas."
LEAN_NATIJA = [NS + x for x in ["majal", "natija", "natija_fia", "akhta_1", "azwaj_1"]]
HUQUL_IHSA = ["sawab", "naqsTaghtiya", "tajawuz", "qabulKhati", "raddKhati", "ikhtiyar", "khataItar", "rafdQari", "khata"]
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
    """أعدادُ المجال بترتيب `majalAadad` في Jisr/NassItarQiyas.lean: الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ، «لا حكم»، بديلان؛
    ثمّ الإطاراتُ البديلة؛ ثمّ ذواتُ الزوج؛ ثمّ الفئاتُ بترتيب FIAT."""
    hukm = [h["hukm"] for h in halat]
    mj = [len(halat)] + [hukm.count(d) for d in ("مقبول", "خطأ", "لا_حكم")]
    mj += [sum(1 for x in hukm if isinstance(x, list))]
    mj += [sum(1 for h in halat if h["itar"] and isinstance(h["itar"][0], list))]
    mj += [sum(1 for h in halat if h.get("zawj") is not None)]
    mj += [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    return mj


# ١. التجميد
tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
for milaf, haql in (("wasf.md", "wasf_sha256"), ("cases.json", "cases_sha256"),
                    ("fahs_cases.py", "fahs_cases_sha256"), ("taalif.md", "taalif_sha256")):
    tahaqqaq(sha(D / milaf) == tajmid[haql], f"بصمةُ {milaf} غيرُ المسجَّلة في tajmid.json")
tahaqqaq([(m["milaf"], m["sha256"]) for m in tajmid["masadir"]] == [BASMAT["قطر"], BASMAT["ألفية"]],
         "بصمتا المصدرين في tajmid.json غيرُ بصمتي القطر والألفية")

# ٢. المولَّد
r = subprocess.run([sys.executable, "-I", str(BINA), "--check"], capture_output=True, text=True)
tahaqqaq(r.returncode == 0, "Jisr/NassItarDawabit.lean ليس مخرجَ المولِّد: " + (r.stdout + r.stderr).strip()[-300:])

# ٢ب. وضعُ الإطار في القارئ (`qari --itar`) موصولٌ بحكم الجملة. التوقّعاتُ يدويّة: الثلاثةُ الأُوَل من النصّ — الفاعلُ مرفوع (القطر L219)،
#     والاسمُ بعد حرف الجرّ مخفوض (L337–338) —، والرابعةُ من تعيين البنّاء: الجملةُ المبدوءةُ باسمٍ خارجَ المجال (wasf.md) فلا إطارَ لها
#     ولا حكم (`la_itar_la_hukm`). العمودُ الثاني وحده (حكمُ الجملة)؛ وأحكامُ الإطارات نفسُها يثبتها Lean (`haraka_tughayyir`، `itar_min_hukm`).
QARI = JADHR / ".lake" / "build" / "bin" / "qari"
ITAR_YADAWI = [("ذَهَبَ الْوَلَدُ", "مقبول"), ("ذَهَبَ الْوَلَدَ", "خطأ"), ("فِي الدَّارِ", "مقبول"), ("الْوَلَدُ ذَهَبَ", "لا_حكم")]
if QARI.exists():
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "j.tsv"
        p.write_text("".join(f"{i}\t{s}\n" for i, (s, _) in enumerate(ITAR_YADAWI)), encoding="utf-8")
        r = subprocess.run([str(QARI), "--itar", str(p)], capture_output=True, text=True)
    sutur = [s.split("\t") for s in r.stdout.splitlines()]
    tahaqqaq(r.returncode == 0 and [s[:2] for s in sutur] == [[str(i), h] for i, (_, h) in enumerate(ITAR_YADAWI)],
             f"qari --itar: {[s[:2] for s in sutur]} غيرُ المتوقَّع اليدويّ")
else:
    tahaqqaq(False, "القارئ غيرُ مبنيّ (lake build qari)")


# ٢ج. خلايا شاهد الحدّ `haykal_fil_la_itar` في Jisr/NassItar.lean منقولةٌ باليد: هي مخرجُ `qari --khalaya` للجمل الثلاث في توثيقه، بترتيبها.
#     فحصُ نصٍّ: تُقرأ الكلماتُ من قوائم `itarat [...] = []` في المبرهنة، والأسماءُ من `let` فيها ومن `def … : Kalima` في QawaidSitta وUtur.
HAYKAL = ["حَمَى الرَّجُلُ أَبَا الْوَلَدِ", "أَبَى الرَّجُلُ الطَّعَامَ", "حَمِيَ الْمَاءُ"]


def kalima_lean(t):
    """كلمةٌ بلغة Lean `⟨[خلايا], b, b⟩` (والخليةُ عددٌ أو جمعٌ وضربٌ لأعداد) إلى (خلايا، b، b)."""
    m = re.fullmatch(r"⟨\[([\d\s,*+]*)\],\s*(true|false),\s*(true|false)⟩", t.strip())
    if not m:
        return None
    khalaya = []
    for c in m.group(1).split(","):
        jam = 0
        for juz in c.split("+"):
            darb = 1
            for x in juz.split("*"):
                darb *= int(x)
            jam += darb
        khalaya.append(jam)
    return (tuple(khalaya), m.group(2) == "true", m.group(3) == "true")


def qawaim_itarat(nass):
    """قوائمُ الكلمات في كلّ `itarat [...]` بالترتيب (عناصرُ القائمة على عمق الأقواس الأوّل)."""
    natija = []
    for m in re.finditer(r"itarat \[", nass):
        i, umq, unsur, anasir = m.end(), 0, "", []
        while not (nass[i] == "]" and umq == 0):
            ch = nass[i]
            umq += ch in "⟨[(" and 1 or 0
            umq -= ch in "⟩])" and 1 or 0
            if ch == "," and umq == 0:
                anasir.append(unsur.strip())
                unsur = ""
            else:
                unsur += ch
            i += 1
        anasir.append(unsur.strip())
        natija.append(anasir)
    return natija


nass_itar = (JADHR / "Jisr/NassItar.lean").read_text(encoding="utf-8")
m = re.search(r"theorem haykal_fil_la_itar :(.*?)decide \+kernel", nass_itar, re.S)
asma = {}
for milaf in ("Jisr/QawaidSitta.lean", "Jisr/Utur.lean"):
    for d in re.finditer(r"^def (\w+) : Kalima := (⟨[^⟩]*⟩)", (JADHR / milaf).read_text(encoding="utf-8"), re.M):
        asma[d.group(1)] = kalima_lean(d.group(2))
if m and QARI.exists():
    for d in re.finditer(r"let (\w+) : Kalima := (⟨[^⟩]*⟩)", m.group(1)):
        asma[d.group(1)] = kalima_lean(d.group(2))
    lean_jumal = [[asma.get(k) if k in asma else kalima_lean(k) for k in q] for q in qawaim_itarat(m.group(1))]
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "h.tsv"
        p.write_text("".join(f"{i}\t{s}\n" for i, s in enumerate(HAYKAL)), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(p)], capture_output=True, text=True)
    qari_jumal = []
    for satr in r.stdout.splitlines():
        ajza = satr.split("\t")
        qari_jumal.append([(tuple(int(x) for x in w.split(";")[0].split(",")), w.split(";")[1] == "1", w.split(";")[2] == "1")
                           for w in ajza[2].split("|")] if len(ajza) == 3 and ajza[1] == "QABUL" else None)
    tahaqqaq(r.returncode == 0 and lean_jumal == qari_jumal,
             f"خلايا `haykal_fil_la_itar` غيرُ مخرج qari --khalaya: {lean_jumal} مقابل {qari_jumal}")
else:
    tahaqqaq(False, "لا مبرهنةَ `haykal_fil_la_itar` في Jisr/NassItar.lean أو القارئ غيرُ مبنيّ")

# ٣. السجلّات
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"natija_(\d+)\.json$", p.name).group(1)))
arqam = [int(re.search(r"natija_(\d+)\.json$", p.name).group(1)) for p in natayij]
tahaqqaq(bool(arqam) and arqam == list(range(1, len(arqam) + 1)), f"أرقامُ السجلّات غيرُ متتالية من 1: {arqam}")
qiyas = QIYAS.read_text(encoding="utf-8")
if natayij:
    tahaqqaq(NATIJA_1 is not None and sha(natayij[0]) == NATIJA_1, "natija_1.json غيرُ ما أُودع أوّلًا")
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
    tahaqqaq(m is not None, "لا مبرهنةَ natija بصيغتها في Jisr/NassItarQiyas.lean")
    if m:
        json_ = [akhir["ihsa"][h] for h in HUQUL_IHSA]
        tahaqqaq([int(x) for x in m.group(1).split(",")] == json_, f"{natayij[-1].name}: ihsa {json_} غيرُ مبرهنة natija")
    m = re.search(r"theorem natija_fia :.*?:= by", qiyas, re.S)
    tt = tuples(m.group(0)) if m else []
    tahaqqaq(len(tt) == 5 and [t[0] for t in tt] == [akhir["bil_fia"][f] for f in FIAT],
             f"{natayij[-1].name}: bil_fia غيرُ مبرهنة natija_fia")
    adad_fia = [sum(1 for h in halat if h["fia"] == f) for f in FIAT]
    tahaqqaq(len(tt) == 5 and all(a <= sum(t) <= 2 * a for t, a in zip(tt, adad_fia)),
             f"حقولُ الفئات في natija_fia {[sum(t) for t in tt]} خارجَ حدّها من حالات cases.json {adad_fia}")
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
    tahaqqaq(m is not None, "لا مبرهنةَ azwaj_1 بصيغتها في Jisr/NassItarQiyas.lean")
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
                 f"{natayij[-1].name}: «{ism}» ليست مبرهنةً في Jisr/NassItarQiyas.lean")
    tahaqqaq(akhir["halat"] == len(halat), f"{natayij[-1].name}: halat غيرُ ما في cases.json")
    tahaqqaq(sum(akhir["ihsa"].values()) == akhir["huqul_masula"], f"{natayij[-1].name}: مجموعُ ihsa غيرُ huqul_masula")

# ٤. المجال من cases.json وحده
m = re.search(r"theorem majal : majalAadad = \[([\d, ]+)\]", qiyas)
tahaqqaq(m is not None, "لا مبرهنةَ majal بصيغتها في Jisr/NassItarQiyas.lean")
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
            k, n = s["masdar"], s["satr"]
            tahaqqaq(any(a <= n <= b for a, b in NITAQ[k]), f"سندُ {h['id']} خارجَ نطاق {k}: س{n}")
            satr = re.sub(r"^(### \| |~~|# )", "", masadir[k][n - 1])
            tahaqqaq(s["nass"] in satr, f"سندُ {h['id']} ليس في {k} س{n} بحذف البادئة وحدها")
    r = subprocess.run([sys.executable, "-I", str(D / "fahs_cases.py")], capture_output=True, text=True, cwd=str(D))
    tahaqqaq(r.returncode == 0, "فاحصُ المؤلّف رفض الحالات: " + (r.stdout + r.stderr)[-400:])
    ziyada = f"؛ و{sum(len(h['sanad']) for h in halat)} سندًا للحالات في أسطرها، وفاحصُ المؤلّف 0"
else:
    ziyada = "؛ الأسانيدُ لم تُفحص (المودَعان غائبان)"

if fashal:
    print("\n".join(fashal))
    print(f"ضابط من النصّ إلى الإطار: فشل {len(fashal)}")
    sys.exit(1)
print(f"ضابط من النصّ إلى الإطار: {najah}/{najah} — {len(halat)} حالةً و{akhir['huqul_masula']} حقلًا مسؤولًا، "
      f"و{len(arqam)} سجلًّا آخرُها natija_{arqam[-1]} لبصمات الشفرة الحاليّة{ziyada}")
