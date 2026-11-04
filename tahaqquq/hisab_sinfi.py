"""الحسابُ الصنفيّ في بايثون: مرآةُ آلات المالك السبع، والعدُّ بالاستنفاد عليها، والعدُّ على صفوف الأصناف كما في Lean.

يقرؤه tahaqquq/test_hisab.py (البوّابة ٥خ٢). المرآةُ منقولةٌ باليد من تعريفات Lean بأسطرها (تحت كلّ دالّة)، فهي مستقلّةٌ عن الحساب الصنفيّ
لا عن تلك التعريفات، ولا مولَّدةٌ منها؛ والصفوفُ تُقرأ من نصّ Lean نفسِه (`saffJ`، `saffK`، `saffS`، `saffM`، `saffA`). والصفوفُ وأعدادُ المالك
يبرهنها Lean، فما يكشفه هذا الفحصُ وحده فسادُ المرآة.
"""
import os
import re
from functools import lru_cache

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SLGE/Ladder.lean:21
makharijSizes = [3, 2, 2, 1, 1, 3, 1, 1, 1, 1, 3, 3, 3, 1, 3]


def blockDec(ss, i):  # SLGE/Core.lean:19
    if not ss:
        return (0, i)
    if i < ss[0]:
        return (0, i)
    r = blockDec(ss[1:], i - ss[0])
    return (r[0] + 1, r[1])


def maddOf(h):  # SLGE/Ladder.lean:121
    return 2 if h == 0 else (28 if h == 1 else 11)


def grp(c):  # SLGE/Law.lean:37
    return blockDec(makharijSizes, c)[0]


def weak(c):  # SLGE/Law.lean:40
    return c in (2, 11, 28)


def conflict(k, m):  # SLGE/Law.lean:43
    return grp(k) == grp(m) and k != m and not weak(k) and not weak(m)


