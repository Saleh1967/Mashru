import SLGE.Wad
import SLGE.Maqam

/-!
# الضميرُ البارز: الاتّصالُ والانفصال والترتيب في قطر الندى (س124–128) والألفية (س105–119)

**الطلب.** قولُ المالك 2026-10-28 (لفظُه ووقتُه، 00:33 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها): «يجب الاستفادة من ما لم نغطه وموجود في المراجع سواء
استنتجته انت او موجود في المرفق وعمل lean له شرط ان يكون متناسق ومتكامل ومترابط مع البرهان واالحساب وفق الدستور وأفضل الممارسات …
نفذ انت والوكلاء  و». والضميرُ في Lean القائمة قائمةُ ألفاظٍ بسماتها (`SLGE.Maqam.damair`)، وأوّلُ المعارف في `SLGE.Wad.maarif`، بلا حكمٍ على
صورته. واختيارُ هذه القطعة بعد أسماء الإشارة، ونطاقُها، قرارُ البنّاء.

**المصدر.** `qatr.txt` المختوم (`2d9241be…`) الأسطر 124–128، و`alfiyya.txt` المختوم (`13b351a0…`) الأسطر 105–119 (والسطرُ 108 علامةُ صفحة).
والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_damir.py` على المودَعين موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/damir/wasf.md` بأعيانها): العاملُ `Amil`، والموقعُ `Mawqi`، ورتبةُ الضمير المتّصل
بالعامل قبل المسؤول عنه `qablahu` (أو لا شيء)، ورتبةُ المسؤول عنه `Rutba`، وصورتُه `Shakl`، والضرورة. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ
قارئٍ من النصّ.**

**المخرج** `Jawab`: الحكمُ `Hukm` (`maqbul` أو `khata` أو `laHukm`)، والدرجةُ قائمةً `List Daraja`: درجةٌ واحدة، أو درجتان حيث يحكم النطاقُ
على الصورة نفسِها بدرجتين من مصدرين أو قائلين، ولا تحمل الحقولُ ما يفرّق بينهما. وحين لا يكون الحكمُ «مقبولًا» فالدرجةُ `[bila]`.

**الحكم** (`jawab`)، بالترتيب:
1. **اتّساقُ الحقول.** «ابتداء» مع «لا_عامل» وحده، وبلا ضميرٍ قبله؛ و«اسم» بلا ضميرٍ قبله (`qablahu` في المواصفة المفعولُ الأوّل، أو اسمُ «كان»،
   أو ضميرُ الرفع المتّصلُ بالفعل، ولا شيءَ منها للاسم)؛ وما خالف ذلك «لا حكم».
