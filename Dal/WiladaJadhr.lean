import Dal.QanunAdad
import SLGE.Root

/-!
# ولادةُ الجذر بقانون العدّ الواحد، والحدُّ الأدنى المكتمل

قولُ المالك في الجلسة (2026-11-01، لفظُه ووقتُه 12:19 من ملخّص الجلسة بعد ضغطها):
«نحتاج برهان ولادة الجذر جبريا وفق استقراء قانون الاستنفاد انت لم تأخذ في الاعتبار كيف بنينا البرهان من المخارج ورخصنا الاحرف داخل المخرج وبنينا الشيفرة ومن يفسر كل شيء اذا وضع قانون التجاور وفق قانون الابتداء وقانون الوصل وقانون الفصل وقانون الوقف وبالحد الأدنى المكتمل …»
ثمّ (12:40): «… ولكن يجب ان نوحد الحساب من الان وصاعدا بقانون واحد جبري».

**الولادة.** آلةُ الجذر `Mroot` للمالك (`SLGE/Root.lean`) كما هي، وعدُّها `Mroot.lev` بالاستنفاد (`SLGE/Count.lean`).
والأصنافُ من جدول المخارج ووسيط حروف العلّة (`weak`، `SLGE/Law.lean`) واستبعاد الألف: صنفُ الحامل عددُ ما يجاوره في مخرجه (`sinf`)، فالحوامل غيرُ الألف تسعةٌ بلا مجاور
(ق ك ض ل ن ر ف ي و)، وعشرةٌ بمجاورٍ واحد (ء ه، ع ح، غ خ، ج ش، ب م)، وتسعةٌ بمجاورَين (ط د ت، ز س ص، ظ ذ ث) — `asnaf`.
وحالاتُ الآلة بعد الحامل تتكافأ بصنفه (`jadhr_mutakafi`)، فقانونُ العدّ الواحد (`Dal.QanunAdad.qanun_adad`) يعدّ
الجذورَ على خمسة أصناف، ومنه التكرار لكلّ طول (`wilada`):
`R(k+4) = 25·R(k+3) + 54·R(k+2) + 18·R(k+1)`، وأوّلُه 28 و756 و20430 (`wilada_awwal`)،
وعددا المالك للرباعيّ والخماسيّ (`SLGE.Law.root4`، `root5`) يُشتقّان به أيضًا (`jadhr_bil_qanun`)، وقضيّتاه في `SLGE/Root.lean`
باقيتان بحسابهما بالجدول `tab`.

**الحدُّ الأدنى المكتمل** (§٤). الصورتان من رأس ملفّ المالك `SLGE/Root.lean` (س7–8: «‎فَعْل‎ للثاني والثالث، و‎يَفْعَل‎ للأوّل
والثاني»)، ومبرهنتُه `tajawur_root` تثبت اتّجاهًا: التجاورُ يمتنع فيهما. و`kamil3` يُتمّه بالاتّجاهين: قانونُ الجذر الثلاثيّ هو قانونُ
الوصل نفسُه على الصورتين معًا؛ ولا تكفي إحداهما (`la_yakfi_wahid`).

**التعيين** (البنّاء): الأصنافُ الخمسةُ وصفوفُها، وتسميةُ `kamil3` بقول المالك «بالحد الأدنى المكتمل» — قراءتي تنتظر إمضاءك.

المبرهنات: 23 بالمعيار الموحَّد: لكلّ 10 (`potJ`، `wazn1`، `lev_jadhr`، `x_dead`، `x_khatwa`، `jadhr_khatwa`، `wilada`، `tawlid`، `d96`،
`kamil3` — وهذه على المجال المنتهي ‎a b c < 29‎ ببرهانٍ بالحالات لا بـ decide)؛ وتعريفيّة 3 (`x_bidaya`، `r30`، `mayyitJ`)؛ وعلى الشاهد 7 برهانُها
decide (`sinfT_sinf`، `asnaf`، `jadhr_shahid`، `wasl_khatwa`، `r1`، `r2`، `la_yakfi_wahid`)؛ و3 على الشاهد خارجَ حرف المعيار، معلَن
(`jadhr_mutakafi`: حقولٌ بـ decide ومعها `root_close` للمالك؛ `wilada_awwal`: omega على مبرهنات؛ `jadhr_bil_qanun`: `tawlid` على `wilada`).
-/

