import Dal.WiladaJadhr

/-!
# ولادةُ الكلمة بقانون العدّ الواحد: موقوفًا عليها وفي الوصل

قولُ المالك في الجلسة (2026-11-01، 12:40 بتوقيت عمّان): «… ولكن يجب ان نوحد الحساب من الان وصاعدا بقانون واحد جبري».

آلةُ الكلمة للمالك (`SLGE.Law.Mword` موقوفًا عليها، و`MwordWasl` في الوصل) كما هي، وعدُّها `Machine.lev` بالاستنفاد.
وحالاتُها السبعُ والتسعون تتكافأ في ثلاثة عشر صنفًا (`kalima_mutakafi_waqf`، `kalima_mutakafi_wasl`)، فيعدّ قانونُ العدّ
الواحد (`Dal.QanunAdad.qanun_adad`) الكلمةَ على صفوفها، ويخرج منه التكرار لكلّ درجة:
* موقوفًا عليها: `L(k+4) = 168·L(k+3) + 2296·L(k+2)` (`wilada_waqf`)؛
* وفي الوصل: `L(k+3) = 168·L(k+2) + 2296·L(k+1)` (`wilada_wasl`).

والمعاملان يساويان عددَي مقطعين على آلة المالك: 168 ما وزنُه صامتٌ واحد (‎CV‎ و‎CVV‎، 84 و84)، و2296 ‎CVC‎
(`kalima_maqati`)؛ وكونُ ذلك سببَهما قراءةُ البنّاء. والفرقُ بين الوقف والوصل صنفٌ واحد: الساكنان المعلّقان على الوقف (‎4‎) يُقبلان
موقوفًا عليهما وحدهما، ولا ينتقل منهما شيءٌ إلّا إلى الممتنع، فلا يُعدّ منهما إلّا الدرجةُ صفرٌ موقوفًا عليها
(`y FW 4 0 = 1` و`y FL 4 0 = 0`)، وبه يتأخّر التكرارُ في الوقف درجةً.
وأعدادُ المالك (`SLGE.Law.word_levels`، `word_levels_wasl`) تُشتقّ به أيضًا، وبعدها الدرجةُ الرابعة (`kalima_bil_qanun`)؛ وقضيّتاه في
`SLGE/Law.lean` باقيتان بحسابهما بالجدول `tab`.

**الأصناف** (‎0‎ ابتداء، ‎1‎ بعد مفتوح، ‎2‎ بعد مضمومٍ أو مكسور، ‎3‎ بعد مدّ، ‎4‎ ساكنان معلّقان على الوقف، ‎5‎ مدٌّ ثمّ ساكن،
‎6‎ مدٌّ ثمّ ألفٌ ساكنة، ‎7‎ حدٌّ بعد ‎5‎، ‎8‎ ممتنع، ‎9‎–‎11‎ بعد ساكنٍ مُغلِقٍ صنفُ حامله بمجاورٍ واحد وبلا مجاور وبمجاورَين،
‎12‎ الحالةُ ‎5‎) وصفوفُها تعيينُ البنّاء، يفحصه التكافؤُ نفسُه؛ وما لا يُبلغ من الابتداء — منه 37 و38+k و5 و8 و69 — في أصنافٍ أيضًا.

المبرهنات: 25 بالمعيار الموحَّد: لكلّ 12 (`potK`، `wazn1K`، `pK_le`، `y_khatwa`، `y_dead`، `kalima_khatwa`، `lev_waqf`، `lev_wasl`، `tawlid`،
`awail`، `wilada_waqf`، `wilada_wasl`)؛ وتعريفيّة 2 (`saffK_kabir`، `mayyitK`)؛ وعلى الشاهد 6 برهانُها decide (`sinfK`، `waznK`، `saffK_hadd`،
`bidaya_waqf`، `bidaya_wasl`، `kalima_maqati`)؛ و5 على الشاهد خارجَ حرف المعيار، معلَن (`maghluqK`: `fin_close` للمالك؛ `adadK`: من ثلاثَ عشرةَ
مساعدةً خاصّةً برهانُها decide، اثنتا عشرةَ على ثمانِ حالاتٍ وواحدةٌ على حالة — لأنّ decide على الحالات كلِّها معًا بلغ 5.2 غيغابايت —؛
`kalima_mutakafi_waqf` و`kalima_mutakafi_wasl`: بنيتان من تلك؛ `kalima_bil_qanun`: `awail`).

