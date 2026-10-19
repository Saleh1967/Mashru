/-
  Dal/Tamthil.lean — ثباتُ التمثيل: تبديلُ الترميز بترميزٍ لا يفقد شيئًا لا يغيّر عمل الآلة — حالتَها الأخيرة، ومجموعَ
  أوزانها، وقبولَها — ثمّ تطبيقُه على ترميز الخلية `Dal.Khaliya` إلى رقمها في `Fin 116` بالاتّجاهين.

  السند: وثيقةٌ رفعها المالك (2026-10-19) بعنوان «Representation-Invariance & Semantic Preservation»، بقوله: «تغيير جوهري
  يجب برهانه واعتماده … برهن ذلك او اعتذر عن البرهان». شيفرتها كما رُفعت لم تُبنَ: خطآن في البرهانين، لا في القضيّة —
  `weight_preserved`: ‏`simp only [… transport …]` فكّ التعريف داخل الحدّ التكراريّ فلم يجد `rw [ih]` نمطه (أُصلح بحقائق
  `have` معزولة ثمّ `show` ثمّ `rw` مرتّب)؛ و`acceptance_preserved`: ‏`rw` لم يُغلق هدفًا مساويًا بالتعريف وحده (أُصلح
  بـ `congrArg`). بُنيت مُصلحةً خارج المستودع، وأذن المالك بنقلها (2026-10-19 16:11: «أوافق على نقل المبرهنات وفق افضل
  الممارسات للمشروع»). وصُحِّح جدولُ المقابلة في الوثيقة: آلاتُ `SLGE.Law` (δ، ω، run) تعمل على الأعداد مباشرةً فلا تمثيلَ
  ثانيًا لها اليوم تنقله القضيّة؛ و`SLGE.Core.decS_encS` ترميزٌ آخر (قائمة أعداد إلى عدد) لا ترميزُ الخلية؛ والمقابلُ
  الصحيح على مستوى الخلية `Dal.n`/`Dal.fakk` بمبرهنتيهما `fakk_n` و`n_fakk`.

  الحدّ (معلَن): القضيّة عامّة؛ وتطبيقها هنا على الخلية ورقمها وحده. وصلُها بقارئ المحرّك أو بآلات SLGE لم يُبنَ.
-/
import Dal.Khaliya

namespace Dal
namespace Tamthil

universe u v
variable {U : Type u} {B : Type v}

/-- ترميزٌ لا يفقد شيئًا: الفكُّ بعد الطيّ يعيد الأصل. -/
structure Tarmiz (U : Type u) (B : Type v) where
  tayy : U → B
  fakk : B → U
  fakk_tayy : ∀ x : U, fakk (tayy x) = x

/-- آلةٌ على أبجديّة U: انتقالٌ، ووزنٌ لكلّ خطوة، وقبولٌ للحالة. -/
structure Ala (U : Type u) where
  Hala : Type
  khatwa : Hala → U → Hala
  wazn : Hala → U → Nat
  qubul : Hala → Bool

/-- تشغيلُ الآلة على كلمة: الحالة الأخيرة. -/
def tashghil (M : Ala U) : M.Hala → List U → M.Hala
  | q, [] => q
  | q, x :: xs => tashghil M (M.khatwa q x) xs

/-- مجموعُ الأوزان على الكلمة. -/
def majmuWazn (M : Ala U) : M.Hala → List U → Nat
  | _, [] => 0
  | q, x :: xs => M.wazn q x + majmuWazn M (M.khatwa q x) xs

/-- نقلُ الآلة إلى الأبجديّة المرمَّزة: تفكّ الرمز ثمّ تعمل كما كانت. -/
def naql (M : Ala U) (E : Tarmiz U B) : Ala B :=
  { Hala := M.Hala
    khatwa := fun q b => M.khatwa q (E.fakk b)
    wazn := fun q b => M.wazn q (E.fakk b)
    qubul := M.qubul }