namespace Dal.WiladaJadhr
open SLGE SLGE.Law Dal.QanunAdad

/-! ## ١. الأصنافُ من جدول المخارج -/

/-- صنفُ الحامل: عددُ الحوامل غيرِ الألف التي تجاوره في مخرجه (فيمتنع أن تليه). -/
def sinf (c : Nat) : Nat := ((List.range 29).filter fun b => b != 2 && conflict c b).length

/-- جدولُ الصنف للحوامل التسعة والعشرين (يساوي `sinf`: `sinfT_sinf`). -/
def sinfT : List Nat := [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0]

theorem sinfT_sinf : ∀ c < 29, sinfT.getD c 0 = sinf c := by decide +kernel

/-- **الأصناف:** تسعةُ حوامل بلا مجاور، وعشرةٌ بمجاورٍ واحد، وتسعةٌ بمجاورَين؛ والممنوعُ مرتَّبًا 28 زوجًا. -/
theorem asnaf : ((List.range 29).filter fun c => c != 2 && sinf c == 0).length = 9 ∧
    ((List.range 29).filter fun c => c != 2 && sinf c == 1).length = 10 ∧
    ((List.range 29).filter fun c => c != 2 && sinf c == 2).length = 9 ∧
    ((List.range 29).map fun c => if c = 2 then 0 else sinf c).sum = 28 := by decide +kernel

/-- صنفُ حالة الآلة: الابتداء 0، وبعد الحامل ‎`c`‎ ‎`1 + sinf c`‎، والممتنع 4. -/
def sJ (q : Nat) : Nat := if q = 0 then 0 else if q ≤ 29 then 1 + sinfT.getD (q - 1) 0 else 4

/-- **صفوفُ الأصناف** (الوزن، الصنفُ الهدف، العدد): بعد الحامل يسقط من صنفه بعددِ ما يجاوره، والألفُ إلى الممتنع. -/
def saffJ : Nat → List (Nat × Nat × Nat)
  | 0 => [(1, 1, 9), (1, 2, 10), (1, 3, 9), (1, 4, 1)]
  | 1 => [(1, 1, 9), (1, 2, 10), (1, 3, 9), (1, 4, 1)]
  | 2 => [(1, 1, 9), (1, 2, 9), (1, 3, 9), (1, 4, 2)]
  | 3 => [(1, 1, 9), (1, 2, 10), (1, 3, 7), (1, 4, 3)]
  | 4 => [(1, 4, 29)]
  | _ => []

def QJ : Asnaf := ⟨5, saffJ, fun i => i == 1 || i == 2 || i == 3⟩

/-- **التكافؤ:** حالاتُ آلة الجذر تتكافأ بأصنافها. -/
theorem jadhr_mutakafi : Mutakafi Mroot QJ 1 sJ (fun q => q < 31) where
  maghluq := fun q hq b hb => root_close q hq b hb
  sinf := by show ∀ q < 31, sJ q < 5; decide +kernel
  wazn := fun _ _ _ _ => Nat.le_refl 1
  saff := by show ∀ q < 31, ∀ e ∈ saffJ (sJ q), e.1 ≤ 1 ∧ e.2.1 < 5; decide +kernel
  qubul := by show ∀ q < 31, decide (1 ≤ q ∧ q ≤ 29) = (sJ q == 1 || sJ q == 2 || sJ q == 3); decide +kernel
  adad := by
    show ∀ q < 31, ∀ u ≤ 1, ∀ j < 5, ((List.range 29).filter fun b => (1 : Nat) == u && sJ (δr q b) == j).length =
      (((saffJ (sJ q)).filter fun e => e.1 == u && e.2.1 == j).map fun e => e.2.2).sum
    decide +kernel

/-! ## ٢. العدُّ على الأصناف -/

/-- ما يُكمل الجذرَ بطول ‎`n`‎ من الصنف ‎`i`‎. -/
def x (i n : Nat) : Nat := QJ.C n n i

theorem mayyitJ : ∀ i, (i == 4) = true → QJ.F i = false ∧ ∀ e ∈ QJ.saff i, (e.2.1 == 4) = true := by
  intro i hi; simp at hi; subst hi; exact ⟨rfl, by simp [QJ, saffJ]⟩

