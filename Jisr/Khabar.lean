import SLGE.Wad
import SLGE.Simat2
import Aql.Isnad

/-!
# الخبرُ في قطر الندى (س157–162) والألفية (س177–188)

**الطلب.** قولُ المالك 2026-10-28 (لفظُه ووقتُه، 00:33 بتوقيت عمّان، من ملخّص الجلسة بعد ضغطها):
«يجب الاستفادة من ما لم نغطه وموجود في المراجع سواء استنتجته انت او موجود في المرفق وعمل lean له شرط ان يكون متناسق ومتكامل ومترابط مع البرهان واالحساب وفق الدستور وأفضل الممارسات … نفذ انت والوكلاء  و»
والجملةُ الاسميّة في Lean القائمة: الرابطةُ الإسناديّة بأنماطها (`Aql.Isnad`: الصغرى والكبرى بشرط «من سببه» والظرفيّة)، وإطاراتُ
المالك (`SLGE.Tarkib`: الخبرُ الجملةُ برابطٍ مستترٍ يحيل إلى المبتدأ)، ومطابقةُ الخبر المفرد (`SLGE.Simat2`: الجامدُ فارغ، والمشتقُّ ذو ضمير)؛ بلا حكمٍ
على أنواع الرابط غيرِ الضمير، ولا على الإخبار بالزمان عن الذات، ولا على الوصف ومرفوعه. واختيارُ هذه القطعة، ونطاقُها، قرارُ البنّاء.

