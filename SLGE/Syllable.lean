import SLGE.Law

/-!
# المقطع وحده: ترقيمٌ متدرّجٌ لا ثغرةَ فيه

المقطعُ سلسلةٌ فيها متحرّكٌ واحد. آلتُه آلةُ القانون نفسُها مع شرطٍ واحد: لا متحرّكَ ولا حدَّ بعد الأوّل.
فيُرقَّم ما يرخّصه القانونُ من المقاطع وحدَه — لا ما يُعَدّ من القوالب وتُميته الألف — ترقيمًا متدرّجًا
بعدد الصوامت: ‎168‎ ثمّ ‎4648‎ ثمّ ‎130144‎، ومجموعُها ‎134960‎؛ والمرخَّصُ منها في الوصل ‎4816‎.
-/

namespace SLGE
namespace Law

def δ1 (q a : Nat) : Nat :=
  if 1 ≤ q ∧ a < 116 ∧ a % 4 < 3 then 96 else if a = 116 then 96 else δ q a

def Msyl : Machine := ⟨116, δ1, ω, Fwaqf⟩
def MsylWasl : Machine := ⟨116, δ1, ω, Fwasl⟩

theorem δ1_dead (a : Nat) : δ1 96 a = 96 := by
  unfold δ1; split
  · rfl
  · split
    · rfl
    · exact δ_big a (Nat.le_refl 96)

theorem run1_dead (F : Nat → Bool) : ∀ l, (Machine.mk 116 δ1 ω F).runL 96 l = 96
  | [] => rfl
  | a :: l => by
    show (Machine.mk 116 δ1 ω F).runL (δ1 96 a) l = 96
    rw [δ1_dead]; exact run1_dead F l

theorem δ1_eq (q a : Nat) (h : δ1 q a ≠ 96) : δ1 q a = δ q a := by
  unfold δ1 at h ⊢; split
  · simp_all
  · split
    · simp_all
    · rfl

theorem run1_live (F : Nat → Bool) : ∀ (q : Nat) (l : List Nat), (Machine.mk 116 δ1 ω F).runL q l ≠ 96 →
    (Machine.mk 116 δ1 ω F).runL q l = run q l ∧ (Machine.mk 116 δ1 ω F).wtL q l = wt q l
  | _, [], _ => ⟨rfl, rfl⟩
  | q, a :: l, h => by
    have hd : δ1 q a ≠ 96 := by
      intro e; apply h
      show (Machine.mk 116 δ1 ω F).runL (δ1 q a) l = 96
      rw [e]; exact run1_dead F l
    have ih := run1_live F (δ1 q a) l h
    rw [δ1_eq q a hd] at ih
    constructor
    · show (Machine.mk 116 δ1 ω F).runL (δ1 q a) l = run (δ q a) l
      rw [δ1_eq q a hd]; exact ih.1
    · show ω q a + (Machine.mk 116 δ1 ω F).wtL (δ1 q a) l = ω q a + wt (δ q a) l
      rw [δ1_eq q a hd, ih.2]

theorem live_of (F : Nat → Bool) (hF : ∀ q, F q = true → q ≠ 96) (l : List Nat)
    (h : (Machine.mk 116 δ1 ω F).Lic 0 l) : (Machine.mk 116 δ1 ω F).runL 0 l ≠ 96 :=
  hF _ h.2

/-- أعلى وزنٍ يبقى من كلّ حالةٍ داخل مقطعٍ واحد. -/
def maxw (q : Nat) : Nat :=
  if q = 0 then 3 else if q ≤ 4 then 2 else if q < 35 then 1
  else if 67 ≤ q ∧ q < 96 then 1 else 0

theorem fin_maxw : ∀ q < 96, ∀ a < 116, δ1 q a ≠ 96 → ω q a + maxw (δ1 q a) ≤ maxw q := by
  decide +kernel

theorem fin_close1 : ∀ q < 97, ∀ a < 116, δ1 q a < 97 := by decide +kernel

theorem δ1_le (q a : Nat) : δ1 q a ≤ 96 := by
  unfold δ1; split
  · omega
  · split
    · omega
    · exact δ_le q a

