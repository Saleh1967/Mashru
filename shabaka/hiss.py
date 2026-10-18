"""فصلُ المعاني داخل الجذر: شبكةُ اللزوم على عُقَد المعنى لا على الجذر.

السند:
  * سيبويه (الكتاب س247–251): «اتفاق اللفظين واختلاف المعنيين … قولك وجدت عليه من الموجدة ووجدت إذا أردت وجدان الضالة» —
    اللفظُ الواحد لمعنيين، يفرّق بينهما المصدرُ والصيغة.
  * مغني اللبيب (س2247): «الباء المفردة حرف جر لأربعة عشر معنى»، وسيبويه اقتصر على الإلصاق «معنى لا يفارقها» — فللّفظ أصلٌ
    جامعٌ ومعانٍ متعدّدة: مستويان لا مستوى واحد. والأصلُ الجامع في الجذر عند ابن فارس (R4)، والمعاني في صيغ اللسان.

القاعدة (تعيين البنّاء، H1–H3):
  H1 عقدةُ المعنى: (جذر، مكوّن). صيغُ الجذر التي تتجاور في حدِّ تفسيرٍ واحد (من آخر حدٍّ «. ؛ :» إلى النقطتين) معنًى واحد،
     ويُجمع ما اشترك منها بالاتّحاد (union-find). صيغةٌ لم تقع في حدٍّ عقدةٌ وحدها.
  H2 الصلة: بين عقدة اللفظ المفسَّر وعقدة صيغة الكلمة في التفسير — لا بين جذرين.
  H3 عقدةُ المالك لجذرٍ: مكوّنُ الصيغة المساوية للجذر نفسه (المصدر/الاسم المجرّد: علم، فهم، عقل، طلب، درس، كتب، قلم). إن لم
     تقع تلك الصيغة في حدٍّ فلا عقدة (لا حكم).
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/hiss.py [--asas R…] [--uqad R…]
"""
import collections
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as J  # noqa: E402


class Ittihad:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def bina(hiss):
    """المكوّنات والصلات: (uqda(R,f)، صلاتٌ بين عُقَد)."""
    U = Ittihad()
    for A, wf, hadd, naw, B, bf, satr in hiss:
        U.find((A, wf))
        for f in hadd:
            U.union((A, wf), (A, f))
        U.find((B, bf))

    def uqda(R, f):
        return U.find((R, f))
    silat = [(uqda(A, wf), naw, uqda(B, bf), satr) for A, wf, hadd, naw, B, bf, satr in hiss]
    return U, uqda, silat


def uqdat_malik(U, R):
    """H3: مكوّنُ الصيغة المساوية للجذر، إن وقعت في حدّ."""
    return U.find((R, R)) if (R, R) in U.p else None


def kathafa_hiss(silat, nodes):
    E = {frozenset((a, b)) for a, _, b, _ in silat if a != b}
    n = [x for x in nodes if x is not None]
    pairs = [(n[i], n[j]) for i in range(len(n)) for j in range(i + 1, len(n))]
    return sum(1 for p in pairs if frozenset(p) in E), len(pairs), [p for p in pairs if frozenset(p) in E]