**المصدر.** `qatr.txt` المختوم (`2d9241be…`) الأسطر 157–162 إلى «"ما مضروب العمران"»، و`alfiyya.txt` المختوم (`13b351a0…`) الأسطر 177–188.
وما سواها من الباب (الابتداءُ بالنكرة، وترتيبُ الجزأين، والحذفُ، وتعدّدُ الخبر) خارجَ النطاق. والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها
`tahaqquq/test_khabar.py` على المودَعين موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/khabar/wasf.md` بأعيانها): البناء (مبتدأٌ وخبر، أو وصفٌ ومرفوعُه)؛ وفي الأوّل: ما يدلّ عليه
المبتدأ، ونوعُ الخبر، والرابط، وما يرفعه المفرد، ولمن معنى المشتقّ، والإفادة؛ وفي الثاني: الاعتماد، وعددا الوصف والمرفوع، والإعرابُ المسؤول عنه؛
و`la` حيث لا ينطبق الحقل. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ قارئٍ من النصّ.**

**المخرج** `Jawab`: الحكم (`maqbul` أو `khata` أو `laHukm`)، والدرجةُ قائمةً (`qalil`، `bitawil`، `bila`)؛ وحين لا يكون الحكمُ «مقبولًا» فالدرجةُ
`[bila]`.

**الحكم** (`jawab`): قولُ كلّ مصدرٍ وحده (`qatr`، `alfiyya`: حكمٌ بدرجته، أو سكوت)، ثمّ الجمعُ بينهما (`jamaa`): ما سكت عنه مصدرٌ فحكمُه حكمُ الآخر،
وما اختلفا في حكمه «لا حكم»، وما اتّفقا على قبوله بدرجتين فالدرجتان معًا (نصُّ المواصفة في «المصدران»). وقبل ذلك اتّساقُ الحقول (`muttasiq`)، وما
خالفه «لا حكم».

1. **الخبرُ الجملة** (المصدران): لا بدّ له من رابط («والخبر جملة لها رابط»، قطر س157؛
   «ومفردا يأتي ويأتي جمله ... حاوية معنى الذي سيقت له»، ألفيّة س183)؛ والرابطُ ضميرٌ («زيد أبوه قائم»)، أو اسمُ إشارة («ولباس التقوى ذلك خير»)،
   أو إعادةُ المبتدأ («الحاقة ما الحاقة»)، أو عمومٌ («زيد نعم الرجل»)؛ ولا رابطَ في الجملة التي هي المبتدأ («إلا في نحو: {قل هو الله أحد}»، س158؛
   «وإن تكن إياه معنى اكتفى ... بها كنطقي الله حسبي وكفى»، س184). وبلا رابطٍ خطأ.
2. **الخبرُ المفرد** (الألفية وحدها؛ والقطرُ في نطاقه لا يذكره)، من «والمفرد الجامد فارغ وإن ... يشتق فهو ذو ضمير مستكن» (س185)
   و«وأبرزنه مطلقا حيث تلا ... ما ليس معناه له محصلا» (س186):
   - الجامدُ فارغ: بلا مرفوعٍ مقبول، وبضميرٍ أو ظاهرٍ خطأ.
   - المشتقُّ ذو ضميرٍ مستكنّ، ويُبرَز مطلقًا إذا تلا ما ليس معناه له: المستكنُّ لصاحبه والبارزُ لغيره مقبولان، والبارزُ لصاحبه والمستكنُّ لغيره خطأ،
     وبلا ضميرٍ خطأ؛ ورفعُ الظاهر سكوت.
3. **الظرفُ والجارُّ والمجرور** (المصدران): «وظرفا منصوبا … وجارا ومجرورا» (قطر س159)، «وأخبروا بظرف أو بحرف جر» (ألفيّة س187)؛ مقبول.
4. **الزمانُ** (المصدران): عن الذات غيرَ مفيدٍ خطأ («ولا يخبر بالزمان عن الذات»، قطر س160–161؛ «ولا يكون اسم زمان خبرا ... عن جثة وإن يفد فأخبرا»،
   س188)؛ ومفيدًا مقبولٌ متأوَّلًا في القطر («والليلة والهلال متأول»، س161) وبلا درجةٍ في الألفية («وإن يفد فأخبرا»)، فالدرجتان معًا. وعن المعنى:
   مقبولٌ في القطر بإطلاق «وظرفا»، وفي الألفية مقبولٌ مفيدًا، وغيرَ مفيدٍ خطأ («والخبر الجزء المتم الفائدة»، س182)، فغيرُ المفيد عن المعنى «لا حكم»
   لاختلافهما.
5. **الوصفُ ومرفوعُه:**
   - القطر: «ويغني عن الخبر مرفوع وصف معتمد على استفهام، أو نفي» (س161–162): الوصفُ المفردُ معتمدًا مرفوعُه فاعلٌ أغنى، مقبول، وبلا اعتمادٍ خطأ
     (شرطُ الصورة)؛ ولا يحكم في الإعراب الآخر.
   - الألفية: «وأول مبتدأ والثاني ... فاعل اغنى في أسار ذان» (س178)، و«وقس كاستفهام النفي وقد ... يجوز نحو فائز أولو الرشد» (س179: بلا اعتمادٍ
     قليل)، و«والثاني مبتدا وذا الوصف خبر ... إن في سوى الإفراد طبقا استقر» (س180): إن طابق الوصفُ مرفوعَه في غير الإفراد فهو خبرٌ مقدَّم مقبول،
     والفاعلُ الذي أغنى خطأ؛ وإلّا فالخبرُ المقدَّم خطأ (شرطُ الصورة)، والفاعلُ مقبولٌ معتمدًا وقليلًا بلا اعتماد.

**ما هو تعيينُ البنّاء** (لا نصُّ النطاق):
- الروابطُ الخمسةُ مقبولةٌ في الجملتين الاسميّة والفعليّة، وفي ما يدلّ على ذاتٍ وعلى معنى؛ و«حاوية معنى الذي سيقت له» يشملها.
- «فارغ»: لا ضميرَ ولا ظاهر؛ و«ذو ضمير مستكن» لما معناه لصاحبه، والبارزُ له خطأ؛ والمشتقُّ الرافعُ ظاهرًا لا يحكم فيه النطاق.
- الإفادةُ في الزمان عن المعنى من «المتم الفائدة» (س182)؛ والقطرُ لا يقيّد الزمانَ عن المعنى بها.
- «وصف» في القطر مفردٌ كمثاليه («أقاطن قوم سلمى»، «ما مضروب العمران»)، وحكمُ المثنّى والمجموع من الألفية وحدها؛ والمطابقةُ في غير الإفراد شرطٌ للخبر
  المقدَّم، وهي فيه تُخرج الفاعلَ الذي أغنى؛ والاعتمادُ لا أثرَ له في الخبر المقدَّم.
- الشرطُ حكمٌ في الصورة بلا شرطها (مفتاحُ المواصفة)، وما لا يذكره مصدرٌ سكوتٌ منه.

**الصلة بقطع Lean القائمة:**
- `ibtida_wad`: «الابتداء» عاملٌ معنويٌّ في `SLGE.Wad.manawiF` يرفع الاسمين، بسطر القطر 152 (عنوانُ الباب).
- `isnad_kubra`: الكبرى برابطٍ ضميرٍ كلامٌ في `Aql.Isnad` وهنا مقبولة، وبلا سببٍ ليست كلامًا وهنا خطأ.
- **خلافٌ معلَن مع `Aql.Isnad.yastaghni`** (`khilaf_isnad_rabit`): الكبرى لا تكون كلامًا إلّا والمبتدأُ «من سببه» بإضمار (الكتاب س654–655)، والقطرُ
  والألفيةُ هنا تقبلان الإشارةَ والإعادةَ والعمومَ رابطًا؛ فالكبرى بلا إضمارٍ برابطٍ من هذه مقبولةٌ هنا وليست كلامًا هناك. والقرارُ للمالك.
- `isnad_wasf`: الوصفُ بفاعلٍ سببيّ كلامٌ في `Aql.Isnad` (س654)، والنطاقُ هنا ساكتٌ عن المشتقّ الرافع ظاهرًا («لا حكم»).
- `tarkib_rabit`: في إطارات المالك (`SLGE.Tarkib.framesL`) الخبرُ الجملةُ الفعليّة بفاعلٍ مستترٍ يحيل إلى المبتدأ مرخَّص، وبفاعلٍ حاضرٍ لا يحيل إليه غيرُ
  مرخَّص؛ وهنا الأوّلُ مقبولٌ والثاني بلا رابطٍ خطأ.
- `simat2_jamid`: في `SLGE.Simat.annOK2` الجامدُ لا يُطلب فيه ضمير، وهنا الجامدُ الفارغُ مقبول.

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/khabar/tajmid.json`؛
`hawkama/منهج_الضوابط.md`). ونتيجتُها على الضابط في `Jisr/KhabarQiyas.lean`، لا هنا.

