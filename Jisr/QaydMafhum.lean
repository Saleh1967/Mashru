/-
  Jisr/QaydMafhum.lean — شهادةُ القيد من البنية: تحت `bilBunya` لا يبقى قيدُ المنطوق إلّا بشاهدٍ في بنيته: صفٌّ من جدول العوامل،
  أو أسلوبٌ أو بابٌ من جرد قطر الندى المبنيّ في Lean، أو وصفٌ من أربعةٍ معرَّفٍ هنا أسطرُه داخلَ باب «يعمل عمل فعله»، أو منشئُ الاسم.

  قولُ المالك (2026-10-24، 19:14): «يجب ان تعمل lean. لقواعد سيبويه وكذلك lean قطر الندى وكذلك lean للعوامل و lean المقاييس
  واربط ب lean المفهوم»؛ واختار من الأسئلة الرابطَ الأوّل: «القيود من العوامل والقطر (موصى به)».

  **ما كان:** في `Jisr/MantuqMafhum.lean` قيدُ المنطوق (`Mudaa.qayd`: صفة/شرط/غاية/عدد/اسم) و«إنما» (`Mudaa.innama`) يُودَعان باليد،
  ولا يُفحص لهما شاهدٌ من النحو؛ وممّا «أُغفل معلَنًا» في رأسه: «وآلةُ الشرط والغاية (س573، س578)».

  **ما هنا:** بنيةُ المنطوق قائمةُ عناصر (`Unsur`)، كلٌّ منها كائنٌ في Lean المشروع:
  * صفٌّ من جدول العوامل المختوم (`Awamil.table`، مولَّدٌ من المودَع ومطابَقٌ له بـ`tahaqquq/test_awamil.py`)؛
  * أسلوبٌ من جرد القطر (`Ikhbar.Uslub`، بسطره `Ikhbar.satr`)؛
  * بابُ إعرابٍ على الدالّ من القطر (`JisrDal.Bab`)؛
  * وصفٌ من الأوصاف الأربعة التي يعدّها القطر في «باب يعمل عمل فعله سبعة» (L347): اسم الفاعل (L358)، واسم المفعول (L365)، والصفة
    المشبّهة (L366)، واسم التفضيل (L370) — وأسطرُها داخلَ الباب بين `Ikhbar.satr .amal` و`Ikhbar.satr .nat` (`wasf_fi_bab_amal`)؛
  * والاسم: علمٌ (القطر L129) أو اسمُ جنس (ج3 س582) — ولا أسلوبَ له في جرد القطر المبنيّ، فهو منشئٌ هنا بسطره في التعليق وحده؛
  * و«إنما»: «إنّ» مقرونةً بما الحرفيّة — القطر L189–190: «إن لم تقترن بهن ما الحرفية: نحو {إنما الله إله / واحد}»؛ ج3 س584 —
    منشئٌ هنا بسطره في التعليق وحده.

  **التعيين** (تعيينُ البنّاء، معروضٌ على المالك — `unsurQayd`):
  * **الشرط:** صفّا الجدول في الصنف 10 أو 11 («أدوات الشرط الجازمة» و«غير الجازمة» في `Awamil.sinfIsm`)، وأسلوبُ الشرط في القطر (L115).
    ج3 س573: «تعليق الحكم على الشيء بكلمة «إن» أو غيرها من الشروط اللغوية»، ولا يعدّد غيرَ «إن»؛ فعدُّ الأربعة عشر كلِّها من «الشروط اللغوية»
    تعيين — وفي المغني «لولا» «لربط امتناع الثانية بوجود الأولى» (mughni L6304)، و«لوما» «بمنزلة لولا» (L6398)، ومثالُها في التنزيل {لو ما تأتينا بالملائكة} للتحضيض، وحصرُها فيه زعمُ المالقي وابنُ هشام «ويرده» (L6398–6399).
  * **الغاية:** صفُّ الجدول لفظُه «إلى» أو أوّلُه «حتى». ج3 س578: «الأحكام التي وردت مغياة بـ«حتى» و«إلى»»، أي حين تُستعمل للغاية؛
    والمغني يعدّ لكلٍّ معانيَ: «إلى» «له ثمانية معان» … «أحدها انتهاء الغاية الزمانية» (L1633–1634)، و«حتى» «انتهاء الغاية وهو الغالب والتعليل وبمعنى إلا»
    (L2754–2755)، والداخلةُ على المضارع المنصوب «مرادفة إلى … ومرادفة كي التعليلية» (L2805–2806)، والعاطفةُ «بمعنى الواو» (L2792). فالشاهدُ
    هنا اللفظُ لا المعنى: صفُّ «حتى» يشهد للغاية ولو كانت في المثال للتعليل — والتمييزُ بين المعاني للبنية لا للجدول.
  * **الصفة:** وصفٌ من الأربعة، والنعتُ («التابع المشتق أو المؤول به» L376)، والحالُ («وصف فضلة» L308). ج3 س568: «تعليق الحكم بصفة من صفات الذات».
  * **العدد:** أسلوبُ العدد (L414 «باب العدد من ثلاثة إلى تسعة»؛ والمئةُ في L316 «كتمييز المئة وما فوقها» من باب التمييز، وفي
    `Jisr/Mulhaqat.lean` يُعدّ «العدد (القطر L414–417 مع تمييزه L314–317)»؛ فإلحاقُ «مائة» بأسلوب العدد تعيين) والمثنّى (`JisrDal.Bab.muthanna`، L82–83).
    ج3 س580 يجعل «القرشين» «إطلاق لمطلق العدد»، ومثالَ «إِذَا بَلَغَ الْمَاءُ قُلَّتَيْنِ لَمْ يَحْمِلِ الْخَبَثَ» في مفهوم العدد.
  * **الاسم:** علمٌ أو اسمُ جنس. **و«إنما»:** مانعٌ لا قيد.

  **الربط** (`bilBunya`): القيدُ المودَع يبقى إن شهدت له البنية ويسقط إن لم تشهد؛ و«إنما» في البنية مانعٌ ولو لم تُودَع (و«إنما»
  المودَعةُ تبقى بلا شاهد). ولا يُحسب القيدُ من البنية حسابًا: قد تشهد لقيدين (مثالُ س580 «إِذَا بَلَغَ الْمَاءُ قُلَّتَيْنِ لَمْ يَحْمِلِ الْخَبَثَ»: أداةُ شرطٍ ومثنًّى، وج3 يعدّه في مفهوم العدد)،
  فالإيداعُ يختار، والبنيةُ تشهد.

  **ما ثبت** (بالمعيار الموحَّد في `Nizam/Asas.lean`): 15 مبرهنة —
  * لكلّ (7): `qayd_bilBunya`، `mukhalafa_mashuda` (كلُّ مفهوم مخالفةٍ تحت `bilBunya` صنفُه صنفُ قيدٍ مودَعٍ يشهد له عنصرٌ في بنية
    منطوقه)، `la_mukhalafa_bila_shahid`، `innama_bunya_yamna`، `bilBunya_sawa` (إن شهدت البنيةُ لكلّ قيدٍ مودَع ولم يكن فيها «إنما»
    فالمودَعُ هو هو)، و`ghayr_mukhalafa_baqi` مع `ghayr_mukhalafa_yabqa` (ما ليس مخالفةً يُخرجه الجسرُ بعد الربط إن وفقط إن أخرجه قبله).
  * على الشاهد (8): `adawat_shart` (أربع عشرة بأسمائها)، `adawat_ghaya` (أربع)، `shahid_istifham` («متى» و«أين» و«ما» و«مَن» أدواتِ
    استفهامٍ لا تشهد للشرط، وأدواتِ شرطٍ تشهد)، `ghaib_la_yashhad` (أربعٌ من أدوات القطر L115 بلا صفٍّ في الجدول)، `wasf_fi_bab_amal`،
    `shawahid_mashuda`، `shawahid_sawa` (الجسرُ على أمثلة ج3 العشرين بعد الربط هو هو)، و`shahid_bila_bunya_wa_innama` (مبنيّ).

  **حدُّه:** مبرهناتُ «لكلّ» خواصُّ للتعيين كما رُمِّز، لا مطابقتُه للنبهاني ولا للقطر. والبنيةُ لكلّ منطوقٍ (`bunya`) تحليلُ البنّاء
  لأمثلة ج3، لا مُخرَجُ قارئٍ من النصّ (النصّ إلى الإطار، الحزمة P4، لم يُبنَ). والربطُ غيرُ موصولٍ بالمحرّك (لا يستورده إلّا `Audit.lean`)،
  و`MantuqMafhum.jisr` بلا `bilBunya` يقبل القيدَ بلا شاهدٍ كما كان. وأدواتُ القطر L115 الغائبةُ عن الجدول لا تشهد بصفّ. وشرطا الصفة والعدد
  (الإفهام والسياق) والمانعان الآخران (الأغلب، النصّ المعطِّل) مودَعةٌ كما في `MantuqMafhum`. بلا sorry ولا axiom ولا native_decide.
