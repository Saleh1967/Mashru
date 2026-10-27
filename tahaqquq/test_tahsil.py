"""التحصيلُ المحاذي وشهادتُه (Dal/Tahsil.lean، والأداة `tahsil`) على عرّافٍ مستقلّ (tahaqquq/tahsil/).

العرّافُ (oracle.py) وحالاتُه (boundary.json، boundary_kalimat.json) كتبها مؤلّفٌ لم يقرأ إلّا المواصفة wasf.md، وفي سياقه ما حُقن آليًّا
(tawjih_arraf.md)؛ وتوقّعاتُ الحالات مشتقّةٌ باليد لا بتشغيل العرّاف (boundary_src.py). ومواضعُ الغموض في NOTES.md قرأها البنّاء قبل كتابة
التصنيف، فاتّفاقُ الأداة والعرّاف فيها ليس شاهدًا مستقلًّا. يفحص، بلا مودَع:
١. البصمات: ملفّاتُ المواصفة والعرّاف وحالاته وفاحصِها (check_boundary.py) هي المسجَّلة في basamat.json، فلا يتغيّر شيءٌ منها صامتًا.
٢. الحدود: مخرجُ `tahsil` على كلّ حالةٍ في boundary.json وboundary_kalimat.json هو توقّعُها بعينه؛ والعرّافُ نفسُه يوافقها (check_boundary.py).
٣. العشوائيّ: على 7000 نصٍّ بالبذرة 20261027 — 3000 حروفُها مبعثرةٌ من أبجديّةٍ فيها الحواملُ ومقاعدُ الهمزة والخاصّةُ والعلاماتُ الثماني
   وحروفٌ خارج الجدول، و3000 رؤوسٌ بعد كلٍّ منها علامتان على الأكثر، و1000 فيها ألفٌ ولامٌ بعد صدرٍ قد يكون فارغًا (لقاعدة لام التعريف) —
   مخرجُ `tahsil` للمقاطع والكلمات هو مخرجُ oracle.py. ويُطبع عددُ أسماء الأحكام التي بلغها، ولا يُشترط.
٤. الشهادة: حكمُ الفاحص على شهادة كلّ مقطع (`Nizam.Shahada.hukm`، العمودُ الأخير) صورةُ حكم التصنيف: L ← murakhkhas، P ← muallaq:الاسم،
   F ← madkhalFasid:الاسم؛ على مقاطع ٢ و٣ كلّها.
٥. القارئ: على كلماتٍ عشوائيّة (البذرة 20261028) يرخّصها التحصيلُ كلَّها، وهي ألفٌ على الأقلّ، خلايا `qari --khalaya` هي خلايا التحصيل
   (والمبرهنةُ `Dal.QiraaTahsil.qiraa_murakhkhasa`؛ وهذا فحصُ المنفَّذ). وعلى خمسين كلمةً فيها علامتا حركة على حرفٍ واحد يردّها التحصيلُ
   «علامتان متعارضتان»: يردّها القارئُ كلَّها باسمه (وكان قبل وصله بالتحصيل يقرؤها ويأخذ الأخيرة).
٦. الأسماء: كلُّ اسمٍ لحكمٍ P أو F في Dal/Tahsil.lean في wasf.md بين «» بنصّه (فحصُ نصّ)، إلّا «مقطع فارغ» و«خلل داخلي» اللذين لا يصل
   إليهما مقطعٌ، ولا يظهران في مخرجٍ من ٢ و٣.

الطفرات وقاتلُها في البوّابة (أوّلُ اختبارٍ يفشل): P880 (ألفُ الجماعة في غير آخر الكلمة)، P881 (كلُّ سابقٍ أوّلُ كلمته)، P882 (اللاحقُ عبر
الفراغ)، P884 (كلُّ كلمةٍ مرخَّصة)، P885 (كلمةٌ بلا خلايا مرخَّصة)، كلُّها ٢ أو ٣؛ وP883 (اسمُ التعليق في عمود الشهادة، ٤)، وP888 (اسمٌ في Lean
ليس في المواصفة، ٦)، وP886 (قاعدةُ التنوين في العرّاف، ١ بالبصمة، ويقتلها معه ٢ و٣).
**ما لا يُعزل:** ٥ لا طفرةَ تعزله، لأنّ كلَّ تغييرٍ في القارئ يقتله قبله test_qari.py أو فحصُ بصمة القارئ في test_nass.py: فـP887 (خليّةُ الشدّة في
القارئ) يقتلها test_qari.py، وطُفّرت في شجرة العمل نفسِها ثمّ أُعيدت فقتلها ٥ وحده (لا بـtafrat_juz.py). ولا طفرةَ لاتّفاق العرّاف مع حالاته في ٢ ولا لِما في ٦ من عدم الظهور،
لأنّ ما يكسرهما يكسر قبلهما ١ أو ٢؛ ولا لحدِّ الألف في ٥.
التشغيل: python3 -I tahaqquq/test_tahsil.py
"""
import hashlib
import json
import pathlib
import random
import re
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "tahsil"
TAHSIL = JADHR / ".lake" / "build" / "bin" / "tahsil"
QARI = JADHR / ".lake" / "build" / "bin" / "qari"
LEAN = JADHR / "Dal" / "Tahsil.lean"
GHAYR_WASIL = {"مقطع فارغ", "خلل داخلي"}

