import SLGE.Ladder
import SLGE.Count

/-!
# القانون: الابتداءُ والوصلُ والوقف على الخانات ‎29 × 4‎ — برهانٌ واحدٌ مغلق

**الرموز.** الخانةُ ‎(c, s)‎ رمزُها ‎4c + s‎ (هو ‎cellEnc‎ نفسُه)، ‎c < 29‎ الحاملُ بترتيب المخارج،
‎s ∈ {0,1,2}‎ فتحةٌ وضمّةٌ وكسرة، ‎s = 3‎ سكون. والرمز ‎116‎ حدُّ الكلمة.

**القانونُ واحدٌ بثلاثة مواضع:**
* **الابتداء:** لا يُبتدأ بساكن — لا في أوّل السلسلة ولا بعد حدّ الكلمة.
* **الوصل:** لا يلتقي ساكنان، إلّا مدًّا بعده ساكنٌ مُدغَمٌ في المتحرّك الذي يليه (حاملُهما واحد).
* **الوقف:** آخرُ السلسلة يُعفى فيه التقاءُ الساكنين.

والمدُّ ساكنٌ حاملُه مدُّ الحركة قبله (ا بعد الفتحة، و بعد الضمّة، ي بعد الكسرة) — وهذا الجدول
**وسيطٌ معلَن** (‎maddOf‎) لا نتيجة.

**الألفُ عنصرٌ محايد** (وسيطٌ معلَن): لا حالةَ لها إلّا مدَّ الفتحة — فلا تتحرّك (المتحرّكةُ همزة)،
ولا تُغلِق، ولا تقع بعد غير الفتحة.

**الحالات** ‎(< 97)‎: ‎0‎ ابتداء · ‎1+h‎ بعد متحرّك · ‎4‎ بعد مدّ · ‎67+k‎ بعد ساكنٍ مُغلِقٍ حاملُه ‎k‎ ·
‎6+k‎ مدٌّ ثمّ ساكنٌ حاملُه ‎k‎ (معلّقٌ على الإدغام أو الوقف) · ‎35‎ ساكنان مُغلِقان · ‎36‎ مدٌّ ثمّ
ساكنان (معلّقان على الوقف وحده) · ‎37‎ حدٌّ بعد حرّ · ‎38+k‎ حدٌّ بعد ‎6+k‎ · ‎96‎ ممتنع.

**الوزن** = عددُ الصوامت ‎c‎: كلُّ خانةٍ ‎1‎ إلّا المدَّ والحدّ. والدرجاتُ تُرتَّب به.

ثمّ يُبرهَن أنّ المقاطع الستّة ‎CV, CVV, CVC, CVVC, CVCC, CVVCC‎ **نتيجةٌ** للقانون لا مُدخَل:
كلُّ سلسلةٍ يرخّصها تنقسم إليها انقسامًا واحدًا.
-/

namespace SLGE
namespace Law

/-! ## 1. القانون -/

/-- مخرجُ الحامل: رتبتُه في ترتيب المخارج (‎carrierDec‎). -/
def grp (c : Nat) : Nat := (carrierDec c).1

/-- حروفُ العلّة ‎ا و ي‎ مخرجُها الجوف (وسيطٌ معلَن)، فلا تدخل في تجاور المخارج. -/
def weak (c : Nat) : Bool := c == 2 || c == 11 || c == 28

/-- **التجاور:** حاملان مختلفان من مخرجٍ واحد، ليس أحدُهما حرفَ علّة. -/
def conflict (k m : Nat) : Bool := grp k == grp m && k != m && !weak k && !weak m

def δ (q a : Nat) : Nat :=
  if 96 ≤ q ∨ 117 ≤ a then 96
  else if a = 116 then (if (1 ≤ q ∧ q ≤ 4) ∨ 67 ≤ q then 37 else if 6 ≤ q ∧ q < 35 then q + 32 else 96)
  else if a / 4 = 2 ∧ (a % 4 < 3 ∨ q ≠ 1) then 96
  else if a % 4 < 3 then
    (if q ≤ 4 ∨ q = 37 then 1 + a % 4
     else if 6 ≤ q ∧ q < 35 then (if a / 4 = q - 6 then 1 + a % 4 else 96)
     else if 38 ≤ q ∧ q < 67 then (if a / 4 = q - 38 then 1 + a % 4 else 96)
     else if 67 ≤ q then (if conflict (q - 67) (a / 4) then 96 else 1 + a % 4)
     else 96)
  else
    (if 1 ≤ q ∧ q ≤ 3 then (if a / 4 = maddOf (q - 1) then 4 else 67 + a / 4)
     else if q = 4 then 6 + a / 4 else if 67 ≤ q then 35
     else if 6 ≤ q ∧ q < 35 then 36 else 96)

def ω (q a : Nat) : Nat :=
  if a < 116 ∧ a % 4 = 3 ∧ 1 ≤ q ∧ q ≤ 3 ∧ a / 4 = maddOf (q - 1) then 0
  else if a = 116 then 0 else 1

/-- الوقف: كلُّ حالةٍ حيّةٍ غيرِ الابتداء والحدّ. -/
def Fwaqf (q : Nat) : Bool := decide ((1 ≤ q ∧ q ≤ 36) ∨ (67 ≤ q ∧ q < 96))
/-- الوصل: ما يقبل أن يليه متحرّك. -/
def Fwasl (q : Nat) : Bool := decide ((1 ≤ q ∧ q ≤ 34) ∨ (67 ≤ q ∧ q < 96))

def run : Nat → List Nat → Nat
  | q, [] => q
  | q, a :: l => run (δ q a) l

def wt : Nat → List Nat → Nat
  | _, [] => 0
  | q, a :: l => ω q a + wt (δ q a) l

def mk (A : Nat) (F : Nat → Bool) : Machine := ⟨A, δ, ω, F⟩
/-- الكلمةُ موقوفًا عليها: ‎116‎ خانة. -/
def Mword : Machine := mk 116 Fwaqf
/-- الكلمةُ في الوصل. -/
def MwordWasl : Machine := mk 116 Fwasl
/-- الجملةُ موقوفًا عليها: الخاناتُ وحدُّ الكلمة. -/
def Msent : Machine := mk 117 Fwaqf

theorem mk_run (A : Nat) (F : Nat → Bool) : ∀ q l, (mk A F).runL q l = run q l
  | _, [] => rfl
  | q, a :: l => mk_run A F (δ q a) l

theorem mk_wt (A : Nat) (F : Nat → Bool) : ∀ q l, (mk A F).wtL q l = wt q l
  | _, [] => rfl
  | q, a :: l => by
    show ω q a + (mk A F).wtL (δ q a) l = ω q a + wt (δ q a) l
    rw [mk_wt A F (δ q a) l]

theorem run_append (q : Nat) (l r : List Nat) : run q (l ++ r) = run (run q l) r := by
  induction l generalizing q with
  | nil => rfl
  | cons a l ih => exact ih (δ q a)

theorem wt_append (q : Nat) (l r : List Nat) : wt q (l ++ r) = wt q l + wt (run q l) r := by
  induction l generalizing q with
  | nil => simp [wt, run]
  | cons a l ih => simp only [List.cons_append, wt, run, ih]; omega

theorem δ_big {q : Nat} (a : Nat) (h : 96 ≤ q) : δ q a = 96 := by simp [δ, h]

theorem run_dead : ∀ l, run 96 l = 96
  | [] => rfl
  | a :: l => by simp only [run, δ_big a (Nat.le_refl 96)]; exact run_dead l

theorem dead_not (q : Nat) (h : q = 96) : Fwaqf q = false ∧ Fwasl q = false := by
  subst h; decide

/-! ### الوقائعُ المنتهية — كلُّها يفحصها النواة -/

