/-
  Jisr/Utur.lean — أطرُ الطبقات الثلاث على القانون العامّ (ابتداء/وصل/وقف): الدالُّ وحده، والمدلولُ وحده، والدالُّ والمدلولُ معًا.
  قرار المالك (2026-10-16): «بناء أطر الدال وحده lean and slge وأطر المدلول وحده والأهم أطر الدال والمدلول معا lean slge وفق
  القانون العام».

  **القانون العامّ** عند المالك ثلاثةُ أحكام — الابتداءُ والوصلُ والوقف — نصُّه في الدالّ (`SLGE/Law.lean` رأس الملفّ: «القانونُ
  واحدٌ بثلاثة مواضع: الابتداء: لا يُبتدأ بساكن… الوصل: لا يلتقي ساكنان… الوقف: آخرُ السلسلة يُعفى فيه التقاءُ الساكنين»؛ وفي
  `SLGE/Necessity.lean` س25: «الحدُّ الأدنى المكتمل: يُبتدأ به (القانون من الحالة 0)، ويوصَل (الانتقالاتُ)، ويوقَف عليه بعد التسكين» =
  `complete'`)، وفي التركيب (`SLGE/Tarkib.lean`: «القانون في التركيب»)، وفي الإحالة والسمات (`Maqam`، `Simat`). وهنا يُستوفى على
  الطبقات الثلاث التي رتّبها ج3 (737: اللفظ باعتبار الدالّ وحده؛ 753: باعتبار المدلول وحده؛ 771: باعتبار الدالّ والمدلول معًا — كما
  في `Dal/AqsamAllafz.lean`، `Madlul/AqsamAlmadlul.lean`، `Jisr/AqsamDalMadlul.lean`): لكلّ طبقةٍ إطارٌ وثلاثةُ أحكامٍ مسمّاةٍ
  بموضعها، وشواهدُ بـ decide، ورقمٌ يُفكّ للمدلول وللطبقة الثالثة (والدالُّ برقم المالك `encS`). **أحكامُ الدالّ الثلاثة هنا قراءةٌ
  لتقسيم المالك في Necessity س25 (لا نقلٌ لـ`Fwasl`)؛
  وتعيينُها على المدلول وعلى الطبقة الثالثة قرارٌ معلَنٌ للبنّاء** على نهجه — لا نصَّ عنده يسمّي الثلاثةَ في المدلول (`MadlulAwwalan`،
  `Category`). **أمضى المالكُ التعييناتِ 2026-10-16:** `nisabMahmul`، وازدواجُ «التقييدية» (قيدٌ هنا / مفعوليةٌ في `Nisab`)، وخانتا
  المسند والمسند إليه، و`jinsMahmul`، و`qismDawr` (كان/ظنّ فعل)، و`halaIrab`، وحدُّ الطبقة (المستترُ والضميرُ المتّصل والمثنّى والمضارعُ
  خبرًا خارجَه)؛ ووافق على ما بعدها: معجمُ الأجناس وخواصّها مودَعًا، ثمّ الأسماءُ من المخصّص والسمات، وجسرُ `Maqam` والإعرابُ
  بالحروف والتنازع.

  **١. إطارُ الدالّ وحده** `ItarDal = List NawMaqta`: نمطُ مقاطع السلسلة من تقطيعنا المبرهَن (`Dal.qatta`: `qatta_sahih`، `qatta_wahid`،
  `anwa_sitta`)، ولا نمطَ للفارغ. الأحكامُ على آلة المالك `Msent`: **ابتداء** الانتقالُ الأوّل من الحالة 0 حيّ (`δ 0 a ≠ 96`: لا
  ساكنَ ولا ألفَ متحرّكةً أوّلًا)؛ **وصل** الانتقالاتُ كلُّها حيّة في السلسلة كما تُقرأ (`run 0 l ≠ 96`: قانونُ الوصل داخلَ السلسلة —
  **وهو غيرُ `Fwasl` المالك** الذي يسأل عن قبول متحرّكٍ بعد الآخر: «بِنْت» حيّةُ الانتقالات وقفًا بساكنين و`Fwasl` يردّها إن وُصلت،
  `wasl_ghayr_Fwasl`)؛ **وقف** «المكتمل» عند المالك بعينه `complete'` (وقفيّةٌ بعد تسكين الآخر) — **وهو يحوي الابتداءَ والوصلَ بعد
  التسكين**، فالفصلُ بين الثلاثة هنا فصلٌ بالتسمية والموضع (خللُ كلٍّ يُسمّى) لا تقسيمٌ إلى شروطٍ مستقلّة؛ وما يزيده الإطارُ على المكتمل
  هو الوصلُ كما تُقرأ. العلاقاتُ مبرهَنة: الوصلُ والوقفُ كلٌّ منهما يستلزم الابتداء (`wasl_yastalzim_ibtida`، `waqf_yastalzim_ibtida`)؛
  والوصلُ والوقفُ مستقلّان على الشاهد (`wasl_waqf_mustaqillan`: الخليةُ الواحدة توصَل ولا يوقَف عليها، و«لَا» بألفٍ متحرّكة آخرًا تكتمل
  بالتسكين وتموت كما تُقرأ)؛ وما استوفى الثلاثةَ فحالتُه كما تُقرأ وقفيّةٌ (`dal_waqf_kama_yuqra` على `mover_step` المالك). والإطارُ أضيقُ
  من `complete'`: على السلاسل من خليتين، 84 يكتملها التسكينُ وتموت كما تُقرأ، وآخرُها ألفٌ متحرّكة (`dal_vs_complete`).
  الاستنفاد: لا سلسلةَ من خلية (المالك `nec_second`)، وعلى الخليتين الإطارُ والتقطيعُ سواء (`itar_dal_istinfad_2`)؛ و9,436 سلسلةً
  من خليتين يرخّصها الإطار: CV·CV 7056، CVV 84، CVC 2296، ولا نمطَ رابع (`itar_dal_anmat_2`). السلسلةُ «يرخّصها الإطار» لا «كلمة»:
  الكلمةُ وضعٌ فوق الدالّ.

  **٢. إطارُ المدلول وحده** `ItarMadlul = (موضوع، محمول، نسبة)` على مدلول المالك (`SLGE.Awwalan.Madlul`: حقيقةٌ وخواصُّ وعلاقاتٌ
  وقابليّاتٌ وأفراد، ومعنًى في نفسه `ind` وزمانٌ بهيئته `tim` — ولا لفظ). المحمولُ من الحقول الأربعة، والنسبةُ من الثلاث (`Jisr/Nisab.lean`).
  الأحكام (تعيينُ البنّاء): **ابتداء** = صلاحيةُ الموضوع مسندًا إليه بقانون المالك `Cat.roles` (معنًى في نفسه لا زمانَ بهيئته:
  `harf_la_yubtada`، `fil_la_yubtada`)؛ **وصل** = حكمٌ **ثلاثيّ** على نهج م13 من دستور الوكيل (ثلاثيّتُه: حقيقة / مجازٌ برخصة / لا حكم؛
  وثلاثيّةُ هذه الطبقة: مرخَّص / لا حكم / ممتنع — والمجازُ برخصةٍ مؤجَّلٌ إلى طبقة الحكم فوقها): «ممتنع» إن كانت
  النسبةُ ممّا لا يحتمله المحمول (`nisabMahmul`: الخاصّةُ إسنادٌ أو تقييد، القابليّةُ والفردُ إسناد، العلاقةُ إضافة — تعيينٌ معلَن)، وإلّا
  «مرخَّص» إن كان المحمولُ في حقول الموضوع (الوضع: حقيقة)، وإلّا «لا حكم» (غيابُ الشاهد ليس امتناعًا؛ المجازُ برخصةٍ في طبقة الحكم —
  م10) — `wasl_thulathi`؛ **وقف** = الإفادةُ بالإسناد (المالك `Category`: الكلامُ إسنادٌ أو تعلُّقٌ بمسندٍ مقدَّر)، والقيدُ (تقييديةٌ أو
  إضافية) جزءٌ لا كلام. والضمُّ (`damm`) يرتّب: الممتنعُ ثمّ لا حكم ثمّ الترخيص، ولا يخترع امتناعًا (`damm_mumtani`). **«التقييدية»
  هنا للخاصّة قيدًا (النعت: «الولدُ الصغير»)، وفي `Jisr/Nisab.lean` للمفعولية من أدوار المالك** — النسبةُ واحدة (ج3 721: التقييد)
  والموضعان مختلفان، ولا تبلغ التقييديةُ الطبقةَ الثالثة من خانة المسند (فهو خبرٌ أو فعلٌ أو مجرور).

  **٣. إطارُ الدالّ والمدلول معًا** `Itar3 = (الإطارُ النحويّ الممدود `Mulhaqat.Itar`، كلماتُ الخانات الظاهرة — خانات المالك الظاهرة
  بترتيبها ثمّ الملحقات بترتيبها (النائبُ خانتُه خانةُ المالك، والعاملُ الاسميّ صفةٌ لا كلمة) — بخلاياها `Dal.Kalima`، مدلولاتُها، الإسنادُ
  الدلاليّ)`. **حدُّ الطبقة** (`fiHadd`، معلَن؛ وما خرج عنه «لا حكم» لا «ممتنع»: `kharij_alhadd`): لا إطارَ ثانٍ (التنازع)، ولا ملحقَ
  متقدّمًا (`qabl`) ولا عاملَ اسميًّا (معمولاتُه إطارٌ فرعيّ بلا كلماتٍ هنا) ولا نائبَ مجرورًا، وكلُّ ملحقٍ يرسو على آخر خانةٍ ظاهرة أو على
  ملحق — فترتيبُ الكلمات ترتيبُ النطق؛ والمسندُ والمسندُ إليه ظاهران (المستترُ والمقدَّرُ إحالةٌ في `Maqam` غيرُ مجسورة) أو شبهُ الجملة
  بلا مسندٍ إليه (موضوعُه من المقام، يُعطى في الإسناد ولا يُفحص على كلمة)؛ والأسماءُ المعربة مفردة (الإعرابُ بالحركة على الخلية الأخيرة؛
  المثنّى والجموعُ بالحروف غيرُ مجسورة؛ والأسماءُ الخمسة والمنقوصُ والمقصور لا يُميَّزون بلا معجم: فجوةٌ معلَنة). **ابتداء**: الإطارُ
  النحويّ مرخَّص (`itarOK`)، والكلماتُ بعدد الظواهر، ولكلٍّ مدلول، وأوّلُ الكلمات يُبتدأ بها في صورة ابتدائها، والموضوعُ يصلح مسندًا إليه.
  **وصل**: التركيبُ بإصلاح همزة الوصل ثلاثيًّا (`Dal.rakkib`: ما لا إصلاحَ له عند المالك `Khalal.laHukm` لا حكم، والميّتُ ممتنع —
  `hukmTarkib`)، وكلُّ كلمةٍ مكتملةٌ دالًّا في صورة ابتدائها (`complete'` كما في `SentOK` المالك)، وحالةُ آخر كلّ كلمةٍ معربةٍ ما يطلبه
  موضعُها (`reqState` لخانات المالك، `Mulhaqat.halatAt` للملحقات)، والتنوينُ في الاسم المعرب نونٌ ساكنة بعد حركة الإعراب (قرار القارئ)
  فتُقرأ الحركةُ قبلَه (`halaIrab`) — **وهذان دون `SentOK` المالك: هو يفحص المبنيَّ أيضًا (فيطلب للماضي ضمّةً: `reqState 1 0 2`) ويقرأ
  آخرَ خليةٍ (`lastSt`) فيردّ «ذَهَبَ الْوَلَدُ» و«ذَهَبَ وَلَدٌ» كليهما**، معلَن؛ وقسمُ مدلول كلّ خانةٍ عند المالك (`Cat.kindOfMadlul`) قسمُ خانتها بدورها وأداة الإطار (فعلٌ لدور الفعل وللناسخ الفعليّ كان/ظنّ،
  حرفٌ للأداة في غيرهما وللجارّ، اسمٌ لسواهما — `qismDawr`؛ والملحقاتُ أسماء)؛ وموضوعُ الإسناد مدلولُ المسند إليه الظاهر (المبتدأُ وإلّا
  الفاعل)، ومحمولُه حقيقةُ مدلول المسند الظاهر بجنسه (الفعلُ قابليّة؛ الخبرُ خاصّةٌ أو فردٌ أو قابليّةٌ بوصفٍ مشتقّ؛ والمجرورُ في شبه
  الجملة علاقةٌ إليه — `jinsMahmul`)، ونسبةُ الإسناد نسبةُ خانة المسند بتعيين `Nisab.nisbaOf` على علاقة المالك `semOf` (الجسرُ بين
  التعيينين)، ووصلُ المدلول ثلاثيًّا. **وقف**: السلسلةُ المركَّبة إطارُ دالٍّ مرخَّص (ابتداءً ووصلًا ووقفًا)، والإسنادُ تامٌّ — أو تعلُّقٌ
  (إضافية) في شبه الجملة. **الترخيصُ والحكم** (م10: الحكمُ فوق الترخيص لا فيه): `tarkhis3` كلُّ ما سبق سوى وصل المدلول، و`hukm3`
  ثلاثيٌّ يضمّه إلى حكم الوضع — «لا حكم» خارجَ الحدّ، ويرثه من التركيب ومن وصل المدلول؛ والحكمُ لا يُسقط ترخيصًا (`hukm_la_yusqit_tarkhis`:
  المرخَّصُ في الحدّ لا يكون ممتنعًا — مرخَّصٌ أو لا حكم؛ و`hukm3_murakhkhas`: المرخَّصُ حكمًا = ترخيصٌ في الحدّ مع حقيقة الوضع). **وما
  ردّه إطارُ المالك لأنّه ليس في جدول أطره `framesL` (مفعولان…) «لا حكم» بسبب `laTamthil`** — قرار المالك 2026-10-20 (13:01):
  «لا حكم بسببٍ مسمّى»، وكان قبله ممتنعًا (LC11 من «سجلّ التزامات الإغلاق»). وما ردّه قانونُ سماته `uOK` أو قواعدُ الملحقات بنصّ القطر
  (تابعٌ على غير اسم…) فممتنع: منعٌ بنصّ. **ولكلّ «لا حكم» سببٌ مسمّى** من `SababLaHukm` (`laHukm_bisabab`)؛ ومن الحدّ أيضًا
  `illaAkhir` (الفجوةُ المعلنة أعلاه نُفّذت: الأسماءُ الخمسة والمنقوصُ والمقصور آخرُها حرفُ علّةٍ ساكن) و`mamnuMuhtamal` (فتحةُ الممنوع
  في موضع الجرّ محتملة، كـ`JisrDal.mamnu_fatha`). وما ليس
  هنا (معلَن): قانونُ ابتداء الكلام بين الجمل (`Tarkib.discOK`)، والسماتُ فوق القسم (ومنها الزمنُ ماضيًا/مضارعًا/أمرًا: `Attr.1` لا
  يقابله شيءٌ في الكلمة ولا في المدلول البوليّ `tim`)، والمفاعيلُ الراسية على الفعل تتأخّر عن خانات المالك كلِّها (`yataakhkhar`).
  الاحتواء `itar3_yahtawi` على الترخيص (ومنه ترخيصُ آلة المالك `Msent` للسلسلة المركَّبة عبر `Dal.jumla_murakhkhasa`) و`itar3_yahtawi_hukm`
  على الحكم؛ الرقم `itar3_value`. الشواهد: «ذَهَبَ الْوَلَدُ»، «ذَهَبَ وَلَدٌ»، «فِي الدَّارِ»، «ذَهَبَ الْوَلَدُ مُسْرِعًا»، «كَانَ الْوَلَدُ ذَاهِبًا»، وشواهدُ الحدّ —
  بمدلولاتٍ مبنيّةٍ على نسق المالك (`insan`، `shams`): أمثلةٌ لا مودَع؛ ومعجمُ الأجناس وخواصّها وقابليّاتها مودَعٌ ينتظر.

  الوسم: مبرهن (الاستلزامات، `dal_waqf_kama_yuqra`، الاحتواء، الفكّ، ثلاثُ النِّسَب، ثلاثيّةُ الحكم، حدُّ الطبقة)، ومبرهن على الشاهد
  (decide/decide +kernel على الأمثلة والعدّ — ومنه الاستقلالُ `wasl_waqf_mustaqillan` و`wasl_ghayr_Fwasl`). وأسبابُ «لا حكم» (2026-10-20) بالمعيار الموحَّد (`Nizam/Asas.lean`): 3 لكلّ (`laHukm_bisabab`،
  `la_tamthil_la_hukm`، `mumtani_mumaththal`)، و3 تعريفيّة (`ofBool_ne_laHukm`، `damm_laHukm`، `fiHadd_mumaththal`)، و1 على الشاهد
  (`shahid_asbab`)؛ طفراتها P329–P332. موادُّ دستور الوكيل
  (AGENT_CONSTITUTION.md في Saleh1967/Alghanem — ليس في هذا المستودع؛ نصُّها من خلاصته في مهارة dustur-al-wakil): م10 «الحكمُ فوق
  الترخيص لا فيه»، م13 «الحكمُ ثلاثيٌّ … ولا يُسقط ترخيصًا … لا يُستنتج الامتناع من غياب الشاهد».
