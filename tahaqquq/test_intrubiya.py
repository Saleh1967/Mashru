"""هيكلُ الإنتروبيا (Jisr/Intrubiya.lean، Jisr/IntrubiyaShahada.lean، scripts/intrubiya.py، scripts/bina_intrubiya_shahada.py).

توقّعاتُه مستقلّةٌ عن الشيفرة المفحوصة. يفحص، بلا مودَع:
١. العدّ: تعدادٌ صريحٌ لكلمات الطول 3 كلِّها (116³) على law.json مباشرةً، وتجميعٌ بالحالة حتى 4، يساويان أعدادًا منسوخةً هنا من `#eval
   lawCount` في Lean (لا من بايثون)؛ و`Qanun.adad` يساويها حتى 12؛ والأعدادُ نفسُها نصُّ `adad_waqf`/`adad_wasl` في Lean.
٢. الشهادة: الملفّ المولَّد هو مخرجُ المولِّد بالبايت، ومتباينتاه صادقتان بأعدادٍ صحيحةٍ محسوبةٍ هنا مستقلّةً عن المولِّد، والحدّان
   يحصران نسبةَ نموّ الأعداد المنسوخة.
٣. المقدِّرات: H وMiller–Madow على توزيعاتٍ قيمُها باليد.
٤. البناء على مداخلَ مصنوعة: الحاملُ والحالةُ مستقلّان ⇒ I = 0؛ مرتبطان ⇒ I = 1؛ الخلايا تُنقل بالجسر قبل الآلة (كَتَبَ في Mashru
   32,72,104 ← حالةُ البداية ترى ذرّة NABT 84)؛ محاسبةُ الخانات 96 × 116؛ والغيابُ ليس امتناعًا.
٥. الجسر: جدولُ `nabtBridge` تقابليّ، وصفوفٌ باليد من جدولَي المخارج (Dal/Makharij.lean) وNABT (Nabt/Cell.lean).
٦. التحصيل: الأداةُ `tahsil` على كلماتٍ خلاياها مشتقّةٌ باليد من الجدولين ومن المواصفة tahaqquq/tahsil/wasf.md (كَتَبَ، رَبِّ، أَنْ، فِي،
   و«الْحَمْدُ» بهمزة أل منذ التعديل الثالث، والمعلَّقُ «اعْبُدُوا» باسم قاعدته).
٧. الختم: بصمةُ مودَعٍ خاطئة تُرفض قبل أيّ قراءة.
ومع المودَع (MUDAA_DIR فيه quran-simple-enhanced.txt ببصمته المسجَّلة مرشّحًا): هويّاتُ المحاسبة على المودَع كلِّه، وإعادةُ المخرج بالبايت.

الطفرات وقاتلُها: P930–P937 (Jisr/Intrubiya.lean وJisr/IntrubiyaShahada.lean) يقتلها البناء؛ وP938–P945 (scripts/intrubiya.py) وP946
(المولِّد) يقتلها هذا الاختبار: P938 بـ٤ (النقل)، وP939 بـ٣، وP940 بـ١، وP941 وP942 بـ٤، وP943 بـ٤، وP944 بـ٧، وP945 بـ٦، وP946 بـ٢.
التشغيل: python3 -I tahaqquq/test_intrubiya.py
"""

import json
import math
import os
import pathlib
import re
import subprocess
import sys
import tempfile
from collections import Counter

JADHR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(JADHR / "scripts"))
import intrubiya as it  # noqa: E402

LAW = JADHR / "jadawil" / "law.json"
SHAHADA = JADHR / "Jisr" / "IntrubiyaShahada.lean"
QURAN_SHA = "37633090743d403886b334d12dd911d1994e49767faa9f2be0f01fd48b466c5a"

# من `#eval (List.range 13).map (lawCount false)` و`(lawCount true)` في Lean، منسوخةً يدويًّا
LEAN_WAQF = [0, 84, 9436, 1052128, 110116720, 11666282992, 1232884139200, 130357303246912,
             13781695424115136, 1457066346148274176, 154047295783696123648,
             16286554839002537565952, 1721885591168655910466560]
LEAN_WASL = [0, 84, 9436, 987840, 104650672, 11059529712, 1169361417280, 123627829926720,
             13070520528415168, 1381871448257674752, 146097501524599749376,
             15446064896990387052288, 1633025392049327181638656]

