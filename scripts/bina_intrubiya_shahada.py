"""يولّد Jisr/IntrubiyaShahada.lean: شهادةَ متّجهٍ موجب لحدَّي معدّل نموّ القانون، ويتحقّق منها بأعدادٍ صحيحة قبل الكتابة.

الحدُّ الأعلى (`hadd_aala`): متّجهٌ `v` بأعدادٍ صحيحة، و`D·(Tv)(q) ≤ P·v(q)` لكلّ حالة، والنهائيّةُ تحت `C·v`؛ فـ`D^n·N_n ≤ C·P^n·v(0)`.
الحدُّ الأدنى (`hadd_adna`): متّجهٌ `u`، و`R·u(q) ≤ S·(Tu)(q)`، و`E·u ≤ N_K` على الحالات؛ فـ`E·R^n·u(0) ≤ S^n·N_(K+n)`.
والمتّجهان من متّجه بيرون للحالات الحيّة (تكرار القوى، float)، مقرَّبين إلى أعدادٍ صحيحة؛ وصحّتُهما لا تتوقّف على دقّة float:
تُفحص هنا بأعدادٍ صحيحة، ثمّ في Lean بـ`decide +kernel`.

تشغيل: python3 -I scripts/bina_intrubiya_shahada.py [--check]   (يكتب الملفّ، أو يطابقه بالبايت)
"""

import json
import sys
from fractions import Fraction
from pathlib import Path

JADHR = Path(__file__).resolve().parent.parent
LAW = JADHR / "jadawil" / "law.json"
OUT = JADHR / "Jisr" / "IntrubiyaShahada.lean"
DEAD, Q, A = 96, 97, 116
SCALE = 10 ** 12
D = 10 ** 4                       # المقامُ المشترك للنسبتين
K = 4                             # طولُ القاعدة للحدّ الأدنى


def qanun():
    d = json.loads(LAW.read_text(encoding="utf-8"))
    return [[t[0] for t in row] for row in d["transitions"]], d["final_waqf"]


def T(step, f):
    return [sum(f[step[q][a]] for a in range(A)) for q in range(Q)]


def perron(step):
    x = [1.0 if q != DEAD else 0.0 for q in range(Q)]
    lam = 0.0
    for _ in range(2000):
        y = T(step, x)
        y[DEAD] = 0.0
        lam = max(y)
        x = [t / lam for t in y]
    return lam, x


def lawvec(step, final, n):
    v = [1 if final[q] else 0 for q in range(Q)]
    for _ in range(n):
        v = T(step, v)
    return v


