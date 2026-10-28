/-
# الضمير على ضابطه المجمَّد — النتيجةُ على الشفرة الحاليّة

**ما يُقارَن.** لكلّ حالةٍ من `Dawabit.halat` (كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين، وفي سياقه ما حُقن آليًّا — `taalif.md` —،
وجُمّدت ببصمتها في `tahaqquq/dawabit/damir/tajmid.json` قبل الشفرة): الحكمُ المتوقَّع وحكمُ `Jisr.Damir.jawab`، والدرجةُ حين يكون المتوقَّعُ
«مقبول»، بتصنيف `Dabit.qarinHukm` و`Dabit.qarinDaraja`.

**الوسم.** العدُّ «مبرهن على الشاهد» (`decide` على الحالات المجمَّدة). ومعناه موافقةُ الشفرة لقراءةٍ مستقلّةٍ للنطاق، لا تغطيةُ اللغة:
الحالاتُ مؤلَّفة لا عيّنةٌ من استعمال.

**التشغيلات.** المبرهناتُ هنا على الشفرة الحاليّة دائمًا. وسجلُّ كلّ تشغيلٍ ملفٌّ في `tahaqquq/dawabit/damir/` (`natija_1.json` …)،
ويفحصه `tahaqquq/test_damir.py`:
- `natija_1.json`: التشغيلُ الأوّل على الشفرة المجمَّدة في `af3356c`، قبل أن يقرأ البنّاءُ الحالات: 55 صوابًا من 69 حقلًا مسؤولًا (46 حكمًا و23
  درجة): نقصُ تغطيةٍ 5 (D08، D10، D45 حكمًا ودرجةً، D46)، وتجاوزٌ 5 (D12، D14، D17، D32، D34)، وخطأٌ في الدرجة 4 (D23، D25، D31، D33). وأسماءُ
  مبرهناته أسماؤها في `6b378d8`. والأربعةُ الأخيرة بالمواصفة نقصُ تغطية (`qarinDaraja` يومئذٍ تخالفها)، فعدُّه بها 55/9/5/0 (`mulhaq_1.md` §١).
- `natija_2.json`: بعد تعديل `Jisr/Damir.lean` بقراءة المؤلّف في المواضع كلِّها (فيه «ما غُيّر بعد قراءة الحالات»)، على مادّةٍ مكشوفة: 69 من 69.
- `natija_3.json`: بعد مراجعة `murajii` (مقارنةُ الدرجة على المواصفة، وتغييران في الحكم بلا حالة؛ `mulhaq_1.md` §٥): 69 من 69.
-/
import Jisr.DamirDawabit

namespace Jisr
namespace Damir
namespace Qiyas

open Dabit Dawabit

/-- أعدادُ المجال بترتيبٍ ثابت (يحسبها `tahaqquq/test_damir.py` من `cases.json` بالترتيب نفسه): الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ،
    «لا حكم»، بديلان؛ ثمّ الدرجةُ المتوقَّعة لما متوقَّعُه «مقبول»: راجح، مرجوح، سواء، بلا درجة، بديلان؛ ثمّ ذواتُ الزوج؛ ثمّ الفئات: موجب،
    حدّ، خارج، عموم، غموض. -/
def majalAadad : List Nat :=
  let maq := halat.filter (·.hukm == [.maqbul])
  [halat.length] ++
  [Hukm.maqbul, .khata, .laHukm].map (fun d => (halat.filter (·.hukm == [d])).length) ++
  [(halat.filter (fun h => decide (2 ≤ h.hukm.length))).length] ++
  [Daraja.rajih, .marjuh, .sawa, .bila].map (fun d => (maq.filter (·.daraja == [d])).length) ++
  [(maq.filter (fun h => decide (2 ≤ h.daraja.length))).length,
   (halat.filter (·.zawj.isSome)).length] ++
  [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => (halat.filter (·.fia == f)).length)

/-- **المجالُ غيرُ فارغ ولا مائلٍ إلى «لا حكم»:** 46 حالة. والحكمُ المتوقَّع: مقبول 23، وخطأ 16، و«لا حكم» 7، وبديلان في 0؛ والدرجةُ
    فيما متوقَّعُه «مقبول»: راجح 2، ومرجوح 3، وسواء 2، وبلا درجة 7، وبديلان 9؛ و34 حالةً لها زوج. والفئات: موجب 13، وحدّ 10، وخارج 7،
    وعموم 7، وغموض 9. -/
theorem majal : majalAadad = [46, 23, 16, 7, 0, 2, 3, 2, 7, 9, 34, 13, 10, 7, 7, 9] := by
  decide +kernel

/-- **النتيجة:** 69 صوابًا من 69 حقلًا مسؤولًا (على الشفرة الحاليّة ومادّةٍ مكشوفة؛ والأوّلُ 55/69 في `natija_1.json`). -/
theorem natija : ihsa (natayij halat) = ⟨69, 0, 0, 0, 0, 0, 0, 0⟩ := by
  decide +kernel

/-- **بالفئات** (حقولًا): موجب 26، وحدّ 10، وخارج 7، وعموم 8، وغموض 18 — كلُّها صواب. -/
theorem natija_fia :
    [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => ihsa ((natayij halat).filter (·.2.1 == f))) =
      [⟨26, 0, 0, 0, 0, 0, 0, 0⟩, ⟨10, 0, 0, 0, 0, 0, 0, 0⟩, ⟨7, 0, 0, 0, 0, 0, 0, 0⟩, ⟨8, 0, 0, 0, 0, 0, 0, 0⟩,
       ⟨18, 0, 0, 0, 0, 0, 0, 0⟩] := by
  decide +kernel

/-- **ولا إخفاق.** وفي التشغيل الأوّل أربعةَ عشرَ حقلًا بأسمائها في `natija_1.json`. -/
theorem akhta_sifr : akhta (natayij halat) = [] := by
  decide +kernel

/-- الحقلان في الحالة صوابٌ كلاهما. -/
def sawab (i : String) : Bool :=
  (natayij halat).all fun x => !(x.1 == i || x.1 == i ++ "/daraja") || x.2.2 == Natija.sawab

/-- **الأزواج** (مدخلان يختلفان في حقلٍ واحد): سبعةَ عشرَ زوجًا، يتغيّر جوابُ المحرّك فيها كلِّها، ويصيب الطرفان معًا فيها كلِّها. وفي
    التشغيل الأوّل أصاب الطرفان معًا في تسعة (`natija_1.json`). -/
theorem azwaj_1 :
    (azwaj halat).length = 17 ∧ ((azwaj halat).filter (·.2.2)).length = 17 ∧
    ((azwaj halat).filter fun p => sawab p.1 && sawab p.2.1).length = 17 := by
  decide +kernel

end Qiyas
end Damir
end Jisr
