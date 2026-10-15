/-
  Aql/Aqliyya.lean — العقل والعقلية عند النبهاني، طبقة «الحكم» في المنظومة.

  السند (أسطر الملفّات المحوَّلة: التفكير = a3.txt، ج1 = a1.txt):
  * التفكير 55: العقل «نقل الحسّ بالواقع بواسطة الحواسّ إلى الدماغ، ووجود معلومات سابقة يُفسَّر
    بواسطتها هذا الواقع». ج1 317: لا بحث عقليّ إن فُقد واحد من الأربعة.
  * التفكير 37: الإحساس وحده لا يُنتج فكرًا ولو تكرّر.
  * التفكير 39–41: المعلومات السابقة يجب أن تكون عن الواقع أو متعلّقة به.
  * ج1 29: العقلية «الكيفية التي يُربط فيها الواقع بالمعلومات، أو المعلومات بالواقع، بقياسها إلى
    قاعدة واحدة أو قواعد معيّنة»؛ «ومن هنا يأتي اختلاف العقليات».
  * ج1 35: العقل مفطور، والعقلية تتكوّن بفعل الإنسان، وللقاعدة الأثر الأكبر في تكوينها.
  * ج1 57: إن تعدّدت القواعد كانت الشخصية «لا لون لها».
  * التفكير 65: الحكم بوجود الشيء قطعيّ، وبحقيقته أو صفته ظنّيّ.
  * ج1 27: المعنى «مفهوم» إن كان له واقع محسوس أو مسلَّم به عن محسوس، وإلّا «معلومة».

  الفرق بين العقل والعقلية في هذا الملف: العقل = اجتماع الأركان الأربعة وتعلّق المعلومة بالواقع
  (`aql`)؛ والعقلية = ذلك مقيسًا إلى قاعدة (`aqliyya`). القاعدة معامل، فلا عقلية بلا قاعدة معيّنة.
  بلا sorry ولا axiom ولا native_decide.
-/
namespace Aql

variable {W M H : Type}   -- الواقع، المعلومة السابقة، الحكم

/-- الأركان الأربعة (التفكير 55؛ ج1 317). الواقع قد يغيب، والمعلومات قائمة قد تفرغ. -/
structure Arkan (W M : Type) where
  waqi     : Option W
  hiss     : Bool
  dimagh   : Bool
  maalumat : List M

/-- تعلّق المعلومة بالواقع (التفكير 39–41)، والقاعدة التي يُقاس إليها الربط (ج1 29). -/
structure Qaida (W M H : Type) where
  qis : W → M → Option H

/-- المعلومات التي يُفسَّر بها الواقع: المتعلّقة به وحدها. -/
def mufassira (taalluq : W → M → Bool) (w : W) (ms : List M) : List M :=
  ms.filter (taalluq w)

/-- العقل: هل قام الإدراك؟ الأركان الأربعة، ومعلومةٌ واحدة على الأقلّ متعلّقة بالواقع. -/
def aql (taalluq : W → M → Bool) (a : Arkan W M) : Bool :=
  a.hiss && a.dimagh &&
    match a.waqi with
    | none => false
    | some w => !(mufassira taalluq w a.maalumat).isEmpty

/-- العقلية: الربط مقيسًا إلى قاعدة؛ مخرجه الأحكام. -/
def aqliyya (taalluq : W → M → Bool) (q : Qaida W M H) (a : Arkan W M) : List H :=
  if a.hiss && a.dimagh then
    match a.waqi with
    | none => []
    | some w => (mufassira taalluq w a.maalumat).filterMap (q.qis w)
  else []

/-! ## ١. لا حكم إن نقص ركن -/

theorem la_hukm_bila_waqi (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M)
    (h : a.waqi = none) : aqliyya t q a = [] := by
  unfold aqliyya; rw [h]; split <;> rfl

theorem la_hukm_bila_hiss (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M)
    (h : a.hiss = false) : aqliyya t q a = [] := by
  unfold aqliyya; simp [h]

theorem la_hukm_bila_dimagh (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M)
    (h : a.dimagh = false) : aqliyya t q a = [] := by
  unfold aqliyya; simp [h]

theorem la_hukm_bila_maalumat (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M)
    (h : a.maalumat = []) : aqliyya t q a = [] := by
  unfold aqliyya; rw [h]; split
  · cases a.waqi <;> rfl
  · rfl

/-! ## ٢. المعلومة غير المتعلّقة بالواقع لا تفسّره (التفكير 39–41) -/

theorem ghayr_mutaalliq_la_yufassir (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M) (w : W)
    (hw : a.waqi = some w) (h : ∀ m ∈ a.maalumat, t w m = false) : aqliyya t q a = [] := by
  have : mufassira t w a.maalumat = [] := by
    unfold mufassira; rw [List.filter_eq_nil_iff]; intro m hm; simp [h m hm]
  unfold aqliyya; rw [hw]; split
  · simp [this]
  · rfl

