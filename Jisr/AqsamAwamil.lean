/-
  Jisr/AqsamAwamil.lean — معجم أقسام الكلم: أوّلُ قطعةٍ منه — أقسامُ العوامل المئة (اسم/فعل/حرف) عبر عائلات المالك في
  `SLGE/Wad.lean` (المنقولة عن قطر الندى بأسطرها). إذن المالك بلفظه (2026-10-16): «موافق ويعتمد معجم أقسام الكلم وسماتها
  مودَعًا (أو الإذن بتعيينه من المخصّص والعوامل المئة وقطر الندى) ومغني اللبيب والكتاب والشخصية الثالث ليقرأ القارئ الأطر».

  الطريقة: العاملُ في الجدول (`Jisr/AwamilJadwal.lean`) يُطابَق باسمه — مجرَّدًا من الحركات والشدّة والمسافات وما بين
  القوسين — مع عائلة المالك التي عملُها عملُ صنفه (الصنف 1 ↔ كان L170، 2 ↔ إنّ L187، 3 ↔ ظنّ L208، 4 ↔ النواصب L96،
  5 ↔ الجوازم L112، 7 ↔ حروف الجرّ L338–339)، فيأخذ قسمَها عند المالك (`Wad.Amil.kind`). ما لا عائلةَ له، أو عائلتُه بلا
  قسمٍ عند المالك (أسماء الشرط L115، كاد وأخواتها، العطف، الشرط غير الجازم، الاستفهام، النداء، حتى المصدرية وفاء السببية
  وواو المعية، خلا/عدا/حاشا، صار/ليس، عدّ/جعل، لا الناهية ولام الأمر)، فلا حكم (`none`) حتّى يُنقل من المغني أو الكتاب بأسطره.
  الوسم: مطابَق لعائلات المالك في Wad (المنقولة عن القطر بأسطرها)؛ والعدّ 45/100 بـ decide على القوائم، من `#eval` قبل كتابته.
-/
import Jisr.Awamil
import SLGE.Wad

namespace Jisr
namespace AqsamAwamil
open SLGE.Cat (Kind)

/-- تجريد الاسم للمطابقة: حذف الحركات والشدّة والتنوين والمسافات وما بين القوسين (وسيط معلَن). -/
def tajrid (s : String) : String :=
  let cs := s.toList
  let rec go : List Char → Bool → List Char
    | [], _ => []
    | c :: r, inside =>
      if c == '(' then go r true
      else if c == ')' then go r false
      else if inside then go r true
      else if ['َ', 'ُ', 'ِ', 'ْ', 'ّ', 'ً', 'ٌ', 'ٍ', ' '].contains c then go r false
      else c :: go r false
  String.ofList (go cs false)

/-- عائلة المالك التي عملُها عملُ الصنف. -/
def aila : Nat → List SLGE.Wad.Amil
  | 1 => SLGE.Wad.kanaF | 2 => SLGE.Wad.innaF | 3 => SLGE.Wad.zannaF | 4 => SLGE.Wad.nasbF
  | 5 => SLGE.Wad.jazm1F | 7 => SLGE.Wad.jarrF | _ => []

/-- قسم العامل من عائلته عند المالك إن طابق اسمُه. -/
def qismOf (ism : String) (sinf : Nat) : Option Kind :=
  ((aila sinf).find? fun a => tajrid a.name == tajrid ism).bind (·.kind)

/-- المعجم: (العامل، صنفه، قسمه أو لا حكم). -/
def mujam : List (String × Nat × Option Kind) :=
  Awamil.table.map fun r => (r.1, r.2.1, qismOf r.1 r.2.1)

/-- **45 من المئة لها قسمٌ من القطر عبر عائلات المالك** (حروف الجرّ 14، النواصب 4، الجوازم 2، كان 11، إنّ 6، ظنّ 8)،
و55 لا حكمَ لها بعد؛ ولا عاملٌ منها اسمٌ (المعجم هنا حروفٌ وأفعال). -/
theorem mujam_45 :
    (mujam.filter fun r => r.2.2.isSome).length = 45 ∧
    (mujam.filter fun r => r.2.2 == some .harf).length = 26 ∧
    (mujam.filter fun r => r.2.2 == some .fil).length = 19 ∧
    (mujam.filter fun r => r.2.2 == some .ism).length = 0 ∧
    ([1, 2, 3, 4, 5, 7].map fun c => (mujam.filter fun r => r.2.1 == c && r.2.2.isSome).length) =
      [11, 6, 8, 4, 2, 14] := by decide

/-- ما لا حكمَ له بعد، بأصنافه: 1 (صار، ليس)، 3 (عدّ، جعل)، 4 (حتى المصدرية، فاء السببية، واو المعية)، 5 (لا الناهية،
لام الأمر)، 6 (كاد وأخواتها)، 7 (خلا، عدا، حاشا)، 8، 9، 10، 11، 12، 13. -/
theorem bila_hukm :
    ((mujam.filter fun r => r.2.2.isNone).map (·.2.1)).eraseDups = [1, 3, 6, 7, 8, 5, 9, 4, 10, 11, 12, 13] ∧
    (mujam.filter fun r => r.2.2.isNone).length = 55 := by decide

/-- شواهد المطابقة: «ما زال» بـ«مازال» عند المالك، و«رُبَّ» بـ«رب»، و«حتى (جر)» بـ«حتى»، و«إنّ» حرفٌ و«كان» فعل. -/
theorem shawahid :
    qismOf "ما زال" 1 = some .fil ∧ qismOf "رُبَّ" 7 = some .harf ∧ qismOf "حتى (جر)" 7 = some .harf ∧
    qismOf "إنّ" 2 = some .harf ∧ qismOf "كان" 1 = some .fil ∧ qismOf "صار" 1 = none ∧ qismOf "مَن" 10 = none := by
  decide

end AqsamAwamil
end Jisr
