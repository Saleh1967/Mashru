"""اختبارُ فرضيّة الـ116 على جذور المعجمين المختومين.

**الفرضيّة** كما نقلتُها بعبارتي عن رسالة المالك الأولى (`Madlul/جدول_اللزوم.md` في التزام 313b4e1، السطر 24؛ نصُّها الحرفيّ لم يعد
في يدي): عددُ الجذوع في المعجمين محدودٌ مقيس، والرباعيُّ والخماسيُّ يتولّدان من توافيق الـ116. و116 = 29 حاملًا × 4 حالات (`SLGE/Law.lean`). وفي `SLGE/Root.lean` (ملفّ المالك) آلةُ الجذر المرخَّص
`Mroot` بعددها مبرهنًا: 20,430 ثلاثيًّا (`root3`)، 552,078 رباعيًّا (`root4`)، 14,918,778 خماسيًّا (`root5`)؛ ورقمُ الكلمة = رقمُ الجذر ×
عددُ الأوزان + رقمُ الوزن.

**الصياغةُ القابلةُ للاختبار (تعيين البنّاء):** المعجمان بلا حركةٍ واحدة (عدٌّ في المودَعات: 0 حركة)، فشقُّ الحالات (الأوزان) لا يُختبر هنا؛
ويُختبر شقُّ الحوامل — الجذر — بأربع دعاوى:
  F1 السلامة: كلُّ جذرٍ مشهودٍ مرخَّصٌ في `Mroot` (لا ألفَ أصلًا، ولا يتجاور حاملان مختلفان من مخرجٍ واحد غيرَ حروف العلّة).
     الألفُ في عناوين المعجمين لا تكون إلّا حرفَ علّةٍ غيرَ معيَّن (بغا، قام) فتُرمَّز واوًا، ولا أثر لذلك في الحكم: حرفُ العلّة لا يدخل
     التجاور (`Madlul.Fard116.illa_sawa`). فمنعُ الألف لا يُختبر هنا (اصطلاحُ الكتابة يوافقه)، ويُختبر التجاور وحده.
  F2 المحدوديّة: نسبةُ المشهود من المرخَّص لكلّ طول.
  F3 التولّد: الرباعيُّ المشهود ثلاثيٌّ مشهودٌ زيد عليه حامل (G1: إسقاطٌ واحدٌ على الأقلّ ثلاثيٌّ مشهود)، أو ثلاثيّان (G2 = N1 في naht.py)،
     أو ثنائيٌّ مكرَّر abab (Gr، «زلزل»)؛ والخماسيّ على الرباعيّ كذلك.
  F4 القيودُ المنقولة: ما قال أهلُ اللغة إنّه «لا يأتلف في كلمة واحدة» (اللسان والمقاييس بأسطرهما في `QUYUD`) — هل يصدّقه المعجم،
     وهل يتضمّنه قانونُ التجاور؟
خطّا الأساس: (U) الجذورُ المرخَّصة نفسُها بالتساوي — فضاءُ المالك المولَّد؛ (P) حروفُ المعجم نفسُها مبعثرةً بين جذوره موضعًا موضعًا (تحفظ
تكرار كلّ حرفٍ في كلّ موضع)، 2000 سحبة بالبذرة 20261018؛ وفي F3 تُبقى السحوبُ المرخَّصةُ وحدها.
الجمهور: عناوينُ اللسان المقبولة (`jadwal_luzum.mawadd_lisan`)، وعناوينُ المقاييس الثلاثيّة؛ وخماسيُّ اللسان من عناوين بلا وسم «### $»
(«# سفرجل: السفرجل» س205405) بنمط «# W: (و)ال؟W» وآخرُه حرفُ بابه — عيّنةٌ لا جرد. ورباعيُّ المقاييس لا يُعدّ: عناوينُه الأربعيّة
ثلاثيّةٌ معتلّةٌ بياء الرسم (ثروي، جدوي) إلّا قليلًا.
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/fard116.py [--lean [--lean-dir <مجلّد>]] [--json <مخرج>]
"""
import json
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as J  # noqa: E402

ROOT = J.ROOT
BIDHRA = 20261018
SAHB = 2000


