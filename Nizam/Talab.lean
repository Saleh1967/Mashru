/-
  Nizam/Talab.lean — قرار المالك ٢ (2026-10-18، 19:39): «الأمر والالتماس والسؤال "لا حكم" بلا مقام».

  السند (ج3 س415، ترقيم `scripts/tahwil_docx.py`): «وإن كان الطلب لتحصيل الماهية مع الاستعلاء على المطلوب منه فهو الأمر …
  وإن كان الطلب لتحصيل الماهية مع التساوي فهو الالتماس، كطلب الشخص من نظيره كقولك لصديقك: أعطني الكتاب … وإن كان الطلب
  لتحصيل الماهية مع التسفل، أي التذلل، فهو السؤال». فالفارقُ بين الثلاثة رتبةُ المتكلّم من المخاطَب، وهي من المقام لا من اللفظ؛
  والصيغةُ الواحدة («افعل») تقع في الثلاثة. ومن اللفظ وحده يُرخَّص «طلبُ تحصيل الماهية» (`talabMinSigha`)، والقسمةُ الثلاثيّة
  «لا حكم» حتّى يُودَع المقام (`la_qisma_bila_maqam`)؛ ولا دالّةَ من الصيغة وحدها تستردّ القسم (`la_dalla_min_sigha`) — على
  نمط `Jisr.QiraaSimat.la_dalla_tasturidd`.
  التعيينُ المعلن: الصيغةُ هنا مجرّدةٌ (`Sigha` بنوعٍ واحدٍ لصيغة الطلب)؛ ربطُها بخلايا القارئ لم يُبنَ (م٤ في البروتوكول).
  بلا sorry ولا axiom ولا native_decide.
-/
import Nizam.Asas

namespace Nizam.Talab

/-- رتبةُ المتكلّم من المخاطَب (ج3 س415): استعلاءٌ أو تساوٍ أو تسفّل. وهي من المقام. -/
inductive Rutba | istila | tasawi | tasafful
  deriving DecidableEq, Repr

/-- أقسامُ الطلب لتحصيل الماهية الثلاثة. -/
inductive Qism | amr | iltimas | sual
  deriving DecidableEq, Repr

/-- صيغةُ الطلب لتحصيل الماهية («افعل»)، مجرّدةً عن خلاياها. -/
inductive Sigha | ifal
  deriving DecidableEq, Repr

/-- ما يرخّصه اللفظ وحده: طلبُ تحصيل الماهية، لا أكثر. -/
inductive Madlul | talabTahsil
  deriving DecidableEq, Repr

def talabMinSigha : Jisr Sigha Madlul := fun _ => .murakhkhas .talabTahsil

/-- القسمُ بالرتبة (س415). -/
def qismBiRutba : Rutba → Qism
  | .istila => .amr
  | .tasawi => .iltimas
  | .tasafful => .sual

/-- القسمةُ الثلاثيّة: بمقامٍ مودَعٍ (رتبةٍ) تُرخَّص، وبلا مقامٍ لا حكم. -/
def qisma (maqam : Option Rutba) : Jisr Madlul Qism := fun _ =>
  match maqam with
  | some r => .murakhkhas (qismBiRutba r)
  | none => .laHukm

/-- بلا مقام: من الصيغة إلى القسم «لا حكم»، لا امتناع ولا ترخيص. -/
theorem la_qisma_bila_maqam (s : Sigha) : tarkib talabMinSigha (qisma none) s = .laHukm := rfl

/-- وبمقامٍ مودَعٍ يُرخَّص القسمُ الذي تعيّنه الرتبة. -/
theorem qisma_bil_maqam (s : Sigha) (r : Rutba) :
    tarkib talabMinSigha (qisma (some r)) s = .murakhkhas (qismBiRutba r) := rfl

/-- ولا دالّةَ من الصيغة وحدها تطابق القسمةَ في كلّ مقام: الصيغةُ الواحدة تقع في الثلاثة. -/
theorem la_dalla_min_sigha : ¬ ∃ f : Sigha → Qism, ∀ r, f .ifal = qismBiRutba r := by
  rintro ⟨f, hf⟩
  have h1 := hf .istila
  have h2 := hf .tasawi
  rw [h1] at h2
  cases h2

/-- والقسمةُ بالرتبة متباينة: كلُّ رتبةٍ قسمٌ مختلف (فالمقامُ وحده يفرّق). -/
theorem qismBiRutba_mutabayin (r₁ r₂ : Rutba) (h : qismBiRutba r₁ = qismBiRutba r₂) : r₁ = r₂ := by
  cases r₁ <;> cases r₂ <;> first | rfl | cases h

end Nizam.Talab
