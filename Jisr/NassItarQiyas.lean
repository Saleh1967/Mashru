/-
# من النصّ إلى الإطار في ل1 على ضابطها المجمَّد — النتيجةُ على الشفرة الحاليّة

**ما يُقارَن** (`Jisr/NassItarDabit.lean`، بنصّ المواصفة `tahaqquq/dawabit/nass/wasf.md` §القياس): لكلّ حالةٍ من `Dabit.halat` (كتبها مؤلّفٌ
مستقلٌّ إجرائيًّا من المواصفة والنطاق، وفي سياقه ما حُقن آليًّا — `taalif.md` —، وجُمّدت ببصمتها في `tahaqquq/dawabit/nass/tajmid.json` قبل
الشفرة): حقلُ الحكم دائمًا (`hukmNass` على خلايا الجملة كما قرأها القارئ)، وحقلُ الإطار حيث المتوقَّعُ «مقبول» وحكمُ المحرّك «مقبول»
(`maqbula`).

**الوسم.** المبرهناتُ الستّ على الشاهد بالمعيار الموحَّد (`Nizam/Asas.lean`)، والعدُّ «مبرهن على الشاهد» (`decide` على الحالات المجمَّدة).
ومعناه موافقةُ الشفرة لقراءةٍ مستقلّةٍ للنطاق، لا تغطيةُ اللغة: الحالاتُ مؤلَّفة لا عيّنةٌ من استعمال.

**انحرافٌ عن المنهج §٤-ج** (`hawkama/منهج_الضوابط.md`: «والبنّاءُ لا يقرأ الحالات ولا وصفَ التأليف حتى تُدفع الشفرة»): قرأ البنّاءُ من
`taalif.md` أسطرَه 1–25 (ما قرأه المؤلّف وما لم يقرأه وما حُقن، بلا حالة) قبل دفع الشفرة، وذكره `tajmid.json` (`qabl_shifra`)، وتوجيهُ المؤلّف
أذن به (`tawjih_muallif.md`)؛ والتفصيلُ في `tahaqquq/dawabit/nass/mulhaq_1.md` (ضبطه المراجع المستقلّ).

**التشغيلات.** المبرهناتُ هنا على الشفرة الحاليّة دائمًا. وسجلُّ كلّ تشغيلٍ ملفٌّ في `tahaqquq/dawabit/nass/` (`natija_1.json` …).
- `natija_1.json`: التشغيلُ الأوّل على الشفرة المجمَّدة في `ecf92e2`، قبل أن يقرأ البنّاءُ الحالات: 61 صوابًا من 71.
- `natija_2.json`: على مادّةٍ مكشوفة، بعد تصحيح رأس `Jisr/NassItar.lean` في `8ddf814` (توثيقٌ وحده: اقتباسُ القطر L343 مُدَّ إلى مستثناه،
  وإحالةٌ إلى مبرهنةٍ لا وجودَ لها صُحّحت، وعدُّ المبرهنات): الأعدادُ نفسُها.
- `natija_3.json`: على مادّةٍ مكشوفة، بعد مراجعة `murajii` الأولى (توثيقٌ في `Jisr/NassItar.lean` و`Jisr/NassItarDabit.lean`، وشاهدُ حدٍّ
  `haykal_fil_la_itar`؛ والشفرةُ الحاكمة كما هي): الأعدادُ نفسُها، ومعها عدُّ الأزواج التي يصيب طرفاها (10).

**الإخفاقاتُ العشرة** (`akhta_1`)، وأسبابُها على إطاراتها مبرهنةٌ على الشاهد (`asbab_akhta`: `hukmSitta` و`asbabLaHukm` و`qiraaSitta`
و`waslBase` لكلّ إطار)، وقراءتُها قراءةُ البنّاء:
- **N04، N21، N24، N28، N35** (الياءُ أو الألفُ آخرَ الفاعل المضاف: «جَاءَ أَبِي الْوَلَدِ»، «حَمِي»، «هَنَا»، «فَا»، «ذَا»؛ المتوقَّع خطأ): حرفُ علّةٍ
  آخرًا في موضع الرفع تُقدَّر عليه الحركة (`Utur.illaMuqaddara`؛ القطر L92–93) فـ«لا حكم» بسببه المسمّى (`illaAkhir`)؛ وصفُّ الأسماء الستّة لا
  يخطّئ إلّا موضعَ الواو بعد ضمّةٍ رفعًا بلا رخصةٍ ولا وقف (`qiraaSitta`)، فلا يرفعه إلى خطأ. والإطارُ الآخر (مفعولٌ بعد الفاعل) ممتنعٌ من
  `waslBase`، والجمعُ «لا حكم».