**وعدٌّ مباشرٌ معلَن:** `kalima_maqati` يعدّ على آلة `Mword` خانةً وخانتين بـ decide لا بالأصناف، شاهدًا لمعنى المعاملين؛ و84 الأولى يثبت المالك
نظيرَها على 117 رمزًا (`SLGE.Law.cell_count`)، و168 على آلة المقطع (`SLGE.Law.sl1`)؛ وقسمةُ 4648 (`sl2`) إلى 2296 ‎CVC‎ و2352 ‎CVVC‎ عدُّ أداةٍ
(مرآةُ بايثون في مسوّدة الجلسة) بلا وسم.
-/

namespace Dal.WiladaKalima
open SLGE SLGE.Law Dal.QanunAdad
open Dal.WiladaJadhr (sinfT)

/-- صنفُ حالة الكلمة. -/
def sK (q : Nat) : Nat :=
  if q = 0 ∨ q = 37 then 0 else if q = 1 then 1 else if q = 2 ∨ q = 3 then 2 else if q = 4 then 3
  else if q = 5 then 12 else if q = 8 then 6 else if q ≤ 34 then 5 else if q ≤ 36 then 4
  else if q = 40 then 8 else if q ≤ 66 then 7
  else if q ≤ 95 then (if sinfT.getD (q - 67) 0 = 0 then 10 else if sinfT.getD (q - 67) 0 = 1 then 9 else 11)
  else 8

/-- **صفوفُ الأصناف** (الوزن، الصنفُ الهدف، العدد) على الخانات الـ116. -/
def saffK : Nat → List (Nat × Nat × Nat)
  | 0 => [(1, 1, 28), (1, 2, 56), (1, 8, 32)]
  | 1 => [(0, 3, 1), (1, 1, 28), (1, 2, 56), (1, 8, 3), (1, 9, 10), (1, 10, 9), (1, 11, 9)]
  | 2 => [(0, 3, 1), (1, 1, 28), (1, 2, 56), (1, 8, 4), (1, 9, 10), (1, 10, 8), (1, 11, 9)]
  | 3 => [(1, 1, 28), (1, 2, 56), (1, 5, 28), (1, 8, 4)]
  | 4 => [(1, 8, 116)]
  | 5 => [(1, 1, 1), (1, 2, 2), (1, 4, 28), (1, 8, 85)]
  | 6 => [(1, 4, 28), (1, 8, 88)]
  | 7 => [(1, 1, 1), (1, 2, 2), (1, 8, 113)]
  | 8 => [(1, 8, 116)]
  | 9 => [(1, 1, 27), (1, 2, 54), (1, 4, 28), (1, 8, 7)]
  | 10 => [(1, 1, 28), (1, 2, 56), (1, 4, 28), (1, 8, 4)]
  | 11 => [(1, 1, 26), (1, 2, 52), (1, 4, 28), (1, 8, 10)]
  | 12 => [(1, 8, 116)]
  | _ => []

/-- القبولُ موقوفًا عليها: كلُّ صنفٍ إلّا الابتداءَ وحدَّ ما بعد ‎5‎ والممتنع. -/
def FW (i : Nat) : Bool := !(i == 0 || i == 7 || i == 8)
/-- القبولُ في الوصل: ويسقط الساكنان المعلّقان على الوقف (‎4‎). -/
def FL (i : Nat) : Bool := !(i == 0 || i == 4 || i == 7 || i == 8)

