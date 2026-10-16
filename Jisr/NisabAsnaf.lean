/-
  Jisr/NisabAsnaf.lean — النِّسَبُ الثلاث على أصناف العوامل المئة: تعيينُها على أدوار معمولات كلّ صنفٍ من الثلاثة عشر.
  قرارُ المالك (2026-10-17، 00:09): «وكذلك النِّسَبُ الثلاث على الأصناف (ج3 721): تعيينُها على أصناف المئة (Jisr/Nisab.lean عيّنها على أدوار
  الأطر لا على الأصناف — "ما ليس هنا" في ترويسة Jisr/Awamil.lean)».

  **النصّ** (ج3 = الشخصية الإسلامية ج3، النصُّ المحوَّل `a2.txt` بأسطره، مرشَّحٌ غير مختوم): س721 «وهي، أي الألفاظ، وضعت ليفيد الوضع النسب
  الإسنادية، أو التقييدية، أو الإضافية، بين المفردات، بضم بعضها إلى بعض، كالفاعلية، والمفعولية، وغيرهما» — وفيه لا تعريفَ للثلاث سوى المثالين
  (الفاعلية والمفعولية)؛ وس932 «حروف الإضافة، وهي ما يفضي بمعاني الأفعال إلى الأسماء» (حروفُ الجرّ بتسمية سيبويه). والقطرُ (مودَع مختوم) L268
  «المفعول به، وهو ما وقع عليه فعل الفاعل ك "ضربت زيدا" ومنه المنادى». والعلاقاتُ عند المالك `SLGE.Simat.semOf` على أدواره (0 مبتدأ/اسم،
  1 خبر، 2 فعل، 6 مجرور): 1 مسندٌ إليه، 2 مسند، 5 تعلّق؛ وأدوارُ جدول العوامل `Jisr/Awamil.lean` (`dawrIsm`): 0، 1، 2، 6، 9، 10، 11، 12، 13.

  **التعيين (البنّاء، يُعرض على المالك):** `semDawr` امتدادُ `semOf` إلى أدوار العوامل: أدوارُ المالك بعلاقته (0 ← 1، 1 ← 2، 2 ← 2، 6 ← 5:
  `muwafiq_semOf`)؛ فعلُ الشرط وجوابه (11، 12) مسندان في جملتيهما (2) — والعلاقةُ بين الجملتين سببيّةٌ عند المالك (`Simat.sababiyya`،
  `TarkibExt.shartState`) خارجَ الثلاث؛ المنادى (13) مفعوليّة (4: القطر L268) فنسبتُه التقييدية (`Nisab.nisbaOf 4`)؛ المعطوفُ عليه والمعطوف
  (9، 10) تساوٍ: لا علاقةَ لهما بالعامل، والتابعُ يأخذ نسبةَ متبوعه (`Awamil.rawabit 8`). ثمّ `nisbaDawr = Nisab.nisbaOf ∘ semDawr`،
  و`nisabSinf c` نِسَبُ أدوار معادلات الصنف `Awamil.muadalat c`. ومفعولا ظنّ (الصنف 3، الدوران 0 و1) إسناديان بعلاقة المالك (مبتدأٌ وخبرٌ في
  الأصل)، ومفعوليّتُهما للناسخ هي ازدواجُ «التقييدية» الذي أمضاه المالك في `Jisr/Utur.lean` (2026-10-16) — معلَنٌ لا مبنيّ.

  **المبرهنات (على الشاهد، 7؛ `decide` على جدول المالك `Awamil.table`/`muadalat` وعلاقاته `semOf`):** `muwafiq_semOf` (الامتدادُ يوافق
  المالك على أدواره)، `jadwal_nisab` (الجدولُ كاملًا: الأصنافُ الثلاثة عشر بنِسَب أدوارها)، `kull_mamul_nisba` (كلُّ معمولٍ في كلّ معادلةٍ له
  نسبة؛ والعطفُ تساوٍ بلا نسبة)، `idafiyya_jarr` (الإضافيةُ على المجرور وحده، في حروف الجرّ ولام التعليل — «حروف الإضافة» ج3 س932)،
  `taqyidiyya_nida` (التقييديةُ على مستوى الصنف في النداء وحده)، `isnadiyya_asnaf` (الإسناديةُ في النواسخ الثلاثة وكاد والنواصب والجوازم
  ولام التعليل والشرط الجازم)، `ihsa_awamil` (المئةُ بنِسَب معمولاتها: 57 إسنادية، 18 إضافية، 4 تقييدية، 22 بلا معمولٍ ذي نسبة — ولام
  التعليل في الأوليين). الوسم: مبرهن على الشاهد (جدول المالك وتعيين البنّاء)؛ وتعيينُ 11–13 و9–10 رأيُ البنّاء المعلَن حتّى يمضيه المالك.
  الجدولُ `nisab_asnaf.tsv` مسجَّلٌ «مرشّحًا» حتّى يأذن المالك بختمه؛ ومطابقتُه `tahaqquq/test_nisab_asnaf.py`.
-/
import Jisr.Nisab
import Jisr.Awamil

set_option autoImplicit false

namespace Jisr
namespace NisabAsnaf
open Nisab Awamil SLGE.Simat

/-- علاقةُ دور المعمول — امتدادُ `Simat.semOf` إلى أدوار جدول العوامل (تعيين البنّاء): فعلُ الشرط وجوابه مسندان (2)، والمنادى مفعوليّة (4)،
والمعطوفُ عليه والمعطوف تساوٍ (0)، وسائرُ الأدوار بعلاقة المالك. -/
def semDawr (r : Nat) : Nat :=
  match r with
  | 11 | 12 => 2
  | 13 => 4
  | 9 | 10 => 0
  | _ => semOf r

