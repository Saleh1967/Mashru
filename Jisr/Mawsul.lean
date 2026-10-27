import SLGE.Wad
import SLGE.Maqam

/-!
# الموصولُ وصلتُه في قطر الندى (س137–143) والألفية (س146–157)

**الطلب.** قولُ المالك 2026-10-28 (لفظُه ووقتُه، 00:33 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها): «يجب الاستفادة من ما لم نغطه وموجود في المراجع سواء
استنتجته انت او موجود في المرفق وعمل lean له شرط ان يكون متناسق ومتكامل ومترابط مع البرهان واالحساب وفق الدستور وأفضل الممارسات …
نفذ انت والوكلاء». والموصولُ في Lean القائمة قائمةُ ألفاظٍ (`SLGE.Wad.mawsul`)، وسماتُ الخاصّ منه وشرطُ العائد (`SLGE.Maqam.mawsulKhass`،
`SLGE.Maqam.silaOK`)، بلا حكمٍ على صورة اللفظ بموضعه ولا على نوع الصلة. واختيارُ هذه القطعة بعد الضمير، ونطاقُها، قرارُ البنّاء.

**المصدر.** `qatr.txt` المختوم (`2d9241be…`) الأسطر 137–143، و`alfiyya.txt` المختوم (`13b351a0…`) الأسطر 146–157. وما بعدها من الباب (س159–165:
إعرابُ «أي» وشروطُ حذف العائد) خارجَ النطاق. والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_mawsul.py` على المودَعين موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/mawsul/wasf.md` بأعيانها): اللفظ `Lafz`، وما يقع عليه `Sima`، والموضع، وتشديدُ النون،
واللغة، وما قبله، والإلغاء، ونوعُ الصلة `Sila`، والعائد `Aid` وسمتُه. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ قارئٍ من النصّ.**

**المخرج** `Jawab`: الحكم (`maqbul` أو `khata` أو `laHukm`)، والدرجةُ قائمةً (`qalil`، `nazr`، `lugha`، `bila`)؛ وحين لا يكون الحكمُ «مقبولًا»
فالدرجةُ `[bila]`.

**الحكم** (`jawab`)، بالترتيب، وأوّلُ ما يُخرج غيرَ «مقبول» هو الجواب:
1. **اتّساقُ الحقول** (`muttasiq`): التشديدُ في لفظٍ آخرُه نون، والإلغاءُ في «ذا»، و«لا عائد» في العائد وسمتِه معًا؛ وما خالف ذلك «لا حكم».
2. **اللفظ** (`lafzJ`):
   - «الذي» للمفرد المذكّر و«التي» للمفرد المؤنّث («وهو الذي والتي»، قطر س137؛ «موصول الأسماء الذي الأنثى التي»، ألفيّة س147).
   - «اللذان» و«اللتان» رفعًا، و«اللذين» و«اللتين» جرًّا ونصبًا («واللذان واللتان بالألف رفعا وبالياء جرا ونصبا»، س137–138)، والنونُ مشدّدةً
     مقبولة («والنون إن تشدد فلا ملامه»، ألفيّة س148). و«اللذيان» و«اللتيان» خطأ («واليا إذا ما ثنيا لا تثبت»، س147).
   - «الذين» لجمع المذكّر في المواضع كلّها («الذين بالياء مطلقا»، قطر س138؛ «الذين مطلقا»، ألفيّة س150)، و«اللذون» رفعًا لغة («وبعضهم بالواو رفعا
     نطقا»، س150)؛ و«الألى» لجمع المذكّر (س138، س150).
   - «اللائي» و«اللاتي» لجمع المؤنّث (قطر س138–139)، و«اللات» و«اللاء» كذلك (ألفيّة س151)، و«اللاء» لجمع المذكّر نزر («واللاء كالذين نزرا
     وقعا»، س151).
   - «من» و«ما» و«أي» و«أل» لكلّ معنى («وبمعنى الجميع من وما وأي، وأل»، قطر س139؛ «ومن وما وأل تساوي ما ذكر»، ألفيّة س152).
   - «ذو» لكلّ معنى في لغة طيئ («وذو في لغة طي»، قطر س140؛ «وهكذا ذو عند طيئ شهر»، س152)، و«ذات» للمفرد المؤنّث و«ذوات» لجمع المؤنّث عندهم
     («وكالتي أيضا لديهم ذات وموضع اللاتي أتى ذوات»، س153)؛ وفي غير لغتهم «لا حكم».
   - «ذا» لكلّ معنى بعد «ما» أو «من» الاستفهاميّتين غيرَ ملغاة («وذا بعد ما أو من الاستفهاميتين»، قطر س140؛ «ومثل ماذا بعدما استفهام أومن إذا لم تلغ
     في الكلام»، س154)، وفي غير ذلك «لا حكم».
   - وما سوى ذلك من لفظٍ لمعنًى أو موضعٍ جعل النطاقُ له غيرَه خطأ (مفتاحُ الصورة في المواصفة).