**المبرهنات** (بالمعيار الموحَّد في `Nizam/Asas.lean`)، وهي خواصُّ هذا التعيين على مجاله، لا قوانينُ في اللغة:
- تعريفيّة (11): `bawwaba_la_hukm`، `jumla_bila_rabit`، `rawabit`، `zarf_maqbul`، `zaman_dhat`، `zaman_maana`، `mushtaq_ibraz`، `jamid_farigh`، `wasf_tabaq`،
  `bila_itimad`، `ikhtilaf_la_hukm` (اختلافُ المصدرين في الحكم «لا حكم»). وبرهانُها فكُّ التعريفات وتفكيكُ الحالات.
- لكلّ (2): `hukm_min_masdar` (لا حكمَ إلّا بقول مصدرٍ يحكم به؛ تستدعي مساعدًا خاصًّا `jamaa_min`)، `ghayr_maqbul_bila` (تستدعي المساعدَين الخاصّين
  `qatr_bila` و`alfiyya_bila`). والمساعداتُ الثلاثة تعريفيّة.
- على الشاهد (7): `ibtida_wad`، `isnad_kubra`، `khilaf_isnad_rabit`، `isnad_wasf`، `tarkib_rabit`، `simat2_jamid`، `shawahid`.

**حدُّه.** المدخلُ تحليلٌ يُعطى؛ ولا ابتداءَ بالنكرة ولا ترتيبَ ولا حذفَ ولا تعدّد (س152–155، س162–167؛ ألفيّة س189–207)؛ ولا تعلّقَ للظرف بمحذوف؛ ولا
وصلَ بالقارئ ولا بالمحرّك.
-/

namespace Jisr
namespace Khabar

inductive Binya | mubtadaKhabar | wasfMarfu
  deriving DecidableEq, Repr

inductive Jins | dhat | maana | la
  deriving DecidableEq, Repr

inductive NawKhabar | mufradJamid | mufradMushtaq | jumlaIsmiyya | jumlaFiliyya | zarfMakan | zarfZaman | jarMajrur | la
  deriving DecidableEq, Repr

inductive Rabit | damir | ishara | iada | umum | hiya | laRabit | la
  deriving DecidableEq, Repr

inductive Marfu | mustakin | bariz | zahir | laShay | la
  deriving DecidableEq, Repr

inductive Jaryan | lisahibihi | lighayrihi | la
  deriving DecidableEq, Repr

inductive Ifada | mufid | ghayrMufid | la
  deriving DecidableEq, Repr

inductive Itimad | istifham | nafy | laItimad | la
  deriving DecidableEq, Repr

inductive Adad | mufrad | muthanna | jam | la
  deriving DecidableEq, Repr

inductive Tahlil | failAghna | khabarMuqaddam | la
  deriving DecidableEq, Repr

structure Dakhil where
  binya : Binya
  jins : Jins
  khabar : NawKhabar
  rabit : Rabit
  marfu : Marfu
  jaryan : Jaryan
  ifada : Ifada
  itimad : Itimad
  wasfAdad : Adad
  marfuAdad : Adad
  tahlil : Tahlil
  deriving DecidableEq, Repr

inductive Hukm | maqbul | khata | laHukm
  deriving DecidableEq, Repr

inductive Daraja | qalil | bitawil | bila
  deriving DecidableEq, Repr

structure Jawab where
  hukm : Hukm
  daraja : List Daraja
  deriving DecidableEq, Repr

def maqbulJ (ds : List Daraja) : Jawab := ⟨.maqbul, ds⟩
def khataJ : Jawab := ⟨.khata, [.bila]⟩
def laHukmJ : Jawab := ⟨.laHukm, [.bila]⟩

/-! ## ١. اتّساقُ الحقول -/

def NawKhabar.jumla : NawKhabar → Bool
  | .jumlaIsmiyya | .jumlaFiliyya => true
  | _ => false

def NawKhabar.mufrad : NawKhabar → Bool
  | .mufradJamid | .mufradMushtaq => true
  | _ => false