/-- نسبةُ دور المعمول من علاقته (`Nisab.nisbaOf`). -/
def nisbaDawr (r : Nat) : Option Nisba := nisbaOf (semDawr r)

/-- أدوارُ معمولات الصنف من معادلاته (بلا تكرار). -/
def adwar (c : Nat) : List Nat := ((muadalat c).flatMap fun alt => alt.map (·.1)).eraseDups

/-- نِسَبُ الصنف: لكلّ دورٍ من أدواره نسبتُه. -/
def nisabSinf (c : Nat) : List (Nat × Option Nisba) := (adwar c).map fun r => (r, nisbaDawr r)

/-- **الامتدادُ يوافق المالك على أدواره** (0، 1، 2، 6) — على الشاهد. -/
theorem muwafiq_semOf : [0, 1, 2, 6].all (fun r => semDawr r == semOf r) = true := by decide

/-- **الجدولُ كاملًا** — الأصنافُ الثلاثة عشر (بأرقام المالك `Awamil.sinfIsm`) بنِسَب أدوارها: كان وإنّ وظنّ (الاسمُ والخبرُ إسناديان)،
النواصبُ والجوازم (المضارعُ مسند)، كاد (الاسمُ والمضارع)، حروفُ الجرّ (المجرورُ إضافية)، العطفُ (تساوٍ: لا معادلة)، لامُ التعليل (مجرورٌ إضافية
أو مضارعٌ إسنادية)، الشرطُ الجازم (فعلُه وجوابُه إسناديان)، الشرطُ غيرُ الجازم والاستفهام (لا فرض)، النداءُ (المنادى تقييدية). -/
theorem jadwal_nisab :
    (List.range 14).map nisabSinf =
      [[], [(0, some .isnadiyya), (1, some .isnadiyya)], [(0, some .isnadiyya), (1, some .isnadiyya)],
       [(0, some .isnadiyya), (1, some .isnadiyya)], [(2, some .isnadiyya)], [(2, some .isnadiyya)],
       [(0, some .isnadiyya), (2, some .isnadiyya)], [(6, some .idafiyya)], [], [(6, some .idafiyya), (2, some .isnadiyya)],
       [(11, some .isnadiyya), (12, some .isnadiyya)], [], [], [(13, some .taqyidiyya)]] := by decide

/-- **كلُّ معمولٍ في كلّ معادلةٍ له نسبةٌ من الثلاث**؛ والعطفُ تساوٍ (`rawabit`) بلا معادلةٍ ولا نسبةٍ لدورَيه — على الشاهد. -/
theorem kull_mamul_nisba :
    (List.range 14).all (fun c => (adwar c).all fun r => (nisbaDawr r).isSome) = true ∧
    rawabit 8 = [(9, 10)] ∧ nisbaDawr 9 = none ∧ nisbaDawr 10 = none ∧ adwar 8 = [] := by decide

/-- **الإضافيةُ على المجرور وحده** (الدور 6)، وفي صنفين: حروفُ الجرّ ولامُ التعليل — «حروف الإضافة … ما يفضي بمعاني الأفعال إلى الأسماء»
(ج3 س932) — على الشاهد. -/
theorem idafiyya_jarr :
    (List.range 14).all (fun c => (adwar c).all fun r => (nisbaDawr r == some .idafiyya) == (r == 6)) = true ∧
    ((List.range 14).filter fun c => (adwar c).contains 6) = [7, 9] := by decide

/-- **التقييديةُ على مستوى الصنف في النداء وحده** (المنادى مفعولٌ به: القطر L268)؛ ومفعولا ظنّ إسناديان بعلاقة المالك (الازدواجُ معلَن). -/
theorem taqyidiyya_nida :
    ((List.range 14).filter fun c => (nisabSinf c).any fun x => x.2 == some .taqyidiyya) = [13] ∧
    nisabSinf 3 = [(0, some .isnadiyya), (1, some .isnadiyya)] := by decide

/-- **الإسناديةُ** في النواسخ الثلاثة وكاد والنواصب والجوازم ولام التعليل والشرط الجازم — على الشاهد. -/
theorem isnadiyya_asnaf :
    ((List.range 14).filter fun c => (nisabSinf c).any fun x => x.2 == some .isnadiyya) = [1, 2, 3, 4, 5, 6, 9, 10] := by decide

/-- عواملُ الجدول التي في نِسَب معمولاتها النسبةُ `n`. -/
def awamilBi (n : Nisba) : List String :=
  (table.filter fun g => (nisabSinf g.2.1).any fun x => x.2 == some n).map (·.1)

/-- **إحصاءُ المئة بنِسَب معمولاتها**: 57 إسنادية، 18 إضافية، 4 تقييدية، و22 بلا معمولٍ ذي نسبة (العطف 8، الشرطُ غيرُ الجازم 4، الاستفهام 10)؛
ولامُ التعليل في الأوليين فالمجموعُ 101 على 100 عامل — على الشاهد. -/
theorem ihsa_awamil :
    (awamilBi .isnadiyya).length = 57 ∧ (awamilBi .idafiyya).length = 18 ∧ (awamilBi .taqyidiyya).length = 4 ∧
    (table.filter fun g => nisabSinf g.2.1 = []).length = 22 ∧ awamilBi .taqyidiyya = ["يا", "أيا", "هيا", "آ"] ∧
    (awamilBi .isnadiyya).filter (awamilBi .idafiyya).contains = ["لام التعليل"] := by decide

end NisabAsnaf
end Jisr
