/-
  Jisr/JisrDal.lean — الجسرُ إلى الدالّ: الإعرابُ بالحروف والتقديرُ وجرُّ الممنوع من الصرف بالفتحة وصيغةُ المجهول، على خلايا الكلمة وأطر المالك
  (`SLGE/Bridge.lean`: الحالةُ تحمل الإعراب، والعلاماتُ الفرعيّة حواملُها من حروف الزيادة؛ `SLGE/Wad.lean`: الإعراباتُ الأربعة).
  قرارُ المالك (2026-10-17، 00:09): «يجب عمل lean الجسر للدال … عمل الجسر lean وslge وبعدها ننتقل للإنشاء».

  **المرجع** (قطر الندى، مودَع مختوم، بأسطره): L75–77 «أنواع الإعراب أربعة … فيرفع بضمة، وينصب بفتحة، ويجر بكسرة، ويجزم بحذف حركة، إلا
  الأسماء الستة»؛ L78–80: «وهي أبوه وأخوه وحموها / وهنوه وفوه وذو مال، فترفع بالواو وتنصب بالألف وتجر بالياء»؛ L82–83: «والمثنى كالزيدان فيرفع
  بالألف، وجمع المذكر السالم كالزيدون فيرفع / بالواو، ويجران وينصبان بالياء»؛ L86–88: «وأولات وما جمع بألف وتاء مزيدتين وما سمي به منهما فينصب
  بالكسرة … / … وما لا ينصرف فيجر بالفتحة نحو "بأفضل منه"، / إلا مع أل نحو "بالأفضل" أو بالإضافة نحو "بأفضلكم"»؛ L88–90: «والأمثلة الخمسة، وهي
  / تفعلان وتفعلون بالياء والتاء فيهما، وتفعلين، فترفع بثبوت النون، وتجزم / وتنصب بحذفها»؛ L90–91: «والفعل المضارع المعتل / الآخر فيجزم بحذف
  آخره، نحو "لم يغز ولم يخش ولم يرم"»؛ L92–95: «فصل: تقدر جميع الحركات في نحو "غلامي والفتى" ويسمى مقصورا، والضمة / والكسرة في نحو "القاضي"
  ويسمى منقوصا، والضمة والفتحة في نحو "يخشى"، / والضمة في نحو "يدعو ويقضي". وتظهر الفتحة في نحو "إن القاضي لن يقضي ولن / يدعو"»؛ المجهول L241–244:
  «ويضم أول الفعل مطلقا، ويشاركه ثاني نحو / تعلم، وثالث نحو انطلق. ويفتح ما قبل الآخر في المضارع، ويكسر في الماضي»؛ موانع الصرف L419–421
  (بالاسم عند المالك `Wad.mawani9`).

  **الصورة.** الخليةُ `4·حرف + حالة` (فتحة 0، ضمّة 1، كسرة 2، سكون 3 — `Dal.Khaliya`؛ الحروفُ بترتيب المخارج `Dal.Makharij.hawamil`: ا 2، ي 11،
  ن 14، و 28). (١) **البابُ معلَن** `Bab`: المفردُ المنصرف وجمعُ التكسير، والفعلُ الصحيح، والمقصور، والمنقوص، والمضافُ إلى الياء، والأسماءُ
  الستّة، والمثنّى، وجمعُ المذكر السالم، وجمعُ المؤنث السالم، والممنوعُ من الصرف (مجرّدًا أو مع أل والإضافة)، والأمثلةُ الخمسة، والمضارعُ المعتلّ
  الآخر — فالدالُّ لا يقرّر بابَ الكلمة (أهي مثنًّى أم اسمٌ آخرُه ألفٌ ونون؟): البابُ من المعجم، والجسرُ يقرأ الإعرابَ من الخلايا **بعد** إعلان
  الباب (كما أنّ الدالَّ وحده لا يقرّر المدلول: `Bridge.dal_undetermines`). (٢) **الحكمُ من الدالّ** `HukmDal` ثلاثيّ: معيَّنٌ، أو محتمَلٌ بين أكثر
  من إعرابٍ (الدالُّ لا يفرّق: ياءُ المثنّى والجمع نصبًا وجرًّا، فتحةُ الممنوع نصبًا وجرًّا، تقديرُ المقصور)، أو لا حكم (خليةٌ لا يقبلها الباب).
  `hukm` يقرأ الخليةَ الأخيرة (وقبلَها في المثنّى والجمع). (٣) **الأصليةُ** هي تقابلُ المالك بعينه (`Bridge.irabState`: `asliyya_bij`)؛
  **والفرعيةُ** توافق جدولَه `Bridge.farIya` حاملًا حاملًا (`muwafiq_farIya` على شواهد القطر) وحواملُها من حروف الزيادة (`Bridge.fariya_augs`).
  (٤) **التقدير**: المقصورُ والمضافُ إلى الياء لا يعيّنان شيئًا (`maqsur_la_yuayyin`، `mudaf_la_yuayyin`)، والمنقوصُ تظهر فتحتُه وحدَها
  (`manqus_fatha_zahira`). (٥) **الممنوع**: فتحتُه نصبٌ أو جرٌّ ولا كسرةَ له، ومع أل أو الإضافة يُجرّ بالكسرة (`mamnu_fatha`، `mamnu_bi_al`).
  (٦) **الأمثلةُ الخمسة**: بالنون رفعٌ وبحذفها نصبٌ أو جزم (`amthila_nun`). (٧) **المجهول** `majhul`: ضمُّ الأوّل (ومعه الثاني في نحو تعلّم،
  والثالث في نحو انطلق — بالصيغة المعلَنة `Siga`)، وفتحُ ما قبل الآخر في المضارع وكسرُه في الماضي؛ يحفظ الحروفَ والطولَ (`majhul_huruf`،
  `majhul_tul`)، ولا يُبنى من أقلّ من ثلاث خلايا (`majhul_qasir`)؛ وهو نظيرُ `Shabaka.jahhil` على الأدوار: ذاك يبدّل الدورَ وهذا يبدّل الحركات.
  (٨) **الشواهد** مبنيّةً خلايا (20): أبو/أبا/أبي (قبل المضاف إليه)، الزيدان/الزيدين/بالزيدين، الزيدون/الزيدين/بالزيدين، مسلماتُ/مسلماتِ، بأفضلَ/بالأفضلِ، تفعلانِ/تفعلا، يخشى، يدعو/يدعوَ،
  القاضي/القاضيَ، ضَرَبَ→ضُرِبَ، يَضْرِبُ→يُضْرَبُ، تَعَلَّمَ→تُعُلِّمَ، انْطَلَقَ→انْطُلِقَ.

  **المبرهنات (لكلّ، 2؛ استقراءٌ على القائمة):** `majhul_huruf`، `majhul_tul`. **تعريفيّة (9؛ فكُّ `hukm` على الخلية الأخيرة بالقواعد المساعدة
  `harf_kh`/`hala_kh`/`akhir_append`):** `asliyya_bij`، `maqsur_la_yuayyin`، `mudaf_la_yuayyin`، `yayn_la_yufarriq`، `manqus_fatha_zahira`، `mamnu_fatha`،
  `mamnu_bi_al`، `amthila_nun`، `majhul_qasir`. **على الشاهد (4):** `sitta_hamil` (على `Law.augs`)، `muwafiq_farIya` (على `Bridge.farIya` بشواهد
  القطر العشرين)، `shawahid_hukm`، `shawahid_majhul`. (15 في `Audit.lean`؛ والقواعدُ المساعدة `badilInda_harf`/`badilInda_tul`/`musharik_*` داخليّة.)

  الوسم: مبرهن (لكلّ) / تعريفيّة / على الشاهد كما سُمّي. تعييناتُ البنّاء (تُعرض على المالك): البابُ معلَنٌ من المعجم لا من الدالّ؛ قراءةُ
  الخليتين الأخيرتين في المثنّى والجمع بلا اعتبار حركة النون؛ المنقوصُ المنوَّن (قاضٍ) غيرُ مبنيّ (التنوينُ في القارئ)؛ موانعُ الصرف التسعة
  نفسُها (أيُّ اسمٍ ممنوع) من المعجم (`Wad.mawani9` بالاسم)؛ المضارعُ المعتلّ: الجزمُ بحذف حرف العلّة يُقرأ من غياب حرف العلّة آخرًا؛ صيغُ المجهول
  الثلاث (بسيط/تفعّل/انفعل) تعيينٌ على مثالَي القطر، وتصريفُ قال وباع (L244) لم يُبنَ. الجدولُ `jisr_dal.tsv` مسجَّلٌ «مرشّحًا» حتّى يأذن المالك
  بختمه؛ ومطابقتُه `tahaqquq/test_jisrdal.py`.
