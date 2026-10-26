/-
# صكُّ الجملة على ضابطه المجمَّد — النتيجةُ على الشفرة الحاليّة

**ما يُقارَن.** لكلّ حالةٍ من `Dawabit.halatQ` و`Dawabit.halatS` و`Dawabit.halatM` (كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والنطاق،
وفي سياقه ما حُقن آليًّا — `taalif.md` —، وجُمّدت ببصمتها في `tahaqquq/dawabit/sakk/tajmid.json` قبل الشفرة) حقولُها المسؤولة:
- **القوّة:** `awwal` بمخرج `awwal`، و`thani` بمخرج `thani`.
- **السبب:** `sabab` بمخرج `sabab`.
- **المرجع:** `marji` بمخرج `marji`.

والمقارنةُ قائمتين **مجموعتين** (`qarin`)، على المواصفة:
- التساوي صواب.
- و«لا حكم» حيث المتوقَّعُ حكمٌ نقصُ تغطية (`naqsTaghtiya`).
- وحكمٌ حيث المتوقَّعُ «لا حكم» تجاوز (`tajawuz`).
- وفي `غموض`: بعضُ البديلين اختيارٌ بلا مرجّح (`ikhtiyar`).
- وما سوى ذلك خطأ (`khata`)، ومنه مخرجٌ ذو بديلين حيث المتوقَّعُ أحدُهما.

**الوسم.** العدُّ «مبرهن على الشاهد» (`decide` على الحالات المجمَّدة). ومعناه موافقةُ الشفرة لقراءةٍ مستقلّةٍ للنطاق، لا تغطيةُ اللغة:
الحالاتُ مؤلَّفة لا عيّنةٌ من استعمال.

**التشغيلات.** المبرهناتُ هنا على الشفرة الحاليّة دائمًا. وسجلُّ كلّ تشغيلٍ ملفٌّ في `tahaqquq/dawabit/sakk/` (`natija_1.json` …)، ويفحص
`tahaqquq/test_sakk.py` أنّ بصمةَ الأوّل ثابتةٌ فيه، وأنّ كلّ سجلٍّ بعده يحمل بصمةَ ما قبله، وأنّ آخرَها لبصمة الشفرة الحاليّة وأعدادُه هي
أعدادُ هذه المبرهنات.
- `natija_1.json`: التشغيلُ الأوّل على الشفرة المجمَّدة في `1112732`: 48 صوابًا من 54. الإخفاقاتُ ستّة:
  - S01 (غموض، القوّةُ الأولى): اختيارٌ بلا مرجّح، فالشفرةُ تُخرج الخبرَ وحده.
  - S14 (غموض) وS24 (حدّ)، السبب: نقصُ تغطية.
  - S25 (موجب)، السبب: خطأ؛ الشفرةُ تُخرج الوجهين حيث المتوقَّعُ السببيّة.
  - S38 وS42 (خارج)، المرجع: تجاوز؛ الشفرةُ تحكم بالاحتمال في الإشارة إلى اثنين، والنطاقُ لا يحكم فيها.
-/
import Jisr.SakkJumla
import Jisr.SakkJumlaDawabit

namespace Jisr
namespace SakkJumla
namespace Qiyas

open Dawabit

inductive Natija
  | sawab | naqsTaghtiya | tajawuz | ikhtiyar | khata
  deriving DecidableEq, Repr

/-- القائمتان مجموعتين. -/
def sawa {α : Type} [DecidableEq α] (a b : List α) : Bool := a.all (b.contains ·) && b.all (a.contains ·)

/-- المتوقَّعُ `taw` والمخرجُ `makh`، و`la` قيمةُ «لا حكم» في الحقل. -/
def qarin {α : Type} [DecidableEq α] (la : α) (f : Fia) (taw makh : List α) : Natija :=
  if sawa taw makh then .sawab
  else if makh = [la] then .naqsTaghtiya
  else if taw = [la] then .tajawuz
  else if f = .ghumud && makh.all (taw.contains ·) then .ikhtiyar
  else .khata

inductive Haql
  | awwal | thani | sabab | marji
  deriving DecidableEq, Repr

def natayij : List (String × Fia × Haql × Natija) :=
  halatQ.flatMap (fun h =>
    [(h.ism, h.fia, Haql.awwal, qarin Quwwa.laHukm h.fia h.awwal [awwal h.dakhil]),
     (h.ism, h.fia, Haql.thani, qarin Quwwa.laHukm h.fia h.thani (thani h.dakhil))]) ++
  halatS.map (fun h => (h.ism, h.fia, Haql.sabab, qarin Sabab.laHukm h.fia h.sabab (sabab h.dakhil))) ++
  halatM.map (fun h => (h.ism, h.fia, Haql.marji, qarin Marji.laHukm h.fia h.marji [marji h.dakhil]))

structure Ihsa where
  sawab : Nat
  naqsTaghtiya : Nat
  tajawuz : Nat
  ikhtiyar : Nat
  khata : Nat
  deriving DecidableEq, Repr

def ihsa (l : List (String × Fia × Haql × Natija)) : Ihsa :=
  let c (n : Natija) := (l.filter (fun x => x.2.2.2 == n)).length
  ⟨c .sawab, c .naqsTaghtiya, c .tajawuz, c .ikhtiyar, c .khata⟩

