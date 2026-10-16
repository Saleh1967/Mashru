/-
  Jisr/JisrDal.lean — الجسرُ إلى الدالّ: الإعرابُ بالحروف والتقديرُ وجرُّ الممنوع من الصرف بالفتحة وصيغةُ المجهول، على خلايا الكلمة وأطر المالك
  (`SLGE/Bridge.lean`: الحالةُ تحمل الإعراب، والعلاماتُ الفرعيّة حواملُها من حروف الزيادة؛ `SLGE/Wad.lean`: الإعراباتُ الأربعة؛ `SLGE/Hamza.lean`:
  صورةُ الابتداء بهمزة الوصل؛ `Dal/Khaliya.lean`: الخليةُ حاملٌ وحالة دون 116؛ `Jisr/Utur.lean`: قارئُ الحالة `halaIrab`).
  قرارُ المالك (2026-10-17، 00:09): «يجب عمل lean الجسر للدال … عمل الجسر lean وslge وبعدها ننتقل للإنشاء».

  **المرجع** (قطر الندى، مودَع مختوم، بأسطره — «/» موضعُ انقطاع السطر في المودَع):
  L75–78 «فصل: أنواع الإعراب أربعة … فيرفع بضمة، وينصب بفتحة، / ويجر بكسرة، ويجزم بحذف حركة، إلا الأسماء الستة»؛
  L78–79 «وهي أبوه وأخوه وحموها / وهنوه وفوه وذو مال، فترفع بالواو وتنصب بالألف وتجر بالياء»؛ L79–80 «والأفصح / استعمال هن كغد»؛
  L82–83 «والمثنى كالزيدان فيرفع بالألف، وجمع المذكر السالم كالزيدون فيرفع / بالواو، ويجران وينصبان بالياء»؛ L83–85 الملحقاتُ (كلا وكلتا مع الضمير،
  اثنان واثنتان، أولو وعشرون وأخواته، عالمون، أهلون، وابلون، أرضون، سنون وبابه، بنون، عليون)؛
  L86–88 «وأولات وما جمع بألف وتاء مزيدتين وما سمي به منهما فينصب بالكسرة، نحو / خلق السموات، واصطفى البنات وما لا ينصرف فيجر بالفتحة نحو
  "بأفضل منه"، / إلا مع أل نحو "بالأفضل" أو بالإضافة نحو "بأفضلكم"»؛ L88–90 «والأمثلة الخمسة، وهي / تفعلان وتفعلون بالياء والتاء فيهما،
  وتفعلين، فترفع بثبوت النون، وتجزم / وتنصب بحذفها، نحو "فإن لم تفعلوا ولن تفعلوا"»؛ L90–91 «والفعل المضارع المعتل / الآخر فيجزم بحذف آخره،
  نحو "لم يغز ولم يخش ولم يرم"»؛ L92–95 «فصل: تقدر جميع الحركات في نحو "غلامي والفتى" ويسمى مقصورا، والضمة / والكسرة في نحو "القاضي" ويسمى
  منقوصا، والضمة والفتحة في نحو "يخشى"، / والضمة في نحو "يدعو ويقضي". وتظهر الفتحة في نحو "إن القاضي لن يقضي ولن / يدعو"»؛ المجهول L242–244
  «ويضم أول الفعل مطلقا، ويشاركه ثاني نحو / تعلم، وثالث نحو انطلق. ويفتح ما قبل الآخر في المضارع، ويكسر في الماضي، / ولك في نحو قال وباع
  الكسر مخلصا ومشما ضما والضم مخلصا»؛ موانعُ الصرف L420–421 (بالاسم عند المالك `Wad.mawani9`). وشواهدُ من أبوابٍ أخرى بأسطرها: L130 «كنية
  ك"أبي عمرو"»، L204 «"لا مسلمات"، وعلى الياء في نحو "لا رجلين" و "لا مسلمين"»، L226 «"قام الزيدون" و "قامت الهندات"»، L285 «"يالله للمسلمين"»، L385 «أخاك أخاك إن من لا أخا له».

  **الصورة.** الخليةُ `4·حرف + حالة` (فتحة 0، ضمّة 1، كسرة 2، سكون 3)؛ `harf`/`hala` هما فكُّ المالك `Dal.fakk` بعينه (`harf_fakk`)، والحواملُ
  مواضعُها في جدول المخارج `Dal.hawamil` (ا 2، ي 11، ن 14، و 28: `hawamil_huruf`). (١) **البابُ معلَن** `Bab`: المفردُ المنصرف، والفعلُ الصحيح،
  والمقصور، والمنقوص، والمضافُ إلى الياء، والأسماءُ الستّة، والمثنّى، وجمعُ المذكر السالم، وجمعُ المؤنث السالم، والممنوعُ من الصرف (مجرّدًا أو مع أل
  والإضافة)، والأمثلةُ الخمسة، والمضارعُ المعتلّ الآخر — فالدالُّ لا يقرّر بابَ الكلمة (أهي مثنًّى أم اسمٌ آخرُه ألفٌ ونون؟): البابُ من المعجم،
  والجسرُ يقرأ الإعرابَ من الخلايا **بعد** إعلان الباب (كما أنّ الدالَّ وحده لا يقرّر المدلول: `Bridge.dal_undetermines`)؛ والملحقاتُ بالمثنّى
  والجمع (L83–85) وأولات (L86) وهن (L79–80) تدخل بإعلان بابها من المعجم لا بشاهدٍ هنا. (٢) **الحكمُ من الدالّ** `HukmDal` ثلاثيّ: معيَّنٌ، أو
  محتمَلٌ بين أكثر من إعرابٍ (الدالُّ لا يفرّق: ياءُ المثنّى والجمع نصبًا وجرًّا، فتحةُ الممنوع نصبًا وجرًّا، تقديرُ المقصور)، أو لا حكم (خليةٌ لا
  يقبلها الباب: حرفُ المدّ غيرُ ساكنٍ في المثنّى والجمع والستّة والمقصور، ومضارعٌ معتلٌّ آخرُه واوٌ مضمومة …). `hukm` يقرأ الخليةَ الأخيرة (وقبلَها في
  المثنّى والجمع). (٣) **الأصليةُ** تقابلُ المالك بعينه (`Bridge.irabState`: `asliyya_tuqabil`)، وتوافق قارئَ الطبقة الثالثة `Utur.halaIrab` في
  المفرد غير المنوَّن (`mufrad_halaIrab`؛ والتنوينُ لا يقرؤه الجسر: `mufrad_tanwin`)؛ **والفرعيةُ**: صفوفُ جدول المالك `Bridge.farIya` العشرة
  بأبوابنا (`farIyaBab_malik`)، ولكلّ صفٍّ القاعدةُ على كلّ كلمة (`farIya_kull`) وشاهدٌ يحمله (`muwafiq_farIya`)، وحواملُها من حروف الزيادة
  (`sitta_hamil`؛ وعند المالك `Bridge.fariya_augs`). (٤) **التقدير**: المقصورُ والمضافُ إلى الياء لا يعيّنان شيئًا (`maqsur_la_yuayyin`،
  `mudaf_la_yuayyin`)، والمنقوصُ تظهر فتحتُه وحدَها (`manqus_fatha_zahira`). (٥) **الممنوع**: فتحتُه نصبٌ أو جرٌّ ولا كسرةَ له، ومع أل أو الإضافة
  يُجرّ بالكسرة (`mamnu_fatha`، `mamnu_bi_al`). (٦) **الأمثلةُ الخمسة**: بالنون رفعٌ وبحذفها نصبٌ أو جزم (`amthila_nun`). (٧) **المجهول** `majhul`:
  ضمُّ الأوّل (ومعه الثاني في نحو تعلّم، والثالث في نحو انطلق — بالصيغة المعلَنة `Siga`)، وفتحُ ما قبل الآخر في المضارع وكسرُه في الماضي؛ يحفظ
  الحروفَ والطولَ والخلايا دون 116 (`majhul_huruf`، `majhul_tul`، `majhul_dun_116`)، ويُرفض باسمه ما قصُر عن موضع المشارِك بثلاثٍ أو فيه حرفُ مدٍّ
  ساكن — الأجوفُ والناقص (قال وباع: ثلاثةُ أوجهٍ L244 لم تُبنَ) — (`majhul_marfud`)؛ وعلى صورة الابتداء عند المالك (`Law.ibtidaForm`): مجهولُ
  «انطلق» هو صورةُ ابتداء مجهوله، فضمُّ الثالث يضمّ همزةَ الوصل بقاعدته `waslHaraka` (`intilaq_wasl`)؛ وهو نظيرُ `Shabaka.jahhil` على الأدوار.
  (٨) **الشواهد** مبنيّةً خلايا (24: 23 بلفظ القطر بأسطرها، ومثالٌ مبنيّ واحد «بالزيدين» مثنًّى مجرورًا — لم أجد جرَّ مثنًّى بلفظه في المودَع كلِّه؛
  الأقربُ «لا رجلين» L204 نصبًا و«اثنين واثنتين» L450 صورةً في باب همزة الوصل): ذو، أخاك، أبي، الزيدان، رجلين، الزيدون، مسلمين، للمسلمين، الهندات،
  مسلمات، بأفضل، بالأفضل، تفعلان، تفعلوا (نصبًا وجزمًا)، يغز، يخش، يرم، يخشى، يدعو (رفعًا ونصبًا)، القاضي (رفعًا ونصبًا)؛ والمجهول: ضَرَبَ→ضُرِبَ، يَضْرِبُ→يُضْرَبُ، تَعَلَّمَ→تُعُلِّمَ، اِنْطَلَقَ→اُنْطُلِقَ.

  **المبرهنات (لكلّ، 3؛ استقراءٌ على القائمة):** `majhul_huruf`، `majhul_tul`، `majhul_dun_116`. **تعريفيّة (13؛ فكُّ التعريفات على الخلية
  الأخيرة بالقواعد المساعدة `harf_kh`/`hala_kh`/`akhir_append`، وبالتقسيم على الحالة):** `harf_fakk`، `asliyya_tuqabil`، `maqsur_la_yuayyin`،
  `mudaf_la_yuayyin`، `yayn_la_yufarriq`، `manqus_fatha_zahira`، `mamnu_fatha`، `mamnu_bi_al`، `amthila_nun`، `farIya_kull`، `mufrad_halaIrab`،
  `mufrad_tanwin`، `majhul_marfud`. **على الشاهد (7؛ `decide`):** `hawamil_huruf` (على `Dal.hawamil`)، `sitta_hamil` (على `Law.augs`)،
  `farIyaBab_malik` (على `Bridge.farIya`)، `muwafiq_farIya` (لكلّ صفٍّ من العشرة شاهدٌ يحمله)، `shawahid_hukm`، `shawahid_majhul`، `intilaq_wasl`
  (على `Law.ibtidaForm`). (23 في `Audit.lean`؛ والقواعدُ المساعدة `badilInda_*`/`musharik_*` داخليّة.) الإعرابُ المخرَج `SLGE.Wad.Irab` (إعراباتُ
  المالك الأربعة) لا `Jisr.Awamil.Irab` (إعرابُ جدول العوامل؛ الجسرُ بينهما لم يُبنَ).

  الوسم: مبرهن (لكلّ) / تعريفيّة / على الشاهد كما سُمّي. تعييناتُ البنّاء (تُعرض على المالك): البابُ معلَنٌ من المعجم لا من الدالّ (ومن أعلن الصحيحَ
  معتلًّا فجزمُه المقروء على عهدته)؛ حرفُ المدّ ساكنٌ في الحوامل، وحركةُ النون في المثنّى والجمع والأمثلة لا تُقرأ، وحركةُ ياء المضاف إليها لا تُقرأ؛
  الأسماءُ الستّة تُقرأ قبل المضاف إليه (ضميرًا أو اسمًا: أبوه، ذو مال) وقطعُه قرارُ القارئ؛ الخلايا بالرسم (همزةُ الوصل حاملًا 0 بحركتها، واللامُ
  الشمسية لامًا ساكنة) ولا يقرأ الجسرُ إلّا الخليةَ الأخيرة وقبلَها؛ المنقوصُ المنوَّن (قاضٍ) والتنوينُ عامّةً في القارئ؛ موانعُ الصرف التسعة نفسُها
  من المعجم (`Wad.mawani9` بالاسم)؛ المضارعُ المعتلّ: الجزمُ بحذف حرف العلّة يُقرأ من غياب حرف المدّ آخرًا؛ صيغُ المجهول الثلاث (بسيط/تفعّل/انفعل)
  على مثالَي القطر، وموضعُ المشارِك بثلاثٍ أقلَّ طولٍ، ورفضُ المعتلّ؛ والمجهولُ على صورة الابتداء (همزةُ الوصل خليةً). الجدولُ `jisr_dal.tsv` مسجَّلٌ
  «مرشّحًا» حتّى يأذن المالك بختمه؛ ومطابقتُه `tahaqquq/test_jisrdal.py`.