-/
import SLGE.Bridge
import Dal.Makharij

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

/-- الحروفُ الحوامل في الإعراب بالحروف (بترتيب `Dal.Makharij.hawamil`): ا 2، ي 11، ن 14، و 28. -/
def alif : Nat := 2
def ya : Nat := 11
def nun : Nat := 14
def waw : Nat := 28

/-- الصيغةُ الصرفيّة للمجهول (القطر L242–243): بسيطٌ (ضمُّ الأوّل)، وما شاركه ثانيه (تعلّم)، وما شاركه ثالثه (انطلق). -/
inductive Siga | basit | thani | thalith
deriving DecidableEq, Repr

/-- أبوابُ الإعراب على الدالّ — تُعلَن من المعجم لا من الدالّ. -/
inductive Bab
  | mufrad                 -- المفرد المنصرف وجمع التكسير: بالحركات (L77)
  | filSahih               -- الفعل المضارع الصحيح الآخر: ضمّة/فتحة/سكون
  | maqsur                 -- تُقدَّر جميع الحركات (L92)
  | manqus                 -- تُقدَّر الضمّة والكسرة وتظهر الفتحة (L93، L95)
  | mudafLiYa              -- المضاف إلى ياء المتكلّم (L92)
  | sitta                  -- الأسماء الستّة: بالواو والألف والياء (L78–80)
  | muthanna               -- بالألف رفعًا وبالياء نصبًا وجرًّا (L82–83)
  | jamMudhakkar           -- بالواو رفعًا وبالياء نصبًا وجرًّا (L82–83)
  | jamMuannath            -- يُنصب بالكسرة (L86–87)
  | mamnu (alAwIdafa : Bool) -- ما لا ينصرف: يُجرّ بالفتحة إلّا مع أل أو الإضافة (L87–88)
  | amthila                -- الأمثلة الخمسة: بثبوت النون وحذفها (L88–90)
  | mudariMutall           -- المضارع المعتلّ الآخر: جزمه بالحذف وتقديره (L90–91، L94–95)