-/
import Jisr.MantuqMafhum
import Jisr.AwamilJadwal
import Jisr.Ikhbar
import Jisr.JisrDal

namespace Jisr
namespace QaydMafhum

open MantuqMafhum

/-! ## ١. العناصر وما تشهد له -/

/-- الأوصافُ الأربعة من «باب يعمل عمل فعله سبعة» في القطر (L347). -/
inductive Wasf | fail | mafuul | mushabbaha | tafdil
  deriving DecidableEq, Repr

/-- سطرُ الوصف في القطر. -/
def wasfSatr : Wasf → Nat
  | .fail => 358 | .mafuul => 365 | .mushabbaha => 366 | .tafdil => 370

/-- عنصرٌ في بنية المنطوق. -/
inductive Unsur
  /-- الصفُّ i من جدول العوامل المختوم `Awamil.table`. -/
  | adat (i : Nat)
  /-- أسلوبٌ من جرد القطر (`Ikhbar.Uslub`). -/
  | uslub (u : Ikhbar.Uslub)
  /-- بابُ إعرابٍ على الدالّ من القطر (`JisrDal.Bab`). -/
  | bab (b : JisrDal.Bab)
  /-- وصفٌ من الأربعة. -/
  | wasf (w : Wasf)
  /-- علمٌ (القطر L129) أو اسمُ جنس (ج3 س582). -/
  | ism
  /-- «إنّ» مقرونةً بما الحرفيّة (القطر L189–190). -/
  | innama
  deriving DecidableEq, Repr