2. **الابتداء** (`ibtidaJ`): المتّصلُ خطأٌ في الاختيار («وذو اتصال منه ما لا يبتدا»، ألفيّة س106)، و«لا حكم» في الضرورة: يحتمل الرسمُ بلا شكلٍ أن يقيّد
   «اختيارا» الشطرَ الأوّل من س106 أيضًا (أفصح به المؤلّف في `taalif.md`، القرار ٥)؛ والمنفصلُ «لا حكم»: أمثلتُه في النطاق («أو منفصل ك"أنا
   وأنت وإياي"»، قطر س126؛ «كأنت وهو»، ألفيّة س105؛ «أنا هو ... وأنت»، س113؛ «إياي»، س114) بلا موضع، والمفتاحُ يقبل الصورةَ «في الموضع الذي يذكره».
3. **بعد «إلا»** (`illaJ`): المتّصلُ خطأ «اختيارا» («ولا يلي إلا اختيارا أبدا»، س106)، وفي الضرورة «لا حكم»؛ والمنفصلُ «لا حكم»: لا نصَّ فيه.
4. **يلي عاملًا لواحدٍ أو اسمًا مضافًا، ولا ضميرَ قبله** (`asliJ`): المتّصلُ مقبول، والمنفصلُ خطأ ولو في الضرورة («ولا فصل مع إمكان الوصل»،
   قطر س126–127، مطلقًا؛ وإمكانُ الوصل فيه بمثاليه «أكرمك» و«غلامه»، س126). وقيدُ الألفيّة «وفي اختيار» (س115) لا يرفع نفيَ القطر المطلق.
5. **يلي العامل وقبله ضميرٌ متّصل** (`tartibJ`)، لكلّ عاملٍ غيرِ الاسم: س119 أخذًا بقراءة المؤلّف («لم يقيّده النطاقُ بالمفعولين»، `taalif.md`
   القرار ٧)، وس118 بعلّتها نفسِها تعيينًا للبنّاء (أدناه)؛ و`qablahu` في المواصفة يشمل ضميرَ الرفع المتّصل بالفعل.
   - **الأوّلُ أخصّ** (المتكلّمُ أخصُّ من المخاطَب، والمخاطَبُ من الغائب): المتّصلُ مقبول («وقدم الأخص في اتصال»، س118). والمنفصل:
     - لمفعولين («سلنيه»): المتّصلُ [`rajih`، `sawa`]، والمنفصلُ [`marjuh`، `sawa`]. فالقطرُ يجعل الفصلَ فيه «بمرجوحية» (س127)، والألفيّةُ
       «وصل أو افصل» بلا تفضيل (س116).
     - «ظنّ» و«كان» («ظننتكه»، «كنته»، «خلتنيه»): المتّصلُ والمنفصلُ كلاهما [`rajih`، `marjuh`]. فالقطرُ يجعل الفصلَ فيهما «برجحان» (س127–128)،
       وابنُ مالك يختار الاتّصال وغيرُه الانفصال («واتصالا ... أختار غيري اختار الانفصالا»، س117).
     - وفي غيرها: المتّصلُ بلا درجة، والمنفصلُ خطأ «في اختيار» («وفي اختيار لا يجيء المنفصل ... إذ تأتى أن يجئ المتصل»، س115؛ وإمكانُ الوصل من
       س118)، وفي الضرورة «لا حكم».
   - **الرتبةُ واحدة**: المتّصلُ خطأ («وفي اتحاد الرتبة الزم فصلا»، س119)، إلّا الغائبين فمقبولٌ مرجوح («وقد يبيح الغيب فيه وصلا»، س119)؛
     والمنفصلُ مقبول، راجحٌ في الغائبين (مقابلَ مرجوحيّة الوصل فيهما)، وبلا درجةٍ في غيرهما.
   - **الثاني أخصّ**: المنفصلُ مقبولٌ `sawa` («وقدمن ما شئت في اتفصال»، س118؛ و«ما شئت» في المفتاح سواء)؛ والمتّصلُ «لا حكم»: «وقدم الأخص في
     اتصال» أمرٌ بصورته، والمفتاحُ يجعل الأمرَ قبولًا لصورته لا نفيًا لعكسها.
6. **يلي عاملًا لمفعولين أو «ظنّ» أو «كان» ولا ضميرَ قبله:** «لا حكم». الترتيبُ في النطاق بين ضميرين.

**ما هو تعيينُ البنّاء** (لا نصُّ النطاق):
- رجحانُ الاتّصال في «سلنيه» عند القطر من مرجوحيّة الفصل فيه، ورجحانُه في «ظننتكه» و«كنته» عند ابن مالك من اختياره، ورجحانُ الفصل في الغائبين
  من مرجوحيّة الوصل فيهما: الدرجةُ المتمّمة.
- ما لا يفرّق بينه الحقلُ (القطرُ أم الألفيّة، ابنُ مالكٍ أم غيرُه) قائمةُ درجتين، لا اختيار.
- الضرورةُ لا تغيّر إلّا ما قُيّد بـ«اختيارا» (س106) أو «في اختيار» (س115) ولا نفيَ مطلقًا له من القطر: المتّصلُ بعد «إلا» ومبتدأً، والمنفصلُ بعد ضميرٍ
  أخصَّ في عاملٍ لواحد.
- الأخصّيّةُ ترتيبُ الرتب الثلاث المتكلّمُ فالمخاطَبُ فالغائب، وهي ترتيبُ الشخص في سمات `SLGE.Maqam` (`akhass_shakhs`). والنطاقُ لا ينصّ على هذا
  الترتيب، وأمثلتُه («سلنيه»، «ظننتكه»، «كنته»، «خلتنيه») حاضرٌ قبل غائب.
- **س118 لكلّ عامل** (غيرِ الاسم) بعلّة المؤلّف في س119، لا بقراءته: لم يكتب حالةً لس118 في عاملٍ لواحد. ونتيجتُه في العامل لواحد: الأوّلُ أخصّ
  متّصلًا مقبول، ومنفصلًا خطأٌ في الاختيار («وفي اختيار لا يجيء المنفصل»، وإمكانُ الوصل من «وقدم الأخص في اتصال») و«لا حكم» في الضرورة؛ والثاني
  أخصّ منفصلًا مقبولٌ `sawa` («ما شئت»، والمؤلّفُ يعطي «سواء» حيث للترتيب بديلٌ مختلفُ المدخل، القرار ٨)، ومتّصلًا «لا حكم». ولا حالةَ تمسّه.
- **درجاتُ «سلنيه» و«ظننتكه» و«كنته» و«خلتنيه» ممدودةٌ بالأخصّيّة** على كلّ أوّلٍ أخصّ في عاملها، ومنه المتكلّمُ قبل المخاطَب وليس من أمثلة
  النطاق؛ وامتدادُ المؤلّف (القرار ٢) على العامل نفسه والترتيب نفسه، يتغيّر فيه الأوّلُ ما بقي ضميرَ حضور. ولا حالةَ تمسّ المتكلّمَ قبل المخاطَب.

**الصلة بقطع Lean القائمة:**
- `awwal_maarif`: أوّلُ `SLGE.Wad.maarif` «الضمير».
- `akhass_shakhs`: رتبةُ الضمير من سمته في `SLGE.Maqam.damair` (الشخصُ 1 و2 و3)، والأخصّيّةُ هي الأقلُّ شخصًا؛ وصورُ `damair` الأربعَ عشرةَ
  منفصلةٌ كلُّها، ولها رتبة، ولا يحكم النطاقُ في الابتداء بها (`damair_rutab`).
- **وفي ملفّات المالك حكمٌ في الابتداء بها من جهةٍ أخرى:** `SLGE.Maqam.participants_free` («المتكلّمُ والمخاطبُ يُبتدأ بهما»: إحالتُهما إلى المقام)،
  و`SLGE.Maqam.ghaib_needs_ante` (الغائبُ لا يُبتدأ به بلا سابق إلّا ضميرَ الشأن)، و`SLGE/Tarkib.lean` («ولا يُبتدأ بضميرٍ يحيل إلى ما بعده»).
  والمسألتان مختلفتان: هناك إحالةُ الضمير، وهنا صورتُه؛ فـ«أنا قائم» (D12) «لا حكم» في صورته هنا، ويُبتدأ به في إحالته هناك. لا تناقض، ولا ربط.

**المنهج.** الشفرةُ المجمَّدة كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/damir/tajmid.json`؛
`hawkama/منهج_الضوابط.md`)، ودُفعت في `af3356c`، والتشغيلُ الأوّل عليها في `natija_1.json` (55/69). وهذا الملفُّ عُدّل بعدها (أدناه). ونتيجتُه على
الضابط في `Jisr/DamirQiyas.lean`، لا هنا.

**ما غُيّر بعد قراءة الحالات** (فالتشغيلُ الثاني وما بعده على مادّةٍ مكشوفة)، أخذًا بقراءة المؤلّف في المواضع الثلاثة عشر كلِّها، ومعه تعيينٌ
للبنّاء: س118 لكلّ عاملٍ غيرِ الاسم (أعلاه؛ وامتدادُ الدرجات بالأخصّيّة في الشفرة المجمَّدة نفسِها):
- **المنفصلُ في الضرورة بلا ضميرٍ قبله خطأ** (كان «لا حكم»): قيدُ الألفيّة «في اختيار» لا يرفع نفيَ القطر المطلق، والمفتاحُ يحكم فيما خرج عن
  القيد «بلفظٍ آخر من النطاق». الحالتان: D08 وD10.
- **المنفصلُ مبتدأً وبعد «إلا» «لا حكم»** (كانا مقبولين): كان قبولُهما مفهومَ «لا يبتدا» و«مع إمكان الوصل»، والمفتاحُ لا يقبل الصورةَ إلّا في
  موضعٍ يذكره. الحالات: D12 وD14 وD17.
- **قواعدُ الترتيب لكلّ عامل** (كانت للعوامل الثلاثة، و«يلي العامل» مع ضميرٍ قبله برتبته في غيرها «لا حكم»): اتّحادُ الرتبة في عاملٍ لواحد
  خطأٌ متّصلًا، ومرجوحٌ في الغائبين (قراءةُ المؤلّف، القرار ٧). الحالتان: D45 وD46. وس118 في العامل لواحد بالعلّة نفسِها (تعيين، بلا حالة).
- **الثاني أخصّ: المتّصلُ «لا حكم»** (كان خطأ)، **والمنفصلُ `sawa`** (كان بلا درجة). الحالات: D31 وD32 وD33 وD34.
- **الفصلُ في الغائبين راجح** (كان بلا درجة). الحالتان: D23 وD25.
- **وبعد مراجعة `murajii`** (بلا حالةٍ تمسّه): «اسم» مع ضميرٍ قبله غيرُ متّسق («لا حكم»؛ كان يُحكم فيه بقواعد الترتيب)، والمتّصلُ مبتدأً في
  الضرورة «لا حكم» (كان خطأ).
- **وما تغيّر في المجال كلّه** مسرودٌ بمدخلاته في `tahaqquq/dawabit/damir/mulhaq_1.md` §٢ (مقابلةُ جواب الشفرة المجمَّدة بجواب هذه على 864 مدخلًا،
  بسكربتٍ محفوظٍ فيه)؛ والحالاتُ تمسّ منه الثلاثةَ عشرَ الفاشلة وحدها.

**المبرهنات** (بالمعيار الموحَّد في `Nizam/Asas.lean`)، وهي خواصُّ هذا التعيين على مجاله، لا قوانينُ في اللغة:
- تعريفيّة (10): `ibtida_muttasil`، `ibtida_munfasil_la_hukm`، `illa_muttasil`، `illa_munfasil_la_hukm`، `fasl_maa_imkan`،
  `tartib_munfasil_maqbul`، `tartib_muttasil_iff`، `darura_la_tughayyir_illa_ikhtiyar`، `ghayr_maqbul_bila_daraja`، `la_hukm_iff`. وبرهانُها فكُّ
  التعريفات وتفكيكُ الحالات على مجالٍ منتهٍ.
- لكلّ (1): `akhass_shakhs` (على السمات، بـ`omega`).
- على الشاهد (3): `awwal_maarif`، `damair_rutab`، `shawahid`.

**حدُّه.** المدخلُ تحليلٌ يُعطى؛ ولا مستترَ ولا نونَ وقاية ولا عددَ ولا جنس؛ والدرجةُ قائمةٌ حيث يختلف المصدران، لا مرجّحَ بينهما؛ ووصلُ الغائبين
في عاملٍ لواحد مرجوحٌ هنا بنصّ س119، وقال المؤلّف في D45: «وخارج النطاق يعد هذا الوصل أصلا لا مرجوحا»؛ ولا وصلَ بالقارئ ولا بالمحرّك.
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

/-- العواملُ التي لا تُذكر في النطاق إلّا والضميرُ بعد ضميرٍ («سلنيه» و«ظننتكه» و«كنته» و«خلتنيه»)، فلا حكمَ فيها بلا ضميرٍ قبله. وقواعدُ
    الترتيب (س118–119) لكلّ عاملٍ غيرِ الاسم. -/
def Amil.tartib : Amil → Bool
  | .filIthnayn | .zann | .kana => true
  | _ => false

/-- الابتداء: المتّصلُ لا يُبتدأ به في الاختيار. -/
def ibtidaJ (s : Shakl) (darura : Bool) : Jawab :=
  match s with
  | .muttasil => if darura then laHukmJ else khataJ
  | .munfasil => laHukmJ

/-- بعد «إلا»: المتّصلُ لا يليها «اختيارا»؛ والمنفصلُ لا يحكم فيه النطاق. -/
def illaJ (s : Shakl) (darura : Bool) : Jawab :=
  match s with
  | .muttasil => if darura then laHukmJ else khataJ
  | .munfasil => laHukmJ

/-- الأصل، بلا ضميرٍ قبله: الوصلُ ممكنٌ فلا فصل («ولا فصل مع إمكان الوصل» مطلقًا في القطر). -/
def asliJ (s : Shakl) : Jawab :=
  match s with
  | .muttasil => maqbulJ [.bila]
  | .munfasil => khataJ

/-- الترتيبُ بين ضميرين: `q` رتبةُ الأوّل، و`r` رتبةُ المسؤول عنه. -/
def tartibJ (a : Amil) (q r : Rutba) (s : Shakl) (darura : Bool) : Jawab :=
  if akhass q r then
    match a, s with
    | .filIthnayn, .muttasil => maqbulJ [.rajih, .sawa]
    | .filIthnayn, .munfasil => maqbulJ [.marjuh, .sawa]
    | .zann, _ => maqbulJ [.rajih, .marjuh]
    | .kana, _ => maqbulJ [.rajih, .marjuh]
    | _, .muttasil => maqbulJ [.bila]
    | _, .munfasil => if darura then laHukmJ else khataJ
  else if decide (q = r) then
    match s with
    | .munfasil => if decide (r = .ghaib) then maqbulJ [.rajih] else maqbulJ [.bila]
    | .muttasil => if decide (r = .ghaib) then maqbulJ [.marjuh] else khataJ
  else
    match s with
    | .munfasil => maqbulJ [.sawa]
    | .muttasil => laHukmJ

/-- **الحكم.** -/
def jawab (d : Dakhil) : Jawab :=
  match d.mawqi, d.amil with
  | .ibtida, .laAmil => if d.qablahu.isSome then laHukmJ else ibtidaJ d.shakl d.darura
  | .ibtida, _ => laHukmJ
  | _, .laAmil => laHukmJ
  | .badIlla, _ => illaJ d.shakl d.darura
  | .yali, a =>
    match d.qablahu with
    | none => if a.tartib then laHukmJ else asliJ d.shakl
    | some q => if a = .ism then laHukmJ else tartibJ a q d.rutba d.shakl d.darura

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

/-- **الابتداءُ بالمتّصل:** خطأٌ في الاختيار، و«لا حكم» في الضرورة. -/
theorem ibtida_muttasil (d : Dakhil) (hm : d.mawqi = .ibtida) (ha : d.amil = .laAmil) (hq : d.qablahu = none)
    (hs : d.shakl = .muttasil) : jawab d = (if d.darura then laHukmJ else khataJ) := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm ha hq hs; cases dr <;> rfl

/-- **والابتداءُ بالمنفصل لا يحكم فيه النطاق** (أمثلةُ المنفصل فيه بلا موضع). -/
theorem ibtida_munfasil_la_hukm (d : Dakhil) (hm : d.mawqi = .ibtida) (ha : d.amil = .laAmil) (hs : d.shakl = .munfasil) :
    jawab d = laHukmJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hs; subst hm ha hs
  rcases q with _ | (_ | _ | _) <;> rfl

/-- **المتّصلُ بعد «إلا»:** خطأٌ في الاختيار، و«لا حكم» في الضرورة. -/
theorem illa_muttasil (d : Dakhil) (hm : d.mawqi = .badIlla) (ha : d.amil ≠ .laAmil) (hs : d.shakl = .muttasil) :
    jawab d = (if d.darura then laHukmJ else khataJ) := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hs; subst hm hs
  cases a <;> simp_all [jawab, illaJ]

/-- **والمنفصلُ بعد «إلا» لا يحكم فيه النطاق.** -/
theorem illa_munfasil_la_hukm (d : Dakhil) (hm : d.mawqi = .badIlla) (hs : d.shakl = .munfasil) : jawab d = laHukmJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm hs; subst hm hs
  cases a <;> simp_all [jawab, illaJ]

/-- **لا فصلَ مع إمكان الوصل** (مطلقًا، ولو في الضرورة): يلي عاملًا لواحدٍ أو اسمًا، بلا ضميرٍ قبله، منفصلًا: خطأ. -/
theorem fasl_maa_imkan (d : Dakhil) (hm : d.mawqi = .yali) (ha : d.amil.tartib = false) (hl : d.amil ≠ .laAmil)
    (hq : d.qablahu = none) (hs : d.shakl = .munfasil) : jawab d = khataJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  simp only at hm ha hl hq hs; subst hm hq hs
  cases a <;> simp_all [jawab, asliJ, Amil.tartib]

/-- **الفصلُ بعد ضميرٍ في «ظنّ» و«كان» والمفعولين مقبولٌ دائمًا** («وقدمن ما شئت في اتفصال»، «الزم فصلا»، «سلنيه» و«ظننتكه» و«كنته»). -/
theorem tartib_munfasil_maqbul (d : Dakhil) (q : Rutba) (hm : d.mawqi = .yali) (ha : d.amil.tartib = true)
    (hq : d.qablahu = some q) (hs : d.shakl = .munfasil) : (jawab d).hukm = .maqbul := by
  obtain ⟨a, m, q', r, s, dr⟩ := d
  simp only at hm ha hq hs; subst hm hq hs
  cases a <;> cases q <;> cases r <;> cases dr <;> simp_all [jawab, tartibJ, akhass, Rutba.shakhs, Amil.tartib, maqbulJ]

/-- **والوصلُ بعد ضميرٍ، لكلّ عاملٍ غيرِ الاسم، مقبولٌ إذا وفقط إذا كان الأوّلُ أخصَّ أو كانا غائبين** («وقدم الأخص في اتصال»، «وقد يبيح الغيب
    فيه وصلا»). -/
theorem tartib_muttasil_iff (d : Dakhil) (q : Rutba) (hm : d.mawqi = .yali) (hl : d.amil ≠ .laAmil) (hi : d.amil ≠ .ism)
    (hq : d.qablahu = some q) (hs : d.shakl = .muttasil) :
    (jawab d).hukm = .maqbul ↔ (akhass q d.rutba = true ∨ (q = .ghaib ∧ d.rutba = .ghaib)) := by
  obtain ⟨a, m, q', r, s, dr⟩ := d
  simp only at hm hl hi hq hs; subst hm hq hs
  cases a <;> cases q <;> cases r <;> cases dr <;> simp_all [jawab, tartibJ, akhass, Rutba.shakhs, Amil.tartib, maqbulJ, khataJ, laHukmJ]

/-- **الضرورةُ لا تغيّر إلّا ما قُيّد بالاختيار:** إن اختلف الحكمُ بالضرورة وحدها فهو في الاختيار خطأ، وفي الضرورة «لا حكم». -/
theorem darura_la_tughayyir_illa_ikhtiyar (d : Dakhil) (h : jawab { d with darura := true } ≠ jawab { d with darura := false }) :
    jawab { d with darura := false } = khataJ ∧ jawab { d with darura := true } = laHukmJ := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  cases a <;> cases m <;> rcases q with _ | (_ | _ | _) <;> cases r <;> cases s <;> simp_all [jawab, illaJ, asliJ, ibtidaJ, tartibJ, Amil.tartib, akhass, Rutba.shakhs, maqbulJ, khataJ, laHukmJ]

/-- **ما ليس مقبولًا فدرجتُه `[bila]`.** -/
theorem ghayr_maqbul_bila_daraja (d : Dakhil) (h : (jawab d).hukm ≠ .maqbul) : (jawab d).daraja = [.bila] := by
  obtain ⟨a, m, q, r, s, dr⟩ := d
  cases a <;> cases m <;> rcases q with _ | (_ | _ | _) <;> cases r <;> cases s <;> cases dr <;>
    simp_all [jawab, illaJ, asliJ, ibtidaJ, tartibJ, Amil.tartib, akhass, Rutba.shakhs, maqbulJ, khataJ, laHukmJ]

/-- **مواضعُ «لا حكم»:** حقولٌ غيرُ متّسقة (ومنها ضميرٌ قبل المبتدأ أو قبل الاسم)؛ أو المنفصلُ مبتدأً أو بعد «إلا»؛ أو المتّصلُ مبتدأً أو بعد
    «إلا» في الضرورة؛ أو باب الترتيب بلا ضميرٍ قبله؛ أو الوصلُ والثاني أخصّ؛ أو الفصلُ في الضرورة بعد ضميرٍ أخصَّ في العامل لواحد. -/
theorem la_hukm_iff (d : Dakhil) :
    (jawab d).hukm = .laHukm ↔
      ((d.mawqi = .ibtida) ≠ (d.amil = .laAmil)) ∨
      (d.mawqi = .ibtida ∧ d.amil = .laAmil ∧ (d.qablahu.isSome = true ∨ d.shakl = .munfasil ∨ d.darura = true)) ∨
      (d.mawqi = .badIlla ∧ d.amil ≠ .laAmil ∧ (d.shakl = .munfasil ∨ d.darura = true)) ∨
      (d.mawqi = .yali ∧ d.amil ≠ .laAmil ∧ d.amil.tartib = true ∧ d.qablahu = none) ∨
      (d.mawqi = .yali ∧ d.amil = .ism ∧ d.qablahu.isSome = true) ∨
      (d.mawqi = .yali ∧ d.amil ≠ .laAmil ∧ d.amil ≠ .ism ∧ ∃ q, d.qablahu = some q ∧ akhass d.rutba q = true ∧ d.shakl = .muttasil) ∨
      (d.mawqi = .yali ∧ d.amil = .filWahid ∧ ∃ q, d.qablahu = some q ∧ akhass q d.rutba = true ∧
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

/-- **الضمائرُ المنفصلة في `SLGE.Maqam.damair` لها رتبةٌ كلُّها، وفيها الرتبُ الثلاث؛ ولا يحكم النطاقُ في الابتداء بها.** -/
theorem damair_rutab :
    SLGE.Maqam.damair.all (fun d => (rutbaMin d.2.2).isSome) = true ∧
    [Rutba.mutakallim, .mukhatab, .ghaib].all (fun r => SLGE.Maqam.damair.any (fun d => rutbaMin d.2.2 == some r)) = true ∧
    SLGE.Maqam.damair.all (fun d => match rutbaMin d.2.2 with
      | some r => jawab ⟨.laAmil, .ibtida, none, r, .munfasil, false⟩ == laHukmJ
      | none => false) = true := by
  decide

/-- **الشواهد** (تحليلُ البنّاء لأمثلة النطاق): «أكرمك» و«غلامه» متّصلين مقبولان وفصلُهما خطأ ولو في الضرورة؛ و«أنا» مبتدأً، والمنفصلُ بعد
    «إلا»، «لا حكم»؛ و«سلنيه» و«ظننتكه» و«كنته» و«خلتنيه» بدرجاتها، ومعها **تعميمُ الأخصّيّة** (المتكلّمُ قبل المخاطَب في «ظنّ»، وليس من أمثلة النطاق)؛
    واتّحادُ الرتبة لعاملين (المفعولين والعامل لواحد)؛ والثاني أخصّ؛ والعاملُ لواحدٍ بعد ضميرٍ أخصّ (تعيين)؛ و«اسم» مع ضميرٍ قبله، والمتّصلُ مبتدأً في
    الضرورة، «لا حكم». -/
theorem shawahid :
    jawab ⟨.filWahid, .yali, none, .mukhatab, .muttasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.filWahid, .yali, none, .mukhatab, .munfasil, false⟩ = khataJ ∧
    jawab ⟨.filWahid, .yali, none, .mukhatab, .munfasil, true⟩ = khataJ ∧
    jawab ⟨.ism, .yali, none, .ghaib, .muttasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.laAmil, .ibtida, none, .mutakallim, .munfasil, false⟩ = laHukmJ ∧
    jawab ⟨.filWahid, .badIlla, none, .mukhatab, .munfasil, false⟩ = laHukmJ ∧
    jawab ⟨.filIthnayn, .yali, some .mutakallim, .ghaib, .muttasil, false⟩ = maqbulJ [.rajih, .sawa] ∧
    jawab ⟨.filIthnayn, .yali, some .mutakallim, .ghaib, .munfasil, false⟩ = maqbulJ [.marjuh, .sawa] ∧
    jawab ⟨.zann, .yali, some .mukhatab, .ghaib, .muttasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.zann, .yali, some .mutakallim, .ghaib, .munfasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.zann, .yali, some .mutakallim, .mukhatab, .munfasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.kana, .yali, some .mutakallim, .ghaib, .muttasil, false⟩ = maqbulJ [.rajih, .marjuh] ∧
    jawab ⟨.filIthnayn, .yali, some .mukhatab, .mukhatab, .muttasil, false⟩ = khataJ ∧
    jawab ⟨.filIthnayn, .yali, some .ghaib, .ghaib, .muttasil, false⟩ = maqbulJ [.marjuh] ∧
    jawab ⟨.filIthnayn, .yali, some .ghaib, .ghaib, .munfasil, false⟩ = maqbulJ [.rajih] ∧
    jawab ⟨.filWahid, .yali, some .ghaib, .ghaib, .muttasil, false⟩ = maqbulJ [.marjuh] ∧
    jawab ⟨.filWahid, .yali, some .mukhatab, .mukhatab, .muttasil, false⟩ = khataJ ∧
    jawab ⟨.filIthnayn, .yali, some .ghaib, .mukhatab, .munfasil, false⟩ = maqbulJ [.sawa] ∧
    jawab ⟨.zann, .yali, some .mukhatab, .mutakallim, .muttasil, false⟩ = laHukmJ ∧
    jawab ⟨.filWahid, .yali, some .mutakallim, .ghaib, .muttasil, false⟩ = maqbulJ [.bila] ∧
    jawab ⟨.filWahid, .yali, some .mutakallim, .ghaib, .munfasil, false⟩ = khataJ ∧
    jawab ⟨.filWahid, .yali, some .mutakallim, .ghaib, .munfasil, true⟩ = laHukmJ ∧
    jawab ⟨.ism, .yali, some .ghaib, .ghaib, .muttasil, false⟩ = laHukmJ ∧
    jawab ⟨.laAmil, .ibtida, none, .mutakallim, .muttasil, true⟩ = laHukmJ := by
  decide

end Damir
end Jisr
