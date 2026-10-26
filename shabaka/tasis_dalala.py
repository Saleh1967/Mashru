"""شبكةُ الدلالة على جدول اللزوم الكامل: التعريفُ من أساسٍ معلن، مقابلَ البلوغ.

مرآةُ `Madlul/TasisDalala.lean` على الجدول الكامل (`luzum_mujam.tsv`، مودَعٌ مرشّحٌ لم يُختم). عدُّ أداة، لا قياسٌ على مرجعٍ محجوب.

القواعد (تعيينات البنّاء):
  T1 المعرِّفات: لكلّ جذرِ مادّةٍ A معرِّفاتُه جذورُ B في صفوفه غيرِ صفوف التعليل (luzum)، من المعجمين معًا (مدخلٌ واحدٌ
     للجذر)؛ كـ`TasisDalala.Jadwal.defJ`. وجذرٌ لا صفَّ له إلّا التعليل لا مدخلَ له.
  T2 أساسُ «معروف»: عنوانٌ في اللسان «### $ R: W: G»، وG حتّى أوّل «.» أو «؛» أو «،» (تُضمّ أسطرُ المادّة حتّى تبلغ إحداها)
     هو «معروف» أو «معروفة» بعد تطبيع المستخرِج ← الجذرُ R. وعدُّ ما يقول فيه المعجمُ «معروف» أساسًا قراءةُ البنّاء.
  T3 التعريف: يُعرَّف المدخلُ إذا عُرفت معرِّفاتُه كلُّها؛ كـ`TasisDalala.iqfal` حتّى الثبات. وما لا مدخلَ له لا يُعرَّف إلّا أساسًا.
  T3م بحرف المقال (arXiv:1411.0129): ما لا مدخلَ له معرَّفٌ بلا شرط؛ كـ`TasisDalala.Jadwal.defMaqal`.
  T4 البلوغ: جذرٌ له طريقٌ على الحواف (A ← معرِّفُه B) إلى جذرٍ في الأساس. معيارٌ أضعف: الترابطُ لا التعريف.
  T5 النواة (Harnad): تُحذف تكرارًا الجذورُ التي لا تعرّف شيئًا ممّا بقي.
  T6 الأساسُ الجشع: يُضاف إلى الأساس غيرُ المعرَّف الأكثرُ ورودًا في معرِّفات غير المعرَّف، حتّى يُعرَّف الكلّ: حدٌّ أعلى لأصغر أساس.
والعقدُ: جذورُ المواد كلُّها ومعرِّفاتُها بلا التعليل؛ كـ`TasisDalala.Jadwal.kalimat`. فالجذرُ الذي لا صفَّ له إلّا التعليل عقدةٌ بلا مدخل.
التشغيل: MUDAA_DIR=<مجلّدٌ فيه luzum_mujam.tsv وlisan.txt> python3 -I shabaka/tasis_dalala.py
"""
import collections
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as jl  # noqa: E402

LUZUM = "luzum"
MARUF = {jl.norm("معروف"), jl.norm("معروفة")}
HEAD = re.compile(r"^### \$\s*([^:\s]+):[^:.؛،]*:(.*)$")
CLEAN = re.compile(r"ms\d+|«\d+»|PageV\d+P\d+")


def muarrifat(rows):
    """T1: صفوفٌ (A، النوع، B) ← {A: معرِّفاته}."""
    D = collections.defaultdict(set)
    for a, naw, b in rows:
        if naw != LUZUM:
            D[a].add(b)
    return dict(D)


def uqad(rows):
    """العقد: جذورُ المواد ومعرِّفاتُها بلا التعليل."""
    return {a for a, _, _ in rows} | {b for _, naw, b in rows if naw != LUZUM}


def iqfal(D, G):
    """T3: المعرَّفُ من الأساس G."""
    K = set(G)
    while True:
        new = {v for v, ds in D.items() if v not in K and ds <= K}
        if not new:
            return K
        K |= new


def iqfal_maqal(D, N, G):
    """T3م: المعرَّفُ من الأساس G بحرف المقال."""
    return iqfal(D, set(G) | (N - set(D))) & N