/-- قيدُ الأداة من صفّها في الجدول (تعيين): صنفا الشرط 10 و11 شرط، ولفظُ «إلى» أو ما أوّلُه «حتى» غاية، وما سواهما لا قيد. -/
def adatQayd (i : Nat) : Option Qayd :=
  match Awamil.table[i]? with
  | none => none
  | some (ism, sinf, _) =>
    if sinf == 10 || sinf == 11 then some .shart
    else if ism == "إلى" || ism.startsWith "حتى" then some .ghaya
    else none

/-- قيدُ الأسلوب من جرد القطر (تعيين). -/
def uslubQayd : Ikhbar.Uslub → Option Qayd
  | .shart => some .shart
  | .nat => some .sifa
  | .hal => some .sifa
  | .adad => some .adad
  | _ => none

/-- القيدُ الذي يشهد له العنصر (تعيين). -/
def unsurQayd : Unsur → Option Qayd
  | .adat i => adatQayd i
  | .uslub u => uslubQayd u
  | .bab .muthanna => some .adad
  | .bab _ => none
  | .wasf _ => some .sifa
  | .ism => some .ism
  | .innama => none

/-- البنيةُ تشهد للقيد q: فيها عنصرٌ يشهد له. -/
def mashud (b : List Unsur) (q : Qayd) : Bool :=
  b.any (fun u => unsurQayd u == some q)

/-! ## ٢. الربط: المودَعُ مع بنيته -/

variable {Mn L : Type}

/-- القيدُ المودَع يبقى إن شهدت له البنية، و«إنما» في البنية مانع. وما سوى الحقلين كما أُودع. -/
def bilBunya (D : Mudaa Mn L) (b : Mn → List Unsur) : Mudaa Mn L :=
  { D with
    qayd := fun m => (D.qayd m).filter (mashud (b m))
    innama := fun m => D.innama m || (b m).contains .innama }

/-- **القيدُ بعد الربط** هو المودَعُ المشهود. -/
theorem qayd_bilBunya (D : Mudaa Mn L) (b : Mn → List Unsur) (m : Mn) (q : Qayd) :
    (bilBunya D b).qayd m = some q ↔ D.qayd m = some q ∧ mashud (b m) q = true := by
  simp only [bilBunya]
  cases h : D.qayd m with
  | none => simp
  | some q' =>
    simp only [Option.filter_some, Option.some.injEq]
    by_cases hm : mashud (b m) q' = true
    · simp only [hm, ite_true, Option.some.injEq]
      constructor
      · intro e; subst e; exact ⟨rfl, hm⟩
      · intro ⟨e, _⟩; exact e
    · simp only [hm, ite_false, reduceCtorEq, false_iff, not_and]
      intro e; subst e; simpa using hm