def QK (F : Nat → Bool) : Asnaf := ⟨13, saffK, F⟩

theorem maghluqK : ∀ q < 97, ∀ b < 116, δ q b < 97 := fun q hq b hb => fin_close q hq b (by omega)
theorem sinfK : ∀ q < 97, sK q < 13 := by decide +kernel
theorem waznK : ∀ q < 97, ∀ b < 116, ω q b ≤ 1 := by decide +kernel
theorem saffK_hadd : ∀ q < 97, ∀ e ∈ saffK (sK q), e.1 ≤ 1 ∧ e.2.1 < 13 := by decide +kernel
/-- ما يُفحص لكلّ حالة: عددُ انتقالاتها بكلّ وزنٍ إلى كلّ صنفٍ هو ما في صفّ صنفها. -/
abbrev ShartK (q : Nat) : Prop := ∀ u ≤ 1, ∀ j < 13,
    ((List.range 116).filter fun b => ω q b == u && sK (δ q b) == j).length =
      (((saffK (sK q)).filter fun e => e.1 == u && e.2.1 == j).map fun e => e.2.2).sum

private theorem ShartK_0 : ∀ r < 8, ShartK (r + 0) := by decide +kernel
private theorem ShartK_1 : ∀ r < 8, ShartK (r + 8) := by decide +kernel
private theorem ShartK_2 : ∀ r < 8, ShartK (r + 16) := by decide +kernel
private theorem ShartK_3 : ∀ r < 8, ShartK (r + 24) := by decide +kernel
private theorem ShartK_4 : ∀ r < 8, ShartK (r + 32) := by decide +kernel
private theorem ShartK_5 : ∀ r < 8, ShartK (r + 40) := by decide +kernel
private theorem ShartK_6 : ∀ r < 8, ShartK (r + 48) := by decide +kernel
private theorem ShartK_7 : ∀ r < 8, ShartK (r + 56) := by decide +kernel
private theorem ShartK_8 : ∀ r < 8, ShartK (r + 64) := by decide +kernel
private theorem ShartK_9 : ∀ r < 8, ShartK (r + 72) := by decide +kernel
private theorem ShartK_10 : ∀ r < 8, ShartK (r + 80) := by decide +kernel
private theorem ShartK_11 : ∀ r < 8, ShartK (r + 88) := by decide +kernel
private theorem ShartK_12 : ∀ r < 1, ShartK (r + 96) := by decide +kernel

theorem adadK : ∀ q < 97, ShartK q := by
  intro q hq
  have h : q < 8 ∨ (8 ≤ q ∧ q < 16) ∨ (16 ≤ q ∧ q < 24) ∨ (24 ≤ q ∧ q < 32) ∨ (32 ≤ q ∧ q < 40) ∨ (40 ≤ q ∧ q < 48) ∨ (48 ≤ q ∧ q < 56) ∨ (56 ≤ q ∧ q < 64) ∨ (64 ≤ q ∧ q < 72) ∨ (72 ≤ q ∧ q < 80) ∨ (80 ≤ q ∧ q < 88) ∨ (88 ≤ q ∧ q < 96) ∨ (96 ≤ q ∧ q < 97) := by omega
  rcases h with h | h | h | h | h | h | h | h | h | h | h | h | h
  · have := ShartK_0 q h; rwa [Nat.add_zero] at this
  · have := ShartK_1 (q - 8) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_2 (q - 16) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_3 (q - 24) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_4 (q - 32) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_5 (q - 40) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_6 (q - 48) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_7 (q - 56) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_8 (q - 64) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_9 (q - 72) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_10 (q - 80) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_11 (q - 88) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this
  · have := ShartK_12 (q - 96) (by omega); rwa [Nat.sub_add_cancel (by omega)] at this