theorem fin_mover : ∀ q < 97, ∀ a < 116, a % 4 < 3 → δ q a ≠ 96 → δ q a = 1 + a % 4 := by
  decide +kernel

theorem mover_step (q a : Nat) (ha : a < 116) (hm : a % 4 < 3) (h : δ q a ≠ 96) :
    δ q a = 1 + a % 4 := by
  by_cases hq : q < 97
  · exact fin_mover q hq a ha hm h
  · exact absurd (δ_big a (by omega)) h

theorem mover_wt (q a : Nat) (hm : a % 4 < 3) (ha : a < 116) : ω q a = 1 := by
  unfold ω
  rw [if_neg (by omega), if_neg (by omega)]

theorem fin_nuc : ∀ h < 3, ∀ b < 116, b % 4 = 3 → (b / 4 ≠ 2 ∨ h = 0) →
    δ (1 + h) b = (if b / 4 = maddOf h then 4 else 67 + b / 4) ∧
    ω (1 + h) b = (if b / 4 = maddOf h then 0 else 1) := by
  decide +kernel

theorem fin_afterK : ∀ k < 29, k ≠ 2 → δ 4 (4 * k + 3) = 6 + k ∧ ω 4 (4 * k + 3) = 1 := by
  decide +kernel

theorem fin_afterC : ∀ j < 29, ∀ k < 29, k ≠ 2 →
    δ (67 + j) (4 * k + 3) = 35 ∧ ω (67 + j) (4 * k + 3) = 1 := by
  decide +kernel

theorem fin_afterJ : ∀ j < 29, ∀ k < 29, k ≠ 2 →
    δ (6 + j) (4 * k + 3) = 36 ∧ ω (6 + j) (4 * k + 3) = 1 := by
  decide +kernel

/-- بعد المدّ يصير الساكنُ معلَّقًا، وبعد المُغلِق ساكنَين، وبعد المعلَّق ثلاثة. -/
theorem fin_after (b : Nat) (hb : b < 116) (h3 : b % 4 = 3) (hA : b / 4 ≠ 2) :
    δ 4 b = 6 + b / 4 ∧ ω 4 b = 1 ∧ (∀ j < 29, δ (67 + j) b = 35 ∧ ω (67 + j) b = 1) ∧
    ∀ j < 29, δ (6 + j) b = 36 ∧ ω (6 + j) b = 1 := by
  have e : b = 4 * (b / 4) + 3 := by omega
  have k := fin_afterK (b / 4) (by omega) hA
  rw [← e] at k
  refine ⟨k.1, k.2, fun j hj => ?_, fun j hj => ?_⟩
  · have := fin_afterC j hj (b / 4) (by omega) hA
    rw [← e] at this; exact this
  · have := fin_afterJ j hj (b / 4) (by omega) hA
    rw [← e] at this; exact this

/-- **الألفُ لا تتحرّك ولا تُغلِق:** من أيّ حالة. -/
theorem fin_alif : (∀ q < 97, ∀ s < 3, δ q (8 + s) = 96) ∧ δ 4 11 = 96 ∧ (∀ j < 29, δ (67 + j) 11 = 96) ∧
    (∀ j < 29, δ (6 + j) 11 = 96) ∧ (∀ h < 3, h ≠ 0 → δ (1 + h) 11 = 96) := by decide +kernel

theorem alif_mover_dead (q s : Nat) (hs : s < 3) : δ q (8 + s) = 96 := by
  by_cases hq : q < 97
  · exact fin_alif.1 q hq s hs
  · exact δ_big _ (by omega)

theorem madd_ok : ∀ h < 3, maddOf h ≠ 2 ∨ h = 0 := by decide

theorem fin_term : ∀ a < 117, δ 35 a = 96 ∧ δ 36 a = 96 := by decide +kernel

/-- **الوصل:** بعد ‎CVCC‎ و‎CVVCC‎ لا يَرِد شيء — لا متحرّكٌ ولا ساكنٌ ولا حدّ. -/
theorem terminal (a : Nat) : δ 35 a = 96 ∧ δ 36 a = 96 := by
  by_cases h : 117 ≤ a
  · simp [δ, h]
  · exact fin_term a (by omega)

theorem fin_hash : ∀ q < 97, ∀ c < 117, δ (δ q 116) c ≠ 96 → c < 116 ∧ c % 4 < 3 := by
  decide +kernel

theorem fin_hashF : ∀ q < 97, Fwaqf (δ q 116) = false := by decide +kernel

theorem fin_start : ∀ a < 117, δ 0 a ≠ 96 → a < 116 ∧ a % 4 < 3 := by decide +kernel

theorem fin_close : ∀ q < 97, ∀ a < 117, δ q a < 97 := by decide +kernel

def pot (q : Nat) : Nat :=
  if q = 0 then 0 else if q ≤ 3 then 2 else if q = 4 then 1
  else if q < 35 then 1 else if q = 35 then 2 else if q = 36 then 1
  else if 67 ≤ q ∧ q < 96 then 2 else 0

theorem fin_pot : ∀ q < 96, ∀ a < 117, δ q a ≠ 96 → 1 + pot (δ q a) ≤ 3 * ω q a + pot q := by
  decide +kernel

theorem δ_le (q a : Nat) : δ q a ≤ 96 := by
  by_cases h : q < 97 ∧ a < 117
  · exact Nat.le_of_lt_succ (fin_close q h.1 a h.2)
  · have : 96 ≤ q ∨ 117 ≤ a := by omega
    simp [δ, this]

/-! ## 2. النتائج: ما يلزم عن القانون -/

/-- **الابتداء:** لا يُبتدأ بساكنٍ ولا بحدّ. -/
theorem ibtida (a : Nat) (ha : a < 117) (h : δ 0 a ≠ 96) : a < 116 ∧ a % 4 < 3 :=
  fin_start a ha h

/-- **الاستنفادُ في الخانة:** الخاناتُ المرخَّصة ابتداءً ‎84‎ من ‎116‎ — المتحرّكاتُ وحدها، والألفُ لا تتحرّك. -/
theorem cell_count : ((List.range 117).filter fun a => Fwaqf (run 0 [a])).length = 84 := by
  decide +kernel

/-- **الحذفُ نتيجة:** «قَالْتُ» ممتنعةٌ بالقانون (مدٌّ ثمّ ساكنٌ غيرُ مدغم)، و«قُلْتُ» مرخَّصة.
ق=7، ا=2، ل=13، ت=18 بترتيب المخارج. -/
theorem qaltu : run 0 [4*7+0, 4*2+3, 4*13+3, 4*18+1] = 96 ∧
    Fwaqf (run 0 [4*7+1, 4*13+3, 4*18+1]) = true := by decide

/-- **الإدغامُ نتيجة:** «حَاجَّ» (ح=4، ج=9) مرخَّصةٌ لأنّ الساكنَ بعد المدّ مُدغمٌ في مثله،
ومثلُها بغير الإدغام ممتنعة؛ وفي الوقف يُعفى التقاؤهما. -/
theorem hajja : Fwaqf (run 0 [4*4+0, 4*2+3, 4*9+3, 4*9+0]) = true ∧
    run 0 [4*4+0, 4*2+3, 4*9+3, 4*7+0] = 96 ∧
    Fwaqf (run 0 [4*4+0, 4*2+3, 4*9+3]) = true := by decide

/-- **الوقفُ يُعفي، والوصلُ يمنع:** «بِنْتْ» (ب=26، ن=14، ت=18) مرخَّصةٌ موقوفًا عليها،
ممتنعةٌ إن وُصلت بمتحرّك. -/
theorem bint : Fwaqf (run 0 [4*26+2, 4*14+3, 4*18+3]) = true ∧
    Fwasl (run 0 [4*26+2, 4*14+3, 4*18+3]) = false ∧
    run 0 [4*26+2, 4*14+3, 4*18+3, 4*7+0] = 96 := by decide