def delta(q, a):  # SLGE/Law.lean:45
    if 96 <= q or 117 <= a:
        return 96
    if a == 116:
        if (1 <= q <= 4) or 67 <= q:
            return 37
        if 6 <= q < 35:
            return q + 32
        return 96
    if a // 4 == 2 and (a % 4 < 3 or q != 1):
        return 96
    if a % 4 < 3:
        if q <= 4 or q == 37:
            return 1 + a % 4
        if 6 <= q < 35:
            return 1 + a % 4 if a // 4 == q - 6 else 96
        if 38 <= q < 67:
            return 1 + a % 4 if a // 4 == q - 38 else 96
        if 67 <= q:
            return 96 if conflict(q - 67, a // 4) else 1 + a % 4
        return 96
    if 1 <= q <= 3:
        return 4 if a // 4 == maddOf(q - 1) else 67 + a // 4
    if q == 4:
        return 6 + a // 4
    if 67 <= q:
        return 35
    if 6 <= q < 35:
        return 36
    return 96


def omega(q, a):  # SLGE/Law.lean:60
    if a < 116 and a % 4 == 3 and 1 <= q <= 3 and a // 4 == maddOf(q - 1):
        return 0
    if a == 116:
        return 0
    return 1


def Fwaqf(q):  # SLGE/Law.lean:65
    return (1 <= q <= 36) or (67 <= q < 96)


def Fwasl(q):  # SLGE/Law.lean:67
    return (1 <= q <= 34) or (67 <= q < 96)


def delta_r(q, c):  # SLGE/Root.lean:57
    if 30 <= q or 29 <= c or c == 2:
        return 30
    if q == 0:
        return c + 1
    if conflict(q - 1, c):
        return 30
    return c + 1


augs = [20, 0, 13, 18, 27, 28, 14, 11, 1, 2]  # SLGE/Root.lean:379


def delta_a(q, a):  # SLGE/Root.lean:383
    return delta(q, a) if (a // 4) in augs else 96


def delta1(q, a):  # SLGE/Syllable.lean:14
    if 1 <= q and a < 116 and a % 4 < 3:
        return 96
    if a == 116:
        return 96
    return delta(q, a)


# الآلاتُ السبع: (الرموز، الانتقال، الوزن، القبول) — أسطرُ تعريفها في Lean.
ALAT = {
    "Mroot": (29, delta_r, lambda q, c: 1, lambda q: 1 <= q <= 29),  # SLGE/Root.lean:61
    "Maug": (116, delta_a, omega, Fwasl),  # SLGE/Root.lean:386
    "Mword": (116, delta, omega, Fwaqf),  # SLGE/Law.lean:79
    "MwordWasl": (116, delta, omega, Fwasl),  # SLGE/Law.lean:81
    "Msent": (117, delta, omega, Fwaqf),  # SLGE/Law.lean:83
    "Msyl": (116, delta1, omega, Fwaqf),  # SLGE/Syllable.lean:17
    "MsylWasl": (116, delta1, omega, Fwasl),  # SLGE/Syllable.lean:18
}


def lev_istinfad(ism, K, j, q0=0):
    """عددُ المالك ‎`lev K q0 j = C (K·j) j q0`‎ بالاستنفاد على المرآة (SLGE/Count.lean: `C`، `lev`)."""
    A, d, w, F = ALAT[ism]

    @lru_cache(maxsize=None)
    def C(f, ww, q):
        r = 1 if (ww == 0 and F(q)) else 0
        if f == 0:
            return r
        for b in range(A):
            o = w(q, b)
            if o <= ww:
                r += C(f - 1, ww - o, d(q, b))
        return r
    return C(K * j, j, q0)


# ---- الصفوفُ من نصّ Lean

# كلُّ آلة: (الملفّ، اسمُ الصفوف، اسمُ القبول أو None لقبولٍ مكتوبٍ في Asnaf نفسِها)
SUFUF = {
    "Mroot": ("SLGE/Root.lean", "saffJ", None),
    "Maug": ("SLGE/Root.lean", "saffA", "FA"),
    "Mword": ("SLGE/Law.lean", "saffK", "FW"),
    "MwordWasl": ("SLGE/Law.lean", "saffK", "FL"),
    "Msent": ("SLGE/Law.lean", "saffS", "FW"),
    "Msyl": ("SLGE/Syllable.lean", "saffM", "FWm"),
    "MsylWasl": ("SLGE/Syllable.lean", "saffM", "FLm"),
}


def sufuf(src, ism):
    """صفوفُ `def <ism> : Nat → List (Nat × Nat × Nat)`: ‎`| i => [(u, j, n), …]`‎."""
    m = re.search(rf"def {ism} : Nat → List \(Nat × Nat × Nat\)\n((?:  \| .*\n)+)", src)
    if not m:
        raise ValueError(f"لا صفوفَ باسم {ism}")
    out = {}
    for line in m.group(1).splitlines():
        k = re.match(r"  \| (\d+) => \[(.*)\]$", line)
        if not k:
            continue
        out[int(k.group(1))] = [tuple(int(x) for x in t) for t in re.findall(r"\((\d+), (\d+), (\d+)\)", k.group(2))]
    return out


def qubul(src, ism):
    """القبولُ على الصنف: ‎`def F (i : Nat) : Bool := !(i == a || …)`‎ (كلُّ صنفٍ إلّا المذكور)."""
    m = re.search(rf"def {ism} \(i : Nat\) : Bool := !\(([^)]*)\)", src)
    if not m:
        raise ValueError(f"لا قبولَ باسم {ism}")
    la = {int(x) for x in re.findall(r"i == (\d+)", m.group(1))}
    return lambda i: i not in la


def qubul_jadhr(src):
    """قبولُ الجذر في `QJ`: ‎`fun i => i == 1 || …`‎ (المذكورُ وحده)."""
    m = re.search(r"def QJ : Asnaf := ⟨\d+, saffJ, fun i => ([^⟩]*)⟩", src)
    na = {int(x) for x in re.findall(r"i == (\d+)", m.group(1))}
    return lambda i: i in na


def lev_bil_sufuf(ism, K, j, i0=0):
    """العدُّ على صفوف الأصناف (‎`Asnaf.C`‎ في SLGE/HisabSinfi.lean) من صنف الابتداء، بطول ‎`K·j`‎."""
    path, saff, F = SUFUF[ism]
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    rows = sufuf(src, saff)
    acc = qubul_jadhr(src) if F is None else qubul(src, F)

    @lru_cache(maxsize=None)
    def C(f, w, i):
        r = 1 if (w == 0 and acc(i)) else 0
        if f == 0:
            return r
        for (u, t, n) in rows.get(i, []):
            if u <= w:
                r += n * C(f - 1, w - u, t)
        return r
    return C(K * j, j, i0)


def aadad_al_malik():
    """أعدادُ المالك من نصّ قضاياه: ‎`<آلة>.lev 3 0 <درجة> = <عدد>`‎ في SLGE/Root.lean وLaw.lean وSyllable.lean."""
    out = set()
    for p in ("SLGE/Root.lean", "SLGE/Law.lean", "SLGE/Syllable.lean"):
        src = open(os.path.join(ROOT, p), encoding="utf-8").read()
        for m in re.finditer(r"\b(\w+)\.lev 3 0 (\d+) = (\d+)\b", src):
            if m.group(1) in ALAT:
                out.add((m.group(1), int(m.group(2)), int(m.group(3))))
    return sorted(out)


def qisma(*isms):
    """أقلُّ القِسَم المتكافئة أصنافًا ممّا يحفظ قبولَ الآلات المعطاة معًا (انتقالُها ووزنُها واحد)، بالتنقيح من قسمة القبول.
    أداةٌ لآلةٍ جديدة، لا يقرؤها الاختبار. ترجع صنفَ كلّ حالة بترقيم أوّل ظهور."""
    A, d, w, _ = ALAT[isms[0]]
    Fs = [ALAT[m][3] for m in isms]
    Q = 31 if isms[0] == "Mroot" else 97
    cls = [tuple(F(q) for F in Fs) for q in range(Q)]
    while True:
        sig, new = {}, []
        for q in range(Q):
            cnt = {}
            for b in range(A):
                k = (w(q, b), cls[d(q, b)])
                cnt[k] = cnt.get(k, 0) + 1
            s = (cls[q], tuple(sorted(cnt.items())))
            new.append(sig.setdefault(s, len(sig)))
        if len(set(new)) == len(set(cls)):
            order = {}
            return [order.setdefault(c, len(order)) for c in new]
        cls = new