/-- **التكافؤ (الوقف):** حالاتُ الكلمة موقوفًا عليها تتكافأ في ثلاثة عشر صنفًا. -/
theorem kalima_mutakafi_waqf : Mutakafi Mword (QK FW) 1 sK (fun q => q < 97) where
  maghluq := fun q hq b hb => maghluqK q hq b hb
  sinf := sinfK
  wazn := fun q hq b hb => waznK q hq b hb
  saff := saffK_hadd
  qubul := by show ∀ q < 97, Fwaqf q = FW (sK q); decide +kernel
  adad := adadK

/-- **التكافؤ (الوصل).** -/
theorem kalima_mutakafi_wasl : Mutakafi MwordWasl (QK FL) 1 sK (fun q => q < 97) where
  maghluq := fun q hq b hb => maghluqK q hq b hb
  sinf := sinfK
  wazn := fun q hq b hb => waznK q hq b hb
  saff := saffK_hadd
  qubul := by show ∀ q < 97, Fwasl q = FL (sK q); decide +kernel
  adad := adadK

/-! ## العدُّ على الأصناف -/

def pK (i : Nat) : Nat := if i = 1 ∨ i = 2 then 1 else 0

theorem saffK_kabir (i : Nat) (h : 13 ≤ i) : saffK i = [] := by
  match i, h with
  | n + 13, _ => rfl

theorem mayyitK (F : Nat → Bool) (hF : F 8 = false) :
    ∀ i, (i == 8) = true → (QK F).F i = false ∧ ∀ e ∈ (QK F).saff i, (e.2.1 == 8) = true := by
  intro i hi; simp at hi; subst hi
  exact ⟨hF, by simp [QK, saffK]⟩

theorem potK (F : Nat → Bool) : ∀ i, (i == 8) = false → ∀ e ∈ (QK F).saff i, (e.2.1 == 8) = false →
    pK e.2.1 + 1 ≤ pK i + 2 * e.1 := by
  intro i hi e he hj
  have : i < 13 ∨ 13 ≤ i := by omega
  rcases this with h | h
  · have k : ∀ i < 13, (i == 8) = false → ∀ e ∈ saffK i, (e.2.1 == 8) = false → pK e.2.1 + 1 ≤ pK i + 2 * e.1 := by
      decide +kernel
    exact k i h hi e he hj
  · simp [QK, saffK_kabir i h] at he

theorem wazn1K (F : Nat → Bool) : ∀ i, ∀ e ∈ (QK F).saff i, e.1 ≤ 1 := by
  intro i e he
  have : i < 13 ∨ 13 ≤ i := by omega
  rcases this with h | h
  · have k : ∀ i < 13, ∀ e ∈ saffK i, e.1 ≤ 1 := by decide +kernel
    exact k i h e he
  · simp [QK, saffK_kabir i h] at he

/-- ما يُكمل الكلمةَ بوزن ‎`n`‎ من الصنف ‎`i`‎ (بطولٍ كافٍ ‎`2n + 1`‎). -/
def y (F : Nat → Bool) (i n : Nat) : Nat := (QK F).C (2 * n + 1) n i

theorem pK_le : ∀ i, pK i ≤ 1 := by intro i; unfold pK; split <;> omega

/-- **الخطوة:** الصنفُ بوزن ‎`n + 1`‎ مجموعُ صفّه: ما وزنُه صفرٌ في الدرجة نفسِها، وما وزنُه واحدٌ في ‎`n`‎. -/
theorem y_khatwa (F : Nat → Bool) (hF : F 8 = false) (i n : Nat) : y F i (n + 1) = (QK F).base (n + 1) i +
    (((QK F).saff i).map fun e => e.2.2 * (if e.1 = 0 then y F e.2.1 (n + 1) else y F e.2.1 n)).sum :=
  (QK F).C_khatwa1 2 1 pK (· == 8) (mayyitK F hF) (potK F) (by decide +kernel) pK_le (wazn1K F) n i