theorem wt_bound1 (F : Nat → Bool) : ∀ (l : List Nat) (q : Nat), q < 96 → (∀ a ∈ l, a < 116) →
    (Machine.mk 116 δ1 ω F).runL q l ≠ 96 → (Machine.mk 116 δ1 ω F).wtL q l ≤ maxw q
  | [], _, _, _, _ => Nat.zero_le _
  | a :: l, q, hq, hl, h => by
    have hd : δ1 q a ≠ 96 := by
      intro e; apply h
      show (Machine.mk 116 δ1 ω F).runL (δ1 q a) l = 96
      rw [e]; exact run1_dead F l
    have hs := fin_maxw q hq a (hl a (by simp)) hd
    have ih := wt_bound1 F l (δ1 q a) (by have := δ1_le q a; omega) (fun b hb => hl b (by simp [hb])) h
    show ω q a + (Machine.mk 116 δ1 ω F).wtL (δ1 q a) l ≤ maxw q
    omega

theorem hK1 (F : Nat → Bool) (hF : ∀ q, F q = true → q ≠ 96) :
    ∀ l, (Machine.mk 116 δ1 ω F).Lic 0 l → l.length ≤ 3 * (Machine.mk 116 δ1 ω F).wtL 0 l := by
  intro l hl
  have hlive := live_of F hF l hl
  have e := run1_live F 0 l hlive
  rw [e.2]
  apply bound l (fun a ha => by have := hl.1 a ha; simp at this; omega)
  rw [← e.1]; exact hlive

theorem hW1 (F : Nat → Bool) (hF : ∀ q, F q = true → q ≠ 96) :
    ∀ l, (Machine.mk 116 δ1 ω F).Lic 0 l → (Machine.mk 116 δ1 ω F).wtL 0 l ≤ 3 := by
  intro l hl
  have := wt_bound1 F l 0 (by decide) (fun a ha => by have := hl.1 a ha; simp at this; exact this)
    (live_of F hF l hl)
  simpa [maxw] using this

theorem hFwaqf : ∀ q, Fwaqf q = true → q ≠ 96 := fun q h => live_of_F q (Or.inl h)
theorem hFwasl : ∀ q, Fwasl q = true → q ≠ 96 := fun q h => live_of_F q (Or.inr h)

theorem lev_tab (F : Nat → Bool) (j : Nat) (hj : j ≤ 3) :
    (Machine.mk 116 δ1 ω F).lev 3 0 j = (((Machine.mk 116 δ1 ω F).tab 97 3 (3 * j)).getD j []).getD 0 0 :=
  ((Machine.mk 116 δ1 ω F).tab_eq 97 3 fin_close1 (3 * j) j 0 hj (by decide)).symm

theorem sl0 : Msyl.lev 3 0 0 = 0 := by rw [Msyl, lev_tab _ 0 (by decide)]; decide +kernel
theorem sl1 : Msyl.lev 3 0 1 = 168 := by rw [Msyl, lev_tab _ 1 (by decide)]; decide +kernel
theorem sl2 : Msyl.lev 3 0 2 = 4648 := by rw [Msyl, lev_tab _ 2 (by decide)]; decide +kernel
theorem sl3 : Msyl.lev 3 0 3 = 130144 := by rw [Msyl, lev_tab _ 3 (by decide)]; decide +kernel
theorem slw1 : MsylWasl.lev 3 0 1 = 168 := by rw [MsylWasl, lev_tab _ 1 (by decide)]; decide +kernel
theorem slw2 : MsylWasl.lev 3 0 2 = 4648 := by rw [MsylWasl, lev_tab _ 2 (by decide)]; decide +kernel
theorem slw3 : MsylWasl.lev 3 0 3 = 0 := by rw [MsylWasl, lev_tab _ 3 (by decide)]; decide +kernel

/-- **الاستنفادُ في المقطع:** ‎0, 168, 4648, 130144‎ لصامتٍ ‎0, 1, 2, 3‎؛ وفي الوصل ‎0, 168, 4648, 0‎. -/
theorem syl_levels : Msyl.lev 3 0 0 = 0 ∧ Msyl.lev 3 0 1 = 168 ∧ Msyl.lev 3 0 2 = 4648 ∧
    Msyl.lev 3 0 3 = 130144 ∧
    MsylWasl.lev 3 0 1 = 168 ∧ MsylWasl.lev 3 0 2 = 4648 ∧ MsylWasl.lev 3 0 3 = 0 :=
  ⟨sl0, sl1, sl2, sl3, slw1, slw2, slw3⟩