3. **الصلة** (`silaJ`):
   - لـ«أل» الوصفُ الصريح («وأل في وصف صريح لغير تفضيل»، قطر س139؛ «وصلة أل الوصف»، س140؛ «وصفة صريحة صلة أل»، ألفيّة س157)، والفعلُ المعرب قليل
     («وكونها بمعرب الأفعال قل»، س157)؛ وما سواهما خطأ، ومنه اسمُ التفضيل.
   - لغيرها الجملةُ الخبريّة والظرفُ والجارُّ والمجرورُ التامّان («وصلة غيرها إما جملة خبرية … أو ظرف أو جار ومجرور تامان»، قطر س141–143؛ «وجملة أو شبهها
     الذي وصل به»، ألفيّة س156)؛ وما سواها خطأ.
   - ولا موصولَ بلا صلة («وكلها يلزم بعده صله»، س155).
4. **العائد** (`aidJ`):
   - لا صلةَ بلا ضميرٍ يعود («ذات ضمير طبق للموصول يسمى عائدا»، قطر س141؛ «على ضمير لائق مشتمله»، ألفيّة س155)، والمحذوفُ في الجملة مقبول («وقد
     يحذف»، س141)، وفي غيرها «لا حكم».
   - والعائدُ على سمة المعنى: في اللفظ الخاصّ خطأٌ إن خالفها؛ وفي المشترك («من» وأخواتها) خطأٌ إن خالف المعنى واللفظَ (المفردَ المذكّر) معًا، و«لا حكم»
     إن وافق اللفظَ دون المعنى: «طبق للموصول» لا يقول أيُّهما.

**ما هو تعيينُ البنّاء** (لا نصُّ النطاق):
- اللغةُ قيدٌ على «ذو» و«ذات» و«ذوات» وحدها؛ وغيرُها يُحكم فيه بلا نظرٍ إلى اللغة. وما قبله والموضعُ لا أثرَ لهما إلّا في «ذا» والمثنّى و«اللذون».
- «ذو» عند طيئ لكلّ معنى (من «تساوي ما ذكر» و«وهكذا»)، و«ذات» و«ذوات» لما ذُكرتا له وحده.
- «طبق للموصول» في المشترك: الموافقُ للمعنى مقبول، والموافقُ للّفظ وحده «لا حكم».
- المحذوفُ في غير الجملة «لا حكم»: «وقد يحذف» في سياق الجملة الخبريّة.
- ترتيبُ الأحكام: الاتّساقُ فاللفظُ فالصلةُ فالعائد، وأوّلُ ما يُخرج غيرَ «مقبول» هو الجواب، وإلّا فالمقبولُ بدرجة اللفظ ثمّ الصلة.

