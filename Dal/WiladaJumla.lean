import Dal.WiladaKalima

/-!
# ولادةُ الجملة بقانون العدّ الواحد: الأصنافُ نفسُها والحدُّ انتقالٌ بلا وزن

قولُ المالك في الجلسة (2026-11-01، 12:40 بتوقيت عمّان): «… ولكن يجب ان نوحد الحساب من الان وصاعدا بقانون واحد جبري».

آلةُ الجملة للمالك (`SLGE.Law.Msent`: الخاناتُ الـ116 والحدُّ 116) كما هي. وأصنافُ الكلمة الثلاثة عشر (`Dal.WiladaKalima.sK`)
نفسُها تتكافأ عليها (`jumla_mutakafi`)، وحدُّ الكلمة مدخلٌ وزنُه صفر: من الأصناف ‎1‎ و‎2‎ و‎3‎ و‎9‎ و‎10‎ و‎11‎ إلى الابتداء، ومن ‎5‎ إلى ‎7‎،
وممّا سواها إلى الممتنع. فيخرج من القانون الواحد التكرار لكلّ درجة: `S(k+4) = 336·S(k+3) + 4676·S(k+2)` (`wilada_jumla`)،
وأعدادُ المالك (`SLGE.Law.sent_levels`) تُشتقّ به أيضًا، وبعدها الدرجةُ الرابعة 7490858144 (`jumla_bil_qanun`)؛ وقضيّتُه في
`SLGE/Law.lean` باقيةٌ بحسابها بالجدول `tab`.

والمعاملان من صفوف الأصناف (`jumla_khatwa`)؛ والمبرهَنُ التكرارُ نفسُه، وتأويلُ 336 و4676 بالمقاطع لم يُبنَ.

المبرهنات: 18 بالمعيار الموحَّد: لكلّ 10 (`potS`، `wazn1S`، `pS_le`، `z_khatwa`، `z_dead`، `jumla_khatwa`، `lev_jumla`، `tawlidS`، `awailS`،
`wilada_jumla`)؛ وتعريفيّة 2 (`saffS_kabir`، `mayyitS`)؛ وعلى الشاهد 3 برهانُها decide (`saffS_hadd`، `waznS`، `bidaya_jumla`)؛ و3 على الشاهد خارجَ
حرف المعيار، معلَن (`adadS`: من ثلاثَ عشرةَ مساعدةً خاصّةً برهانُها decide؛ `jumla_mutakafi`: بنيةٌ منها و`fin_close` للمالك؛ `jumla_bil_qanun`: `awailS`).
-/

namespace Dal.WiladaJumla
open SLGE SLGE.Law Dal.QanunAdad Dal.WiladaKalima

/-- **صفوفُ الأصناف** على الخانات والحدّ (117 رمزًا). -/
def saffS : Nat → List (Nat × Nat × Nat)
  | 0 => [(0, 8, 1), (1, 1, 28), (1, 2, 56), (1, 8, 32)]
  | 1 => [(0, 0, 1), (0, 3, 1), (1, 1, 28), (1, 2, 56), (1, 8, 3), (1, 9, 10), (1, 10, 9), (1, 11, 9)]
  | 2 => [(0, 0, 1), (0, 3, 1), (1, 1, 28), (1, 2, 56), (1, 8, 4), (1, 9, 10), (1, 10, 8), (1, 11, 9)]
  | 3 => [(0, 0, 1), (1, 1, 28), (1, 2, 56), (1, 5, 28), (1, 8, 4)]
  | 4 => [(0, 8, 1), (1, 8, 116)]
  | 5 => [(0, 7, 1), (1, 1, 1), (1, 2, 2), (1, 4, 28), (1, 8, 85)]
  | 6 => [(0, 8, 1), (1, 4, 28), (1, 8, 88)]
  | 7 => [(0, 8, 1), (1, 1, 1), (1, 2, 2), (1, 8, 113)]
  | 8 => [(0, 8, 1), (1, 8, 116)]
  | 9 => [(0, 0, 1), (1, 1, 27), (1, 2, 54), (1, 4, 28), (1, 8, 7)]
  | 10 => [(0, 0, 1), (1, 1, 28), (1, 2, 56), (1, 4, 28), (1, 8, 4)]
  | 11 => [(0, 0, 1), (1, 1, 26), (1, 2, 52), (1, 4, 28), (1, 8, 10)]
  | 12 => [(0, 8, 1), (1, 8, 116)]
  | _ => []

def QS : Asnaf := ⟨13, saffS, FW⟩