def asas_hiss(U, silat, S, budhur=2000, bidhra=20261018, nafidha=100):
    """خطُّ أساسٍ على عُقَد المالك: كلُّ جذرٍ يُستبدل بجذرٍ له عقدةُ مالك من نافذة ±nafidha في رتبة درجة عقدته."""
    deg = collections.Counter()
    E = set()
    for a, _, b, _ in silat:
        if a != b and frozenset((a, b)) not in E:
            E.add(frozenset((a, b)))
            deg[a] += 1
            deg[b] += 1
    roots = sorted({r for (r, f) in U.p if f == r})
    cand = [(deg[U.find((r, r))], r) for r in roots]
    cand.sort()
    pos = {r: i for i, (_, r) in enumerate(cand)}
    obs, tot, _ = kathafa_hiss(silat, [uqdat_malik(U, r) for r in S])
    random.seed(bidhra)
    res = []
    for _ in range(budhur):
        pick = []
        for x in S:
            if x not in pos:
                continue
            i = pos[x]
            pick.append(cand[random.randint(max(0, i - nafidha), min(len(cand) - 1, i + nafidha))][1])
        res.append(kathafa_hiss(silat, [U.find((r, r)) for r in pick])[0])
    return obs, tot, sum(1 for v in res if v >= obs) / budhur, collections.Counter(res)


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    S = J.sijill()
    p = os.path.join(D, "lisan.txt")
    if J.basma(p) != S["lisan.txt"]["sha256"]:
        sys.exit("رُفض lisan.txt: بصمته لا تطابق السجلّ")
    L = open(p, encoding="utf-8").read().split("\n")
    ml = J.mawadd_lisan(L)
    Jd = J.Jadhr(ml)
    hiss = []
    J.lisan_qadaya(Jd, ml, hiss=hiss)
    U, uqda, silat = bina(hiss)
    comps = collections.defaultdict(set)
    for (R, f) in list(U.p):
        comps[U.find((R, f))].add(f)
    per_root = collections.Counter(r for (r, _) in comps)
    multi = sum(1 for r, c in per_root.items() if c > 1)
    print("مشاهدات المعنى:", len(hiss), "| عُقَد:", len(comps), "| جذورٌ لها أكثر من عقدة:", multi, "من", len(per_root))
    if "--lean" in sys.argv:
        R7 = ["كتب", "درس", "قلم", "علم", "فهم", "طلب", "عقل"]
        malik = [(r, uqdat_malik(U, r)) for r in R7]
        sil, seen = [], set()
        for a, naw, b, satr in silat:
            if a[0] in R7 and b[0] in R7 and a[0] != b[0] and (a, b) not in seen:
                seen.add((a, b))
                sil.append((a, naw, b, satr))
        q = lambda x: '"' + x + '"'
        lines = ["/- مولَّدٌ بـ `python3 -I shabaka/hiss.py --lean` من لسان العرب المختوم (قواعد H1–H3 في `shabaka/hiss.py`). لا يُحرَّر يدويًّا. -/",
                 "namespace Ishtirak", "",
                 "/-- عقدةُ المالك لكلّ جذرٍ من السبعة: (الجذر، ممثّلُ مكوّن الصيغة المساوية للجذر). -/",
                 "def uqadMalik : List (String × String) := [" + ", ".join(f"({q(r)}, {q(n[1])})" for r, n in malik if n) + "]", "",
                 f"/-- {len(sil)} صلةً على عُقَد المعنى بين جذرين من السبعة: (جذر، عقدة، جذر، عقدة، سطر اللسان). -/",
                 "def silatHiss : List (String × String × String × String × Nat) := [",
                 ",\n".join(f"  ({q(a[0])}, {q(a[1])}, {q(b[0])}, {q(b[1])}, {satr})" for a, naw, b, satr in sil), "]", "", "end Ishtirak", ""]
        out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Madlul", "IshtirakData.lean")
        open(out, "w", encoding="utf-8").write("\n".join(lines))
        print(out, len(sil))
    if "--uqad" in sys.argv:
        for R in [x for x in sys.argv[sys.argv.index("--uqad") + 1:] if not x.startswith("--")]:
            ks = sorted((c for c in comps if c[0] == R), key=lambda c: -len(comps[c]))
            print(R, "عقدة المالك:", uqdat_malik(U, R), "| عُقَده:", [(c[1], sorted(comps[c])[:8]) for c in ks[:8]])
    if "--asas" in sys.argv:
        R7 = []
        for r in sys.argv[sys.argv.index("--asas") + 1:]:
            if r.startswith("--"):
                break
            R7.append(r)
        nodes = [uqdat_malik(U, r) for r in R7]
        obs, tot, sil = kathafa_hiss(silat, nodes)
        print("عُقَد المالك:", dict(zip(R7, nodes)))
        print("الصلات المباشرة بين عُقَد المالك:", obs, "من", tot, sil)
        for a, naw, b, satr in silat:
            if {a[0], b[0]} <= set(R7) and a[0] != b[0]:
                print("  صلةٌ بين الجذرين:", a, naw, b, "س" + str(satr), "| عقدتا المالك؟", a in nodes, b in nodes)
        o, t, pv, dist = asas_hiss(U, silat, R7)
        print("خطّ الأساس على العُقَد: المشاهد", o, "من", t, "| P =", pv, "| التوزيع:", sorted(dist.items()))


if __name__ == "__main__":
    main()