sys.path.insert(0, str(D))
import oracle  # noqa: E402

fails = []


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def shaghghil(nusus):
    """يشغّل الأداة على قائمة نصوص، ويعيد لكلّ نصٍّ (مقاطع، كلمات، أحكام الشهادة)."""
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "in.tsv"
        p.write_text("".join(f"{i}\t{' '.join(str(ord(c)) for c in t)}\n" for i, t in enumerate(nusus)), encoding="utf-8")
        r = subprocess.run([str(TAHSIL), str(p)], capture_output=True, text=True)
    if r.returncode != 0:
        fails.append(f"tahsil خرج {r.returncode}: {r.stderr[-300:]}")
        return None
    out = [([], [], []) for _ in nusus]
    for line in r.stdout.split("\n"):
        if not line:
            continue
        f = line.split("\t")
        k = int(f[0])
        if f[1] == "M":
            cells = [int(x) for x in f[8].split(",") if x]
            out[k][0].append({"i": int(f[2]), "a": int(f[3]), "b": int(f[4]), "hukm": f[5], "sinf": f[6], "ism": f[7],
                              "khalaya": cells})
            out[k][2].append(f[9])
        elif f[1] == "K":
            cells = [int(x) for x in f[5].split(",") if x]
            out[k][1].append({"a": int(f[2]), "b": int(f[3]), "murakhkhasa": f[4] == "1", "khalaya": cells})
        else:
            fails.append(f"سطرٌ غيرُ متوقَّع من tahsil: {line[:100]}")
    return out


def shahada_matlub(m):
    if m["hukm"] == "L":
        return "murakhkhas"
    if m["hukm"] == "P":
        return "muallaq:" + m["ism"]
    return "madkhalFasid:" + m["ism"]


def fahs_shahada(nusus, out, wasf):
    for t, (ms, _, sh) in zip(nusus, out):
        for m, s in zip(ms, sh):
            if s != shahada_matlub(m):
                fails.append(f"٤ ({wasf}): شهادةُ المقطع {m['i']} في {t!r}: {s!r}، والمتوقَّع {shahada_matlub(m)!r}")
                return


def ghayr_wasil(nusus, out, wasf):
    for t, (ms, _, _) in zip(nusus, out):
        for m in ms:
            if m["ism"] in GHAYR_WASIL:
                fails.append(f"٦ ({wasf}): «{m['ism']}» في مخرج {t!r}")
                return


# ١. البصمات
basamat = json.loads((D / "basamat.json").read_text(encoding="utf-8"))
for f, b in basamat.items():
    if sha(D / f) != b:
        fails.append(f"١: بصمةُ {f} تغيّرت")
print(f"١ البصمات: {len(basamat)} ملفًّا")

# ٢. الحدود
hudud = json.loads((D / "boundary.json").read_text(encoding="utf-8"))
hudud_k = json.loads((D / "boundary_kalimat.json").read_text(encoding="utf-8"))
nusus2 = [c["nass"] for c in hudud] + [c["nass"] for c in hudud_k]
out2 = shaghghil(nusus2)
if out2 is not None:
    for c, o in zip(hudud, out2):
        if o[0] != c["tawaqqu"]:
            fails.append(f"٢: «{c.get('label', '')}» {c['nass']!r}: {o[0]} ≠ {c['tawaqqu']}")
    for c, o in zip(hudud_k, out2[len(hudud):]):
        if o[1] != c["tawaqqu"]:
            fails.append(f"٢ (الكلمات): «{c.get('label', '')}» {c['nass']!r}: {o[1]} ≠ {c['tawaqqu']}")
    fahs_shahada(nusus2, out2, "الحدود")
    ghayr_wasil(nusus2, out2, "الحدود")