/-- **النقلُ يحفظ التشغيل**: الآلة المنقولة على الكلمة المرمَّزة تنتهي إلى الحالة نفسِها. -/
theorem naql_yahfaz_tashghil (M : Ala U) (E : Tarmiz U B) (q : M.Hala) (xs : List U) :
    tashghil (naql M E) q (xs.map E.tayy) = tashghil M q xs := by
  induction xs generalizing q with
  | nil => rfl
  | cons x xs ih =>
      simp only [List.map_cons, tashghil, naql, E.fakk_tayy]
      exact ih (M.khatwa q x)

/-- **النقلُ يحفظ مجموع الأوزان**. -/
theorem naql_yahfaz_wazn (M : Ala U) (E : Tarmiz U B) (q : M.Hala) (xs : List U) :
    majmuWazn (naql M E) q (xs.map E.tayy) = majmuWazn M q xs := by
  induction xs generalizing q with
  | nil => rfl
  | cons x xs ih =>
      have hk : (naql M E).khatwa q (E.tayy x) = M.khatwa q x := by
        simp [naql, E.fakk_tayy]
      have hw : (naql M E).wazn q (E.tayy x) = M.wazn q x := by
        simp [naql, E.fakk_tayy]
      show (naql M E).wazn q (E.tayy x)
             + majmuWazn (naql M E) ((naql M E).khatwa q (E.tayy x)) (xs.map E.tayy)
           = M.wazn q x + majmuWazn M (M.khatwa q x) xs
      rw [hw, hk, ih]

/-- **النقلُ يحفظ القبول**. -/
theorem naql_yahfaz_qubul (M : Ala U) (E : Tarmiz U B) (q : M.Hala) (xs : List U) :
    (naql M E).qubul (tashghil (naql M E) q (xs.map E.tayy)) = M.qubul (tashghil M q xs) :=
  congrArg M.qubul (naql_yahfaz_tashghil M E q xs)

/-! ## التطبيق على الخلية ورقمها (Dal/Khaliya.lean) -/

/-- الخليةُ إلى رقمها: ترميزٌ لا يفقد (`fakk_n`). -/
def tarmizKhaliya : Tarmiz Khaliya (Fin 116) := ⟨Dal.n, Dal.fakk, fakk_n⟩

/-- والرقمُ إلى خليته: ترميزٌ لا يفقد أيضًا (`n_fakk`)؛ فالتمثيلان متكافئان في الاتّجاهين. -/
def tarmizRaqm : Tarmiz (Fin 116) Khaliya := ⟨Dal.fakk, Dal.n, n_fakk⟩

/-- **أيُّ آلةٍ على الخلايا تعمل على أرقامها عملَها نفسَه**: الحالة الأخيرة والأوزان والقبول سواء. -/
theorem khaliya_raqm_sawa (M : Ala Khaliya) (q : M.Hala) (xs : List Khaliya) :
    tashghil (naql M tarmizKhaliya) q (xs.map Dal.n) = tashghil M q xs ∧
    majmuWazn (naql M tarmizKhaliya) q (xs.map Dal.n) = majmuWazn M q xs ∧
    (naql M tarmizKhaliya).qubul (tashghil (naql M tarmizKhaliya) q (xs.map Dal.n)) = M.qubul (tashghil M q xs) :=
  ⟨naql_yahfaz_tashghil M tarmizKhaliya q xs, naql_yahfaz_wazn M tarmizKhaliya q xs,
   naql_yahfaz_qubul M tarmizKhaliya q xs⟩

/-- **وبالعكس**: أيُّ آلةٍ على الأرقام تعمل على خلاياها عملَها نفسَه. -/
theorem raqm_khaliya_sawa (M : Ala (Fin 116)) (q : M.Hala) (xs : List (Fin 116)) :
    tashghil (naql M tarmizRaqm) q (xs.map Dal.fakk) = tashghil M q xs ∧
    majmuWazn (naql M tarmizRaqm) q (xs.map Dal.fakk) = majmuWazn M q xs ∧
    (naql M tarmizRaqm).qubul (tashghil (naql M tarmizRaqm) q (xs.map Dal.fakk)) = M.qubul (tashghil M q xs) :=
  ⟨naql_yahfaz_tashghil M tarmizRaqm q xs, naql_yahfaz_wazn M tarmizRaqm q xs,
   naql_yahfaz_qubul M tarmizRaqm q xs⟩

end Tamthil
end Dal