deriving DecidableEq, Repr

/-- حكمُ الإعراب من الدالّ: معيَّن، أو محتمَلٌ بين أكثر من إعراب (الدالّ لا يفرّق)، أو لا حكم. -/
inductive HukmDal
  | muayyan (i : Irab)
  | muhtamal (l : List Irab)
  | laHukm
deriving DecidableEq, Repr

/-- الإعرابُ من الحالة الأصلية (تقابلُ المالك `Bridge.irabState` معكوسًا). -/
def irabMinHala : Nat → Option Irab
  | 0 => some .nasb | 1 => some .raf | 2 => some .jarr | 3 => some .jazm | _ => none

/-- الخليةُ الأخيرة وما قبلها. -/
def akhir (l : List Nat) : Option Nat := l.getLast?
def qablAkhir (l : List Nat) : Option Nat := l.dropLast.getLast?

theorem akhir_append (l : List Nat) (c : Nat) : akhir (l ++ [c]) = some c := by simp [akhir]
theorem akhir_append2 (l : List Nat) (d c : Nat) : akhir (l ++ [d, c]) = some c := by simp [akhir]
theorem qablAkhir_append (l : List Nat) (d c : Nat) : qablAkhir (l ++ [d, c]) = some d := by
  simp [qablAkhir, List.dropLast_append_of_ne_nil]