/-! ## 3. المقطع: نتيجةُ القانون -/

def sym (y : Nat × Nat) : Nat := 4 * y.1 + y.2

def chainOf (x : Syl) : List Nat := (cellsOf x).map sym

theorem sym_eq_cellEnc (c s : Nat) : sym (c, s) = cellEnc c s := by
  simp [sym, cellEnc, mixEnc]; omega

theorem chain0 (o k₁ k₂ : Nat) : chainOf (0, o, k₁, k₂) = [4 * (o / 3) + o % 3] := rfl
theorem chain1 (o k₁ k₂ : Nat) :
    chainOf (1, o, k₁, k₂) = [4 * (o / 3) + o % 3, 4 * maddOf (o % 3) + 3] := rfl
theorem chain2 (o k₁ k₂ : Nat) :
    chainOf (2, o, k₁, k₂) = [4 * (o / 3) + o % 3, 4 * skip (maddOf (o % 3)) k₁ + 3] := rfl
theorem chain3 (o k₁ k₂ : Nat) :
    chainOf (3, o, k₁, k₂) = [4 * (o / 3) + o % 3, 4 * maddOf (o % 3) + 3, 4 * k₁ + 3] := rfl
theorem chain4 (o k₁ k₂ : Nat) : chainOf (4, o, k₁, k₂) =
    [4 * (o / 3) + o % 3, 4 * skip (maddOf (o % 3)) k₁ + 3, 4 * k₂ + 3] := rfl
theorem chain5 (o k₁ k₂ : Nat) : chainOf (5, o, k₁, k₂) =
    [4 * (o / 3) + o % 3, 4 * maddOf (o % 3) + 3, 4 * k₁ + 3, 4 * k₂ + 3] := rfl

/-- حالةُ ما بعد المقطع: ‎CV→1+h, CVV→4, CVC→67+k, CVVC→6+k₁, CVCC→35, CVVCC→36‎. -/
def endSt (x : Syl) : Nat :=
  match x.1 with
  | 0 => 1 + x.2.1 % 3 | 1 => 4 | 2 => 67 + skip (maddOf (x.2.1 % 3)) x.2.2.1 | 3 => 6 + x.2.2.1
  | 4 => 35 | _ => 36

/-- عددُ صوامت المقطع: ‎CV, CVV → 1‎؛ ‎CVC, CVVC → 2‎؛ ‎CVCC, CVVCC → 3‎. -/
def cOf (x : Syl) : Nat := x.1 / 2 + 1

def onsetSym (x : Syl) : Nat := 4 * (x.2.1 / 3) + x.2.1 % 3

/-- المُغلِقاتُ (الساكنُ غيرُ المدّ) في المقطع. -/
def closers (x : Syl) : List Nat :=
  match x.1 with
  | 2 => [skip (maddOf (x.2.1 % 3)) x.2.2.1]
  | 3 => [x.2.2.1]
  | 4 => [skip (maddOf (x.2.1 % 3)) x.2.2.1, x.2.2.2]
  | 5 => [x.2.2.1, x.2.2.2]
  | _ => []

/-- الألفُ لا فاتحٌ ولا مُغلِق. -/
def AlifOK (x : Syl) : Prop := x.2.1 / 3 ≠ 2 ∧ ∀ c ∈ closers x, c ≠ 2

theorem maddOf_lt (h : Nat) : maddOf h < 29 := by unfold maddOf; split <;> (try split) <;> omega

/-- **قانونُ المقطع مشتقّ:** من أيّ حالةٍ تقبل فاتحَه، يسير المقطعُ إلى ‎endSt‎ بوزن ‎cOf‎. -/
theorem syl_run (x : Syl) (hx : Valid x) (ha : AlifOK x) (q : Nat) (hq : δ q (onsetSym x) ≠ 96) :
    run q (chainOf x) = endSt x ∧ wt q (chainOf x) = cOf x := by
  obtain ⟨t, o, k₁, k₂⟩ := x
  obtain ⟨ht, ho, h₁, h₂⟩ := hx
  dsimp only at ht ho h₁ h₂
  simp only [onsetSym] at hq
  have hm : (4 * (o / 3) + o % 3) % 4 < 3 := by omega
  have hl : 4 * (o / 3) + o % 3 < 116 := by omega
  have h0 := mover_step q _ hl hm hq
  have w0 := mover_wt q _ hm hl
  have hmod : (4 * (o / 3) + o % 3) % 4 = o % 3 := by omega
  rw [hmod] at h0
  have hh : o % 3 < 3 := by omega
  have hM := maddOf_lt (o % 3)
  have nM := fin_nuc (o % 3) hh (4 * maddOf (o % 3) + 3) (by omega) (by omega)
    (by have := madd_ok (o % 3) hh; omega)
  obtain ⟨_, hcl⟩ := ha
  have eM : (4 * maddOf (o % 3) + 3) / 4 = maddOf (o % 3) := by omega
  rw [eM, if_pos rfl, if_pos rfl] at nM
  match t, ht with
  | 0, _ => constructor <;> simp [chain0, run, wt, h0, w0, endSt, cOf]
  | 1, _ => constructor <;> simp [chain1, run, wt, h0, w0, nM, endSt, cOf]
  | 2, _ =>
    simp only [radix] at h₁
    have hs := skip_lt (maddOf (o % 3)) k₁ hM h₁
    have nC := fin_nuc (o % 3) hh (4 * skip (maddOf (o % 3)) k₁ + 3) (by omega) (by omega)
      (Or.inl (by have := hcl (skip (maddOf (o % 3)) k₁) (by simp [closers]); omega))
    have eC : (4 * skip (maddOf (o % 3)) k₁ + 3) / 4 = skip (maddOf (o % 3)) k₁ := by omega
    rw [eC, if_neg (skip_ne _ _), if_neg (skip_ne _ _)] at nC
    constructor <;> simp [chain2, run, wt, h0, w0, nC, endSt, cOf]
  | 3, _ =>
    simp only [radix] at h₁
    have a3 := fin_after (4 * k₁ + 3) (by omega) (by omega)
      (by have := hcl k₁ (by simp [closers]); omega)
    have e3 : (4 * k₁ + 3) / 4 = k₁ := by omega
    rw [e3] at a3
    constructor <;> simp [chain3, run, wt, h0, w0, nM, a3.1, a3.2.1, endSt, cOf]
  | 4, _ =>
    simp only [radix] at h₁ h₂
    have hs := skip_lt (maddOf (o % 3)) k₁ hM h₁
    have nC := fin_nuc (o % 3) hh (4 * skip (maddOf (o % 3)) k₁ + 3) (by omega) (by omega)
      (Or.inl (by have := hcl (skip (maddOf (o % 3)) k₁) (by simp [closers]); omega))
    have eC : (4 * skip (maddOf (o % 3)) k₁ + 3) / 4 = skip (maddOf (o % 3)) k₁ := by omega
    rw [eC, if_neg (skip_ne _ _), if_neg (skip_ne _ _)] at nC
    have a4 := fin_after (4 * k₂ + 3) (by omega) (by omega)
      (by have := hcl k₂ (by simp [closers]); omega)
    have a4c := a4.2.2.1 (skip (maddOf (o % 3)) k₁) hs
    constructor <;> simp [chain4, run, wt, h0, w0, nC, a4c.1, a4c.2, endSt, cOf]
  | 5, _ =>
    simp only [radix] at h₁ h₂
    have a3 := fin_after (4 * k₁ + 3) (by omega) (by omega)
      (by have := hcl k₁ (by simp [closers]); omega)
    have e3 : (4 * k₁ + 3) / 4 = k₁ := by omega
    rw [e3] at a3
    have a5 := (fin_after (4 * k₂ + 3) (by omega) (by omega)
      (by have := hcl k₂ (by simp [closers]); omega)).2.2.2 k₁ h₁
    constructor <;> simp [chain5, run, wt, h0, w0, nM, a3.1, a3.2.1, a5.1, a5.2, endSt, cOf]

