/-
  Aql/TalaqqiFikri.lean — شروطُ فهم النصّ الفكريّ (التلقّي الفكريّ) قاعدةً مرخَّصةً متدرّجة.

  الطلب: قولُ المالك في الجلسة 2026-11-22 (20:54 بتوقيت عمّان):
  «إدراك الواقع وتصور المدلول معلومات سابقة بمستوى الموضوع ثلاث شروط للتلقي الفكري اضبط بالترخيص الجبري المتدرج».
  ولفظُ «التلقي الفكري» ليس في الكتاب؛ والنصُّ الذي يعدّ الشروطَ الثلاثة «فهم النص الفكري» في «التفكير»، وجعلُهما
  شيئًا واحدًا قراءةُ البنّاء (والنصُّ نفسُه يقول [210] «لأن فهم الفكر يعني أخذه»).

  السند (أرقامُ فقرات «التفكير» في تحويلٍ نصّيٍّ رفعه المالك في الجلسة؛ تُستعمل كما في `Aql/Muhakat.lean`):
  * [210]: «ومن هنا يشترط في فهم النص الفكري إلى جانب المعلومات السابقة ثلاثة شروط: أحدها أن تكون المعلومات السابقة في
    مستوى الفكر الذي يراد فهمه، وثانيها أن يدرك واقعها كما هو إدراكاً يحدده ويميزه عن غيره، وثالثها أن يتصور هذا الواقع
    تصوراً صحيحاً يعطي الصورة الحقيقية عنه. وبدون هذه الثلاثة مجتمعة لا يمكن فهم النص الفكري».
  * [204]: «والتفكير في النصوص الفكرية، أي فهمها لا يتأتى إلا بوجود معلومات سابقة عن موضوع النص»؛ و«وإلا فهمت الكلام
    فهماً لغوياً … ولكنه على كل حال ليس فهماً للفكر، وإنما هو فهم لغوي».
  * [209]: «فإذا كانت المعلومات السابقة هي المعلومات اللغوية فإنها لا تكفي إلا إلى التفسير اللغوي ولا تكفي لتفسير الفكر».
  * [211]: «فإنه لا يكفي وجود معلومات سابقة في مستواها، بل لا بد أن يكون إلى جانب ذلك إدراك لواقعها وتصور لمدلولها».
  * [212]: «ولذلك لا بد لفهم النصوص الفكرية من إدراك واقعها وتصور مدلولها، لاتخاذ الموقف اللازم تجاهها، إما الأخذ وإما
    الترك والمحاربة».

  التعيين (البنّاء، معلَن):
  * القضايا ثمانٍ لكلّ فكرٍ `f`: خمسٌ أصولٌ في الرتبة صفر (المعلوماتُ اللغويّة، والمعلوماتُ السابقة عن الموضوع، وكونُها في
    مستوى الفكر، وإدراكُ الواقع، وتصوّرُ المدلول)، والفهمُ اللغويّ والفهمُ الفكريّ في الرتبة ١، والموقفُ في الرتبة ٢.
  * «في مستوى الفكر» أصلٌ مستقلٌّ عن «المعلومات السابقة» وإن كان النصُّ يجعله صفةً لها؛ فقانونُ الفهم الفكريّ يشترطهما معًا.
  * المعلوماتُ اللغويّة ليست مقدّمةً للفهم الفكريّ: النصُّ لا يشترطها في [210]، ومثالُه العربُ «فهموه وأخذوا به، لا لأن
    لغتهم كانت تمكنهم من فهمه». ومن هنا لا يُبنى أنّ الفهمَ الفكريّ يقتضي الفهمَ اللغويّ.
  * الموقفُ (أخذٌ أو تركٌ ومحاربة) قضيّةٌ واحدة: النصُّ يعلّق الموقفَ بالفهم لا تعيينَه أخذًا أو تركًا، فتعيينُه لم يُبنَ.
  * الأصولُ يقرّرها مُدخِلُها (`A`)، وصدقُها لا يُبرهن: «إدراكاً يحدده ويميزه» و«تصوراً صحيحاً» حكمٌ على المتلقّي لا تحمله الصورة.

  الوسم: «لكلّ» لما برهانُه على كلّ فكرٍ وكلّ أصول، و«على الشاهد» لما برهانُه `decide` على مثال. بلا sorry ولا axiom ولا
  native_decide.