theorem saffS_hadd : ∀ q < 97, ∀ e ∈ saffS (sK q), e.1 ≤ 1 ∧ e.2.1 < 13 := by decide +kernel
theorem waznS : ∀ q < 97, ∀ b < 117, ω q b ≤ 1 := by decide +kernel
/-- ما يُفحص لكلّ حالة: عددُ انتقالاتها بكلّ وزنٍ إلى كلّ صنفٍ هو ما في صفّ صنفها. -/
abbrev ShartS (q : Nat) : Prop := ∀ u ≤ 1, ∀ j < 13,
    ((List.range 117).filter fun b => ω q b == u && sK (δ q b) == j).length =
      (((saffS (sK q)).filter fun e => e.1 == u && e.2.1 == j).map fun e => e.2.2).sum

private theorem ShartS_0 : ∀ r < 8, ShartS (r + 0) := by decide +kernel
private theorem ShartS_1 : ∀ r < 8, ShartS (r + 8) := by decide +kernel
private theorem ShartS_2 : ∀ r < 8, ShartS (r + 16) := by decide +kernel
private theorem ShartS_3 : ∀ r < 8, ShartS (r + 24) := by decide +kernel
private theorem ShartS_4 : ∀ r < 8, ShartS (r + 32) := by decide +kernel
private theorem ShartS_5 : ∀ r < 8, ShartS (r + 40) := by decide +kernel
private theorem ShartS_6 : ∀ r < 8, ShartS (r + 48) := by decide +kernel
private theorem ShartS_7 : ∀ r < 8, ShartS (r + 56) := by decide +kernel
private theorem ShartS_8 : ∀ r < 8, ShartS (r + 64) := by decide +kernel
private theorem ShartS_9 : ∀ r < 8, ShartS (r + 72) := by decide +kernel
private theorem ShartS_10 : ∀ r < 8, ShartS (r + 80) := by decide +kernel
private theorem ShartS_11 : ∀ r < 8, ShartS (r + 88) := by decide +kernel
private theorem ShartS_12 : ∀ r < 1, ShartS (r + 96) := by decide +kernel

theorem adadS : ∀ q < 97, ShartS q := by
  intro q hq
  have h : q < 8 ∨ (8 ≤ q ∧ q < 16) ∨ (16 ≤ q ∧ q < 24) ∨ (24 ≤ q ∧ q < 32) ∨ (32 ≤ q ∧ q < 40) ∨ (40 ≤ q ∧ q < 48) ∨ (48 ≤ q ∧ q < 56) ∨ (56 ≤ q ∧ q < 64) ∨ (64 ≤ q ∧ q < 72) ∨ (72 ≤ q ∧ q < 80) ∨ (80 ≤ q ∧ q < 88) ∨ (88 ≤ q ∧ q < 96) ∨ (96 ≤ q ∧ q < 97) := by omega
  rcases h with h | h | h | h | h | h | h | h | h | h | h | h | h
  · have := ShartS_0 q h; rwa [Nat.add_zero] at this
  · have := ShartS_1 (q - 8) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_2 (q - 16) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_3 (q - 24) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_4 (q - 32) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_5 (q - 40) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_6 (q - 48) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_7 (q - 56) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_8 (q - 64) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_9 (q - 72) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_10 (q - 80) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_11 (q - 88) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartS_12 (q - 96) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this

/-- **التكافؤ:** حالاتُ الجملة تتكافأ في أصناف الكلمة الثلاثة عشر نفسِها. -/
theorem jumla_mutakafi : Mutakafi Msent QS 1 sK (fun q => q < 97) where
  maghluq := fun q hq b hb => fin_close q hq b hb
  sinf := sinfK
  wazn := fun q hq b hb => waznS q hq b hb
  saff := saffS_hadd
  qubul := by show ∀ q < 97, Fwaqf q = FW (sK q); decide +kernel
  adad := adadS

/-! ## العدُّ على الأصناف -/

/-- الجهد: يكفي الصنفَ طولُ ‎`3·w + pS i`‎. -/
def pS (i : Nat) : Nat := if i = 1 ∨ i = 2 then 2 else if i = 3 ∨ i = 5 ∨ i = 9 ∨ i = 10 ∨ i = 11 then 1 else 0

theorem saffS_kabir (i : Nat) (h : 13 ≤ i) : saffS i = [] := by
  match i, h with
  | n + 13, _ => rfl

theorem mayyitS : ∀ i, (i == 8) = true → QS.F i = false ∧ ∀ e ∈ QS.saff i, (e.2.1 == 8) = true := by
  intro i hi; simp at hi; subst hi; exact ⟨rfl, by simp [QS, saffS]⟩