def bulugh(D, G):
    """T4: ما له طريقٌ إلى الأساس."""
    radd = collections.defaultdict(set)
    for v, ds in D.items():
        for d in ds:
            radd[d].add(v)
    R, stack = set(G), list(G)
    while stack:
        x = stack.pop()
        for v in radd.get(x, ()):
            if v not in R:
                R.add(v)
                stack.append(v)
    return R


def nawat(D, N):
    """T5: نواةُ Harnad على العقد N."""
    alive = set(N)
    while True:
        used = {d for v in alive for d in D.get(v, ()) if d in alive}
        drop = alive - used
        if not drop:
            return alive
        alive -= drop


def jashi(D, N, G):
    """T6: أساسٌ جشع يعرّف كلَّ العقد N (حدٌّ أعلى لأصغر أساسٍ يضمّ G)."""
    B = set(G) & N
    K = iqfal(D, B)
    while not N <= K:
        und = N - K
        cnt = collections.Counter(d for v in und for d in D.get(v, ()) if d not in K)
        pick = max(und, key=lambda v: (cnt.get(v, 0), v))
        B.add(pick)
        K = iqfal(D, K | {pick})
    return B


def asas_maruf(lines):
    """T2: [(الجذر، السطر)] لعناوين اللسان التي تفسيرُها الأوّل «معروف»."""
    out = []
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if not m:
            continue
        txt, j = m.group(2), i + 1
        while j < len(lines) and not lines[j].startswith("### ") and not re.search("[.؛،]", txt):
            txt += " " + jl.satr(lines[j])
            j += 1
        g = re.split("[.؛،]", CLEAN.sub(" ", txt), maxsplit=1)[0].strip()
        if jl.norm(g) in MARUF:
            out.append((jl.norm(m.group(1)), i + 1))
    return out


def main():
    D_ = os.environ.get("MUDAA_DIR")
    if not D_:
        sys.exit("MUDAA_DIR غيرُ معيَّن")
    S = jl.sijill()
    for f in ("luzum_mujam.tsv", "lisan.txt"):
        if jl.basma(os.path.join(D_, f)) != S[f]["sha256"]:
            sys.exit(f"{f}: البصمةُ لا تطابق السجلّ")
    with open(os.path.join(D_, "luzum_mujam.tsv"), encoding="utf-8") as fh:
        rows = [(r[1], r[3], r[4]) for r in list(csv.reader(fh, delimiter="\t"))[1:]]
    D = muarrifat(rows)
    N = uqad(rows)
    lines = open(os.path.join(D_, "lisan.txt"), encoding="utf-8").read().split("\n")
    asas = asas_maruf(lines)
    G = {r for r, _ in asas}
    p = lambda x: f"{len(x)} ({100 * len(x) / len(N):.2f}%)"
    print(f"الصفوف {len(rows)} | العقد {len(N)} | لها مدخل {len(D)}")
    print(f"أساسُ «معروف» (T2): {len(asas)} عنوانًا، {len(G)} جذرًا، منها في العقد {len(G & N)}")
    K = iqfal(D, G & N) & N
    print(f"المعرَّف من الأساس (T3): {p(K)}، منها الأساسُ نفسُه {len(G & N)} وجديدٌ {len(K - G)}")
    print(f"البالغ إلى الأساس (T4): {p(bulugh(D, G & N))}")
    print(f"المعرَّف من أساسٍ فارغ: {len(iqfal(D, set()))}")
    L = N - set(D)
    M0, MG = iqfal_maqal(D, N, set()), iqfal_maqal(D, N, G & N)
    print(f"بحرف المقال (T3م): ما لا مدخلَ له {len(L)}؛ من أساسٍ فارغ {p(M0)} = {len(L)} بلا مدخل + جديدٌ {len(M0 - L)}؛"
          f" ومن الأساس {p(MG)} = {len(L)} بلا مدخل + الأساسُ {len(G & N - L)} + جديدٌ {len(MG - L - G)}")
    Kn = nawat(D, N)
    print(f"النواة (T5): {p(Kn)}، منها بلا مدخل {len(Kn - set(D))}")
    B = jashi(D, N, G)
    print(f"أساسٌ جشع يعرّف الكلّ (T6): {len(G & N)} + {len(B) - len(G & N)} = {p(B)}")


if __name__ == "__main__":
    main()