-/
import Aql.Qaida

namespace Aql.TalaqqiFikri

open _root_.Qaida

variable {F : Type}

/-- قضايا التلقّي لفكرٍ واحد. -/
inductive Qadiyya (F : Type)
  | lugha (f : F)        -- معلوماتٌ لغويّة: معاني الألفاظ والتراكيب ([204])
  | maalumat (f : F)     -- معلوماتٌ سابقة عن موضوع النصّ ([204])
  | mustawa (f : F)      -- المعلوماتُ السابقة في مستوى الفكر (الشرط الأوّل، [210])
  | waqi (f : F)         -- إدراكُ الواقع يحدّده ويميّزه (الشرط الثاني، [210])
  | tasawwur (f : F)     -- تصوّرُ المدلول تصوّرًا صحيحًا (الشرط الثالث، [210])
  | fahmLughawi (f : F)  -- فهمٌ لغويّ ([204])
  | fahmFikri (f : F)    -- فهمُ الفكر = أخذُه ([210])
  | mawqif (f : F)       -- الموقف: أخذٌ أو تركٌ ومحاربة ([212])
deriving DecidableEq, Repr

open Qadiyya

/-- الرتبة: الأصولُ صفر، والفهمان واحد، والموقفُ اثنان. -/
def rutba : Qadiyya F → Nat
  | lugha _ | maalumat _ | mustawa _ | waqi _ | tasawwur _ => 0
  | fahmLughawi _ | fahmFikri _ => 1
  | mawqif _ => 2

def qLughawi (f : F) : Qanun (Qadiyya F) := ⟨"فهم-لغوي", [lugha f], fahmLughawi f⟩
def qFikri (f : F) : Qanun (Qadiyya F) := ⟨"فهم-فكري", [maalumat f, mustawa f, waqi f, tasawwur f], fahmFikri f⟩
def qMawqif (f : F) : Qanun (Qadiyya F) := ⟨"موقف", [fahmFikri f], mawqif f⟩

/-- قاعدةُ التلقّي للفكر `f`، إصدارُها «talaqqi-0.1». -/
def qaidaOf (f : F) : Qaida (Qadiyya F) := ⟨"talaqqi-0.1", [qLughawi f, qFikri f, qMawqif f]⟩

/-- الأصولُ مقبولةٌ في الرتبة صفر وحدها. -/
def Usul (A : Qadiyya F → Prop) : Prop := ∀ p, A p → rutba p = 0

/-- لكلّ: القاعدةُ متدرّجة (مقدّماتُ كلّ قانونٍ أدنى رتبةً من نتيجته). -/
theorem mutadarrija (f : F) : Mutadarrija (qaidaOf f) rutba := by
  intro r hr
  simp only [qaidaOf, List.mem_cons, List.not_mem_nil, or_false] at hr
  rcases hr with rfl | rfl | rfl
  · refine ⟨by simp [qLughawi], ?_⟩
    intro m hm; simp only [qLughawi, List.mem_singleton] at hm; subst hm; simp [rutba, qLughawi]
  · refine ⟨by simp [qFikri], ?_⟩
    intro m hm; simp only [qFikri, List.mem_cons, List.not_mem_nil, or_false] at hm
    rcases hm with rfl | rfl | rfl | rfl <;> simp [rutba, qFikri]
  · refine ⟨by simp [qMawqif], ?_⟩
    intro m hm; simp only [qMawqif, List.mem_singleton] at hm; subst hm; simp [rutba, qMawqif]