def jadwal_malik():
    """الحوامل وأحجام المخارج من `Dal/Makharij.lean`، وحروفُ العلّة من `SLGE/Law.lean` — بنصّهما."""
    t = open(os.path.join(ROOT, "Dal", "Makharij.lean"), encoding="utf-8").read()
    haw = re.findall(r"'(.)'", re.search(r"def hawamil : List Char :=\s*\[(.*?)\]", t, re.S).group(1))
    ahjam = [int(x) for x in re.search(r"def ahjam : List Nat := \[([^\]]*)\]", t).group(1).split(",")]
    law = open(os.path.join(ROOT, "SLGE", "Law.lean"), encoding="utf-8").read()
    weak = [int(x) for x in re.search(r"def weak \(c : Nat\) : Bool := c == (\d+) \|\| c == (\d+) \|\| c == (\d+)", law).groups()]
    return haw, ahjam, set(weak)


HAW, AHJAM, WEAK = jadwal_malik()
ALIF = HAW.index("ا")
GRP = [g for g, n in enumerate(AHJAM) for _ in range(n)]
N = len(HAW)


def conflict(a, b):
    return GRP[a] == GRP[b] and a != b and a not in WEAK and b not in WEAK


def murakhkhas(r):
    """آلةُ `Mroot` (SLGE/Root.lean: δr) بحالاتها: 0 ابتداء، c+1 بعد الحامل c، 30 ممتنع؛ والقبولُ 1..29."""
    q = 0
    for c in r:
        if q >= 30 or c >= 29 or c == ALIF:
            q = 30
        elif q == 0:
            q = c + 1
        elif conflict(q - 1, c):
            q = 30
        else:
            q = c + 1
    return 1 <= q <= 29


def adad_murakhkhas(k):
    """عددُ المرخَّص بطول k بالبرمجة الديناميّة على الحامل الأخير."""
    v = [1 if c != ALIF else 0 for c in range(N)]
    for _ in range(k - 1):
        v = [0 if c == ALIF else sum(v[a] for a in range(N) if not conflict(a, c)) for c in range(N)]
    return sum(v)


def ramz(w):
    """الجذرُ المكتوب ← حوامل؛ الألفُ حرفُ علّةٍ غيرُ معيَّن يُرمَّز واوًا (`illa_sawa`)."""
    return [HAW.index("و") if ch == "ا" else HAW.index(ch) for ch in w]


QUYUD = [  # (الحرفان، القائل، المعجم، السطر، النصّ الحرفيّ)
    ("عح", "الخليل", "lisan", 143025, "قال الخليل: العين والحاء لا يأتلفان في كلمة واحدة أصلية"),
    ("حه", "الخليل", "lisan", 42494, "وبعد الحاء الهاء ولم يأتلفا في كلمة واحدة أصلية الحروف"),
    ("صس", "الأزهري", "lisan", 107377, "قال الأزهري: لا تأتلف الصاد مع"),
    ("صز", "الأزهري", "lisan", 112127, "قال الأزهري: لا تأتلف الصاد مع السين ولا مع"),
    ("جق", "الجوهري", "lisan", 174513, "قال الجوهري: الجيم والقاف لا يجتمعان في كلمة واحدة من كلام العرب"),
    ("صج", "الجوهري", "lisan", 126042, "الإجاص دخيل لأن الجيم والصاد لا يجتمعان"),
    ("طج", "الجوهري", "lisan", 254417, "وكلاهما معرب لأن الطاء والجيم لا يجتمعان في أصل"),
    ("ءغ", "—", "lisan", 300224, "لأن الهمزة والغين لا يجتمعان في بناء كلمة واحدة"),
    ("خع", "ابن فارس", "maqayis", 11825, "اعلم أن الخاء لا يكاد يأتلف مع العين إلا بدخيل"),
    ("صط", "شمر", "lisan", 193447, "لأن الصاد والطاء لا يكاد يجتمعان في محض كلامهم"),
]