-/
import SLGE.Bridge
import SLGE.Hamza
import Dal.Makharij
import Jisr.Utur

set_option autoImplicit false

namespace Jisr
namespace JisrDal
open SLGE SLGE.Wad

/-! ## ١. الخلية والباب والحكم -/

/-- حرفُ الخلية (رقمُ حامله في جدول المخارج) وحالتُها (فتحة 0، ضمّة 1، كسرة 2، سكون 3). -/
def harf (c : Nat) : Nat := c / 4
def hala (c : Nat) : Nat := c % 4

/-- خليةٌ من حرفٍ وحالة. -/
def kh (h s : Nat) : Nat := 4 * h + s

theorem harf_kh (h s : Nat) (hs : s < 4) : harf (kh h s) = h := by unfold harf kh; omega
theorem hala_kh (h s : Nat) (hs : s < 4) : hala (kh h s) = s := by unfold hala kh; omega

/-- **الحرفُ والحالةُ هما فكُّ المالك** `Dal.fakk` بعينه (الخلية `Dal.Khaliya`: حاملٌ وحالة، `n = 4·حامل + حالة`) — تعريفيّة. -/
theorem harf_fakk (m : Fin 116) : (Dal.fakk m).hamil.val = harf m.val ∧ (Dal.fakk m).hala.val = hala m.val := ⟨rfl, rfl⟩