/-- `la` في الحقل إذا وفقط إذا لم ينطبق. -/
def muttasiq (d : Dakhil) : Bool :=
  match d.binya with
  | .mubtadaKhabar =>
    d.jins != .la && d.khabar != .la &&
    (d.rabit != .la) == d.khabar.jumla && (d.marfu != .la) == d.khabar.mufrad &&
    (d.jaryan != .la) == (d.khabar == .mufradMushtaq) && (d.ifada != .la) == (d.khabar == .zarfZaman) &&
    d.itimad == .la && d.wasfAdad == .la && d.marfuAdad == .la && d.tahlil == .la
  | .wasfMarfu =>
    d.jins == .la && d.khabar == .la && d.rabit == .la && d.marfu == .la && d.jaryan == .la && d.ifada == .la &&
    d.itimad != .la && d.wasfAdad != .la && d.marfuAdad != .la && d.tahlil != .la

/-! ## ٢. قولُ كلّ مصدر -/

/-- قولُ مصدر: حكمٌ بدرجته، أو سكوت (`none`). -/
abbrev Qawl := Option Jawab

/-- الوصفُ يطابق مرفوعَه في غير الإفراد. -/
def tabaq (d : Dakhil) : Bool := d.wasfAdad == d.marfuAdad && d.wasfAdad != .mufrad

/-- **القطر** (س157–162). -/
def qatr (d : Dakhil) : Qawl :=
  match d.binya with
  | .mubtadaKhabar =>
    match d.khabar with
    | .jumlaIsmiyya | .jumlaFiliyya => some (if d.rabit = .laRabit then khataJ else maqbulJ [.bila])
    | .zarfMakan | .jarMajrur => some (maqbulJ [.bila])
    | .zarfZaman =>
      match d.jins, d.ifada with
      | .dhat, .mufid => some (maqbulJ [.bitawil])
      | .dhat, _ => some khataJ
      | _, _ => some (maqbulJ [.bila])
    | _ => none
  | .wasfMarfu =>
    match d.tahlil with
    | .failAghna =>
      if d.wasfAdad = .mufrad then some (if d.itimad = .laItimad then khataJ else maqbulJ [.bila]) else none
    | _ => none

/-- **الألفية** (س177–188). -/
def alfiyya (d : Dakhil) : Qawl :=
  match d.binya with
  | .mubtadaKhabar =>
    match d.khabar with
    | .jumlaIsmiyya | .jumlaFiliyya => some (if d.rabit ≠ .laRabit then maqbulJ [.bila] else khataJ)
    | .mufradJamid => some (if d.marfu = .laShay then maqbulJ [.bila] else khataJ)
    | .mufradMushtaq =>
      match d.jaryan, d.marfu with
      | .lisahibihi, .mustakin => some (maqbulJ [.bila])
      | .lighayrihi, .bariz => some (maqbulJ [.bila])
      | _, .zahir => none
      | _, _ => some khataJ
    | .jarMajrur | .zarfMakan => some (maqbulJ [.bila])
    | .zarfZaman => some (if d.ifada = .mufid then maqbulJ [.bila] else khataJ)
    | .la => none
  | .wasfMarfu =>
    match d.tahlil with
    | .failAghna =>
      some (if tabaq d then khataJ else if d.itimad = .laItimad then maqbulJ [.qalil] else maqbulJ [.bila])
    | .khabarMuqaddam => some (if tabaq d then maqbulJ [.bila] else khataJ)
    | .la => none

/-! ## ٣. الجمعُ بين المصدرين، والجواب -/

/-- درجاتُ القبولين بلا تكرار. -/
def damm (a b : List Daraja) : List Daraja := a ++ b.filter (fun x => !a.contains x)

/-- **الجمع:** ما سكت عنه أحدُهما فحكمُ الآخر؛ واتّفاقُهما على القبول بدرجتيهما معًا، وعلى الخطأ خطأ؛ واختلافُهما في الحكم «لا حكم». -/
def jamaa : Qawl → Qawl → Jawab
  | none, none => laHukmJ
  | some a, none => a
  | none, some b => b
  | some a, some b =>
    if a.hukm = b.hukm then (if a.hukm = .maqbul then maqbulJ (damm a.daraja b.daraja) else a) else laHukmJ

def jawab (d : Dakhil) : Jawab :=
  if !muttasiq d then laHukmJ else jamaa (qatr d) (alfiyya d)

/-! ## ٤. الأسانيد -/