/-- **الاستنفادُ في المقطع:** كلُّ مقطعٍ صحيحٍ مرخَّصٌ في الوقف، ولا يرخَّص في الوصل إلّا الأربعة
الأولى ‎(CV, CVV, CVC, CVVC)‎ — بشرط ألّا تكون الألفُ فاتحًا ولا مُغلِقًا. -/
theorem syl_law (x : Syl) (hx : Valid x) (ha : AlifOK x) :
    Fwaqf (run 0 (chainOf x)) = true ∧ (Fwasl (run 0 (chainOf x)) = true ↔ x.1 < 4) := by
  have hq : δ 0 (onsetSym x) ≠ 96 :=
    (by decide +kernel : ∀ o < 87, o / 3 ≠ 2 → δ 0 (4 * (o / 3) + o % 3) ≠ 96) x.2.1 hx.2.1 ha.1
  rw [(syl_run x hx ha 0 hq).1]
  obtain ⟨t, o, k₁, k₂⟩ := x
  obtain ⟨ht, ho, h₁, h₂⟩ := hx
  dsimp only at ht ho h₁ h₂
  match t, ht with
  | 0, _ => simp only [endSt, Fwaqf, Fwasl]; constructor <;> simp <;> omega
  | 1, _ | 4, _ | 5, _ => simp [endSt, Fwaqf, Fwasl]
  | 2, _ =>
    simp only [radix] at h₁
    have := skip_lt (maddOf (o % 3)) k₁ (maddOf_lt _) h₁
    simp [endSt, Fwaqf, Fwasl]; omega
  | 3, _ => simp only [radix] at h₁; simp [endSt, Fwaqf, Fwasl]; omega

theorem blockEnc_take : ∀ (ss : List Nat) (m k : Nat), m ≤ ss.length →
    blockEnc ss m k = (ss.take m).sum + k
  | ss, 0, k, _ => by cases ss <;> simp [blockEnc]
  | [], _ + 1, _, h => by simp at h
  | s :: ss, m + 1, k, h => by
    simp only [blockEnc, List.take_succ_cons, List.sum_cons]
    rw [blockEnc_take ss m k (by simp at h; omega)]; omega

theorem syl_bounds (x : Syl) (hx : Valid x) :
    (sylSizes.take x.1).sum ≤ sylEnc x ∧ sylEnc x < (sylSizes.take x.1).sum + sylSizes.getD x.1 0 := by
  obtain ⟨t, o, k₁, k₂⟩ := x
  obtain ⟨ht, ho, h₁, h₂⟩ := hx
  dsimp only at ht ho h₁ h₂ ⊢
  have hmix := mix_lt 87 _ _ o k₁ k₂ ho h₁ h₂
  have e : sylEnc (t, o, k₁, k₂) = (sylSizes.take t).sum +
      mixEnc (radix t).1 (radix t).2 o k₁ k₂ := by
    unfold sylEnc; exact blockEnc_take _ _ _ (by simp [sylSizes]; omega)
  rw [e, sylSizes_getD t ht]; omega

/-- **ترقيمُ المقطع متدرّج:** ما فيه صامتٌ واحد في ‎[0, 174)‎، وما فيه اثنان في ‎[174, 5133)‎،
وما فيه ثلاثة — المرخَّصُ في الوقف وحده — في ‎[5133, 148944)‎. -/
theorem syl_graded (x : Syl) (hx : Valid x) :
    (cOf x = 1 ↔ sylEnc x < 174) ∧ (cOf x = 2 ↔ 174 ≤ sylEnc x ∧ sylEnc x < 5133) ∧
    (cOf x = 3 ↔ 5133 ≤ sylEnc x) ∧ (x.1 < 4 ↔ sylEnc x < 5133) := by
  have hb := syl_bounds x hx
  have ht : x.1 < 6 := hx.1
  simp only [cOf]
  generalize sylEnc x = n at hb ⊢
  generalize x.1 = t at hb ht ⊢
  have : t = 0 ∨ t = 1 ∨ t = 2 ∨ t = 3 ∨ t = 4 ∨ t = 5 := by omega
  rcases this with rfl | rfl | rfl | rfl | rfl | rfl <;>
    simp only [show sylSizes = [87, 87, 2436, 2523, 70644, 73167] from by decide] at hb <;>
    simp at hb <;> omega

/-! ## 4. القانونُ يقسم كلَّ سلسلةٍ يرخّصها إلى مقاطع: وجودٌ ووحدانيّة -/

def wordChain (w : List Syl) : List Nat := w.flatMap chainOf

def sentChain : List (List Syl) → List Nat
  | [] => []
  | [w] => wordChain w
  | w :: v :: S => wordChain w ++ 116 :: sentChain (v :: S)

def ValidS (S : List (List Syl)) : Prop := ∀ v ∈ S, v ≠ [] ∧ ∀ x ∈ v, Valid x ∧ AlifOK x

theorem unskip_lt (m c : Nat) (hm : m < 29) (hc : c < 29) (hne : c ≠ m) : unskip m c < 28 := by
  unfold unskip; split <;> omega

theorem skip_unskip (m c : Nat) (hne : c ≠ m) : skip m (unskip m c) = c := by
  unfold skip unskip
  by_cases h : c < m
  · simp [h]
  · have : ¬ (c - 1 < m) := by omega
    simp [h, this]; omega

/-- خانةٌ ساكنةٌ حاملُها الألفُ بعد غير الفتحة، أو بعد ساكن، تُميت السلسلة. -/
theorem kill (q b : Nat) (rest : List Nat) (h : δ q b = 96) : run q (b :: rest) = 96 := by
  simp only [run, h, run_dead]

