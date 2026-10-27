import SLGE.Wad
import SLGE.Maqam

/-!
# الضميرُ البارز: الاتّصالُ والانفصال والترتيب في قطر الندى (س124–128) والألفية (س105–119)

**الطلب.** قولُ المالك 2026-10-28 (لفظُه ووقتُه، 00:33 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها): «يجب الاستفادة من ما لم نغطه وموجود في المراجع سواء
استنتجته انت او موجود في المرفق وعمل lean له شرط ان يكون متناسق ومتكامل ومترابط مع البرهان واالحساب وفق الدستور وأفضل الممارسات …
نفذ انت والوكلاء». والضميرُ في Lean القائمة قائمةُ ألفاظٍ بسماتها (`SLGE.Maqam.damair`)، وأوّلُ المعارف في `SLGE.Wad.maarif`، بلا حكمٍ على
صورته. واختيارُ هذه القطعة بعد أسماء الإشارة، ونطاقُها، قرارُ البنّاء.

**المصدر.** `qatr.txt` المختوم (`2d9241be…`) الأسطر 124–128، و`alfiyya.txt` المختوم (`13b351a0…`) الأسطر 105–119 (والسطرُ 108 علامةُ صفحة).
والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_damir.py` على المودَعين موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/damir/wasf.md` بأعيانها): العاملُ `Amil`، والموقعُ `Mawqi`، ورتبةُ الضمير المتّصل
بالعامل قبل المسؤول عنه `qablahu` (أو لا شيء)، ورتبةُ المسؤول عنه `Rutba`، وصورتُه `Shakl`، والضرورة. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ
قارئٍ من النصّ.**

**المخرج** `Jawab`: الحكمُ `Hukm` (`maqbul` أو `khata` أو `laHukm`)، والدرجةُ قائمةً `List Daraja`: درجةٌ واحدة، أو درجتان حيث يحكم النطاقُ
على الصورة نفسِها بدرجتين من مصدرين أو قائلين، ولا تحمل الحقولُ ما يفرّق بينهما. وحين لا يكون الحكمُ «مقبولًا» فالدرجةُ `[bila]`.

**الحكم** (`jawab`)، بالترتيب:
1. **اتّساقُ الحقول.** «ابتداء» مع «لا_عامل» وحده، وبلا ضميرٍ قبله؛ وما خالف ذلك «لا حكم».
2. **الابتداء** (`ibtidaJ`): المتّصلُ خطأ («وذو اتصال منه ما لا يبتدا»، ألفيّة س106)، والمنفصلُ مقبول («كأنت وهو سم بالضمير»، س105؛ «وذو
   إرتفاع وانفصال أنا هو»، س113).
3. **بعد «إلا»** (`illaJ`): المتّصلُ خطأ «اختيارا» («ولا يلي إلا اختيارا أبدا»، س106)، وفي الضرورة «لا حكم»؛ والمنفصلُ مقبول، إذ لا يمكن الوصل
   («ولا فصل مع إمكان الوصل»، قطر س126–127؛ «وفي اختيار لا يجيء المنفصل إذ تأتى أن يجئ المتصل»، ألفيّة س115).
4. **يلي العامل، والعاملُ يتعدّى إلى واحدٍ أو اسمٌ مضاف** (`asliJ`): المتّصلُ مقبول، والمنفصلُ خطأ «في اختيار»، وفي الضرورة «لا حكم» (الموضعان
   السابقان). فإن كان قبله ضميرٌ متّصلٌ برتبته نفسِها فـ«لا حكم»: لا يتعرّض النطاقُ لاتّحاد الرتبة إلّا في باب الترتيب.
