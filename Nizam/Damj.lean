/-
  Nizam/Damj.lean — جبرُ الدمج المبرهن: مرحلةُ الدمج الأولى (إذن المالك 2026-10-19 16:16: «موافق ولك الأذن … «م1»
  (Nizam/Damj.lean) … نفذ وفق افضل الممارسات»). «م1» هنا اسمُ المرحلة في عرض الدمج الذي أمضاه المالك، لا م1 في جدول
  مراحل المنظومة (`hawkama/البروتوكول.md` §٩: حجرُ الزاوية T3). لا يستورد شيئًا.

  السببُ: دمجان على قائمة الطفرات أسقطا قيودًا (تاريخُ git، يعيده `tahaqquq/test_hawadith.py`):
  * 767e09b: أضاف main سبعَ طفرات (P163–P169) على أساسٍ خلا منها، فحُلّت كتلةُ التعارض في tafrat.json بأخذ طرف الفرع كلِّه.
  * feb12a8 (#35): في الأساس أربعٌ (P150–P153 بأسمائها في الاختبار) خلا منها الفرعُ بلا شاهد وأبقاها main؛ فحمل git الحذفَ
    بلا تعارضٍ في موضعه (وكتلةُ التعارض الوحيدة في الملفّ في موضعٍ آخر).
  الدمجُ النصّيّ يعمل على الأسطر لا على القيود. والبند ٤أ يكشف الفقدَ بعد وقوعه؛ وهذه الوحدة تعرّف الدمجَ الصحيح نفسَه ليُبنى
  عليه سائقُ دمجٍ وفحصٌ في CI (مرحلةُ الدمج الثانية، لم تُبنَ).

  التصميم (معروضٌ على المالك وأمضاه): دمجٌ ثلاثيّ لكلّ مفتاح على الأساس o والطرفين a وb —
  * رأيُ الطرف في المفتاح (`ray`): الحاضرُ بقيمته؛ والغائبُ بشاهدِ حذفٍ صحيح (`sahih`: بصمتُه غيرُ فارغةٍ وهي بصمةُ تعريف الأساس،
    وسببُه وحقلُ إذنه غيرُ فارغين) محذوف؛ والغائبُ بلا شاهدٍ صحيح **لم يغيّر شيئًا** — لا حذفَ بلا شاهد.
  * الدمجُ (`damj1`): ما اتّفق عليه الطرفان يؤخذ؛ وما غيّره طرفٌ وحده يؤخذ تغييرُه؛ وما غيّراه مختلفَين تعارضٌ معلَن (`taarud`).
    فالحذفُ مقابلَ التعديل تعارض، وتعريفان مختلفان لاسمٍ واحد تعارض.
  * القائمةُ (`damj`): لا تُقبل إن كان في الأساس أو أحد الطرفين اسمٌ مكرَّر، أو في مفتاحٍ واحدٍ تعارض (`mutaarida` تسمّيه)؛
    ومفاتيحُ الناتج بلا تكرار، ويحمل الناتجُ شواهدَ ما حُذف (`shawahidBaqiya`)، فهو طرفٌ صالحٌ لدمجٍ تالٍ.

  ما يُبرهن (لكلّ أساسٍ وطرفين ودالّةِ بصمة):
  * التناظر `damj_tanazur`، والتكرار `damj_tikrar`، والطرف الواحد `damj_janib_wahid`، والتجميع `damj_tajmii`
    ((a ⊔ b) ⊔ c و a ⊔ (b ⊔ c) يُقبلان معًا ويتساويان في كلّ مفتاح؛ وفي المفتاح الواحد `damj1_tajmii`).
  * متى يُقبل `damj_maqbul_iff` (لا تكرار ولا تعارض — لا أكثر ولا أقلّ)، والتعارضُ يمنع القبول `taarud_yamna`، وأسماؤه `mem_mutaarida`.
  * عدمُ الفقد: `la_faqd` لمفاتيح الأساس (نمط #35)، و`la_faqd_janib` لقيود الطرف (نمط 767e09b: الإضافةُ لا تضيع أبدًا)؛ وعدمُ
    الاختلاق `la_ikhtira`؛ والناتجُ بلا تكرار `damj_bilaTakrar`، ورأيُه قيمُه `ray_damj`، والمحذوفُ لا يعود `hadhf_yabqa`؛ والجامعة
    `salamat_damj`.
  * وعلى الشاهد (`decide +kernel`): الحادثتان بنموذجهما وأسمائهما الحقيقيّة، وحالاتُ شاهد الحذف، وعدمُ العودة، والتعارضُ المسمّى،
    والتكرار، وأسماءُ المبرهنات المحميّة.

  الحدّ (معلَن):
  * البصمة دالّةٌ معامِلٌ (`basmaOf`)، وتبايُنُها مفترضٌ لا مبرهن؛ والمثالان هنا (`basmaTafra`، والهويّة لنصّ المبرهنة) تمثيلٌ
    نصّيّ لا SHA-256 — بصمةُ التشغيل الحقيقيّة وسائقُ الدمج وفحصُ CI في المرحلة الثانية.
  * حقلُ الإذن يُشترط غيرَ فارغ، ومصدرُه لا يُتحقّق هنا؛ وصيغةُ الشاهد هنا (مع البصمة) غيرُ صيغة السجلّ القائم
    `tahaqquq/tafrat_mahdhufa.json` ({ism، sabab، idhn} بلا بصمة).
  * شاهدُ حذفٍ غيرُ صحيح، أو شاهدٌ والقيمةُ حاضرة، يُهمَل بلا تشخيص (الحضورُ أقوى شاهد).
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

/-- شاهدُ حذفٍ: المفتاح، وبصمةُ التعريف المحذوف، وسببُه، وحقلُ إذنٍ (يُشترط غيرَ فارغ؛ ومصدرُه لا يُتحقّق هنا). -/
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

/-- نصٌّ غيرُ فارغ بلغة Bool. -/
theorem ghayr_farigh (t : String) : (!t.isEmpty) = true ↔ t ≠ "" := by
  cases h : t.isEmpty
  · refine ⟨fun _ he => ?_, fun _ => rfl⟩
    rw [he] at h; exact absurd h (by decide)
  · exact ⟨fun hh => by simp at hh, fun hn => absurd (String.isEmpty_iff.mp h) hn⟩

section
variable {K V : Type} [DecidableEq K] [DecidableEq V]

/-- الشاهدُ صحيحٌ لحذف تعريف الأساس w: بصمتُه غيرُ فارغةٍ وهي بصمةُ w، وسببُه وحقلُ إذنه غيرُ فارغين. -/
def sahih (basmaOf : V → String) (w : V) (s : ShahidHadhf K) : Bool :=
  !s.basma.isEmpty && s.basma == basmaOf w && !s.sabab.isEmpty && !s.idhn.isEmpty

omit [DecidableEq K] [DecidableEq V] in
theorem sahih_iff (basmaOf : V → String) (w : V) (s : ShahidHadhf K) :
    sahih basmaOf w s = true ↔ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "" := by
  unfold sahih
  rw [Bool.and_eq_true, Bool.and_eq_true, Bool.and_eq_true, ghayr_farigh, ghayr_farigh, ghayr_farigh, beq_iff_eq]
  exact ⟨fun ⟨⟨⟨a, b⟩, c⟩, d⟩ => ⟨a, b, c, d⟩, fun ⟨a, b, c, d⟩ => ⟨⟨⟨a, b⟩, c⟩, d⟩⟩

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

/-- غيابُ الناتج وأحدُ الطرفين حاضر: فذاك الطرفُ لم يغيّر، والآخرُ هو الغائب. -/
theorem damj1_ghaib (o a b : Option V) (ha : a ≠ none) (h : damj1 o a b = .qima none) : a = o ∧ b = none := by
  unfold damj1 at h
  by_cases h1 : a = b
  · rw [ite_eq_left h1] at h; cases h; exact absurd rfl ha
  · rw [ite_eq_right h1] at h
    by_cases h2 : a = o
    · rw [ite_eq_left h2] at h; cases h; exact ⟨h2, rfl⟩
    · rw [ite_eq_right h2] at h
      by_cases h3 : b = o
      · rw [ite_eq_left h3] at h; cases h; exact absurd rfl ha
      · rw [ite_eq_right h3] at h; cases h

/-- دمجٌ يلي دمجًا: التعارضُ يسري، وإلّا فدمجُ القيمة بالثالث. -/
def natijaThumma (o : Option V) (x : Natija V) (c : Option V) : Natija V :=
  match x with
  | .taarud => .taarud
  | .qima r => damj1 o r c

/-- دمجٌ يسبق دمجًا: الأوّلُ بنتيجة دمج الآخرَين. -/
def natijaQabl (o : Option V) (a : Option V) (y : Natija V) : Natija V :=
  match y with
  | .taarud => .taarud
  | .qima r => damj1 o a r

/-- **التجميع في المفتاح الواحد**: (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c) على أساسٍ واحد، والتعارضُ يسري في الجهتين. -/
theorem damj1_tajmii (o a b c : Option V) :
    natijaThumma o (damj1 o a b) c = natijaQabl o a (damj1 o b c) := by
  unfold damj1
  by_cases h1 : a = b <;> by_cases h2 : a = o <;> by_cases h3 : b = o <;>
    by_cases h4 : b = c <;> by_cases h5 : c = o <;> by_cases h6 : a = c <;>
    simp_all [natijaThumma, natijaQabl, damj1]

/-! ## ٤. رأيُ الطرف: متى يكون غيابًا ومتى يكون قيمة -/

omit [DecidableEq V] in
/-- الغيابُ في رأي الطرف، ولمفتاحه تعريفٌ w في الأساس: خلا منه الطرفُ وفيه شاهدٌ صحيحٌ لهذا المفتاح على w. -/
theorem ray_ghaib_sahih (basmaOf : V → String) (w : V) (x : Nuskha K V) (k : K)
    (h : ray basmaOf (some w) x k = none) :
    bahth x.qaima k = none ∧ ∃ s ∈ x.mahdhufa, s.miftah = k ∧ sahih basmaOf w s = true := by
  unfold ray at h
  cases hb : bahth x.qaima k with
  | some v => simp [hb] at h
  | none =>
    simp only [hb] at h
    refine ⟨rfl, ?_⟩
    by_cases hm : hadhfMaadhun basmaOf x k w = true
    · obtain ⟨s, hs, hsk⟩ := List.any_eq_true.mp hm
      rw [Bool.and_eq_true, beq_iff_eq] at hsk
      exact ⟨s, hs, hsk.1, hsk.2⟩
    · simp [hm] at h

omit [DecidableEq V] in
/-- **الغيابُ لا يكون حذفًا إلّا بشاهد**: رأيُ الطرف «غائب» في مفتاحٍ له في الأساس تعريفٌ w يقتضي أنّ الطرف خلا منه، وفيه
    شاهدٌ لهذا المفتاح بصمتُه غيرُ فارغةٍ وهي بصمةُ w، وسببُه وحقلُ إذنه غيرُ فارغين. -/
theorem ray_ghaib (basmaOf : V → String) (w : V) (x : Nuskha K V) (k : K)
    (h : ray basmaOf (some w) x k = none) :
    bahth x.qaima k = none ∧
      ∃ s ∈ x.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "" := by
  obtain ⟨h1, s, hs, hk, hsa⟩ := ray_ghaib_sahih basmaOf w x k h
  exact ⟨h1, s, hs, hk, (sahih_iff basmaOf w s).mp hsa⟩

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
/-- الحاضرُ رأيُه قيمتُه. -/
theorem ray_hadir (basmaOf : V → String) (o : Option V) (x : Nuskha K V) (k : K) (v : V)
    (h : bahth x.qaima k = some v) : ray basmaOf o x k = some v := by
  unfold ray; rw [h]

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

/-- القائمةُ بلا تكرار (يبقى آخرُ ورودٍ لكلّ عنصر). -/
def farid : List K → List K
  | [] => []
  | k :: ks => if k ∈ farid ks then farid ks else k :: farid ks

omit [DecidableEq V] in
theorem mem_farid (l : List K) (k : K) : k ∈ farid l ↔ k ∈ l := by
  induction l with
  | nil => simp [farid]
  | cons x xs ih =>
    simp only [farid]
    by_cases hx : x ∈ farid xs
    · rw [ite_eq_left hx, ih, List.mem_cons]
      exact ⟨Or.inr, fun h => h.elim (fun he => by subst he; exact ih.mp hx) id⟩
    · rw [ite_eq_right hx, List.mem_cons, List.mem_cons, ih]

omit [DecidableEq V] in
theorem farid_nodup (l : List K) : (farid l).Nodup := by
  induction l with
  | nil => exact List.nodup_nil
  | cons x xs ih =>
    simp only [farid]
    by_cases hx : x ∈ farid xs
    · rw [ite_eq_left hx]; exact ih
    · rw [ite_eq_right hx]; exact List.nodup_cons.mpr ⟨hx, ih⟩

/-- المفاتيحُ كلُّها بلا تكرار: ما في الأساس والطرفين. -/
def mafatih (o a b : Nuskha K V) : List K :=
  farid (o.qaima.map Prod.fst ++ a.qaima.map Prod.fst ++ b.qaima.map Prod.fst)

/-- جمعُ النتائج: تعارضٌ في مفتاحٍ واحدٍ يُسقط الدمج كلَّه؛ والغائبُ لا يُكتب. -/
def jam (f : K → Natija V) : List K → Option (List (K × V))
  | [] => some []
  | k :: ks =>
    match f k, jam f ks with
    | .taarud, _ => none
    | .qima _, none => none
    | .qima none, some l => some l
    | .qima (some v), some l => some ((k, v) :: l)

/-- النسخةُ بلا مفتاحٍ مكرَّر. -/
def bilaTakrar (x : Nuskha K V) : Bool := decide (x.qaima.map Prod.fst).Nodup

/-- شواهدُ الحذف الباقية في الناتج: كلُّ شاهدٍ من الطرفين صحيحٍ على تعريف الأساس لمفتاحٍ غاب عن الناتج — فلا يعود محذوفٌ
    في دمجٍ تالٍ (`hadhf_yabqa`). -/
def shawahidBaqiya (basmaOf : V → String) (o a b : Nuskha K V) (l : List (K × V)) : List (ShahidHadhf K) :=
  (a.mahdhufa ++ b.mahdhufa).filter fun s =>
    (bahth l s.miftah).isNone &&
      match bahth o.qaima s.miftah with
      | some w => sahih basmaOf w s
      | none => false

/-- الدمج: نسخةٌ واحدة بشواهدها، أو لا شيء إن كان في الأساس أو أحد الطرفين مفتاحٌ مكرَّر، أو في مفتاحٍ تعارض. -/
def damj (basmaOf : V → String) (o a b : Nuskha K V) : Option (Nuskha K V) :=
  if bilaTakrar o && bilaTakrar a && bilaTakrar b then
    (jam (damjMiftah basmaOf o a b) (mafatih o a b)).map fun l => ⟨l, shawahidBaqiya basmaOf o a b l⟩
  else none

/-- المفاتيحُ المتعارضة بأسمائها. -/
def mutaarida (basmaOf : V → String) (o a b : Nuskha K V) : List K :=
  (mafatih o a b).filter fun k => damjMiftah basmaOf o a b k == .taarud

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
/-- مفاتيحُ الناتج قائمةٌ جزئيّةٌ من المفاتيح بترتيبها. -/
theorem jam_juz (f : K → Natija V) (ks : List K) (l : List (K × V)) (h : jam f ks = some l) :
    (l.map Prod.fst).Sublist ks := by
  induction ks generalizing l with
  | nil => simp only [jam] at h; cases h; exact List.Sublist.slnil
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
          exact (ih l' hj).cons k0
        | some v =>
          simp only [Option.some.injEq] at h; subst h
          exact (ih l' hj).cons_cons k0

omit [DecidableEq K] [DecidableEq V] in
theorem jam_mafatih (f : K → Natija V) (ks : List K) (l : List (K × V)) (h : jam f ks = some l) :
    ∀ k ∈ l.map Prod.fst, k ∈ ks :=
  fun _ hk => (jam_juz f ks l h).subset hk

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

omit [DecidableEq V] in
theorem mem_mafatih (o a b : Nuskha K V) (k : K) :
    k ∈ mafatih o a b ↔ k ∈ o.qaima.map Prod.fst ∨ k ∈ a.qaima.map Prod.fst ∨ k ∈ b.qaima.map Prod.fst := by
  rw [mafatih, mem_farid, List.mem_append, List.mem_append, or_assoc]

/-- خارجَ المفاتيح لا شيء: لا أساسَ ولا طرف، فالنتيجةُ غيابٌ بلا تعارض. -/
theorem damjMiftah_kharij (basmaOf : V → String) (o a b : Nuskha K V) (k : K) (hk : k ∉ mafatih o a b) :
    damjMiftah basmaOf o a b k = .qima none := by
  rw [mem_mafatih, not_or, not_or] at hk
  obtain ⟨ho, ha, hb⟩ := hk
  unfold damjMiftah ray
  rw [bahth_ghaib _ _ ho, bahth_ghaib _ _ ha, bahth_ghaib _ _ hb]
  exact damj1_tikrar none none

/-- فكُّ القبول: المدخلاتُ بلا تكرار، والجمعُ على المفاتيح نجح، والناتجُ قيودُه وشواهدُه الباقية. -/
theorem damj_some (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) :
    bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true ∧
      jam (damjMiftah basmaOf o a b) (mafatih o a b) = some m.qaima ∧
      m.mahdhufa = shawahidBaqiya basmaOf o a b m.qaima := by
  unfold damj at hm
  by_cases ht : (bilaTakrar o && bilaTakrar a && bilaTakrar b) = true
  · rw [ite_eq_left ht] at hm
    rw [Bool.and_eq_true, Bool.and_eq_true] at ht
    obtain ⟨⟨h1, h2⟩, h3⟩ := ht
    cases hj : jam (damjMiftah basmaOf o a b) (mafatih o a b) with
    | none => rw [hj] at hm; cases hm
    | some l =>
      rw [hj] at hm
      simp only [Option.map_some, Option.some.injEq] at hm
      subst hm
      exact ⟨h1, h2, h3, rfl, rfl⟩
  · rw [ite_eq_right ht] at hm; cases hm

/-- **الدمجُ المقبول نقطةً نقطة**: في كلّ مفتاح — داخلَ المفاتيح وخارجَها — قيمةُ الناتج هي نتيجةُ دمج ذلك المفتاح. -/
theorem damj_nuqta (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) :
    damjMiftah basmaOf o a b k = .qima (bahth m.qaima k) := by
  obtain ⟨_, _, _, hj, _⟩ := damj_some basmaOf o a b m hm
  by_cases hk : k ∈ mafatih o a b
  · exact jam_sahih _ _ _ hj k hk
  · rw [damjMiftah_kharij basmaOf o a b k hk]
    have : k ∉ m.qaima.map Prod.fst := fun h => hk (jam_mafatih _ _ _ hj k h)
    rw [bahth_ghaib m.qaima k this]

/-- **الناتجُ بلا تكرار**: مفاتيحُه قائمةٌ جزئيّةٌ من مفاتيحَ بلا تكرار. -/
theorem damj_bilaTakrar (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) : bilaTakrar m = true := by
  obtain ⟨_, _, _, hj, _⟩ := damj_some basmaOf o a b m hm
  exact decide_eq_true ((farid_nodup _).sublist (jam_juz _ _ _ hj))

/-! ## ٦. القوانين -/

/-- **متى يُقبل الدمج**: المدخلاتُ بلا تكرار، ولا تعارضَ في أيّ مفتاح — لا أكثر ولا أقلّ. -/
theorem damj_maqbul_iff (basmaOf : V → String) (o a b : Nuskha K V) :
    (∃ m, damj basmaOf o a b = some m) ↔
      (bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true) ∧
        ∀ k, damjMiftah basmaOf o a b k ≠ .taarud := by
  constructor
  · rintro ⟨m, hm⟩
    obtain ⟨h1, h2, h3, _, _⟩ := damj_some basmaOf o a b m hm
    refine ⟨⟨h1, h2, h3⟩, fun k h => ?_⟩
    rw [damj_nuqta basmaOf o a b m hm k] at h; cases h
  · rintro ⟨⟨h1, h2, h3⟩, hk⟩
    obtain ⟨l, hl⟩ := jam_some (damjMiftah basmaOf o a b) (mafatih o a b) (fun k _ => hk k)
    refine ⟨⟨l, shawahidBaqiya basmaOf o a b l⟩, ?_⟩
    unfold damj
    rw [h1, h2, h3]
    simp [hl]

/-- **المتعارضُ مسمًّى**: مفتاحٌ في `mutaarida` هو مفتاحٌ تعارض فيه الطرفان، لا غير. -/
theorem mem_mutaarida (basmaOf : V → String) (o a b : Nuskha K V) (k : K) :
    k ∈ mutaarida basmaOf o a b ↔ damjMiftah basmaOf o a b k = .taarud := by
  unfold mutaarida
  rw [List.mem_filter, beq_iff_eq]
  constructor
  · exact fun h => h.2
  · intro h
    refine ⟨?_, h⟩
    by_cases hk : k ∈ mafatih o a b
    · exact hk
    · rw [damjMiftah_kharij basmaOf o a b k hk] at h; cases h

/-- **التعارضُ يمنع القبول**: تعارضٌ في مفتاحٍ واحد — أيًّا كان — يُسقط الدمج كلَّه. -/
theorem taarud_yamna (basmaOf : V → String) (o a b : Nuskha K V) (k : K)
    (h : damjMiftah basmaOf o a b k = .taarud) : damj basmaOf o a b = none := by
  cases hd : damj basmaOf o a b with
  | none => rfl
  | some m => rw [damj_nuqta basmaOf o a b m hd k] at h; cases h

/-- **رأيُ الناتج قيمُه**: الناتجُ طرفًا في دمجٍ تالٍ على الأساس نفسِه رأيُه في كلّ مفتاحٍ قيمتُه — فالمحذوفُ بشاهدٍ يبقى
    محذوفًا بشاهده المحمول. -/
theorem ray_damj (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) :
    ray basmaOf (bahth o.qaima k) m k = bahth m.qaima k := by
  cases hk : bahth m.qaima k with
  | some v => exact ray_hadir basmaOf _ m k v hk
  | none =>
    unfold ray
    rw [hk]
    cases ho : bahth o.qaima k with
    | none => rfl
    | some w =>
      simp only
      have hn := damj_nuqta basmaOf o a b m hm k
      rw [hk] at hn
      unfold damjMiftah at hn
      rw [ho] at hn
      obtain ⟨_, _, _, _, hsh⟩ := damj_some basmaOf o a b m hm
      have hx : ∃ s ∈ a.mahdhufa ++ b.mahdhufa, s.miftah = k ∧ sahih basmaOf w s = true := by
        rcases damj1_la_ikhtira _ _ _ _ hn with ha | hb
        · obtain ⟨_, s, hs, hsk, hsa⟩ := ray_ghaib_sahih basmaOf w a k ha.symm
          exact ⟨s, List.mem_append_left _ hs, hsk, hsa⟩
        · obtain ⟨_, s, hs, hsk, hsa⟩ := ray_ghaib_sahih basmaOf w b k hb.symm
          exact ⟨s, List.mem_append_right _ hs, hsk, hsa⟩
      obtain ⟨s, hs, hsk, hsa⟩ := hx
      have hmem : s ∈ m.mahdhufa := by
        rw [hsh]
        unfold shawahidBaqiya
        rw [List.mem_filter]
        refine ⟨hs, ?_⟩
        rw [hsk, hk, ho]
        simp [hsa]
      have : hadhfMaadhun basmaOf m k w = true :=
        List.any_eq_true.mpr ⟨s, hmem, by rw [Bool.and_eq_true, beq_iff_eq]; exact ⟨hsk, hsa⟩⟩
      rw [ite_eq_left this]

/-- **المحذوفُ بشاهدٍ لا يعود**: ما حُذف بشاهدٍ صحيح في دمجٍ يبقى محذوفًا إن دُمج الناتجُ بعدُ بطرفٍ لم يغيّره. -/
theorem hadhf_yabqa (basmaOf : V → String) (o a b c : Nuskha K V) (m m' : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (hm' : damj basmaOf o m c = some m') (k : K)
    (hk : bahth m.qaima k = none) (hc : ray basmaOf (bahth o.qaima k) c k = bahth o.qaima k) :
    bahth m'.qaima k = none := by
  have h := damj_nuqta basmaOf o m c m' hm' k
  unfold damjMiftah at h
  rw [ray_damj basmaOf o a b m hm k, hk, hc, damj1_janib_wahid] at h
  exact (Natija.qima.inj h).symm

/-- **التناظر**: الدمجُ لا يفضّل طرفًا — قبولُه واحدٌ بالترتيبين، وقيمُه واحدةٌ في كلّ مفتاح. -/
theorem damj_tanazur (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) :
    ∃ m', damj basmaOf o b a = some m' ∧ ∀ k, bahth m'.qaima k = bahth m.qaima k := by
  have hs : ∀ k, damjMiftah basmaOf o b a k = damjMiftah basmaOf o a b k := fun k => by
    unfold damjMiftah; exact damj1_tanazur _ _ _
  obtain ⟨⟨h1, h2, h3⟩, _⟩ := (damj_maqbul_iff basmaOf o a b).mp ⟨m, hm⟩
  obtain ⟨m', hm'⟩ := (damj_maqbul_iff basmaOf o b a).mpr ⟨⟨h1, h3, h2⟩, fun k h => by
    rw [hs k, damj_nuqta basmaOf o a b m hm k] at h; cases h⟩
  refine ⟨m', hm', fun k => ?_⟩
  have h1 := damj_nuqta basmaOf o b a m' hm' k
  rw [hs k, damj_nuqta basmaOf o a b m hm k] at h1
  exact (Natija.qima.inj h1).symm

/-- **التكرار**: دمجُ طرفٍ بنفسه لا يتعارض (متى خلت المدخلات من التكرار)، ونتيجتُه رأيُه هو. -/
theorem damj_tikrar (basmaOf : V → String) (o a : Nuskha K V) (ho : bilaTakrar o = true) (ha : bilaTakrar a = true) :
    ∃ m, damj basmaOf o a a = some m ∧ ∀ k, bahth m.qaima k = ray basmaOf (bahth o.qaima k) a k := by
  have hk : ∀ k, damjMiftah basmaOf o a a k = .qima (ray basmaOf (bahth o.qaima k) a k) := fun k =>
    damj1_tikrar _ _
  obtain ⟨m, hm⟩ := (damj_maqbul_iff basmaOf o a a).mpr ⟨⟨ho, ha, ha⟩, fun k h => by rw [hk k] at h; cases h⟩
  refine ⟨m, hm, fun k => ?_⟩
  have := damj_nuqta basmaOf o a a m hm k
  rw [hk k] at this; exact (Natija.qima.inj this).symm

/-- **الطرفُ الواحد**: إن لم يغيّر أحدُ الطرفين شيئًا فالدمجُ رأيُ الآخر، بلا تعارض. -/
theorem damj_janib_wahid (basmaOf : V → String) (o a : Nuskha K V) (ho : bilaTakrar o = true)
    (ha : bilaTakrar a = true) :
    ∃ m, damj basmaOf o a ⟨o.qaima, []⟩ = some m ∧ ∀ k, bahth m.qaima k = ray basmaOf (bahth o.qaima k) a k := by
  have hk : ∀ k, damjMiftah basmaOf o a ⟨o.qaima, []⟩ k = .qima (ray basmaOf (bahth o.qaima k) a k) := fun k => by
    unfold damjMiftah; rw [ray_asas]; exact damj1_janib_wahid _ _
  obtain ⟨m, hm⟩ := (damj_maqbul_iff basmaOf o a ⟨o.qaima, []⟩).mpr
    ⟨⟨ho, ha, ho⟩, fun k h => by rw [hk k] at h; cases h⟩
  refine ⟨m, hm, fun k => ?_⟩
  have := damj_nuqta basmaOf o a ⟨o.qaima, []⟩ m hm k
  rw [hk k] at this; exact (Natija.qima.inj this).symm

/-- **لا فقدَ لمفتاح الأساس بلا شاهد** (حادثةُ #35، feb12a8: مفاتيحُ في الأساس خلا منها طرفٌ بلا شاهد): مفتاحٌ في الأساس غاب
    عن الدمج المقبول ⇒ طرفٌ خلا منه وفيه شاهدُ حذفٍ صحيحٌ لهذا المفتاح على تعريف الأساس. -/
theorem la_faqd (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) (w : V)
    (ho : bahth o.qaima k = some w) (hk : bahth m.qaima k = none) :
    (bahth a.qaima k = none ∧
      ∃ s ∈ a.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") ∨
    (bahth b.qaima k = none ∧
      ∃ s ∈ b.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") := by
  have h := damj_nuqta basmaOf o a b m hm k
  rw [hk] at h
  unfold damjMiftah at h
  rw [ho] at h
  rcases damj1_la_ikhtira _ _ _ _ h with ha | hb
  · exact Or.inl (ray_ghaib basmaOf w a k ha.symm)
  · exact Or.inr (ray_ghaib basmaOf w b k hb.symm)

/-- **لا فقدَ لقيدِ طرفٍ بلا شاهد** (حادثةُ 767e09b: إضافاتُ main غابت لأنّ الطرف الآخر خلا منها): قيدٌ في الطرف a غاب عن الدمج
    المقبول ⇒ كان في الأساس بقيمته نفسِها (لم يغيّره a)، والطرفُ الآخر خلا منه وفيه شاهدُ حذفٍ صحيحٌ عليه. فالإضافةُ لا تضيع أبدًا. -/
theorem la_faqd_janib (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) (v : V)
    (ha : bahth a.qaima k = some v) (hk : bahth m.qaima k = none) :
    bahth o.qaima k = some v ∧ bahth b.qaima k = none ∧
      ∃ s ∈ b.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf v ∧ s.sabab ≠ "" ∧ s.idhn ≠ "" := by
  have h := damj_nuqta basmaOf o a b m hm k
  rw [hk] at h
  unfold damjMiftah at h
  rw [ray_hadir basmaOf _ a k v ha] at h
  obtain ⟨hov, hb⟩ := damj1_ghaib _ _ _ (by simp) h
  rw [← hov] at hb
  obtain ⟨h1, h2⟩ := ray_ghaib basmaOf v b k hb
  exact ⟨hov.symm, h1, h2⟩

/-- **لا اختلاق**: كلّ قيمةٍ في الدمج المقبول قيمتُها في الأساس أو في أحد الطرفين. -/
theorem la_ikhtira (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) (v : V) (h : bahth m.qaima k = some v) :
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

/-- **التجميع**: (a ⊔ b) ⊔ c و a ⊔ (b ⊔ c) على أساسٍ واحد يُقبلان معًا أو يُرفضان معًا، وقيمُهما واحدةٌ في كلّ مفتاح. -/
theorem damj_tajmii (basmaOf : V → String) (o a b c : Nuskha K V) :
    ((damj basmaOf o a b).bind fun ab => damj basmaOf o ab c).isSome =
      ((damj basmaOf o b c).bind fun bc => damj basmaOf o a bc).isSome ∧
    ∀ l r, (damj basmaOf o a b).bind (fun ab => damj basmaOf o ab c) = some l →
      (damj basmaOf o b c).bind (fun bc => damj basmaOf o a bc) = some r →
      ∀ k, bahth l.qaima k = bahth r.qaima k := by
  -- النتيجةُ المركّبة لكلّ مفتاح، من الجهتين، واحدةٌ بـ damj1_tajmii
  let O := fun k => bahth o.qaima k
  let NY := fun k => natijaThumma (O k) (damjMiftah basmaOf o a b k) (ray basmaOf (O k) c k)
  let NQ := fun k => natijaQabl (O k) (ray basmaOf (O k) a k) (damjMiftah basmaOf o b c k)
  have hsawa : ∀ k, NY k = NQ k := fun k => damj1_tajmii _ _ _ _
  -- الجهةُ اليسرى: قبولُها ⟺ لا تكرار ولا تعارض في NY، وقيمُها قيمُ NY
  have yasar : ∀ l, (damj basmaOf o a b).bind (fun ab => damj basmaOf o ab c) = some l →
      (bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true ∧ bilaTakrar c = true) ∧
        ∀ k, NY k = .qima (bahth l.qaima k) := by
    intro l h
    cases hab : damj basmaOf o a b with
    | none => rw [hab] at h; cases h
    | some ab =>
      rw [hab] at h
      simp only [Option.bind_some] at h
      obtain ⟨h1, h2, h3, _, _⟩ := damj_some basmaOf o a b ab hab
      obtain ⟨_, _, h4, _, _⟩ := damj_some basmaOf o ab c l h
      refine ⟨⟨h1, h2, h3, h4⟩, fun k => ?_⟩
      have e1 := damj_nuqta basmaOf o a b ab hab k
      have e2 := damj_nuqta basmaOf o ab c l h k
      unfold damjMiftah at e2
      rw [ray_damj basmaOf o a b ab hab k] at e2
      show natijaThumma (O k) (damjMiftah basmaOf o a b k) (ray basmaOf (O k) c k) = _
      rw [e1]; exact e2
  have yasar' : (bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true ∧ bilaTakrar c = true) →
      (∀ k, NY k ≠ .taarud) → ∃ l, (damj basmaOf o a b).bind (fun ab => damj basmaOf o ab c) = some l := by
    rintro ⟨h1, h2, h3, h4⟩ hn
    obtain ⟨ab, hab⟩ := (damj_maqbul_iff basmaOf o a b).mpr ⟨⟨h1, h2, h3⟩, fun k ht => hn k (by
      show natijaThumma _ (damjMiftah basmaOf o a b k) _ = _
      rw [ht]; rfl)⟩
    obtain ⟨l, hl⟩ := (damj_maqbul_iff basmaOf o ab c).mpr ⟨⟨h1, damj_bilaTakrar basmaOf o a b ab hab, h4⟩,
      fun k ht => hn k (by
        show natijaThumma _ (damjMiftah basmaOf o a b k) _ = _
        unfold damjMiftah at ht
        rw [ray_damj basmaOf o a b ab hab k] at ht
        rw [damj_nuqta basmaOf o a b ab hab k]; exact ht)⟩
    exact ⟨l, by rw [hab]; exact hl⟩
  -- الجهةُ اليمنى بالمثل على NQ
  have yamin : ∀ r, (damj basmaOf o b c).bind (fun bc => damj basmaOf o a bc) = some r →
      (bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true ∧ bilaTakrar c = true) ∧
        ∀ k, NQ k = .qima (bahth r.qaima k) := by
    intro r h
    cases hbc : damj basmaOf o b c with
    | none => rw [hbc] at h; cases h
    | some bc =>
      rw [hbc] at h
      simp only [Option.bind_some] at h
      obtain ⟨h1, h3, h4, _, _⟩ := damj_some basmaOf o b c bc hbc
      obtain ⟨_, h2, _, _, _⟩ := damj_some basmaOf o a bc r h
      refine ⟨⟨h1, h2, h3, h4⟩, fun k => ?_⟩
      have e1 := damj_nuqta basmaOf o b c bc hbc k
      have e2 := damj_nuqta basmaOf o a bc r h k
      unfold damjMiftah at e2
      rw [ray_damj basmaOf o b c bc hbc k] at e2
      show natijaQabl (O k) (ray basmaOf (O k) a k) (damjMiftah basmaOf o b c k) = _
      rw [e1]; exact e2
  have yamin' : (bilaTakrar o = true ∧ bilaTakrar a = true ∧ bilaTakrar b = true ∧ bilaTakrar c = true) →
      (∀ k, NQ k ≠ .taarud) → ∃ r, (damj basmaOf o b c).bind (fun bc => damj basmaOf o a bc) = some r := by
    rintro ⟨h1, h2, h3, h4⟩ hn
    obtain ⟨bc, hbc⟩ := (damj_maqbul_iff basmaOf o b c).mpr ⟨⟨h1, h3, h4⟩, fun k ht => hn k (by
      show natijaQabl _ _ (damjMiftah basmaOf o b c k) = _
      rw [ht]; rfl)⟩
    obtain ⟨r, hr⟩ := (damj_maqbul_iff basmaOf o a bc).mpr ⟨⟨h1, h2, damj_bilaTakrar basmaOf o b c bc hbc⟩,
      fun k ht => hn k (by
        show natijaQabl _ _ (damjMiftah basmaOf o b c k) = _
        unfold damjMiftah at ht
        rw [ray_damj basmaOf o b c bc hbc k] at ht
        rw [damj_nuqta basmaOf o b c bc hbc k]; exact ht)⟩
    exact ⟨r, by rw [hbc]; exact hr⟩
  refine ⟨?_, fun l r hl hr k => ?_⟩
  · apply Bool.eq_iff_iff.mpr
    rw [Option.isSome_iff_exists, Option.isSome_iff_exists]
    constructor
    · rintro ⟨l, hl⟩
      obtain ⟨ht, hv⟩ := yasar l hl
      exact yamin' ht (fun k h => by rw [← hsawa k, hv k] at h; cases h)
    · rintro ⟨r, hr⟩
      obtain ⟨ht, hv⟩ := yamin r hr
      exact yasar' ht (fun k h => by rw [hsawa k, hv k] at h; cases h)
  · have h1 := (yasar l hl).2 k
    have h2 := (yamin r hr).2 k
    rw [hsawa k, h2] at h1
    exact (Natija.qima.inj h1).symm

/-- **سلامةُ الدمج** (الجامعة): الدمجُ المقبول لا يفقد مفتاحًا بلا شاهد، ولا يختلق قيمة، ويأخذ ما اتّفق عليه الطرفان، ويأخذ
    تغييرَ الطرف الذي غيّر حين لم يغيّر الآخر — أيًّا كان الطرفُ الذي لم يغيّر. -/
theorem salamat_damj (basmaOf : V → String) (o a b : Nuskha K V) (m : Nuskha K V)
    (hm : damj basmaOf o a b = some m) (k : K) :
    (∀ w, bahth o.qaima k = some w → bahth m.qaima k = none →
      (bahth a.qaima k = none ∧
        ∃ s ∈ a.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "") ∨
      (bahth b.qaima k = none ∧
        ∃ s ∈ b.mahdhufa, s.miftah = k ∧ s.basma ≠ "" ∧ s.basma = basmaOf w ∧ s.sabab ≠ "" ∧ s.idhn ≠ "")) ∧
    (∀ v, bahth m.qaima k = some v →
      bahth o.qaima k = some v ∨ bahth a.qaima k = some v ∨ bahth b.qaima k = some v) ∧
    (ray basmaOf (bahth o.qaima k) a k = ray basmaOf (bahth o.qaima k) b k →
      bahth m.qaima k = ray basmaOf (bahth o.qaima k) a k) ∧
    (ray basmaOf (bahth o.qaima k) b k = bahth o.qaima k →
      bahth m.qaima k = ray basmaOf (bahth o.qaima k) a k) ∧
    (ray basmaOf (bahth o.qaima k) a k = bahth o.qaima k →
      bahth m.qaima k = ray basmaOf (bahth o.qaima k) b k) := by
  have hn := damj_nuqta basmaOf o a b m hm k
  unfold damjMiftah at hn
  refine ⟨fun w ho hk => la_faqd basmaOf o a b m hm k w ho hk,
          fun v h => la_ikhtira basmaOf o a b m hm k v h, fun he => ?_, fun he => ?_, fun he => ?_⟩
  · rw [he, damj1_tikrar] at hn; rw [he]; exact (Natija.qima.inj hn).symm
  · rw [he, damj1_janib_wahid] at hn; exact (Natija.qima.inj hn).symm
  · rw [he, damj1_tanazur, damj1_janib_wahid] at hn; exact (Natija.qima.inj hn).symm

end

/-! ## ٧. المثالان: قائمةُ الطفرات وأسماءُ المبرهنات المحميّة، وشواهدُ الحادثتين -/

/-- قيدُ طفرةٍ بلا اسمه (الاسمُ مفتاح). -/
structure Tafra where
  milaf : String
  min : String
  ila : String
deriving DecidableEq, Repr

/-- بصمةُ الطفرة في النموذج: تسلسلُها نصًّا (تمثيلٌ لا SHA-256؛ وتبايُنُه مفترضٌ لا مبرهن — حقلٌ فيه فاصلةُ الجدولة قد
    يصطدم بغيره؛ البصمةُ الحقيقيّة في المرحلة الثانية). -/
def basmaTafra (t : Tafra) : String := t.milaf ++ "\t" ++ t.min ++ "\t" ++ t.ila

/-- أسماءُ المبرهنات المحميّة: الاسمُ مفتاح، والقيمةُ بصمةُ نصّ المبرهنة (تُحسب في المرحلة الثانية)، فبصمتُها هي نفسُها. -/
def basmaNass (s : String) : String := s

def tA : Tafra := ⟨"A.lean", "x", "y"⟩
def tB : Tafra := ⟨"B.lean", "p", "q"⟩
def tC : Tafra := ⟨"C.lean", "u", "v"⟩
def tA' : Tafra := ⟨"A.lean", "x", "z"⟩

/-- قيمُ الناتج في مفاتيحَ مسمّاة (للشواهد). -/
def qiyam {V : Type} (m : Option (Nuskha String V)) (ks : List String) : Option (List (Option V)) :=
  m.map fun n => ks.map (bahth n.qaima)

/-- **حادثةُ #35 (feb12a8) بنموذجها** (على الشاهد): في الأساس P150_tadammun_ala_ghayr_juz؛ الفرعُ خلا منه بلا شاهد؛ main أبقاه
    وأضاف P163_khatt_asas_fail_open. الدمجُ النصّيّ حمل الحذفَ بلا تعارض؛ وهنا يبقى الاثنان. -/
theorem shahid_hadith_35 :
    qiyam (damj basmaTafra ⟨[("P150_tadammun_ala_ghayr_juz", tA)], []⟩ ⟨[], []⟩
      ⟨[("P150_tadammun_ala_ghayr_juz", tA), ("P163_khatt_asas_fail_open", tB)], []⟩)
      ["P150_tadammun_ala_ghayr_juz", "P163_khatt_asas_fail_open"] = some [some tA, some tB] := by
  decide +kernel

/-- **حادثةُ 767e09b بنموذجها** (على الشاهد): أضاف الفرعُ P152_joinTrailing_bila_fasil وأضاف main ‏P163_khatt_asas_fail_open على
    أساسٍ خلا منهما؛ الدمجُ النصّيّ حلّ كتلةَ التعارض بأخذ طرفٍ كلِّه فضاعت إضافاتُ main؛ وهنا تبقى الإضافتان. -/
theorem shahid_hadith_767e09b :
    qiyam (damj basmaTafra ⟨[("P150_adj_tabdil_or_and", tA)], []⟩
      ⟨[("P150_adj_tabdil_or_and", tA), ("P152_joinTrailing_bila_fasil", tC)], []⟩
      ⟨[("P150_adj_tabdil_or_and", tA), ("P163_khatt_asas_fail_open", tB)], []⟩)
      ["P150_adj_tabdil_or_and", "P152_joinTrailing_bila_fasil", "P163_khatt_asas_fail_open"] =
      some [some tA, some tC, some tB] := by
  decide +kernel

/-- **شاهدُ الحذف** (على الشاهد): حذفٌ بشاهدٍ صحيحٍ يُحذف؛ وغيابٌ بلا شاهد، أو بشاهدٍ لتعريفٍ آخر، أو لمفتاحٍ آخر، أو بلا
    سبب، أو بلا إذن، لا يحذف. -/
theorem shawahid_hadhf :
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩)
      ["P1"] = some [none] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], []⟩ ⟨[("P1", tA)], []⟩) ["P1"] = some [some tA] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tB, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩)
      ["P1"] = some [some tA] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P2", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩)
      ["P1"] = some [some tA] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩)
      ["P1"] = some [some tA] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", ""⟩]⟩ ⟨[("P1", tA)], []⟩)
      ["P1"] = some [some tA] := by
  decide +kernel

/-- **المحذوفُ لا يعود** (على الشاهد): ناتجُ حذفٍ بشاهدٍ يحمل شاهدَه، فدمجُه بفرعٍ تفرّع قبل الحذف لا يعيد المحذوف. -/
theorem shahid_hadhf_la_yaud :
    ((damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA)], []⟩).bind
      fun m => damj basmaTafra ⟨[("P1", tA)], []⟩ m ⟨[("P1", tA)], []⟩).map (fun n => bahth n.qaima "P1") =
      some none := by
  decide +kernel

/-- **تعارضٌ مسمًّى** (على الشاهد): حذفٌ مقابلَ تعديل، وتعديلان مختلفان، يُسقطان الدمج ويُسمّى المفتاح؛ وتعديلٌ واحدٌ يؤخذ؛
    ومفتاحٌ مكرَّرٌ في طرفٍ يُسقطه. -/
theorem shawahid_taarud :
    damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[], [⟨"P1", basmaTafra tA, "حُذف الكود", "المالك"⟩]⟩ ⟨[("P1", tA')], []⟩ = none ∧
    damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[("P1", tA')], []⟩ ⟨[("P1", tB)], []⟩ = none ∧
    mutaarida basmaTafra ⟨[("P1", tA), ("P2", tB)], []⟩ ⟨[("P1", tA'), ("P2", tB)], []⟩ ⟨[("P1", tB), ("P2", tB)], []⟩ =
      ["P1"] ∧
    qiyam (damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[("P1", tA')], []⟩ ⟨[("P1", tA)], []⟩) ["P1"] = some [some tA'] ∧
    damj basmaTafra ⟨[("P1", tA)], []⟩ ⟨[("P1", tA), ("P1", tB)], []⟩ ⟨[("P1", tA)], []⟩ = none := by
  decide +kernel

/-- **أسماءُ المبرهنات المحميّة** (على الشاهد): اسمٌ غاب عن طرفٍ بلا شاهدٍ يبقى؛ وبشاهدٍ ببصمة نصّه وإذنٍ يُحذف؛ وقيمةٌ
    بصمتُها فارغةٌ لا يحذفها شاهدٌ فارغ. -/
theorem shawahid_mubarhanat :
    qiyam (damj basmaNass ⟨[("Idaa.sijill_faregh", "n1")], []⟩ ⟨[], []⟩ ⟨[("Idaa.sijill_faregh", "n1")], []⟩)
      ["Idaa.sijill_faregh"] = some [some "n1"] ∧
    qiyam (damj basmaNass ⟨[("Idaa.sijill_faregh", "n1")], []⟩ ⟨[], [⟨"Idaa.sijill_faregh", "n1", "استُبدلت", "المالك"⟩]⟩
      ⟨[("Idaa.sijill_faregh", "n1")], []⟩) ["Idaa.sijill_faregh"] = some [none] ∧
    qiyam (damj basmaNass ⟨[("T", "")], []⟩ ⟨[], [⟨"T", "", "س", "إ"⟩]⟩ ⟨[("T", "")], []⟩) ["T"] = some [some ""] := by
  decide +kernel

end Damj
end Nizam
