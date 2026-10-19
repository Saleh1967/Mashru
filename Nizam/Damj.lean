/-
  Nizam/Damj.lean — جبرُ الدمج المبرهن: مرحلةُ الدمج الأولى (إذن المالك 2026-10-19 16:16: «موافق ولك الأذن … «م1»
  (Nizam/Damj.lean) … نفذ وفق افضل الممارسات»). «م1» هنا اسمُ المرحلة في عرض الدمج الذي أمضاه المالك، لا م1 في جدول
  مراحل المنظومة (`hawkama/البروتوكول.md` §٩: حجرُ الزاوية T3). لا يستورد شيئًا.

  السببُ: دمجان على قائمة الطفرات أسقطا قيودًا بلا تعارضٍ ظاهر (P163–P169 بدمج 767e09b، وP150–P153 بدمج #35): الدمجُ النصّيّ
  يعمل على الأسطر لا على القيود، فملفٌّ في سطرٍ واحد يُحلّ تعارضُه بأخذ أحد الطرفين كلّه. والبند ٤أ في البوّابة يكشف الحذفَ
  بعد وقوعه؛ وهذه الوحدة تعرّف الدمجَ الصحيح نفسَه ليُبنى عليه سائقُ دمجٍ وفحصٌ في CI (مرحلةُ الدمج الثانية، لم تُبنَ).

  التصميم (معروضٌ على المالك وأمضاه): دمجٌ ثلاثيّ لكلّ مفتاح على الأساس o والطرفين a وb —
  * رأيُ الطرف في المفتاح (`ray`): الحاضرُ بقيمته؛ والغائبُ بشاهدِ حذفٍ صحيحٍ (بصمتُه بصمةُ تعريف الأساس، وسببُه وإذنُه غيرُ
    فارغين) محذوف؛ والغائبُ بلا شاهدٍ صحيح **لم يغيّر شيئًا** — لا حذفَ بلا شاهد.
  * الدمجُ (`damj1`): ما اتّفق عليه الطرفان يؤخذ؛ وما غيّره طرفٌ وحده يؤخذ تغييرُه؛ وما غيّراه مختلفَين تعارضٌ معلَن (`taarud`).
    فالحذفُ مقابلَ التعديل تعارض.
  * والقائمةُ كلُّها (`damj`): لا تُقبل إن كان في مفتاحٍ واحدٍ تعارض.

  ما يُبرهن (لكلّ أساسٍ وطرفين ودالّةِ بصمة): التناظر `damj_tanazur`، والتكرار `damj_tikrar`، والطرف الواحد `damj_janib_wahid`،
  والتعارض يمنع القبول `taarud_yamna`، وعدمُ الفقد `la_faqd` (مفتاحُ الأساس لا يغيب عن الدمج إلّا بشاهد حذفٍ صحيحٍ في طرفٍ غاب
  عنه)، وعدمُ الاختلاق `la_ikhtira`، والجامعة `salamat_damj`. وعلى الشاهد: حادثةُ #35 بنموذجها، وحالاتُ شاهد الحذف.

  الحدّ (معلَن):
  * البصمة دالّةٌ معامِلٌ (`basmaOf`)؛ والمثالان هنا (`basmaTafra`، والهويّة لنصّ المبرهنة) تمثيلٌ نصّيّ لا SHA-256 — بصمةُ
    التشغيل الحقيقيّة وسائقُ الدمج وفحصُ CI في المرحلة الثانية.
  * القائمةُ الناتجة قد تكرّر مفتاحًا بقيمةٍ واحدة (المفاتيح من الثلاث موصولة)؛ والمبرهناتُ كلُّها على `bahth` (أوّلُ قيمة)،
    فلا يمسّها التكرار؛ وإزالتُه في المرحلة الثانية.
  * سجلُّ الإيداع `mudaat/sijill.json` خارج المرحلة الأولى (قرار التصميم).
  بلا sorry ولا axiom ولا native_decide.
-/

namespace Nizam
namespace Damj

/-! ## ١. البحث في قائمة الأزواج -/

/-- أوّلُ قيمةٍ للمفتاح في القائمة. -/
def bahth {K V : Type} [DecidableEq K] : List (K × V) → K → Option V
  | [], _ => none
  | (k', v) :: l, k => if k' = k then some v else bahth l k

theorem bahth_mawjud {K V : Type} [DecidableEq K] (l : List (K × V)) (k : K) (v : V)
    (h : bahth l k = some v) : k ∈ l.map Prod.fst := by
  induction l with
  | nil => simp [bahth] at h
  | cons p l ih =>
    obtain ⟨k', v'⟩ := p
    simp only [bahth] at h
    by_cases hk : k' = k
    · simp [hk]
    · rw [ite_eq_right hk] at h
      simp [ih h]

theorem bahth_ghaib {K V : Type} [DecidableEq K] (l : List (K × V)) (k : K)
    (h : k ∉ l.map Prod.fst) : bahth l k = none := by
  cases hb : bahth l k with
  | none => rfl
  | some v => exact absurd (bahth_mawjud l k v hb) h

/-! ## ٢. شاهدُ الحذف والنسخة ورأيُ الطرف -/

/-- شاهدُ حذفٍ: المفتاح، وبصمةُ التعريف المحذوف، وسببُه، وإذنُ المالك. -/
structure ShahidHadhf (K : Type) where
  miftah : K
  basma : String
  sabab : String
  idhn : String
deriving DecidableEq, Repr

/-- نسخةٌ من القائمة: قيودُها، وشواهدُ ما حُذف منها. -/
structure Nuskha (K V : Type) where
  qaima : List (K × V)
  mahdhufa : List (ShahidHadhf K)

section
variable {K V : Type} [DecidableEq K] [DecidableEq V]

/-- الشاهدُ صحيحٌ لحذف تعريف الأساس w: بصمتُه بصمةُ w، وسببُه وإذنُه غيرُ فارغين. -/
def sahih (basmaOf : V → String) (w : V) (s : ShahidHadhf K) : Bool :=
  s.basma == basmaOf w && !s.sabab.isEmpty && !s.idhn.isEmpty

/-- في النسخة شاهدٌ صحيحٌ لحذف المفتاح k على تعريف الأساس w. -/
def hadhfMaadhun (basmaOf : V → String) (x : Nuskha K V) (k : K) (w : V) : Bool :=
  x.mahdhufa.any fun s => s.miftah == k && sahih basmaOf w s

/-- رأيُ النسخة x في المفتاح k نسبةً إلى قيمة الأساس o: الحاضرُ بقيمته؛ والغائبُ بشاهدٍ صحيحٍ محذوف؛ والغائبُ بلا شاهدٍ
    صحيحٍ على ما كان في الأساس (لا حذفَ بلا شاهد). -/
def ray (basmaOf : V → String) (o : Option V) (x : Nuskha K V) (k : K) : Option V :=
  match bahth x.qaima k with
  | some v => some v
  | none =>
    match o with
    | some w => if hadhfMaadhun basmaOf x k w then none else some w
    | none => none

/-- نتيجةُ الدمج في مفتاح: قيمةٌ (أو غياب)، أو تعارضٌ معلَن. -/
inductive Natija (V : Type) where
  | qima (v : Option V)
  | taarud
deriving DecidableEq, Repr

/-- الدمجُ الثلاثيّ في مفتاحٍ واحد: المتّفَق يؤخذ؛ وتغييرُ طرفٍ وحده يؤخذ؛ وتغييران مختلفان تعارض. -/
def damj1 (o a b : Option V) : Natija V :=
  if a = b then .qima a
  else if a = o then .qima b
  else if b = o then .qima a
  else .taarud

/-! ## ٣. قوانين المفتاح الواحد -/

theorem damj1_tanazur (o a b : Option V) : damj1 o a b = damj1 o b a := by
  unfold damj1
  by_cases h1 : a = b
  · subst h1; rfl
  · have h1' : b ≠ a := fun h => h1 h.symm
    rw [ite_eq_right h1, ite_eq_right h1']
    by_cases h2 : a = o
    · subst h2
      have : b ≠ a := h1'
      rw [ite_eq_left rfl, ite_eq_right this, ite_eq_left rfl]
    · rw [ite_eq_right h2]
      by_cases h3 : b = o
      · rw [ite_eq_left h3, ite_eq_left h3]
      · rw [ite_eq_right h3, ite_eq_right h3, ite_eq_right h2]

theorem damj1_tikrar (o a : Option V) : damj1 o a a = .qima a := by
  simp [damj1]

theorem damj1_janib_wahid (o a : Option V) : damj1 o a o = .qima a := by
  unfold damj1
  by_cases h : a = o
  · rw [ite_eq_left h, h]
  · rw [ite_eq_right h, ite_eq_right h, ite_eq_left rfl]

/-- **التعارضُ معلَنٌ وحده**: لا تعارضَ إلّا حيث غيّر الطرفان كلاهما واختلفا. -/
theorem damj1_taarud_iff (o a b : Option V) : damj1 o a b = .taarud ↔ a ≠ b ∧ a ≠ o ∧ b ≠ o := by
  unfold damj1
  by_cases h1 : a = b
  · rw [ite_eq_left h1]; simp [h1]
  · rw [ite_eq_right h1]
    by_cases h2 : a = o
    · rw [ite_eq_left h2]; simp [h2]
    · rw [ite_eq_right h2]
      by_cases h3 : b = o
      · rw [ite_eq_left h3]; simp [h3]
      · rw [ite_eq_right h3]; exact ⟨fun _ => ⟨h1, h2, h3⟩, fun _ => rfl⟩

/-- لا تُختلَق قيمة: ما يخرج من الدمج رأيُ أحد الطرفين. -/
theorem damj1_la_ikhtira (o a b r : Option V) (h : damj1 o a b = .qima r) : r = a ∨ r = b := by
  unfold damj1 at h
  by_cases h1 : a = b
  · rw [ite_eq_left h1] at h; cases h; exact Or.inl rfl
  · rw [ite_eq_right h1] at h
    by_cases h2 : a = o
    · rw [ite_eq_left h2] at h; cases h; exact Or.inr rfl
    · rw [ite_eq_right h2] at h
      by_cases h3 : b = o
      · rw [ite_eq_left h3] at h; cases h; exact Or.inl rfl
      · rw [ite_eq_right h3] at h; cases h

/-! ## ٤. رأيُ الطرف: متى يكون غيابًا ومتى يكون قيمة -/

omit [DecidableEq V] in
/-- **الغيابُ لا يكون حذفًا إلّا بشاهد**: رأيُ الطرف «غائب» في مفتاحٍ له في الأساس تعريفٌ w يقتضي أنّ الطرف خلا منه، وفيه
    شاهدٌ لهذا المفتاح بصمتُه بصمةُ w وسببُه وإذنُه غيرُ فارغين. -/
theorem ray_ghaib (basmaOf : V → String) (w : V) (x : Nuskha K V) (k : K)
    (h : ray basmaOf (some w) x k = none) :
    bahth x.qaima k = none ∧
      ∃ s ∈ x.mahdhufa, s.miftah = k ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "" := by
  unfold ray at h
  cases hb : bahth x.qaima k with
  | some v => simp [hb] at h
  | none =>
    simp only [hb] at h
    refine ⟨rfl, ?_⟩
    by_cases hm : hadhfMaadhun basmaOf x k w = true
    · obtain ⟨s, hs, hsk⟩ := List.any_eq_true.mp hm
      simp only [sahih, Bool.and_eq_true, beq_iff_eq, Bool.not_eq_true'] at hsk
      obtain ⟨hk, ⟨hbm, hsa⟩, hid⟩ := hsk
      have h0 : ("" : String).isEmpty = true := by decide
      refine ⟨s, hs, hk, hbm, ?_, ?_⟩
      · intro he; rw [he, h0] at hsa; cases hsa
      · intro he; rw [he, h0] at hid; cases hid
    · simp [hm] at h

omit [DecidableEq V] in
/-- رأيُ الطرف قيمةً: حاضرةٌ فيه، أو غائبةٌ عنه وهي قيمةُ الأساس. -/
theorem ray_qima (basmaOf : V → String) (o : Option V) (x : Nuskha K V) (k : K) (v : V)
    (h : ray basmaOf o x k = some v) : bahth x.qaima k = some v ∨ o = some v := by
  unfold ray at h
  cases hb : bahth x.qaima k with
  | some v' => simp only [hb] at h; exact Or.inl h
  | none =>
    simp only [hb] at h
    cases o with
    | none => simp at h
    | some w =>
      by_cases hm : hadhfMaadhun basmaOf x k w = true
      · simp [hm] at h
      · simp only [hm, Bool.false_eq_true, ite_false] at h; exact Or.inr h

omit [DecidableEq V] in
/-- طرفٌ لم يغيّر شيئًا (قيودُ الأساس بلا شواهد حذف) رأيُه الأساسُ نفسُه. -/
theorem ray_asas (basmaOf : V → String) (o : Nuskha K V) (k : K) :
    ray basmaOf (bahth o.qaima k) ⟨o.qaima, []⟩ k = bahth o.qaima k := by
  unfold ray
  cases hb : bahth o.qaima k with
  | some v => rfl
  | none => rfl

/-! ## ٥. دمجُ القائمة -/

/-- نتيجةُ الدمج في المفتاح k. -/
def damjMiftah (basmaOf : V → String) (o a b : Nuskha K V) (k : K) : Natija V :=
  damj1 (bahth o.qaima k) (ray basmaOf (bahth o.qaima k) a k) (ray basmaOf (bahth o.qaima k) b k)

/-- المفاتيحُ كلُّها: ما في الأساس والطرفين. -/
def mafatih (o a b : Nuskha K V) : List K :=
  o.qaima.map Prod.fst ++ a.qaima.map Prod.fst ++ b.qaima.map Prod.fst

/-- جمعُ النتائج: تعارضٌ في مفتاحٍ واحدٍ يُسقط الدمج كلَّه؛ والغائبُ لا يُكتب. -/
def jam (f : K → Natija V) : List K → Option (List (K × V))
  | [] => some []
  | k :: ks =>
    match f k, jam f ks with
    | .taarud, _ => none
    | .qima _, none => none
    | .qima none, some l => some l
    | .qima (some v), some l => some ((k, v) :: l)

/-- الدمج: قائمةٌ واحدة، أو لا شيء إن كان تعارض. -/
def damj (basmaOf : V → String) (o a b : Nuskha K V) : Option (List (K × V)) :=
  jam (damjMiftah basmaOf o a b) (mafatih o a b)

omit [DecidableEq K] [DecidableEq V] in
theorem jam_taarud (f : K → Natija V) (ks : List K) (k : K) (hk : k ∈ ks) (h : f k = .taarud) :
    jam f ks = none := by
  induction ks with
  | nil => cases hk
  | cons k' ks ih =>
    simp only [jam]
    rcases List.mem_cons.mp hk with he | hk
    · subst he; rw [h]
    · rw [ih hk]; cases f k' <;> rfl

omit [DecidableEq K] [DecidableEq V] in
theorem jam_mafatih (f : K → Natija V) (ks : List K) (l : List (K × V)) (h : jam f ks = some l) :
    ∀ k ∈ l.map Prod.fst, k ∈ ks := by
  induction ks generalizing l with
  | nil => simp only [jam] at h; cases h; simp
  | cons k0 ks ih =>
    simp only [jam] at h
    cases hf : f k0 with
    | taarud => rw [hf] at h; cases h
    | qima r =>
      cases hj : jam f ks with
      | none => rw [hf, hj] at h; cases r <;> cases h
      | some l' =>
        rw [hf, hj] at h
        cases r with
        | none =>
          simp only [Option.some.injEq] at h; subst h
          intro k hk; exact List.mem_cons_of_mem _ (ih l' hj k hk)
        | some v =>
          simp only [Option.some.injEq] at h; subst h
          intro k hk
          simp only [List.map_cons, List.mem_cons] at hk
          rcases hk with rfl | hk
          · exact List.mem_cons_self
          · exact List.mem_cons_of_mem _ (ih l' hj k hk)

omit [DecidableEq V] in
theorem jam_sahih (f : K → Natija V) (ks : List K) (l : List (K × V)) (h : jam f ks = some l) :
    ∀ k ∈ ks, f k = .qima (bahth l k) := by
  induction ks generalizing l with
  | nil => intro k hk; cases hk
  | cons k0 ks ih =>
    simp only [jam] at h
    cases hf : f k0 with
    | taarud => rw [hf] at h; cases h
    | qima r =>
      cases hj : jam f ks with
      | none => rw [hf, hj] at h; cases r <;> cases h
      | some l' =>
        rw [hf, hj] at h
        have ih' := ih l' hj
        cases r with
        | none =>
          simp only [Option.some.injEq] at h; subst h
          intro k hk
          rcases List.mem_cons.mp hk with he | hk
          · subst he
            rw [hf]
            cases hb : bahth l' k with
            | none => rfl
            | some v =>
              have := ih' k (jam_mafatih f ks l' hj k (bahth_mawjud l' k v hb))
              rw [hf, hb] at this; cases this
          · exact ih' k hk
        | some v =>
          simp only [Option.some.injEq] at h; subst h
          intro k hk
          by_cases he : k0 = k
          · subst he; rw [hf]; simp [bahth]
          · have hk' : k ∈ ks := by
              rcases List.mem_cons.mp hk with he' | hk'
              · exact absurd he'.symm he
              · exact hk'
            rw [ih' k hk']; simp [bahth, he]

omit [DecidableEq K] [DecidableEq V] in
theorem jam_some (f : K → Natija V) (ks : List K) (h : ∀ k ∈ ks, f k ≠ .taarud) :
    ∃ l, jam f ks = some l := by
  induction ks with
  | nil => exact ⟨[], rfl⟩
  | cons k0 ks ih =>
    obtain ⟨l, hl⟩ := ih (fun k hk => h k (List.mem_cons_of_mem _ hk))
    simp only [jam]
    cases hf : f k0 with
    | taarud => exact absurd hf (h k0 List.mem_cons_self)
    | qima r =>
      rw [hl]
      cases r with
      | none => exact ⟨l, rfl⟩
      | some v => exact ⟨(k0, v) :: l, rfl⟩

/-- خارجَ المفاتيح لا شيء: لا أساسَ ولا طرف، فالنتيجةُ غيابٌ بلا تعارض. -/
theorem damjMiftah_kharij (basmaOf : V → String) (o a b : Nuskha K V) (k : K) (hk : k ∉ mafatih o a b) :
    damjMiftah basmaOf o a b k = .qima none := by
  simp only [mafatih, List.mem_append, not_or] at hk
  obtain ⟨⟨ho, ha⟩, hb⟩ := hk
  unfold damjMiftah ray
  rw [bahth_ghaib _ _ ho, bahth_ghaib _ _ ha, bahth_ghaib _ _ hb]
  exact damj1_tikrar none none

/-- **الدمجُ المقبول نقطةً نقطة**: في كلّ مفتاح — داخلَ المفاتيح وخارجَها — قيمةُ القائمة الناتجة هي نتيجةُ دمج ذلك المفتاح. -/
theorem damj_nuqta (basmaOf : V → String) (o a b : Nuskha K V) (m : List (K × V))
    (hm : damj basmaOf o a b = some m) (k : K) :
    damjMiftah basmaOf o a b k = .qima (bahth m k) := by
  by_cases hk : k ∈ mafatih o a b
  · exact jam_sahih _ _ _ hm k hk
  · rw [damjMiftah_kharij basmaOf o a b k hk]
    have : k ∉ m.map Prod.fst := fun h => hk (jam_mafatih _ _ _ hm k h)
    rw [bahth_ghaib m k this]

/-! ## ٦. القوانين -/

/-- **التعارضُ يمنع القبول**: تعارضٌ في مفتاحٍ واحد — أيًّا كان — يُسقط الدمج كلَّه. -/
theorem taarud_yamna (basmaOf : V → String) (o a b : Nuskha K V) (k : K)
    (h : damjMiftah basmaOf o a b k = .taarud) : damj basmaOf o a b = none := by
  by_cases hk : k ∈ mafatih o a b
  · exact jam_taarud _ _ k hk h
  · rw [damjMiftah_kharij basmaOf o a b k hk] at h; cases h

/-- **التناظر**: الدمجُ لا يفضّل طرفًا — قبولُه واحدٌ بالترتيبين، وقيمُه واحدةٌ في كلّ مفتاح. -/
theorem damj_tanazur (basmaOf : V → String) (o a b : Nuskha K V) (m : List (K × V))
    (hm : damj basmaOf o a b = some m) :
    ∃ m', damj basmaOf o b a = some m' ∧ ∀ k, bahth m' k = bahth m k := by
  have hs : ∀ k, damjMiftah basmaOf o b a k = damjMiftah basmaOf o a b k := fun k => by
    unfold damjMiftah; exact damj1_tanazur _ _ _
  obtain ⟨m', hm'⟩ := jam_some (damjMiftah basmaOf o b a) (mafatih o b a) (fun k _ h => by
    rw [hs k, damj_nuqta basmaOf o a b m hm k] at h; cases h)
  refine ⟨m', hm', fun k => ?_⟩
  have h1 := damj_nuqta basmaOf o b a m' hm' k
  rw [hs k, damj_nuqta basmaOf o a b m hm k] at h1
  exact (Natija.qima.inj h1).symm

/-- **التكرار**: دمجُ طرفٍ بنفسه لا يتعارض، ونتيجتُه رأيُه هو. -/
theorem damj_tikrar (basmaOf : V → String) (o a : Nuskha K V) :
    ∃ m, damj basmaOf o a a = some m ∧ ∀ k, bahth m k = ray basmaOf (bahth o.qaima k) a k := by
  have hk : ∀ k, damjMiftah basmaOf o a a k = .qima (ray basmaOf (bahth o.qaima k) a k) := fun k =>
    damj1_tikrar _ _
  obtain ⟨m, hm⟩ := jam_some (damjMiftah basmaOf o a a) (mafatih o a a) (fun k _ h => by
    rw [hk k] at h; cases h)
  refine ⟨m, hm, fun k => ?_⟩
  have := damj_nuqta basmaOf o a a m hm k
  rw [hk k] at this; exact (Natija.qima.inj this).symm

/-- **الطرفُ الواحد**: إن لم يغيّر أحدُ الطرفين شيئًا فالدمجُ رأيُ الآخر، بلا تعارض. -/
theorem damj_janib_wahid (basmaOf : V → String) (o a : Nuskha K V) :
    ∃ m, damj basmaOf o a ⟨o.qaima, []⟩ = some m ∧ ∀ k, bahth m k = ray basmaOf (bahth o.qaima k) a k := by
  have hk : ∀ k, damjMiftah basmaOf o a ⟨o.qaima, []⟩ k = .qima (ray basmaOf (bahth o.qaima k) a k) := fun k => by
    unfold damjMiftah; rw [ray_asas]; exact damj1_janib_wahid _ _
  obtain ⟨m, hm⟩ := jam_some (damjMiftah basmaOf o a ⟨o.qaima, []⟩) (mafatih o a ⟨o.qaima, []⟩)
    (fun k _ h => by rw [hk k] at h; cases h)
  refine ⟨m, hm, fun k => ?_⟩
  have := damj_nuqta basmaOf o a ⟨o.qaima, []⟩ m hm k
  rw [hk k] at this; exact (Natija.qima.inj this).symm

/-- **لا فقدَ بلا شاهد**: مفتاحٌ في الأساس غاب عن الدمج المقبول ⇒ طرفٌ خلا منه وفيه شاهدُ حذفٍ لهذا المفتاح بصمتُه بصمةُ
    تعريف الأساس، وسببُه وإذنُه غيرُ فارغين. (حادثتا 767e09b و#35: غيابٌ بلا شاهد.) -/
theorem la_faqd (basmaOf : V → String) (o a b : Nuskha K V) (m : List (K × V))
    (hm : damj basmaOf o a b = some m) (k : K) (w : V)
    (ho : bahth o.qaima k = some w) (hk : bahth m k = none) :
    (bahth a.qaima k = none ∧
      ∃ s ∈ a.mahdhufa, s.miftah = k ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") ∨
    (bahth b.qaima k = none ∧
      ∃ s ∈ b.mahdhufa, s.miftah = k ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") := by
  have h := damj_nuqta basmaOf o a b m hm k
  rw [hk] at h
  unfold damjMiftah at h
  rw [ho] at h
  rcases damj1_la_ikhtira _ _ _ _ h with ha | hb
  · exact Or.inl (ray_ghaib basmaOf w a k ha.symm)
  · exact Or.inr (ray_ghaib basmaOf w b k hb.symm)

/-- **لا اختلاق**: كلّ قيمةٍ في الدمج المقبول قيمتُها في الأساس أو في أحد الطرفين. -/
theorem la_ikhtira (basmaOf : V → String) (o a b : Nuskha K V) (m : List (K × V))
    (hm : damj basmaOf o a b = some m) (k : K) (v : V) (h : bahth m k = some v) :
    bahth o.qaima k = some v ∨ bahth a.qaima k = some v ∨ bahth b.qaima k = some v := by
  have hn := damj_nuqta basmaOf o a b m hm k
  rw [h] at hn
  unfold damjMiftah at hn
  rcases damj1_la_ikhtira _ _ _ _ hn with ha | hb
  · rcases ray_qima basmaOf _ a k v ha.symm with h1 | h1
    · exact Or.inr (Or.inl h1)
    · exact Or.inl h1
  · rcases ray_qima basmaOf _ b k v hb.symm with h1 | h1
    · exact Or.inr (Or.inr h1)
    · exact Or.inl h1

/-- **سلامةُ الدمج** (الجامعة): الدمجُ المقبول لا يفقد مفتاحًا بلا شاهد، ولا يختلق قيمة، ويأخذ ما اتّفق عليه الطرفان، ويأخذ
    تغييرَ الطرف الذي غيّر حين لم يغيّر الآخر. -/
theorem salamat_damj (basmaOf : V → String) (o a b : Nuskha K V) (m : List (K × V))
    (hm : damj basmaOf o a b = some m) (k : K) :
    (∀ w, bahth o.qaima k = some w → bahth m k = none →
      (bahth a.qaima k = none ∧
        ∃ s ∈ a.mahdhufa, s.miftah = k ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") ∨
      (bahth b.qaima k = none ∧
        ∃ s ∈ b.mahdhufa, s.miftah = k ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "")) ∧
    (∀ v, bahth m k = some v →
      bahth o.qaima k = some v ∨ bahth a.qaima k = some v ∨ bahth b.qaima k = some v) ∧
    (ray basmaOf (bahth o.qaima k) a k = ray basmaOf (bahth o.qaima k) b k →
      bahth m k = ray basmaOf (bahth o.qaima k) a k) ∧
    (ray basmaOf (bahth o.qaima k) b k = bahth o.qaima k →
      bahth m k = ray basmaOf (bahth o.qaima k) a k) := by
  have hn := damj_nuqta basmaOf o a b m hm k
  unfold damjMiftah at hn
  refine ⟨fun w ho hk => la_faqd basmaOf o a b m hm k w ho hk,
          fun v h => la_ikhtira basmaOf o a b m hm k v h, fun he => ?_, fun he => ?_⟩
  · rw [he, damj1_tikrar] at hn; rw [he]; exact (Natija.qima.inj hn).symm
  · rw [he, damj1_janib_wahid] at hn; exact (Natija.qima.inj hn).symm

end

/-! ## ٧. المثالان: قائمةُ الطفرات وأسماءُ المبرهنات المحميّة -/

/-- قيدُ طفرةٍ بلا اسمه (الاسمُ مفتاح). -/
structure Tafra where
  milaf : String
  min : String
  ila : String
deriving DecidableEq, Repr

/-- بصمةُ الطفرة في النموذج: تسلسلُها نصًّا (تمثيلٌ لا SHA-256؛ البصمةُ الحقيقيّة في المرحلة الثانية). -/
def basmaTafra (t : Tafra) : String := t.milaf ++ "\t" ++ t.min ++ "\t" ++ t.ila

/-- أسماءُ المبرهنات المحميّة: الاسمُ مفتاح، والقيمةُ بصمةُ نصّ المبرهنة (تُحسب في المرحلة الثانية)، فبصمتُها هي نفسُها. -/
def basmaNass (s : String) : String := s

def tA : Tafra := ⟨"A.lean", "x", "y"⟩
def tB : Tafra := ⟨"B.lean", "p", "q"⟩
def tC : Tafra := ⟨"C.lean", "u", "v"⟩
def tA' : Tafra := ⟨"A.lean", "x", "z"⟩

/-- **حادثةُ #35 بنموذجها** (على الشاهد): الأساسُ فيه P149؛ أضاف main ‏P150 وأضاف الفرعُ P163؛ الدمجُ يحفظ الثلاثة ولا يتعارض. -/
theorem shahid_dumija_bila_faqd :
    (damj basmaTafra ⟨[("P149", tA)], []⟩ ⟨[("P149", tA), ("P150", tB)], []⟩ ⟨[("P149", tA), ("P163", tC)], []⟩).map
      (fun m => (bahth m "P149", bahth m "P150", bahth m "P163")) = some (some tA, some tB, some tC) := by
  decide +kernel

/-- **شاهدُ الحذف** (على الشاهد): حذفٌ بشاهدٍ صحيحٍ يُحذف؛ وغيابٌ بلا شاهد، أو بشاهدٍ لتعريفٍ آخر، أو بلا إذن، لا يحذف؛ وحذفٌ
    مقابلَ تعديلٍ تعارض. -/
theorem shawahid_hadhf :
    (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩).map
      (bahth · "P1") = some none ∧
    (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], []⟩ ⟨[("P1", tA)], []⟩).map (bahth · "P1") = some (some tA) ∧
    (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tB, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩).map
      (bahth · "P1") = some (some tA) ∧
    (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", ""⟩]⟩ ⟨[("P1", tA)], []⟩).map
      (bahth · "P1") = some (some tA) ∧
    damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA')], []⟩ = none := by
  decide +kernel

/-- **تعديلان مختلفان تعارض، وتعديلٌ واحدٌ يؤخذ** (على الشاهد). -/
theorem shawahid_taadil :
    damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[("P1", tA')], []⟩ ⟨[("P1", tB)], []⟩ = none ∧
    (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[("P1", tA')], []⟩ ⟨[("P1", tA)], []⟩).map (bahth · "P1") = some (some tA') := by
  decide +kernel

/-- **أسماءُ المبرهنات المحميّة** (على الشاهد): اسمٌ غاب عن طرفٍ بلا شاهدٍ يبقى؛ وبشاهدٍ ببصمة نصّه وإذنٍ يُحذف. -/
theorem shawahid_mubarhanat :
    (damj basmaNass ⟨[("Idaa.sijill_faregh", "n1")], []⟩ ⟨[], []⟩ ⟨[("Idaa.sijill_faregh", "n1")], []⟩).map
      (bahth · "Idaa.sijill_faregh") = some (some "n1") ∧
    (damj basmaNass ⟨[("Idaa.sijill_faregh", "n1")], []⟩ ⟨[], [⟨"Idaa.sijill_faregh", "n1", "استُبدلت", "المالك"⟩]⟩
      ⟨[("Idaa.sijill_faregh", "n1")], []⟩).map (bahth · "Idaa.sijill_faregh") = some none := by
  decide +kernel

end Damj
end Nizam