/-- **أوّلُ مقطع:** سلسلةٌ حيّةٌ تبدأ بمتحرّك تبدأ بمقطعٍ صحيحٍ واحد — لا ألفَ فيه فاتحًا ولا مُغلِقًا —
وما بعده لا يبدأ بساكن. -/
theorem split (q a : Nat) (rest : List Nat) (ha : a < 116) (hm : a % 4 < 3)
    (hl : run q (a :: rest) ≠ 96) :
    ∃ x r, (Valid x ∧ AlifOK x) ∧ a :: rest = chainOf x ++ r ∧
      (∀ b ∈ r.head?, ¬ (b < 116 ∧ b % 4 = 3)) := by
  have hq : δ q a ≠ 96 := fun h => hl (kill q a rest h)
  have h1 := mover_step q a ha hm hq
  have haA : a / 4 ≠ 2 := by
    intro h2; apply hq
    have : a = 8 + a % 4 := by omega
    rw [this]; exact alif_mover_dead q _ hm
  obtain ⟨o, hod⟩ : ∃ o, o = 3 * (a / 4) + a % 4 := ⟨_, rfl⟩
  have ho : o < 87 := by omega
  have hoa : 4 * (o / 3) + o % 3 = a := by omega
  have hoh : o % 3 = a % 4 := by omega
  have hoA : o / 3 ≠ 2 := by omega
  have v0 : Valid (0, o, 0, 0) ∧ AlifOK (0, o, 0, 0) :=
    ⟨⟨by simp, ho, by simp [radix], by simp [radix]⟩, hoA, by simp [closers]⟩
  have v1 : Valid (1, o, 0, 0) ∧ AlifOK (1, o, 0, 0) :=
    ⟨⟨by simp, ho, by simp [radix], by simp [radix]⟩, hoA, by simp [closers]⟩
  have hM := maddOf_lt (a % 4)
  rcases rest with _ | ⟨b, rest⟩
  · exact ⟨(0, o, 0, 0), [], v0, by rw [chain0, hoa]; rfl, by simp⟩
  by_cases hb : b < 116 ∧ b % 4 = 3
  rotate_left
  · exact ⟨(0, o, 0, 0), b :: rest, v0, by rw [chain0, hoa]; rfl, by simpa using hb⟩
  have hl2 : run (δ (1 + a % 4) b) rest ≠ 96 := by simpa only [run, h1] using hl
  by_cases hmb : b / 4 = maddOf (a % 4)
  · -- مدّ
    have n2 := fin_nuc (a % 4) hm b hb.1 hb.2 (by have := madd_ok (a % 4) hm; omega)
    rw [if_pos hmb, if_pos hmb] at n2
    rw [n2.1] at hl2
    have hbm : 4 * maddOf (a % 4) + 3 = b := by omega
    rcases rest with _ | ⟨c, rest⟩
    · exact ⟨(1, o, 0, 0), [], v1, by rw [chain1, hoa, hoh, hbm]; rfl, by simp⟩
    by_cases hc : c < 116 ∧ c % 4 = 3
    rotate_left
    · exact ⟨(1, o, 0, 0), c :: rest, v1, by rw [chain1, hoa, hoh, hbm]; rfl, by simpa using hc⟩
    have hcA : c / 4 ≠ 2 := by
      intro h2; apply hl2; apply kill
      have : c = 11 := by omega
      rw [this]; exact fin_alif.2.1
    have a3 := fin_after c hc.1 hc.2 hcA
    have hl3 : run (6 + c / 4) rest ≠ 96 := by simpa only [run, a3.1] using hl2
    have hcm : 4 * (c / 4) + 3 = c := by omega
    have v3 : Valid (3, o, c / 4, 0) ∧ AlifOK (3, o, c / 4, 0) :=
      ⟨⟨by simp, ho, by simp only [radix]; omega, by simp [radix]⟩, hoA,
        by simp only [closers]; simpa using hcA⟩
    rcases rest with _ | ⟨d, rest⟩
    · exact ⟨(3, o, c / 4, 0), [], v3, by rw [chain3, hoa, hoh, hbm, hcm]; rfl, by simp⟩
    by_cases hd : d < 116 ∧ d % 4 = 3
    rotate_left
    · exact ⟨(3, o, c / 4, 0), d :: rest, v3, by rw [chain3, hoa, hoh, hbm, hcm]; rfl,
        by simpa using hd⟩
    have hdA : d / 4 ≠ 2 := by
      intro h2; apply hl3; apply kill
      have : d = 11 := by omega
      rw [this]; exact fin_alif.2.2.2.1 (c / 4) (by omega)
    have a4 := ((fin_after d hd.1 hd.2 hdA).2.2.2 (c / 4) (by omega)).1
    have hdm : 4 * (d / 4) + 3 = d := by omega
    have v5 : Valid (5, o, c / 4, d / 4) ∧ AlifOK (5, o, c / 4, d / 4) :=
      ⟨⟨by simp, ho, by simp only [radix]; omega, by simp only [radix]; omega⟩, hoA,
        by simp only [closers]; intro x hx; simp at hx; omega⟩
    rcases rest with _ | ⟨e, rest⟩
    · exact ⟨(5, o, c / 4, d / 4), [], v5, by rw [chain5, hoa, hoh, hbm, hcm, hdm]; rfl, by simp⟩
    by_cases he : e < 116 ∧ e % 4 = 3
    · exfalso; apply hl3
      simp only [run, a4, (terminal e).2, run_dead]
    · exact ⟨(5, o, c / 4, d / 4), e :: rest, v5, by rw [chain5, hoa, hoh, hbm, hcm, hdm]; rfl,
        by simpa using he⟩
  · -- ساكنٌ مُغلِق
    have hbA : b / 4 ≠ 2 := by
      intro h2
      have hh0 : a % 4 ≠ 0 := by intro h0; apply hmb; rw [h0]; simpa [maddOf] using h2
      apply hl2; apply kill
      have : b = 11 := by omega
      rw [this]; exact fin_alif.2.2.2.2 (a % 4) hm hh0
    have n2 := fin_nuc (a % 4) hm b hb.1 hb.2 (Or.inl hbA)
    rw [if_neg hmb, if_neg hmb] at n2
    rw [n2.1] at hl2
    have hk := unskip_lt (maddOf (a % 4)) (b / 4) hM (by omega) hmb
    have hsk := skip_unskip (maddOf (a % 4)) (b / 4) hmb
    have hbm : 4 * skip (maddOf (a % 4)) (unskip (maddOf (a % 4)) (b / 4)) + 3 = b := by
      rw [hsk]; omega
    have v2 : Valid (2, o, unskip (maddOf (a % 4)) (b / 4), 0) ∧
        AlifOK (2, o, unskip (maddOf (a % 4)) (b / 4), 0) :=
      ⟨⟨by simp, ho, by simp only [radix]; omega, by simp [radix]⟩, hoA,
        by simp only [closers, hoh, hsk]; simpa using hbA⟩
    rcases rest with _ | ⟨c, rest⟩
    · exact ⟨_, [], v2, by rw [chain2, hoa, hoh, hbm]; rfl, by simp⟩
    by_cases hc : c < 116 ∧ c % 4 = 3
    rotate_left
    · exact ⟨_, c :: rest, v2, by rw [chain2, hoa, hoh, hbm]; rfl, by simpa using hc⟩
    have hcA : c / 4 ≠ 2 := by
      intro h2; apply hl2; apply kill
      have : c = 11 := by omega
      rw [this]; exact fin_alif.2.2.1 (b / 4) (by omega)
    have a3 := ((fin_after c hc.1 hc.2 hcA).2.2.1 (b / 4) (by omega)).1
    have hl3 : run 35 rest ≠ 96 := by simpa only [run, a3] using hl2
    have hcm : 4 * (c / 4) + 3 = c := by omega
    have v4 : Valid (4, o, unskip (maddOf (a % 4)) (b / 4), c / 4) ∧
        AlifOK (4, o, unskip (maddOf (a % 4)) (b / 4), c / 4) :=
      ⟨⟨by simp, ho, by simp only [radix]; omega, by simp only [radix]; omega⟩, hoA,
        by simp only [closers, hoh, hsk]; intro x hx; simp at hx; omega⟩
    rcases rest with _ | ⟨d, rest⟩
    · exact ⟨_, [], v4, by rw [chain4, hoa, hoh, hbm, hcm]; rfl, by simp⟩
    by_cases hd : d < 116 ∧ d % 4 = 3
    · exfalso; apply hl3
      simp only [run, (terminal d).1, run_dead]
    · exact ⟨_, d :: rest, v4, by rw [chain4, hoa, hoh, hbm, hcm]; rfl, by simpa using hd⟩

theorem chainOf_ne (x : Syl) : chainOf x ≠ [] := by
  obtain ⟨t, o, k₁, k₂⟩ := x
  unfold chainOf cellsOf; split <;> simp

theorem sentChain_cons (x : Syl) (w : List Syl) (S : List (List Syl)) :
    sentChain ((x :: w) :: S) = chainOf x ++ sentChain (w :: S) := by
  cases S <;> simp [sentChain, wordChain, List.flatMap_cons]

theorem run_lt68 : ∀ (q : Nat) (l : List Nat), q < 97 → run q l < 97
  | _, [], h => h
  | q, a :: l, _ => run_lt68 (δ q a) l (by have := δ_le q a; omega)

