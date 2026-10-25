/-
# «هذا باب مجارى أواخر الكلم من العربية» عند سيبويه (الكتاب، س111–233)

**المصدر.** `sibawayhi.txt` المختوم (`a160f940…`)، الأسطر 111–233: من العنوان إلى ما قبل «هذا باب المسند والمسند إليه». ورقمُ السطر
خاصٌّ بهذا الملفّ. والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_majari.py` على المودَع موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/majari/wasf.md` بأعيانها): صنفُ الكلمة `Sinf`، ولفظُها لغير المتمكّن، وموضعُها
`Mawdi`. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ قارئٍ من النصّ** (P4 لم يُبنَ).

**المخرج** `Jawab`: علاماتُ آخرها في الموضع (`alamat`، واحدةٌ أو اثنتان) وهل هي بناءٌ لا يزول؛ أو `laYakun` (البابُ ينفي الموضعَ عن
الصنف)؛ أو `laHukm`.

**الأضربُ الأربعة.** «فالنصب والفتح في اللفظ ضرب واحد والجر والكسر فيه ضرب واحد وكذلك الرفع والضم والجزم والوقف» (س113–115): العلامةُ
تُسمّى باسم الحركة، والفرقُ بين الإعراب والبناء في `bina` وحده.

**ما هو تعيينُ البنّاء** (لا نصُّ الباب):
- **الاسمُ الذي لا ينصرف** رفعُه ضمّةٌ ونصبُه فتحة كالمتمكّن، بعموم «وحروف الإعراب للأسماء المتمكنة» (س119)؛ والبابُ لا ينصّ إلّا على
  جرّه مفتوحًا (س209) وانجراره بالألف واللام والإضافة (س226–227).
- **جمعُ المؤنّث** رفعُه ضمّة، بالعموم نفسه؛ والبابُ ينصّ على كسرة الجرّ والنصب (س169).
- **المضارعُ الساكنُ الآخر** نصبُه «لا حكم»: البابُ يذكر رفعَه ساكنًا وجزمَه بالحذف (س230–233) ولا يذكر نصبَه.
- **ما يُبنى** (الماضي والأمر ونونُ النسوة وغيرُ المتمكّن) علامتُه واحدةٌ في كلّ موضع، والموضعُ لا يغيّرها؛ إلّا الجرَّ في الفعل: «ليس في
  الأفعال المضارعة جر» (س125) يُطبَّق على المضارع كلّه ومنه نونُ النسوة. والماضي يقع موقعَ الاسم صفةً (س142–143)، فلا يُنفى عنه موضع.
- **غيرُ المتمكّن بلفظه** من أمثلة الباب وحدها (س138–140، س151–154)، و«حيث» ضمّةٌ وفتحة (`ghamid`: البابُ يذكرها في الضربين). وما سواها
  «لا حكم».