def ihsaFia (f : Fia) : Ihsa := ihsa (natayij.filter (fun x => x.2.1 == f))

/-- الإخفاقاتُ بأسمائها: (الحالة، الحقل، النتيجة). -/
def akhta : List (String × Haql × Natija) :=
  (natayij.filter (fun x => x.2.2.2 != .sawab)).map (fun x => (x.1, x.2.2.1, x.2.2.2))

/-! ## المقارنة (على الشاهد) -/

/-- **المجموعتان**: الترتيبُ لا يهمّ، والبعضُ في الغموض اختيار وفي غيره خطأ، والزائدُ خطأ، والامتناعُ نقصُ تغطية، والحكمُ حيث لا حكمَ تجاوز. -/
theorem qarin_shawahid :
    qarin Sabab.laHukm .mujib [.illa, .ghayrMadhkur] [.ghayrMadhkur, .illa] = .sawab ∧
    qarin Sabab.laHukm .ghumud [.illa, .ghayrMadhkur] [.illa] = .ikhtiyar ∧
    qarin Sabab.laHukm .mujib [.illa, .ghayrMadhkur] [.illa] = .khata ∧
    qarin Sabab.laHukm .mujib [.illa] [.illa, .ghayrMadhkur] = .khata ∧
    qarin Sabab.laHukm .mujib [.illa] [.laHukm] = .naqsTaghtiya ∧
    qarin Sabab.laHukm .kharij [.laHukm] [.illa] = .tajawuz := by
  decide

/-! ## النتيجةُ على الشفرة الحاليّة (على الشاهد) -/

/-- عددُ المتوقَّع في حقلٍ: «لا حكم»، وقيمةٌ واحدةٌ غيرُه، وبديلان فأكثر. -/
def tawzi {α : Type} [DecidableEq α] (la : α) (l : List (List α)) : List Nat :=
  [(l.filter (· = [la])).length, (l.filter (fun x => x.length = 1 && x ≠ [la])).length,
   (l.filter (fun x => decide (2 ≤ x.length))).length]

/-- أعدادُ المجال بترتيبٍ ثابت (يحسبها `tahaqquq/test_sakk.py` من `cases.json` بالترتيب نفسه): حالاتُ الأنواع الثلاثة، والحقولُ المسؤولة؛
    ثمّ لكلّ حقلٍ (`awwal`، `thani`، `sabab`، `marji`) متوقَّعُه: «لا حكم»، وقيمةٌ واحدةٌ غيرُه، وبديلان فأكثر. -/
def majalAadad : List Nat :=
  [halatQ.length, halatS.length, halatM.length, natayij.length] ++
  tawzi Quwwa.laHukm (halatQ.map (·.awwal)) ++ tawzi Quwwa.laHukm (halatQ.map (·.thani)) ++
  tawzi Sabab.laHukm (halatS.map (·.sabab)) ++ tawzi Marji.laHukm (halatM.map (·.marji))

/-- **المجالُ غيرُ فارغ ولا مائلٍ إلى «لا حكم»:** 12 حالةَ قوّة، و18 سببًا، و12 مرجعًا، و54 حقلًا مسؤولًا. ومتوقَّعُ القوّة الأولى:
    «لا حكم» 0، وقيمةٌ واحدة 11، وبديلان 1؛ والثانية: 0، و11، و1؛ والسبب: 1، و13، و4؛ والمرجع: 6، و6، و0. -/
theorem majal : majalAadad = [12, 18, 12, 54, 0, 11, 1, 0, 11, 1, 1, 13, 4, 6, 6, 0] := by
  decide +kernel

/-- **النتيجة:** 48 صوابًا من 54، ونقصُ تغطيةٍ 2، وتجاوزٌ 2، واختيارٌ بلا مرجّح 1، وخطأٌ 1 (على الشفرة المجمَّدة؛ `natija_1.json`). -/
theorem natija : ihsa natayij = ⟨48, 2, 2, 1, 1⟩ := by
  decide +kernel

/-- **بالفئات:** موجب 21 من 22 (خطأٌ واحد)، حدّ 8 من 9 (نقصٌ واحد)، خارج 2 من 4 (تجاوزان)، عموم 11 من 11، غموض 6 من 8 (نقصٌ واختيار). -/
theorem natija_fia :
    [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map ihsaFia =
      [⟨21, 0, 0, 0, 1⟩, ⟨8, 1, 0, 0, 0⟩, ⟨2, 0, 2, 0, 0⟩, ⟨11, 0, 0, 0, 0⟩, ⟨6, 1, 0, 1, 0⟩] := by
  decide +kernel

/-- **الإخفاقاتُ بأسمائها.** -/
theorem akhta_1 :
    akhta = [("S01", .awwal, .ikhtiyar), ("S14", .sabab, .naqsTaghtiya), ("S24", .sabab, .naqsTaghtiya),
             ("S25", .sabab, .khata), ("S38", .marji, .tajawuz), ("S42", .marji, .tajawuz)] := by
  decide +kernel

end Qiyas
end SakkJumla
end Jisr