def shahada():
    step, final = qanun()
    lam, x = perron(step)
    # الأعلى: v ≥ متّجه بيرون، وموجبٌ على كلّ حالةٍ غير الميّتة (فتشمل النهائيّة)
    v = [0 if q == DEAD else int(x[q] * SCALE) + SCALE // 10 ** 6 for q in range(Q)]
    P = int(lam * D) + 1
    while not all(D * t <= P * vq for t, vq in zip(T(step, v), v)):
        P += 1
    C = 1
    assert all((1 if final[q] else 0) <= C * v[q] for q in range(Q))
    # الأدنى: u ≤ متّجه بيرون (يُقطع ما دون العتبة)، تحت N_K
    nk = lawvec(step, final, K)
    u0 = [0 if q == DEAD or x[q] < 1e-6 else int(x[q] * SCALE) for q in range(Q)]
    R = int(lam * D) - 1
    while not all(R * uq <= D * t for uq, t in zip(u0, T(step, u0))):
        R -= 1
    E, S = 1, D
    # نُصغّر u إلى ما تحت N_K بقسمةٍ صحيحةٍ واحدة (تحفظ الشرط: الشرطان خطّيّان في u بعد القسمة؟ لا — يُعاد الفحص)
    g = min(nk[q] * SCALE // u0[q] for q in range(Q) if u0[q])
    u = [uq * g // SCALE for uq in u0]
    while not all(R * uq <= D * t for uq, t in zip(u, T(step, u))):
        R -= 1
    assert all(E * uq <= nq for uq, nq in zip(u, nk))
    assert v[0] > 0 and u[0] > 0 and R > 0
    return {"v": v, "P": P, "C": C, "u": u, "R": R, "S": S, "E": E, "D": D, "K": K, "lam": lam}


def lean(s):
    vs = ", ".join(map(str, s["v"]))
    us = ", ".join(map(str, s["u"]))
    return f'''import Jisr.Intrubiya

/-!
# شهادةُ حدَّي معدّل نموّ القانون (مولَّد — لا يُحرَّر يدويًّا)

مولَّدٌ بـ`python3 -I scripts/bina_intrubiya_shahada.py`، ويطابقه `tahaqquq/test_intrubiya.py` بالبايت. المتّجهان مقرَّبان من متّجه بيرون
للحالات الحيّة، وصحّتُهما مفحوصةٌ هنا بـ`decide +kernel` لا بالتقريب.

- **الأعلى:** `{s["D"]}^n · N_n ≤ {s["C"]} · {s["P"]}^n · v₀` لكلّ `n` (`lawCount_aala`).
- **الأدنى:** `{s["E"]} · {s["R"]}^n · u₀ ≤ {s["S"]}^n · N_({s["K"]}+n)` لكلّ `n` (`lawCount_adna`).

فمعدّلُ النموّ بين `{s["R"]}/{s["S"]}` و`{s["P"]}/{s["D"]}`، ولوغاريتمُه (الإنتروبيا الطوبولوجيّة للقانون بالبتّ) يُحسب خارج Lean.
وقيمُ `N_n` حتى 4 مبرهنةٌ على الشاهد (`adad_waqf`، `adad_wasl`).
-/

namespace Jisr.Intrubiya

open Nabt.Law

def shahadaV : List Nat := [{vs}]

def shahadaU : List Nat := [{us}]

def fV (q : Nat) : Nat := shahadaV.getD q 0
def fU (q : Nat) : Nat := shahadaU.getD q 0

theorem shahadaV_T : ∀ q : Fin 97, {s["D"]} * T fV q.val ≤ {s["P"]} * fV q.val := by decide +kernel

theorem shahadaV_final : ∀ q : Fin 97,
    (if (machine false).final q.val then 1 else 0) ≤ {s["C"]} * fV q.val := by decide +kernel

theorem shahadaU_T : ∀ q : Fin 97, {s["R"]} * fU q.val ≤ {s["S"]} * T fU q.val := by decide +kernel

theorem shahadaU_qaida : ∀ q : Fin 97, {s["E"]} * fU q.val ≤ (lawVec false {s["K"]}).getD q.val 0 := by
  decide +kernel

theorem lawCount_aala (n : Nat) : {s["D"]} ^ n * lawCount false n ≤ {s["C"]} * {s["P"]} ^ n * fV 0 := by
  rw [lawCount, lawVec_eq false n 0 (by decide)]
  exact hadd_aala false fV {s["C"]} {s["P"]} {s["D"]} (fun q hq => shahadaV_T ⟨q, hq⟩)
    (fun q hq => shahadaV_final ⟨q, hq⟩) n 0 (by decide)

theorem lawCount_adna (n : Nat) :
    {s["E"]} * {s["R"]} ^ n * fU 0 ≤ {s["S"]} ^ n * lawCount false ({s["K"]} + n) := by
  rw [lawCount, lawVec_eq false ({s["K"]} + n) 0 (by decide)]
  exact hadd_adna false fU {s["K"]} {s["R"]} {s["S"]} {s["E"]} (fun q hq => shahadaU_T ⟨q, hq⟩)
    (fun q hq => (lawVec_eq false {s["K"]} q hq) ▸ shahadaU_qaida ⟨q, hq⟩) n 0 (by decide)

theorem adad_waqf :
    lawCount false 0 = 0 ∧ lawCount false 1 = 84 ∧ lawCount false 2 = 9436 ∧
    lawCount false 3 = 1052128 ∧ lawCount false 4 = 110116720 := by
  decide +kernel

theorem adad_wasl :
    lawCount true 0 = 0 ∧ lawCount true 1 = 84 ∧ lawCount true 2 = 9436 ∧
    lawCount true 3 = 987840 ∧ lawCount true 4 = 104650672 := by
  decide +kernel

/-- الوصلُ أضيقُ من الوقف ابتداءً من الطول الثالث، على الشاهد. -/
theorem wasl_adyaq_3 : lawCount true 3 < lawCount false 3 := by decide +kernel

end Jisr.Intrubiya
'''


def main():
    s = shahada()
    text = lean(s)
    if "--check" in sys.argv:
        ok = OUT.read_text(encoding="utf-8") == text
        print("CHECK_OK" if ok else "CHECK_DIFF")
        sys.exit(0 if ok else 1)
    OUT.write_text(text, encoding="utf-8")
    print(f"P/D = {Fraction(s['P'], s['D'])} ; R/S = {Fraction(s['R'], s['S'])} ; λ≈{s['lam']:.6f} ; v0={s['v'][0]} u0={s['u'][0]}")


if __name__ == "__main__":
    main()