5. **يلي عاملًا لمفعولين أو «ظنّ» أو «كان»، وقبله ضميرٌ متّصل** (`tartibJ`):
   - **الأوّلُ أخصّ** (المتكلّمُ أخصُّ من المخاطَب، والمخاطَبُ من الغائب): الوجهان مقبولان («وقدم الأخص في اتصال وقدمن ما شئت في اتفصال»، س118).
     ودرجتُهما:
     - لمفعولين («سلنيه»): المتّصلُ [`rajih`، `sawa`]، والمنفصلُ [`marjuh`، `sawa`]. فالقطرُ يجعل الفصلَ فيه «بمرجوحية» (س127)، والألفيّةُ
       «وصل أو افصل» بلا تفضيل (س116).
     - «ظنّ» و«كان» («ظننتكه»، «كنته»، «خلتنيه»): المتّصلُ والمنفصلُ كلاهما [`rajih`، `marjuh`]. فالقطرُ يجعل الفصلَ فيهما «برجحان» (س127–128)،
       وابنُ مالك يختار الاتّصال وغيرُه الانفصال («واتصالا أختار غيري اختار الانفصالا»، س117).
   - **الرتبةُ واحدة**: المنفصلُ مقبول، والمتّصلُ خطأ («وفي اتحاد الرتبة الزم فصلا»، س119)، إلّا الغائبين فمقبولٌ مرجوح («وقد يبيح الغيب فيه
     وصلا»، س119).
   - **الثاني أخصّ**: المنفصلُ مقبول («وقدمن ما شئت في اتفصال»)، والمتّصلُ خطأ («وقدم الأخص في اتصال»).
6. **يلي عاملًا لمفعولين أو «ظنّ» أو «كان» ولا ضميرَ قبله:** «لا حكم». الترتيبُ في النطاق بين ضميرين.

**ما هو تعيينُ البنّاء** (لا نصُّ النطاق):
- رجحانُ الاتّصال في «سلنيه» عند القطر من مرجوحيّة الفصل فيه، ورجحانُه في «ظننتكه» و«كنته» عند ابن مالك من اختياره.
- ما لا يفرّق بينه الحقلُ (القطرُ أم الألفيّة، ابنُ مالكٍ أم غيرُه) قائمةُ درجتين، لا اختيار.
- الضرورةُ لا تغيّر إلّا ما قُيّد «باختيار» («ولا يلي إلا اختيارا»، «وفي اختيار لا يجيء المنفصل»)، فتجعله «لا حكم».
- المنفصلُ بعد «إلا» مقبولٌ من «مع إمكان الوصل» و«إذ تأتى أن يجئ المتصل» بمفهومهما: الوصلُ لا يمكن بعدها.
- قواعدُ الترتيب (س118–119) على العوامل الثلاثة وحدها، و«يلي العامل» مع ضميرٍ قبله برتبته في غيرها «لا حكم».
- الأخصّيّةُ ترتيبُ الرتب الثلاث المتكلّمُ فالمخاطَبُ فالغائب، وهي ترتيبُ الشخص في سمات `SLGE.Maqam` (`akhass_shakhs`).