theorem potS : ∀ i, (i == 8) = false → ∀ e ∈ QS.saff i, (e.2.1 == 8) = false → pS e.2.1 + 1 ≤ pS i + 3 * e.1 := by
  intro i hi e he hj
  have : i < 13 ∨ 13 ≤ i := by omega
  rcases this with h | h
  · have k : ∀ i < 13, (i == 8) = false → ∀ e ∈ saffS i, (e.2.1 == 8) = false → pS e.2.1 + 1 ≤ pS i + 3 * e.1 := by
      decide +kernel
    exact k i h hi e he hj
  · simp [QS, saffS_kabir i h] at he

theorem wazn1S : ∀ i, ∀ e ∈ QS.saff i, e.1 ≤ 1 := by
  intro i e he
  have : i < 13 ∨ 13 ≤ i := by omega
  rcases this with h | h
  · have k : ∀ i < 13, ∀ e ∈ saffS i, e.1 ≤ 1 := by decide +kernel
    exact k i h e he
  · simp [QS, saffS_kabir i h] at he

theorem pS_le : ∀ i, pS i ≤ 2 := by intro i; unfold pS; split <;> (try split) <;> omega

/-- ما يُكمل الجملةَ بوزن ‎`n`‎ من الصنف ‎`i`‎ (بطولٍ كافٍ ‎`3n + 2`‎). -/
def z (i n : Nat) : Nat := QS.C (3 * n + 2) n i

theorem z_khatwa (i n : Nat) : z i (n + 1) = QS.base (n + 1) i +
    ((QS.saff i).map fun e => e.2.2 * (if e.1 = 0 then z e.2.1 (n + 1) else z e.2.1 n)).sum :=
  QS.C_khatwa1 3 2 pS (· == 8) mayyitS potS (by decide +kernel) pS_le wazn1S n i

theorem z_dead (n : Nat) : z 8 n = 0 := QS.mayyit_sifr (· == 8) mayyitS _ _ 8 rfl

/-- **صفوفُ الخطوة.** -/
theorem jumla_khatwa (n : Nat) :
    z 0 (n + 1) = 28 * z 1 n + 56 * z 2 n ∧
    z 1 (n + 1) = z 0 (n + 1) + z 3 (n + 1) + 28 * z 1 n + 56 * z 2 n + 10 * z 9 n + 9 * z 10 n + 9 * z 11 n ∧
    z 2 (n + 1) = z 0 (n + 1) + z 3 (n + 1) + 28 * z 1 n + 56 * z 2 n + 10 * z 9 n + 8 * z 10 n + 9 * z 11 n ∧
    z 3 (n + 1) = z 0 (n + 1) + 28 * z 1 n + 56 * z 2 n + 28 * z 5 n ∧
    z 4 (n + 1) = 0 ∧
    z 5 (n + 1) = z 7 (n + 1) + z 1 n + 2 * z 2 n + 28 * z 4 n ∧
    z 7 (n + 1) = z 1 n + 2 * z 2 n ∧
    z 9 (n + 1) = z 0 (n + 1) + 27 * z 1 n + 54 * z 2 n + 28 * z 4 n ∧
    z 10 (n + 1) = z 0 (n + 1) + 28 * z 1 n + 56 * z 2 n + 28 * z 4 n ∧
    z 11 (n + 1) = z 0 (n + 1) + 26 * z 1 n + 52 * z 2 n + 28 * z 4 n := by
  have d := z_dead
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
  · rw [z_khatwa]
    simp [QS, saffS, Asnaf.base, d, FW]
    try omega

theorem bidaya_jumla : z 0 0 = 0 ∧ z 1 0 = 2 ∧ z 2 0 = 2 ∧ z 3 0 = 1 ∧ z 4 0 = 1 ∧ z 5 0 = 1 ∧ z 7 0 = 0 ∧
    z 9 0 = 1 ∧ z 10 0 = 1 ∧ z 11 0 = 1 := by decide +kernel

/-- **العدُّ بالأصناف:** عددُ الجمل بوزن ‎`n`‎ عند المالك هو العدُّ من صنف الابتداء. -/
theorem lev_jumla (n : Nat) : Msent.lev 3 0 n = z 0 n := by
  unfold Machine.lev z
  rw [qanun_adad Msent QS 1 sK _ jumla_mutakafi (3 * n) n 0 (by decide +kernel)]
  exact QS.C_thabit2 3 pS (· == 8) mayyitS potS n 0 _ _ (by have : pS 0 = 0 := rfl; omega) (by have : pS 0 = 0 := rfl; omega)