/-- الحروفُ الحوامل في الإعراب بالحروف (بترتيب `Dal.hawamil`): ا 2، ي 11، ن 14، و 28. -/
def alif : Nat := 2
def ya : Nat := 11
def nun : Nat := 14
def waw : Nat := 28

/-- **الحواملُ الأربعة مواضعُها في جدول المخارج المعلَن** `Dal.hawamil` — على الشاهد. -/
theorem hawamil_huruf :
    Dal.hawamil[alif]? = some 'ا' ∧ Dal.hawamil[ya]? = some 'ي' ∧ Dal.hawamil[nun]? = some 'ن' ∧ Dal.hawamil[waw]? = some 'و' := by
  decide

/-- حرفُ مدٍّ ساكن: ألفٌ أو واوٌ أو ياءٌ بالسكون. -/
def maddSakin (c : Nat) : Bool := (harf c == alif || harf c == waw || harf c == ya) && hala c == 3

/-- الصيغةُ الصرفيّة للمجهول (القطر L242–243): بسيطٌ (ضمُّ الأوّل)، وما شاركه ثانيه (تعلّم)، وما شاركه ثالثه (انطلق). -/
inductive Siga | basit | thani | thalith
deriving DecidableEq, Repr

/-- أبوابُ الإعراب على الدالّ — تُعلَن من المعجم لا من الدالّ. -/
inductive Bab
  | mufrad                 -- المفرد المنصرف: بالحركات (L77–78)؛ وجمع التكسير مثله (قراءة البنّاء: القطر لا يسمّيه هنا، «كسير» 0 في المودَع)
  | filSahih               -- الفعل المضارع الصحيح الآخر: ضمّة/فتحة/سكون (L76–78)
  | maqsur                 -- تُقدَّر جميع الحركات (L92)
  | manqus                 -- تُقدَّر الضمّة والكسرة وتظهر الفتحة (L93–94)
  | mudafLiYa              -- المضاف إلى ياء المتكلّم (L92)
  | sitta                  -- الأسماء الستّة: بالواو والألف والياء (L78–79)
  | muthanna               -- بالألف رفعًا وبالياء نصبًا وجرًّا (L82–83)
  | jamMudhakkar           -- بالواو رفعًا وبالياء نصبًا وجرًّا (L82–83)
  | jamMuannath            -- يُنصب بالكسرة (L86–87)
  | mamnu (alAwIdafa : Bool) -- ما لا ينصرف: يُجرّ بالفتحة إلّا مع أل أو الإضافة (L87–88)
  | amthila                -- الأمثلة الخمسة: بثبوت النون وحذفها (L88–90)
  | mudariMutall           -- المضارع المعتلّ الآخر: جزمه بالحذف وتقديره (L90–91، L93–95)
