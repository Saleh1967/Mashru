/-
  Aql/NizamMarifi.lean — العقدُ الناظم: شروطُ المجال الناظم (العقل والتفكير) على كلّ نظامٍ معرفيّ في المشروع.

  الطلب: قولُ المالك في الجلسة (2026-11-24، 14:02 بتوقيت عمّان):
  «بأيّ طلبٍ نبدأ؟ أقترح العقد الناظم. موافق ان يكون العقد الناظم هو الأساس كما  تُودَع قسمة تغطي الكون والإنسان والحياةوتغطي («أحياء وأشياء»، ثمّ الكواكب والجبال) جدولًا، ابني العقد الناظم»
  وصدرُه («بأيّ طلبٍ نبدأ؟ أقترح العقد الناظم.») سؤالُ البنّاء ألصقه. والتصميمُ من `hawkama/هيكلة_المعرفة.md` §٢ج و§٨ (الطلب ١)،
  وهو مقترحُ البنّاء؛ وعدُّ القطعة خارج الضابط المجمَّد قراءتُه تنتظر إمضاءَ المالك (بنيةٌ لا تحكم على لفظٍ من مصدر).

  البناء: `NizamMarifi P` نظامٌ معرفيٌّ على أقوالٍ من نوع `P`. وشروطُ الحوكمة الأربعة الأولى في نوعه أو تعريفاته:
  * ح١ (الترخيصُ المتدرّج): القاعدةُ متدرّجةٌ حقلًا في البنية (`mutadarrija`)، ولا يُقبل قولٌ إلّا بسلسلةٍ يقبلها
    `Qaida.maqbul` (`yaqbal`)، وكلُّ مقبولٍ مرخَّص (`maqbul_murakhkhas`).
  * ح٢ (الأصولُ من المودَع): الأصلُ بالتعريف ما رتبتُه صفرٌ وسندُه يبدأ ببصمةٍ غيرِ فارغة لمودَعٍ في سجلّ النظام (`aslB`،
    على `Idaa.aslMusajjal`)؛ فما رتبتُه صفرٌ لا يُرخَّص إلّا كذلك (`sifr_musajjal`).
  * ح٣ (الحكمُ ثلاثيّ، والغيابُ ليس امتناعًا): `hukm` قيمةٌ من `Nizam.Phi.K3`؛ مرخَّصٌ إذا وفقط إذا قُبل (`hukm_P_iff`)، ولا
    يُخرج امتناعًا أبدًا (`hukm_la_mumtani`): الامتناعُ يحتاج مانعًا مسمًّى، ولا مانعَ في هذا العقد بعد.
  * ح٤ (لا «مفهوم» بلا واقعٍ مختوم): مرتبةُ المعنى `martaba` هي `Maratib.martabatMaana` على شواهدَ يقبلها سجلُّ النظام،
    فيرث `la_mafhum_bila_waqi` (`la_mafhum_bila_waqi`)، وكلُّ شاهدٍ لمفهومٍ قيدُه «واقعٌ مختوم» في السجلّ (`mafhum_waqi`).
  ح٥–ح٧ (النقلُ بدرجته، والضابطُ المجمَّد، والوراثة) على الملفّات والتاريخ، فهي في البوّابة لا في النوع (§٢ج).

  النسخةُ الأولى: الشبكة (`Madlul/Shabaka.lean`) نظامًا معرفيًّا، سجلُّه «جدول العلاقات» المختوم وحده («معلومات-سابقة»،
  البصمة من `mudaat/sijill.json`): أصولُه أصولُ الشبكة بعينها (`shabaka_aslB`)، وما تقبله هو ما تقبله (`shabaka_yaqbal`)، فشواهدُها
  المقبولة مرخَّصةٌ في العقد (`shahid_shabaka`)؛ ولا مفهومَ فيها أصلًا لأنّ سجلَّها بلا «واقع مختوم» (`shabaka_la_mafhum`).
  ونسخةُ قاعدة التلقّي الفكريّ (`Aql/TalaqqiFikri.lean`) تنتظر دمجَ طلبها (#141).

  لم يُبنَ: المانعُ المسمّى (فيكون الامتناعُ ممكنًا)، والانتباهُ والاسترجاعُ والربطُ عمليّاتٍ في العقد (§٢ب، الطلب ٣)،
  وإلزامُ أنظمة المشروع القائمة بأن تكون نُسخًا منه (البوّابة لا تفحصه).
  بلا sorry ولا axiom ولا native_decide.
-/
import Aql.Maratib
import Nizam.Phi
import Madlul.Shabaka

namespace NizamMarifi
open _root_.Qaida

/-- النظامُ المعرفيّ: قاعدةٌ متدرّجةٌ برتبةٍ (ح١ في النوع)، وسندٌ لكلّ قول، وسجلُّ مودَعاتٍ بأنواعها. -/
structure NizamMarifi (P : Type) where
  ism         : String
  qaida       : _root_.Qaida.Qaida P
  rutba       : P → Nat
  mutadarrija : Mutadarrija qaida rutba
  sanad?      : P → Option String
  sijill      : List (String × Idaa.Naw)

variable {P : Type} [DecidableEq P]

namespace NizamMarifi

/-- ح٢: الأصلُ ما رتبتُه صفرٌ وسندُه يبدأ ببصمةٍ غيرِ فارغة لمودَعٍ في السجلّ. -/
def aslB (n : NizamMarifi P) (p : P) : Bool :=
  n.rutba p == 0 && Idaa.aslMusajjal n.sanad? (n.sijill.map Prod.fst) p

/-- ح١: القبولُ بسلسلةٍ يقبلها الفاحص على قاعدة النظام وأصوله. -/
def yaqbal (n : NizamMarifi P) (c : Iddia P) : Bool := maqbul n.qaida n.aslB c

/-- ح٣: الحكمُ ثلاثيّ، والمقبولُ مرخَّص وما سواه «لا حكم». -/
def hukm (n : NizamMarifi P) (c : Iddia P) : Nizam.Phi.K3 := if n.yaqbal c then .P else .U

/-- ح٤: مرتبةُ المعنى على الشواهد التي يقبلها سجلُّ النظام. -/
def martaba (n : NizamMarifi P) (m : Nat) (sh : List Maratib.ShahidWaqi) : Maratib.Mukhraj :=
  Maratib.martabatMaana m (Maratib.shuhudMutabara n.sijill sh)

omit [DecidableEq P] in
/-- الأصلُ رتبتُه صفر. -/
theorem asl_rutba_sifr (n : NizamMarifi P) {p : P} (h : n.aslB p = true) : n.rutba p = 0 := by
  unfold aslB at h
  simp only [Bool.and_eq_true, beq_iff_eq] at h
  exact h.1

omit [DecidableEq P] in
/-- الأصلُ سندُه يبدأ ببصمةٍ غيرِ فارغة لمودَعٍ في السجلّ. -/
theorem asl_musajjal (n : NizamMarifi P) {p : P} (h : n.aslB p = true) :
    ∃ s b, n.sanad? p = some s ∧ b ∈ n.sijill.map Prod.fst ∧ b ≠ "" ∧ s.startsWith b = true := by
  unfold aslB at h
  simp only [Bool.and_eq_true] at h
  exact Idaa.aslMusajjal_sanad _ _ _ h.2

/-- ح١: كلُّ مقبولٍ مرخَّصٌ في قاعدة النظام على أصوله. -/
theorem maqbul_murakhkhas (n : NizamMarifi P) (c : Iddia P) (h : n.yaqbal c = true) :
    Murakhkhas n.qaida (fun p => n.aslB p = true) c.qawl :=
  Qaida.maqbul_murakhkhas n.qaida n.aslB c h

omit [DecidableEq P] in
/-- ح٢: ما رتبتُه صفرٌ لا يُرخَّص في النظام إلّا أصلًا سندُه مودَعٌ في السجلّ. -/
theorem sifr_musajjal (n : NizamMarifi P) {p : P}
    (h : Murakhkhas n.qaida (fun p => n.aslB p = true) p) (h0 : n.rutba p = 0) :
    ∃ s b, n.sanad? p = some s ∧ b ∈ n.sijill.map Prod.fst ∧ b ≠ "" ∧ s.startsWith b = true :=
  n.asl_musajjal (rutba_sifr_asl n.qaida n.rutba _ n.mutadarrija h h0)

/-- ح١ وح٢ معًا: القولُ المقبولُ في الرتبة صفر سندُه مودَعٌ في السجلّ. -/
theorem maqbul_sifr_musajjal (n : NizamMarifi P) (c : Iddia P) (h : n.yaqbal c = true)
    (h0 : n.rutba c.qawl = 0) :
    ∃ s b, n.sanad? c.qawl = some s ∧ b ∈ n.sijill.map Prod.fst ∧ b ≠ "" ∧ s.startsWith b = true :=
  n.sifr_musajjal (n.maqbul_murakhkhas c h) h0

/-- ح٣: الحكمُ مرخَّصٌ إذا وفقط إذا قُبلت السلسلة. -/
theorem hukm_P_iff (n : NizamMarifi P) (c : Iddia P) : n.hukm c = .P ↔ n.yaqbal c = true := by
  unfold hukm
  cases n.yaqbal c <;> simp

/-- ح٣: الغيابُ ليس امتناعًا: لا يُخرج العقدُ امتناعًا بلا مانعٍ مسمًّى. -/
theorem hukm_la_mumtani (n : NizamMarifi P) (c : Iddia P) : n.hukm c ≠ .N := by
  unfold hukm
  cases n.yaqbal c <;> simp

omit [DecidableEq P] in
/-- ح٤: بلا مودَعٍ من نوع «واقع مختوم» في سجلّ النظام لا مفهومَ فيه، أيًّا كانت الشواهد. -/
theorem la_mafhum_bila_waqi (n : NizamMarifi P) (hs : ∀ b ∈ n.sijill, b.2 ≠ .waqiMakhtum)
    (m : Nat) (sh : List Maratib.ShahidWaqi) : n.martaba m sh = .maaluma m :=
  Maratib.la_mafhum_bila_waqi n.sijill hs m sh

omit [DecidableEq P] in
/-- ح٤: كلُّ شاهدٍ لمفهومٍ في النظام من الشواهد المعطاة، وقيدُه في السجلّ «واقعٌ مختوم» ببصمةٍ غيرِ فارغة يبدأ بها. -/
theorem mafhum_waqi (n : NizamMarifi P) (m m' : Nat) (sh sh' : List Maratib.ShahidWaqi) (hne : sh' ≠ [])
    (he : n.martaba m sh = .mafhum m' sh' hne) (s : Maratib.ShahidWaqi) (hs : s ∈ sh') :
    s ∈ sh ∧ ∃ b ∈ n.sijill, b.1 ≠ "" ∧ s.basma.startsWith b.1 = true ∧ b.2 = .waqiMakhtum := by
  unfold martaba Maratib.martabatMaana at he
  split at he
  · cases he
  · cases he
    exact Maratib.shuhudMutabara_sanad n.sijill sh s hs

end NizamMarifi

/-! ## النسخةُ الأولى: الشبكة -/

open Madlul.Shabaka

/-- بصمةُ «جدول العلاقات» المختوم (`alaqat.tsv`، «معلومات-سابقة»؛ من `mudaat/sijill.json`). -/
def basmaAlaqat : String := "0269d2cee8b8032c225c674ac4e85acc22168791137cf71044e7bb3bacadc146"

/-- الشبكةُ نظامًا معرفيًّا: سندُ أصلها «جدول العلاقات» المختوم، وسجلُّها هو وحده. -/
def shabakaNizam (sh : Shabaka) : NizamMarifi Qawl where
  ism := "الشبكة"
  qaida := qaidaOf sh
  rutba := rutba
  mutadarrija := qaida_mutadarrija sh
  sanad? q := if sh.aslB q then some basmaAlaqat else none
  sijill := [(basmaAlaqat, .maalumatSabiqa)]

theorem basmaAlaqat_sadiqa : basmaAlaqat.startsWith basmaAlaqat = true ∧ basmaAlaqat.isEmpty = false := by
  decide +kernel

/-- أصولُ الشبكة في العقد هي أصولُها بعينها. -/
theorem shabaka_aslB (sh : Shabaka) (q : Qawl) : (shabakaNizam sh).aslB q = sh.aslB q := by
  obtain ⟨hst, hne⟩ := basmaAlaqat_sadiqa
  unfold NizamMarifi.aslB
  by_cases h : sh.aslB q = true
  · have h0 : rutba q = 0 := by
      cases q <;> first | rfl | simp [Shabaka.aslB] at h
    simp [shabakaNizam, Idaa.aslMusajjal, h, h0, hst, hne]
  · simp only [Bool.not_eq_true] at h
    simp [shabakaNizam, Idaa.aslMusajjal, h]

/-- ما تقبله الشبكةُ في العقد هو ما يقبله فاحصُها. -/
theorem shabaka_yaqbal (sh : Shabaka) (c : Iddia Qawl) :
    (shabakaNizam sh).yaqbal c = maqbul (qaidaOf sh) sh.aslB c := by
  have : (shabakaNizam sh).aslB = sh.aslB := funext (shabaka_aslB sh)
  unfold NizamMarifi.yaqbal
  rw [this]; rfl

/-- **على الشاهد:** «الحيوان يشرب الماء» مرخَّصٌ في العقد، بسلسلة `shawahid_maqbula` الأولى. -/
theorem shahid_shabaka :
    (shabakaNizam shabaka).hukm ⟨.nisba "الحيوان" "شرب" "الماء",
      [.asl (.qabiliyya "الحيوان" "شرب"), .asl (.mafooliyya "شرب" "الماء"),
       khatwa shabaka [.qabiliyya "الحيوان" "شرب", .mafooliyya "شرب" "الماء"] (.nisba "الحيوان" "شرب" "الماء")]⟩ = .P := by
  rw [NizamMarifi.hukm_P_iff, shabaka_yaqbal]
  exact shawahid_maqbula.1

/-- لا مفهومَ في الشبكة: سجلُّها «معلومات سابقة» لا «واقع مختوم». -/
theorem shabaka_la_mafhum (sh : Shabaka) (m : Nat) (s : List Maratib.ShahidWaqi) :
    (shabakaNizam sh).martaba m s = .maaluma m :=
  (shabakaNizam sh).la_mafhum_bila_waqi (by simp [shabakaNizam]) m s

end NizamMarifi