/-- **الربطُ محافظ:** إن شهدت البنيةُ لكلّ قيدٍ مودَع ولم يكن فيها «إنما»، فالمودَعُ بعد الربط هو هو، فالجسرُ هو هو. -/
theorem bilBunya_sawa (D : Mudaa Mn L) (b : Mn → List Unsur)
    (hq : ∀ m q, D.qayd m = some q → mashud (b m) q = true)
    (hi : ∀ m, (b m).contains .innama = false) : bilBunya D b = D := by
  cases D with
  | mk kalimat qayd mufhim siyaqAdad innama aghlab muattil naqid muwafiq iqtida tanbih ishara =>
    simp only [bilBunya, Mudaa.mk.injEq, and_true, true_and]
    refine ⟨?_, ?_⟩
    · funext m
      cases h : qayd m with
      | none => rfl
      | some q => simp [hq m q h]
    · funext m
      have hn : Unsur.innama ∉ b m := by simpa using hi m
      simp [hn]

variable [DecidableEq L]

/-- **كلُّ مفهوم مخالفةٍ تحت `bilBunya` مشهود:** صنفُه صنفُ قيدٍ مودَعٍ يشهد له عنصرٌ في بنية منطوقه. -/
theorem mukhalafa_mashuda (D : Mudaa Mn L) (b : Mn → List Unsur) {ms : List Mn} {f : Mafhum Mn L}
    {k : SLGE.Madlul.Mukhalafa} (h : f ∈ jisr (bilBunya D b) ms) (hk : f.naw = .mukhalafa k) :
    ∃ q u, D.qayd f.asl = some q ∧ sinfOf q = some k ∧ u ∈ b f.asl ∧ unsurQayd u = some q := by
  obtain ⟨q, hq, hs⟩ := mukhalafa_min_qayd (bilBunya D b) h hk
  obtain ⟨hd, hm⟩ := (qayd_bilBunya D b f.asl q).1 hq
  obtain ⟨u, hu, he⟩ := List.any_eq_true.1 hm
  exact ⟨q, u, hd, hs, hu, by simpa using he⟩

/-- **لا مخالفةَ بلا شاهد:** قيدٌ مودَعٌ لا يشهد له عنصرٌ في البنية لا يُخرج تحت `bilBunya` مفهومَ مخالفة. -/
theorem la_mukhalafa_bila_shahid (D : Mudaa Mn L) (b : Mn → List Unsur) {m : Mn} {q : Qayd}
    (hq : D.qayd m = some q) (hm : mashud (b m) q = false) :
    ∀ f ∈ jisrMn (bilBunya D b) m, ∀ k, f.naw ≠ .mukhalafa k := by
  intro f hf k hk
  obtain ⟨q', _, _, hq', _⟩ := mem_mukhalafaOf (bilBunya D b) (mukhalafa_min_mukhalafaOf (bilBunya D b) hf hk)
  obtain ⟨hd, hm'⟩ := (qayd_bilBunya D b m q').1 hq'
  rw [hq] at hd; cases hd
  rw [hm] at hm'; cases hm'

/-- **«إنما» في البنية تمنع المخالفة** تحت `bilBunya` ولو لم تُودَع (س584؛ القطر L189–190). -/
theorem innama_bunya_yamna (D : Mudaa Mn L) (b : Mn → List Unsur) {m : Mn}
    (h : (b m).contains .innama = true) :
    ∀ f ∈ jisrMn (bilBunya D b) m, ∀ k, f.naw ≠ .mukhalafa k := by
  have hmem : Unsur.innama ∈ b m := by simpa using h
  apply mani_yamna_mukhalafa
  simp [mawani, bilBunya, hmem]