- **N34، N36، N38** («ذُو/ذَا/ذِي الْمَالِ»؛ المتوقَّع مقبول): رخصةُ «ذو» مشروطةٌ بالصحبة وهي لا تُقرأ من الدالّ (`QawaidSitta.dhu_la_rukhsa`)،
  فيبقى سببُ `Utur`: الإعرابُ بالحرف في N34، وحرفُ العلّة آخرًا في N36 وN38.
- **N45** («جَاءَ الضَّارِبُ الرَّجُلِ»؛ المتوقَّع مقبول): مستثنى القطر L344–345 لم يُبنَ (رأسُ `Jisr/NassItar.lean`)، فلا إطارَ بمضافٍ إليه، والإطارُ
  الباقي (مفعولٌ مجرور) ممتنعٌ من `waslBase`: حالُ الكلمة غيرُ حال موضعها.
- **N46** («جَاءَ أَبًا»، خارج؛ المتوقَّع «لا حكم»، لاحتمال القصر عند المؤلّف): حالُ الكلمة تُقرأ من حركة ما قبل التنوين (`Utur.halaIrab` في
  `waslBase`)، فالفتحةُ نصبٌ في موضع الرفع، فخطأ؛ وقراءةُ الستّة فيه مرخَّصة — وهو الحدُّ المعلَن في `Utur` للمقصور المنوَّن («ذَهَبَ فَتًى»
  ممتنعة، `shahid_baqi`).
ولم تُغيَّر الشفرةُ الحاكمة لأيٍّ منها: كلُّ تغييرٍ بعد قراءة الحالات تشغيلٌ على مادّةٍ مكشوفة لا يشهد للضابط.
-/
import Jisr.NassItarDawabit

namespace Jisr
namespace NassItar
namespace Qiyas

open Jisr.Utur Dabit

/-- أعدادُ المجال بترتيبٍ ثابت (يحسبها `tahaqquq/test_nass.py` من `cases.json` بالترتيب نفسه): الحالات؛ ثمّ الحكمُ المتوقَّع: مقبول، خطأ،
    «لا حكم»، بديلان؛ ثمّ الإطاراتُ البديلة؛ ثمّ ذواتُ الزوج؛ ثمّ الفئاتُ: موجب، حدّ، خارج، عموم، غموض. -/
def majalAadad : List Nat :=
  [halat.length] ++
  [Hukm.murakhkhas, .mumtani, .laHukm].map (fun d => (halat.filter (·.hukm == [d])).length) ++
  [(halat.filter (fun h => decide (2 ≤ h.hukm.length))).length,
   (halat.filter (fun h => decide (2 ≤ h.itar.length))).length,
   (halat.filter (·.zawj.isSome)).length] ++
  [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => (halat.filter (·.fia == f)).length)

/-- **المجالُ غيرُ فارغ ولا مائلٍ إلى «لا حكم»:** 50 حالة. والمتوقَّع: مقبول 25، وخطأ 20، و«لا حكم» 5، ولا بديلين في حكمٍ ولا في إطار؛
    و34 حالةً في 17 زوجًا. والفئات: موجب 19، وحدّ 20، وخارج 5، وعموم 6، وغموض 0 (بحث المؤلّفُ فلم يجد، `taalif.md`). -/
theorem majal : majalAadad = [50, 25, 20, 5, 0, 0, 34, 19, 20, 5, 6, 0] := by
  decide +kernel

/-- **النتيجة:** 61 صوابًا من 71 حقلًا (50 حكمًا و21 إطارًا): 8 نقوص تغطية، وتجاوزٌ واحد، وردٌّ خاطئٌ واحد؛ ولا قبولَ خاطئ، ولا خطأَ
    إطار، ولا رفضَ من القارئ. -/
theorem natija : ihsa (natayij halat) = ⟨61, 8, 1, 0, 1, 0, 0, 0, 0⟩ := by
  decide +kernel

/-- **بالفئات:** موجب 30 ونقوصٌ ثلاثة وردٌّ واحد، وحدّ 15 ونقوصٌ خمسة، وخارج 4 وتجاوزٌ واحد، وعموم 12، وغموض لا شيء. -/
theorem natija_fia :
    [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => ihsa ((natayij halat).filter (·.2.1 == f))) =
      [⟨30, 3, 0, 0, 1, 0, 0, 0, 0⟩, ⟨15, 5, 0, 0, 0, 0, 0, 0, 0⟩, ⟨4, 0, 1, 0, 0, 0, 0, 0, 0⟩, ⟨12, 0, 0, 0, 0, 0, 0, 0, 0⟩,
       ⟨0, 0, 0, 0, 0, 0, 0, 0, 0⟩] := by
  decide +kernel