-/
import Dal.Jumla
import SLGE.MadlulAwwalan
import SLGE.Category
import Jisr.Mulhaqat
import Jisr.Nisab

set_option synthInstance.maxSize 8192
set_option synthInstance.maxHeartbeats 0
set_option maxRecDepth 100000
set_option autoImplicit false

namespace Jisr
namespace Utur
open SLGE SLGE.Law SLGE.Tarkib SLGE.Simat SLGE.Kull SLGE.Awwalan Dal

/-! ## ١. إطار الدال وحده -/

abbrev ItarDal := List NawMaqta

/-- نمطُ مقاطع السلسلة (خلاياها بأرقامها دون 116)؛ ولا نمطَ للفارغ. -/
def itarDal (l : List Nat) : Option ItarDal := if l.isEmpty then none else (qatta l).map (·.map nawMaqta)

/-- **ابتداء:** الانتقالُ الأوّل من الحالة 0 حيّ. -/
def ibtidaDal (l : List Nat) : Bool := match l with | a :: _ => δ 0 a != 96 | [] => false
/-- **وصل:** السلسلةُ غيرُ فارغة وانتقالاتُها كلُّها حيّة كما تُقرأ. -/
def waslDal (l : List Nat) : Bool := !l.isEmpty && run 0 l != 96
/-- **وقف:** `complete'` المالك — وقفيّةٌ بعد تسكين الآخر. -/
def waqfDal (l : List Nat) : Bool := complete' l

/-- إطارُ الدالّ المرخَّص: الأحكامُ الثلاثة. -/
def dalOK (l : List Nat) : Bool := ibtidaDal l && waslDal l && waqfDal l

/-- **ما يُوصَل ويُوقَف عليه بعد التسكين فحالتُه كما يُقرأ وقفيّة** (من أيّ حالة): بالاستقراء على السلسلة؛ والخليةُ الأخيرة إن كانت
متحرّكةً حيّةً فالحالةُ «بعد متحرّك» `1 + h` (المالك `mover_step`) وهي وقفيّة. -/
theorem waqf_kama_yuqra (l : List Nat) :
    ∀ q, run q l ≠ 96 → Fwaqf (run q (waqfForm l)) = true → Fwaqf (run q l) = true := by
  induction l with
  | nil => intro q _ h; simpa [waqfForm] using h
  | cons a l ih =>
    intro q hr hw
    cases l with
    | nil =>
      by_cases hv : a < 116 ∧ a % 4 < 3
      · simp only [run] at hr ⊢
        rw [mover_step q a hv.1 hv.2 hr]; simp only [Fwaqf, decide_eq_true_eq]; omega
      · simp only [waqfForm, hv, ite_false] at hw; exact hw
    | cons b l =>
      simp only [waqfForm, run] at hw hr ⊢
      exact ih (δ q a) hr hw

/-- **ما رخّصه إطارُ الدالّ فحالتُه كما يُقرأ وقفيّة** — وهو ما تطلبه مبرهنةُ المالك `jumla_murakhkhasa` للجملة. -/
theorem dal_waqf_kama_yuqra (l : List Nat) (h : dalOK l = true) : Fwaqf (run 0 l) = true := by
  unfold dalOK waslDal waqfDal complete' at h
  simp only [Bool.and_eq_true, bne_iff_ne, ne_eq] at h
  exact waqf_kama_yuqra l 0 h.1.2.2 h.2

/-- **الوصلُ يستلزم الابتداء:** ما مات انتقالُه الأوّل ماتت سلسلتُه (المالك `run_dead`). -/
theorem wasl_yastalzim_ibtida (l : List Nat) (h : waslDal l = true) : ibtidaDal l = true := by
  unfold waslDal at h
  cases l with
  | nil => simp at h
  | cons a l =>
    simp only [ibtidaDal, bne_iff_ne, ne_eq]
    intro hc
    simp [run, hc, run_dead] at h

/-- **والوقفُ يستلزم الابتداء:** التسكينُ لا يُحيي انتقالًا أوّلَ ميّتًا — الخليةُ الواحدة المتحرّكة تصير ساكنةً فلا يُبتدأ بها، وما
بعد خليةٍ ميّتةٍ ميّت. -/
theorem waqf_yastalzim_ibtida (l : List Nat) (h : waqfDal l = true) : ibtidaDal l = true := by
  unfold waqfDal complete' at h
  cases l with
  | nil => simp [waqfForm, run, Fwaqf] at h
  | cons a l =>
    simp only [ibtidaDal, bne_iff_ne, ne_eq]
    intro hc
    cases l with
    | nil =>
      by_cases hv : a < 116 ∧ a % 4 < 3
      · have hs : δ 0 (4 * (a / 4) + 3) = 96 := by
          have : ∀ b < 116, b % 4 = 3 → δ 0 b = 96 := by decide
          exact this _ (by omega) (by omega)
        simp [waqfForm, hv.1, hv.2, run, hs, Fwaqf] at h
      · simp [waqfForm, hv, run, hc, Fwaqf] at h
    | cons b l => simp [waqfForm, run, hc, run_dead, Fwaqf] at h

/-- **الوصلُ والوقفُ مستقلّان (على الشاهد):** «لَ» (خليةٌ واحدة) توصَل ولا يوقَف عليها؛ و«لَا» بألفٍ متحرّكةٍ آخرًا (8) يكتملها التسكينُ
(ألفُ مدٍّ بعد الفتحة) وتموت كما تُقرأ (الألفُ لا تتحرّك عند المالك). -/
theorem wasl_waqf_mustaqillan :
    waslDal [52] = true ∧ waqfDal [52] = false ∧ waqfDal [52, 8] = true ∧ waslDal [52, 8] = false := by decide

/-- **«الوصل» هنا غيرُ `Fwasl` المالك (قبولُ متحرّكٍ بعد الآخر):** «بِنْت» حيّةُ الانتقالات ووقفيّةٌ فيرخّصها الإطار، و`Fwasl` يردّها
إن وُصلت (المالك `bint`: «مرخَّصةٌ موقوفًا عليها، ممتنعةٌ إن وُصلت بمتحرّك»؛ حالتُها 35: ساكنان مُغلِقان). -/
theorem wasl_ghayr_Fwasl :
    waslDal [106, 59, 75] = true ∧ waqfDal [106, 59, 75] = true ∧ Fwasl (run 0 [106, 59, 75]) = false := by decide

/-- **لا يُبتدأ بساكن:** الخليةُ الساكنة أوّلًا تُميت الآلة (المالك `nec_vowel`)، فلا نمطَ (`qatta`) ولا ابتداءَ ولا إطار. -/
theorem la_itar_bisakin (a : Nat) (ha : a < 116) (hs : a % 4 = 3) (l : List Nat) :
    itarDal (a :: l) = none ∧ ibtidaDal (a :: l) = false ∧ dalOK (a :: l) = false := by
  have hd : δ 0 a = 96 := by
    have : ∀ b < 116, b % 4 = 3 → δ 0 b = 96 := by decide
    exact this a ha hs
  refine ⟨by simp [itarDal, qatta, qattaRaw, hs], by simp [ibtidaDal, hd], by simp [dalOK, ibtidaDal, hd]⟩