/-- **الربطُ لا يُضيف غيرَ المخالفة:** كلُّ مفهومٍ غيرِ مخالفةٍ يُخرجه الجسرُ بعد الربط يُخرجه قبله. -/
theorem ghayr_mukhalafa_baqi (D : Mudaa Mn L) (b : Mn → List Unsur) {m : Mn} {f : Mafhum Mn L}
    (h : f ∈ jisrMn (bilBunya D b) m) (hk : ∀ k, f.naw ≠ .mukhalafa k) : f ∈ jisrMn D m := by
  have hmh : mahmul (bilBunya D b) m = mahmul D m := rfl
  have hmt : muwafiqTabi (bilBunya D b) m = muwafiqTabi D m := rfl
  unfold jisrMn at h ⊢
  rw [hmh, hmt] at h
  cases hp : mahmul D m
  · simp [hp] at h
  · simp only [hp, ite_true, List.mem_append] at h ⊢
    rcases h with (((h | h) | h) | h) | h
    · exact Or.inl (Or.inl (Or.inl (Or.inl h)))
    · exact Or.inl (Or.inl (Or.inl (Or.inr h)))
    · exact Or.inl (Or.inl (Or.inr h))
    · exact Or.inl (Or.inr h)
    · obtain ⟨_, k, _, _, _, _, _, _, hf⟩ := mem_mukhalafaOf (bilBunya D b) h
      exact absurd (by rw [hf]) (hk k)

/-- **ولا يُسقطه:** كلُّ مفهومٍ غيرِ مخالفةٍ يُخرجه الجسرُ قبل الربط يُخرجه بعده. -/
theorem ghayr_mukhalafa_yabqa (D : Mudaa Mn L) (b : Mn → List Unsur) {m : Mn} {f : Mafhum Mn L}
    (h : f ∈ jisrMn D m) (hk : ∀ k, f.naw ≠ .mukhalafa k) : f ∈ jisrMn (bilBunya D b) m := by
  have hmh : mahmul (bilBunya D b) m = mahmul D m := rfl
  have hmt : muwafiqTabi (bilBunya D b) m = muwafiqTabi D m := rfl
  unfold jisrMn at h ⊢
  rw [hmh, hmt]
  cases hp : mahmul D m
  · simp [hp] at h
  · simp only [hp, ite_true, List.mem_append] at h ⊢
    rcases h with (((h | h) | h) | h) | h
    · exact Or.inl (Or.inl (Or.inl (Or.inl h)))
    · exact Or.inl (Or.inl (Or.inl (Or.inr h)))
    · exact Or.inl (Or.inl (Or.inr h))
    · exact Or.inl (Or.inr h)
    · obtain ⟨_, k, _, _, _, _, _, _, hf⟩ := mem_mukhalafaOf D h
      exact absurd (by rw [hf]) (hk k)

/-! ## ٣. على الجدول المختوم وجرد القطر -/

/-- أسماءُ صفوف الجدول التي تشهد للقيد q، بترتيب الجدول. -/
def adawatOf (q : Qayd) : List String :=
  (List.range Awamil.table.length).filterMap fun i =>
    if adatQayd i = some q then (Awamil.table[i]?).map (·.1) else none

/-- **أدواتُ الشرط الأربع عشرة** من الجدول (الصنفان 10 و11). -/
theorem adawat_shart :
    adawatOf .shart = ["إنْ", "مَن", "ما", "مهما", "متى", "أين", "أينما", "أنى", "حيثما", "كيفما",
      "إذا", "لو", "لولا", "لوما"] := by
  decide +kernel

/-- **أدواتُ الغاية الأربع** من الجدول («إلى» و«حتى» في صفوفها الثلاثة). -/
theorem adawat_ghaya :
    adawatOf .ghaya = ["إلى", "حتى (جر)", "حتى (عطف)", "حتى (المصدرية)"] := by
  decide +kernel

/-- صفُّ (اللفظ، الصنف) في الجدول؛ وما ليس فيه موضعٌ خارجه (طولُ الجدول). -/
def saff (ism : String) (sinf : Nat) : Nat :=
  (Awamil.table.findIdx? fun r => r.1 == ism && r.2.1 == sinf).getD Awamil.table.length

/-- **الألفاظُ الأربعة المشتركة بين الشرط والاستفهام:** أداةَ شرطٍ (الصنف 10) تشهد للشرط، وأداةَ استفهامٍ (الصنف 12) لا تشهد له. -/
theorem shahid_istifham :
    ["متى", "أين", "ما", "مَن"].all (fun w => mashud [.adat (saff w 10)] .shart) = true ∧
    ["متى", "أين", "ما", "مَن"].all (fun w => !mashud [.adat (saff w 12)] .shart) = true := by
  decide +kernel