theorem y_dead (F : Nat → Bool) (hF : F 8 = false) (n : Nat) : y F 8 n = 0 :=
  (QK F).mayyit_sifr (· == 8) (mayyitK F hF) _ _ 8 rfl

/-- **صفوفُ الخطوة** لكلّ قبولٍ لا يقبل الممتنع. -/
theorem kalima_khatwa (F : Nat → Bool) (hF : F 8 = false) (n : Nat) :
    y F 0 (n + 1) = 28 * y F 1 n + 56 * y F 2 n ∧
    y F 1 (n + 1) = y F 3 (n + 1) + 28 * y F 1 n + 56 * y F 2 n + 10 * y F 9 n + 9 * y F 10 n + 9 * y F 11 n ∧
    y F 2 (n + 1) = y F 3 (n + 1) + 28 * y F 1 n + 56 * y F 2 n + 10 * y F 9 n + 8 * y F 10 n + 9 * y F 11 n ∧
    y F 3 (n + 1) = 28 * y F 1 n + 56 * y F 2 n + 28 * y F 5 n ∧
    y F 4 (n + 1) = 0 ∧
    y F 5 (n + 1) = y F 1 n + 2 * y F 2 n + 28 * y F 4 n ∧
    y F 9 (n + 1) = 27 * y F 1 n + 54 * y F 2 n + 28 * y F 4 n ∧
    y F 10 (n + 1) = 28 * y F 1 n + 56 * y F 2 n + 28 * y F 4 n ∧
    y F 11 (n + 1) = 26 * y F 1 n + 52 * y F 2 n + 28 * y F 4 n := by
  have d := y_dead F hF
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
  · rw [y_khatwa F hF]
    simp [QK, saffK, Asnaf.base, d]
    try omega

theorem bidaya_waqf : y FW 0 0 = 0 ∧ y FW 1 0 = 2 ∧ y FW 2 0 = 2 ∧ y FW 3 0 = 1 ∧ y FW 4 0 = 1 ∧ y FW 5 0 = 1 ∧
    y FW 9 0 = 1 ∧ y FW 10 0 = 1 ∧ y FW 11 0 = 1 := by decide +kernel

theorem bidaya_wasl : y FL 0 0 = 0 ∧ y FL 1 0 = 2 ∧ y FL 2 0 = 2 ∧ y FL 3 0 = 1 ∧ y FL 4 0 = 0 ∧ y FL 5 0 = 1 ∧
    y FL 9 0 = 1 ∧ y FL 10 0 = 1 ∧ y FL 11 0 = 1 := by decide +kernel

/-- **العدُّ بالأصناف (الوقف):** عددُ الكلمات بوزن ‎`n`‎ عند المالك هو العدُّ من صنف الابتداء. -/
theorem lev_waqf (n : Nat) : Mword.lev 3 0 n = y FW 0 n := by
  unfold Machine.lev y
  rw [qanun_adad Mword (QK FW) 1 sK _ kalima_mutakafi_waqf (3 * n) n 0 (by decide +kernel)]
  exact (QK FW).C_thabit2 2 pK (· == 8) (mayyitK FW rfl) (potK FW) n 0 _ _ (by have : pK 0 = 0 := rfl; omega)
    (by have : pK 0 = 0 := rfl; omega)

theorem lev_wasl (n : Nat) : MwordWasl.lev 3 0 n = y FL 0 n := by
  unfold Machine.lev y
  rw [qanun_adad MwordWasl (QK FL) 1 sK _ kalima_mutakafi_wasl (3 * n) n 0 (by decide +kernel)]
  exact (QK FL).C_thabit2 2 pK (· == 8) (mayyitK FL rfl) (potK FL) n 0 _ _ (by have : pK 0 = 0 := rfl; omega)
    (by have : pK 0 = 0 := rfl; omega)