/-- **الإطارُ أضيقُ من `complete'` المالك بالألف المتحرّكة آخرًا:** على السلاسل من خليتين، ما اكتمل عنده ولم يرخّصه الإطارُ
آخرُه ألفٌ متحرّكة (8، 9، 10) — 84 سلسلة من 9,520 مكتملة. -/
theorem dal_vs_complete :
    (List.range 116).all (fun a => (List.range 116).all fun b =>
      !(complete' [a, b] && !dalOK [a, b]) || (b == 8 || b == 9 || b == 10)) = true ∧
    ((List.range 116).map fun a => ((List.range 116).filter fun b => complete' [a, b] && !dalOK [a, b]).length).sum = 84 ∧
    ((List.range 116).map fun a => ((List.range 116).filter fun b => complete' [a, b]).length).sum = 9520 := by decide +kernel

/-- وكلُّ ما رخّصه الإطارُ مكتملٌ عند المالك (بالتعريف: الوقفُ هو `complete'`). -/
theorem dal_yastalzim_complete (l : List Nat) (h : dalOK l = true) : complete' l = true := by
  unfold dalOK waqfDal at h; simp only [Bool.and_eq_true] at h; exact h.2

/-- **استنفادُ أطر الدالّ على الخلية والخليتين:** لا سلسلةَ من خليةٍ (المالك `nec_second`)؛ ومن خليتين الإطارُ والتقطيعُ سواء:
ما رخّصه الإطارُ له نمطٌ وما له نمطٌ رخّصه الإطار. -/
theorem itar_dal_istinfad_2 :
    ((List.range 116).filter fun a => dalOK [a]).length = 0 ∧
    (List.range 116).all (fun a => (List.range 116).all fun b => (itarDal [a, b]).isSome == dalOK [a, b]) = true := by
  decide +kernel

/-- **أنماطُ الخليتين:** كما تُقرأ CV·CV (7056) أو CVV (84) أو CVC (2296) ولا رابع — 9,436 سلسلةً يرخّصها الإطار. -/
theorem itar_dal_anmat_2 :
    (List.range 116).all (fun a => (List.range 116).all fun b =>
      match itarDal [a, b] with
      | none => true
      | some p => p == [.CV, .CV] || p == [.CVV] || p == [.CVC]) = true ∧
    ([[NawMaqta.CV, .CV], [.CVV], [.CVC]].map fun p =>
      ((List.range 116).map fun a => ((List.range 116).filter fun b => itarDal [a, b] == some p).length).sum) =
      [7056, 84, 2296] ∧ 7056 + 84 + 2296 = 9436 := by decide +kernel

/-- شواهدُ النمط: «كِتَاب» CV·CVVC، «بِنْت» CVCC، «ذَهَبَ» CV·CV·CV، «قَالَ» CVV·CV؛ والإطارُ يرخّص «ذَهَبَ» و«قَالَ» و«بِنْت» (وقفًا
بساكنين) ولا يرخّص ما أوّله ساكنٌ أو ألفٌ متحرّكة، ولا الفارغ؛ و«قَالَ» وقفًا CVVC. -/
theorem itar_dal_shawahid :
    itarDal [4 * 8 + 2, 4 * 18 + 0, 4 * 2 + 3, 4 * 26 + 3] = some [.CV, .CVVC] ∧
    itarDal [4 * 26 + 2, 4 * 14 + 3, 4 * 18 + 3] = some [.CVCC] ∧
    itarDal [92, 4, 104] = some [.CV, .CV, .CV] ∧ itarDal [28, 11, 52] = some [.CVV, .CV] ∧
    itarDal (waqfForm [28, 11, 52]) = some [.CVVC] ∧
    dalOK [92, 4, 104] = true ∧ dalOK [28, 11, 52] = true ∧ dalOK [4 * 26 + 2, 4 * 14 + 3, 4 * 18 + 3] = true ∧
    dalOK [11, 28] = false ∧ dalOK [8, 52] = false ∧ dalOK [] = false ∧ waslDal [] = false ∧ itarDal [] = none := by
  decide +kernel

/-! ## ٢. إطار المدلول وحده -/

/-- المحمول: من حقول مدلول المالك الأربعة (خاصّة، علاقة إلى مدلولٍ آخر، قابليّة، فرد). -/
inductive Mahmul
  | khassa (k : Nat) | alaqa (r ila : Nat) | qabiliyya (q : Nat) | fard (f : Nat)
deriving DecidableEq, Repr

structure ItarMadlul where
  mawdu : Madlul
  mahmul : Mahmul
  nisba : Nisab.Nisba
deriving DecidableEq, Repr

/-- الحكمُ الثلاثيّ: مرخَّص، أو لا حكم (غيابُ شاهدٍ لا امتناع)، أو ممتنع. -/
inductive Hukm | murakhkhas | laHukm | mumtani
deriving DecidableEq, Repr

/-- ضمُّ الأحكام: الممتنعُ يغلب، ثمّ لا حكم، ثمّ الترخيص. -/
def damm : Hukm → Hukm → Hukm
  | .mumtani, _ => .mumtani
  | _, .mumtani => .mumtani
  | .laHukm, _ => .laHukm
  | _, .laHukm => .laHukm
  | .murakhkhas, .murakhkhas => .murakhkhas

def ofBool (b : Bool) : Hukm := if b then .murakhkhas else .mumtani

theorem damm_murakhkhas (a b : Hukm) : damm a b = .murakhkhas ↔ a = .murakhkhas ∧ b = .murakhkhas := by
  cases a <;> cases b <;> simp [damm]

/-- **الضمُّ لا يخترع امتناعًا:** الممتنعُ من ممتنعٍ في أحد الطرفين لا غير — فلا يصير «لا حكم» ممتنعًا بالضمّ. -/
theorem damm_mumtani (a b : Hukm) : damm a b = .mumtani ↔ a = .mumtani ∨ b = .mumtani := by
  cases a <;> cases b <;> simp [damm]

theorem ofBool_murakhkhas (b : Bool) : ofBool b = .murakhkhas ↔ b = true := by cases b <;> simp [ofBool]

/-- **ابتداء** (صلاحيةُ المسند إليه): الموضوعُ معنًى في نفسه لا زمانَ بهيئته (المالك `Cat.roles`). -/
def ibtidaMadlul (u : ItarMadlul) : Bool := (SLGE.Cat.roles u.mawdu.ind u.mawdu.tim).1

/-- المحمولُ في حقول الموضوع (الوضع: «حقيقة»). -/
def fiHuqul (m : Madlul) : Mahmul → Bool
  | .khassa k => m.khawass.contains k
  | .alaqa r x => m.alaqat.contains (r, x)
  | .qabiliyya q => m.qabiliyyat.contains q
  | .fard f => m.afrad.contains f

/-- النِّسَبُ التي يحتملها المحمول (تعيينٌ معلَن): الخاصّةُ تُسند أو تقيّد، والقابليّةُ والفردُ يُسندان، والعلاقةُ إضافة. -/
def nisabMahmul : Mahmul → List Nisab.Nisba
  | .khassa _ => [.isnadiyya, .taqyidiyya]
  | .alaqa _ _ => [.idafiyya]
  | .qabiliyya _ => [.isnadiyya]
  | .fard _ => [.isnadiyya]

/-- **وصل** ثلاثيًّا: نسبةٌ لا يحتملها المحمول ← ممتنع؛ وإلّا فالمحمولُ في الحقول ← مرخَّص، وإلّا ← لا حكم. -/
def waslMadlul (u : ItarMadlul) : Hukm :=
  if !(nisabMahmul u.mahmul).contains u.nisba then .mumtani
  else if fiHuqul u.mawdu u.mahmul then .murakhkhas else .laHukm

/-- **وقف:** الإفادةُ بالإسناد (المالك `Category`: الكلامُ إسناد؛ وتعلُّقُ شبه الجملة بمسندٍ مقدَّر يُحكَم في الطبقة الثالثة حيث يُعرَف
نوعُ الإطار، لا هنا). -/
def waqfMadlul (u : ItarMadlul) : Bool := u.nisba == .isnadiyya

/-- القيدُ (تقييدٌ أو إضافة): ابتداءٌ ووصلٌ بلا وقف — جزءُ كلامٍ لا كلام. -/
def hukmQayd (u : ItarMadlul) : Hukm := damm (ofBool (ibtidaMadlul u)) (waslMadlul u)
/-- الإطارُ المدلوليّ التامّ: الأحكامُ الثلاثة. -/
def hukmMadlul (u : ItarMadlul) : Hukm := damm (hukmQayd u) (ofBool (waqfMadlul u))

/-- **لا يُبتدأ بحرف:** ما ليس معنًى في نفسه لا يصلح مسندًا إليه (المالك `Cat.roles`). -/
theorem harf_la_yubtada (u : ItarMadlul) (h : u.mawdu.ind = false) : ibtidaMadlul u = false := by
  simp [ibtidaMadlul, SLGE.Cat.roles, h]

/-- **ولا بفعل:** الزمانُ بهيئته لا يُسند إليه (المالك `Cat.roles`: الدورُ الأوّل `ind && !tim`). -/
theorem fil_la_yubtada (u : ItarMadlul) (h : u.mawdu.tim = true) : ibtidaMadlul u = false := by
  simp [ibtidaMadlul, SLGE.Cat.roles, h]

/-- **لكلّ محمولٍ نسبة؛ والإسنادُ لكلّ محمولٍ غيرِ العلاقة، والعلاقةُ إضافةٌ وحدها.** -/
theorem nisab_mahmul (m : Mahmul) :
    (nisabMahmul m) ≠ [] ∧
    ((nisabMahmul m).contains .isnadiyya ↔ (match m with | .alaqa _ _ => False | _ => True)) ∧
    ((nisabMahmul m).contains .idafiyya ↔ (match m with | .alaqa _ _ => True | _ => False)) := by
  cases m <;> simp [nisabMahmul]

/-- **الحكمُ ثلاثيٌّ لا يُسقط ترخيصًا ولا يخترع امتناعًا (م13):** الامتناعُ من النسبة وحدها، والترخيصُ من الحقول، ولا حكمَ إذا
وفقط إذا احتمل المحمولُ النسبةَ ولم يكن في الحقول — فغيابُ الشاهد ليس امتناعًا. -/
theorem wasl_thulathi (u : ItarMadlul) :
    (waslMadlul u = .mumtani ↔ (nisabMahmul u.mahmul).contains u.nisba = false) ∧
    (waslMadlul u = .murakhkhas ↔ (nisabMahmul u.mahmul).contains u.nisba = true ∧ fiHuqul u.mawdu u.mahmul = true) ∧
    (waslMadlul u = .laHukm ↔ (nisabMahmul u.mahmul).contains u.nisba = true ∧ fiHuqul u.mawdu u.mahmul = false) := by
  unfold waslMadlul
  cases hn : (nisabMahmul u.mahmul).contains u.nisba <;> cases hf : fiHuqul u.mawdu u.mahmul <;> simp

/-- مدلولاتٌ مبنيّة على نسق المالك (`insan`، `shams`): «الولد» (معنًى في نفسه، كلّيّ؛ خاصّتُه 21، وعلاقتُه 1 إلى «الدار» 30،
وقابليّتاه 10 و11)، «ذهب» (حدثٌ بزمانٍ بهيئته، حقيقتُه 10) و«طار» (12)، «الدار» (ذات، 30)، و«في» (أداةٌ لا معنى في نفسها). -/
def walad : Madlul := { haqiqa := 20, khawass := [21], alaqat := [(1, 30)], qabiliyyat := [10, 11], afrad := [1, 1] }
def dhahab : Madlul := { haqiqa := 10, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := true }
def tara : Madlul := { haqiqa := 12, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := true }
def dar : Madlul := { haqiqa := 30, khawass := [31], alaqat := [], qabiliyyat := [], afrad := [1] }
def fi : Madlul := { haqiqa := 40, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], ind := false }

/-- **شواهد المدلول:** «الولدُ ذاهبٌ» (قابليّة 10) إسنادٌ مرخَّص؛ «الولدُ طائرٌ» (قابليّة 12 ليست في حقوله) لا حكم — لا ممتنع؛
«الولدُ الصغيرُ» (خاصّة 21) قيدٌ تقييديّ مرخَّص وليس كلامًا؛ «الولدُ في الدار» (علاقة 1 إلى 30) قيدٌ إضافيّ مرخَّص، وإسنادُ العلاقة
ممتنع؛ ولا يُسند إلى الفعل ولا إلى الحرف؛ و«الإنسانُ ناطقٌ» على مدلول المالك مرخَّص، و«الشمس» تصلح موضوعًا. -/
theorem madlul_shawahid :
    hukmMadlul ⟨walad, .qabiliyya 10, .isnadiyya⟩ = .murakhkhas ∧
    hukmMadlul ⟨walad, .qabiliyya 12, .isnadiyya⟩ = .laHukm ∧ waslMadlul ⟨walad, .qabiliyya 12, .isnadiyya⟩ = .laHukm ∧
    hukmQayd ⟨walad, .khassa 21, .taqyidiyya⟩ = .murakhkhas ∧ hukmMadlul ⟨walad, .khassa 21, .taqyidiyya⟩ = .mumtani ∧
    hukmQayd ⟨walad, .alaqa 1 30, .idafiyya⟩ = .murakhkhas ∧ waslMadlul ⟨walad, .alaqa 1 30, .isnadiyya⟩ = .mumtani ∧
    ibtidaMadlul ⟨dhahab, .khassa 1, .isnadiyya⟩ = false ∧ hukmMadlul ⟨fi, .khassa 1, .isnadiyya⟩ = .mumtani ∧
    hukmMadlul ⟨insan, .khassa 1, .isnadiyya⟩ = .murakhkhas ∧ ibtidaMadlul ⟨shams, .khassa 2, .isnadiyya⟩ = true := by decide

/-! ## ٣. إطار الدال والمدلول معًا -/

/-- الإطارُ الثلاثيّ: الإطارُ النحويّ الممدود، وكلماتُ خاناته الظاهرة بترتيبها (خاناتُ المالك الظاهرة ثمّ الملحقات؛ `Dal.Kalima`: خلايا
بلا همزة الوصل وعلامتُها)، ومدلولُ كلّ كلمة (تصوّرٌ: معلوماتٌ سابقة)، والإسنادُ الدلاليّ. -/
structure Itar3 where
  jisr : Mulhaqat.Itar
  kalimat : List Kalima
  maani : List Madlul
  isnad : ItarMadlul
deriving DecidableEq, Repr

def baseSlots (u : Itar3) : List Slot := u.jisr.ud.f.2.2
def nB (u : Itar3) : Nat := (baseSlots u).length
/-- خاناتُ المالك الظاهرة، ورتَبُ الملحقات الظاهرة في `ml`: كلُّها إلّا النائبَ (خانتُه خانةُ المالك) والعاملَ الاسميّ (صفةٌ على
خانةٍ اسمية لا كلمةٌ). -/
def zawahirBase (u : Itar3) : Nat := (overt (baseSlots u)).length
def zawahirMl (u : Itar3) : List Nat :=
  (List.range u.jisr.ml.length).filter fun j =>
    match u.jisr.ml[j]? with | some m => m.dawr != .naib && m.dawr != .amilIsmi | none => false
def zawahir (u : Itar3) : Nat := zawahirBase u + (zawahirMl u).length
/-- رتبةُ خانة المالك الظاهرة بين الظواهر. -/
def overtIdx (u : Itar3) (i : Nat) : Nat := (((baseSlots u).take i).filter (·.2.1 == 0)).length
/-- خانةُ المسند إليه: المبتدأُ (0) وإلّا الفاعلُ (3)؛ وخانةُ المسند: المجرورُ (6) في شبه الجملة، وإلّا الخبرُ (1) وإلّا الفعلُ (2). -/
def musnadIlayhIdx (u : Itar3) : Option Nat :=
  let rs := roles (baseSlots u)
  if rs.contains 0 then some (rs.idxOf 0) else if rs.contains 3 then some (rs.idxOf 3) else none
def musnadIdx (u : Itar3) : Option Nat :=
  let rs := roles (baseSlots u)
  if u.jisr.ud.f.1 == 2 then (if rs.contains 6 then some (rs.idxOf 6) else none)
  else if rs.contains 1 then some (rs.idxOf 1) else if rs.contains 2 then some (rs.idxOf 2) else none
def madlulOf (u : Itar3) (i : Nat) : Option Madlul :=
  if fillAt (baseSlots u) i == 0 then u.maani[overtIdx u i]? else none
def mahmulHaqiqa : Mahmul → Nat
  | .khassa k => k | .alaqa _ x => x | .qabiliyya q => q | .fard f => f
/-- جنسُ المحمول بخانة المسند: الفعلُ قابليّة؛ الخبرُ خاصّةٌ أو فردٌ أو قابليّة (بوصفٍ مشتقّ)؛ والمجرورُ علاقة. -/
def jinsMahmul : Mahmul → Nat → Bool
  | .qabiliyya _, 2 => true
  | .khassa _, 1 | .fard _, 1 | .qabiliyya _, 1 => true
  | .alaqa _ _, 6 => true
  | _, _ => false
/-- قسمُ الخانة عند المالك من دورها وأداة الإطار: الفعلُ لدور 2 وللأداة 7 إن كانت ناسخًا فعليًّا (كان 1، ظنّ 3: لها زمنٌ عند المالك
`Simat.slotAttrOK`)، والحرفُ للأداة في غيرهما وللجارّ 5، والاسمُ لسواهما. -/
def qismDawr (a r : Nat) : SLGE.Cat.Kind :=
  if r == 2 then .fil else if r == 7 then (if a == 1 || a == 3 then .fil else .harf) else if r == 5 then .harf else .ism
/-- حالةُ الإعراب في آخر الكلمة: التنوينُ في الاسم المعرب نونٌ ساكنة (59) بعد الحركة (قرارُ القارئ) فتُقرأ الحركةُ قبلَه. -/
def halaIrab (ismi : Bool) (w : List Nat) : Nat :=
  match w.reverse with
  | 59 :: a :: _ => if ismi && a % 4 < 3 then a % 4 else 3
  | a :: _ => a % 4
  | [] => 3

/-- **ابتداء:** الإطارُ النحويّ مرخَّص بلا إطارٍ ثانٍ، والكلماتُ بعدد الظواهر ولكلٍّ مدلول وخلاياها خلايا (دون حدّ الكلمة 116)،
وأوّلُ الكلمات يُبتدأ بها، والموضوعُ يصلح مسندًا إليه. -/
def ibtida3 (u : Itar3) : Bool :=
  Mulhaqat.itarOK u.jisr && u.jisr.thani.isNone && u.kalimat.length == zawahir u && u.maani.length == u.kalimat.length &&
  u.kalimat.all (fun w => w.khalaya.all (· < 116)) &&
  (match u.kalimat.head? with | some w => ibtidaDal (ibtida w) | none => false) && ibtidaMadlul u.isnad

/-- خاناتُ المالك الظاهرة: كلمتُها مكتملة، وحالتُها (إن كانت معربة) ما يطلبه موضعُها، وقسمُ مدلولها قسمُ دورها. -/
def waslBase (u : Itar3) : Bool :=
  (List.range (nB u)).all fun i =>
    fillAt (baseSlots u) i != 0 ||
    (let r := Mulhaqat.roleOf u.jisr.ud.f i
     let t := attrAt u.jisr.ud.ats i
     match u.kalimat[overtIdx u i]?, u.maani[overtIdx u i]? with
     | some w, some m =>
       complete' (ibtida w) &&
       (t.2.2.2 || (match reqState u.jisr.ud.f.1 u.jisr.ud.f.2.1 r with
                    | some h => halaIrab (isNom r) w.khalaya == h | none => true)) &&
       SLGE.Cat.kindOfMadlul m == qismDawr u.jisr.ud.f.2.1 r
     | _, _ => false)

/-- حالاتُ الملحق `j` من دوره (`Mulhaqat.halatAt` بوقودٍ يكفي سلسلةَ التوابع كلَّها؛ وفارغُها: لا حالةَ من الدور). -/
def halatMl (u : Itar3) (j : Nat) : List Nat :=
  Mulhaqat.halatAt u.jisr (u.jisr.ml.length + 1) (Mulhaqat.nBase u.jisr + j)

/-- الملحقاتُ الظاهرة: كلمتُها مكتملة، وحالتُها (إن كانت معربة) من حالات دورها، ومدلولُها اسم. -/
def waslMl (u : Itar3) : Bool :=
  (List.range (zawahirMl u).length).all fun k =>
    match (zawahirMl u)[k]? with
    | some j =>
      match u.jisr.ml[j]?, u.kalimat[zawahirBase u + k]?, u.maani[zawahirBase u + k]? with
      | some m, some w, some md =>
        complete' (ibtida w) &&
        (m.t.2.2.2 || (halatMl u j).isEmpty || (halatMl u j).contains (halaIrab true w.khalaya)) &&
        SLGE.Cat.kindOfMadlul md == .ism
      | _, _, _ => false
    | none => false

/-- الجسرُ بين التعيينين: موضوعُ الإسناد مدلولُ المسند إليه الظاهر (ولا يخلو إطارٌ من مسندٍ إليه إلّا شبهُ الجملة: موضوعُه من
المقام)، ونسبتُه نسبةُ خانة المسند الظاهر بتعيين `Nisab.nisbaOf` على علاقة المالك `semOf`، ومحمولُه حقيقةُ مدلول المسند بجنسه. -/
def jisrMadlul (u : Itar3) : Bool :=
  (match musnadIlayhIdx u with
   | some i => (match madlulOf u i with | some m => m == u.isnad.mawdu | none => false)
   | none => u.jisr.ud.f.1 == 2) &&
  (match musnadIdx u with
   | some i =>
     Nisab.nisbaOf (semOf (Mulhaqat.roleOf u.jisr.ud.f i)) == some u.isnad.nisba &&
     (match madlulOf u i with
      | some m => mahmulHaqiqa u.isnad.mahmul == m.haqiqa && jinsMahmul u.isnad.mahmul (Mulhaqat.roleOf u.jisr.ud.f i)
      | none => false)
   | none => false)

/-- حكمُ التركيب ثلاثيًّا من خلل `Dal.rakkib`: همزةُ وصلٍ بعد حالةٍ ليس عند المالك إصلاحٌ لها «لا حكم» لا امتناع؛ والميّتةُ وما لا يوصَل
والفارغةُ ممتنعة. -/
def hukmTarkib (n : Natija) : Hukm :=
  match n.khalal with | none => .murakhkhas | some (.laHukm _) => .laHukm | some _ => .mumtani

/-- **وصل:** التركيبُ بإصلاح المالك (ثلاثيًّا)، وخاناتُ المالك وملحقاتُه بكلماتها وحالاتها وأقسامها، والجسرُ إلى المدلول، ووصلُ
المدلول (ثلاثيًّا). -/
def wasl3 (u : Itar3) : Hukm :=
  damm (hukmTarkib (rakkib u.kalimat)) (damm (ofBool (waslBase u && waslMl u && jisrMadlul u)) (waslMadlul u.isnad))

/-- **وقف:** السلسلةُ المركَّبة إطارُ دالٍّ مرخَّص، والإسنادُ تامٌّ — أو تعلُّقٌ (إضافية) في شبه الجملة (المالك `Category`). -/
def waqf3 (u : Itar3) : Bool :=
  dalOK (rakkib u.kalimat).silsila &&
  (if u.jisr.ud.f.1 == 2 then u.isnad.nisba == .idafiyya else waqfMadlul u.isnad)

/-- آخرُ خانةٍ ظاهرة في إطار المالك. -/
def akhirZahir (u : Itar3) : Option Nat := ((List.range (nB u)).filter fun i => fillAt (baseSlots u) i == 0).getLast?

/-- الملحقاتُ التي تتأخّر عن خانات المالك كلِّها أيًّا كان مرساها (المفاعيلُ على الفعل والحالُ على صاحبها)، فيصيب ترتيبَ النطق وضعُها
بعدها؛ وما سواها (التوابعُ والمضافُ إليه والتمييزُ والمعدود) يلي مرساه فلا يُقبل إلّا على آخر الظواهر أو على ملحق. -/
def yataakhkhar : Mulhaqat.Dawr → Bool
  | .mutlaq | .lahu | .fihi | .maahu | .hal => true
  | _ => false

/-- **الحدُّ المعلَن (أمضاه المالك 2026-10-16):** ما يحكم فيه الإطارُ الثلاثيّ، وما خرج عنه «لا حكم» لا «ممتنع»: لا إطارَ ثانٍ (التنازع)؛ ولا ملحقَ متقدّمًا
(`qabl`) ولا عاملَ اسميًّا (معمولاتُه إطارٌ فرعيّ بلا كلماتٍ هنا) ولا نائبَ مجرورًا (`naibDal 2` يخالف `reqState`)؛ وكلُّ ملحقٍ إمّا
متأخّرٌ بدوره (`yataakhkhar`) وإمّا راسٍ على آخر خانةٍ ظاهرة أو على ملحق — فترتيبُ الكلمات (خانات المالك ثمّ الملحقات بترتيبها) ترتيبُ
النطق؛ والمسندُ والمسندُ إليه ظاهران (المستترُ والمقدَّرُ والضميرُ المتّصل — ملءُ المالك 1 — إحالةٌ في `Maqam` غيرُ مجسورة هنا) أو شبهُ
الجملة بلا مسندٍ إليه؛ والفعلُ المعربُ الظاهر في الفعلية وحدها (في غيرها لا يعيّن إطارُ المالك حالتَه: `reqState … none`)؛ والأسماءُ
المعربة مفردةٌ (`n = 0`: الإعرابُ بالحركة على الخلية الأخيرة؛ المثنّى والجموعُ بالحروف غيرُ مجسورة — والأسماءُ الخمسة والمنقوصُ والمقصور
لا يُميَّزون بلا معجم: فجوةٌ معلَنة). -/
def haddMuallan (u : Itar3) : Bool :=
  u.jisr.thani.isNone &&
  u.jisr.ml.all (fun m => !m.qabl && m.dawr != .amilIsmi && !(m.dawr == .naib && m.naw == 2) &&
    (yataakhkhar m.dawr || some m.marsa == akhirZahir u || m.marsa ≥ nB u) && (m.t.2.2.2 || m.t.2.2.1.2.2 == 0)) &&
  (match musnadIdx u with | some i => fillAt (baseSlots u) i == 0 | none => false) &&
  (match musnadIlayhIdx u with | some i => fillAt (baseSlots u) i == 0 | none => u.jisr.ud.f.1 == 2) &&
  (List.range (nB u)).all (fun i =>
    fillAt (baseSlots u) i != 0 || (attrAt u.jisr.ud.ats i).2.2.2 ||
    (if Mulhaqat.roleOf u.jisr.ud.f i == 2 then u.jisr.ud.f.1 == 1
     else !isNom (Mulhaqat.roleOf u.jisr.ud.f i) || (attrAt u.jisr.ud.ats i).2.2.1.2.2 == 0))

/-! ### أسبابُ «لا حكم» المسمّاة (قرار المالك 2026-10-20، 13:01 بتوقيت عمّان)

قولُ المالك في الجلسة، جوابًا عن سؤال LC11 من «سجلّ التزامات الإغلاق» (مرفقٌ غيرُ مودَع): «لا حكم بسببٍ مسمّى». فما ردّه الإطارُ
لعدم التمثيل لا يُحكم عليه بالامتناع بعد اليوم، ولكلّ «لا حكم» سببٌ مسمًّى (`laHukm_bisabab`). و«عدمُ التمثيل» هنا بحدّه: الإطارُ
ليس في جدول أطر المالك `framesL` (`laTamthil`). أمّا ما يردّه قانونُ سماته `uOK` وقواعدُ الملحقات بنصّ القطر فمنعٌ بنصّ، يبقى ممتنعًا.
ويُضاف إلى الحدّ سببان: فجوةٌ أعلنها الرأسُ ولم يُنفّذها الحدّ — الأسماءُ الخمسة والمنقوصُ والمقصور «لا يُميَّزون بلا معجم» (`illaAkhir`)؛
وفتحةُ الممنوع من الصرف في موضع الجرّ (`mamnuMuhtamal`)، كما يجعلها `JisrDal.mamnu_fatha` محتملةً (نصبًا أو جرًّا) لا معيَّنة.
قبل هذا التعديل: «ذَهَبَ الْفَتَى»، «ذَهَبَ الْقَاضِي»، «فِي أَفْضَلَ» ممتنعة، والإطارُ بمفعولين ممتنع؛ وبعده كلُّها «لا حكم» بسببها
(`shahid_asbab`). وبقي معلَنًا: «فِي أَفْضَلِ» (ممنوعٌ مجرورٌ بالكسرة) مرخَّص — لا يُعرف الممنوعُ من الدالّ بلا معجم؛ والمقصورُ
والمنقوصُ المنوَّنان (فَتًى، قَاضٍ) يُقرأ ما قبل تنوينهما حركةَ إعراب. -/

/-- أسبابُ «لا حكم» في الطبقة الثالثة: أربعةٌ من الحدّ، واثنان من داخله. -/
inductive SababLaHukm
  /-- خارجَ الحدّ المعلَن (`haddMuallan`): إطارٌ ثانٍ، أو ملحقٌ متقدّمٌ أو عاملٌ اسميّ أو نائبٌ مجرور أو ملحقٌ في غير موضع نطقه،
  أو مسندٌ أو مسندٌ إليه غيرُ ظاهر، أو معربٌ غيرُ مفرد، أو فعلٌ معربٌ في غير الفعلية. -/
  | haddMuallan
  /-- الإطارُ ليس في جدول أطر المالك `framesL`: عدمُ تمثيلٍ لا امتناع (LC11). -/
  | laTamthil
  /-- آخرُ كلمةٍ تُطلب حالتُها حرفُ علّةٍ ساكن: الإعرابُ مقدَّرٌ أو بالحرف، لا يُقرأ من الدالّ بلا معجم. -/
  | illaAkhir
  /-- فتحةٌ بلا تنوينٍ ولا أل حيث يُطلب الجرّ ولا تُقبل الفتحة: ممنوعٌ من الصرف محتمل، والبابُ من المعجم. -/
  | mamnuMuhtamal
  /-- همزةُ وصلٍ بعد حالةٍ لا إصلاحَ لها عند المالك (`Khalal.laHukm` في `Dal.rakkib`). -/
  | tarkib
  /-- المحمولُ يحتمل النسبةَ وليس في حقول الموضوع: غيابُ الشاهد (`wasl_thulathi`). -/
  | madlul
deriving DecidableEq, Repr

/-- آخرُ الخلايا حرفُ علّةٍ ساكن: الألف (`kh 2 3` = 11)، أو الياء (`kh 11 3` = 47)، أو الواو (`kh 28 3` = 115). والمنوَّنُ آخرُه
النونُ الساكنة (59) فليس منه. -/
def illaAkhir (w : List Nat) : Bool :=
  match w.reverse with
  | a :: _ => a == 11 || a == 47 || a == 115
  | [] => false

/-- آخرُ الخلايا فتحةٌ بلا تنوين. -/
def fathaAkhir (w : List Nat) : Bool :=
  match w.reverse with
  | a :: _ => a < 116 && a % 4 == 0
  | [] => false

/-- كلُّ كلمةٍ تُطلب حالتُها من موضعها تستوفي `p` بحالاتِ موضعها: خاناتُ المالك الظاهرة غيرُ المبنيّة (`reqState`)، والملحقاتُ
الظاهرة غيرُ المبنيّة ذاتُ الحالات (`halatMl`) — المواضعُ نفسُها التي يفحصها `waslBase` و`waslMl`. -/
def kullMawdi (u : Itar3) (p : List Nat → Kalima → Bool) : Bool :=
  ((List.range (nB u)).all fun i =>
    fillAt (baseSlots u) i != 0 || (attrAt u.jisr.ud.ats i).2.2.2 ||
    (match reqState u.jisr.ud.f.1 u.jisr.ud.f.2.1 (Mulhaqat.roleOf u.jisr.ud.f i), u.kalimat[overtIdx u i]? with
     | some h, some w => p [h] w
     | _, _ => true)) &&
  ((List.range (zawahirMl u).length).all fun k =>
    match (zawahirMl u)[k]? with
    | some j =>
      (match u.jisr.ml[j]?, u.kalimat[zawahirBase u + k]? with
       | some m, some w => m.t.2.2.2 || (halatMl u j).isEmpty || p (halatMl u j) w
       | _, _ => true)
    | none => true)

/-- الإعرابُ لا يمتنع قراءتُه بحرف علّةٍ ساكنٍ آخرًا. -/
def laIllaAkhir (_ : List Nat) (w : Kalima) : Bool := !illaAkhir w.khalaya

/-- ولا بفتحةٍ بلا تنوينٍ ولا أل حيث يُطلب الجرّ ولا تُقبل الفتحة (فالممنوعُ بأل جرُّه كسرة: `JisrDal.mamnu_bi_al`). -/
def laMamnuMuhtamal (hs : List Nat) (w : Kalima) : Bool :=
  !(hs.contains 2 && !hs.contains 0 && fathaAkhir w.khalaya && !w.al)

/-- أسبابُ الخروج عن الحدّ، بترتيبٍ ثابت. -/
def asbabKharij (u : Itar3) : List SababLaHukm :=
  (if haddMuallan u then [] else [.haddMuallan]) ++
  (if framesL.contains u.jisr.ud.f then [] else [.laTamthil]) ++
  (if kullMawdi u laIllaAkhir then [] else [.illaAkhir]) ++
  (if kullMawdi u laMamnuMuhtamal then [] else [.mamnuMuhtamal])

/-- **حدُّ الطبقة:** ما يحكم فيه الإطارُ الثلاثيّ — لا سببَ للخروج عنه. وما خرج عنه «لا حكم» لا «ممتنع» (`kharij_alhadd`). -/
def fiHadd (u : Itar3) : Bool := (asbabKharij u).isEmpty

/-- الإطارُ الثلاثيّ: حكمُه ثلاثيٌّ — «لا حكم» خارجَ الحدّ، ويرث «لا حكم» من التركيب ومن وصل المدلول. -/
def hukm3 (u : Itar3) : Hukm :=
  if fiHadd u then damm (ofBool (ibtida3 u)) (damm (wasl3 u) (ofBool (waqf3 u))) else .laHukm

theorem ibtida3_of_hukm (u : Itar3) (h : hukm3 u ≠ .mumtani) (hf : fiHadd u = true) : ibtida3 u = true := by
  unfold hukm3 at h; simp only [hf, ite_true] at h
  cases hb : ibtida3 u
  · rw [hb] at h; exact absurd ((damm_mumtani _ _).2 (Or.inl rfl)) h
  · rfl

/-- **الترخيصُ دون حكم الوضع** (م10: الحكمُ فوق الترخيص لا فيه): الابتداءُ، والتركيبُ بلا خلل، وخاناتُ المالك وملحقاتُه، والجسرُ،
والوقف — كلُّ ما في الإطار سوى `waslMadlul`. -/
def tarkhis3 (u : Itar3) : Bool :=
  ibtida3 u && (rakkib u.kalimat).khalal.isNone && waslBase u && waslMl u && jisrMadlul u && waqf3 u

theorem hukmTarkib_murakhkhas (n : Natija) : hukmTarkib n = .murakhkhas ↔ n.khalal.isNone = true := by
  unfold hukmTarkib
  cases h : n.khalal with
  | none => simp
  | some k => cases k <;> simp

/-- **الحكمُ المرخَّص = الترخيصُ في الحدّ مع حقيقة الوضع.** -/
theorem hukm3_murakhkhas (u : Itar3) :
    hukm3 u = .murakhkhas ↔ fiHadd u = true ∧ tarkhis3 u = true ∧ waslMadlul u.isnad = .murakhkhas := by
  unfold hukm3 wasl3 tarkhis3 hukmTarkib
  cases fiHadd u <;> cases ibtida3 u <;> cases waslBase u <;> cases waslMl u <;> cases jisrMadlul u <;> cases waqf3 u <;>
    cases waslMadlul u.isnad <;>
    (cases hk : (rakkib u.kalimat).khalal with
      | none => simp [damm, ofBool]
      | some k => cases k <;> simp [damm, ofBool])

/-- **الحكمُ لا يُسقط ترخيصًا (م13):** ما رُخِّص في الحدّ، ونسبتُه ممّا يحتمله محمولُه، لا يصير ممتنعًا بحكم الوضع — مرخَّصٌ إن كان
المحمولُ في حقول الموضوع، وإلّا لا حكم؛ فالامتناعُ من الترخيص (الدالّ والنحو والجسر) أو من النسبة، لا من غياب الشاهد. -/
theorem hukm_la_yusqit_tarkhis (u : Itar3) (hf : fiHadd u = true) (ht : tarkhis3 u = true)
    (hn : (nisabMahmul u.isnad.mahmul).contains u.isnad.nisba = true) : hukm3 u ≠ .mumtani := by
  unfold hukm3; simp only [hf, ite_true]
  unfold tarkhis3 at ht; simp only [Bool.and_eq_true] at ht
  obtain ⟨⟨⟨⟨⟨hi, hk⟩, hb⟩, hm⟩, hj⟩, hq⟩ := ht
  have hT : hukmTarkib (rakkib u.kalimat) = .murakhkhas := (hukmTarkib_murakhkhas _).2 hk
  have hW : waslMadlul u.isnad ≠ .mumtani := fun hc => by
    have h0 := (wasl_thulathi u.isnad).1.1 hc; rw [h0] at hn; exact Bool.false_ne_true hn
  unfold wasl3; rw [hi, hT, hb, hm, hj, hq]
  cases hw : waslMadlul u.isnad
  · decide
  · decide
  · exact absurd hw hW

theorem fiHadd_of_hukm (u : Itar3) (h : hukm3 u ≠ .laHukm) : fiHadd u = true := by
  unfold hukm3 at h
  cases hf : fiHadd u
  · rw [hf] at h; exact absurd rfl h
  · rfl

/-- **الحكمُ خارجَ الحدّ «لا حكم» لا «ممتنع»** — الغيابُ عن الطبقة ليس امتناعًا (م13). -/
theorem kharij_alhadd (u : Itar3) (h : fiHadd u = false) : hukm3 u = .laHukm := by
  unfold hukm3; rw [h]; rfl

/-- أسبابُ «لا حكم» من داخل الحدّ: التركيبُ، ووصلُ المدلول. -/
def asbabDakhil (u : Itar3) : List SababLaHukm :=
  (if hukmTarkib (rakkib u.kalimat) == .laHukm then [.tarkib] else []) ++
  (if waslMadlul u.isnad == .laHukm then [.madlul] else [])

/-- أسبابُ «لا حكم» للإطار الثلاثيّ: أسبابُ الخروج إن خرج عن الحدّ، وإلّا أسبابُ داخله. -/
def asbabLaHukm (u : Itar3) : List SababLaHukm := if fiHadd u then asbabDakhil u else asbabKharij u

theorem ofBool_ne_laHukm (b : Bool) : ofBool b ≠ .laHukm := by cases b <;> simp [ofBool]

/-- **الضمُّ لا يخترع «لا حكم»:** لا حكمَ من الضمّ إلّا من «لا حكم» في أحد الطرفين. -/
theorem damm_laHukm (a b : Hukm) (h : damm a b = .laHukm) : a = .laHukm ∨ b = .laHukm := by
  cases a <;> cases b <;> simp_all [damm]

/-- **لا «لا حكم» بلا سببٍ مسمّى** (قرار المالك 2026-10-20، LC11): كلُّ إطارٍ ثلاثيّ حكمُه «لا حكم» له سببٌ واحدٌ على الأقلّ من
`SababLaHukm`. -/
theorem laHukm_bisabab (u : Itar3) (h : hukm3 u = .laHukm) : asbabLaHukm u ≠ [] := by
  unfold asbabLaHukm
  cases hf : fiHadd u
  · simp only [Bool.false_eq_true, ite_false]
    intro he
    unfold fiHadd at hf
    rw [he] at hf
    exact absurd hf (by decide)
  · simp only [ite_true]
    unfold hukm3 at h
    rw [hf] at h
    simp only [ite_true] at h
    rcases damm_laHukm _ _ h with h1 | h1
    · exact absurd h1 (ofBool_ne_laHukm _)
    · rcases damm_laHukm _ _ h1 with h2 | h2
      · unfold wasl3 at h2
        rcases damm_laHukm _ _ h2 with h3 | h3
        · simp [asbabDakhil, h3]
        · rcases damm_laHukm _ _ h3 with h4 | h4
          · exact absurd h4 (ofBool_ne_laHukm _)
          · simp [asbabDakhil, h4]
      · exact absurd h2 (ofBool_ne_laHukm _)

/-- ما في الحدّ إطارُه في جدول أطر المالك. -/
theorem fiHadd_mumaththal (u : Itar3) (h : fiHadd u = true) : framesL.contains u.jisr.ud.f = true := by
  unfold fiHadd asbabKharij at h
  cases hc : framesL.contains u.jisr.ud.f
  · simp at h
    have hm : framesL.contains u.jisr.ud.f = true := by simpa using h.2.1
    rw [hc] at hm
    exact absurd hm (by decide)
  · rfl

/-- **عدمُ التمثيل «لا حكم» بسببه (LC11):** إطارٌ ليس في جدول أطر المالك لا يُحكم عليه بالامتناع — حكمُه «لا حكم»، وسببُه
`laTamthil`. -/
theorem la_tamthil_la_hukm (u : Itar3) (h : framesL.contains u.jisr.ud.f = false) :
    hukm3 u = .laHukm ∧ SababLaHukm.laTamthil ∈ asbabLaHukm u := by
  have hf : fiHadd u = false := by
    cases hh : fiHadd u
    · rfl
    · have := fiHadd_mumaththal u hh
      rw [h] at this
      exact absurd this (by decide)
  refine ⟨kharij_alhadd u hf, ?_⟩
  have hm : u.jisr.ud.f ∉ framesL := by simpa using h
  unfold asbabLaHukm asbabKharij
  simp [hf, hm]

/-- **ولا امتناعَ إلّا على إطارٍ ممثَّل.** -/
theorem mumtani_mumaththal (u : Itar3) (h : hukm3 u = .mumtani) : framesL.contains u.jisr.ud.f = true :=
  fiHadd_mumaththal u (fiHadd_of_hukm u (by rw [h]; decide))

/-- **الاحتواء (على الترخيص):** الإطارُ الثلاثيّ المرخَّص يحتوي أطرَ طبقاته الدالّةَ والنحويّة: الإطارُ النحويّ مرخَّص، والتركيبُ بلا
خلل، وسلسلةُ الكلمات المركَّبة إطارُ دالٍّ مرخَّص، وتركيبُها مرخَّصٌ بآلة المالك `Msent` وله تقطيعٌ كلماتٍ ومقاطعَ (`jumla_murakhkhasa`؛
شرطُها — خلايا الكلمات دون 116 — من الابتداء). -/
theorem itar3_yahtawi (u : Itar3) (ht : tarkhis3 u = true) :
    Mulhaqat.itarOK u.jisr = true ∧ (rakkib u.kalimat).khalal = none ∧ dalOK (rakkib u.kalimat).silsila = true ∧
    Msent.Lic 0 (rakkib u.kalimat).silsila ∧ ∃ S, ValidS S ∧ sentChain S = (rakkib u.kalimat).silsila := by
  unfold tarkhis3 at ht; simp only [Bool.and_eq_true] at ht
  obtain ⟨⟨⟨⟨⟨hi, hk⟩, -⟩, -⟩, -⟩, hq⟩ := ht
  unfold ibtida3 at hi; simp only [Bool.and_eq_true] at hi
  have hws : ∀ w ∈ u.kalimat, ∀ a ∈ w.khalaya, a < 116 := by
    intro w hw a ha
    have h1 := List.all_eq_true.mp hi.1.1.2 w hw
    have h2 := List.all_eq_true.mp h1 a ha
    simpa using h2
  unfold waqf3 at hq; simp only [Bool.and_eq_true] at hq
  refine ⟨hi.1.1.1.1.1.1, Option.isNone_iff_eq_none.mp hk, hq.1,
    jumla_murakhkhasa u.kalimat hws (dal_waqf_kama_yuqra _ hq.1)⟩

/-- **والاحتواءُ على الحكم:** الإطارُ الثلاثيّ المحكومُ بالترخيص في الحدّ، والقيدُ الدلاليّ مرخَّص، والإسنادُ تامٌّ في غير شبه الجملة. -/
theorem itar3_yahtawi_hukm (u : Itar3) (h : hukm3 u = .murakhkhas) :
    fiHadd u = true ∧ tarkhis3 u = true ∧ hukmQayd u.isnad = .murakhkhas ∧
    (u.jisr.ud.f.1 ≠ 2 → hukmMadlul u.isnad = .murakhkhas) := by
  obtain ⟨hf, ht, hm⟩ := (hukm3_murakhkhas u).1 h
  have ht' := ht
  unfold tarkhis3 at ht'; simp only [Bool.and_eq_true] at ht'
  obtain ⟨⟨⟨⟨⟨hi, -⟩, -⟩, -⟩, -⟩, hq⟩ := ht'
  unfold ibtida3 at hi; simp only [Bool.and_eq_true] at hi
  unfold waqf3 at hq; simp only [Bool.and_eq_true] at hq
  refine ⟨hf, ht, ?_, ?_⟩
  · unfold hukmQayd; rw [hi.2, hm]; rfl
  · intro h2
    unfold hukmMadlul hukmQayd; rw [hi.2, hm]
    have hwq : waqfMadlul u.isnad = true := by
      have := hq.2
      cases hc : (u.jisr.ud.f.1 == 2)
      · rw [hc] at this; simpa using this
      · exact absurd (beq_iff_eq.mp hc) h2
    rw [hwq]; rfl

/-! ### الشواهد: «ذَهَبَ الْوَلَدُ»، «ذَهَبَ وَلَدٌ»، «فِي الدَّارِ» -/

def dhahaba : Kalima := ⟨[92, 4, 104], false, false⟩           -- ذَهَبَ (ذ=23 ه=1 ب=26)
def alWalad : Kalima := ⟨[55, 112, 52, 69], true, true⟩        -- الْوَلَدُ (ل=13 و=28 د=17؛ همزة الوصل تُزاد في الابتداء)
def waladun : Kalima := ⟨[112, 52, 69, 59], false, false⟩      -- وَلَدٌ (التنوين نونٌ ساكنة)
def fiK : Kalima := ⟨[4 * 25 + 2, 4 * 11 + 3], false, false⟩   -- فِي (ف=25 ي=11)
def adDar : Kalima := ⟨[4 * 17 + 3, 4 * 17 + 0, 4 * 2 + 3, 4 * 15 + 2], true, true⟩  -- الدَّارِ (اللامُ مدغمة: دْ دَ ا رِ؛ د=17 ر=15)

def dhahabaAlWalad : Itar3 :=
  { jisr := { ud := Mulhaqat.darabaZayd }, kalimat := [dhahaba, alWalad], maani := [dhahab, walad],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

def dhahabaWaladun : Itar3 :=
  { jisr := { ud := Mulhaqat.jaaRajul }, kalimat := [dhahaba, waladun], maani := [dhahab, walad],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

def fiDar : Itar3 :=
  { jisr := { ud := Mulhaqat.bikam }, kalimat := [fiK, adDar], maani := [fi, dar],
    isnad := ⟨walad, .alaqa 1 30, .idafiyya⟩ }

def kana : Kalima := ⟨[4 * 8 + 0, 4 * 2 + 3, 4 * 14 + 0], false, false⟩   -- كَانَ (ك=8 ن=14)
def dhahiban : Kalima := ⟨[92, 11, 4 * 1 + 2, 104, 59], false, false⟩     -- ذَاهِبًا (ه=1؛ التنوين نونٌ ساكنة)
def hajj : Kalima := ⟨[16, 11, 39], false, false⟩                        -- حَاجْ (شاهد المالك: مدٌّ ثمّ ساكنٌ معلَّق)
def taraK : Kalima := ⟨[4 * 16 + 0, 11, 4 * 15 + 0], false, false⟩       -- طَارَ (ط=16 ر=15)
def dhahaban : Kalima := ⟨[92, 4, 11, 104, 59], false, false⟩            -- ذَهَابًا
def yadhhaba : Kalima := ⟨[4 * 11 + 0, 95, 4, 104], false, false⟩         -- يَذْهَبَ (ي=11؛ بَ آخرًا نصبًا)
def qumtuK : Kalima := ⟨[29, 111, 73], false, false⟩                     -- قُمْتُ (ق=7 م=27 ت=18)
def dhahabM : Madlul := { haqiqa := 10, khawass := [], alaqat := [], qabiliyyat := [], afrad := [] }   -- الذهابُ مصدرًا (اسم)
/-- «الْوَلَدُ يَذْهَبُ»: إطارُ المالك الاسميّ بخبرٍ جملةٍ فعلية (المضارعُ معرب، فاعلُه مستتر). -/
def alWaladYadhhab : UD :=
  { pre := [], f := (0, 0, [(0, 0, 0), (2, 0, 0), (3, 1, 1)]), ats := [noun 1 0 0, mudari 0 0, pron 3 0 0], ex := [e0, e0, e0] }
def kawn : Madlul := { haqiqa := 60, khawass := [], alaqat := [], qabiliyyat := [], afrad := [], tim := true }
def dhahib : Madlul := { haqiqa := 10, khawass := [], alaqat := [], qabiliyyat := [], afrad := [] }

/-- «كَانَ الْوَلَدُ ذَاهِبًا»: إطارُ المالك الاسميّ بالناسخ كان (الأداة 1)، سماتُه كما في مبرهنة المالك `Simat.zaman` (كان ماضٍ مبنيّ). -/
def kanaUD : UD :=
  { pre := [], f := (0, 1, [(7, 0, 0), (0, 0, 0), (1, 0, 0)]), ats := [(0, 9, (0, 0, 0), true), noun 1 0 0, noun 0 0 0],
    ex := [e0, e0, e0] }
def kanaAlWalad : Itar3 :=
  { jisr := { ud := kanaUD }, kalimat := [kana, alWalad, dhahiban], maani := [kawn, walad, dhahib],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

/-- **«ذَهَبَ الْوَلَدُ» على الطبقات الثلاث:** الإطارُ النحويّ فعلٌ وفاعل، والكلمتان تركّبتا بسقوط همزة الوصل بلا إصلاح (بعد متحرّك)،
والفاعلُ مرفوعٌ بضمّته، وقسمُ «ذهب» فعلٌ وقسمُ «الولد» اسمٌ عند المالك، والذهابُ قابليّةٌ للولد حقيقةً؛ ونمطُ الجملة
CV·CV·CVC·CV·CV·CV. و«ذَهَبَ وَلَدٌ» بالتنوين كذلك (بحدّ الكلمة 116). **وما يُخلّ:** «ذَهَبَ الْوَلَدَ» (نصبُ الفاعل: ممتنع)، و«طَارَ الْوَلَدُ»
بمدلول «طار» (قابليّة 12 ليست في حقول الولد: لا حكم — لا ممتنع)، وموضوعٌ غيرُ مدلول الفاعل (ممتنع)، ومدلولُ الفعل بلا زمانٍ بهيئته
(ممتنع)، ومحمولٌ خاصّةً عن فعل (ممتنع)، وكلمةٌ واحدة (ممتنع). -/
theorem shahid_dhahaba_alwalad :
    hukm3 dhahabaAlWalad = .murakhkhas ∧ hukm3 dhahabaWaladun = .murakhkhas ∧
    (rakkib [dhahaba, alWalad]).silsila = [92, 4, 104, 55, 112, 52, 69] ∧ (rakkib [dhahaba, alWalad]).islahat = [(2, .la)] ∧
    (rakkib [dhahaba, waladun]).silsila = [92, 4, 104, 116, 112, 52, 69, 59] ∧
    (qattaJumla [92, 4, 104, 55, 112, 52, 69]).map (·.map (·.map nawMaqta)) = some [[.CV, .CV, .CVC, .CV, .CV, .CV]] ∧
    hukm3 { dhahabaAlWalad with kalimat := [dhahaba, ⟨[55, 112, 52, 68], true, true⟩] } = .mumtani ∧
    hukm3 { dhahabaAlWalad with kalimat := [taraK, alWalad], maani := [tara, walad], isnad := ⟨walad, .qabiliyya 12, .isnadiyya⟩ }
      = .laHukm ∧
    hukm3 { dhahabaAlWalad with isnad := ⟨insan, .qabiliyya 10, .isnadiyya⟩ } = .mumtani ∧
    hukm3 { dhahabaAlWalad with maani := [{ dhahab with tim := false }, walad] } = .mumtani ∧
    hukm3 { dhahabaAlWalad with isnad := ⟨walad, .khassa 10, .isnadiyya⟩ } = .mumtani ∧
    hukm3 { dhahabaAlWalad with kalimat := [dhahaba], maani := [dhahab] } = .mumtani := by decide +kernel

/-- **«فِي الدَّارِ» شبهُ جملة:** تعلُّقٌ بمسندٍ مقدَّر، علاقتُه عند المالك «تعلّق» (`semOf 6 = 5`) وتعيينُها إضافيةً قرارُ `Nisab.nisbaOf`،
ومحمولُه علاقةٌ إلى مدلول المجرور، وموضوعُه من المقام («الولدُ في الدار») — مرخَّص؛ والتركيبُ بحذف المدّ عند همزة الوصل، والمجرورُ
بكسرته؛ وبنسبةٍ إسنادية ممتنع (لا إسنادَ في شبه الجملة)؛ وبجرّ المجرور ضمّةً ممتنع. و«ذَهَبَ الْوَلَدُ» بنسبةٍ تقييدية ممتنع. -/
theorem shahid_fi_dar :
    hukm3 fiDar = .murakhkhas ∧
    (rakkib [fiK, adDar]).silsila = [102, 71, 68, 11, 62] ∧ (rakkib [fiK, adDar]).islahat = [(2, .hadhfMadd)] ∧
    hukm3 { fiDar with isnad := ⟨walad, .alaqa 1 30, .isnadiyya⟩ } = .mumtani ∧
    hukm3 { fiDar with kalimat := [fiK, ⟨[4 * 17 + 3, 4 * 17 + 0, 4 * 2 + 3, 4 * 15 + 1], true, true⟩] } = .mumtani ∧
    hukm3 { dhahabaAlWalad with isnad := ⟨walad, .qabiliyya 10, .taqyidiyya⟩ } = .mumtani := by decide +kernel

def musrian : Kalima := ⟨[4 * 27 + 1, 4 * 20 + 3, 4 * 15 + 2, 4 * 3 + 0, 59], false, false⟩  -- مُسْرِعًا (م=27 س=20 ر=15 ع=3؛ التنوين نونٌ ساكنة)
def musri : Madlul := { haqiqa := 50, khawass := [], alaqat := [], qabiliyyat := [], afrad := [] }

/-- «ذَهَبَ الْوَلَدُ مُسْرِعًا»: الحالُ ملحقٌ (`Mulhaqat.Dawr.hal`) يرسو على الفاعل، كلمتُه ثالثةُ الكلمات. -/
def dhahabaAlWaladMusrian : Itar3 :=
  { jisr := { ud := Mulhaqat.darabaZayd, ml := [{ dawr := .hal, marsa := 1, t := noun 0 0 0 }] },
    kalimat := [dhahaba, alWalad, musrian], maani := [dhahab, walad, musri], isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

/-- **الملحقُ بكلمته:** «ذَهَبَ الْوَلَدُ مُسْرِعًا» مرخَّص — الحالُ منصوبٌ بفتحته قبل التنوين (`Mulhaqat.halatAt`: [0])، ومدلولُه اسم؛
و«مُسْرِعٌ» مرفوعًا ممتنع، وبلا كلمةٍ للحال ممتنع (الكلماتُ بعدد الظواهر)، وبمدلولٍ ذي زمانٍ للحال ممتنع. و«ذَهَبَ الْوَلَدُ ذَهَابًا»
المفعولُ المطلق يرسو على الفعل ويتأخّر عن الفاعل (`yataakhkhar`) — مرخَّص. -/
theorem shahid_hal :
    hukm3 dhahabaAlWaladMusrian = .murakhkhas ∧
    (rakkib [dhahaba, alWalad, musrian]).silsila = [92, 4, 104, 55, 112, 52, 69, 116, 109, 83, 62, 12, 59] ∧
    hukm3 { dhahabaAlWaladMusrian with kalimat := [dhahaba, alWalad, ⟨[109, 83, 62, 13, 59], false, false⟩] } = .mumtani ∧
    hukm3 { dhahabaAlWaladMusrian with kalimat := [dhahaba, alWalad], maani := [dhahab, walad] } = .mumtani ∧
    hukm3 { dhahabaAlWaladMusrian with maani := [dhahab, walad, { musri with tim := true }] } = .mumtani ∧
    hukm3 { dhahabaAlWaladMusrian with
            jisr := { ud := Mulhaqat.darabaZayd, ml := [{ dawr := .mutlaq, marsa := 0, t := noun 0 0 0 }] },
            kalimat := [dhahaba, alWalad, dhahaban], maani := [dhahab, walad, dhahabM] } = .murakhkhas := by decide +kernel

/-- **الناسخُ الفعليّ فعلٌ:** «كَانَ الْوَلَدُ ذَاهِبًا» مرخَّص — الأداةُ كان بزمنٍ عند المالك فقسمُها فعل (`qismDawr`)، واسمُها مرفوع
وخبرُها منصوبٌ بفتحته قبل التنوين، ومحمولُه قابليّةُ الذهاب (الخبرُ وصفٌ مشتقّ: معلَنٌ بلا فحصٍ للاشتقاق في الكود)؛ وبمدلولٍ لكان بلا
زمان ممتنع. -/
theorem shahid_kana :
    hukm3 kanaAlWalad = .murakhkhas ∧
    (rakkib [kana, alWalad, dhahiban]).silsila = [32, 11, 56, 55, 112, 52, 69, 116, 92, 11, 6, 104, 59] ∧
    hukm3 { kanaAlWalad with maani := [{ kawn with tim := false }, walad, dhahib] } = .mumtani := by decide +kernel

/-- **خارجَ الحدّ «لا حكم» لا «ممتنع»:** «ذَهَبَ» بفاعلٍ مستتر و«قُمْتُ» بالضمير المتّصل (الموضوعُ إحالةٌ في المقام)، والحالُ المتقدّم
(`qabl`)، والفاعلُ المثنّى (الإعرابُ بالحروف)، و«الْوَلَدُ يَذْهَبَ» (المضارعُ خبرًا: لا يعيّن إطارُ المالك حالتَه) — كلُّها لا حكم؛ و«حَاجْ»
ثمّ همزةُ وصلٍ بعد مدٍّ وساكنٍ معلَّق لا إصلاحَ لها عند المالك (`Khalal.laHukm`) فلا حكم. -/
theorem shahid_hadd :
    hukm3 { jisr := { ud := Mulhaqat.darabaMudmar }, kalimat := [dhahaba], maani := [dhahab],
            isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ } = .laHukm ∧
    hukm3 { jisr := { ud := Mulhaqat.qumtu }, kalimat := [qumtuK], maani := [dhahab],
            isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ } = .laHukm ∧
    hukm3 { jisr := { ud := alWaladYadhhab }, kalimat := [alWalad, yadhhaba], maani := [walad, dhahab],
            isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ } = .laHukm ∧
    hukm3 { dhahabaAlWaladMusrian with
            jisr := { ud := Mulhaqat.darabaZayd, ml := [{ dawr := .hal, marsa := 1, t := noun 0 0 0, qabl := true }] } } = .laHukm ∧
    hukm3 { dhahabaAlWalad with jisr := { ud := { Mulhaqat.darabaZayd with ats := [past 0 0, noun 1 0 1] } } } = .laHukm ∧
    (rakkib [hajj, alWalad]).khalal = some (.laHukm 2) ∧
    hukm3 { dhahabaAlWalad with kalimat := [hajj, alWalad] } = .laHukm := by decide +kernel

def alFata : Kalima := ⟨[55, 4 * 25 + 0, 4 * 18 + 0, 4 * 2 + 3], true, true⟩                   -- الْفَتَى (ف=25 ت=18؛ ى ألفٌ ساكنة)
def alQadi : Kalima := ⟨[55, 4 * 7 + 0, 4 * 2 + 3, 4 * 12 + 2, 4 * 11 + 3], true, true⟩         -- الْقَاضِي (ق=7 ض=12 ي=11)
def afdala : Kalima := ⟨[4 * 0 + 0, 4 * 25 + 3, 4 * 12 + 0, 4 * 13 + 0], false, false⟩        -- أَفْضَلَ (ء=0 ل=13)
def afdali : Kalima := ⟨[4 * 0 + 0, 4 * 25 + 3, 4 * 12 + 0, 4 * 13 + 2], false, false⟩        -- أَفْضَلِ
def adDara : Kalima := ⟨[4 * 17 + 3, 4 * 17 + 0, 4 * 2 + 3, 4 * 15 + 0], true, true⟩          -- الدَّارَ (بأل وفتحة)
def alWaladaK : Kalima := ⟨[55, 112, 52, 68], true, true⟩                                    -- الْوَلَدَ
/-- فعلٌ وفاعلٌ ومفعولان: إطارٌ ليس في جدول أطر المالك `framesL`. -/
def mafulaynUD : UD := { pre := [], f := (1, 0, [(2, 0, 0), (3, 0, 0), (4, 0, 0), (4, 0, 0)]), ats := [past 0 0, noun 1 0 0, noun 1 0 0, noun 1 0 0], ex := [e0, e0, e0, e0] }
/-- «طَارَ الْوَلَدُ» (قابليّةُ الطيران ليست في حقول الولد)، و«ذَهَبَ» بفاعلٍ مستتر. -/
def taraAlWalad : Itar3 := { dhahabaAlWalad with kalimat := [taraK, alWalad], maani := [tara, walad], isnad := ⟨walad, .qabiliyya 12, .isnadiyya⟩ }
def dhahabaMudmar : Itar3 := { jisr := { ud := Mulhaqat.darabaMudmar }, kalimat := [dhahaba], maani := [dhahab], isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }
def bimafulayn : Itar3 :=
  { jisr := { ud := mafulaynUD },
    kalimat := [dhahaba, alWalad, alWaladaK, alWaladaK], maani := [dhahab, walad, walad, walad],
    isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }

/-- **«لا حكم» بسببه** (قرار المالك 2026-10-20، 13:01؛ LC11). كانت الأربعةُ الأولى ممتنعةً على ca5ed3c (مخرجُ `#eval` في الجلسة):
- «ذَهَبَ الْفَتَى»، «ذَهَبَ الْقَاضِي»: آخرُ الفاعل حرفُ علّةٍ ساكن — `illaAkhir`.
- «فِي أَفْضَلَ»: فتحةٌ بلا تنوينٍ ولا أل في موضع الجرّ — `mamnuMuhtamal`.
- فعلٌ وفاعلٌ ومفعولان: ليس في `framesL` — `laTamthil`.
- «طَارَ الْوَلَدُ» — `madlul`؛ و«حَاجْ» ثمّ همزةُ الوصل — `tarkib`؛ والفاعلُ المستتر — `haddMuallan`؛ و«ذَهَبَ الْوَلَدُ» المرخَّص بلا سبب.

**وما بقي كما كان:** «فِي الدَّارَ» بأل وفتحة ممتنع؛ و«فِي أَفْضَلِ» (ممنوعٌ مجرورٌ بالكسرة) مرخَّص — حدٌّ معلَن: الممنوعُ لا يُعرف من
الدالّ بلا معجم. والمدلولاتُ في الأمثلة الثلاثة الأولى مستعارةٌ من «ذَهَبَ الْوَلَدُ» و«فِي الدَّارِ»: الحكمُ فيها من الحدّ قبل المدلول. -/
theorem shahid_asbab :
    hukm3 { dhahabaAlWalad with kalimat := [dhahaba, alFata] } = .laHukm ∧
    asbabLaHukm { dhahabaAlWalad with kalimat := [dhahaba, alFata] } = [.illaAkhir] ∧
    hukm3 { dhahabaAlWalad with kalimat := [dhahaba, alQadi] } = .laHukm ∧
    asbabLaHukm { dhahabaAlWalad with kalimat := [dhahaba, alQadi] } = [.illaAkhir] ∧
    hukm3 { fiDar with kalimat := [fiK, afdala] } = .laHukm ∧
    asbabLaHukm { fiDar with kalimat := [fiK, afdala] } = [.mamnuMuhtamal] ∧
    hukm3 { fiDar with kalimat := [fiK, afdali] } = .murakhkhas ∧
    hukm3 { fiDar with kalimat := [fiK, adDara] } = .mumtani ∧
    hukm3 bimafulayn = .laHukm ∧ asbabLaHukm bimafulayn = [.laTamthil] ∧
    asbabLaHukm taraAlWalad = [.madlul] ∧
    asbabLaHukm { dhahabaAlWalad with kalimat := [hajj, alWalad] } = [.tarkib] ∧
    asbabLaHukm dhahabaMudmar = [.haddMuallan] ∧
    asbabLaHukm dhahabaAlWalad = [] := by decide +kernel

/-! ## الرقم: الطبقاتُ الثلاث في عددٍ واحد -/

def kalimaCode (w : Kalima) : Nat := pair (encS w.khalaya) (pair (Muwahhad.bCode w.wasl) (Muwahhad.bCode w.al))

theorem kalimaCode_inj (w v : Kalima) (h : kalimaCode w = kalimaCode v) : w = v := by
  obtain ⟨k, a, b⟩ := w; obtain ⟨k', a', b'⟩ := v
  unfold kalimaCode at h
  obtain ⟨h1, h⟩ := pair_injective h
  obtain ⟨h2, h3⟩ := pair_injective h
  simp only at h1 h2 h3
  rw [encS_inj _ _ h1, bCode_inj _ _ h2, bCode_inj _ _ h3]

def madlulCode (m : Madlul) : Nat :=
  pair m.haqiqa (pair (encS m.khawass) (pair (encS (m.alaqat.map fun p => pair p.1 p.2))
    (pair (encS m.qabiliyyat) (pair (encS m.afrad) (pair (Muwahhad.bCode m.yamnaShirka)
      (pair (Muwahhad.bCode m.ind) (Muwahhad.bCode m.tim)))))))

theorem madlulCode_inj (m n : Madlul) (h : madlulCode m = madlulCode n) : m = n := by
  obtain ⟨a, b, c, d, e, f, g, i⟩ := m; obtain ⟨a', b', c', d', e', f', g', i'⟩ := n
  unfold madlulCode at h
  obtain ⟨h1, h⟩ := pair_injective h
  obtain ⟨h2, h⟩ := pair_injective h
  obtain ⟨h3, h⟩ := pair_injective h
  obtain ⟨h4, h⟩ := pair_injective h
  obtain ⟨h5, h⟩ := pair_injective h
  obtain ⟨h6, h⟩ := pair_injective h
  obtain ⟨h7, h8⟩ := pair_injective h
  simp only at h1 h2 h3 h4 h5 h6 h7 h8
  have hc : c = c' := by
    apply map_inj (fun p : Nat × Nat => pair p.1 p.2) _ _ _ (encS_inj _ _ h3)
    intro x y hxy; obtain ⟨p, q⟩ := pair_injective hxy; exact Prod.ext p q
  rw [h1, encS_inj _ _ h2, hc, encS_inj _ _ h4, encS_inj _ _ h5, bCode_inj _ _ h6, bCode_inj _ _ h7, bCode_inj _ _ h8]

def mahmulCode : Mahmul → Nat
  | .khassa k => pair 0 k | .alaqa r x => pair 1 (pair r x) | .qabiliyya q => pair 2 q | .fard f => pair 3 f

theorem mahmulCode_inj (m n : Mahmul) (h : mahmulCode m = mahmulCode n) : m = n := by
  cases m <;> cases n <;> simp only [mahmulCode] at h <;>
    first
    | (exact absurd (pair_injective h).1 (by decide))
    | (rw [(pair_injective h).2])
    | (obtain ⟨h3, h4⟩ := pair_injective (pair_injective h).2; rw [h3, h4])

def nisbaCode : Nisab.Nisba → Nat | .isnadiyya => 0 | .taqyidiyya => 1 | .idafiyya => 2

theorem nisbaCode_inj (a b : Nisab.Nisba) (h : nisbaCode a = nisbaCode b) : a = b := by
  cases a <;> cases b <;> first | rfl | (simp [nisbaCode] at h)

def itarMadlulCode (u : ItarMadlul) : Nat := pair (madlulCode u.mawdu) (pair (mahmulCode u.mahmul) (nisbaCode u.nisba))

theorem itarMadlulCode_inj (u v : ItarMadlul) (h : itarMadlulCode u = itarMadlulCode v) : u = v := by
  obtain ⟨a, b, c⟩ := u; obtain ⟨a', b', c'⟩ := v
  unfold itarMadlulCode at h
  obtain ⟨h1, h⟩ := pair_injective h
  obtain ⟨h2, h3⟩ := pair_injective h
  simp only at h1 h2 h3
  rw [madlulCode_inj _ _ h1, mahmulCode_inj _ _ h2, nisbaCode_inj _ _ h3]

def itar3Enc (u : Itar3) : Nat :=
  pair (Mulhaqat.itarEnc u.jisr) (pair (encS (u.kalimat.map kalimaCode))
    (pair (encS (u.maani.map madlulCode)) (itarMadlulCode u.isnad)))

/-- **الرقمُ الواحد يُفكّ:** إطاران ثلاثيّان في الحدّ غيرُ ممتنعَين (مرخَّصان أو لا حكمَ لهما) برقمٍ واحد — إطارُهما النحويّ واحد
(بمبرهنة الملحقات)، وكلماتُهما واحدة، ومدلولاتُهما واحدة، وإسنادُهما واحد. -/
theorem itar3_value (u v : Itar3) (hu : hukm3 u ≠ .mumtani) (hv : hukm3 v ≠ .mumtani)
    (hfu : fiHadd u = true) (hfv : fiHadd v = true) (h : itar3Enc u = itar3Enc v) : u = v := by
  have hu' := ibtida3_of_hukm u hu hfu; have hv' := ibtida3_of_hukm v hv hfv
  unfold ibtida3 at hu' hv'; simp only [Bool.and_eq_true] at hu' hv'
  unfold itar3Enc at h
  obtain ⟨h1, h⟩ := pair_injective h
  obtain ⟨h2, h⟩ := pair_injective h
  obtain ⟨h3, h4⟩ := pair_injective h
  have e1 := Mulhaqat.itar_value _ _ hu'.1.1.1.1.1.1 hv'.1.1.1.1.1.1 h1
  have e2 := map_inj kalimaCode kalimaCode_inj _ _ (encS_inj _ _ h2)
  have e3 := map_inj madlulCode madlulCode_inj _ _ (encS_inj _ _ h3)
  have e4 := itarMadlulCode_inj _ _ h4
  cases u; cases v
  simp only at e1 e2 e3 e4
  subst e1 e2 e3 e4; rfl

end Utur
end Jisr