/-- **الجسر:** حكمُ الإعراب من الباب المعلَن وخلايا الكلمة. -/
def hukm (b : Bab) (l : List Nat) : HukmDal :=
  match akhir l with
  | none => .laHukm
  | some c =>
    match b with
    | .mufrad => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 2 => .muayyan .jarr | _ => .laHukm
    | .filSahih => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 3 => .muayyan .jazm | _ => .laHukm
    | .maqsur => .muhtamal [.raf, .nasb, .jarr]
    | .mudafLiYa => .muhtamal [.raf, .nasb, .jarr]
    | .manqus => if harf c == ya then (if hala c == 0 then .muayyan .nasb else .muhtamal [.raf, .jarr]) else .laHukm
    | .sitta => if harf c == waw then .muayyan .raf else if harf c == alif then .muayyan .nasb
                else if harf c == ya then .muayyan .jarr else .laHukm
    | .muthanna => if harf c == nun then
          (match qablAkhir l with
           | some d => if harf d == alif then .muayyan .raf else if harf d == ya then .muhtamal [.nasb, .jarr] else .laHukm
           | none => .laHukm)
        else .laHukm
    | .jamMudhakkar => if harf c == nun then
          (match qablAkhir l with
           | some d => if harf d == waw then .muayyan .raf else if harf d == ya then .muhtamal [.nasb, .jarr] else .laHukm
           | none => .laHukm)
        else .laHukm
    | .jamMuannath => match hala c with
      | 1 => .muayyan .raf | 2 => .muhtamal [.nasb, .jarr] | _ => .laHukm
    | .mamnu false => match hala c with
      | 1 => .muayyan .raf | 0 => .muhtamal [.nasb, .jarr] | _ => .laHukm
    | .mamnu true => match hala c with
      | 0 => .muayyan .nasb | 1 => .muayyan .raf | 2 => .muayyan .jarr | _ => .laHukm
    | .amthila => if harf c == nun then .muayyan .raf else .muhtamal [.nasb, .jazm]
    | .mudariMutall => if harf c == alif then .muhtamal [.raf, .nasb]
                       else if harf c == waw || harf c == ya then (if hala c == 0 then .muayyan .nasb else .muayyan .raf)
                       else .muayyan .jazm

/-- هل يحتمل الحكمُ هذا الإعراب؟ -/
def yahtamil : HukmDal → Irab → Bool
  | .muayyan i, j => i == j
  | .muhtamal l, j => l.contains j
  | .laHukm, _ => false

/-! ## ٢. الأصلية تقابلُ المالك، والفرعية توافق جدولَه -/

/-- **العلاماتُ الأصلية هي تقابلُ المالك بعينه**: المفردُ المنصرف آخرُه حالةُ الإعراب (`Bridge.irabState`) للرفع والنصب والجرّ، والفعلُ
الصحيح للرفع والنصب والجزم — لكلّ كلمةٍ وحرفٍ أخير. -/
theorem asliyya_bij (l : List Nat) (h : Nat) :
    (∀ i : Irab, i ≠ .jazm → hukm .mufrad (l ++ [kh h (Bridge.irabState i)]) = .muayyan i) ∧
    (∀ i : Irab, i ≠ .jarr → hukm .filSahih (l ++ [kh h (Bridge.irabState i)]) = .muayyan i) := by
  refine ⟨fun i hi => ?_, fun i hi => ?_⟩ <;> cases i <;>
    simp [hukm, akhir_append, hala_kh, Bridge.irabState] at *

