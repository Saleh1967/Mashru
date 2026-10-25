/-
# الوقفُ على أواخر الكلم المتحرّكة في الوصل عند سيبويه (الكتاب، س17782–17859)

**المصدر.** `sibawayhi.txt` المختوم (`a160f940…`)، الأسطر 17782–17859: «هذا باب الوقف في أواخر الكلم المتحركة في الوصل» (17782–17807)
و«هذا باب الوقف في آخر الكلم المتحركة في الوصل التي لا تلحقها زيادة في الوقف» (17808–17859). ورقمُ السطر خاصٌّ بهذا الملفّ.
والاقتباساتُ في `asanid` قطعٌ حرفيّة، يفحصها `tahaqquq/test_waqf.py` على المودَع موصولةَ الأسطر.

**المدخل** (حقولُ مواصفة الضابط المجمَّد `tahaqquq/dawabit/waqf/wasf.md` بأعيانها): الحرفُ الأخير `Akhir`، والتنوين، وما قبل الآخر،
وحالُ الآخر في الوصل `Haraka`، ووجهُ الوقف `Wajh`. **والمدخلُ تحليلٌ يُعطى، لا مُخرَجُ قارئٍ من النصّ** (P4 لم يُبنَ)؛ وقانونُ الوقف على
الخلايا (`Dal`، `Jisr/Utur.lean`) لا يُستعمل هنا.

**المخرج** `Hukm`: في الكلام وفي الشعر، كلٌّ من أربع: `maqbul`، `lugha` (يحكيه البابُ عن بعض العرب)، `khata`، `laHukm`.

**ما هو تعيينُ البنّاء** (لا نصُّ الباب):
- **البابُ الثاني** («التي لا تلحقها زيادة في الوقف») يسري على الحرف الصحيح غيرِ المنصوب المنوَّن: فالمنوَّنُ رفعًا وجرًّا منه («هذا خالد»،
  «مررت بخالد»)، والمنوَّنُ نصبًا ليس منه (تلحقه الألف). وأوجهُه في الرفع أربعة (س17810–17811)، وفي النصب والجرّ الرومُ والتضعيفُ
  وإجراؤه مجرى المجزوم بلا إشمام (س17844–17846).
- **التضعيف** لا يكون في الكلام إن سكن ما قبل الآخر («لم يضعفوا نحو عمرو وزيد»، س17838)، ويكون في الشعر بشاهد «جدبا» (س17835)
  وقوله «قالت العرب في الشعر في القوافي» (س17827–17828) — وعمومُ الشعر في التضعيف كلِّه قراءتي.
- **الإسكانُ مع سكون ما قبله** مقبولٌ بقوله «وقد يدعون الإشمام وروم الحركة أيضا» (س17843–17844).
- **الواوُ والياء** بعد المنوَّن رفعًا وجرًّا «لغة»: «يحذفون الياء والواو» (س17795–17796) عامّةً، و«أزد الصراة يقولون هذا زيدو …» (س17805–17806).
- **هاءُ التأنيث** هاءٌ في الوقف (س17786–17787)، والتاءُ «لغة» (س17793–17794)؛ وتاءُ الجمع والتاءُ الملحقة تاءٌ، ولا حكمَ للهاء فيهما (البابُ يفرّق
  ولا يحكم بخطئها).
- **الياءُ بعد الكسرة** («القاضي») تُحذف «وقد يحذفون» (س17797–17798)، وإثباتُها مقبول — والإثباتُ قراءتي من «قد».
- **الهاءُ بعد الحرف الصحيح منصوبًا** «لغة»: «سمع عربيا يقول أعطني أبيضه» (س17857–17858).
- وما سوى ذلك «لا حكم». **والشعر:** ما قُبل في الكلام قُبل في الشعر، والتضعيفُ كلُّه، وما سواهما «لا حكم».
- **بعد قراءة الحالات** (`natija_2.json`، على مادّةٍ مكشوفة): المنوَّنُ نصبًا بالإسكان خطأ («يلحقه» س17783 و«لا يحذفونها في وقف»
  س17802–17803)، وبالتضعيف مع سكون ما قبله خطأٌ في الكلام (س17838) — وكان «لا حكم»؛ والتاءُ الملحقة منوَّنةً نصبًا بالألف («كل اسم منون»)؛ وفي
  الشعر الواوُ والياءُ (س17829–17830) والألفُ بعد غير المنوَّن («ويمد بها في غير موضع التنوين»، س17830–17831)، والتضعيفُ بلا قيد الزيادة —
  وكانت «لا حكم».

