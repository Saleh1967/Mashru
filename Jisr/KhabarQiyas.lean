/-
# الخبرُ على ضابطه المجمَّد — النتيجةُ على الشفرة الحاليّة

**ما يُقارَن.** لكلّ حالةٍ من `Dawabit.halat` (كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين، وفي سياقه ما حُقن آليًّا — `taalif.md` —،
وجُمّدت ببصمتها في `tahaqquq/dawabit/khabar/tajmid.json` قبل الشفرة): الحكمُ المتوقَّع وحكمُ `Jisr.Khabar.jawab`، والدرجةُ حين يكون المتوقَّعُ
«مقبول» وحده، بتصنيف `Dabit.qarinHukm` و`Dabit.qarinDaraja`.

**الوسم.** العدُّ «مبرهن على الشاهد» (`decide` على الحالات المجمَّدة). ومعناه موافقةُ الشفرة لقراءةٍ مستقلّةٍ للنطاق، لا تغطيةُ اللغة:
الحالاتُ مؤلَّفة لا عيّنةٌ من استعمال.

**التشغيلات.** المبرهناتُ هنا على الشفرة الحاليّة دائمًا. وسجلُّ كلّ تشغيلٍ ملفٌّ في `tahaqquq/dawabit/khabar/` (`natija_1.json` …):
- `natija_1.json`: التشغيلُ الأوّل على الشفرة المجمَّدة في `4374052`، قبل أن يقرأ البنّاءُ الحالات.
-/
import Jisr.KhabarDawabit

namespace Jisr
namespace Khabar
namespace Qiyas

open Dabit Dawabit

/-- أعدادُ المجال بترتيبٍ ثابت: الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ، «لا حكم»، بديلان؛ ثمّ الدرجةُ المتوقَّعة لما متوقَّعُه «مقبول»:
    قليل، بتأويل، بلا درجة، بديلان؛ ثمّ ذواتُ الزوج؛ ثمّ الفئات: موجب، حدّ، خارج، عموم، غموض. -/
def majalAadad : List Nat :=
  let maq := halat.filter (·.hukm == [.maqbul])
  [halat.length] ++
  [Hukm.maqbul, .khata, .laHukm].map (fun d => (halat.filter (·.hukm == [d])).length) ++
  [(halat.filter (fun h => decide (2 ≤ h.hukm.length))).length] ++
  [Daraja.qalil, .bitawil, .bila].map (fun d => (maq.filter (·.daraja == [d])).length) ++
  [(maq.filter (fun h => decide (2 ≤ h.daraja.length))).length,
   (halat.filter (·.zawj.isSome)).length] ++
  [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => (halat.filter (·.fia == f)).length)

/-- **المجال:** 57 حالة. والحكمُ المتوقَّع: مقبول 31، وخطأ 18، و«لا حكم» 5، وبديلان في 3؛ والدرجةُ فيما متوقَّعُه «مقبول»: قليل 0، وبتأويل 0،
    وبلا درجة 30، وبديلان 1؛ و38 حالةً لها زوج. والفئات: موجب 16، وحدّ 18، وخارج 5، وعموم 14، وغموض 4. -/
theorem majal : majalAadad = [57, 31, 18, 5, 3, 0, 0, 30, 1, 38, 16, 18, 5, 14, 4] := by
  decide +kernel

/-- **النتيجة:** 85 صوابًا من 88 حقلًا مسؤولًا (57 حكمًا و31 درجة): نقصُ تغطيةٍ 1، وتجاوزان. -/
theorem natija : ihsa (natayij halat) = ⟨85, 1, 2, 0, 0, 0, 0, 0⟩ := by
  decide +kernel

/-- **بالفئات:** موجب 32 صوابًا؛ وحدّ 17 ونقصٌ واحد؛ وخارج 3 وتجاوزان؛ وعموم 28؛ وغموض 5. -/
theorem natija_fia :
    [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => ihsa ((natayij halat).filter (·.2.1 == f))) =
      [⟨32, 0, 0, 0, 0, 0, 0, 0⟩, ⟨17, 1, 0, 0, 0, 0, 0, 0⟩, ⟨3, 0, 2, 0, 0, 0, 0, 0⟩, ⟨28, 0, 0, 0, 0, 0, 0, 0⟩,
       ⟨5, 0, 0, 0, 0, 0, 0, 0⟩] := by
  decide +kernel

/-- **الإخفاقاتُ بأسمائها** (الحقلُ ونتيجتُه؛ و«/daraja» حقلُ الدرجة). -/
theorem akhta_1 :
    akhta (natayij halat) = [("K21", .naqsTaghtiya), ("K35", .tajawuz), ("K36", .tajawuz)] := by
  decide +kernel

/-- الحقلان في الحالة صوابٌ كلاهما. -/
def sawab (i : String) : Bool :=
  (natayij halat).all fun x => !(x.1 == i || x.1 == i ++ "/daraja") || x.2.2 == Natija.sawab

/-- **الأزواج** (مدخلان يختلفان في حقلٍ واحد): تسعةَ عشرَ زوجًا، يتغيّر جوابُ المحرّك فيها كلِّها، ويصيب الطرفان معًا في ثمانيةَ عشر. -/
theorem azwaj_1 :
    (azwaj halat).length = 19 ∧ ((azwaj halat).filter (·.2.2)).length = 19 ∧
    ((azwaj halat).filter fun p => sawab p.1 && sawab p.2.1).length = 18 := by
  decide +kernel

end Qiyas
end Khabar
end Jisr