def jumhur(D):
    S = J.sijill()
    for f in ("lisan.txt", "maqayis.txt"):
        if J.basma(os.path.join(D, f)) != S[f]["sha256"]:
            sys.exit(f"رُفض {f}: بصمته لا تطابق السجلّ")
    L = open(os.path.join(D, "lisan.txt"), encoding="utf-8").read().split("\n")
    M = open(os.path.join(D, "maqayis.txt"), encoding="utf-8").read().split("\n")
    lis = {}
    for r, i, _ in J.mawadd_lisan(L):
        lis.setdefault(r, i)
    # الخماسيّ: «# W: (و)ال؟W» وآخرُه حرفُ بابه
    l5, bab = {}, None
    for i, ln in enumerate(L, 1):
        mb = re.match(r"^### \| (.*)$", ln)
        if mb:
            bab = J.bab_huruf(mb.group(1))
        m = re.match(r"^# ([ء-ي]{5}): (?:و?ال)?\1", ln)
        if m:
            w = J.norm(m.group(1))
            if "ا" not in w and not w.startswith("ال") and (bab is None or w[-1] in bab):
                l5.setdefault(w, i)
    mq = {}
    for r, i, _ in J.mawadd_maqayis(M)[0]:
        if len(r) == 3 and re.fullmatch("[ء-ي]{3}", r) and all(ch in HAW for ch in r):
            mq.setdefault(r, i)
    pop = {"lisan3": {r: i for r, i in lis.items() if len(r) == 3},
           "lisan4": {r: i for r, i in lis.items() if len(r) == 4},
           "lisan5": l5,
           "maqayis3": mq}
    return pop, L, M


def codes(rs):
    return np.array([ramz(r) for r in rs], dtype=np.int64)


def lic_vec(A):
    """murakhkhas على مصفوفة جذور (n×k) — بلا ألف (الرمزُ بعد ramz لا ألف فيه إلّا في السحب)."""
    ok = ~np.any(A == ALIF, axis=1)
    C = CONF[A[:, :-1], A[:, 1:]]
    return ok & ~np.any(C, axis=1)


CONF = np.array([[conflict(a, b) for b in range(N)] for a in range(N)])
SAME = np.array([[GRP[a] == GRP[b] and a != b and a not in WEAK and b not in WEAK for b in range(N)] for a in range(N)])


def shuffle(A, rng):
    return np.stack([rng.permutation(A[:, j]) for j in range(A.shape[1])], axis=1)


def tawlid(A, T, k):
    """G1/G2/Gr لصفوف A (n×k) على مجموعة T (رموز الأطوال k-1)."""
    base = N ** np.arange(k - 2, -1, -1)
    hits = []
    for i in range(k):
        D = np.delete(A, i, axis=1)
        hits.append(np.isin(D @ base, T))
    H = np.stack(hits, axis=1)
    # الإسقاطان المختلفان: حذفُ i وحذفُ j قد يعطيان الثلاثيَّ نفسَه (حرفان متجاوران متساويان)
    dcodes = np.stack([np.delete(A, i, axis=1) @ base for i in range(k)], axis=1)
    g2 = np.zeros(len(A), bool)
    for i in range(k):
        for j in range(i + 1, k):
            g2 |= H[:, i] & H[:, j] & (dcodes[:, i] != dcodes[:, j])
    gr = (A[:, 0] == A[:, 2]) & (A[:, 1] == A[:, 3]) if k == 4 else np.zeros(len(A), bool)
    return H.any(axis=1), g2, gr