- **المعربُ بلا عامل** «لا حكم».

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/majari/tajmid.json`؛
`hawkama/منهج_الضوابط.md`). ونتيجتُها على الضابط في `Jisr/MajariKalimQiyas.lean`، لا هنا.
-/

namespace Jisr
namespace MajariKalim

/-! ## المدخل والمخرج -/

inductive Sinf
  | ismMutamakkin | ismLaYansarif | ismLaYansarifMuarraf | muthanna | jamMudhakkar | jamMuannath
  | mudari | mudariSakin | mudariIthnayn | mudariJam | mudariMukhataba | mudariNiswa | madi | amr | ghayrMutamakkin
  deriving DecidableEq, Repr

inductive Mawdi
  | raf | nasb | jarr | jazm | bilaAmil
  deriving DecidableEq, Repr

structure Kalima where
  sinf : Sinf
  lafz : String
  mawdi : Mawdi
  deriving DecidableEq, Repr

inductive Alama
  | damma | fatha | kasra | sukun | alif | waw | ya | thubutNun | hadhfNun | hadhfAkhir
  deriving DecidableEq, Repr

inductive Jawab
  | alamat (l : List Alama) (bina : Bool)
  | laYakun
  | laHukm
  deriving DecidableEq, Repr

/-! ## ما يُعرب -/

def murab (a : Alama) : Jawab := .alamat [a] false

/-- الأسماءُ: «ليس في الأسماء جزم» (س123). -/
def ism (r n j : Alama) : Mawdi → Jawab
  | .raf => murab r
  | .nasb => murab n
  | .jarr => murab j
  | .jazm => .laYakun
  | .bilaAmil => .laHukm

/-- المضارع: «ليس في الأفعال المضارعة جر» (س125). -/
def fil (r : Jawab) (n : Jawab) (z : Jawab) : Mawdi → Jawab
  | .raf => r
  | .nasb => n
  | .jazm => z
  | .jarr => .laYakun
  | .bilaAmil => .laHukm

/-! ## ما يُبنى -/

/-- غيرُ المتمكّن من أمثلة الباب: الأسماء (س138–140) والحروف (س151–154). -/
def mabni : List (String × List Alama) := [
  ("حيث", [.fatha, .damma]), ("أين", [.fatha]), ("كيف", [.fatha]),
  ("أولاء", [.kasra]), ("حذار", [.kasra]), ("بداد", [.kasra]),
  ("قبل", [.damma]), ("بعد", [.damma]),
  ("من", [.sukun]), ("كم", [.sukun]), ("قط", [.sukun]), ("إذ", [.sukun]),
  ("سوف", [.fatha]), ("ثم", [.fatha]),
  ("الباء", [.kasra]), ("باء الإضافة", [.kasra]), ("اللام", [.kasra]), ("لام الإضافة", [.kasra]),
  ("منذ", [.damma]), ("هل", [.sukun]), ("بل", [.sukun]), ("قد", [.sukun])]

def mabniOf (lafz : String) : Jawab :=
  match mabni.find? (·.1 == lafz) with
  | some (_, l) => .alamat l true
  | none => .laHukm

/-! ## الجواب -/

def jawab (k : Kalima) : Jawab :=
  match k.sinf with
  | .ismMutamakkin => ism .damma .fatha .kasra k.mawdi
  | .ismLaYansarif => ism .damma .fatha .fatha k.mawdi
  | .ismLaYansarifMuarraf => ism .damma .fatha .kasra k.mawdi
  | .muthanna => ism .alif .ya .ya k.mawdi
  | .jamMudhakkar => ism .waw .ya .ya k.mawdi
  | .jamMuannath => ism .damma .kasra .kasra k.mawdi
  | .mudari => fil (murab .damma) (murab .fatha) (murab .sukun) k.mawdi
  | .mudariSakin => fil (murab .sukun) .laHukm (murab .hadhfAkhir) k.mawdi
  | .mudariIthnayn | .mudariJam | .mudariMukhataba => fil (murab .thubutNun) (murab .hadhfNun) (murab .hadhfNun) k.mawdi
  | .mudariNiswa => fil (.alamat [.sukun] true) (.alamat [.sukun] true) (.alamat [.sukun] true) k.mawdi
  | .madi => .alamat [.fatha] true
  | .amr => .alamat [.sukun] true
  | .ghayrMutamakkin => mabniOf k.lafz

/-- بديلان في العلامة. -/
def ghamid (k : Kalima) : Bool :=
  match jawab k with
  | .alamat l _ => l.length ≥ 2
  | _ => false

/-! ## الأسانيد (قطعٌ حرفيّة؛ يفحصها `tahaqquq/test_majari.py` موصولةَ الأسطر) -/

def asanid : List (String × Nat × Nat × String) := [
  ("thamaniya", 112, 113, "وهي تجري على ثماني مجار على النصب والجر والرفع والجزم والفتح والضم والكسر والوقف"),
  ("arbaa", 113, 115, "فالنصب والفتح في اللفظ ضرب واحد والجر والكسر فيه ضرب واحد وكذلك الرفع والضم والجزم والوقف"),
  ("mutamakkina", 118, 120, "فالرفع والجر والنصب والجزم لحروف الإعراب وحروف الإعراب للأسماء المتمكنة وللأفعال المضارعة"),
  ("ismNasbJarrRaf", 122, 123, "والنصب في الأسماء رأيت زيدا والجر مررت بزيد والرفع هذا زيد وليس في الأسماء جزم"),
  ("filNasbRafJazm", 124, 125, "والنصب في المضارع من الأفعال لن يفعل والرفع سيفعل والجزم لم يفعل وليس في الأفعال المضارعة جر"),
  ("ghayrMutamakkina", 135, 136, "وأما الفتح والكسر والضم والوقف فللأسماء غير المتمكنة"),
  ("fathIsm", 138, 139, "فالفتح في الأسماء قولهم حيث وأين وكيف"),
  ("damm", 139, 139, "نحو حيث وقبل وبعد"),
  ("waqfIsm", 140, 140, "والوقف نحو من وكم وقط وإذ"),
  ("madiFath", 140, 141, "والفتح في الأفعال التي لم تجر مجرى المضارعة قولهم ضرب"),
  ("amrWaqf", 149, 149, "الوقف قولهم اضرب في الأمر لم يحركوها"),
  ("harfFath", 151, 152, "والفتح في الحروف التي ليست إلا لمعنى وليست بأسماء ولا أفعال قولهم سوف"),
  ("harfKasr", 152, 152, "والكسر فيها قولهم في باء الإضافة ولامها بزيد ولزيد"),
  ("harfDamm", 153, 153, "والضم فيها منذ"),
  ("harfWaqf", 153, 154, "والوقف فيها قولهم من وهل وبل وقد"),
  ("laDamm", 154, 154, "لا ضم في الفعل"),
  ("muthannaRaf", 157, 157, "يكون في الرفع ألفا"),
  ("muthannaJarr", 158, 158, "ويكون في الجر ياء مفتوحا ما قبلها"),
  ("muthannaNasb", 159, 159, "ويكون في النصب كذلك"),
  ("jamMudhakkar", 166, 167, "إلا أنها واو مضموم ما قبلها في الرفع وفي الجر والنصب ياء مكسور ما قبلها"),
  ("jamMuannath", 169, 169, "ومن ثم جعلوا تاء الجمع في الجر والنصب مكسورة"),
  ("thubutNun", 177, 177, "فجعلوا إعرابه في الرفع ثبات النون"),
  ("hadhfNun", 181, 182, "فأثبتوها في الرفع وحذفوها في الجزم"),
  ("nasbJazm", 182, 182, "ووافق النصب الجزم في الحذف"),
  ("jamFil", 185, 186, "وكذلك إذا لحقت الأفعال علامة للجمع لحقتها زائدتان"),
  ("mukhataba", 189, 189, "وكذلك إذا ألحقت التأنيث في المخاطبة"),
  ("niswa", 193, 194, "وأسكنت ما كان في الواحد حرف الأعراب"),
  ("laYansarifJarr", 209, 209, "فيكون في موضع الجر مفتوحا"),
  ("injarra", 226, 227, "وجميع ما لا ينصرف إذا أدخلت عليه الألف واللام أو أضيف انجر"),
  ("hadhfAkhir", 230, 231, "وأعلم أن الآخر إذا كان يسكن في الرفع حذف في الجزم"),
  ("lamYarmi", 232, 233, "وذلك قولك لم يرم ولم يغز ولم يخش وهو في الرفع ساكن الآخر")]

/-! ## مبرهنات (خواصُّ التعيين على مجاله؛ والضابطُ يشهد أنّه غيرُ فارغ: `Jisr/MajariKalimQiyas.lean`) -/

/-- **لا جزمَ في الأسماء** (بالاستنفاد): لكلّ صنفٍ من الأسماء الستّة المعربة، الجزمُ `laYakun`. -/
theorem la_jazm_fi_asma (l : String) :
    [Sinf.ismMutamakkin, .ismLaYansarif, .ismLaYansarifMuarraf, .muthanna, .jamMudhakkar, .jamMuannath].all
      (fun s => jawab ⟨s, l, .jazm⟩ == .laYakun) = true := by
  rfl

/-- **ولا جرَّ في المضارع** (بالاستنفاد): لكلّ صنفٍ من المضارع، الجرُّ `laYakun`. -/
theorem la_jarr_fi_mudari (l : String) :
    [Sinf.mudari, .mudariSakin, .mudariIthnayn, .mudariJam, .mudariMukhataba, .mudariNiswa].all
      (fun s => jawab ⟨s, l, .jarr⟩ == .laYakun) = true := by
  rfl

/-- **ما يُبنى لا يغيّره الموضع** (تعريفيّة): الماضي والأمر علامتُهما واحدةٌ في كلّ موضع. -/
theorem mabni_la_yataghayyar (l l' : String) (m m' : Mawdi) :
    jawab ⟨.madi, l, m⟩ = jawab ⟨.madi, l', m'⟩ ∧ jawab ⟨.amr, l, m⟩ = jawab ⟨.amr, l', m'⟩ := by
  simp [jawab]

/-- **الإعرابُ بالحرف** (على الشاهد): المثنّى والجمعُ على حدّه وما لحقته علامةُ الفاعلين. -/
theorem irab_bil_harf :
    jawab ⟨.muthanna, "", .raf⟩ = murab .alif ∧ jawab ⟨.muthanna, "", .nasb⟩ = murab .ya ∧
    jawab ⟨.jamMudhakkar, "", .raf⟩ = murab .waw ∧
    jawab ⟨.mudariIthnayn, "", .raf⟩ = murab .thubutNun ∧ jawab ⟨.mudariIthnayn, "", .nasb⟩ = murab .hadhfNun ∧
    jawab ⟨.mudariSakin, "", .jazm⟩ = murab .hadhfAkhir := by
  decide

/-- **ما لا ينصرف** (على الشاهد): جرُّه فتحة، ومعرَّفًا كسرة. -/
theorem la_yansarif :
    jawab ⟨.ismLaYansarif, "", .jarr⟩ = murab .fatha ∧ jawab ⟨.ismLaYansarifMuarraf, "", .jarr⟩ = murab .kasra := by
  decide

/-- **«حيث» علامتان** (على الشاهد)، وغيرُ أمثلة الباب «لا حكم». -/
theorem haythu_wa_ghayruha :
    jawab ⟨.ghayrMutamakkin, "حيث", .bilaAmil⟩ = .alamat [.fatha, .damma] true ∧
    ghamid ⟨.ghayrMutamakkin, "حيث", .raf⟩ = true ∧
    jawab ⟨.ghayrMutamakkin, "متى", .bilaAmil⟩ = .laHukm := by
  decide

end MajariKalim
end Jisr