**المنهج.** شفرةُ هذا الملفّ كُتبت قبل أن يقرأ البنّاءُ حالاتِ الضابط، وجُمّدت الحالاتُ قبلها (`tahaqquq/dawabit/waqf/tajmid.json`؛
`hawkama/منهج_الضوابط.md`)، ودُفعت في `ed25842`، والتشغيلُ الأوّل عليها في `natija_1.json` (41/52). ونتيجتُها على الضابط في
`Dal/WaqfSibawayhiQiyas.lean`، لا هنا.
-/

namespace Dal
namespace WaqfSibawayhi

/-! ## المدخل والمخرج -/

inductive Akhir
  | sahih | haTaanith | taJam | taMulhaqa | yaBaadKasra
  deriving DecidableEq, Repr

inductive Haraka
  | raf | nasb | jarr
  deriving DecidableEq, Repr

inductive Wajh
  | alif | wawAwYa | iskan | ishmam | rawm | tadif | ha | ta | hadhfYa | ithbatYa
  deriving DecidableEq, Repr

structure Kalima where
  akhir : Akhir
  munawwan : Bool
  /-- ما قبل الآخر متحرّك. -/
  qablMutaharrik : Bool
  haraka : Haraka
  wajh : Wajh
  deriving DecidableEq, Repr

inductive Daraja
  | maqbul | lugha | khata | laHukm
  deriving DecidableEq, Repr

structure Hukm where
  kalam : Daraja
  shir : Daraja
  deriving DecidableEq, Repr

/-! ## الحكم -/

/-- أوجهُ البابِ الثاني. -/
def thani (k : Kalima) : Daraja :=
  match k.wajh with
  | .iskan | .rawm => .maqbul
  | .ishmam => if k.haraka == .raf then .maqbul else .khata
  | .tadif => if k.qablMutaharrik then .maqbul else .khata
  | _ => .laHukm

/-- المنوَّنُ نصبًا: «يلحقه … الألف» (س17783)، و«لا يحذفونها في وقف» (س17802–17803)، و«لم يضعفوا» إن سكن ما قبله (س17838). -/
def munawwanNasb (k : Kalima) : Daraja :=
  match k.wajh with
  | .alif => .maqbul
  | .iskan => .khata
  | .tadif => if k.qablMutaharrik then .laHukm else .khata
  | _ => .laHukm

def kalam (k : Kalima) : Daraja :=
  match k.akhir with
  | .sahih =>
    if k.munawwan && k.haraka == .nasb then munawwanNasb k
    else if k.munawwan && k.wajh == .wawAwYa then .lugha
    else if k.haraka == .nasb && k.wajh == .ha then .lugha
    else thani k
  | .haTaanith => match k.wajh with
    | .ha => .maqbul
    | .ta => .lugha
    | _ => .laHukm
  | .taJam => if k.wajh == .ta then .maqbul else .laHukm
  | .taMulhaqa =>
    if k.munawwan && k.haraka == .nasb && k.wajh == .alif then .maqbul
    else if k.wajh == .ta then .maqbul else .laHukm
  | .yaBaadKasra => match k.wajh with
    | .hadhfYa | .ithbatYa => .maqbul
    | _ => .laHukm

/-- الشعر: ما قُبل في الكلام، والتضعيفُ في القوافي (س17827–17828، «جدبا» س17835)، والواوُ والياءُ فيها «فيما لا يدخله ياء ولا واو في
    الكلام» (س17829–17830)، والألفُ «في غير موضع التنوين» (س17830–17831). -/
def shir (k : Kalima) : Daraja :=
  if kalam k == .maqbul then .maqbul
  else if k.akhir == .sahih && k.wajh == .tadif then .maqbul
  else if k.akhir == .sahih && k.wajh == .wawAwYa then .maqbul
  else if k.akhir == .sahih && k.wajh == .alif && !k.munawwan then .maqbul
  else .laHukm

def hukm (k : Kalima) : Hukm := ⟨kalam k, shir k⟩

/-! ## الأسانيد (قطعٌ حرفيّة؛ يفحصها `tahaqquq/test_waqf.py` موصولةَ الأسطر) -/