theorem potJ : ∀ i, (i == 4) = false → ∀ e ∈ QJ.saff i, (e.2.1 == 4) = false →
    (fun _ => 0) e.2.1 + 1 ≤ (fun _ => 0) i + 1 * e.1 := by
  intro i _ e he _
  have : i < 5 ∨ 5 ≤ i := by omega
  rcases this with h | h
  · have : ∀ i < 5, ∀ e ∈ saffJ i, e.1 = 1 := by decide +kernel
    simp only [this i h e he]; omega
  · have : saffJ i = [] := by
      match i, h with
      | n + 5, _ => rfl
    simp [QJ, this] at he

theorem wazn1 : ∀ i, ∀ e ∈ QJ.saff i, e.1 ≤ 1 := by
  intro i e he
  have : i < 5 ∨ 5 ≤ i := by omega
  rcases this with h | h
  · have : ∀ i < 5, ∀ e ∈ saffJ i, e.1 ≤ 1 := by decide +kernel
    exact this i h e he
  · have : saffJ i = [] := by
      match i, h with
      | n + 5, _ => rfl
    simp [QJ, this] at he

/-- **العدُّ بالأصناف:** عددُ الجذور بطول ‎`n`‎ عند المالك هو العدُّ من صنف الابتداء. -/
theorem lev_jadhr (n : Nat) : Mroot.lev 3 0 n = x 0 n := by
  unfold Machine.lev x
  rw [qanun_adad Mroot QJ 1 sJ _ jadhr_mutakafi (3 * n) n 0 (by decide +kernel)]
  exact QJ.C_thabit2 1 (fun _ => 0) (· == 4) mayyitJ potJ n 0 _ _ (by omega) (by omega)

theorem x_dead (n : Nat) : x 4 n = 0 := QJ.mayyit_sifr (· == 4) mayyitJ n n 4 rfl

/-- **الخطوة:** كلُّ صنفٍ بطول ‎`n + 1`‎ مجموعُ صفّه على الأصناف بطول ‎`n`‎. -/
theorem x_khatwa (i n : Nat) : x i (n + 1) = QJ.base (n + 1) i +
    ((QJ.saff i).map fun e => e.2.2 * (if e.1 = 0 then x e.2.1 (n + 1) else x e.2.1 n)).sum := by
  have := QJ.C_khatwa1 1 0 (fun _ => 0) (· == 4) mayyitJ potJ (Nat.le_refl 1) (fun _ => Nat.le_refl 0) wazn1 n i
  simp only [Nat.one_mul, Nat.add_zero] at this
  exact this

theorem x_bidaya (i : Nat) : x i 0 = QJ.base 0 i := rfl

theorem jadhr_khatwa (n : Nat) :
    x 0 (n + 1) = 9 * x 1 n + 10 * x 2 n + 9 * x 3 n ∧
    x 1 (n + 1) = 9 * x 1 n + 10 * x 2 n + 9 * x 3 n ∧
    x 2 (n + 1) = 9 * x 1 n + 9 * x 2 n + 9 * x 3 n ∧
    x 3 (n + 1) = 9 * x 1 n + 10 * x 2 n + 7 * x 3 n := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · rw [x_khatwa]
    simp [QJ, saffJ, Asnaf.base, x_dead]
    omega

/-! ## ٣. قانونُ الولادة -/

/-- **قانونُ الولادة (لكلّ k):** `R(k+4) = 25·R(k+3) + 54·R(k+2) + 18·R(k+1)`، ومعاملاتُه من صفوف الأصناف وحدها. -/
theorem wilada (k : Nat) : Mroot.lev 3 0 (k + 4) = 25 * Mroot.lev 3 0 (k + 3) + 54 * Mroot.lev 3 0 (k + 2) +
    18 * Mroot.lev 3 0 (k + 1) := by
  simp only [lev_jadhr]
  obtain ⟨a0, a1, a2, a3⟩ := jadhr_khatwa k
  obtain ⟨b0, b1, b2, b3⟩ := jadhr_khatwa (k + 1)
  obtain ⟨c0, c1, c2, c3⟩ := jadhr_khatwa (k + 2)
  obtain ⟨d0, d1, d2, d3⟩ := jadhr_khatwa (k + 3)
  simp only [Nat.add_assoc, Nat.reduceAdd] at b0 b1 b2 b3 c0 c1 c2 c3 d0 d1 d2 d3
  omega