/-- القطعُ الحرفيّة: (الاسم، المصدر، السطرُ الأوّل، السطرُ الأخير، النصّ). -/
def asanid : List (String × String × Nat × Nat × String) :=
  [("jumla_rabit", "qatr", 157, 157, "والخبر جملة لها رابط ك"),
   ("rabit_ishara", "qatr", 157, 157, "{ولباس التقوى ذلك خير}"),
   ("rabit_iada", "qatr", 158, 158, "{الحاقة ما الحاقة}"),
   ("rabit_umum", "qatr", 158, 158, "زيد نعم الرجل"),
   ("hiya", "qatr", 158, 158, "إلا في نحو: {قل هو الله أحد}"),
   ("zarf", "qatr", 159, 159, "وظرفا منصوبا، نحو {والركب أسفل منكم}"),
   ("jar", "qatr", 159, 159, "وجارا ومجرورا ك {الحمد لله رب"),
   ("zaman_qatr", "qatr", 160, 161, "ولا يخبر بالزمان عن الذات، والليلة والهلال متأول."),
   ("wasf_qatr", "qatr", 161, 162, "ويغني عن الخبر مرفوع وصف معتمد على استفهام، أو نفي،"),
   ("wasf_mithal", "qatr", 162, 162, "أقاطن قوم سلمى"),
   ("wasf_mithal2", "qatr", 162, 162, "ما مضروب العمران"),
   ("fail_aghna", "alfiyya", 178, 178, "وأول مبتدأ والثاني ... فاعل اغنى في أسار ذان"),
   ("nafy_qalil", "alfiyya", 179, 179, "وقس كاستفهام النفي وقد ... يجوز نحو فائز أولو الرشد"),
   ("tabaq", "alfiyya", 180, 180, "والثاني مبتدا وذا الوصف خبر ... إن في سوى الإفراد طبقا استقر"),
   ("fida", "alfiyya", 182, 182, "والخبر الجزء المتم الفائدة"),
   ("jumla_hawiya", "alfiyya", 183, 183, "ومفردا يأتي ويأتي جمله ... حاوية معنى الذي سيقت له"),
   ("iyyahu", "alfiyya", 184, 184, "وإن تكن إياه معنى اكتفى ... بها كنطقي الله حسبي وكفى"),
   ("jamid_mushtaq", "alfiyya", 185, 185, "والمفرد الجامد فارغ وإن ... يشتق فهو ذو ضمير مستكن"),
   ("ibraz", "alfiyya", 186, 186, "وأبرزنه مطلقا حيث تلا ... ما ليس معناه له محصلا"),
   ("zarf_alfiyya", "alfiyya", 187, 187, "وأخبروا بظرف أو بحرف جر"),
   ("zaman_alfiyya", "alfiyya", 188, 188, "ولا يكون اسم زمان خبرا ... عن جثة وإن يفد فأخبرا")]

/-! ## ٥. المبرهنات -/

/-- **البوّابة:** حقولٌ غيرُ متّسقة «لا حكم». -/
theorem bawwaba_la_hukm (d : Dakhil) (h : muttasiq d = false) : jawab d = laHukmJ := by
  simp [jawab, h]

/-- **الخبرُ الجملةُ بلا رابطٍ خطأ** في المصدرين. -/
theorem jumla_bila_rabit (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hj : d.khabar.jumla = true)
    (hr : d.rabit = .laRabit) : jawab d = khataJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hj hr
    subst hb hr
    cases k <;> simp [NawKhabar.jumla] at hj <;> simp [jawab, hm, qatr, alfiyya, jamaa, khataJ]

/-- **الروابطُ الخمسة مقبولة** بلا درجة. -/
theorem rawabit (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hj : d.khabar.jumla = true)
    (hr : d.rabit ≠ .laRabit) : jawab d = maqbulJ [.bila] := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hj hr
    subst hb
    cases k <;> simp [NawKhabar.jumla] at hj <;> simp [jawab, hm, qatr, alfiyya, jamaa, hr, damm, maqbulJ]

/-- **الظرفُ المكانيّ والجارُّ والمجرور مقبولان** في المصدرين. -/
theorem zarf_maqbul (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar)
    (hk : d.khabar = .zarfMakan ∨ d.khabar = .jarMajrur) : jawab d = maqbulJ [.bila] := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hk
    subst hb
    rcases hk with rfl | rfl <;> simp [jawab, hm, qatr, alfiyya, jamaa, damm, maqbulJ]

/-- **الزمانُ عن الذات:** غيرَ مفيدٍ خطأ، ومفيدًا مقبولٌ بالدرجتين (متأوَّلًا في القطر، وبلا درجةٍ في الألفية). -/
theorem zaman_dhat (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hk : d.khabar = .zarfZaman)
    (hj : d.jins = .dhat) :
    jawab d = if d.ifada = .mufid then maqbulJ [.bitawil, .bila] else khataJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hk hj
    subst hb hk hj
    cases i <;> simp [jawab, hm, qatr, alfiyya, jamaa, damm, maqbulJ, khataJ]

/-- **الزمانُ عن المعنى:** مفيدًا مقبول، وغيرَ مفيدٍ «لا حكم» (القطرُ يقبله بإطلاق «وظرفا»، والألفيةُ تردّه بـ«المتم الفائدة»). -/
theorem zaman_maana (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hk : d.khabar = .zarfZaman)
    (hj : d.jins = .maana) :
    jawab d = if d.ifada = .mufid then maqbulJ [.bila] else laHukmJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hk hj
    subst hb hk hj
    cases i <;> simp [jawab, hm, qatr, alfiyya, jamaa, damm, maqbulJ, khataJ, laHukmJ]