def asanid : List (String × Nat × Nat × String) := [
  ("alif", 17783, 17783, "أما كل اسم منون فإنه يلحقه في حال النصب في الوقف الألف"),
  ("ha", 17786, 17787, "فعلامة التأنيث إذا وصلته التاء وإذا وقفت ألحقت الهاء"),
  ("talhat", 17793, 17794, "وزعم أبو الخطاب أن ناسا من العرب يقولون في الوقف طلحت كما قالوا في تاء الجميع قولا واحدا في الوقف والوصل"),
  ("yahdhifun", 17795, 17796, "فأما في حال الجر والرفع فإنهم يحذفون الياء والواو"),
  ("alqad", 17797, 17798, "وقد يحذفون في الوقف الياء التي قبلها كسرة وهي من نفس الحرف نحو القاض"),
  ("azd", 17805, 17806, "وزعم أبو الخطاب أن أزد الصراة يقولون هذا زيدو وهذا عمرو ومررت بزيدي وبعمري"),
  ("arbaa", 17810, 17811, "فأما المرفوع والمضموم فإنه يوقف عنده على أربعة أوجه بالإشمام وبغير الإشمام كما تقف عند المجزوم والساكن وبأن تروم التحريك وبالتضعيف"),
  ("qawafi", 17827, 17828, "ومن ثم قالت العرب في الشعر في القوافي سبسبا يريد السبسب"),
  ("jadba", 17835, 17835, "لقد خشيت أن أرى جدبا"),
  ("layahdhifunaha", 17802, 17803, "ولا يحذفونها في وقف"),
  ("qawafiWaw", 17829, 17830, "كما يلحقون الواو والياء في القوافي فيما لا يدخله ياء ولا واو في الكلام"),
  ("ghayrTanwin", 17830, 17831, "وأجروا الألف مجراهما لأنها شريكتهما في القوافي ويمد بها في غير موضع التنوين"),
  ("lamYudiffu", 17838, 17838, "فإن كان الحرف الذي قبل آخر حرف ساكنا لم يضعفوا نحو عمرو وزيد"),
  ("yadauna", 17843, 17844, "وقد يدعون الإشمام وروم الحركة أيضا"),
  ("nasbJarr", 17844, 17845, "وأما ما كان في موضع نصب أوجر فإنك تروم فيه الحركة وتضاعف وتفعل فيه ما تفعل بالمجزوم على كل حال"),
  ("laSabil", 17846, 17846, "وأما الإشمام فليس إليه سبيل"),
  ("abyadahu", 17857, 17858, "وحدثني من أثق به أنه سمع عربيا يقول أعطني أبيضه يريد أبيض")]

/-! ## مبرهنات (خواصُّ التعيين على مجاله؛ والضابطُ يشهد أنّه غيرُ فارغ: `Dal/WaqfSibawayhiQiyas.lean`) -/

/-- **لا إشمامَ في النصب والجرّ** (تعريفيّة): «فالنصب والجر لا يوافقان الرفع في الإشمام» (س17852). -/
theorem la_ishmam (m q : Bool) (h : Haraka) (hh : h ≠ .raf) (hn : ¬ (m = true ∧ h = .nasb)) :
    kalam ⟨.sahih, m, q, h, .ishmam⟩ = .khata := by
  cases m <;> cases h <;> simp_all [kalam, thani]

/-- **لا تضعيفَ في الكلام إن سكن ما قبل الآخر، ويكون في الشعر** (تعريفيّة؛ وكان قبل قراءة الحالات بفرض «غيرِ المنوَّن نصبًا»). -/
theorem tadif_baad_sakin (m : Bool) (h : Haraka) :
    hukm ⟨.sahih, m, false, h, .tadif⟩ = ⟨.khata, .maqbul⟩ := by
  cases m <;> cases h <;> simp_all [hukm, kalam, shir, thani, munawwanNasb]

/-- **المنوَّنُ نصبًا وما أُضيف بعد قراءة الحالات** (على الشاهد): الإسكانُ خطأ، والتاءُ الملحقة بالألف، والواوُ في الشعر، والألفُ بعد غير
    المنوَّن في الشعر. -/
theorem munawwan_nasb_shawahid :
    kalam ⟨.sahih, true, false, .nasb, .iskan⟩ = .khata ∧
    kalam ⟨.taMulhaqa, true, false, .nasb, .alif⟩ = .maqbul ∧
    hukm ⟨.sahih, true, false, .raf, .wawAwYa⟩ = ⟨.lugha, .maqbul⟩ ∧
    hukm ⟨.sahih, false, true, .nasb, .alif⟩ = ⟨.laHukm, .maqbul⟩ := by
  decide

/-- **ما قُبل في الكلام قُبل في الشعر** (تعريفيّة). -/
theorem maqbul_kalam_maqbul_shir (k : Kalima) (h : kalam k = .maqbul) : shir k = .maqbul := by
  simp [shir, h]

/-- **الشواهد** (على الشاهد): الألفُ في المنوَّن نصبًا، والإشمامُ في «هذا خالد»، والواوُ عند أزد الصراة لغة، وطلحت لغة. -/
theorem shawahid :
    kalam ⟨.sahih, true, true, .nasb, .alif⟩ = .maqbul ∧
    kalam ⟨.sahih, true, true, .raf, .ishmam⟩ = .maqbul ∧
    kalam ⟨.sahih, true, false, .raf, .wawAwYa⟩ = .lugha ∧
    kalam ⟨.haTaanith, false, false, .raf, .ta⟩ = .lugha ∧
    kalam ⟨.yaBaadKasra, false, false, .jarr, .hadhfYa⟩ = .maqbul := by
  decide

end WaqfSibawayhi
end Dal