deriving DecidableEq, Repr

/-- حكمُ الإعراب من الدالّ: معيَّن، أو محتمَلٌ بين أكثر من إعراب (الدالّ لا يفرّق)، أو لا حكم. -/
inductive HukmDal
  | muayyan (i : Irab)
  | muhtamal (l : List Irab)
  | laHukm
deriving DecidableEq, Repr

/-- الخليةُ الأخيرة وما قبلها. -/
def akhir (l : List Nat) : Option Nat := l.getLast?
def qablAkhir (l : List Nat) : Option Nat := l.dropLast.getLast?

theorem akhir_append (l : List Nat) (c : Nat) : akhir (l ++ [c]) = some c := by simp [akhir]
theorem akhir_append2 (l : List Nat) (d c : Nat) : akhir (l ++ [d, c]) = some c := by simp [akhir]
theorem qablAkhir_append (l : List Nat) (d c : Nat) : qablAkhir (l ++ [d, c]) = some d := by
  simp [qablAkhir, List.dropLast_append_of_ne_nil]

/-- **الجسر:** حكمُ الإعراب من الباب المعلَن وخلايا الكلمة؛ حرفُ المدّ الحاملُ ساكنٌ، وحركةُ النون لا تُقرأ. -/
def hukm (b : Bab) (l : List Nat) : HukmDal :=
  match akhir l with
  | none => .laHukm
  | some c =>
    match b with
    | .mufrad => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 2 => .muayyan .jarr | _ => .laHukm
    | .filSahih => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 3 => .muayyan .jazm | _ => .laHukm
    | .maqsur => if harf c == alif && hala c == 3 then .muhtamal [.raf, .nasb, .jarr] else .laHukm
    | .mudafLiYa => if harf c == ya then .muhtamal [.raf, .nasb, .jarr] else .laHukm
    | .manqus => if harf c == ya then (match hala c with | 0 => .muayyan .nasb | 3 => .muhtamal [.raf, .jarr] | _ => .laHukm)
                 else .laHukm
    | .sitta => if hala c != 3 then .laHukm
                else if harf c == waw then .muayyan .raf else if harf c == alif then .muayyan .nasb
                else if harf c == ya then .muayyan .jarr else .laHukm
    | .muthanna => if harf c == nun then
          (match qablAkhir l with
           | some d => if hala d != 3 then .laHukm
                       else if harf d == alif then .muayyan .raf else if harf d == ya then .muhtamal [.nasb, .jarr] else .laHukm
           | none => .laHukm)
        else .laHukm
    | .jamMudhakkar => if harf c == nun then
          (match qablAkhir l with
           | some d => if hala d != 3 then .laHukm
                       else if harf d == waw then .muayyan .raf else if harf d == ya then .muhtamal [.nasb, .jarr] else .laHukm
           | none => .laHukm)
        else .laHukm
    | .jamMuannath => match hala c with
      | 1 => .muayyan .raf | 2 => .muhtamal [.nasb, .jarr] | _ => .laHukm
    | .mamnu false => match hala c with
      | 1 => .muayyan .raf | 0 => .muhtamal [.nasb, .jarr] | _ => .laHukm
    | .mamnu true => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 2 => .muayyan .jarr | _ => .laHukm
    | .amthila => if harf c == nun then .muayyan .raf else if maddSakin c then .muhtamal [.nasb, .jazm] else .laHukm
    | .mudariMutall => if harf c == alif then (if hala c == 3 then .muhtamal [.raf, .nasb] else .laHukm)
                       else if harf c == waw || harf c == ya then
                         (match hala c with | 0 => .muayyan .nasb | 3 => .muayyan .raf | _ => .laHukm)
                       else .muayyan .jazm

/-- هل يحتمل الحكمُ هذا الإعراب؟ -/
def yahtamil : HukmDal → Irab → Bool
  | .muayyan i, j => i == j
  | .muhtamal l, j => l.contains j
  | .laHukm, _ => false

/-! ## ٢. الأصلية تقابلُ المالك، والفرعية توافق جدولَه -/

/-- **العلاماتُ الأصلية هي تقابلُ المالك بعينه**: المفردُ المنصرف آخرُه حالةُ الإعراب (`Bridge.irabState`) للرفع والنصب والجرّ، والفعلُ
الصحيح للرفع والنصب والجزم — لكلّ كلمةٍ وحرفٍ أخير (في هذا الاتّجاه: من حالة المالك إلى الحكم). -/
theorem asliyya_tuqabil (l : List Nat) (h : Nat) :
    (∀ i : Irab, i ≠ .jazm → hukm .mufrad (l ++ [kh h (Bridge.irabState i)]) = .muayyan i) ∧
    (∀ i : Irab, i ≠ .jarr → hukm .filSahih (l ++ [kh h (Bridge.irabState i)]) = .muayyan i) := by
  refine ⟨fun i hi => ?_, fun i hi => ?_⟩ <;> cases i <;>
    simp [hukm, akhir_append, hala_kh, Bridge.irabState] at *