/-- صفوفُ الخطوة على متتاليةٍ مجرّدة: ما يلزم التكرارَ منها. -/
def Khatwa (Y : Nat → Nat → Nat) : Prop := ∀ n,
    Y 0 (n + 1) = 28 * Y 1 n + 56 * Y 2 n ∧
    Y 1 (n + 1) = Y 3 (n + 1) + 28 * Y 1 n + 56 * Y 2 n + 10 * Y 9 n + 9 * Y 10 n + 9 * Y 11 n ∧
    Y 2 (n + 1) = Y 3 (n + 1) + 28 * Y 1 n + 56 * Y 2 n + 10 * Y 9 n + 8 * Y 10 n + 9 * Y 11 n ∧
    Y 3 (n + 1) = 28 * Y 1 n + 56 * Y 2 n + 28 * Y 5 n ∧
    Y 4 (n + 1) = 0 ∧
    Y 5 (n + 1) = Y 1 n + 2 * Y 2 n + 28 * Y 4 n ∧
    Y 9 (n + 1) = 27 * Y 1 n + 54 * Y 2 n + 28 * Y 4 n ∧
    Y 10 (n + 1) = 28 * Y 1 n + 56 * Y 2 n + 28 * Y 4 n ∧
    Y 11 (n + 1) = 26 * Y 1 n + 52 * Y 2 n + 28 * Y 4 n

/-- **التكرارُ من صفوف الخطوة:** `Y₀(k+4) = 168·Y₀(k+3) + 2296·Y₀(k+2)`، ومن الدرجة الأولى إن لم يُقبل الصنفُ ‎4‎. -/
theorem tawlid (Y : Nat → Nat → Nat) (h : Khatwa Y) (k : Nat) :
    Y 0 (k + 4) = 168 * Y 0 (k + 3) + 2296 * Y 0 (k + 2) ∧
    (Y 4 k = 0 → Y 0 (k + 3) = 168 * Y 0 (k + 2) + 2296 * Y 0 (k + 1)) := by
  obtain ⟨a0, a1, a2, a3, a4, a5, a9, a10, a11⟩ := h k
  obtain ⟨b0, b1, b2, b3, b4, b5, b9, b10, b11⟩ := h (k + 1)
  obtain ⟨c0, c1, c2, c3, c4, c5, c9, c10, c11⟩ := h (k + 2)
  obtain ⟨d0, d1, d2, d3, d4, d5, d9, d10, d11⟩ := h (k + 3)
  simp only [Nat.add_assoc, Nat.reduceAdd] at *
  exact ⟨by omega, fun z => by omega⟩

/-- **الأوائلُ من صفوف الخطوة:** على ‎`f = Y₄(0)`‎ (قبولُ الساكنين المعلّقين). -/
theorem awail (Y : Nat → Nat → Nat) (h : Khatwa Y) (h0 : Y 0 0 = 0) (h1 : Y 1 0 = 2) (h2 : Y 2 0 = 2)
    (h3 : Y 3 0 = 1) (h5 : Y 5 0 = 1) (h9 : Y 9 0 = 1) (h10 : Y 10 0 = 1) (h11 : Y 11 0 = 1) :
    Y 0 1 = 168 ∧ Y 0 2 = 32872 ∧ Y 0 3 = 5908224 + 130144 * Y 4 0 ∧
    Y 0 4 = 1068055744 + 21864192 * Y 4 0 := by
  obtain ⟨a0, a1, a2, a3, a4, a5, a9, a10, a11⟩ := h 0
  obtain ⟨b0, b1, b2, b3, b4, b5, b9, b10, b11⟩ := h 1
  obtain ⟨c0, c1, c2, c3, c4, c5, c9, c10, c11⟩ := h 2
  obtain ⟨d0, d1, d2, d3, d4, d5, d9, d10, d11⟩ := h 3
  simp only [Nat.reduceAdd] at *
  refine ⟨by omega, by omega, by omega, by omega⟩