/-- **أدواتُ القطر L115 بلا صفٍّ في الجدول لا تشهد:** «إذ» و«إذما» و«أي» و«أيان»، بلا شدّةٍ كما في القطر وبها (و«إن» فيه «إنْ»). وفي
`KhulasaIkhbar.ghaib_L115_khamsa` خمسةٌ بمطابقة الاسم مجرَّدًا، خامسُها «إن». -/
theorem ghaib_la_yashhad :
    ["إذ", "إذما", "أي", "أيّ", "أيان", "أيّان"].all (fun w => saff w 10 == Awamil.table.length) = true ∧
    ["إذ", "إذما", "أي", "أيّ", "أيان", "أيّان"].all (fun w => !mashud [.adat (saff w 10)] .shart) = true ∧
    saff "إنْ" 10 ≠ Awamil.table.length := by
  decide +kernel

/-- **الأوصافُ الأربعة داخلَ «باب يعمل عمل فعله»** في جرد القطر: بين سطر الباب (`Ikhbar.satr .amal`) وسطر التوابع (`Ikhbar.satr .nat`). -/
theorem wasf_fi_bab_amal :
    [Wasf.fail, .mafuul, .mushabbaha, .tafdil].all
      (fun w => Ikhbar.satr .amal < wasfSatr w && wasfSatr w < Ikhbar.satr .nat) = true := by
  decide

/-! ## ٤. أمثلةُ ج3: بنيتُها، وشهادتُها لما أُودع لها في `MantuqMafhum.wit`

  البنيةُ تحليلُ البنّاء لكلّ مثال (معلَن؛ والأمثلةُ بأسمائها في `MantuqMafhum.Shahid`): سائمة اسمُ فاعلٍ من سام؛ الأبيض صفةٌ مشبّهة وفي المثال
  أداةُ الشرط إذا؛ أضعافًا مضاعفة حالٌ ونعت؛ مثالُ الحمل بأداة الشرط إنْ في أسلوب الشرط؛ مثالُ الليل بحرف الجرّ إلى في أسلوب الجرّ؛ مثالُ المائة
  عدد؛ القرشين مثنًّى؛ الغنم اسمُ جنس. وسائرُ الأمثلة (لوازمُها غيرُ المخالفة) بنيتُها فارغة: لا قيدَ لها مودَع. -/

/-- بنيةُ أمثلة ج3. -/
def bunya : Shahid → List Unsur
  | .saima => [.wasf .fail]
  | .abyad => [.wasf .mushabbaha, .adat (saff "إذا" 11)]
  | .riba => [.uslub .hal, .uslub .nat]
  | .hamlNafaqa => [.adat (saff "إنْ" 10), .uslub .shart]
  | .layl => [.adat (saff "إلى" 7), .uslub .jarr]
  | .mia => [.uslub .adad]
  | .qirshayn => [.bab .muthanna]
  | .ghanam => [.ism]
  | _ => []

/-- الأمثلةُ العشرون. -/
def kullShahid : List Shahid :=
  [.qatilu, .aatiq, .wadaa, .sariq, .ghadban, .haml30, .bashiru, .uff, .qintar, .dharra, .yatama, .luqata,
   .saima, .abyad, .hamlNafaqa, .layl, .mia, .qirshayn, .ghanam, .riba]

/-- **كلُّ قيدٍ أُودع لأمثلة ج3 تشهد له بنيتُه.** -/
theorem shawahid_mashuda :
    kullShahid.all (fun s => match wit.qayd s with
      | some q => mashud (bunya s) q
      | none => true) = true := by
  decide +kernel

/-- **فالجسرُ على الأمثلة العشرين بعد الربط هو هو.** -/
theorem shawahid_sawa :
    kullShahid.all (fun s => jisrMn (bilBunya wit bunya) s == jisrMn wit s) = true := by
  decide +kernel

/-- **مبنيٌّ:** مثالُ الشرط بلا شاهدٍ في بنيته لا يُخرج مخالفة؛ وبـ«إنما» مع الأداة لا يُخرجها؛ وبالأداة وحدها يُخرجها. -/
theorem shahid_bila_bunya_wa_innama :
    jisrMn (bilBunya wit fun _ => []) .hamlNafaqa = [] ∧
    jisrMn (bilBunya wit fun s => if s = .hamlNafaqa then [.innama, .adat (saff "إنْ" 10)] else bunya s) .hamlNafaqa = [] ∧
    jisrMn (bilBunya wit bunya) .hamlNafaqa = [⟨.mukhalafa .shart, .hamlNafaqa, "لا نفقة لغير الحامل"⟩] := by
  decide +kernel

end QaydMafhum
end Jisr