/-- **الجسرُ يوافق قارئَ الطبقة الثالثة**: في المفرد المنصرف غير المنوَّن الحكمُ معيَّنٌ بإعرابٍ حالتُه عند المالك (`Bridge.irabState`) هي ما يقرؤه
`Utur.halaIrab` آخرَ الكلمة — لكلّ كلمةٍ وخليةٍ أخيرةٍ متحرّكة وإعراب. -/
theorem mufrad_halaIrab (l : List Nat) (c : Nat) (hc : hala c < 3) (i : Irab) :
    hukm .mufrad (l ++ [c]) = .muayyan i ↔ Bridge.irabState i = Utur.halaIrab true (l ++ [c]) := by
  have h59 : c ≠ 59 := by unfold hala at hc; omega
  have hh : Utur.halaIrab true (l ++ [c]) = c % 4 := by
    unfold Utur.halaIrab
    split
    · rename_i a rest heq; simp at heq; omega
    · rename_i a rest heq; simp at heq; omega
    · rename_i heq; simp at heq
  rw [hh]
  have h3 : c % 4 = 0 ∨ c % 4 = 1 ∨ c % 4 = 2 := by unfold hala at hc; omega
  rcases h3 with h | h | h <;> simp [hukm, akhir_append, hala, h] <;> cases i <;> simp [Bridge.irabState]

/-- **التنوينُ لا يقرؤه الجسر** (نونٌ ساكنة 59 آخرًا: في القارئ) — تعريفيّة. -/
theorem mufrad_tanwin (l : List Nat) (c : Nat) : hukm .mufrad (l ++ [c, 59]) = .laHukm := by
  simp [hukm, akhir_append2, hala]

/-- **المقصورُ لا يعيّن شيئًا** — الحركاتُ كلُّها مقدَّرة (L92): لكلّ كلمةٍ وخليةٍ أخيرة. -/
theorem maqsur_la_yuayyin (l : List Nat) (c : Nat) : ∀ i, hukm .maqsur (l ++ [c]) ≠ .muayyan i := by
  intro i; simp only [hukm, akhir_append]; split <;> simp

/-- **المضافُ إلى الياء لا يعيّن شيئًا** (L92). -/
theorem mudaf_la_yuayyin (l : List Nat) (c : Nat) : ∀ i, hukm .mudafLiYa (l ++ [c]) ≠ .muayyan i := by
  intro i; simp only [hukm, akhir_append]; split <;> simp

/-- **ياءُ المثنّى والجمع لا تفرّق النصبَ من الجرّ** — لكلّ كلمةٍ آخرُها ياءٌ ساكنةٌ فنون: محتمَلٌ بينهما (L83). -/
theorem yayn_la_yufarriq (l : List Nat) (sn : Nat) (hsn : sn < 4) :
    hukm .muthanna (l ++ [kh ya 3, kh nun sn]) = .muhtamal [.nasb, .jarr] ∧
    hukm .jamMudhakkar (l ++ [kh ya 3, kh nun sn]) = .muhtamal [.nasb, .jarr] := by
  constructor <;> simp [hukm, akhir_append2, qablAkhir_append, harf_kh, hala_kh, hsn, ya, nun, waw, alif]

/-- **المنقوصُ تظهر فتحتُه وحدَها** (L93–94): ياءٌ مفتوحةٌ نصبٌ، وساكنةٌ الرفعُ والجرُّ مقدَّران، وغيرُهما لا حكم — تعريفيّة. -/
theorem manqus_fatha_zahira (l : List Nat) (s : Nat) (hs : s < 4) :
    hukm .manqus (l ++ [kh ya s]) = (if s = 0 then .muayyan .nasb else if s = 3 then .muhtamal [.raf, .jarr] else .laHukm) := by
  have h4 : s = 0 ∨ s = 1 ∨ s = 2 ∨ s = 3 := by omega
  rcases h4 with rfl | rfl | rfl | rfl <;> simp [hukm, akhir_append, harf_kh, hala_kh, ya]

/-- **الممنوعُ من الصرف**: فتحتُه نصبٌ أو جرّ (الدالّ لا يفرّق)، ولا كسرةَ له (L87–88) — تعريفيّة. -/
theorem mamnu_fatha (l : List Nat) (h : Nat) :
    hukm (.mamnu false) (l ++ [kh h 0]) = .muhtamal [.nasb, .jarr] ∧ hukm (.mamnu false) (l ++ [kh h 2]) = .laHukm := by
  constructor <;> simp [hukm, akhir_append, hala_kh]

/-- **ومع أل أو الإضافة يُجرّ بالكسرة** كالمنصرف (L88) — تعريفيّة. -/
theorem mamnu_bi_al (l : List Nat) (h : Nat) : hukm (.mamnu true) (l ++ [kh h 2]) = .muayyan .jarr := by
  simp [hukm, akhir_append, hala_kh]

/-- **الأمثلةُ الخمسة**: بثبوت النون رفعٌ، وبحذفها (فيبقى حرفُ المدّ ساكنًا) نصبٌ أو جزم (L89–90) — تعريفيّة. -/
theorem amthila_nun (l : List Nat) (sn h : Nat) (hsn : sn < 4) (hh : h = alif ∨ h = waw ∨ h = ya) :
    hukm .amthila (l ++ [kh nun sn]) = .muayyan .raf ∧ hukm .amthila (l ++ [kh h 3]) = .muhtamal [.nasb, .jazm] := by
  constructor
  · simp [hukm, akhir_append, harf_kh nun sn hsn]
  · rcases hh with rfl | rfl | rfl <;> simp [hukm, akhir_append, maddSakin, harf_kh, hala_kh, alif, waw, ya, nun]

/-- **حواملُ الأسماء الستّة** من حروف الزيادة — على الشاهد (جدولُ المالك `Law.augs`؛ وعنده `Bridge.fariya_augs`). -/
theorem sitta_hamil : [waw, alif, ya].all (fun c => Law.augs.contains c) = true := by decide