# جدولا الحوامل باليد: Dal/Makharij.lean (hawamil) وNabt/Cell.lean (canonicalCarriers)
MASHRU = "ءهاعحغخقكجشيضلنرطدتزسصظذثفبمو"
NABT = "ابتثجحخدذرزسشصضطظعغفقكلمنهويء"
FAIL = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


def m(harf, hala):            # رقمُ خلية Mashru
    return 4 * MASHRU.index(harf) + hala


def nb(harf, hala):           # ذرّةُ NABT
    return 4 * NABT.index(harf) + hala


def law_tables():
    d = json.loads(LAW.read_text(encoding="utf-8"))
    return [[t[0] for t in row] for row in d["transitions"]], d["final_waqf"], d["final_wasl"]


def T(step, f):
    return [sum(f[step[q][a]] for a in range(116)) for q in range(97)]


def main():
    step, fw, fs = law_tables()
    qanun = it.Qanun()

    # ١
    k = 0
    for a in range(116):
        for b in range(116):
            qb = step[step[0][a]][b]
            for c in range(116):
                k += fw[step[qb][c]]
    check("تعدادٌ صريحٌ لـ116³ = lawCount false 3", k == LEAN_WAQF[3])
    front = Counter({0: 1})
    ok = True
    for n in range(5):
        ok &= (sum(c for q, c in front.items() if fw[q]), sum(c for q, c in front.items() if fs[q])) == (LEAN_WAQF[n], LEAN_WASL[n])
        nxt = Counter()
        for q, c in front.items():
            for a in range(116):
                nxt[step[q][a]] += c
        front = nxt
    check("تجميعٌ بالحالة حتى 4 = Lean", ok)
    check("Qanun.adad وقفًا = Lean حتى 12", qanun.adad(False, 12) == LEAN_WAQF)
    check("Qanun.adad وصلًا = Lean حتى 12", qanun.adad(True, 12) == LEAN_WASL)
    src = SHAHADA.read_text(encoding="utf-8")
    # بالعدد كاملًا لا ببادئته: «= 84» لا تقبل «= 840» (الفحصُ السابق `in src` كان يقبلها)
    def adad_lean(mode):
        return {int(n): int(v) for n, v in re.findall(rf"lawCount {mode} (\d+) = (\d+)(?!\d)", src)}
    check("أعدادُ adad_waqf في Lean هي المنسوخة بالضبط", adad_lean("false") == {n: LEAN_WAQF[n] for n in range(5)})
    check("أعدادُ adad_wasl في Lean هي المنسوخة بالضبط", adad_lean("true") == {n: LEAN_WASL[n] for n in range(5)})
    check("فحصُ العدد لا يقبل بادئة", not re.findall(r"lawCount false 1 = (\d+)(?!\d)", "lawCount false 1 = 840") == ["84"])

    # ٢
    g = subprocess.run([sys.executable, "-I", str(JADHR / "scripts" / "bina_intrubiya_shahada.py"), "--check"],
                       capture_output=True, text=True)
    check("الشهادة المولَّدة = مخرج المولِّد بالبايت", g.returncode == 0)
    v = [int(x) for x in re.search(r"def shahadaV : List Nat := \[([^\]]*)\]", src).group(1).split(", ")]
    u = [int(x) for x in re.search(r"def shahadaU : List Nat := \[([^\]]*)\]", src).group(1).split(", ")]
    mm = re.search(r"theorem lawCount_aala \(n : Nat\) : (\d+) \^ n \* lawCount false n ≤ (\d+) \* (\d+) \^ n", src)
    D, C, P = map(int, mm.groups())
    ml = re.search(r"(\d+) \* (\d+) \^ n \* fU 0 ≤ (\d+) \^ n \* lawCount false \((\d+) \+ n\)", src)
    E, R, S, K = map(int, ml.groups())
    Tv, Tu = T(step, v), T(step, u)
    check("الأعلى: D·Tv ≤ P·v على الحالات", len(v) == 97 and all(D * a <= P * b for a, b in zip(Tv, v)))
    check("الأعلى: النهائيّة تحت C·v", all((1 if fw[q] else 0) <= C * v[q] for q in range(97)))
    check("الأدنى: R·u ≤ S·Tu على الحالات", len(u) == 97 and all(R * a <= S * b for a, b in zip(u, Tu)))
    nk = [1 if fw[q] else 0 for q in range(97)]
    for _ in range(K):
        nk = T(step, nk)
    check("الأدنى: E·u ≤ N_K", all(E * a <= b for a, b in zip(u, nk)))
    lo, hi = math.log2(R / S), math.log2(P / D)
    ratio = math.log2(LEAN_WAQF[12] / LEAN_WAQF[11])
    check("الحدّان يحصران log2(N₁₂/N₁₁) والفرقُ < 10⁻⁴ بتّ", lo <= ratio + 1e-9 and ratio <= hi + 1e-9 and hi - lo < 1e-4)
    check("القانون دون الشيفرة: P/D < 116", P < 116 * D)

    # ٣
    check("H(منتظم 4) = 2", abs(it.H(Counter({0: 5, 1: 5, 2: 5, 3: 5})) - 2) < 1e-12)
    check("H(1/2,1/4,1/4) = 1.5", abs(it.H(Counter({0: 2, 1: 1, 2: 1})) - 1.5) < 1e-12)
    check("MM(2,1,1) = 1.5 + 2/(8 ln2)", abs(it.H_mm(Counter({0: 2, 1: 1, 2: 1})) - (1.5 + 2 / (8 * math.log(2)))) < 1e-12)
    check("MM على نقطة = 0", it.H_mm(Counter({7: 9})) == 0)

    # ٤ — الجسرُ هويّةٌ هنا إلّا حيث يُختبر النقل
    hawiyya = {i: i for i in range(116)}
    ind = ["w%d" % i for i in range(12)]
    tm = {ind[i]: (4 * (i % 2) + (i // 2) % 2,) for i in range(12)}        # حاملان × حالتان بالتساوي
    r = it.bina(qanun, ind, tm, {}, {}, {}, hawiyya)
    check("I = 0 على مستقلَّين", abs(r["tabaqa2_tahsil"]["I_hamil_hala"]) < 1e-12)
    dep = ["d%d" % i for i in range(8)]
    tm = {dep[i]: ((0,) if i < 4 else (5,)) for i in range(8)}
    r = it.bina(qanun, dep, tm, {}, {}, {}, hawiyya)
    check("I = 1 وH(حالة|حامل) = 0 على مرتبطَين",
          abs(r["tabaqa2_tahsil"]["I_hamil_hala"] - 1) < 1e-12 and abs(r["tabaqa2_tahsil"]["H_hala_bihamil"]) < 1e-12)
    naql = {m(h, s): nb(h, s) for h in MASHRU for s in range(4)}
    r = it.bina(qanun, ["كتب"], {"كتب": (m("ك", 0), m("ت", 0), m("ب", 0))}, {}, {}, {}, naql)
    h0 = [s for s in r["halat"] if s["hala"] == 0][0]
    check("النقلُ قبل الآلة: البدايةُ ترى كَ = 84 لا 32", [t["khaliya"] for t in h0["aala"]] == [84])
    tot = Counter()
    for s in r["halat"]:
        tot.update(s["khanat"])
    check("محاسبة الخانات: 96 × 116", sum(tot.values()) == 96 * 116 and all(sum(s["khanat"].values()) == 116 for s in r["halat"]))
    check("الغيابُ ليس امتناعًا: مشهودٌ + غيرُ مشهود = الحيّ", all(
        s["khanat"].get("مرخَّص_مشهود", 0) + s["khanat"].get("مرخَّص_غير_مشهود", 0) == s["hayy"] for s in r["halat"]))
    check("الممتنع + التعارض = الميّت", all(
        s["khanat"].get("ممتنع_بالقانون", 0) + s["khanat"].get("تعارض", 0) == 116 - s["hayy"] for s in r["halat"]))
    r = it.bina(qanun, ["لْيَ"], {"لْيَ": (m("ل", 3), m("ي", 0))}, {}, {}, {}, naql)
    check("السكونُ أوّلَ الكلمة تعارضٌ معروضٌ بمثاله", [(t["hala"], t["rasm"], t["amthila"]) for t in r["taarudat"]] == [(0, "لْ", ["لْيَ"])])
    check("لا «مفهوم»", r["mafhum"] == 0)

    # ٥
    jn = it.jadwal_naql()
    check("جدولُ nabtBridge تقابليّ", sorted(jn.values()) == list(range(116)))
    check("صفوفٌ باليد: كَ ءَ اَ بْ وِ", all(jn[m(h, s)] == nb(h, s) for h, s in (("ك", 0), ("ء", 0), ("ا", 0), ("ب", 3), ("و", 2))))
    check("الجدولُ كلُّه = الجدولان باليد", jn == naql)

    # ٦
    words = ["كَتَبَ", "رَبِّ", "أَنْ", "فِي", "الْحَمْدُ", "اعْبُدُوا"]
    tm, ta = it.qari_tahsil(words)
    check("كَتَبَ", tm.get("كَتَبَ") == (m("ك", 0), m("ت", 0), m("ب", 0)))
    check("رَبِّ: الشدّةُ خليّةٌ ساكنةٌ قبلها", tm.get("رَبِّ") == (m("ر", 0), m("ب", 3), m("ب", 2)))
    check("أَنْ: المقعدُ همزة", tm.get("أَنْ") == (m("ء", 0), m("ن", 3)))
    check("فِي: الياءُ حرفُ مدّ ساكن", tm.get("فِي") == (m("ف", 2), m("ي", 3)))
    check("الْحَمْدُ: همزةُ أل مفتوحةً (التعديل الثالث، 6)",
          tm.get("الْحَمْدُ") == (m("ء", 0), m("ل", 3), m("ح", 0), m("م", 3), m("د", 1)))
    check("اعْبُدُوا معلَّقٌ بقاعدة همزة الوصل (لا لامَ تعريفٍ بعدها)",
          "اعْبُدُوا" not in tm and "P:قاعدة همزة الوصل" in ta.get("اعْبُدُوا", []))

    # ٦ب — قارئُ NABT الصارم منقولًا إلى Mashru (scripts/abjad_nabt.py)، لا من NABT
    nm, na = it.qari_nabt(["كَتَبَ", "الْحَمْدُ"])
    check("قارئ NABT الصارم: كَتَبَ", nm.get("كَتَبَ") == (nb("ك", 0), nb("ت", 0), nb("ب", 0)))
    check("قارئ NABT الصارم: المؤجَّل باسمه", na.get("الْحَمْدُ") == "DEFER:MISSING_VOCALIZATION")
    check("لا استيرادَ لحزمة nabt في عمليّة الاختبار", "nabt" not in sys.modules and "nabt.alphabet" not in sys.modules)

    # ٧
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        f.write("كَتَبَ\n")
        p = pathlib.Path(f.name)
    try:
        it.tashghil(p, "0" * 64)
        check("بصمةٌ خاطئة تُرفض", False)
    except SystemExit as e:
        check("بصمةٌ خاطئة تُرفض", str(e).startswith("MUDAA_SHA_MISMATCH"))
    p.unlink()

    # مع المودَع
    mdir = os.environ.get("MUDAA_DIR")
    q = pathlib.Path(mdir) / "quran-simple-enhanced.txt" if mdir else None
    if q and q.exists() and it.basma(q) == QURAN_SHA:
        r, md = it.tashghil(q, QURAN_SHA)
        M, Tt = r["mudaa"], r["tabaqa2_tahsil"]
        check("المودَع: 18,200 صورةً بلا «<sel>» وفيها حرف", M["suwar_bila_sel_wa_bihi_harf"] == 18200)
        check("المودَع: المرخَّصُ بالتحصيل ≥ المقبولِ بالقارئ الصارم",
              M["tahsil"]["rumuz_murakhkhasa"] >= M["nabt_sarim"]["rumuz_maqbula"])
        rumuz = q.read_text(encoding="utf-8").split()
        check("المودَع: المرخَّص + غيرُه = الرموز (عدٌّ مستقلّ بالفصل على البياض)",
              M["rumuz"] == len(rumuz) and M["tahsil"]["rumuz_murakhkhasa"] + M["tahsil"]["rumuz_ghayr_murakhkhasa"] == len(rumuz))
        check("المودَع: الحالاتُ المزورة تشمل المدّ (4)", 4 in Tt["halat_muzara"])
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable, "-I", str(JADHR / "scripts" / "intrubiya.py"), "--mudaa", str(q), "--basma", QURAN_SHA,
                            "--khuruj", d], capture_output=True, check=True)
            c = subprocess.run([sys.executable, "-I", str(JADHR / "scripts" / "intrubiya.py"), "--mudaa", str(q), "--basma",
                                QURAN_SHA, "--check", d], capture_output=True, text=True)
            check("المودَع: --check يعيد المخرج بالبايت", c.returncode == 0 and "CHECK_OK" in c.stdout)
    else:
        print("—    المودَع غائب: تُركت فحوصُه")

    print(f"الإنتروبيا: {'فشل ' + str(len(FAIL)) if FAIL else 'مرّت كلّها'}")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