/-- **المشتقّ:** المستكنُّ لصاحبه والبارزُ لغيره مقبولان؛ والظاهرُ «لا حكم»؛ وما سواها خطأ. -/
theorem mushtaq_ibraz (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hk : d.khabar = .mufradMushtaq) :
    jawab d =
      if (d.jaryan = .lisahibihi ∧ d.marfu = .mustakin) ∨ (d.jaryan = .lighayrihi ∧ d.marfu = .bariz) then maqbulJ [.bila]
      else if d.marfu = .zahir then laHukmJ else khataJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hk
    subst hb hk
    cases y <;> cases m <;> simp_all [jawab, qatr, alfiyya, jamaa, muttasiq, NawKhabar.jumla, NawKhabar.mufrad]

/-- **الجامدُ فارغ:** بلا مرفوعٍ مقبول، وما سواه خطأ. -/
theorem jamid_farigh (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .mubtadaKhabar) (hk : d.khabar = .mufradJamid) :
    jawab d = if d.marfu = .laShay then maqbulJ [.bila] else khataJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hk
    subst hb hk
    cases m <;> simp_all [jawab, qatr, alfiyya, jamaa, muttasiq, NawKhabar.jumla, NawKhabar.mufrad]

/-- **المطابقةُ في غير الإفراد:** الخبرُ المقدَّم مقبول، والفاعلُ الذي أغنى خطأ (الألفية س180؛ والقطرُ ساكتٌ في غير المفرد). -/
theorem wasf_tabaq (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .wasfMarfu) (ht : tabaq d = true) :
    jawab d = if d.tahlil = .khabarMuqaddam then maqbulJ [.bila] else khataJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb
    subst hb
    have hw : w ≠ .mufrad := by
      intro e; subst e; simp [tabaq] at ht
    cases l <;> simp_all [jawab, qatr, alfiyya, jamaa, muttasiq]

/-- **الوصفُ المفردُ بلا اعتماد، والمرفوعُ فاعلٌ أغنى: «لا حكم»** — القطرُ يشترط الاعتماد، والألفيةُ تقبله قليلًا. -/
theorem bila_itimad (d : Dakhil) (hm : muttasiq d = true) (hb : d.binya = .wasfMarfu) (hw : d.wasfAdad = .mufrad)
    (hi : d.itimad = .laItimad) (ht : d.tahlil = .failAghna) : jawab d = laHukmJ := by
  cases d with
  | mk b j k r m y i t w f l =>
    simp only at hb hw hi ht
    subst hb hw hi ht
    simp [jawab, hm, qatr, alfiyya, jamaa, tabaq, maqbulJ, khataJ, laHukmJ]

/-- **اختلافُ المصدرين في الحكم «لا حكم»**، لكلّ مدخلٍ متّسق. -/
theorem ikhtilaf_la_hukm (d : Dakhil) (a b : Jawab) (hm : muttasiq d = true) (ha : qatr d = some a) (hb : alfiyya d = some b)
    (h : a.hukm ≠ b.hukm) : jawab d = laHukmJ := by
  simp [jawab, hm, ha, hb, jamaa, h]