/-- صفوفُ خطوة الجملة على متتاليةٍ مجرّدة. -/
def KhatwaS (Z : Nat → Nat → Nat) : Prop := ∀ n,
    Z 0 (n + 1) = 28 * Z 1 n + 56 * Z 2 n ∧
    Z 1 (n + 1) = Z 0 (n + 1) + Z 3 (n + 1) + 28 * Z 1 n + 56 * Z 2 n + 10 * Z 9 n + 9 * Z 10 n + 9 * Z 11 n ∧
    Z 2 (n + 1) = Z 0 (n + 1) + Z 3 (n + 1) + 28 * Z 1 n + 56 * Z 2 n + 10 * Z 9 n + 8 * Z 10 n + 9 * Z 11 n ∧
    Z 3 (n + 1) = Z 0 (n + 1) + 28 * Z 1 n + 56 * Z 2 n + 28 * Z 5 n ∧
    Z 4 (n + 1) = 0 ∧
    Z 5 (n + 1) = Z 7 (n + 1) + Z 1 n + 2 * Z 2 n + 28 * Z 4 n ∧
    Z 7 (n + 1) = Z 1 n + 2 * Z 2 n ∧
    Z 9 (n + 1) = Z 0 (n + 1) + 27 * Z 1 n + 54 * Z 2 n + 28 * Z 4 n ∧
    Z 10 (n + 1) = Z 0 (n + 1) + 28 * Z 1 n + 56 * Z 2 n + 28 * Z 4 n ∧
    Z 11 (n + 1) = Z 0 (n + 1) + 26 * Z 1 n + 52 * Z 2 n + 28 * Z 4 n

/-- **التكرارُ من صفوف الخطوة:** `Z₀(k+4) = 336·Z₀(k+3) + 4676·Z₀(k+2)`. -/
theorem tawlidS (Z : Nat → Nat → Nat) (h : KhatwaS Z) (k : Nat) :
    Z 0 (k + 4) = 336 * Z 0 (k + 3) + 4676 * Z 0 (k + 2) := by
  obtain ⟨a0, a1, a2, a3, a4, a5, a7, a9, a10, a11⟩ := h k
  obtain ⟨b0, b1, b2, b3, b4, b5, b7, b9, b10, b11⟩ := h (k + 1)
  obtain ⟨c0, c1, c2, c3, c4, c5, c7, c9, c10, c11⟩ := h (k + 2)
  obtain ⟨d0, d1, d2, d3, d4, d5, d7, d9, d10, d11⟩ := h (k + 3)
  simp only [Nat.add_assoc, Nat.reduceAdd] at *
  omega

theorem awailS (Z : Nat → Nat → Nat) (h : KhatwaS Z) (h0 : Z 0 0 = 0) (h1 : Z 1 0 = 2) (h2 : Z 2 0 = 2)
    (h3 : Z 3 0 = 1) (h4 : Z 4 0 = 1) (h5 : Z 5 0 = 1) (h7 : Z 7 0 = 0) (h9 : Z 9 0 = 1) (h10 : Z 10 0 = 1)
    (h11 : Z 11 0 = 1) : Z 0 1 = 168 ∧ Z 0 2 = 61096 ∧ Z 0 3 = 21443968 ∧ Z 0 4 = 7490858144 := by
  obtain ⟨a0, a1, a2, a3, a4, a5, a7, a9, a10, a11⟩ := h 0
  obtain ⟨b0, b1, b2, b3, b4, b5, b7, b9, b10, b11⟩ := h 1
  obtain ⟨c0, c1, c2, c3, c4, c5, c7, c9, c10, c11⟩ := h 2
  obtain ⟨d0, d1, d2, d3, d4, d5, d7, d9, d10, d11⟩ := h 3
  simp only [Nat.reduceAdd] at *
  refine ⟨by omega, by omega, by omega, by omega⟩

/-- **قانونُ ولادة الجملة (لكلّ k):** `S(k+4) = 336·S(k+3) + 4676·S(k+2)`. -/
theorem wilada_jumla (k : Nat) :
    Msent.lev 3 0 (k + 4) = 336 * Msent.lev 3 0 (k + 3) + 4676 * Msent.lev 3 0 (k + 2) := by
  simp only [lev_jumla]
  exact tawlidS z jumla_khatwa k

/-- **أعدادُ المالك من القانون:** 0 و168 و61096 و21443968 (`SLGE.Law.sent_levels`)، والدرجةُ الرابعة 7490858144. -/
theorem jumla_bil_qanun : Msent.lev 3 0 0 = 0 ∧ Msent.lev 3 0 1 = 168 ∧ Msent.lev 3 0 2 = 61096 ∧ Msent.lev 3 0 3 = 21443968 ∧
    Msent.lev 3 0 4 = 7490858144 := by
  simp only [lev_jumla]
  obtain ⟨w0, w1, w2, w3, w4, w5, w7, w9, w10, w11⟩ := bidaya_jumla
  exact ⟨w0, awailS z jumla_khatwa w0 w1 w2 w3 w4 w5 w7 w9 w10 w11⟩

end Dal.WiladaJumla