**الصلة بقطع Lean القائمة:**
- `awwal_maarif`: أوّلُ `SLGE.Wad.maarif` «الضمير».
- `akhass_shakhs`: رتبةُ الضمير من سمته في `SLGE.Maqam.damair` (الشخصُ 1 و2 و3)، والأخصّيّةُ هي الأقلُّ شخصًا؛ وصورُ `damair` الأربعَ عشرةَ
  منفصلةٌ كلُّها، ومقبولةٌ في الابتداء (`damair_ibtida`).

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/damir/tajmid.json`؛
`hawkama/منهج_الضوابط.md`). ونتيجتُها على الضابط في `Jisr/DamirQiyas.lean`، لا هنا.

**المبرهنات** (بالمعيار الموحَّد في `Nizam/Asas.lean`)، وهي خواصُّ هذا التعيين على مجاله، لا قوانينُ في اللغة:
- تعريفيّة: `ibtida_muttasil_khata`، `ibtida_munfasil_maqbul`، `illa_muttasil`، `illa_munfasil_maqbul`، `fasl_maa_imkan`، `tartib_munfasil_maqbul`،
  `tartib_muttasil_iff`، `darura_la_tughayyir_illa_ikhtiyar`، `ghayr_maqbul_bila_daraja`، `la_hukm_iff`. وكلُّها مكمَّمةٌ على كلّ مدخل، وبرهانُها
  تفكيكُ الحالات على مجالٍ منتهٍ.
- لكلّ: `akhass_shakhs` (على الشخص الطبيعيّ بحرف المعيار).
- على الشاهد: `awwal_maarif`، `damair_ibtida`، `shawahid`.

**حدُّه.** المدخلُ تحليلٌ يُعطى؛ ولا مستترَ ولا نونَ وقاية ولا عددَ ولا جنس؛ والدرجةُ قائمةٌ حيث يختلف المصدران، لا مرجّحَ بينهما؛ ولا وصلَ بالقارئ
ولا بالمحرّك.
-/

namespace Jisr
namespace Damir

/-- العاملُ في الضمير المسؤول عنه. -/
inductive Amil
  | filWahid    -- فعلٌ يتعدّى إلى واحد
  | filIthnayn  -- فعلٌ يتعدّى إلى مفعولين ليس أصلُهما مبتدأً وخبرًا
  | zann        -- «ظنّ» وأخواتُها
  | kana        -- «كان» وأخواتُها
  | ism         -- اسمٌ مضافٌ إلى الضمير
  | laAmil      -- مبتدأٌ في أوّل الكلام
  deriving DecidableEq, Repr

inductive Mawqi | yali | badIlla | ibtida
  deriving DecidableEq, Repr

inductive Rutba | mutakallim | mukhatab | ghaib
  deriving DecidableEq, Repr

inductive Shakl | muttasil | munfasil
  deriving DecidableEq, Repr

structure Dakhil where
  amil : Amil
  mawqi : Mawqi
  qablahu : Option Rutba
  rutba : Rutba
  shakl : Shakl
  darura : Bool
  deriving DecidableEq, Repr

inductive Hukm | maqbul | khata | laHukm
  deriving DecidableEq, Repr

inductive Daraja | rajih | marjuh | sawa | bila
  deriving DecidableEq, Repr

structure Jawab where
  hukm : Hukm
  daraja : List Daraja
  deriving DecidableEq, Repr

def maqbulJ (ds : List Daraja) : Jawab := ⟨.maqbul, ds⟩
def khataJ : Jawab := ⟨.khata, [.bila]⟩
def laHukmJ : Jawab := ⟨.laHukm, [.bila]⟩

/-- ترتيبُ الرتبة: المتكلّمُ 1، والمخاطَبُ 2، والغائبُ 3 (ترتيبُ الشخص في سمات `SLGE.Maqam`). -/
def Rutba.shakhs : Rutba → Nat
  | .mutakallim => 1
  | .mukhatab => 2
  | .ghaib => 3

/-- الأوّلُ أخصُّ من الثاني. -/
def akhass (a b : Rutba) : Bool := decide (a.shakhs < b.shakhs)

/-- العواملُ التي يجري فيها الترتيبُ بين ضميرين (س118–119، و«سلنيه» و«ظننتكه» و«كنته»). -/
def Amil.tartib : Amil → Bool
  | .filIthnayn | .zann | .kana => true
  | _ => false

/-- الابتداء: المتّصلُ لا يُبتدأ به. -/
def ibtidaJ (s : Shakl) : Jawab :=
  match s with
  | .muttasil => khataJ
  | .munfasil => maqbulJ [.bila]

/-- بعد «إلا»: المتّصلُ لا يليها «اختيارا»؛ والمنفصلُ مقبول. -/
def illaJ (s : Shakl) (darura : Bool) : Jawab :=
  match s with
  | .muttasil => if darura then laHukmJ else khataJ
  | .munfasil => maqbulJ [.bila]

/-- الأصل: الوصلُ ممكنٌ فلا فصلَ «في اختيار». -/
def asliJ (s : Shakl) (darura : Bool) : Jawab :=
  match s with
  | .muttasil => maqbulJ [.bila]
  | .munfasil => if darura then laHukmJ else khataJ

/-- الترتيبُ بين ضميرين: `q` رتبةُ الأوّل، و`r` رتبةُ المسؤول عنه. -/
def tartibJ (a : Amil) (q r : Rutba) (s : Shakl) : Jawab :=
  if akhass q r then
    match a, s with
    | .filIthnayn, .muttasil => maqbulJ [.rajih, .sawa]
    | .filIthnayn, .munfasil => maqbulJ [.marjuh, .sawa]
    | _, _ => maqbulJ [.rajih, .marjuh]
  else if decide (q = r) then
    match s with
    | .munfasil => maqbulJ [.bila]
    | .muttasil => if decide (r = .ghaib) then maqbulJ [.marjuh] else khataJ
  else
    match s with
    | .munfasil => maqbulJ [.bila]
    | .muttasil => khataJ

/-- **الحكم.** -/
def jawab (d : Dakhil) : Jawab :=
  match d.mawqi, d.amil with
  | .ibtida, .laAmil => if d.qablahu.isSome then laHukmJ else ibtidaJ d.shakl
  | .ibtida, _ => laHukmJ
  | _, .laAmil => laHukmJ
  | .badIlla, _ => illaJ d.shakl d.darura
  | .yali, a =>
    match d.qablahu with
    | none => if a.tartib then laHukmJ else asliJ d.shakl d.darura
    | some q =>
      if a.tartib then tartibJ a q d.rutba d.shakl
      else if decide (q = d.rutba) then laHukmJ
      else asliJ d.shakl d.darura

/-! ## الأسانيد -/

/-- الأسانيد: (القاعدة، المصدر، من سطر، إلى سطر، القطعةُ حرفيّةً بعد وصل الأسطر بمسافة). -/
def asanid : List (String × String × Nat × Nat × String) :=
  [("ta3rif", "qatr", 124, 124, "الضمير وهو ما دل على متكلم أو مخاطب أو غائب."),
   ("munfasil_amthila", "qatr", 126, 126, "أو منفصل ك\"أنا وأنت وإياي\"."),
   ("la_fasl", "qatr", 126, 127, "ولا فصل مع إمكان الوصل،"),
   ("salnihi", "qatr", 127, 127, "إلا في نحو الهاء من \"سلنيه\" بمرجوحية،"),
   ("zanantukahu", "qatr", 127, 128, "و \"ظننتكه\" و \"كنته\" برجحان."),
   ("sam", "alfiyya", 105, 105, "فما لذي غيبة أو حضور ... كأنت وهو سم بالضمير"),
   ("la_yubtada", "alfiyya", 106, 106, "وذو اتصال منه ما لا يبتدا ... ولا يلي إلا اختيارا أبدا"),
   ("raf_infisal", "alfiyya", 113, 113, "وذو إرتفاع وانفصال أنا هو"),
   ("nasb_infisal", "alfiyya", 114, 114, "وذو انتصاب في انفصال جعلا ... إياي"),
   ("ikhtiyar", "alfiyya", 115, 115, "وفي اختيار لا يجيء المنفصل ... إذ تأتى أن يجئ المتصل"),
   ("salnihi_wasl_fasl", "alfiyya", 116, 116, "وصل أو افصل هاء سلنيه"),
   ("kuntuhu_khulf", "alfiyya", 116, 116, "في كنته الخلف أنتمي"),
   ("khiltanihi", "alfiyya", 117, 117, "كذاك خلتنيه واتصالا ... أختار غيري اختار الانفصالا"),
   ("akhass", "alfiyya", 118, 118, "وقدم الأخص في اتصال ... وقدمن ما شئت في اتفصال"),
   ("ittihad", "alfiyya", 119, 119, "وفي اتحاد الرتبة الزم فصلا ... وقد يبيح الغيب فيه وصلا")]

/-! ## المبرهنات -/

/-- **الابتداءُ بالمتّصل خطأ.** -/
theorem ibtida_muttasil_khata (d : Dakhil) (hm : d.mawqi = .ibtida) (ha : d.amil = .laAmil) (hq : d.qablahu = none)
    (hs : d.shakl = .muttasil) : jawab d = khataJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm ha hq hs; rfl

/-- **والابتداءُ بالمنفصل مقبولٌ بلا درجة.** -/
theorem ibtida_munfasil_maqbul (d : Dakhil) (hm : d.mawqi = .ibtida) (ha : d.amil = .laAmil) (hq : d.qablahu = none)
    (hs : d.shakl = .munfasil) : jawab d = maqbulJ [.bila] := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm ha hq hs; rfl

/-- **المتّصلُ بعد «إلا»:** خطأٌ في الاختيار، و«لا حكم» في الضرورة. -/
theorem illa_muttasil (d : Dakhil) (hm : d.mawqi = .badIlla) (ha : d.amil ≠ .laAmil) (hs : d.shakl = .muttasil) :
    jawab d = (if d.darura then laHukmJ else khataJ) := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hs; subst hm hs
  cases a <;> simp_all [jawab, illaJ]

/-- **والمنفصلُ بعد «إلا» مقبولٌ بلا درجة.** -/
theorem illa_munfasil_maqbul (d : Dakhil) (hm : d.mawqi = .badIlla) (ha : d.amil ≠ .laAmil) (hs : d.shakl = .munfasil) :
    jawab d = maqbulJ [.bila] := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hs; subst hm hs
  cases a <;> simp_all [jawab, illaJ]

/-- **لا فصلَ مع إمكان الوصل:** يلي عاملًا لا ترتيبَ فيه، بلا ضميرٍ قبله برتبته، منفصلًا في غير ضرورة: خطأ. -/
theorem fasl_maa_imkan (d : Dakhil) (hm : d.mawqi = .yali) (ha : d.amil.tartib = false) (hl : d.amil ≠ .laAmil)
    (hq : d.qablahu ≠ some d.rutba) (hs : d.shakl = .munfasil) (hd : d.darura = false) : jawab d = khataJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hl hq hs hd; subst hm hs hd
  cases a <;> rcases q with _ | (_ | _ | _) <;> cases r <;> simp_all [jawab, asliJ, Amil.tartib]

/-- **الفصلُ في باب الترتيب مقبولٌ دائمًا** («وقدمن ما شئت في اتفصال»، «الزم فصلا»). -/
theorem tartib_munfasil_maqbul (d : Dakhil) (q : Rutba) (hm : d.mawqi = .yali) (ha : d.amil.tartib = true)
    (hq : d.qablahu = some q) (hs : d.shakl = .munfasil) : (jawab d).hukm = .maqbul := by
  obtain ⟨a, m, q', r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm hq hs
  cases a <;> cases q <;> cases r <;> simp_all [jawab, tartibJ, akhass, Rutba.shakhs, Amil.tartib, maqbulJ]

/-- **والوصلُ فيه مقبولٌ إذا وفقط إذا كان الأوّلُ أخصَّ أو كانا غائبين.** -/
theorem tartib_muttasil_iff (d : Dakhil) (q : Rutba) (hm : d.mawqi = .yali) (ha : d.amil.tartib = true)
    (hq : d.qablahu = some q) (hs : d.shakl = .muttasil) :
    (jawab d).hukm = .maqbul ↔ (akhass q d.rutba = true ∨ (q = .ghaib ∧ d.rutba = .ghaib)) := by
  obtain ⟨a, m, q', r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm hq hs
  cases a <;> cases q <;> cases r <;> simp_all [jawab, tartibJ, akhass, Rutba.shakhs, Amil.tartib, maqbulJ, khataJ]

/-- **الضرورةُ لا تغيّر إلّا ما قُيّد بالاختيار:** إن اختلف الحكمُ بالضرورة وحدها فهو في الاختيار خطأ، وفي الضرورة «لا حكم». -/
theorem darura_la_tughayyir_illa_ikhtiyar (d : Dakhil) (h : jawab { d with darura := true } ≠ jawab { d with darura := false }) :
    jawab { d with darura := false } = khataJ ∧ jawab { d with darura := true } = laHukmJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  cases a <;> cases m <;> rcases q with _ | (_ | _ | _) <;> cases r <;> cases s <;> simp_all [jawab, illaJ, asliJ, ibtidaJ, tartibJ, Amil.tartib]

/-- **ما ليس مقبولًا فدرجتُه `[bila]`.** -/
theorem ghayr_maqbul_bila_daraja (d : Dakhil) (h : (jawab d).hukm ≠ .maqbul) : (jawab d).daraja = [.bila] := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  cases a <;> cases m <;> rcases q with _ | (_ | _ | _) <;> cases r <;> cases s <;> cases dr <;>
    simp_all [jawab, illaJ, asliJ, ibtidaJ, tartibJ, Amil.tartib, akhass, Rutba.shakhs, maqbulJ, khataJ, laHukmJ]

/-- **مواضعُ «لا حكم»:** حقولٌ غيرُ متّسقة، أو ضرورةٌ فيما قُيّد بالاختيار، أو باب الترتيب بلا ضميرٍ قبله، أو اتّحادُ الرتبة في غير باب الترتيب. -/
theorem la_hukm_iff (d : Dakhil) :
    (jawab d).hukm = .laHukm ↔
      ((d.mawqi = .ibtida) ≠ (d.amil = .laAmil)) ∨
      (d.mawqi = .ibtida ∧ d.amil = .laAmil ∧ d.qablahu.isSome = true) ∨
      (d.mawqi = .badIlla ∧ d.amil ≠ .laAmil ∧ d.shakl = .muttasil ∧ d.darura = true) ∨
      (d.mawqi = .yali ∧ d.amil ≠ .laAmil ∧ d.amil.tartib = true ∧ d.qablahu = none) ∨
      (d.mawqi = .yali ∧ d.amil ≠ .laAmil ∧ d.amil.tartib = false ∧ d.qablahu = some d.rutba) ∨
      (d.mawqi = .yali ∧ d.amil ≠ .laAmil ∧ d.amil.tartib = false ∧ d.qablahu ≠ some d.rutba ∧
        d.shakl = .munfasil ∧ d.darura = true) := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  cases a <;> cases m <;> rcases q with _ | (_ | _ | _) <;> cases r <;> cases s <;> cases dr <;>
    simp_all [jawab, illaJ, asliJ, ibtidaJ, tartibJ, Amil.tartib, akhass, Rutba.shakhs, maqbulJ, khataJ, laHukmJ]

/-! ## الصلة بـ SLGE -/

/-- رتبةُ الضمير من سمته في `SLGE.Maqam` (الشخص). -/
def rutbaMin (f : SLGE.Maqam.Feat) : Option Rutba :=
  match f.1 with
  | 1 => some .mutakallim
  | 2 => some .mukhatab
  | 3 => some .ghaib
  | _ => none

/-- **الأخصّيّةُ هي الأقلُّ شخصًا:** لكلّ سمتين لهما رتبة، الأوّلُ أخصُّ إذا وفقط إذا كان شخصُه أقلّ. -/
theorem akhass_shakhs (f g : SLGE.Maqam.Feat) (a b : Rutba) (ha : rutbaMin f = some a) (hb : rutbaMin g = some b) :
    akhass a b = true ↔ f.1 < g.1 := by
  obtain ⟨x, _, _⟩ := f
  obtain ⟨y, _, _⟩ := g
  simp only [rutbaMin] at ha hb
  rcases x with _ | _ | _ | _ | x <;> rcases y with _ | _ | _ | _ | y <;> simp_all [akhass] <;>
    subst_vars <;> simp [Rutba.shakhs] <;> omega

/-- **أوّلُ المعارف الضمير** (`SLGE.Wad.maarif`، القطر س123–124). -/
theorem awwal_maarif : SLGE.Wad.maarif[0]? = some "الضمير" := by decide

/-- **الضمائرُ المنفصلة في `SLGE.Maqam.damair` لها رتبةٌ كلُّها، وفيها الرتبُ الثلاث، ويُبتدأ بها.** -/
theorem damair_ibtida :
    SLGE.Maqam.damair.all (fun d => (rutbaMin d.2.2).isSome) = true ∧
    [Rutba.mutakallim, .mukhatab, .ghaib].all (fun r => SLGE.Maqam.damair.any (fun d => rutbaMin d.2.2 == some r)) = true ∧
    SLGE.Maqam.damair.all (fun d => match rutbaMin d.2.2 with
      | some r => jawab ⟨.laAmil, .ibtida, none, r, .munfasil, false⟩ == maqbulJ [.bila]
      | none => false) = true := by
  decide

/-- **الشواهد** (تحليلُ البنّاء لأمثلة النطاق): «أكرمك» متّصلًا مقبول وفصلُه خطأ؛ «إياي» مبتدأً مقبول؛ «سلنيه» و«ظننتكه» و«كنته» و«خلتنيه»
    بدرجاتها؛ واتّحادُ الرتبة. -/
theorem shawahid :
    jawab ⟨.filWahid, .yali, none, .mukhatab, .muttasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.filWahid, .yali, none, .mukhatab, .munfasil, false⟩ = khataJ ∧
    jawab ⟨.ism, .yali, none, .ghaib, .muttasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.laAmil, .ibtida, none, .mutakallim, .munfasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.filIthnayn, .yali, some .mutakallim, .ghaib, .muttasil, false⟩ = maqbulJ [.rajih, .sawa] ∧
    jawab ⟨.filIthnayn, .yali, some .mutakallim, .ghaib, .munfasil, false⟩ = maqbulJ [.marjuh, .sawa] ∧
    jawab ⟨.zann, .yali, some .mutakallim, .mukhatab, .munfasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.kana, .yali, some .mutakallim, .ghaib, .muttasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.zann, .yali, some .mukhatab, .mutakallim, .muttasil, false⟩ = khataJ ∧
    jawab ⟨.filIthnayn, .yali, some .mukhatab, .mukhatab, .muttasil, false⟩ = khataJ ∧
    jawab ⟨.filIthnayn, .yali, some .ghaib, .ghaib, .muttasil, false⟩ = maqbulJ [.marjuh] ∧
    jawab ⟨.filWahid, .badIlla, none, .mukhatab, .munfasil, false⟩ = maqbulJ [.bila] := by
  decide

end Damir
end Jisr