/-- **المقصورُ لا يعيّن شيئًا** — الحركاتُ كلُّها مقدَّرة (L92): لكلّ كلمةٍ وخليةٍ أخيرة. -/
theorem maqsur_la_yuayyin (l : List Nat) (c : Nat) : ∀ i, hukm .maqsur (l ++ [c]) ≠ .muayyan i := by
  intro i; simp [hukm, akhir_append]

/-- **المضافُ إلى الياء لا يعيّن شيئًا** (L92). -/
theorem mudaf_la_yuayyin (l : List Nat) (c : Nat) : ∀ i, hukm .mudafLiYa (l ++ [c]) ≠ .muayyan i := by
  intro i; simp [hukm, akhir_append]

/-- **ياءُ المثنّى والجمع لا تفرّق النصبَ من الجرّ** — لكلّ كلمةٍ آخرُها ياءٌ فنون: محتمَلٌ بينهما (L83). -/
theorem yayn_la_yufarriq (l : List Nat) (sy sn : Nat) (hsy : sy < 4) (hsn : sn < 4) :
    hukm .muthanna (l ++ [kh ya sy, kh nun sn]) = .muhtamal [.nasb, .jarr] ∧
    hukm .jamMudhakkar (l ++ [kh ya sy, kh nun sn]) = .muhtamal [.nasb, .jarr] := by
  constructor <;> simp [hukm, akhir_append2, qablAkhir_append, harf_kh, hsy, hsn, ya, nun, waw, alif]

/-- **المنقوصُ تظهر فتحتُه وحدَها** (L93، L95): ياءٌ مفتوحةٌ نصبٌ، وإلّا الرفعُ والجرُّ مقدَّران — تعريفيّة. -/
theorem manqus_fatha_zahira (l : List Nat) (s : Nat) (hs : s < 4) :
    hukm .manqus (l ++ [kh ya s]) = (if s = 0 then .muayyan .nasb else .muhtamal [.raf, .jarr]) := by
  simp only [hukm, akhir_append, harf_kh ya s hs, hala_kh ya s hs, beq_self_eq_true, if_true]
  by_cases h0 : s = 0
  · subst h0; rfl
  · have : (s == 0) = false := by simp [h0]
    simp [this, h0]

/-- **الممنوعُ من الصرف**: فتحتُه نصبٌ أو جرّ (الدالّ لا يفرّق)، ولا كسرةَ له (L87–88) — تعريفيّة. -/
theorem mamnu_fatha (l : List Nat) (h : Nat) :
    hukm (.mamnu false) (l ++ [kh h 0]) = .muhtamal [.nasb, .jarr] ∧ hukm (.mamnu false) (l ++ [kh h 2]) = .laHukm := by
  constructor <;> simp [hukm, akhir_append, hala_kh]

/-- **ومع أل أو الإضافة يُجرّ بالكسرة** كالمنصرف (L88) — تعريفيّة. -/
theorem mamnu_bi_al (l : List Nat) (h : Nat) : hukm (.mamnu true) (l ++ [kh h 2]) = .muayyan .jarr := by
  simp [hukm, akhir_append, hala_kh]

/-- **الأمثلةُ الخمسة**: بثبوت النون رفعٌ، وبحذفها نصبٌ أو جزم (L89–90) — تعريفيّة. -/
theorem amthila_nun (l : List Nat) (sn h s : Nat) (hsn : sn < 4) (hs : s < 4) (hh : h ≠ nun) :
    hukm .amthila (l ++ [kh nun sn]) = .muayyan .raf ∧ hukm .amthila (l ++ [kh h s]) = .muhtamal [.nasb, .jazm] := by
  constructor
  · simp [hukm, akhir_append, harf_kh nun sn hsn]
  · simp [hukm, akhir_append, harf_kh h s hs, hh]