private theorem jamaa_min (q a : Qawl) (h : (jamaa q a).hukm ≠ .laHukm) :
    (∃ j, q = some j ∧ j.hukm = (jamaa q a).hukm) ∨ (∃ j, a = some j ∧ j.hukm = (jamaa q a).hukm) := by
  cases q with
  | none =>
    cases a with
    | none => simp [jamaa, laHukmJ] at h
    | some b => right; exact ⟨b, rfl, by simp [jamaa]⟩
  | some x =>
    cases a with
    | none => left; exact ⟨x, rfl, by simp [jamaa]⟩
    | some b =>
      left
      refine ⟨x, rfl, ?_⟩
      by_cases e : x.hukm = b.hukm
      · by_cases em : x.hukm = .maqbul
        · have hb' : b.hukm = .maqbul := e ▸ em
          simp [jamaa, hb', em, maqbulJ]
        · have em' : b.hukm ≠ .maqbul := by rw [← e]; exact em
          simp [jamaa, e, em']
      · simp [jamaa, e, laHukmJ] at h

/-- **لا حكمَ إلّا بقول مصدر:** كلُّ «مقبول» أو «خطأ» في الجواب يقوله القطرُ أو الألفية. -/
theorem hukm_min_masdar (d : Dakhil) (h : (jawab d).hukm ≠ .laHukm) :
    (∃ j, qatr d = some j ∧ j.hukm = (jawab d).hukm) ∨ (∃ j, alfiyya d = some j ∧ j.hukm = (jawab d).hukm) := by
  by_cases hm : muttasiq d = true
  · have e : jawab d = jamaa (qatr d) (alfiyya d) := by simp [jawab, hm]
    rw [e] at h ⊢
    exact jamaa_min _ _ h
  · have e : jawab d = laHukmJ := by simp [jawab, hm]
    rw [e] at h; simp [laHukmJ] at h

private theorem qatr_bila (d : Dakhil) (j : Jawab) (h : qatr d = some j) (hj : j.hukm ≠ .maqbul) : j.daraja = [.bila] := by
  unfold qatr at h
  repeat' (split at h)
  all_goals (first | (injection h with h; subst h; simp_all [khataJ, maqbulJ]) | simp at h)

private theorem alfiyya_bila (d : Dakhil) (j : Jawab) (h : alfiyya d = some j) (hj : j.hukm ≠ .maqbul) :
    j.daraja = [.bila] := by
  unfold alfiyya at h
  repeat' (split at h)
  all_goals (first | (injection h with h; subst h; simp_all [khataJ, maqbulJ]) | simp at h)

/-- **الدرجةُ في غير المقبول `[bila]`.** -/
theorem ghayr_maqbul_bila (d : Dakhil) (h : (jawab d).hukm ≠ .maqbul) : (jawab d).daraja = [.bila] := by
  by_cases hm : muttasiq d = true
  · have e : jawab d = jamaa (qatr d) (alfiyya d) := by simp [jawab, hm]
    rw [e] at h ⊢
    cases hq : qatr d with
    | none =>
      cases ha : alfiyya d with
      | none => simp [jamaa, laHukmJ]
      | some b => rw [hq, ha] at h; simp [jamaa] at h ⊢; exact alfiyya_bila d b ha h
    | some x =>
      cases ha : alfiyya d with
      | none => rw [hq, ha] at h; simp [jamaa] at h ⊢; exact qatr_bila d x hq h
      | some b =>
        rw [hq, ha] at h
        by_cases e2 : x.hukm = b.hukm
        · by_cases em : x.hukm = .maqbul
          · have hb' : b.hukm = .maqbul := e2 ▸ em
            simp [jamaa, hb', em, maqbulJ] at h
          · have em' : b.hukm ≠ .maqbul := by rw [← e2]; exact em
            simp [jamaa, e2, em']; exact qatr_bila d x hq em
        · simp [jamaa, e2, laHukmJ]
  · simp [jawab, hm, laHukmJ]

/-! ## ٦. الصلة بقطع Lean القائمة (على الشاهد) -/

/-- **الابتداء** عاملٌ معنويٌّ في `SLGE.Wad.manawiF` يرفع الاسمين، بسطر القطر 152. -/
theorem ibtida_wad :
    SLGE.Wad.manawiF.any (fun a => a.name == "الابتداء" && a.line == 152 &&
      a.eff == [(.ism, .raf), (.ism, .raf)]) = true := by
  decide

def mk (k : NawKhabar) (r : Rabit) (m : Marfu) (y : Jaryan) : Dakhil :=
  ⟨.mubtadaKhabar, .dhat, k, r, m, y, if k = .zarfZaman then .mufid else .la, .la, .la, .la, .la⟩

/-- **الكبرى في `Aql.Isnad`:** برابطٍ ضميرٍ كلام («كان زيد أبوه منطلق»، س9929–9930) وهنا مقبولة؛ وبلا سببٍ ليست كلامًا وهنا بلا رابطٍ خطأ. -/
theorem isnad_kubra :
    Aql.Isnad.yastaghni (.kubra Aql.Isnad.zayd (.sughra Aql.Isnad.abuhu Aql.Isnad.muntaliq)) = true ∧
    jawab (mk .jumlaIsmiyya .damir .la .la) = maqbulJ [.bila] ∧
    Aql.Isnad.yastaghni (.kubra Aql.Isnad.zayd (.sughra Aql.Isnad.amr Aql.Isnad.muntaliq)) = false ∧
    jawab (mk .jumlaIsmiyya .laRabit .la .la) = khataJ := by
  decide

/-- **خلافٌ معلَن مع `Aql.Isnad.yastaghni`:** الكبرى بلا إضمارٍ يعود على المبتدأ ليست كلامًا هناك، وبرابطٍ من الإشارة أو الإعادة أو العموم مقبولةٌ
هنا (القطر س157–158). والقرارُ للمالك. -/
theorem khilaf_isnad_rabit :
    Aql.Isnad.yastaghni (.kubra Aql.Isnad.zayd (.sughra Aql.Isnad.amr Aql.Isnad.muntaliq)) = false ∧
    jawab (mk .jumlaIsmiyya .ishara .la .la) = maqbulJ [.bila] ∧
    jawab (mk .jumlaIsmiyya .iada .la .la) = maqbulJ [.bila] ∧
    jawab (mk .jumlaFiliyya .umum .la .la) = maqbulJ [.bila] := by
  decide

/-- **الوصفُ بفاعلٍ سببيّ** كلامٌ في `Aql.Isnad` («عاقلا أبوه»، س654)، والنطاقُ هنا ساكتٌ عن المشتقّ الرافع ظاهرًا. -/
theorem isnad_wasf :
    Aql.Isnad.yastaghni (.sughra Aql.Isnad.zayd Aql.Isnad.aqilAbuhu) = true ∧
    jawab (mk .mufradMushtaq .la .zahir .lighayrihi) = laHukmJ := by
  decide

/-- **إطاراتُ المالك:** الخبرُ الجملةُ الفعليّة بفاعلٍ مستترٍ يحيل إلى المبتدأ مرخَّص، وبفاعلٍ حاضرٍ لا يحيل إليه غيرُ مرخَّص (`SLGE.Tarkib.mustatir`)؛
وهنا الأوّلُ برابطٍ ضميرٍ مقبول، والثاني بلا رابطٍ خطأ. -/
theorem tarkib_rabit :
    ((0, 0, [(0, 0, 0), (2, 0, 0), (3, 1, 1)]) : SLGE.Tarkib.Frame) ∈ SLGE.Tarkib.framesL ∧
    ((0, 0, [(0, 0, 0), (2, 0, 0), (3, 1, SLGE.Tarkib.deic)]) : SLGE.Tarkib.Frame) ∉ SLGE.Tarkib.framesL ∧
    jawab (mk .jumlaFiliyya .damir .la .la) = maqbulJ [.bila] ∧
    jawab (mk .jumlaFiliyya .laRabit .la .la) = khataJ := by
  decide +kernel

/-- **الجامدُ فارغ** في `SLGE.Simat.annOK2` («هندٌ أسدٌ» بلا مطابقة)، وهنا الجامدُ الفارغُ مقبول، وذو الضمير خطأ. -/
theorem simat2_jamid :
    SLGE.Simat.annOK2 (0, 0, [(0, 0, 0), (1, 0, 0)]) [SLGE.Simat.noun 1 1 0, SLGE.Simat.noun 0 0 0]
      [SLGE.Simat.e0, (0, true, 0, 0)] = true ∧
    jawab (mk .mufradJamid .la .laShay .la) = maqbulJ [.bila] ∧
    jawab (mk .mufradJamid .la .mustakin .la) = khataJ := by
  decide +kernel

/-- **شواهدُ النطاق** (مدخلاتٌ مبنيّة على أمثلته). -/
theorem shawahid :
    -- «والليلة والهلال متأول» وإن يفد فأخبرا: الدرجتان
    jawab (mk .zarfZaman .la .la .la) = maqbulJ [.bitawil, .bila] ∧
    -- «أقاطن قوم سلمى»: وصفٌ مفردٌ معتمدٌ على استفهام ومرفوعُه جمع، فاعلٌ أغنى
    jawab ⟨.wasfMarfu, .la, .la, .la, .la, .la, .la, .istifham, .mufrad, .jam, .failAghna⟩ = maqbulJ [.bila] ∧
    -- «ما مضروب العمران»: على نفي، ومرفوعُه مثنًّى
    jawab ⟨.wasfMarfu, .la, .la, .la, .la, .la, .la, .nafy, .mufrad, .muthanna, .failAghna⟩ = maqbulJ [.bila] ∧
    -- المطابقةُ في المثنّى: الخبرُ المقدَّم
    jawab ⟨.wasfMarfu, .la, .la, .la, .la, .la, .la, .istifham, .muthanna, .muthanna, .khabarMuqaddam⟩ = maqbulJ [.bila] ∧
    -- «أقائم زيد» خبرًا مقدَّمًا: ليس في غير الإفراد
    jawab ⟨.wasfMarfu, .la, .la, .la, .la, .la, .la, .istifham, .mufrad, .mufrad, .khabarMuqaddam⟩ = khataJ ∧
    -- «وأبرزنه»: المشتقُّ لغيره بضميرٍ بارز
    jawab (mk .mufradMushtaq .la .bariz .lighayrihi) = maqbulJ [.bila] ∧
    jawab (mk .mufradMushtaq .la .mustakin .lighayrihi) = khataJ ∧
    -- «قل هو الله أحد»: الجملةُ هي المبتدأ
    jawab (mk .jumlaIsmiyya .hiya .la .la) = maqbulJ [.bila] ∧
    -- الوصفُ المثنّى ومرفوعُه مفردٌ بلا اعتماد: القطرُ ساكتٌ (وصفُه مفرد)، والألفيةُ تقبله قليلًا (س179)
    jawab ⟨.wasfMarfu, .la, .la, .la, .la, .la, .la, .laItimad, .muthanna, .mufrad, .failAghna⟩ = maqbulJ [.qalil] ∧
    -- حقولٌ غيرُ متّسقة: الإفادةُ في غير الزمان
    jawab ⟨.mubtadaKhabar, .dhat, .zarfMakan, .la, .la, .la, .mufid, .la, .la, .la, .la⟩ = laHukmJ := by
  decide

end Khabar
end Jisr