theorem jadhr_shahid : x 1 0 = 1 ∧ x 2 0 = 1 ∧ x 3 0 = 1 := by decide +kernel

/-- **أوّلُ الولادة:** 28 و756 و20430، و`R(3) = 25·R(2) + 54·R(1) + 18`. -/
theorem wilada_awwal : Mroot.lev 3 0 1 = 28 ∧ Mroot.lev 3 0 2 = 756 ∧ Mroot.lev 3 0 3 = 20430 ∧
    Mroot.lev 3 0 3 = 25 * Mroot.lev 3 0 2 + 54 * Mroot.lev 3 0 1 + 18 := by
  simp only [lev_jadhr]
  obtain ⟨z1, z2, z3⟩ := jadhr_shahid
  obtain ⟨a0, a1, a2, a3⟩ := jadhr_khatwa 0
  obtain ⟨b0, b1, b2, b3⟩ := jadhr_khatwa 1
  obtain ⟨c0, c1, c2, c3⟩ := jadhr_khatwa 2
  simp only [Nat.reduceAdd] at a0 a1 a2 a3 b0 b1 b2 b3 c0 c1 c2 c3
  refine ⟨by omega, by omega, by omega, by omega⟩

/-- **التكرارُ يولّد ما بعده:** كلُّ متتاليةٍ على التكرار وأوّلُها 28 و756 و20430 بعدها 552078 و14918778 و403149402. -/
theorem tawlid (R : Nat → Nat) (h : ∀ k, R (k + 4) = 25 * R (k + 3) + 54 * R (k + 2) + 18 * R (k + 1))
    (h1 : R 1 = 28) (h2 : R 2 = 756) (h3 : R 3 = 20430) :
    R 4 = 552078 ∧ R 5 = 14918778 ∧ R 6 = 403149402 := by
  have w0 := h 0
  have w1 := h 1
  have w2 := h 2
  simp only [Nat.reduceAdd] at w0 w1 w2
  refine ⟨by omega, by omega, by omega⟩

/-- **عددا المالك من القانون:** الرباعيُّ 552078 والخماسيُّ 14918778 (`SLGE.Law.root4`، `root5`) نتيجةُ الولادة، وبعدهما
السداسيُّ 403149402. -/
theorem jadhr_bil_qanun : Mroot.lev 3 0 4 = 552078 ∧ Mroot.lev 3 0 5 = 14918778 ∧ Mroot.lev 3 0 6 = 403149402 :=
  tawlid (fun k => Mroot.lev 3 0 k) wilada wilada_awwal.1 wilada_awwal.2.1 wilada_awwal.2.2.1

/-! ## ٤. الحدُّ الأدنى المكتمل: قانونُ الجذر الثلاثيّ هو قانونُ الوصل على صورتين -/

/-- «يَفْعَلُ»: الياءُ مفتوحةً، ثمّ الأوّلُ ساكنًا، ثمّ الثاني مفتوحًا، ثمّ الثالثُ مضمومًا. -/
def yafal (a b c : Nat) : List Nat := [4 * 11 + 0, 4 * a + 3, 4 * b + 0, 4 * c + 1]
/-- «فَعْلُ»: الأوّلُ مفتوحًا، ثمّ الثاني ساكنًا، ثمّ الثالثُ مضمومًا. -/
def fal (a b c : Nat) : List Nat := [4 * a + 0, 4 * b + 3, 4 * c + 1]

theorem wasl_khatwa :
    δ 0 44 = 1 ∧
    (∀ a < 29, δ 1 (4 * a + 3) = if a = 2 then 4 else 67 + a) ∧
    (∀ a < 29, ∀ b < 29, δ (if a = 2 then 4 else 67 + a) (4 * b + 0) =
      if b = 2 ∨ (a ≠ 2 ∧ conflict a b = true) then 96 else 1) ∧
    (∀ c < 29, δ 1 (4 * c + 1) = if c = 2 then 96 else 2) ∧
    (∀ a < 29, δ 0 (4 * a + 0) = if a = 2 then 96 else 1) ∧
    (∀ b < 29, ∀ c < 29, δ (if b = 2 then 4 else 67 + b) (4 * c + 1) =
      if c = 2 ∨ (b ≠ 2 ∧ conflict b c = true) then 96 else 2) := by
  refine ⟨by decide +kernel, by decide +kernel, by decide +kernel, by decide +kernel, by decide +kernel, by decide +kernel⟩