r = subprocess.run([sys.executable, "-I", str(D / "check_boundary.py")], capture_output=True, text=True)
if r.returncode != 0:
    fails.append("٢: العرّافُ يخالف حالاته: " + r.stdout[-300:])
print(f"٢ الحدود: {len(hudud)} حالةً للمقاطع و{len(hudud_k)} للكلمات")

# ٣. العشوائيّ
rng = random.Random(20261027)
HAWAMIL = list(oracle.TABLE)
MAQAID = list(oracle.SEATS)
KHASSA = ["ة", "ى", "آ", "ٱ", "ـ", " "]
ALAMAT = ["َ", "ُ", "ِ", "ْ", "ً", "ٌ", "ٍ", "ّ"]
KHARIJ = ["\t", "ٰ", "،", "a", "٣", "ٓ", "ک"]


def harf_ashwai():
    x = rng.random()
    if x < 0.35:
        return rng.choice(ALAMAT)
    if x < 0.75:
        return rng.choice(HAWAMIL)
    if x < 0.80:
        return rng.choice(MAQAID)
    if x < 0.92:
        return rng.choice(KHASSA)
    return rng.choice(KHARIJ)


def wahda_ashwaiyya():
    """رأسٌ من الجدول أو المقاعد أو الخاصّة، وبعده من صفرٍ إلى علامتين — أقربُ إلى النصّ المشكول من الحروف المبعثرة."""
    x = rng.random()
    ras = rng.choice(HAWAMIL) if x < 0.7 else rng.choice(MAQAID) if x < 0.78 else rng.choice(KHASSA) if x < 0.95 else rng.choice(KHARIJ)
    y = rng.random()
    alamat = [] if y < 0.2 else [rng.choice(ALAMAT[:4])] if y < 0.75 else [rng.choice(ALAMAT[4:7])] if y < 0.85 else \
        rng.sample(["\u0651", rng.choice(ALAMAT[:4])], 2)
    return ras + "".join(alamat)


def al_ashwaiyya():
    """صدرٌ من صفرٍ إلى وحدتين، ثمّ ألفٌ (أو ألفُ وصل) ولامٌ بعلامةٍ أو بدونها، ثمّ حرفٌ مشدَّدٌ أو غيرُه، ثمّ ما يليه — لقاعدة لام التعريف
    وما يجاورها، ولا تبلغها الأسرتان قبلها."""
    sadr = "".join(wahda_ashwaiyya() for _ in range(rng.choice([0, 0, 1, 2])))
    alif = rng.choice(["ا", "ٱ", "ا\u064e"])
    lam = "ل" + rng.choice(["", "", "\u0652", "\u064e"])
    tali = rng.choice(HAWAMIL) + rng.choice(["\u0651\u064e", "\u064e\u0651", "\u064e", "\u0651"])
    baqi = "".join(wahda_ashwaiyya() for _ in range(rng.randint(0, 3)))
    return sadr + alif + lam + tali + baqi + rng.choice(["", "", " " + wahda_ashwaiyya()])


nusus3 = (["".join(harf_ashwai() for _ in range(rng.randint(0, 14))) for _ in range(3000)] +
          ["".join(wahda_ashwaiyya() for _ in range(rng.randint(1, 8))) for _ in range(3000)] +
          [al_ashwaiyya() for _ in range(1000)])
out3 = shaghghil(nusus3)
khilaf = 0
if out3 is not None:
    for t, o in zip(nusus3, out3):
        if o[0] != oracle.tahsil(t) or o[1] != oracle.kalimat(t):
            khilaf += 1
            if khilaf <= 3:
                fails.append(f"٣: {t!r}: tahsil {o[0]} {o[1]}؛ العرّاف {oracle.tahsil(t)} {oracle.kalimat(t)}")
    fahs_shahada(nusus3, out3, "العشوائيّ")
    ghayr_wasil(nusus3, out3, "العشوائيّ")
    maqati = sum(len(o[0]) for o in out3)
    ahkam = {h: sum(1 for o in out3 for m in o[0] if m["hukm"] == h) for h in "LPF"}
    asma3 = {m["ism"] for o in out3 for m in o[0] if m["ism"]}
    print(f"٣ العشوائيّ: {len(nusus3)} نصٍّ، {maqati} مقطعًا (L {ahkam['L']}، P {ahkam['P']}، F {ahkam['F']})، "
          f"{len(asma3)} اسمًا للتعليق والفساد؛ خلافٌ مع العرّاف: {khilaf}")