/-- **والإخفاقاتُ العشرة بأسمائها**، كلُّها في حقل الحكم. -/
theorem akhta_1 :
    akhta (natayij halat) = [("N04", .hukm, .naqsTaghtiya), ("N21", .hukm, .naqsTaghtiya), ("N24", .hukm, .naqsTaghtiya),
      ("N28", .hukm, .naqsTaghtiya), ("N34", .hukm, .naqsTaghtiya), ("N35", .hukm, .naqsTaghtiya),
      ("N36", .hukm, .naqsTaghtiya), ("N38", .hukm, .naqsTaghtiya), ("N45", .hukm, .raddKhati), ("N46", .hukm, .tajawuz)] := by
  decide +kernel

/-- حقلُ الحكم في الحالة صواب. -/
def sawabHukm (i : String) : Bool := (natayij halat).any fun x => x.1 == i && x.2.2.1 == Haql.hukm && x.2.2.2 == Natija.sawab

/-- **تبديلُ علامة الإعراب** (الأزواجُ السبعة عشر): يتغيّر حكمُ المحرّك في ستّة عشر منها، ولا يتغيّر في N34/N35؛ **ويصيب الطرفان معًا
    في عشرة** — وفي ستّةٍ ممّا تغيّر صار أحدُ الطرفين «لا حكم» لا المتوقَّعَ (N03/N04، N20/N21، N23/N24، N27/N28، N36/N37، N38/N39؛
    ضبطه المراجع المستقلّ). ولا رفضَ من القارئ. -/
theorem azwaj_1 :
    (azwaj halat).length = 17 ∧ ((azwaj halat).filter (·.2.2)).length = 16 ∧
    (azwaj halat).filter (!·.2.2) = [("N34", "N35", false)] ∧
    ((azwaj halat).filter fun p => sawabHukm p.1 && sawabHukm p.2.1).length = 10 ∧ rafd halat = [] := by
  decide +kernel

/-- أسبابُ الحكم على إطار: الأدوار، و`hukmSitta`، و`asbabLaHukm`، و`qiraaSitta`، و`waslBase`. -/
structure SababItar where
  adwar : List Dawr
  hukm : Hukm
  asbab : List SababLaHukm
  qiraa : Hukm
  wasl : Bool
  deriving DecidableEq, Repr

/-- أسبابُ الحكم على كلّ إطارٍ في حالة. -/
def sababIkhfaq (i : String) : List SababItar :=
  match (halat.find? (·.ism == i)).bind (·.kalimat) with
  | some ws => (itarat ws).map fun x =>
      ⟨x.1, QawaidSitta.hukmSitta x.2, asbabLaHukm x.2, QawaidSitta.qiraaSitta x.2, waslBase x.2⟩
  | none => []

/-- **أسبابُ الإخفاقات العشرة على إطاراتها** (شاهدُ ما في الرأس):
    * N04 N21 N24 N28 N35: إطارُ المضاف إليه «لا حكم» بسببه `illaAkhir` وقراءةُ الستّة فيه «لا حكم»؛ وإطارُ المفعول ممتنعٌ من `waslBase`.
    * N34: «لا حكم» بسببه `irabBilHarf`؛ وإطارُ المفعول ممتنعٌ من `waslBase`. N36 N38: «لا حكم» بسببه `illaAkhir`.
    * N45 N46: إطارٌ واحدٌ ممتنعٌ من `waslBase` (حالُ الكلمة غيرُ حال موضعها)، وقراءةُ الستّة فيه مرخَّصة. -/
theorem asbab_akhta :
    ["N04", "N21", "N24", "N28", "N35", "N34", "N36", "N38", "N45", "N46"].map sababIkhfaq =
      [[⟨[.fil, .fail, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .laHukm, false⟩],
       [⟨[.fil, .fail, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .laHukm, false⟩],
       [⟨[.fil, .fail, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .laHukm, false⟩],
       [⟨[.fil, .fail, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .laHukm, false⟩],
       [⟨[.fil, .fail, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .laHukm, false⟩],
       [⟨[.fil, .fail, .mudafIlayh], .laHukm, [.irabBilHarf], .laHukm, true⟩, ⟨[.fil, .fail, .maful], .mumtani, [], .murakhkhas, false⟩],
       [⟨[.fil, .fail, .maful, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩],
       [⟨[.harfJarr, .majrur, .mudafIlayh], .laHukm, [.illaAkhir], .laHukm, true⟩],
       [⟨[.fil, .fail, .maful], .mumtani, [], .murakhkhas, false⟩],
       [⟨[.fil, .fail], .mumtani, [], .murakhkhas, false⟩]] := by
  decide +kernel

end Qiyas
end NassItar
end Jisr