/-- مساعد: ما رتبتُه صفر مرخَّصٌ إذا وفقط إذا كان أصلًا. -/
theorem asl_iff (f : F) (A : Qadiyya F → Prop) {p : Qadiyya F} (h0 : rutba p = 0) :
    Murakhkhas (qaidaOf f) A p ↔ A p :=
  ⟨fun h => rutba_sifr_asl _ rutba A (mutadarrija f) h h0, Murakhkhas.asl⟩

/-- لكلّ: الفهمُ الفكريّ مرخَّصٌ إذا وفقط إذا اجتمعت المعلوماتُ السابقة والشروطُ الثلاثة ([210]: «وبدون هذه الثلاثة
    مجتمعة لا يمكن فهم النص الفكري»)، على أصولٍ في الرتبة صفر. -/
theorem fahm_iff (f : F) (A : Qadiyya F → Prop) (hA : Usul A) :
    Murakhkhas (qaidaOf f) A (fahmFikri f) ↔
      A (maalumat f) ∧ A (mustawa f) ∧ A (waqi f) ∧ A (tasawwur f) := by
  constructor
  · intro h
    have key : ∀ p, Murakhkhas (qaidaOf f) A p → p = fahmFikri f →
        A (maalumat f) ∧ A (mustawa f) ∧ A (waqi f) ∧ A (tasawwur f) := by
      intro p hp he
      cases hp with
      | asl ha => subst he; have := hA _ ha; simp [rutba] at this
      | qanun r hr hm =>
        simp only [qaidaOf, List.mem_cons, List.not_mem_nil, or_false] at hr
        rcases hr with rfl | rfl | rfl
        · simp [qLughawi] at he
        · simp only [qFikri] at hm
          have g : ∀ q, q ∈ [maalumat f, mustawa f, waqi f, tasawwur f] → A q :=
            fun q hq => (asl_iff f A (by simp at hq; rcases hq with rfl | rfl | rfl | rfl <;> rfl)).mp (hm q hq)
          exact ⟨g _ (by simp), g _ (by simp), g _ (by simp), g _ (by simp)⟩
        · simp [qMawqif] at he
    exact key _ h rfl
  · rintro ⟨h1, h2, h3, h4⟩
    refine Murakhkhas.qanun (qFikri f) (by simp [qaidaOf]) ?_
    intro m hm
    simp [qFikri] at hm
    rcases hm with rfl | rfl | rfl | rfl <;> exact Murakhkhas.asl ‹_›

/-- لكلّ: نقصُ أيّ شرطٍ يمنع الفهم الفكريّ. -/
theorem naqs_shart (f : F) (A : Qadiyya F → Prop) (hA : Usul A)
    (h : ¬ A (maalumat f) ∨ ¬ A (mustawa f) ∨ ¬ A (waqi f) ∨ ¬ A (tasawwur f)) :
    ¬ Murakhkhas (qaidaOf f) A (fahmFikri f) := by
  rw [fahm_iff f A hA]
  rintro ⟨h1, h2, h3, h4⟩
  rcases h with h | h | h | h <;> contradiction

/-- لكلّ: المعلوماتُ السابقة في مستواها بلا إدراكٍ للواقع ولا تصوّرٍ للمدلول لا تكفي ([211]). -/
theorem mustawa_la_yakfi (f : F) (A : Qadiyya F → Prop) (hA : Usul A) (hw : ¬ A (waqi f)) :
    ¬ Murakhkhas (qaidaOf f) A (fahmFikri f) :=
  naqs_shart f A hA (Or.inr (Or.inr (Or.inl hw)))

