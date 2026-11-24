import Madlul.QismaJadwal
import Madlul.Tayin

/-!
# القسمة: الكون والإنسان والحياة (القطعة الأولى)

قولُ المالك في الجلسة 2026-11-24 (14:02 بتوقيت عمّان): «… كما  تُودَع قسمة تغطي الكون والإنسان والحياةوتغطي («أحياء وأشياء»،
ثمّ الكواكب والجبال) جدولًا …»؛ ثمّ (21:10): «موافق انت خبير نفذ ومعك الأذن بالختم والايداع واعتماد المصادر».

الجدولُ مودَعٌ «معلومات-سابقة»: «جدول القسمة — القطعة الأولى» (qisma.tsv)، مولَّدٌ بـ`scripts/bina_qisma.py` ومنه
`Madlul/QismaJadwal.lean`. صفوفُه من الشخصية ج1 (a1.txt): س523 «الفكرة الكلية عن الكون والإنسان والحياة»، وس321 (الموجوداتُ في
الكون: الأرض والشمس والقمر والنجوم والحيوان والإنسان والدواب والإبل والجبال، وما وراء الكون «مما لا يقع تحت الحس»)؛ ومن اللسان
س24829 «الكوكب والكوكبة: النجم» (فالنجومُ تحت الكواكب)؛ ومن قول المالك نفسِه («أحياء وأشياء»، «الكواكب»). وأبُ ما جعله المالك أو
النصُّ في الكون تعيينُ البنّاء، معلَنٌ في عمود `wasm` من المودَع.

**ما يزيده هذا الملفّ:** لا يُكتب «حيٌّ» أو «شيءٌ» لموجودٍ باليد. يُعيَّن الموجودُ قسمًا من أقسام `Tayin.Qism` (تعيينُ البنّاء، `tayin`)،
ثمّ تُقرأ حياتُه من فصول ذلك القسم (`Tayin.fusul`، المطابَقة للمودَع المختوم `ajnas.tsv` بـ`test_ajnas.py`) بـ`Tayin.hayat`: فما حياتُه
«نعم» تحت «أحياء»، وما حياتُه «لا» تحت «أشياء» (`mawdi`). وما لا تعيينَ له «لا حكم» (لا «ممتنع»).

مبرهن (لكلّ):
- `hayy_iff`: الموجودُ تحت «أحياء» إذا وفقط إذا كان مُعيَّنًا قسمًا حياتُه «نعم» في فصوله.
- `la_tayin_la_mawdi`: ما لا تعيينَ له لا موضعَ له.

مبرهن على الشاهد (decide على الجدول):
- `shajara_sahiha`: كلُّ أبٍ في الجدول اسمٌ فيه.
- `asma_mutamayiza`: لا اسمَ مكرَّر.
- `judhur`: الجذورُ الأربعة: الكون والإنسان والحياة وما وراء الكون.
- `ghayb_la_abna`: ما ليس محسوسًا لا ابنَ له.
- `ghayb_la_tayin`: ما ليس محسوسًا لا يُعيَّن قسمًا.
- `ahya`: تحت «أحياء» الإنسانُ والحيوانُ والدوابُّ والإبل.
- `ashya`: تحت «أشياء» الأرضُ والشمسُ والقمرُ والكواكبُ والنجومُ والجبال.
- `la_hukm`: الكونُ والحياةُ وما وراء الكون و«أحياء» و«أشياء» بلا موضع.

لم يُبنَ: النباتُ (لا صفَّ له في المصدرين بعدُ)؛ وأبٌ آخرُ غيرُ الكون لما في س321؛ ووصلُ القسمة بالعقد الناظم (`Aql/NizamMarifi.lean`،
الطلب #143) ولا بالمحرّك؛ و«مفهوم» لأيّ صفّ: المودَعُ «معلومات-سابقة» لا «واقع مختوم».
-/

namespace Madlul.Qisma
open Madlul.Tayin

/-- صفُّ القسمة. -/
structure Saff where
  raqm : Nat
  ism : String
  ab : String
  mahsus : Bool
deriving DecidableEq

/-- صفوفُ المودَع. -/
def jadwal : List Saff := QismaJadwal.sufuf.map fun (r, i, a, m) => ⟨r, i, a, m⟩

def asma : List String := jadwal.map (·.ism)

/-- تعيينُ البنّاء: قسمُ كلّ موجودٍ من `Tayin.Qism`. -/
def tayin : String → Option Qism
  | "الإنسان" => some .insan
  | "الحيوان" => some .hayawan
  | "الدواب" => some .hayawan
  | "الإبل" => some .hayawan
  | "الأرض" => some .jamad
  | "الشمس" => some .jamad
  | "القمر" => some .jamad
  | "الكواكب" => some .jamad
  | "النجوم" => some .jamad
  | "الجبال" => some .jamad
  | _ => none

/-- موضعُ الموجود: «أحياء» أو «أشياء»، من حياة فصول قسمه. -/
def mawdi (s : String) : Option String :=
  (tayin s).map fun q => if hayat (fusul q) = .naam then "أحياء" else "أشياء"

theorem hayy_iff (s : String) :
    mawdi s = some "أحياء" ↔ ∃ q, tayin s = some q ∧ hayat (fusul q) = .naam := by
  unfold mawdi
  cases h : tayin s with
  | none => simp
  | some q =>
    by_cases hq : hayat (fusul q) = .naam
    · simp [hq]
    · simp [hq]

theorem la_tayin_la_mawdi (s : String) (h : tayin s = none) : mawdi s = none := by
  simp [mawdi, h]

theorem shajara_sahiha : jadwal.all (fun s => s.ab = "" || asma.contains s.ab) = true := by decide +kernel

theorem asma_mutamayiza : asma.Nodup := by decide +kernel

theorem judhur : (jadwal.filter (·.ab = "")).map (·.ism) = ["الكون", "الإنسان", "الحياة", "ما وراء الكون"] := by
  decide +kernel

theorem ghayb_la_abna :
    jadwal.all (fun s => s.mahsus || jadwal.all (fun t => t.ab != s.ism)) = true := by decide +kernel

theorem ghayb_la_tayin : jadwal.all (fun s => s.mahsus || (tayin s.ism).isNone) = true := by decide +kernel

theorem ahya : (jadwal.filter (fun s => mawdi s.ism = some "أحياء")).map (·.ism) =
    ["الإنسان", "الحيوان", "الدواب", "الإبل"] := by decide +kernel

theorem ashya : (jadwal.filter (fun s => mawdi s.ism = some "أشياء")).map (·.ism) =
    ["الأرض", "الشمس", "القمر", "الكواكب", "النجوم", "الجبال"] := by decide +kernel

theorem la_hukm : (jadwal.filter (fun s => (mawdi s.ism).isNone)).map (·.ism) =
    ["الكون", "الحياة", "ما وراء الكون", "أحياء", "أشياء"] := by decide +kernel

end Madlul.Qisma