/-- صفوفُ جدول المالك `Bridge.farIya` بأبوابنا: (الباب، الإعراب، حاملُ العلامة). -/
def farIyaBab : List (Bab × Irab × Nat) :=
  [(.sitta, .raf, waw), (.sitta, .nasb, alif), (.sitta, .jarr, ya),
   (.muthanna, .raf, alif), (.muthanna, .nasb, ya), (.muthanna, .jarr, ya),
   (.jamMudhakkar, .raf, waw), (.jamMudhakkar, .nasb, ya), (.jamMudhakkar, .jarr, ya),
   (.amthila, .raf, nun)]

/-- اسمُ الباب عند المالك في `Bridge.farIya`. -/
def ismBab : Bab → String
  | .sitta => "الأسماء الستة" | .muthanna => "المثنى" | .jamMudhakkar => "جمع المذكر" | .amthila => "الأمثلة الخمسة" | _ => ""

/-- **صفوفُنا هي صفوفُ المالك صفًّا صفًّا** (`Bridge.farIya` بأسمائه) — على الشاهد. -/
theorem farIyaBab_malik : farIyaBab.map (fun x => (ismBab x.1, x.2)) = Bridge.farIya := by decide

/-- لاحقةُ العلامة الفرعية في بابها: حرفُ المدّ ساكنًا آخرًا (الستّة)، أو ساكنًا فالنونُ بحالتها (المثنّى والجمع)، أو النونُ بحالتها (الأمثلة). -/
def lahiqa : Bab → Nat → Nat → List Nat
  | .muthanna, h, sn => [kh h 3, kh nun sn]
  | .jamMudhakkar, h, sn => [kh h 3, kh nun sn]
  | .amthila, h, sn => [kh h sn]
  | _, h, _ => [kh h 3]

/-- **الفرعيةُ على كلّ كلمة**: لكلّ صفٍّ من صفوف جدول المالك العشرة، كلُّ كلمةٍ تنتهي بلاحقة ذلك الحامل في ذلك الباب يحتمل حكمُها ذلك الإعراب
(والمعيَّنُ منها ما لا تشترك فيه الياء) — تعريفيّة لكلّ كلمةٍ وحركةِ نون. -/
theorem farIya_kull (l : List Nat) (sn : Nat) (hsn : sn < 4) :
    farIyaBab.all (fun x => yahtamil (hukm x.1 (l ++ lahiqa x.1 x.2.2 sn)) x.2.1) = true := by
  simp [farIyaBab, lahiqa, hukm, yahtamil, akhir_append, akhir_append2, qablAkhir_append, harf_kh, hala_kh, hsn, waw, alif, ya, nun]

/-! ## ٣. الشواهد: توافقُ جدول المالك `Bridge.farIya` -/

/-- شاهدٌ خلايا: لفظُه، وسطرُ القطر الذي فيه لفظُه (0: مثالٌ مبنيّ)، وبابُه المعلَن، وخلاياه، وإعرابُه المشهود. -/
structure Shahid where
  lafz : String
  satr : Nat
  bab : Bab
  khalaya : List Nat
  irab : Irab
deriving DecidableEq, Repr

/-- الشواهدُ (24): الأسماءُ الستّة قبل المضاف إليه (الحاملُ آخرُها)، والخلايا بالرسم. ء 0، ه 1، ع 3، غ 5، خ 6، ق 7، ج 9، ش 10، ض 12، ل 13، ر 15،
ط 16، د 17، ت 18، ز 19، س 20، ذ 23، ف 25، ب 26، م 27. -/
def shawahid : List Shahid :=
  [⟨"ذو", 79, .sitta, [kh 23 1, kh waw 3], .raf⟩,
   ⟨"أخاك", 385, .sitta, [kh 0 0, kh 6 0, kh alif 3], .nasb⟩,
   ⟨"أبي", 130, .sitta, [kh 0 0, kh 26 2, kh ya 3], .jarr⟩,
   ⟨"الزيدان", 82, .muthanna, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 0, kh alif 3, kh nun 2], .raf⟩,
   ⟨"رجلين", 204, .muthanna, [kh 15 0, kh 9 1, kh 13 0, kh ya 3, kh nun 2], .nasb⟩,
   ⟨"بالزيدين", 0, .muthanna, [kh 26 2, kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 0, kh ya 3, kh nun 2], .jarr⟩,
   ⟨"الزيدون", 82, .jamMudhakkar, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 1, kh waw 3, kh nun 0], .raf⟩,
   ⟨"مسلمين", 204, .jamMudhakkar, [kh 27 1, kh 20 3, kh 13 2, kh 27 2, kh ya 3, kh nun 0], .nasb⟩,
   ⟨"للمسلمين", 285, .jamMudhakkar, [kh 13 2, kh 13 3, kh 27 1, kh 20 3, kh 13 2, kh 27 2, kh ya 3, kh nun 0], .jarr⟩,
   ⟨"الهندات", 226, .jamMuannath, [kh 0 0, kh 13 3, kh 1 2, kh nun 3, kh 17 0, kh alif 3, kh 18 1], .raf⟩,
   ⟨"مسلمات", 204, .jamMuannath, [kh 27 1, kh 20 3, kh 13 2, kh 27 0, kh alif 3, kh 18 2], .nasb⟩,
   ⟨"بأفضل", 87, .mamnu false, [kh 26 2, kh 0 0, kh 25 3, kh 12 0, kh 13 0], .jarr⟩,
   ⟨"بالأفضل", 88, .mamnu true, [kh 26 2, kh 0 0, kh 13 3, kh 0 0, kh 25 3, kh 12 0, kh 13 2], .jarr⟩,
   ⟨"تفعلان", 89, .amthila, [kh 18 0, kh 25 3, kh 3 0, kh 13 0, kh alif 3, kh nun 2], .raf⟩,
   ⟨"تفعلوا", 90, .amthila, [kh 18 0, kh 25 3, kh 3 0, kh 13 1, kh waw 3, kh alif 3], .nasb⟩,
   ⟨"تفعلوا", 90, .amthila, [kh 18 0, kh 25 3, kh 3 0, kh 13 1, kh waw 3, kh alif 3], .jazm⟩,
   ⟨"يغز", 91, .mudariMutall, [kh ya 0, kh 5 3, kh 19 1], .jazm⟩,
   ⟨"يخش", 91, .mudariMutall, [kh ya 0, kh 6 3, kh 10 0], .jazm⟩,
   ⟨"يرم", 91, .mudariMutall, [kh ya 0, kh 15 3, kh 27 2], .jazm⟩,
   ⟨"يخشى", 93, .mudariMutall, [kh ya 0, kh 6 3, kh 10 0, kh alif 3], .raf⟩,
   ⟨"يدعو", 94, .mudariMutall, [kh ya 0, kh 17 3, kh 3 1, kh waw 3], .raf⟩,
   ⟨"يدعو", 95, .mudariMutall, [kh ya 0, kh 17 3, kh 3 1, kh waw 0], .nasb⟩,
   ⟨"القاضي", 93, .manqus, [kh 0 0, kh 13 3, kh 7 0, kh alif 3, kh 12 2, kh ya 3], .raf⟩,
   ⟨"القاضي", 94, .manqus, [kh 0 0, kh 13 3, kh 7 0, kh alif 3, kh 12 2, kh ya 0], .nasb⟩]