/-- لكلّ: الموقفُ (أخذًا أو تركًا) مرخَّصٌ إذا وفقط إذا رُخِّص الفهمُ الفكريّ ([212]). -/
theorem mawqif_iff (f : F) (A : Qadiyya F → Prop) (hA : Usul A) :
    Murakhkhas (qaidaOf f) A (mawqif f) ↔ Murakhkhas (qaidaOf f) A (fahmFikri f) := by
  constructor
  · intro h
    have key : ∀ p, Murakhkhas (qaidaOf f) A p → p = mawqif f → Murakhkhas (qaidaOf f) A (fahmFikri f) := by
      intro p hp he
      cases hp with
      | asl ha => subst he; have := hA _ ha; simp [rutba] at this
      | qanun r hr hm =>
        simp only [qaidaOf, List.mem_cons, List.not_mem_nil, or_false] at hr
        rcases hr with rfl | rfl | rfl
        · simp [qLughawi] at he
        · simp [qFikri] at he
        · exact hm _ (by simp [qMawqif])
    exact key _ h rfl
  · intro h
    exact Murakhkhas.qanun (qMawqif f) (by simp [qaidaOf]) (by intro m hm; simp [qMawqif] at hm; subst hm; exact h)

/-- لكلّ: من المعلومات اللغويّة والمعلومات عن الموضوع وحدهما يُرخَّص الفهمُ اللغويّ ولا يُرخَّص الفهمُ الفكريّ
    ولا الموقف ([204]، [209]). -/
theorem lughawi_la_yakfi (f : F) :
    let A : Qadiyya F → Prop := fun p => p = lugha f ∨ p = maalumat f
    Murakhkhas (qaidaOf f) A (fahmLughawi f) ∧ ¬ Murakhkhas (qaidaOf f) A (fahmFikri f) ∧
      ¬ Murakhkhas (qaidaOf f) A (mawqif f) := by
  intro A
  have hA : Usul A := by intro p hp; rcases hp with rfl | rfl <;> rfl
  have hnf : ¬ Murakhkhas (qaidaOf f) A (fahmFikri f) :=
    naqs_shart f A hA (Or.inr (Or.inl (by rintro (h | h) <;> cases h)))
  refine ⟨Murakhkhas.qanun (qLughawi f) (by simp [qaidaOf]) ?_, hnf, fun h => hnf ((mawqif_iff f A hA).mp h)⟩
  intro m hm; simp [qLughawi] at hm; subst hm; exact Murakhkhas.asl (Or.inl rfl)

/-! ## الشاهد على الفاحص: نصُّ «الوعي السياسي» ([205]–[206]) -/

/-- الفكرُ المقروء في المثال، باسمه. -/
abbrev wai : String := "الواعي-سياسيا"

def aslKamil : Qadiyya String → Bool
  | maalumat _ | mustawa _ | waqi _ | tasawwur _ | lugha _ => true
  | _ => false

def aslBilaTasawwur : Qadiyya String → Bool
  | tasawwur _ => false
  | p => aslKamil p

def silsilaMawqif : List (Khatwa (Qadiyya String)) :=
  [.asl (maalumat wai), .asl (mustawa wai), .asl (waqi wai), .asl (tasawwur wai), .qanun 1, .qanun 2]

/-- على الشاهد: بالأصول الخمسة تقبل سلسلةُ الموقف، وبلا تصوّر المدلول تُرفض هي وسلسلةُ الفهم، وتبقى سلسلةُ الفهم اللغويّ
    مقبولة، ولا يُقبل الموقفُ أصلًا. -/
theorem shahid_wai :
    maqbul (qaidaOf wai) aslKamil ⟨mawqif wai, silsilaMawqif⟩ = true ∧
    maqbul (qaidaOf wai) aslBilaTasawwur ⟨mawqif wai, silsilaMawqif⟩ = false ∧
    maqbul (qaidaOf wai) aslBilaTasawwur ⟨fahmLughawi wai, [.asl (lugha wai), .qanun 0]⟩ = true ∧
    maqbul (qaidaOf wai) aslKamil ⟨mawqif wai, [.asl (mawqif wai)]⟩ = false := by
  decide

end Aql.TalaqqiFikri