theorem structure_aux : ∀ (n : Nat) (l : List Nat) (q : Nat), l.length ≤ n → (∀ b ∈ l, b < 117) →
    (∀ a ∈ l.head?, a < 116 ∧ a % 4 < 3) → l ≠ [] → Fwaqf (run q l) = true →
    ∃ w S, ValidS (w :: S) ∧ l = sentChain (w :: S)
  | 0, l, _, hn, _, _, hne, _ => by
    cases l with
    | nil => exact absurd rfl hne
    | cons _ _ => simp at hn
  | n + 1, [], _, _, _, _, hne, _ => absurd rfl hne
  | n + 1, a :: rest, q, hn, hl, hh, _, hF => by
    have ha := hh a (by simp)
    have hlive : run q (a :: rest) ≠ 96 := fun h => by rw [h] at hF; simp [Fwaqf] at hF
    obtain ⟨x, r, hx, heq, hr⟩ := split q a rest ha.1 ha.2 hlive
    have hlen : r.length ≤ n := by
      have := congrArg List.length heq
      have hc : 0 < (chainOf x).length := List.length_pos_iff.2 (chainOf_ne x)
      simp at this hn; omega
    have hrun : run q (a :: rest) = run (run q (chainOf x)) r := by rw [heq, run_append]
    have hmem : ∀ b ∈ r, b < 117 := fun b hb => hl b (by rw [heq]; simp [hb])
    rcases r with _ | ⟨b, r'⟩
    · refine ⟨[x], [], ?_, by rw [heq]; simp [sentChain, wordChain]⟩
      intro v hv; simp at hv; subst hv; exact ⟨by simp, fun y hy => by simp at hy; subst hy; exact hx⟩
    have hb := hmem b (by simp)
    have hbs : ¬ (b < 116 ∧ b % 4 = 3) := hr b (by simp)
    by_cases hbm : b < 116
    · obtain ⟨w, S, hv, hS⟩ := structure_aux n (b :: r') (run q (chainOf x)) hlen hmem
        (fun c hc => by simp at hc; subst hc; omega) (by simp) (by rw [← hrun]; exact hF)
      refine ⟨x :: w, S, ?_, by rw [heq, hS, sentChain_cons]⟩
      intro v hv
      simp at hv
      rcases hv with rfl | hvm
      · refine ⟨by simp, fun y hy => ?_⟩
        simp at hy; rcases hy with rfl | hy
        · exact hx
        · exact (hv _ (by simp)).2 y hy
      · exact hv v (by simp [hvm])
    · have hb116 : b = 116 := by omega
      subst hb116
      generalize hq2 : run q (chainOf x) = q2 at hrun
      have hq2' : q2 < 97 := by
        rw [← hq2]
        by_cases hq0 : q < 97
        · exact run_lt68 q (chainOf x) hq0
        · exfalso; apply hlive; simp only [run, δ_big a (by omega : 96 ≤ q), run_dead]
      rcases r' with _ | ⟨c, r''⟩
      · exfalso; rw [hrun] at hF; simp only [run] at hF; rw [fin_hashF q2 hq2'] at hF
        exact Bool.false_ne_true hF
      have hc := hmem c (by simp)
      have hcm : c < 116 ∧ c % 4 < 3 := by
        apply fin_hash q2 hq2' c hc
        intro h; rw [hrun] at hF; simp only [run, h, run_dead] at hF; simp [Fwaqf] at hF
      obtain ⟨w, S, hv, hS⟩ := structure_aux n (c :: r'') (δ q2 116) (by simp at hlen ⊢; omega)
        (fun d hd => hmem d (by simp at hd ⊢; exact Or.inr hd))
        (fun d hd => by simp at hd; subst hd; exact hcm) (by simp)
        (by rw [hrun] at hF; exact hF)
      refine ⟨[x], w :: S, ?_, by rw [heq, hS]; simp [sentChain, wordChain]⟩
      intro v hv
      simp at hv
      rcases hv with rfl | hvm
      · exact ⟨by simp, fun y hy => by simp at hy; subst hy; exact hx⟩
      · exact hv v (by simp [hvm])

/-- **القانونُ يولّد المقاطع (الجملة):** كلُّ سلسلةٍ يرخّصها القانون جملةٌ من كلماتٍ غيرِ فارغة، كلُّ
كلمةٍ مقاطعُ صحيحة من الستّة. -/
theorem sent_structure (l : List Nat) (h : Msent.Lic 0 l) : ∃ S, ValidS S ∧ sentChain S = l := by
  obtain ⟨hl, hF0⟩ := h
  have hF : Fwaqf (run 0 l) = true := by rw [Msent, mk_run] at hF0; exact hF0
  have hl' : ∀ b ∈ l, b < 117 := hl
  cases l with
  | nil => exact absurd hF (by decide)
  | cons a rest =>
    have ha : a < 116 ∧ a % 4 < 3 := by
      apply fin_start a (hl' a (by simp))
      intro hd; simp only [run, hd, run_dead] at hF; exact absurd hF (by decide)
    obtain ⟨w, S, hv, hS⟩ := structure_aux _ (a :: rest) 0 (Nat.le_refl _) hl'
      (fun b hb => by simp at hb; subst hb; exact ha) (by simp) hF
    exact ⟨w :: S, hv, hS.symm⟩

theorem mem_sentChain_116 (w v : List Syl) (S : List (List Syl)) : 116 ∈ sentChain (w :: v :: S) := by
  simp [sentChain]

/-- **القانونُ يولّد المقاطع (الكلمة).** -/
theorem word_structure (l : List Nat) (h : Mword.Lic 0 l) :
    ∃ w, w ≠ [] ∧ (∀ x ∈ w, Valid x) ∧ wordChain w = l := by
  have hs : Msent.Lic 0 l := ⟨fun a ha => by
      have h1 := h.1 a ha; have e1 : Mword.A = 116 := rfl; have e2 : Msent.A = 117 := rfl; omega,
    by have := h.2; rw [Mword, mk_run] at this; rw [Msent, mk_run]; exact this⟩
  obtain ⟨S, hv, hS⟩ := sent_structure l hs
  match S, hv, hS with
  | [], _, hS => exact absurd (by rw [← hS]; rfl : l = []) (by
      intro hl; subst hl; have := h.2; rw [Mword, mk_run] at this; exact absurd this (by decide))
  | [w], hv, hS => exact ⟨w, (hv w (by simp)).1, fun x hx => ((hv w (by simp)).2 x hx).1, hS⟩
  | w :: v :: S, _, hS =>
    have := h.1 116 (by rw [← hS]; exact mem_sentChain_116 w v S)
    simp [Mword, mk] at this

/-! ### الوحدانيّة: الانقسامُ واحد -/

theorem cellsOf_bounds (x : Syl) (hx : Valid x) : ∀ y ∈ cellsOf x, y.1 < 29 ∧ y.2 < 4 := by
  obtain ⟨t, o, k₁, k₂⟩ := x
  obtain ⟨ht, ho, h₁, h₂⟩ := hx
  dsimp only at ht ho h₁ h₂
  have hM := maddOf_lt (o % 3)
  intro y hy
  match t, ht with
  | 0, _ => simp [cellsOf] at hy; subst hy; simp; omega
  | 1, _ => simp [cellsOf] at hy; rcases hy with rfl | rfl <;> simp <;> omega
  | 2, _ =>
    simp only [radix] at h₁; have := skip_lt _ _ hM h₁
    simp [cellsOf] at hy; rcases hy with rfl | rfl <;> simp <;> omega
  | 3, _ =>
    simp only [radix] at h₁
    simp [cellsOf] at hy; rcases hy with rfl | rfl | rfl <;> simp <;> omega
  | 4, _ =>
    simp only [radix] at h₁ h₂; have := skip_lt _ _ hM h₁
    simp [cellsOf] at hy; rcases hy with rfl | rfl | rfl <;> simp <;> omega
  | 5, _ =>
    simp only [radix] at h₁ h₂
    simp [cellsOf] at hy; rcases hy with rfl | rfl | rfl | rfl <;> simp <;> omega

def chainCells (l : List Nat) : List (Nat × Nat) := l.map fun a => (a / 4, a % 4)

theorem chainCells_append (l r : List Nat) : chainCells (l ++ r) = chainCells l ++ chainCells r :=
  List.map_append

theorem chainCells_syl (x : Syl) (hx : Valid x) : chainCells (chainOf x) = cellsOf x := by
  simp only [chainCells, chainOf, List.map_map]
  conv => rhs; rw [← List.map_id (cellsOf x)]
  apply List.map_congr_left
  intro y hy
  have := cellsOf_bounds x hx y hy
  obtain ⟨c, s⟩ := y
  simp [sym] at this ⊢; omega

theorem chainCells_word : ∀ (w : List Syl), (∀ x ∈ w, Valid x) →
    chainCells (wordChain w) = wordCells w
  | [], _ => rfl
  | x :: w, h => by
    have e1 : wordChain (x :: w) = chainOf x ++ wordChain w := by simp [wordChain, List.flatMap_cons]
    have e2 : wordCells (x :: w) = cellsOf x ++ wordCells w := by simp [wordCells, List.flatMap_cons]
    rw [e1, e2, chainCells_append, chainCells_syl x (h x (by simp)),
      chainCells_word w (fun y hy => h y (by simp [hy]))]

theorem wordChain_lt (w : List Syl) (hw : ∀ x ∈ w, Valid x) : ∀ a ∈ wordChain w, a < 116 := by
  intro a ha
  simp only [wordChain, chainOf, List.mem_flatMap, List.mem_map] at ha
  obtain ⟨x, hx, y, hy, rfl⟩ := ha
  have := cellsOf_bounds x (hw x hx) y hy
  simp only [sym]; omega

/-- **وحدانيّةُ تقطيع الكلمة:** سلسلتُها تعيّن مقاطعَها. -/
theorem wordChain_inj (w w' : List Syl) (hw : ∀ x ∈ w, Valid x) (hw' : ∀ x ∈ w', Valid x)
    (h : wordChain w = wordChain w') : w = w' := by
  have e := congrArg (fun l => wordOfCells (chainCells l)) h
  simp only [chainCells_word w hw, chainCells_word w' hw', word_of_cells w hw,
    word_of_cells w' hw'] at e
  exact Option.some.inj e

def splitH : List Nat → List (List Nat)
  | [] => [[]]
  | a :: l => if a = 116 then [] :: splitH l else
      match splitH l with
      | [] => [[a]]
      | u :: us => (a :: u) :: us

theorem splitH_word : ∀ (u : List Nat), (∀ a ∈ u, a < 116) → splitH u = [u]
  | [], _ => rfl
  | a :: u, h => by
    have ha := h a (by simp)
    simp only [splitH, if_neg (by omega : a ≠ 116), splitH_word u (fun b hb => h b (by simp [hb]))]

theorem splitH_join : ∀ (u t : List Nat), (∀ a ∈ u, a < 116) →
    splitH (u ++ 116 :: t) = u :: splitH t
  | [], t, _ => by simp [splitH]
  | a :: u, t, h => by
    have ha := h a (by simp)
    simp only [List.cons_append, splitH, if_neg (by omega : a ≠ 116),
      splitH_join u t (fun b hb => h b (by simp [hb]))]

theorem splitH_sent : ∀ (S : List (List Syl)), ValidS S → S ≠ [] →
    splitH (sentChain S) = S.map wordChain
  | [], _, h => absurd rfl h
  | [w], hv, _ => by
    simp only [sentChain, List.map]
    exact splitH_word _ (wordChain_lt w fun x hx => ((hv w (by simp)).2 x hx).1)
  | w :: v :: S, hv, _ => by
    simp only [sentChain]
    rw [splitH_join _ _ (wordChain_lt w fun x hx => ((hv w (by simp)).2 x hx).1)]
    have := splitH_sent (v :: S) (fun u hu => hv u (List.mem_cons_of_mem _ hu)) (by simp)
    rw [show sentChain (v :: S) = sentChain (v :: S) from rfl] at this
    simp only [List.map_cons] at this ⊢
    rw [this]

theorem map_inj_valid : ∀ (S S' : List (List Syl)), ValidS S → ValidS S' →
    S.map wordChain = S'.map wordChain → S = S'
  | [], [], _, _, _ => rfl
  | [], _ :: _, _, _, h => by simp at h
  | _ :: _, [], _, _, h => by simp at h
  | w :: S, w' :: S', hv, hv', h => by
    simp only [List.map_cons, List.cons.injEq] at h
    rw [wordChain_inj w w' (fun x hx => ((hv w (by simp)).2 x hx).1)
      (fun x hx => ((hv' w' (by simp)).2 x hx).1) h.1,
      map_inj_valid S S' (fun u hu => hv u (by simp [hu])) (fun u hu => hv' u (by simp [hu])) h.2]

/-- **وحدانيّةُ تقطيع الجملة:** سلسلتُها تعيّن كلماتها ومقاطعها. -/
theorem sentChain_inj (S S' : List (List Syl)) (hv : ValidS S) (hv' : ValidS S') (hS : S ≠ [])
    (hS' : S' ≠ []) (h : sentChain S = sentChain S') : S = S' := by
  apply map_inj_valid S S' hv hv'
  rw [← splitH_sent S hv hS, ← splitH_sent S' hv' hS', h]

/-! ## 5. الاستنفادُ بالعدّ، والترقيمُ المتدرّج -/

theorem bound_aux : ∀ (l : List Nat) (q : Nat), q < 96 → (∀ a ∈ l, a < 117) → run q l ≠ 96 →
    l.length + pot (run q l) ≤ 3 * wt q l + pot q
  | [], q, _, _, _ => by simp [run, wt]
  | a :: l, q, hq, hl, hr => by
    have hd : δ q a ≠ 96 := fun h => hr (by simp only [run, h, run_dead])
    have hs := fin_pot q hq a (hl a (by simp)) hd
    have hle := δ_le q a
    have ih := bound_aux l (δ q a) (by omega) (fun b hb => hl b (by simp [hb])) hr
    simp only [run, wt, List.length_cons] at ih ⊢
    omega

theorem bound (l : List Nat) (hl : ∀ a ∈ l, a < 117) (hr : run 0 l ≠ 96) : l.length ≤ 3 * wt 0 l := by
  have := bound_aux l 0 (by decide) hl hr
  simp [pot] at this; omega

theorem live_of_F (q : Nat) (h : Fwaqf q = true ∨ Fwasl q = true) : q ≠ 96 := by
  intro hq; subst hq; simp [Fwaqf, Fwasl] at h

theorem hK (A : Nat) (F : Nat → Bool) (hA : A ≤ 117) (hF : ∀ q, F q = true → q ≠ 96) :
    ∀ l, (mk A F).Lic 0 l → l.length ≤ 3 * (mk A F).wtL 0 l := by
  intro l ⟨hl, h⟩
  rw [mk_wt]; rw [mk_run] at h
  exact bound l (fun a ha => by have := hl a ha; simp [mk] at this; omega) (hF _ h)

/-- سلسلةُ ‎n‎ فتحاتٍ على الباء (ب=26): «بَبَبَ…». -/
theorem chain_ba : ∀ n : Nat, run 1 (List.replicate n (4 * 26)) = 1 ∧ wt 1 (List.replicate n (4 * 26)) = n
  | 0 => ⟨rfl, rfl⟩
  | n + 1 => by
    have := chain_ba n
    simp only [List.replicate_succ, run, wt]
    have e1 : δ 1 (4 * 26) = 1 := by decide
    have e2 : ω 1 (4 * 26) = 1 := by decide
    rw [e1, e2, this.1, this.2]; exact ⟨rfl, by omega⟩

theorem hpos (A : Nat) (F : Nat → Bool) (hA : 105 ≤ A) (hF1 : F 1 = true) :
    ∀ j, 0 < (mk A F).lev 3 0 (j + 1) := by
  intro j
  let l := List.replicate (j + 1) (4 * 26)
  have hrun : run 0 l = 1 ∧ wt 0 l = j + 1 := by
    have := chain_ba j
    simp only [l, List.replicate_succ, run, wt]
    have e1 : δ 0 (4 * 26) = 1 := by decide
    have e2 : ω 0 (4 * 26) = 1 := by decide
    rw [e1, e2, this.1, this.2]; exact ⟨rfl, by omega⟩
  have hacc : (mk A F).Acc (3 * (j + 1)) (j + 1) 0 l := by
    rw [Machine.acc_iff]
    refine ⟨fun a ha => ?_, by simp [l]; omega, by rw [mk_wt]; exact hrun.2,
      by rw [mk_run, hrun.1]; exact hF1⟩
    simp [l] at ha; subst ha; simp [mk]; omega
  have := (mk A F).rank_lt l _ _ _ hacc
  unfold Machine.lev; omega

theorem closure68 (A : Nat) (F : Nat → Bool) (hA : A ≤ 117) :
    ∀ q < 97, ∀ a < (mk A F).A, (mk A F).δ q a < 97 := by
  intro q hq a ha
  exact fin_close q hq a (by simp [mk] at ha; omega)

/-- **العدُّ في الدرجات (الكلمة موقوفًا عليها):** ‎0, 168, 32872, 6038368‎ لصامتٍ ‎0, 1, 2, 3‎. -/
theorem word_levels : Mword.lev 3 0 0 = 0 ∧ Mword.lev 3 0 1 = 168 ∧ Mword.lev 3 0 2 = 32872 ∧
    Mword.lev 3 0 3 = 6038368 := by
  have t := fun f w => (Mword.tab_eq 97 3 (closure68 116 Fwaqf (by decide)) f w 0)
  simp only [Machine.lev]
  rw [← t 0 0 (by decide) (by decide), ← t 3 1 (by decide) (by decide),
    ← t 6 2 (by decide) (by decide), ← t 9 3 (by decide) (by decide)]
  decide +kernel

/-- **العدُّ في الدرجات (الكلمة في الوصل):** يسقط ‎CVCC‎ و‎CVVCC‎ آخرًا: ‎5908224‎ في الثالثة. -/
theorem word_levels_wasl : MwordWasl.lev 3 0 1 = 168 ∧ MwordWasl.lev 3 0 2 = 32872 ∧
    MwordWasl.lev 3 0 3 = 5908224 := by
  have t := fun f w => (MwordWasl.tab_eq 97 3 (closure68 116 Fwasl (by decide)) f w 0)
  simp only [Machine.lev]
  rw [← t 3 1 (by decide) (by decide), ← t 6 2 (by decide) (by decide),
    ← t 9 3 (by decide) (by decide)]
  decide +kernel

/-- **العدُّ في الدرجات (الجملة):** ‎0, 168, 61096, 21443968‎. -/
theorem sent_levels : Msent.lev 3 0 0 = 0 ∧ Msent.lev 3 0 1 = 168 ∧ Msent.lev 3 0 2 = 61096 ∧
    Msent.lev 3 0 3 = 21443968 := by
  have t := fun f w => (Msent.tab_eq 97 3 (closure68 117 Fwaqf (by decide)) f w 0)
  simp only [Machine.lev]
  rw [← t 0 0 (by decide) (by decide), ← t 3 1 (by decide) (by decide),
    ← t 6 2 (by decide) (by decide), ← t 9 3 (by decide) (by decide)]
  decide +kernel

def wordNum (l : List Nat) : Nat := Mword.gEnc 3 0 l
def wordOfNum (n : Nat) : List Nat := Mword.gDec 3 0 n
def sentNum (l : List Nat) : Nat := Msent.gEnc 3 0 l
def sentOfNum (n : Nat) : List Nat := Msent.gDec 3 0 n

theorem word_graded :
    (∀ l, Mword.Lic 0 l → wordOfNum (wordNum l) = l) ∧
    (∀ n, Mword.Lic 0 (wordOfNum n) ∧ wordNum (wordOfNum n) = n) ∧
    (∀ l, Mword.Lic 0 l → Machine.offFrom (Mword.lev 3 0) 0 (Mword.wtL 0 l) ≤ wordNum l ∧
      wordNum l < Machine.offFrom (Mword.lev 3 0) 0 (Mword.wtL 0 l + 1)) :=
  Mword.graded 3 0 (hK 116 Fwaqf (by decide) fun q h => live_of_F q (Or.inl h))
    (hpos 116 Fwaqf (by decide) (by decide))

theorem sent_graded :
    (∀ l, Msent.Lic 0 l → sentOfNum (sentNum l) = l) ∧
    (∀ n, Msent.Lic 0 (sentOfNum n) ∧ sentNum (sentOfNum n) = n) ∧
    (∀ l, Msent.Lic 0 l → Machine.offFrom (Msent.lev 3 0) 0 (Msent.wtL 0 l) ≤ sentNum l ∧
      sentNum l < Machine.offFrom (Msent.lev 3 0) 0 (Msent.wtL 0 l + 1)) :=
  Msent.graded 3 0 (hK 117 Fwaqf (by decide) fun q h => live_of_F q (Or.inl h))
    (hpos 117 Fwaqf (by decide) (by decide))

/-- **عددُ الدرجة ‎W‎ (الكلمة):** المرخَّصاتُ بوزن ‎W‎ تقابلُ ‎[0, lev W)‎. -/
theorem word_count (W : Nat) :
    (∀ l, Mword.Lic 0 l → Mword.wtL 0 l = W → Mword.rank (3 * W) W 0 l < Mword.lev 3 0 W) ∧
    (∀ l l', Mword.Lic 0 l → Mword.Lic 0 l' → Mword.wtL 0 l = W → Mword.wtL 0 l' = W →
      Mword.rank (3 * W) W 0 l = Mword.rank (3 * W) W 0 l' → l = l') ∧
    (∀ i, i < Mword.lev 3 0 W → ∃ l, Mword.Lic 0 l ∧ Mword.wtL 0 l = W ∧
      Mword.rank (3 * W) W 0 l = i) :=
  Mword.level_count 3 0 W (hK 116 Fwaqf (by decide) fun q h => live_of_F q (Or.inl h))

/-- **عددُ الدرجة ‎W‎ (الجملة).** -/
theorem sent_count (W : Nat) :
    (∀ l, Msent.Lic 0 l → Msent.wtL 0 l = W → Msent.rank (3 * W) W 0 l < Msent.lev 3 0 W) ∧
    (∀ l l', Msent.Lic 0 l → Msent.Lic 0 l' → Msent.wtL 0 l = W → Msent.wtL 0 l' = W →
      Msent.rank (3 * W) W 0 l = Msent.rank (3 * W) W 0 l' → l = l') ∧
    (∀ i, i < Msent.lev 3 0 W → ∃ l, Msent.Lic 0 l ∧ Msent.wtL 0 l = W ∧
      Msent.rank (3 * W) W 0 l = i) :=
  Msent.level_count 3 0 W (hK 117 Fwaqf (by decide) fun q h => live_of_F q (Or.inl h))

end Law
end SLGE