theorem offFrom_four (L : Nat → Nat) : Machine.offFrom L 0 (3 + 1) = L 0 + L 1 + L 2 + L 3 := by
  show L 0 + (L 1 + (L 2 + (L 3 + 0))) = _; omega

theorem eoff : Machine.offFrom (Msyl.lev 3 0) 0 (3 + 1) = 134960 := by
  rw [offFrom_four, sl0, sl1, sl2, sl3]

def sylNum (l : List Nat) : Nat := Msyl.gEnc 3 0 l
def sylOfNum (n : Nat) : List Nat := Msyl.gDecF 3 0 3 n

/-- **ترقيمُ المقطع المرخَّص:** تقابلٌ بين المقاطع التي يرخّصها القانون و‎[0, 134960)‎، متدرّجٌ بالصوامت. -/
theorem syl_numbering :
    (∀ l, Msyl.Lic 0 l → sylOfNum (sylNum l) = l) ∧
    (∀ n, n < 134960 → Msyl.Lic 0 (sylOfNum n) ∧ sylNum (sylOfNum n) = n) ∧
    (∀ l, Msyl.Lic 0 l → Machine.offFrom (Msyl.lev 3 0) 0 (Msyl.wtL 0 l) ≤ sylNum l ∧
      sylNum l < Machine.offFrom (Msyl.lev 3 0) 0 (Msyl.wtL 0 l + 1)) := by
  have g := Msyl.gradedFin 3 0 3 (hK1 Fwaqf hFwaqf) (hW1 Fwaqf hFwaqf)
  exact ⟨g.1, fun n hn => g.2.1 n (by rw [eoff]; exact hn), g.2.2⟩

/-- **المقطعُ المرخَّص أحدُ الستّة، ولا ألفَ فيه فاتحًا ولا مُغلِقًا.** -/
theorem syl_structure (l : List Nat) (h : Msyl.Lic 0 l) :
    ∃ x, Valid x ∧ AlifOK x ∧ chainOf x = l := by
  have hlive : Msyl.runL 0 l ≠ 96 := hFwaqf _ h.2
  have e := run1_live Fwaqf 0 l hlive
  have hrun : run 0 l ≠ 96 := by rw [← e.1]; exact hlive
  cases l with
  | nil => exact absurd h.2 (by decide)
  | cons a rest =>
    have hA : ∀ b ∈ a :: rest, b < 116 := h.1
    have ha : a < 116 ∧ a % 4 < 3 := by
      apply fin_start a (by have := hA a (by simp); omega)
      intro hd; apply hrun; simp only [run, hd, run_dead]
    obtain ⟨x, r, ⟨hx, hxa⟩, heq, hr⟩ := split 0 a rest ha.1 ha.2 hrun
    refine ⟨x, hx, hxa, ?_⟩
    rcases r with _ | ⟨b, r'⟩
    · simpa using heq.symm
    · exfalso
      have hb : b < 116 := hA b (by rw [heq]; simp)
      have hbs := hr b (by simp)
      have hq0 : δ 0 (onsetSym x) ≠ 96 := by
        intro hd; apply hrun; rw [heq, run_append]
        obtain ⟨t, o, k₁, k₂⟩ := x
        have : chainOf (t, o, k₁, k₂) = onsetSym (t, o, k₁, k₂) :: (chainOf (t, o, k₁, k₂)).tail := by
          match t with
          | 0 | 1 | 2 | 3 | 4 => rfl
          | _ + 5 => rfl
        rw [this]; simp only [run, hd, run_dead, δ_big _ (Nat.le_refl 96)]
      have hs := (syl_run x hx hxa 0 hq0).1
      have hpos : 1 ≤ endSt x := by
        unfold endSt; split <;> omega
      have hsame : Msyl.runL 0 (chainOf x) = endSt x := by
        have hl1 : Msyl.runL 0 (chainOf x) ≠ 96 := by
          intro h0; apply hlive; rw [heq, Machine.runL_append, h0]; exact run1_dead Fwaqf _
        exact (run1_live Fwaqf 0 _ hl1).1.trans hs
      apply hlive
      rw [heq, Machine.runL_append, hsame]
      show Msyl.runL (δ1 (endSt x) b) r' = 96
      have : δ1 (endSt x) b = 96 := by
        unfold δ1; rw [if_pos ⟨hpos, hb, by omega⟩]
      rw [this]; exact run1_dead Fwaqf r'

end Law
end SLGE