def nisba(x):
    return round(100.0 * x, 1)


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    rng = np.random.default_rng(BIDHRA)
    pop, L, M = jumhur(D)
    out = {"bidhra": BIDHRA, "sahb": SAHB, "malik": {k: adad_murakhkhas(k) for k in (3, 4, 5)}}
    # F1 + F2
    out["F1"], out["F2"] = {}, {}
    for name, d in pop.items():
        rs = sorted(d)
        A = codes(rs)
        k = A.shape[1]
        lic = lic_vec(A)
        mukh = [(rs[i], d[rs[i]], [HAW[a] + HAW[b] for a, b in zip(A[i, :-1], A[i, 1:]) if CONF[a, b]]) for i in np.where(~lic)[0]]
        nul = []
        for _ in range(SAHB):
            S = shuffle(A, rng)
            nul.append(np.mean(~lic_vec(S)))
        nul = np.array(nul)
        obs = float(np.mean(~lic))
        uni = 1 - out["malik"][k] / (N - 1) ** k
        out["F1"][name] = {"n": len(rs), "mukhalif": len(mukh), "nisba": nisba(obs), "U": nisba(uni),
                           "P_mutawassit": nisba(float(nul.mean())), "P_madan": [nisba(float(nul.min())), nisba(float(nul.max()))],
                           "P_qima": float(np.mean(nul <= obs)), "amthila": mukh}
        out["F2"][name] = {"mashhud_murakhkhas": int(lic.sum()), "mukhtalif_ramzan": len({rmz(rs[i]) for i in np.where(lic)[0]}),
                           "murakhkhas": out["malik"][k],
                           "nisba": round(100.0 * lic.sum() / out["malik"][k], 3)}
    # التجاورُ في غير المتجاورَين (1–3): لا يقول فيه القانون شيئًا
    A3 = codes(sorted(pop["lisan3"]))
    obs13 = float(np.mean(SAME[A3[:, 0], A3[:, 2]]))
    obs12 = float(np.mean(SAME[A3[:, 0], A3[:, 1]] | SAME[A3[:, 1], A3[:, 2]]))
    n13 = np.array([np.mean(SAME[S[:, 0], S[:, 2]]) for S in (shuffle(A3, rng) for _ in range(SAHB))])
    out["ghayr_mutajawir"] = {"mawdi_1_3": nisba(obs13), "P_mutawassit": nisba(float(n13.mean())),
                              "P_qima": float(np.mean(n13 <= obs13)), "mutajawir": nisba(obs12)}
    # F3: التولّد
    out["F3"] = {}
    for k, name, tname in ((4, "lisan4", "lisan3"), (5, "lisan5", "lisan4")):
        A = codes(sorted(pop[name]))
        T = codes(sorted(pop[tname])) @ (N ** np.arange(k - 2, -1, -1))
        g1, g2, gr = tawlid(A, T, k)
        res = {"n": len(A), "G1": nisba(g1.mean()), "G2": nisba(g2.mean()), "Gr": nisba(gr.mean()),
               "G1_n": int(g1.sum()), "G2_n": int(g2.sum()), "Gr_n": int(gr.sum())}
        for nul_name in ("U", "P"):
            vals = []
            for _ in range(SAHB if k == 4 else 500):
                if nul_name == "U":
                    S = rng.integers(0, N, size=(4 * len(A), k))
                else:
                    S = shuffle(A, rng)
                S = S[lic_vec(S)][: len(A)]
                a, b, c = tawlid(S, T, k)
                vals.append((a.mean(), b.mean(), c.mean()))
            V = np.array(vals)
            res[nul_name] = {"G1": nisba(V[:, 0].mean()), "G2": nisba(V[:, 1].mean()), "Gr": nisba(V[:, 2].mean()),
                             "G1_madan": [nisba(V[:, 0].min()), nisba(V[:, 0].max())],
                             "G1_P": float(np.mean(V[:, 0] >= g1.mean())), "G2_P": float(np.mean(V[:, 1] >= g2.mean())),
                             "Gr_P": float(np.mean(V[:, 2] >= gr.mean()))}
        out["F3"][name] = res
    # F4: القيودُ المنقولة
    src = {"lisan": L, "maqayis": M}
    allr = {r: i for r, i in pop["lisan3"].items()}
    allr.update(pop["lisan4"])
    rs = sorted(allr)
    A3, A4 = codes(sorted(r for r in rs if len(r) == 3)), codes(sorted(r for r in rs if len(r) == 4))
    bans = []
    for pair, qail, muj, satr_no, nass in QUYUD:
        if nass not in src[muj][satr_no - 1]:
            sys.exit(f"القيد {pair}: النصّ ليس في {muj} س{satr_no}")
        bans.append((HAW.index(pair[0]), HAW.index(pair[1])))

    def wujud(A):
        P = np.zeros((len(A), N), bool)
        for j in range(A.shape[1]):
            P[np.arange(len(A)), A[:, j]] = True
        return P
    nul = np.zeros((SAHB, len(bans)), int)
    for t in range(SAHB):
        P3, P4 = wujud(shuffle(A3, rng)), wujud(shuffle(A4, rng))
        for b, (x, y) in enumerate(bans):
            nul[t, b] = int(np.sum(P3[:, x] & P3[:, y]) + np.sum(P4[:, x] & P4[:, y]))
    out["F4"] = []
    for b, (pair, qail, muj, satr_no, nass) in enumerate(QUYUD):
        a, c = bans[b]
        fihi = [r for r in rs if pair[0] in r and pair[1] in r]
        mutaj = [r for r in fihi if any({x, y} == {pair[0], pair[1]} for x, y in zip(r, r[1:]))]
        out["F4"].append({"zawj": pair, "qail": qail, "mujam": muj, "satr": satr_no, "nass": nass,
                          "qanun": bool(CONF[a, c]), "fihi": len(fihi), "mutajawir": len(mutaj),
                          "P_mutawassit": round(float(nul[:, b].mean()), 1), "P_madan": [int(nul[:, b].min()), int(nul[:, b].max())],
                          "P_qima": float(np.mean(nul[:, b] <= len(fihi))),
                          "amthila": [(r, allr[r]) for r in fihi]})
    # قيدُ ابن فارس الثلاثيّ (المقاييس س40850): «النون والراء والباء لا يأتلفان»
    nass_nrb = "النون والراء والباء لا يأتلفان، وقد يكون بينهما دخيل"
    if nass_nrb not in M[40850 - 1]:
        sys.exit("قيد ن ر ب: النصّ ليس في المقاييس س40850")
    nrb = [r for r in rs if all(ch in r for ch in "نرب")]
    na, ra, ba = HAW.index("ن"), HAW.index("ر"), HAW.index("ب")
    nn = []
    for _ in range(SAHB):
        c = 0
        for A in (A3, A4):
            P = wujud(shuffle(A, rng))
            c += int(np.sum(P[:, na] & P[:, ra] & P[:, ba]))
        nn.append(c)
    nn = np.array(nn)
    out["F4_nrb"] = {"mujam": "maqayis", "satr": 40850, "nass": nass_nrb, "fihi": len(nrb), "amthila": nrb,
                     "P_mutawassit": round(float(nn.mean()), 1), "P_madan": [int(nn.min()), int(nn.max())],
                     "P_qima": float(np.mean(nn <= len(nrb)))}
    # التجاورُ زوجًا زوجًا في ثلاثيّ اللسان: المشهودُ O والمتوقَّعُ E بالبعثرة (E = Σ مواضع n_i(a)·n_j(b)/n، متوسّطُها بعينه)
    n3 = len(A3)
    cnt = [np.bincount(A3[:, j], minlength=N) for j in range(3)]

    def OE(a, b):
        O = int(np.sum(((A3[:, 0] == a) & (A3[:, 1] == b)) | ((A3[:, 0] == b) & (A3[:, 1] == a)) |
                       ((A3[:, 1] == a) & (A3[:, 2] == b)) | ((A3[:, 1] == b) & (A3[:, 2] == a))))
        E = sum(cnt[i][a] * cnt[i + 1][b] + (cnt[i][b] * cnt[i + 1][a] if a != b else 0) for i in (0, 1)) / n3
        return O, round(E, 1)
    out["azwaj_qanun"] = [(HAW[a] + HAW[b], *OE(a, b)) for a in range(N) for b in range(a + 1, N) if CONF[a, b]]
    ghayr = [(HAW[a] + HAW[b], *OE(a, b)) for a in range(N) for b in range(a + 1, N)
             if a != ALIF and b != ALIF and not CONF[a, b] and a not in WEAK and b not in WEAK]
    # أشدُّ ما يُتجنَّب خارج القانون (E ≥ 20) بترتيب O/E، ومعه بُعدُ المخرجين في جدول المالك (|grp a − grp b|)
    dist = {HAW[a] + HAW[b]: abs(GRP[a] - GRP[b]) for a in range(N) for b in range(N)}
    out["ashadd_tajannuban"] = [(*g, dist[g[0]]) for g in sorted([g for g in ghayr if g[2] >= 20], key=lambda g: g[1] / g[2])[:15]]
    # التماثل: حاملان متماثلان — القانونُ يجيزهما متجاورين (conflict يشترط الاختلاف)
    tam = {}
    for (i, j) in ((0, 1), (1, 2), (0, 2)):
        O = int(np.sum(A3[:, i] == A3[:, j]))
        E = round(float(np.sum(cnt[i] * cnt[j]) / n3), 1)
        tam[f"{i + 1}{j + 1}"] = (O, E, [r for r in sorted(pop["lisan3"]) if r[i] == r[j]][:12])
    out["tamathul"] = tam
    j = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else os.path.join(ROOT, "shabaka", "out", "fard116.json")
    with open(j, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    if "--lean" in sys.argv:
        lean(pop, out, sys.argv[sys.argv.index("--lean-dir") + 1] if "--lean-dir" in sys.argv else None)
    print(json.dumps({k: v for k, v in out.items() if k not in ("F4", "azwaj_qanun")}, ensure_ascii=False, indent=1)[:6000])
    for q in out["F4"]:
        print(q["zawj"], q["qail"], "قانون" if q["qanun"] else "-", "في الجذر", q["fihi"], "متجاور", q["mutajawir"],
              "خط الأساس", q["P_mutawassit"], "P", q["P_qima"], [r for r, _ in q["amthila"]][:12])
    print("أزواج القانون (O, E):", out["azwaj_qanun"])
    print("أشدّ ما يُتجنَّب خارج القانون:", out["ashadd_tajannuban"])
    print("التماثل:", {k: v[:2] for k, v in out["tamathul"].items()})


def rmz(r):
    """رمزُ الجذر: حواملُه أرقامًا بالأساس 29، الأوّلُ أعلاها (`Madlul.Fard116.ramz`)."""
    return sum(c * N ** (len(r) - 1 - i) for i, c in enumerate(ramz(r)))


def lean(pop, out, d_out=None):
    """يكتب `Madlul/Fard116Data.lean` (الجماهير رموزًا، كلُّ جمهورٍ عددٌ واحد يفكّه `codes`؛ قائمةٌ حرفيّةٌ بآلاف العناصر تتجاوز حدَّ
    العمق في Lean) و`Madlul/Fard116Shawahid.lean` (مبرهناتُ الشاهد واحدةً واحدة: المرورُ الواحد على آلاف الجذور في نواة Lean يكلّف
    قرابة نصف غيغابايت، فلا يُجمع مروران في مبرهنة)."""
    def pack(rs, k):
        B = N ** k
        return sum(rmz(r) * B ** i for i, r in enumerate(sorted(rs)))
    t3 = {rmz(r) for r in pop["lisan3"]}
    t4 = {rmz(r) for r in pop["lisan4"]}
    d = ["/- مولَّد بـ `python3 -I shabaka/fard116.py --lean` من المودَعَين المختومَين (lisan.txt، maqayis.txt)؛ لا يُحرَّر يدويًّا.",
         "   الحواملُ بترتيب `Dal.hawamil`؛ والألفُ في العنوان حرفُ علّةٍ غيرُ معيَّن يُرمَّز واوًا (28).",
         "   رمزُ الجذر حواملُه أرقامًا بالأساس 29 (الأوّلُ أعلاها)؛ والجمهورُ عددٌ واحد: الجذرُ i رقمُه i بالأساس 29^k،",
         "   بترتيب حروف العناوين. -/",
         "namespace Madlul.Fard116Data", "",
         "/-- m رمزًا من العدد n بالأساس B. -/",
         "def codes (B : Nat) : Nat → Nat → List Nat",
         "  | 0, _ => []",
         "  | m + 1, n => n % B :: codes B m (n / B)", ""]
    for name, k in (("lisan3", 3), ("lisan4", 4), ("lisan5", 5), ("maqayis3", 3)):
        d.append(f"/-- {name}: {len(pop[name])} عنوانًا مختلفًا بطول {k}. -/")
        d.append(f"def {name} : List Nat := codes {N ** k} {len(pop[name])} {hex(pack(pop[name], k))}")
        d.append("")
    d.append(f"/-- خريطةُ ثلاثيّ اللسان: البِتّ رمزُ الجذر. -/\ndef bits3 : Nat := {hex(sum(1 << x for x in t3))}\n")
    d.append(f"/-- خريطةُ رباعيّ اللسان. -/\ndef bits4 : Nat := {hex(sum(1 << x for x in t4))}\n")
    d.append("end Madlul.Fard116Data\n")
    open(os.path.join(d_out or os.path.join(ROOT, "Madlul"), "Fard116Data.lean"), "w", encoding="utf-8").write("\n".join(d))

    H = {h: i for i, h in enumerate(HAW)}
    s = ["/- مولَّد بـ `python3 -I shabaka/fard116.py --lean`؛ لا يُحرَّر يدويًّا. مبرهن على الشاهد: كلُّ مبرهنةٍ مرورٌ واحدٌ على جمهورٍ",
         "   من `Madlul/Fard116Data.lean` بتعريفات `Madlul/Fard116.lean`؛ والأعدادُ أعدادُ `shabaka/out/fard116.json` بعينها. -/",
         "import Madlul.Fard116", "", "namespace Madlul.Fard116.Shawahid", "open SLGE.Law Madlul.Fard116 Madlul.Fard116Data", ""]
    for name, k in (("lisan3", 3), ("maqayis3", 3), ("lisan4", 4), ("lisan5", 5)):
        bad = [rmz(r) for r, _, _ in out["F1"][name]["amthila"]]
        f = "licN3" if k == 3 else f"licK {k}"
        s.append(f"/-- المخالِفُ لآلة الجذر في {name}: {len(bad)} — {'، '.join(r for r, _, _ in out['F1'][name]['amthila'])}. -/")
        s.append(f"theorem mukhalif_{name} : {name}.filter (fun c => !{f} c) = {bad} := by decide +kernel\n")
    for (zawj, O, _E) in out["azwaj_qanun"]:
        a, b = H[zawj[0]], H[zawj[1]]
        s.append(f"/-- {zawj[0]}–{zawj[1]} متجاورين في ثلاثيّ اللسان: {O}. -/")
        s.append(f"theorem jiwar_{a}_{b} : (lisan3.filter (fun c => jiwarN c {a} {b})).length = {O} := by decide +kernel\n")
    for (zawj, O, _E, _d) in out["ashadd_tajannuban"]:
        a, b = H[zawj[0]], H[zawj[1]]
        s.append(f"/-- {zawj[0]}–{zawj[1]} (خارج القانون) متجاورين في ثلاثيّ اللسان: {O}. -/")
        s.append(f"theorem jiwar_{min(a, b)}_{max(a, b)} : (lisan3.filter (fun c => jiwarN c {a} {b})).length = {O} ∧ "
                 f"conflict {a} {b} = false := by decide +kernel\n")
    for key, (O, _E, _) in out["tamathul"].items():
        i, j = int(key[0]) - 1, int(key[1]) - 1
        s.append(f"/-- الموضعان {key[0]} و{key[1]} متماثلان في ثلاثيّ اللسان: {O}. -/")
        s.append(f"theorem tamathul_{key} : (lisan3.filter (fun c => mithlN c {i} {j})).length = {O} := by decide +kernel\n")
    for q in out["F4"]:
        a, b = H[q["zawj"][0]], H[q["zawj"][1]]
        n3 = sum(len(r) == 3 for r, _ in q["amthila"])
        n4 = sum(len(r) == 4 for r, _ in q["amthila"])
        s.append(f"/-- {q['qail']} ({q['mujam']} س{q['satr']}): «{q['nass']}» — {q['zawj'][0]} و{q['zawj'][1]} معًا: {n3} ثلاثيًّا و{n4} رباعيًّا. -/")
        s.append(f"theorem qayd_{a}_{b} : (lisan3.filter (fun c => maanN3 c {a} {b})).length = {n3} ∧ "
                 f"(lisan4.filter (fun c => maanK 4 c {a} {b})).length = {n4} := by decide +kernel\n")
    f3 = out["F3"]
    s.append("/-- الرباعيُّ من الثلاثيّ: ثلاثيٌّ مشهودٌ بإسقاطِ حامل (G1). -/")
    s.append(f"theorem tawlid4_G1 : (lisan4.filter (G1 4 bits3)).length = {f3['lisan4']['G1_n']} := by decide +kernel\n")
    s.append("/-- وثلاثيّان مختلفان (G2). -/")
    s.append(f"theorem tawlid4_G2 : (lisan4.filter (G2 4 bits3)).length = {f3['lisan4']['G2_n']} := by decide +kernel\n")
    s.append("/-- وثنائيٌّ مكرَّر abab (Gr). -/")
    s.append(f"theorem tawlid4_Gr : (lisan4.filter Gr).length = {f3['lisan4']['Gr_n']} := by decide +kernel\n")
    s.append("/-- الخماسيُّ من الرباعيّ: G1 وG2. -/")
    s.append(f"theorem tawlid5 : (lisan5.filter (G1 5 bits4)).length = {f3['lisan5']['G1_n']} ∧ "
             f"(lisan5.filter (G2 5 bits4)).length = {f3['lisan5']['G2_n']} := by decide +kernel\n")
    s.append("end Madlul.Fard116.Shawahid\n")
    open(os.path.join(d_out or os.path.join(ROOT, "Madlul"), "Fard116Shawahid.lean"), "w", encoding="utf-8").write("\n".join(s))


if __name__ == "__main__":
    main()