/-- **حواملُ الأسماء الستّة** من حروف الزيادة — تعريفيّة على جدول المالك (`Bridge.fariya_augs`). -/
theorem sitta_hamil : [waw, alif, ya].all (fun c => Law.augs.contains c) = true := by decide

/-! ## ٣. الشواهد: توافقُ جدول المالك `Bridge.farIya` -/

/-- شواهدُ القطر خلايا: (الباب، الكلمة، الإعرابُ المشهود)؛ الأسماءُ الستّة قبل المضاف إليه (الحاملُ آخرُها). ب 26، ه 1، ز 19، د 17، م 27، س 20، ل 13، ت 18، ف 25، ض 12، ع 3، خ 6، ش 10، ق 7. -/
def shawahid : List (String × Bab × List Nat × Irab) :=
  [("أبو(ه)", .sitta, [kh 0 0, kh 26 1, kh waw 3], .raf),
   ("أبا(ه)", .sitta, [kh 0 0, kh 26 0, kh alif 3], .nasb),
   ("أبي(ه)", .sitta, [kh 0 0, kh 26 2, kh ya 3], .jarr),
   ("الزيدان", .muthanna, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 0, kh alif 3, kh nun 2], .raf),
   ("الزيدين", .muthanna, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 0, kh ya 3, kh nun 2], .nasb),
   ("بالزيدين", .muthanna, [kh 26 2, kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 0, kh ya 3, kh nun 2], .jarr),
   ("الزيدون", .jamMudhakkar, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 1, kh waw 3, kh nun 0], .raf),
   ("الزيدين", .jamMudhakkar, [kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 2, kh ya 3, kh nun 0], .nasb),
   ("بالزيدين", .jamMudhakkar, [kh 26 2, kh 0 0, kh 13 3, kh 19 0, kh ya 3, kh 17 2, kh ya 3, kh nun 0], .jarr),
   ("مسلماتُ", .jamMuannath, [kh 27 1, kh 20 3, kh 13 2, kh 27 0, kh alif 3, kh 18 1], .raf),
   ("مسلماتِ", .jamMuannath, [kh 27 1, kh 20 3, kh 13 2, kh 27 0, kh alif 3, kh 18 2], .nasb),
   ("بأفضلَ", .mamnu false, [kh 26 2, kh 0 0, kh 25 3, kh 12 0, kh 13 0], .jarr),
   ("بالأفضلِ", .mamnu true, [kh 26 2, kh 0 0, kh 13 3, kh 0 0, kh 25 3, kh 12 0, kh 13 2], .jarr),
   ("تفعلانِ", .amthila, [kh 18 0, kh 25 3, kh 3 0, kh 13 0, kh alif 3, kh nun 2], .raf),
   ("تفعلا", .amthila, [kh 18 0, kh 25 3, kh 3 0, kh 13 0, kh alif 3], .nasb),
   ("يخشى", .mudariMutall, [kh ya 0, kh 6 3, kh 10 0, kh alif 3], .raf),
   ("يدعو", .mudariMutall, [kh ya 0, kh 17 3, kh 3 1, kh waw 3], .raf),
   ("يدعوَ", .mudariMutall, [kh ya 0, kh 17 3, kh 3 1, kh waw 0], .nasb),
   ("القاضي", .manqus, [kh 0 0, kh 13 3, kh 7 0, kh alif 3, kh 12 2, kh ya 3], .raf),
   ("القاضيَ", .manqus, [kh 0 0, kh 13 3, kh 7 0, kh alif 3, kh 12 2, kh ya 0], .nasb)]

/-- **الشواهدُ العشرون**: كلُّ شاهدٍ يحتمل إعرابَه المشهود، والمعيَّنُ منها أحدَ عشرَ والباقي محتمَل (الدالّ لا يفرّق). -/
theorem shawahid_hukm :
    shawahid.all (fun s => yahtamil (hukm s.2.1 s.2.2.1) s.2.2.2) = true ∧
    (shawahid.filter fun s => match hukm s.2.1 s.2.2.1 with | .muayyan _ => true | _ => false).length = 11 := by decide

