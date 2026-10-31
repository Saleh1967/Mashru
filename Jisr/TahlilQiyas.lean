/-
# قراءةُ الجملة بالعوامل على ضابطها المجمَّد — النتيجةُ على الشفرة الحاليّة

**ما يُقارَن** (`Jisr/TahlilDabit.lean`، بنصّ المواصفة `tahaqquq/dawabit/tahlil/wasf.md` §القياس): لكلّ حالةٍ من `Dabit.halat` (كتبها مؤلّفٌ
مستقلٌّ إجرائيًّا من المواصفة والقطر، وفي سياقه ما حُقن آليًّا — `taalif.md` —، وجُمّدت ببصمتها في `tahaqquq/dawabit/tahlil/tajmid.json` قبل
الشفرة): حقلُ الحكم دائمًا (`hukmJumla` على خلايا الجملة كما قرأها القارئ)، وحقلُ الأدوار حيث المتوقَّعُ «مقبول» وحكمُ المحرّك «مقبول»
(`adwarMaqbula`).

**الوسم.** خمسُ مبرهناتٍ على الشاهد بالمعيار الموحَّد (`Nizam/Asas.lean`): `majal`، `natija`، `natija_fia`، `akhta_1`، `azwaj_1` (`decide` على
الحالات المجمَّدة). ومعنى العدّ موافقةُ الشفرة لقراءةٍ مستقلّةٍ للنطاق، لا تغطيةُ اللغة: الحالاتُ مؤلَّفة لا عيّنةٌ من استعمال.

**التشغيلات.** المبرهناتُ هنا على الشفرة الحاليّة دائمًا. وسجلُّ كلّ تشغيلٍ ملفٌّ في `tahaqquq/dawabit/tahlil/` (`natija_1.json` …).
- `natija_1.json`: التشغيلُ الأوّل على الشفرة كما دُفعت في `1d97220` (والحالاتُ مجمَّدةٌ في `9ea302c` قبلها): 59 صوابًا من 81 حقلًا (55 حكمًا و26
  أدوارًا).
-/
import Jisr.TahlilDawabit

namespace Jisr
namespace Tahlil
namespace Qiyas

open Jisr.Utur Dabit

/-- أعدادُ المجال بترتيبٍ ثابت (يحسبها `tahaqquq/test_tahlil.py` من `cases.json` بالترتيب نفسه): الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ،
    «لا حكم»، بديلان؛ ثمّ القراءاتُ البديلة؛ ثمّ ذواتُ الزوج؛ ثمّ الفئاتُ: موجب، حدّ، خارج، عموم، غموض. -/
def majalAadad : List Nat :=
  [halat.length] ++
  [Hukm.murakhkhas, .mumtani, .laHukm].map (fun d => (halat.filter (·.hukm == [d])).length) ++
  [(halat.filter (fun h => decide (2 ≤ h.hukm.length))).length,
   (halat.filter (fun h => decide (2 ≤ h.adwar.length))).length,
   (halat.filter (·.zawj.isSome)).length] ++
  [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => (halat.filter (·.fia == f)).length)

/-- **المجالُ غيرُ فارغ ولا مائلٍ إلى «لا حكم»:** 55 حالة. والمتوقَّع: مقبول 31، وخطأ 18، و«لا حكم» 5، وبديلان في حكمٍ واحد، وقراءتان في
    حالةٍ واحدة؛ و28 حالةً في 14 زوجًا. والفئات: موجب 16، وحدّ 18، وخارج 5، وعموم 14، وغموض 2. -/
theorem majal : majalAadad = [55, 31, 18, 5, 1, 1, 28, 16, 18, 5, 14, 2] := by
  decide +kernel

/-- **النتيجة:** 59 صوابًا من 81 حقلًا: 15 نقصَ تغطية، و4 تجاوزات، وقبولٌ خاطئٌ واحد، واختيارٌ بلا مرجّحٍ واحد، وخطأُ أدوارٍ واحد؛ ولا ردَّ
    خاطئ، ولا رفضَ من القارئ، ولا خطأَ في البديلين. -/
theorem natija : ihsa (natayij halat) = ⟨59, 15, 4, 1, 0, 1, 1, 0, 0⟩ := by
  decide +kernel

/-- **بالفئات:** موجب 26 ونقوصٌ ثلاثة؛ وحدّ 7 ونقوصٌ عشرة وقبولٌ خاطئٌ واحد؛ وخارج 1 وأربعُ تجاوزات؛ وعموم 25 ونقصٌ واحد وخطأُ أدوارٍ واحد؛
    وغموض: نقصٌ واحد واختيارٌ واحد. -/
theorem natija_fia :
    [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => ihsa ((natayij halat).filter (·.2.1 == f))) =
      [⟨26, 3, 0, 0, 0, 0, 0, 0, 0⟩, ⟨7, 10, 0, 1, 0, 0, 0, 0, 0⟩, ⟨1, 0, 4, 0, 0, 0, 0, 0, 0⟩, ⟨25, 1, 0, 0, 0, 0, 1, 0, 0⟩,
       ⟨0, 1, 0, 0, 0, 1, 0, 0, 0⟩] := by
  decide +kernel

/-- **والإخفاقاتُ الاثنان والعشرون بأسمائها.** -/
theorem akhta_1 :
    akhta (natayij halat) = [("T05", .hukm, .naqsTaghtiya), ("T06", .hukm, .naqsTaghtiya), ("T07", .hukm, .naqsTaghtiya),
      ("T08", .hukm, .naqsTaghtiya), ("T14", .hukm, .naqsTaghtiya), ("T15", .hukm, .naqsTaghtiya), ("T22", .hukm, .qabulKhati),
      ("T23", .hukm, .naqsTaghtiya), ("T25", .hukm, .naqsTaghtiya), ("T27", .hukm, .naqsTaghtiya), ("T32", .hukm, .naqsTaghtiya),
      ("T38", .adwar, .khataAdwar), ("T39", .hukm, .naqsTaghtiya), ("T41", .hukm, .naqsTaghtiya), ("T43", .hukm, .naqsTaghtiya),
      ("T48", .hukm, .naqsTaghtiya), ("T49", .hukm, .tajawuz), ("T50", .hukm, .tajawuz), ("T52", .hukm, .tajawuz),
      ("T53", .hukm, .tajawuz), ("T54", .hukm, .naqsTaghtiya), ("T55", .hukm, .ikhtiyar)] := by
  decide +kernel

/-- حقلُ الحكم في الحالة صواب. -/
def sawabHukm (i : String) : Bool := (natayij halat).any fun x => x.1 == i && x.2.2.1 == Haql.hukm && x.2.2.2 == Natija.sawab

/-- **تبديلُ كلمةٍ واحدة** (الأزواجُ الأربعة عشر): يتغيّر حكمُ المحرّك في ثلاثة عشر منها، ولا يتغيّر في T06/T07؛ **ويصيب الطرفان معًا في
    ستّة.** ولا رفضَ من القارئ. -/
theorem azwaj_1 :
    (azwaj halat).length = 14 ∧ ((azwaj halat).filter (·.2.2)).length = 13 ∧
    (azwaj halat).filter (!·.2.2) = [("T06", "T07", false)] ∧
    ((azwaj halat).filter fun p => sawabHukm p.1 && sawabHukm p.2.1).length = 6 ∧ rafd halat = [] := by
  decide +kernel

end Qiyas
end Tahlil
end Jisr