/-- **الشواهدُ الأربعة والعشرون**: كلُّ شاهدٍ يحتمل إعرابَه المشهود، والمعيَّنُ منها أربعةَ عشرَ والباقي محتمَل (الدالّ لا يفرّق)؛ وثلاثةٌ
وعشرون منها بلفظ القطر في سطره (يفحصه الاختبارُ على المودَع) ومثالٌ مبنيّ واحد. -/
theorem shawahid_hukm :
    shawahid.all (fun s => yahtamil (hukm s.bab s.khalaya) s.irab) = true ∧
    (shawahid.filter fun s => match hukm s.bab s.khalaya with | .muayyan _ => true | _ => false).length = 14 ∧
    (shawahid.filter fun s => s.satr != 0).length = 23 := by decide

/-- **لكلّ صفٍّ من صفوف جدول المالك شاهدٌ يحمله**: بذلك الباب، حاملُ علامته ذلك الحرفُ بعينه، وحكمُه من الدالّ يحتمل ذلك الإعراب — على الشاهد
(وجوديّةٌ على الصفوف العشرة؛ والقاعدةُ على كلّ كلمة في `farIya_kull`). -/
theorem muwafiq_farIya :
    farIyaBab.all (fun x => shawahid.any fun s =>
      s.bab == x.1 && s.irab == x.2.1 && yahtamil (hukm s.bab s.khalaya) x.2.1 &&
      (match s.bab with
       | .muthanna | .jamMudhakkar => qablAkhir s.khalaya |>.map harf
       | _ => akhir s.khalaya |>.map harf) == some x.2.2) = true := by decide

/-! ## ٤. صيغةُ المجهول على الخلايا -/

/-- تبديلُ حالة الخلية (الحالةُ بالباقي على 4 فلا تخرج الخليةُ عن حرفها). -/
def badilHala (c s : Nat) : Nat := 4 * harf c + s % 4

/-- تبديلُ حالة الخلية رقم `i` (من الصفر). -/
def badilInda : List Nat → Nat → Nat → List Nat
  | [], _, _ => []
  | c :: cs, 0, s => badilHala c s :: cs
  | c :: cs, i + 1, s => c :: badilInda cs i s

theorem badilHala_harf (c s : Nat) : harf (badilHala c s) = harf c := by
  unfold badilHala harf; omega

theorem badilHala_lt (c s : Nat) (hc : c < 116) : badilHala c s < 116 := by
  unfold badilHala harf; omega

theorem badilInda_harf (l : List Nat) (i s : Nat) : (badilInda l i s).map harf = l.map harf := by
  induction l generalizing i with
  | nil => rfl
  | cons c cs ih =>
    cases i with
    | zero => simp [badilInda, badilHala_harf]
    | succ i => simp [badilInda, ih]

theorem badilInda_tul (l : List Nat) (i s : Nat) : (badilInda l i s).length = l.length := by
  induction l generalizing i with
  | nil => rfl
  | cons c cs ih =>
    cases i with
    | zero => simp [badilInda]
    | succ i => simp [badilInda, ih]

theorem badilInda_lt (l : List Nat) (i s : Nat) (hl : ∀ c ∈ l, c < 116) : ∀ c ∈ badilInda l i s, c < 116 := by
  induction l generalizing i with
  | nil => intro c hc; simp [badilInda] at hc
  | cons a as ih =>
    intro c hc
    cases i with
    | zero =>
      simp only [badilInda, List.mem_cons] at hc
      rcases hc with rfl | hc
      · exact badilHala_lt a s (hl a (List.mem_cons_self))
      · exact hl c (List.mem_cons_of_mem a hc)
    | succ i =>
      simp only [badilInda, List.mem_cons] at hc
      rcases hc with rfl | hc
      · exact hl c (List.mem_cons_self)
      · exact ih i (fun d hd => hl d (List.mem_cons_of_mem a hd)) c hc

/-- موضعُ المشارِك في الضمّ (من الصفر): الأوّلُ وحده، أو الثاني، أو الثالث. -/
def mawdiMusharik : Siga → Nat
  | .basit => 0 | .thani => 1 | .thalith => 2

/-- مشاركةُ الثاني (تعلّم) أو الثالث (انطلق) في الضمّ. -/
def musharik : Siga → List Nat → List Nat
  | .basit, l => l
  | .thani, l => badilInda l 1 1
  | .thalith, l => badilInda l 2 1