/-- **قانونُ الولادة موقوفًا عليها (لكلّ k):** `L(k+4) = 168·L(k+3) + 2296·L(k+2)`. -/
theorem wilada_waqf (k : Nat) : Mword.lev 3 0 (k + 4) = 168 * Mword.lev 3 0 (k + 3) + 2296 * Mword.lev 3 0 (k + 2) := by
  simp only [lev_waqf]
  exact (tawlid (y FW) (kalima_khatwa FW rfl) k).1

/-- **قانونُ الولادة في الوصل (لكلّ k):** `L(k+3) = 168·L(k+2) + 2296·L(k+1)`. -/
theorem wilada_wasl (k : Nat) :
    MwordWasl.lev 3 0 (k + 3) = 168 * MwordWasl.lev 3 0 (k + 2) + 2296 * MwordWasl.lev 3 0 (k + 1) := by
  simp only [lev_wasl]
  refine (tawlid (y FL) (kalima_khatwa FL rfl) k).2 ?_
  cases k with
  | zero => exact bidaya_wasl.2.2.2.2.1
  | succ m => exact (kalima_khatwa FL rfl m).2.2.2.2.1

/-- **أعدادُ المالك من القانون:** 0 و168 و32872 و6038368 موقوفًا عليها، و5908224 في الوصل للدرجة الثالثة
(`SLGE.Law.word_levels`، `word_levels_wasl`)، والدرجةُ الرابعة 1089919936 و1068055744. -/
theorem kalima_bil_qanun : Mword.lev 3 0 0 = 0 ∧ Mword.lev 3 0 1 = 168 ∧ Mword.lev 3 0 2 = 32872 ∧ Mword.lev 3 0 3 = 6038368 ∧
    Mword.lev 3 0 4 = 1089919936 ∧ MwordWasl.lev 3 0 1 = 168 ∧ MwordWasl.lev 3 0 2 = 32872 ∧
    MwordWasl.lev 3 0 3 = 5908224 ∧ MwordWasl.lev 3 0 4 = 1068055744 ∧ MwordWasl.lev 3 0 0 = 0 := by
  simp only [lev_waqf, lev_wasl]
  obtain ⟨w0, w1, w2, w3, w4, w5, w9, w10, w11⟩ := bidaya_waqf
  obtain ⟨l0, l1, l2, l3, l4, l5, l9, l10, l11⟩ := bidaya_wasl
  have aw := awail (y FW) (kalima_khatwa FW rfl) w0 w1 w2 w3 w5 w9 w10 w11
  have al := awail (y FL) (kalima_khatwa FL rfl) l0 l1 l2 l3 l5 l9 l10 l11
  rw [w4] at aw
  rw [l4] at al
  exact ⟨w0, aw.1, aw.2.1, aw.2.2.1, aw.2.2.2, al.1, al.2.1, al.2.2.1, al.2.2.2, l0⟩

/-- **المقاطع:** خانةٌ واحدةٌ مقبولةٌ وقفًا 84 (‎CV‎)، وخانتان بصامتٍ واحد 84 (‎CV‎ ثمّ مدّ: ‎CVV‎)، وخانتان بصامتين تنتهيان بعد ساكنٍ
مُغلِق 2296 (‎CVC‎) — عدٌّ مباشرٌ على آلة المالك. -/
theorem kalima_maqati :
    ((List.range 116).filter fun a => Fwaqf (run 0 [a])).length = 84 ∧
    (((List.range 116).flatMap fun a => (List.range 116).map fun b => [a, b]).filter
      fun l => Fwaqf (run 0 l) && wt 0 l == 1).length = 84 ∧
    (((List.range 116).flatMap fun a => (List.range 116).map fun b => [a, b]).filter
      fun l => wt 0 l == 2 && 67 ≤ run 0 l && run 0 l < 96).length = 2296 := by
  decide +kernel

end Dal.WiladaKalima