/-- ولا يقوم عقلٌ بلا معلومة متعلّقة. -/
theorem la_aql_bila_taalluq (t : W → M → Bool) (a : Arkan W M) (w : W)
    (hw : a.waqi = some w) (h : ∀ m ∈ a.maalumat, t w m = false) : aql t a = false := by
  have : mufassira t w a.maalumat = [] := by
    unfold mufassira; rw [List.filter_eq_nil_iff]; intro m hm; simp [h m hm]
  unfold aql; rw [hw]; simp [this]

/-! ## ٣. التكرار لا يُنشئ فكرًا (التفكير 37)
    الإحساس بالواقع n مرّة بلا معلومات سابقة: لا حكم واحد، أيًّا كان n. -/

theorem takrar_la_yunshi_fikran (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M)
    (h : a.maalumat = []) (n : Nat) :
    ((List.replicate n a).flatMap (aqliyya t q)) = [] := by
  induction n with
  | zero => rfl
  | succ k ih => simp [List.replicate_succ, List.flatMap_cons, la_hukm_bila_maalumat t q a h, ih]

/-! ## ٤. الأحكام كلّها مقيسة إلى القاعدة: لا حكم يخرج من غيرها (ج1 29) -/

theorem kull_hukm_min_alqaida (t : W → M → Bool) (q : Qaida W M H) (a : Arkan W M) (h : H)
    (hh : h ∈ aqliyya t q a) :
    ∃ w m, a.waqi = some w ∧ m ∈ a.maalumat ∧ t w m = true ∧ q.qis w m = some h := by
  unfold aqliyya at hh
  split at hh
  · rcases hw : a.waqi with _ | w
    · rw [hw] at hh; simp at hh
    · rw [hw] at hh
      simp only [List.mem_filterMap, mufassira, List.mem_filter] at hh
      obtain ⟨m, ⟨hm, ht⟩, hq⟩ := hh
      exact ⟨w, m, rfl, hm, ht, hq⟩
  · simp at hh

/-! ## ٥. اختلاف العقليات من القاعدة، وتعدّد القواعد يُفقد اللون (ج1 29، 57) -/

/-- تناقض حكمين، يعطيه المودَع (نفي وإثبات لشيء واحد مثلًا). -/
def Mutasiq (tanaqud : H → H → Prop) (hs : List H) : Prop :=
  ∀ x ∈ hs, ∀ y ∈ hs, ¬ tanaqud x y

/-- شاهد: الأركان نفسها، وقاعدتان؛ كلٌّ منهما متّسقة وحدها، وجمعهما متناقض.
    حكما الشاهد: true = «يُقبل»، false = «يُرفض»، والتناقض اختلافهما. -/
def wShahid : Arkan Unit Unit := ⟨some (), true, true, [()]⟩
def qAkhdh : Qaida Unit Unit Bool := ⟨fun _ _ => some true⟩
def qRadd  : Qaida Unit Unit Bool := ⟨fun _ _ => some false⟩
def tAll : Unit → Unit → Bool := fun _ _ => true
def tanaqudB (x y : Bool) : Prop := x ≠ y

theorem ikhtilaf_alaqliyyat :
    aqliyya tAll qAkhdh wShahid ≠ aqliyya tAll qRadd wShahid := by decide

theorem qaida_wahida_mutasiqa :
    Mutasiq tanaqudB (aqliyya tAll qAkhdh wShahid) ∧ Mutasiq tanaqudB (aqliyya tAll qRadd wShahid) := by
  refine ⟨?_, ?_⟩ <;> intro x hx y hy <;> simp [aqliyya, wShahid, qAkhdh, qRadd, tAll, mufassira] at hx hy <;>
    subst hx <;> subst hy <;> simp [tanaqudB]

theorem taaddud_alqawaid_la_lawn :
    ¬ Mutasiq tanaqudB (aqliyya tAll qAkhdh wShahid ++ aqliyya tAll qRadd wShahid) := by
  intro h
  exact h true (by decide) false (by decide) (by simp [tanaqudB])

/-! ## ٦. مرتبة الحكم ومرتبة المعنى (التفكير 65؛ ج1 27) -/

inductive NawHukm | wujud | haqiqaAwSifa deriving DecidableEq, Repr
inductive Martaba | qati | zanni deriving DecidableEq, Repr

/-- الحكم بالوجود عن حسٍّ قطعيّ؛ والحكم بالحقيقة أو الصفة ظنّيّ دائمًا. -/
def martaba : NawHukm → Bool → Martaba
  | .wujud, true => .qati
  | _, _ => .zanni

theorem haqiqa_zanniyya (hiss : Bool) : martaba .haqiqaAwSifa hiss = .zanni := rfl

inductive MartabaMana | mafhum | maaluma deriving DecidableEq, Repr

/-- المفهوم ما له شاهد واقع (محسوس أو مسلَّم به عن محسوس)، وإلّا فمعلومة. -/
def martabaMana (shuhud : List String) : MartabaMana :=
  if shuhud.isEmpty then .maaluma else .mafhum

theorem la_mafhum_bila_shahid : martabaMana [] = .maaluma := rfl

theorem mafhum_bishahid (s : String) (ss : List String) : martabaMana (s :: ss) = .mafhum := rfl

end Aql