theorem musharik_harf (g : Siga) (l : List Nat) : (musharik g l).map harf = l.map harf := by
  cases g <;> simp [musharik, badilInda_harf]

theorem musharik_tul (g : Siga) (l : List Nat) : (musharik g l).length = l.length := by
  cases g <;> simp [musharik, badilInda_tul]

theorem musharik_lt (g : Siga) (l : List Nat) (hl : ∀ c ∈ l, c < 116) : ∀ c ∈ musharik g l, c < 116 := by
  cases g with
  | basit => exact hl
  | thani => exact badilInda_lt l 1 1 hl
  | thalith => exact badilInda_lt l 2 1 hl

/-- **المجهول** (L242–244): ضمُّ الأوّل — ومعه الثاني في نحو تعلّم، والثالث في نحو انطلق — وكسرُ ما قبل الآخر في الماضي وفتحُه في المضارع،
على صورة الابتداء (همزةُ الوصل خليةً). يُرفض باسمه ما قصُر عن موضع المشارِك بثلاث خلايا، وما فيه حرفُ مدٍّ ساكن (الأجوفُ والناقص: قال وباع
ثلاثةُ أوجهٍ L244، ولم تُبنَ). -/
def majhul (madi : Bool) (g : Siga) (l : List Nat) : Option (List Nat) :=
  if l.length < mawdiMusharik g + 3 ∨ l.any maddSakin = true then none
  else some (badilInda (musharik g (badilInda l 0 1)) (l.length - 2) (if madi then 2 else 0))

/-- **المجهولُ يحفظ الحروف**: الحروفُ بعينها وإنّما تتبدّل الحركات — لكلّ كلمة. -/
theorem majhul_huruf (madi : Bool) (g : Siga) (l l' : List Nat) (h : majhul madi g l = some l') : l'.map harf = l.map harf := by
  unfold majhul at h
  split at h
  · exact absurd h (by simp)
  · simp only [Option.some.injEq] at h
    rw [← h, badilInda_harf, musharik_harf, badilInda_harf]

/-- **المجهولُ يحفظ الطول**. -/
theorem majhul_tul (madi : Bool) (g : Siga) (l l' : List Nat) (h : majhul madi g l = some l') : l'.length = l.length := by
  unfold majhul at h
  split at h
  · exact absurd h (by simp)
  · simp only [Option.some.injEq] at h
    rw [← h, badilInda_tul, musharik_tul, badilInda_tul]

/-- **المجهولُ لا يخرج عن خلايا الكلمة** (`Dal.Khaliya`: دون 116) — لكلّ كلمةٍ خلاياها دون 116. -/
theorem majhul_dun_116 (madi : Bool) (g : Siga) (l l' : List Nat) (hl : ∀ c ∈ l, c < 116) (h : majhul madi g l = some l') :
    ∀ c ∈ l', c < 116 := by
  unfold majhul at h
  split at h
  · exact absurd h (by simp)
  · simp only [Option.some.injEq] at h
    rw [← h]
    exact badilInda_lt _ _ _ (musharik_lt g _ (badilInda_lt l 0 1 hl))

/-- **ما يُرفض باسمه**: القصيرُ عن موضع المشارِك بثلاث، وذو حرفِ المدّ الساكن — لكلّ صيغة، تعريفيّة. -/
theorem majhul_marfud (madi : Bool) (g : Siga) (l : List Nat) (hl : l.length < mawdiMusharik g + 3 ∨ l.any maddSakin = true) :
    majhul madi g l = none := by
  unfold majhul
  split
  · rfl
  · rename_i hn; exact absurd hl hn

/-- الشواهد: ضَرَبَ→ضُرِبَ، يَضْرِبُ→يُضْرَبُ، تَعَلَّمَ→تُعُلِّمَ (الشدّة خليتان: ساكنٌ فمتحرّك)، اِنْطَلَقَ→اُنْطُلِقَ (همزةُ الوصل حاملًا 0 مكسورةً في
الابتداء، ومضمومةً في المجهول). ض 12، ر 15، ب 26، ط 16، ق 7. -/
theorem shawahid_majhul :
    majhul true .basit [kh 12 0, kh 15 0, kh 26 0] = some [kh 12 1, kh 15 2, kh 26 0] ∧
    majhul false .basit [kh ya 0, kh 12 3, kh 15 2, kh 26 1] = some [kh ya 1, kh 12 3, kh 15 0, kh 26 1] ∧
    majhul true .thani [kh 18 0, kh 3 0, kh 13 3, kh 13 0, kh 27 0] = some [kh 18 1, kh 3 1, kh 13 3, kh 13 2, kh 27 0] ∧
    majhul true .thalith [kh 0 2, kh nun 3, kh 16 0, kh 13 0, kh 7 0] = some [kh 0 1, kh nun 3, kh 16 1, kh 13 2, kh 7 0] := by
  decide

/-- **انطلق على صورة الابتداء عند المالك**: مجهولُ صورة الابتداء (`Law.ibtidaForm`: همزةُ الوصل حاملًا 0 بحركةٍ مشتقّةٍ من الثالث
`waslHaraka`: ضمّةٌ إن ضُمَّ الثالث وإلّا كسرة) هو صورةُ ابتداء المجهول — فضمُّ الثالث (L243) يضمّ همزةَ الوصل بقاعدة المالك — على الشاهد. -/
theorem intilaq_wasl :
    majhul true .thalith (Law.ibtidaForm false [kh nun 3, kh 16 0, kh 13 0, kh 7 0]) =
      some (Law.ibtidaForm false [kh nun 3, kh 16 1, kh 13 2, kh 7 0]) := by
  decide

end JisrDal
end Jisr