/-- جدولُ المالك `Bridge.farIya` بأبوابنا: الاسمُ ← الباب. -/
def babOf : String → Option Bab
  | "الأسماء الستة" => some .sitta | "المثنى" => some .muthanna | "جمع المذكر" => some .jamMudhakkar
  | "الأمثلة الخمسة" => some .amthila | _ => none

/-- **توافقُ جدول المالك**: لكلّ صفٍّ (باب، إعراب، حامل) في `Bridge.farIya` شاهدٌ من أبوابنا بذلك الباب، حاملُ علامته ذلك الحرفُ بعينه،
وحكمُه من الدالّ يحتمل ذلك الإعراب. -/
theorem muwafiq_farIya :
    Bridge.farIya.all (fun x => shawahid.any fun s =>
      babOf x.1 == some s.2.1 && s.2.2.2 == x.2.1 && yahtamil (hukm s.2.1 s.2.2.1) x.2.1 &&
      (match s.2.1 with
       | .muthanna | .jamMudhakkar => qablAkhir s.2.2.1 |>.map harf
       | _ => akhir s.2.2.1 |>.map harf) == some x.2.2) = true := by decide

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

/-- مشاركةُ الثاني (تعلّم) أو الثالث (انطلق) في الضمّ. -/
def musharik : Siga → List Nat → List Nat
  | .basit, l => l
  | .thani, l => badilInda l 1 1
  | .thalith, l => badilInda l 2 1

theorem musharik_harf (g : Siga) (l : List Nat) : (musharik g l).map harf = l.map harf := by
  cases g <;> simp [musharik, badilInda_harf]

theorem musharik_tul (g : Siga) (l : List Nat) : (musharik g l).length = l.length := by
  cases g <;> simp [musharik, badilInda_tul]

/-- **المجهول** (L242–244): ضمُّ الأوّل — ومعه الثاني في نحو تعلّم، والثالث في نحو انطلق — وكسرُ ما قبل الآخر في الماضي وفتحُه في المضارع؛
ولا يُبنى من أقلّ من ثلاث خلايا. -/
def majhul (madi : Bool) (g : Siga) (l : List Nat) : Option (List Nat) :=
  if l.length < 3 then none
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

/-- **لا مجهولَ من أقلّ من ثلاث خلايا** — لكلّ صيغة. -/
theorem majhul_qasir (madi : Bool) (g : Siga) (l : List Nat) (hl : l.length < 3) : majhul madi g l = none := by
  simp [majhul, hl]

/-- الشواهد: ضَرَبَ→ضُرِبَ، يَضْرِبُ→يُضْرَبُ، تَعَلَّمَ→تُعُلِّمَ (الشدّة خليتان: ساكنٌ فمتحرّك)، انْطَلَقَ→انْطُلِقَ (همزة الوصل ألفًا). ض 12، ر 15، ب 26، ط 16، ق 7. -/
theorem shawahid_majhul :
    majhul true .basit [kh 12 0, kh 15 0, kh 26 0] = some [kh 12 1, kh 15 2, kh 26 0] ∧
    majhul false .basit [kh ya 0, kh 12 3, kh 15 2, kh 26 1] = some [kh ya 1, kh 12 3, kh 15 0, kh 26 1] ∧
    majhul true .thani [kh 18 0, kh 3 0, kh 13 3, kh 13 0, kh 27 0] = some [kh 18 1, kh 3 1, kh 13 3, kh 13 2, kh 27 0] ∧
    majhul true .thalith [kh alif 3, kh nun 3, kh 16 0, kh 13 0, kh 7 0] = some [kh alif 1, kh nun 3, kh 16 1, kh 13 2, kh 7 0] := by
  decide

end JisrDal
end Jisr