# ٥. القارئ
rng5 = random.Random(20261028)
HARAKAT = ALAMAT[:4]


def kalima_ashwaiyya():
    w = ""
    for _ in range(rng5.randint(1, 5)):
        w += rng5.choice(HAWAMIL + MAQAID)
        x = rng5.random()
        if x < 0.75:
            w += rng5.choice(HARAKAT)
        elif x < 0.9:
            w += "ّ" + rng5.choice(HARAKAT)
    return w


kalimat5 = [kalima_ashwaiyya() for _ in range(2000)]
out5 = shaghghil(kalimat5)
if out5 is not None:
    murakhkhasa = [(w, o[1][0]["khalaya"]) for w, o in zip(kalimat5, out5) if len(o[1]) == 1 and o[1][0]["murakhkhasa"]]
    harakatan = [rng5.choice(HAWAMIL) + rng5.choice(HARAKAT) + rng5.choice(HARAKAT) + rng5.choice(HAWAMIL) + rng5.choice(HARAKAT)
                 for _ in range(50)]
    out5b = shaghghil(harakatan)
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "q.tsv"
        p.write_text("".join(f"{i}\t{w}\n" for i, (w, _) in enumerate(murakhkhasa)) +
                     "".join(f"h{i}\t{w}\n" for i, w in enumerate(harakatan)), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(p)], capture_output=True, text=True)
    sawa = 0
    radd_harakatan = 0
    for line in r.stdout.split("\n"):
        if not line:
            continue
        k, hal, baqi = line.split("\t", 2)
        if k.startswith("h"):
            i = int(k[1:])
            mardud = out5b is not None and out5b[i][0][0]["ism"] == "علامتان متعارضتان"
            if mardud and hal == "RAFD" and "علامتان متعارضتان: «" in baqi:
                radd_harakatan += 1
            continue
        w, ks = murakhkhasa[int(k)]
        cells = [int(x) for x in baqi.split(";")[0].split(",") if x] if hal == "QABUL" else None
        if cells == ks:
            sawa += 1
        elif sawa + 1 < 4:
            fails.append(f"٥: {w!r}: القارئ {hal} {baqi[:60]}، والتحصيل {ks}")
    if sawa != len(murakhkhasa) or len(murakhkhasa) < 1000:
        fails.append(f"٥: سواءٌ {sawa} من {len(murakhkhasa)} كلمةً مرخَّصة")
    if radd_harakatan != len(harakatan):
        fails.append(f"٥: علامتا حركةٍ على حرف: يردّها القارئ «علامتان متعارضتان» في {radd_harakatan} من {len(harakatan)}")
    print(f"٥ القارئ: {sawa} من {len(murakhkhasa)} كلمةً يرخّصها التحصيل خلاياها في القارئ هي هي؛ "
          f"وعلامتا حركةٍ على حرف: يردّها القارئ والتحصيلُ باسمها في {radd_harakatan} من {len(harakatan)}")

# ٦. الأسماء
lean = LEAN.read_text(encoding="utf-8")
wasf = (D / "wasf.md").read_text(encoding="utf-8")
asma = set(re.findall(r'\.(?:P|F) "([^"]+)"', lean))
fi_wasf = set(re.findall(r"«([^»]+)»", wasf))
naqis = sorted(asma - fi_wasf - GHAYR_WASIL)
if naqis:
    fails.append(f"٦: أسماءٌ في Dal/Tahsil.lean ليست في المواصفة: {naqis}")
print(f"٦ الأسماء: {len(asma)} اسمًا في Lean، منها {len(asma & fi_wasf)} في المواصفة و{len(asma & GHAYR_WASIL)} لا يصل إليه مقطع")

if fails:
    for f in fails:
        print("خلل:", f)
    print(f"التحصيل: فشل ({len(fails)})")
    sys.exit(1)
print("التحصيل: نجح")