**الصلة بقطع Lean القائمة:**
- `asma_qatr`: ألفاظُ `SLGE.Wad.mawsul` الأربعةَ عشرَ ألفاظٌ هنا، و«الموصول» رابعةُ `SLGE.Wad.maarif`.
- `maqam_khass`: كلُّ لفظٍ في `SLGE.Maqam.mawsulKhass` مقبولٌ هنا لمعنًى من سمته، بصلةٍ خبريّةٍ وعائدٍ مستترٍ موافق.

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/mawsul/tajmid.json`؛
`hawkama/منهج_الضوابط.md`). ونتيجتُها على الضابط في `Jisr/MawsulQiyas.lean`، لا هنا.

**المبرهنات** (بالمعيار الموحَّد في `Nizam/Asas.lean`)، وهي خواصُّ هذا التعيين على مجاله، لا قوانينُ في اللغة:
- تعريفيّة (9): `ghayr_muttasiq_la_hukm`، `lafz_khata`، `sila_khata`، `bila_sila`، `silat_al`، `silat_ghayriha`، `la_aid_khata`،
  `tashdid_la_yughayyir`، `lugha_la_tughayyir`. وبرهانُها فكُّ التعريفات وتفكيكُ الحالات.
- لكلّ (1): `ghayr_maqbul_bila` (تستدعي مساعداتٍ خاصّةً في الملفّ: سلامةُ كلّ حكمٍ جزئيّ وسلامةُ الضمّ).
- على الشاهد (3): `asma_qatr`، `maqam_khass`، `shawahid`.

**حدُّه.** المدخلُ تحليلٌ يُعطى؛ ولا إعرابَ لـ«أي» ولا شروطَ لحذف العائد (س159–165)؛ ولا تفريقَ بين العاقل وغيره؛ ولا وصلَ بالقارئ ولا بالمحرّك.
-/

namespace Jisr
namespace Mawsul

inductive Lafz
  | alladhi | allati | alladhani | allatani | alladhayni | allatayni | alladhiyani | allatiyani | alladhina | alladhuna
  | alula | allai | allati_j | allat | allaa | man | ma | ayy | al | dhu | dhat | dhawat | dha
  deriving DecidableEq, Repr

/-- اللفظُ كما في المواصفة. -/
def Lafz.nass : Lafz → String
  | .alladhi => "الذي" | .allati => "التي" | .alladhani => "اللذان" | .allatani => "اللتان" | .alladhayni => "اللذين"
  | .allatayni => "اللتين" | .alladhiyani => "اللذيان" | .allatiyani => "اللتيان" | .alladhina => "الذين" | .alladhuna => "اللذون"
  | .alula => "الألى" | .allai => "اللائي" | .allati_j => "اللاتي" | .allat => "اللات" | .allaa => "اللاء" | .man => "من"
  | .ma => "ما" | .ayy => "أي" | .al => "أل" | .dhu => "ذو" | .dhat => "ذات" | .dhawat => "ذوات" | .dha => "ذا"

/-- آخرُه نون. -/
def Lafz.nun : Lafz → Bool
  | .alladhani | .allatani | .alladhayni | .allatayni | .alladhiyani | .allatiyani | .alladhina | .alladhuna => true
  | _ => false

/-- المشترك: لكلّ معنى. -/
def Lafz.mushtarak : Lafz → Bool
  | .man | .ma | .ayy | .al | .dhu | .dha => true
  | _ => false

inductive Sima
  | mufradMudhakkar | mufradMuannath | muthannaMudhakkar | muthannaMuannath | jamMudhakkar | jamMuannath
  deriving DecidableEq, Repr

inductive Mawdi | raf | nasb | jarr
  deriving DecidableEq, Repr

inductive Lugha | ghayrMadhkura | tayyi
  deriving DecidableEq, Repr

inductive Qabl | maIstifham | manIstifham | ghayruhuma
  deriving DecidableEq, Repr

inductive Sila
  | jumlaKhabariyya | jumlaInshaiyya | zarfTamm | zarfNaqis | jarrTamm | jarrNaqis | wasfSarih | ismTafdil | filMurab | laSila
  deriving DecidableEq, Repr

inductive Aid | zahir | mustatir | mahdhuf | laAid
  deriving DecidableEq, Repr

structure Dakhil where
  lafz : Lafz
  marji : Sima
  mawdi : Mawdi
  tashdid : Bool
  lugha : Lugha
  qabl : Qabl
  mulgha : Bool
  sila : Sila
  aid : Aid
  aidSima : Option Sima   -- `none`: «لا عائد»
  deriving DecidableEq, Repr

inductive Hukm | maqbul | khata | laHukm
  deriving DecidableEq, Repr

inductive Daraja | qalil | nazr | lugha | bila
  deriving DecidableEq, Repr

structure Jawab where
  hukm : Hukm
  daraja : List Daraja
  deriving DecidableEq, Repr

def maqbulJ (ds : List Daraja) : Jawab := ⟨.maqbul, ds⟩
def khataJ : Jawab := ⟨.khata, [.bila]⟩
def laHukmJ : Jawab := ⟨.laHukm, [.bila]⟩

/-- اتّساقُ الحقول. -/
def muttasiq (d : Dakhil) : Bool :=
  (!d.tashdid || d.lafz.nun) && (!d.mulgha || decide (d.lafz = .dha)) &&
  (decide (d.aid = .laAid) == d.aidSima.isNone)

def muthannaM (m : Sima) : Bool := decide (m = .muthannaMudhakkar)
def muthannaF (m : Sima) : Bool := decide (m = .muthannaMuannath)

/-- حكمُ اللفظ بمعناه وموضعه ولغته وما قبله. -/
def lafzJ (d : Dakhil) : Jawab :=
  let yes (b : Bool) : Jawab := if b then maqbulJ [.bila] else khataJ
  match d.lafz with
  | .alladhi => yes (decide (d.marji = .mufradMudhakkar))
  | .allati => yes (decide (d.marji = .mufradMuannath))
  | .alladhani => yes (muthannaM d.marji && decide (d.mawdi = .raf))
  | .allatani => yes (muthannaF d.marji && decide (d.mawdi = .raf))
  | .alladhayni => yes (muthannaM d.marji && decide (d.mawdi ≠ .raf))
  | .allatayni => yes (muthannaF d.marji && decide (d.mawdi ≠ .raf))
  | .alladhiyani | .allatiyani => khataJ
  | .alladhina | .alula => yes (decide (d.marji = .jamMudhakkar))
  | .alladhuna => if decide (d.marji = .jamMudhakkar) && decide (d.mawdi = .raf) then maqbulJ [.lugha] else khataJ
  | .allai | .allati_j | .allat => yes (decide (d.marji = .jamMuannath))
  | .allaa =>
    if decide (d.marji = .jamMuannath) then maqbulJ [.bila]
    else if decide (d.marji = .jamMudhakkar) then maqbulJ [.nazr]
    else khataJ
  | .man | .ma | .ayy | .al => maqbulJ [.bila]
  | .dhu => if decide (d.lugha = .tayyi) then maqbulJ [.bila] else laHukmJ
  | .dhat => if decide (d.lugha = .tayyi) then yes (decide (d.marji = .mufradMuannath)) else laHukmJ
  | .dhawat => if decide (d.lugha = .tayyi) then yes (decide (d.marji = .jamMuannath)) else laHukmJ
  | .dha =>
    if decide (d.qabl ≠ .ghayruhuma) && !d.mulgha then maqbulJ [.bila] else laHukmJ

/-- حكمُ الصلة. -/
def silaJ (l : Lafz) (s : Sila) : Jawab :=
  match l with
  | .al =>
    match s with
    | .wasfSarih => maqbulJ [.bila]
    | .filMurab => maqbulJ [.qalil]
    | _ => khataJ
  | _ =>
    match s with
    | .jumlaKhabariyya | .zarfTamm | .jarrTamm => maqbulJ [.bila]
    | _ => khataJ

/-- حكمُ العائد. -/
def aidJ (d : Dakhil) : Jawab :=
  match d.aid, d.aidSima with
  | .laAid, _ => khataJ
  | _, none => laHukmJ
  | a, some s =>
    if decide (a = .mahdhuf) && !decide (d.sila = .jumlaKhabariyya) then laHukmJ
    else if decide (s = d.marji) then maqbulJ [.bila]
    else if d.lafz.mushtarak && decide (s = .mufradMudhakkar) then laHukmJ
    else khataJ

/-- ضمُّ جوابين: أوّلُ غير المقبول، وإلّا المقبولُ بدرجاتهما المذكورة. -/
def damm (a b : Jawab) : Jawab :=
  if a.hukm ≠ .maqbul then a
  else if b.hukm ≠ .maqbul then b
  else
    let ds := (a.daraja ++ b.daraja).filter (· ≠ .bila)
    maqbulJ (if ds.isEmpty then [.bila] else ds)

/-- **الحكم.** -/
def jawab (d : Dakhil) : Jawab :=
  if !muttasiq d then laHukmJ
  else damm (lafzJ d) (damm (silaJ d.lafz d.sila) (aidJ d))

/-! ## الأسانيد -/

/-- الأسانيد: (القاعدة، المصدر، من سطر، إلى سطر، القطعةُ حرفيّةً بعد وصل الأسطر بمسافة). -/
def asanid : List (String × String × Nat × Nat × String) :=
  [("khass_mufrad", "qatr", 137, 137, "ثم الموصول، وهو الذي والتي،"),
   ("muthanna", "qatr", 137, 138, "واللذان واللتان بالألف رفعا وبالياء جرا ms03 ونصبا،"),
   ("jam_mudhakkar", "qatr", 138, 138, "ولجمع المذكر الذين بالياء مطلقا والألى،"),
   ("jam_muannath", "qatr", 138, 139, "ولجمع المؤنث اللائي واللاتي،"),
   ("mushtarak", "qatr", 139, 139, "وبمعنى الجميع من وما وأي،"),
   ("al", "qatr", 139, 140, "وأل في وصف صريح لغير تفضيل كالضارب والمضروب،"),
   ("dhu", "qatr", 140, 140, "وذو في لغة طي،"),
   ("dha", "qatr", 140, 140, "وذا بعد ما أو من الاستفهاميتين."),
   ("silat_al", "qatr", 140, 140, "وصلة أل الوصف،"),
   ("sila", "qatr", 141, 141, "وصلة غيرها إما جملة خبرية ذات ضمير طبق للموصول يسمى عائدا، وقد يحذف"),
   ("shibh", "qatr", 143, 143, "أو ظرف أو جار ومجرور تامان"),
   ("khass_A", "alfiyya", 147, 147, "موصول الأسماء الذي الأنثى التي ... واليا إذا ما ثنيا لا تثبت"),
   ("tashdid", "alfiyya", 148, 148, "والنون إن تشدد فلا ملامه"),
   ("jam_A", "alfiyya", 150, 150, "جمع الذى الألى الذين مطلقا ... وبعضهم بالواو رفعا نطقا"),
   ("jam_muannath_A", "alfiyya", 151, 151, "باللات واللاء التي قد جمعا ... واللاء كالذين نزرا وقعا"),
   ("mushtarak_A", "alfiyya", 152, 152, "ومن وما وأل تساوي ما ذكر ... وهكذا ذو عند طيئ شهر"),
   ("dhat", "alfiyya", 153, 153, "وكالتي أيضا لديهم ذات ... وموضع اللاتي أتى ذوات"),
   ("dha_A", "alfiyya", 154, 154, "ومثل ماذا بعدما استفهام ... أومن إذا لم تلغ في الكلام"),
   ("sila_lazima", "alfiyya", 155, 155, "وكلها يلزم ms03 بعده صله ... على ضمير لائق مشتمله"),
   ("shibh_A", "alfiyya", 156, 156, "وجملة أو شبهها الذي وصل"),
   ("al_A", "alfiyya", 157, 157, "وصفة صريحة صلة أل ... وكونها بمعرب الأفعال قل")]

/-! ## المبرهنات -/

/-- **الحقولُ غيرُ المتّسقة «لا حكم».** -/
theorem ghayr_muttasiq_la_hukm (d : Dakhil) (h : muttasiq d = false) : jawab d = laHukmJ := by
  simp [jawab, h]

/-- **اللفظُ لا يوافق معناه أو موضعه: خطأ**، أيًّا كانت الصلةُ والعائد. -/
theorem lafz_khata (d : Dakhil) (hm : muttasiq d = true) (h : lafzJ d = khataJ) : jawab d = khataJ := by
  simp [jawab, hm, h, damm, khataJ]

/-- **الصلةُ مقدَّمةٌ على العائد:** إن قُبل اللفظُ وكانت الصلةُ خطأً فالجوابُ خطأ. -/
theorem sila_khata (d : Dakhil) (hm : muttasiq d = true) (hl : (lafzJ d).hukm = .maqbul)
    (hs : silaJ d.lafz d.sila = khataJ) : jawab d = khataJ := by
  simp [jawab, hm, hl, hs, damm, khataJ]

/-- **لا موصولَ بلا صلة.** -/
theorem bila_sila (l : Lafz) : silaJ l .laSila = khataJ := by
  cases l <;> rfl

/-- **صلةُ «أل» الوصفُ الصريح، والفعلُ المعرب قليل، وما سواهما خطأ.** -/
theorem silat_al (s : Sila) :
    silaJ .al s = (if s = .wasfSarih then maqbulJ [.bila] else if s = .filMurab then maqbulJ [.qalil] else khataJ) := by
  cases s <;> rfl

/-- **وصلةُ غيرها الجملةُ الخبريّةُ والظرفُ والجارُّ التامّان، وما سواها خطأ.** -/
theorem silat_ghayriha (l : Lafz) (s : Sila) (hl : l ≠ .al) :
    silaJ l s = (if s = .jumlaKhabariyya ∨ s = .zarfTamm ∨ s = .jarrTamm then maqbulJ [.bila] else khataJ) := by
  cases l <;> cases s <;> simp_all [silaJ]

/-- **لا صلةَ بلا عائد.** -/
theorem la_aid_khata (d : Dakhil) (h : d.aid = .laAid) : aidJ d = khataJ := by
  simp [aidJ, h]

/-- **التشديدُ لا يغيّر الجواب** في لفظٍ آخرُه نون («فلا ملامه»). -/
theorem tashdid_la_yughayyir (d : Dakhil) (h : d.lafz.nun = true) :
    jawab { d with tashdid := true } = jawab { d with tashdid := false } := by
  simp [jawab, muttasiq, h, lafzJ, aidJ, silaJ]

/-- **اللغةُ لا تغيّر إلّا «ذو» و«ذات» و«ذوات».** -/
theorem lugha_la_tughayyir (d : Dakhil) (l : Lugha) (h : d.lafz ≠ .dhu ∧ d.lafz ≠ .dhat ∧ d.lafz ≠ .dhawat) :
    jawab { d with lugha := l } = jawab d := by
  obtain ⟨lf, m, w, t, lg, q, ml, s, a, as⟩ := d
  simp only at h
  cases lf <;> simp_all [jawab, muttasiq, lafzJ, aidJ, silaJ]

/-- جوابٌ سليم: ما ليس مقبولًا فدرجتُه `[bila]`. -/
def Jawab.salim (j : Jawab) : Prop := j.hukm ≠ .maqbul → j.daraja = [.bila]

private theorem lafzJ_salim (d : Dakhil) : (lafzJ d).salim := by
  obtain ⟨lf, m, w, t, lg, q, ml, s, a, as⟩ := d
  cases lf <;> simp only [lafzJ, Jawab.salim] <;> (repeat' split) <;> simp [maqbulJ, khataJ, laHukmJ]

private theorem silaJ_salim (l : Lafz) (s : Sila) : (silaJ l s).salim := by
  cases l <;> cases s <;> simp [silaJ, Jawab.salim, maqbulJ, khataJ]

private theorem aidJ_salim (d : Dakhil) : (aidJ d).salim := by
  obtain ⟨lf, m, w, t, lg, q, ml, s, a, as⟩ := d
  simp only [aidJ, Jawab.salim]; (repeat' split) <;> simp [maqbulJ, khataJ, laHukmJ]

private theorem damm_salim (a b : Jawab) (ha : a.salim) (hb : b.salim) : (damm a b).salim := by
  unfold damm Jawab.salim at *
  by_cases h1 : a.hukm = .maqbul <;> by_cases h2 : b.hukm = .maqbul <;> simp_all [maqbulJ]

/-- **ما ليس مقبولًا فدرجتُه `[bila]`.** -/
theorem ghayr_maqbul_bila (d : Dakhil) (h : (jawab d).hukm ≠ .maqbul) : (jawab d).daraja = [.bila] := by
  have hs : (jawab d).salim := by
    unfold jawab
    split
    · simp [Jawab.salim, laHukmJ]
    · exact damm_salim _ _ (lafzJ_salim d) (damm_salim _ _ (silaJ_salim _ _) (aidJ_salim d))
  exact hs h

/-! ## الصلة بـ SLGE -/

def lafzat : List Lafz :=
  [.alladhi, .allati, .alladhani, .allatani, .alladhayni, .allatayni, .alladhiyani, .allatiyani, .alladhina, .alladhuna,
   .alula, .allai, .allati_j, .allat, .allaa, .man, .ma, .ayy, .al, .dhu, .dhat, .dhawat, .dha]

/-- اللفظُ من نصّه. -/
def lafzMin (s : String) : Option Lafz := lafzat.find? (·.nass == s)

/-- **ألفاظُ `SLGE.Wad.mawsul` ألفاظٌ هنا، و«الموصول» رابعةُ `SLGE.Wad.maarif`.** -/
theorem asma_qatr :
    SLGE.Wad.mawsul.all (fun s => (lafzMin s).isSome) = true ∧ SLGE.Wad.maarif[3]? = some "الموصول" := by
  decide

/-- المعنى من سمة المالك (الشخصُ غائب، والجنسُ 0 مذكّر و1 مؤنّث، والعددُ 0 و1 و2). -/
def simaMin : SLGE.Maqam.Feat → Option Sima
  | (3, 0, 0) => some .mufradMudhakkar
  | (3, 1, 0) => some .mufradMuannath
  | (3, 0, 1) => some .muthannaMudhakkar
  | (3, 1, 1) => some .muthannaMuannath
  | (3, 0, 2) => some .jamMudhakkar
  | (3, 1, 2) => some .jamMuannath
  | _ => none

/-- **كلُّ لفظٍ في `SLGE.Maqam.mawsulKhass` مقبولٌ هنا لمعنى سمته**، رفعًا، بصلةٍ خبريّةٍ وعائدٍ مستترٍ يوافقه. -/
theorem maqam_khass :
    SLGE.Maqam.mawsulKhass.all (fun x => match lafzMin x.1, simaMin x.2 with
      | some l, some m => jawab ⟨l, m, .raf, false, .ghayrMadhkura, .ghayruhuma, false, .jumlaKhabariyya, .mustatir, some m⟩ ==
          maqbulJ [.bila]
      | _, _ => false) = true := by
  decide

/-- **الشواهد** (تحليلُ البنّاء لأمثلة النطاق). -/
theorem shawahid :
    let d (l : Lafz) (m : Sima) (w : Mawdi) (s : Sila) : Dakhil := ⟨l, m, w, false, .ghayrMadhkura, .ghayruhuma, false, s, .mustatir, some m⟩
    jawab (d .alladhi .mufradMudhakkar .raf .jumlaKhabariyya) = maqbulJ [.bila] ∧
    jawab (d .allati .mufradMudhakkar .raf .jumlaKhabariyya) = khataJ ∧
    jawab (d .alladhayni .muthannaMudhakkar .raf .jumlaKhabariyya) = khataJ ∧
    jawab (d .alladhayni .muthannaMudhakkar .jarr .jumlaKhabariyya) = maqbulJ [.bila] ∧
    jawab { d .alladhani .muthannaMudhakkar .raf .jumlaKhabariyya with tashdid := true } = maqbulJ [.bila] ∧
    jawab (d .alladhiyani .muthannaMudhakkar .raf .jumlaKhabariyya) = khataJ ∧
    jawab (d .alladhina .jamMudhakkar .nasb .jumlaKhabariyya) = maqbulJ [.bila] ∧
    jawab (d .alladhuna .jamMudhakkar .raf .jumlaKhabariyya) = maqbulJ [.lugha] ∧
    jawab (d .alladhuna .jamMudhakkar .jarr .jumlaKhabariyya) = khataJ ∧
    jawab (d .allaa .jamMudhakkar .raf .jumlaKhabariyya) = maqbulJ [.nazr] ∧
    jawab (d .man .jamMuannath .raf .jumlaKhabariyya) = maqbulJ [.bila] ∧
    jawab (d .al .mufradMudhakkar .raf .wasfSarih) = maqbulJ [.bila] ∧
    jawab (d .al .mufradMudhakkar .raf .ismTafdil) = khataJ ∧
    jawab (d .al .mufradMudhakkar .raf .filMurab) = maqbulJ [.qalil] ∧
    jawab (d .al .mufradMudhakkar .raf .jumlaKhabariyya) = khataJ ∧
    jawab (d .dhu .mufradMudhakkar .raf .jumlaKhabariyya) = laHukmJ ∧
    jawab { d .dhu .mufradMudhakkar .raf .jumlaKhabariyya with lugha := .tayyi } = maqbulJ [.bila] ∧
    jawab { d .dhat .mufradMuannath .raf .jumlaKhabariyya with lugha := .tayyi } = maqbulJ [.bila] ∧
    jawab { d .dha .mufradMudhakkar .raf .jumlaKhabariyya with qabl := .maIstifham } = maqbulJ [.bila] ∧
    jawab { d .dha .mufradMudhakkar .raf .jumlaKhabariyya with qabl := .maIstifham, mulgha := true } = laHukmJ ∧
    jawab (d .alladhi .mufradMudhakkar .raf .jumlaInshaiyya) = khataJ ∧
    jawab (d .alladhi .mufradMudhakkar .raf .zarfTamm) = maqbulJ [.bila] ∧
    jawab (d .alladhi .mufradMudhakkar .raf .zarfNaqis) = khataJ ∧
    jawab (d .alladhi .mufradMudhakkar .raf .laSila) = khataJ ∧
    jawab { d .alladhi .mufradMudhakkar .raf .jumlaKhabariyya with aid := .laAid, aidSima := none } = khataJ ∧
    jawab { d .alladhi .mufradMudhakkar .raf .jumlaKhabariyya with aid := .mahdhuf } = maqbulJ [.bila] ∧
    jawab { d .alladhi .mufradMudhakkar .raf .jumlaKhabariyya with aidSima := some .mufradMuannath } = khataJ ∧
    jawab { d .man .jamMuannath .raf .jumlaKhabariyya with aidSima := some .mufradMudhakkar } = laHukmJ := by
  decide

end Mawsul
end Jisr