theorem r1 : ∀ a < 29, δr 0 a = if a = 2 then 30 else a + 1 := by decide +kernel
theorem r2 : ∀ a < 29, ∀ b < 29, δr (a + 1) b = if b = 2 ∨ conflict a b = true then 30 else b + 1 := by
  decide +kernel
theorem r30 (x : Nat) : δr 30 x = 30 := by simp [δr]
theorem d96 (x : Nat) : δ 96 x = 96 := δ_big x (Nat.le_refl 96)

/-- **الحدُّ الأدنى المكتمل (الثلاثيّ):** يرخّص قانونُ الجذر الجذرَ إذا وفقط إذا رخّص قانونُ الوصل «يَفْعَلُ» و«فَعْلُ» معًا. -/
theorem kamil3 (a b c : Nat) (ha : a < 29) (hb : b < 29) (hc : c < 29) :
    Mroot.F ([a, b, c].foldl δr 0) = true ↔
      (Fwasl (run 0 (yafal a b c)) = true ∧ Fwasl (run 0 (fal a b c)) = true) := by
  obtain ⟨e1, e2, e3, e4, f1, f3⟩ := wasl_khatwa
  simp only [yafal, fal, List.foldl, run]
  rw [e1, e2 a ha, e3 a ha b hb, f1 a ha]
  rw [r1 a ha]
  by_cases h1 : a = 2
  · subst h1; simp [r30, d96, Mroot, Fwasl]
  · rw [if_neg h1, if_neg h1, r2 a ha b hb, e2 b hb]
    by_cases h2 : b = 2 ∨ conflict a b = true
    · rw [if_pos h2]
      have : (b = 2 ∨ (a ≠ 2 ∧ conflict a b = true)) := by
        rcases h2 with h | h
        · exact Or.inl h
        · exact Or.inr ⟨h1, h⟩
      rw [if_pos this]; simp [r30, d96, Mroot, Fwasl]
    · rw [if_neg h2]
      have h2' : ¬ (b = 2 ∨ (a ≠ 2 ∧ conflict a b = true)) := fun h => h2 (by
        rcases h with h | h
        · exact Or.inl h
        · exact Or.inr h.2)
      rw [if_neg h2', e4 c hc, f3 b hb c hc]
      have hb2 : b ≠ 2 := fun h => h2 (Or.inl h)
      rw [r2 b hb c hc]
      by_cases h3 : c = 2 ∨ conflict b c = true
      · rw [if_pos h3]
        rcases h3 with h | h
        · subst h; simp [r30, d96, Mroot, Fwasl]
        · rw [if_pos (Or.inr ⟨hb2, h⟩)]; by_cases hc2 : c = 2 <;> simp [hc2, r30, d96, Mroot, Fwasl]
      · rw [if_neg h3]
        have hc2 : c ≠ 2 := fun h => h3 (Or.inl h)
        have h3' : ¬ (c = 2 ∨ (b ≠ 2 ∧ conflict b c = true)) := fun h => h3 (by
          rcases h with h | h
          · exact Or.inl h
          · exact Or.inr h.2)
        rw [if_neg hc2, if_neg h3']
        simp [Mroot, Fwasl]; omega

/-- **ولا تكفي إحداهما:** «يَفْعَلُ» يقبل «لطد» و«فَعْلُ» يقبل «طدل» (الطاءُ والدالُ متجاوران)، وكلاهما مرفوضٌ جذرًا.
ل = 13، ط = 16، د = 17. -/
theorem la_yakfi_wahid :
    Fwasl (run 0 (yafal 13 16 17)) = true ∧ Mroot.F ([13, 16, 17].foldl δr 0) = false ∧
    Fwasl (run 0 (fal 16 17 13)) = true ∧ Mroot.F ([16, 17, 13].foldl δr 0) = false := by decide +kernel

end Dal.WiladaJadhr
