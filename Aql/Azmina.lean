/-
  Aql/Azmina.lean — الأزمنةُ على محور الآن: الآنُ محايدٌ (صفر)، والإزاحاتُ عنه بالوحدات (ساعة، يوم، أسبوع، شهر، سنة) سالبةً لما مضى
  وموجبةً لما يأتي؛ وأسماءُ الإزاحات من اللسان (أمس، أوّل من أمس، الغد، بعد غد، عام أوّل، عام قابل)؛ وتحويلُ الوحدات حيث نصّ اللسان
  (الأسبوع سبعة أيام، السنة اثنا عشر شهرًا) و«لا حكم» حيث لم ينصّ (الشهر بالأيام)؛ وانتقالُ الآن (كلّ يوم يصير أمسًا)؛ واستقامةُ الكلام
  ومحالُه عند سيبويه على الإزاحات.

  قرارُ المالك (2026-10-16، 20:06) بلفظه: «فإذا زمن الان هو المحايد وناقص الوحدة الزمنية ساعه وساعتين ويوم واسبوع وشهر وسنة هكذا وزائد
  واحد غدا وزائد سبعة اسبوع وزائد شهر وزائد سنة اعمل lean الازمنة».

  **السند** (بأسطره؛ الاقتباساتُ بلفظ المصدر):
  - لسان العرب (مختوم): س245811: «والآن تقع على كل وقت حاضر لا يخص بعض ذلك دون بعض»؛ س149201: «الساعة: جزء من أجزاء الليل والنهار»؛
    س149208: «والساعة: الوقت الحاضر»؛ س244209: «اليوم: معروف مقداره من طلوع الشمس إلى غروبها»؛ س148327: «والسبوع والأسبوع من الأيام: تمام
    سبعة أيام»؛ س87957–87958: «ابن سيده: والشهر العدد المعروف / من الأيام، سمي بذلك لأنه يشهر بالقمر وفيه علامة ابتدائه وانتهائه»؛ س82632:
    «السنة اثنا عشر شهرا»؛ س199682: «الحول: سنة بأسرها»؛ س263594: «السنة: واحدة السنين. قال ابن سيده: السنة العام».
  - أسماءُ الإزاحات — لسان العرب: س112305: «أمس: من ظروف الزمان مبني على الكسر إلا أن ينكر أو يعرف»؛ س112333–112335: «ابن السكيت: تقول ما
    رأيته مذ / أمس، فإن لم تره يوما قبل ذلك قلت: ما رأيته مذ أول من أمس، فإن لم تره / يومين قبل ذلك قلت: ما رأيته مذ أول من أول من أمس»؛
    س112353: «ما رأيته / قبل أمس بيوم؛ يريد من أول من أمس»؛ س112344–112345: «يقولون إذا نكروه كل يوم يصير أمسا، وكل أمس مضى فلن يعود»؛
    س289554: «الغدو: أصل الغد، وهو اليوم الذي يأتي بعد يومك»؛ س289556: «والغد ثاني يومك»؛ س70859–70861: «يقال ما رأيته مذ عام الأول، /
    وقال العوام: مذ عام أول … / … لم أره مذ يومان ولم / أره منذ يومين»؛ س212565: «يقال: عام قابل أي مقبل».
  - الكتاب (مختوم) س263–264: «فأما المستقيم الحسن فقولك أتيتك أمس وسآتيك غدا | وأما محال فأن تنقض أول / كلامك بآخره فتقول أتيتك غدا
    وسآتيك أمس»؛ س267: «المحال الكذب فأن تقول سوف أشرب ماء البحر أمس»؛ س348: «سيذهب فإنه دليل على أنه يكون فيما يستقبل من الزمان»؛
    س9760–9761: «سوف يفعل لأنها بمنزلة السين التي / في قولك سيفعل»؛ ج3 (مرشّح) س926: «وتخليص المستقبل عن الحاضر بدخول السين أو سوف».
  - المخصّص (مختوم) س31081: «صاحب العين الوقت المقدار من الدهر»؛ س31121: «الحول السنة بأسرها».

  **الصورة.** الوحداتُ `Wahda` سلّمٌ برتبة (`rutba_tartib`). الإزاحةُ `Izaha` عددٌ صحيح من وحدة؛ **الآنُ محايد**: صفرُ كلّ وحدة، عنصرٌ محايد
  للجمع (`al_an_muhayid`)، والعكسُ يردّ إلى الآن (`aks_yarudd`). **الأزمنةُ الثلاثة من الإشارة** (`zamanOf`: سالب ماضٍ، صفر حال، موجب مستقبل؛
  `zaman_hasir`)، والعكسُ يقلب الماضي مستقبلًا والحالَ حالًا (`aks_yaqlib`) — فالتناظرُ حول الآن. **الأسماء** إزاحاتٌ باليوم والسنة: أمس −1،
  أوّل من أمس −2، أوّل من أوّل من أمس −3 (`awwalMin` ينقص يومًا — اللسان س112333–112335، 112353)، اليوم 0، الغد +1 «ثاني يومك» (`bad` يزيد يومًا)،
  بعد غد +2؛ عام أوّل −1 سنة، عام قابل +1 سنة. **انتقالُ الآن** (`markaz k`: الإزاحةُ نفسُها من آنٍ متأخّرٍ بـ k): كلُّ يوم يصير أمسًا
  (`kull_yawm_yasir_amsan`)، وكلُّ أمسٍ مضى فلن يعود (`kull_ams_mada_lan_yaud`: لا انتقالٍ إلى الأمام يعيده)، والانتقالُ يحفظ الفروقَ والترتيب
  (`markaz_yahfaz_farq`). **التحويل** حيث نصّ اللسان: الأسبوع 7 أيام (`usbu_sabat_ayyam`)، السنة 12 شهرًا (`sana_ithna_ashar`)؛ والشهرُ بالأيام
  والسنةُ بالأيام «لا حكم» (`shahr_bil_ayyam_la_hukm`؛ اللسان: «العدد المعروف من الأيام» بلا عدد — فلا يُعيَّن)؛ واليومُ 24 ساعة تعيينُ البنّاء
  (اللسان: «جزء من أجزاء الليل والنهار» بلا عدد)؛ والتحويلُ يحفظ الإشارة (`tahwil_yahfaz_ishara`). **الاستقامةُ والمحال** (الكتاب س263–267):
  الكلامُ يستقيم إذا وافق زمنُ الفعل إشارةَ الظرف (`yastaqim`): «أتيتك أمس» و«سآتيك غدا» مستقيمان، و«أتيتك غدا» و«سوف أشرب … أمس» محالان
  (على الشاهد)، ولا إزاحةَ تستقيم مع الماضي والمستقبل معًا (`la_yastaqim_maan`). **الجسرُ إلى الأزمنة الخمسة** (`Awwaliyyat.zaman5Of`): إزاحةٌ
  موجبةٌ من الآن مستقبلٌ (منفَّسٌ أو لا) وسالبةٌ ماضٍ (منقطعٌ أو متّصل) (`izaha_mustaqbal`، `izaha_madi`).

  **المبرهنات (لكلّ، 16):** `al_an_muhayid`، `aks_yarudd`، `aks_aks`، `zaman_hasir`، `aks_yaqlib`، `al_an_hal`، `markaz_sifr`، `markaz_markaz`،
  `markaz_yahfaz_farq`، `kull_ams_mada_lan_yaud`، `tahwil_yahfaz_ishara`، `shahr_bil_ayyam_la_hukm`، `la_yastaqim_maan`، `izaha_mustaqbal`،
  `izaha_madi`، `awwalMin_bad`. **على الشاهد (12؛ decide على المبنيّ):** `rutba_tartib`، `rutba_injective`، `asma_azmina` (أسماءُ الإزاحات
  بأزمنتها)، `awwal_min_ams`، `qabl_ams_biyawm`، `ghad_thani_yawmik`، `kull_yawm_yasir_amsan`، `usbu_sabat_ayyam`، `sana_ithna_ashar`، `yawm_24`
  (تعيين)، `mustaqim_hasan_ams_ghad`، `muhal_ghad_ams`. (28 في `Audit.lean`؛ مسلّماتها propext/Quot.sound فقط — بلا `Classical.choice`.)

  الوسم: مبرهن (لكلّ) ما سُمّي كذلك؛ مبرهن على الشاهد (decide/rfl/simp على المبنيّ) ما سُمّي كذلك. تعييناتُ البنّاء (تُعرض على المالك):
  اليومُ 24 ساعة؛ الشهرُ والسنةُ بالأيام «لا حكم» حتّى يُودَع عددٌ (الهلاليّ 29/30 أو الشمسيّ)؛ «السين» في «سآتيك» مستقبلٌ منفَّس كـ«سوف»
  (الكتاب س9760–9761، ج3 س926)؛ أسماءُ الإزاحات باليوم والسنة من اللسان وما لا اسمَ له في اللسان (بعد غد، قبل/بعد شهر) بالعدد والوحدة.
  الجدولُ `azmina.tsv` مسجَّلٌ «مرشّحًا» حتّى يأذن المالك بختمه؛ ومطابقتُه `tahaqquq/test_azmina.py`.
-/
import Aql.Awwaliyyat

set_option autoImplicit false

namespace Aql
namespace Azmina
open Aql.Awwaliyyat

/-! ## ١. الوحدات والإزاحة والآن المحايد -/

/-- الوحداتُ الزمنية سلّمًا: الساعة، اليوم، الأسبوع، الشهر، السنة. -/
inductive Wahda | saa | yawm | usbu | shahr | sana
deriving DecidableEq, Repr

/-- رتبةُ الوحدة في السلّم (الساعة 0 … السنة 4). -/
def Wahda.rutba : Wahda → Nat
  | .saa => 0
  | .yawm => 1
  | .usbu => 2
  | .shahr => 3
  | .sana => 4

/-- السلّمُ مرتَّبٌ تصاعدًا (على الشاهد). -/
theorem rutba_tartib : Wahda.saa.rutba < Wahda.yawm.rutba ∧ Wahda.yawm.rutba < Wahda.usbu.rutba ∧
    Wahda.usbu.rutba < Wahda.shahr.rutba ∧ Wahda.shahr.rutba < Wahda.sana.rutba := by decide

/-- الرتبةُ تميّز الوحدات (على الشاهد). -/
theorem rutba_injective : ∀ u v : Wahda, u.rutba = v.rutba → u = v := by
  intro u v; cases u <;> cases v <;> decide

/-- إزاحةٌ عن الآن: عددٌ صحيح من وحدة — سالبٌ لما مضى، موجبٌ لما يأتي. -/
structure Izaha where
  adad : Int
  wahda : Wahda
deriving DecidableEq, Repr

/-- **الآنُ محايد:** صفرُ كلّ وحدة. -/
def alAn (u : Wahda) : Izaha := ⟨0, u⟩

/-- عكسُ الإزاحة: المرآةُ حول الآن. -/
def Izaha.aks (i : Izaha) : Izaha := ⟨-i.adad, i.wahda⟩

/-- جمعُ إزاحتين من وحدةٍ واحدة (ومن وحدتين مختلفتين: لا حكم). -/
def jam (i j : Izaha) : Option Izaha := if i.wahda = j.wahda then some ⟨i.adad + j.adad, i.wahda⟩ else none

/-- **الآنُ عنصرٌ محايد** للجمع من الجهتين. -/
theorem al_an_muhayid (i : Izaha) : jam (alAn i.wahda) i = some i ∧ jam i (alAn i.wahda) = some i := by
  simp [jam, alAn]

/-- **العكسُ يردّ إلى الآن:** زائدُ k ثمّ ناقصُ k. -/
theorem aks_yarudd (i : Izaha) : jam i i.aks = some (alAn i.wahda) := by
  simp [jam, Izaha.aks, alAn]; omega

theorem aks_aks (i : Izaha) : i.aks.aks = i := by simp [Izaha.aks]

/-! ## ٢. الأزمنةُ الثلاثة من الإشارة -/

inductive Zaman3 | madi | hal | mustaqbal
deriving DecidableEq, Repr

/-- زمنُ الإزاحة من إشارتها: سالبٌ ماضٍ، صفرٌ حال، موجبٌ مستقبل. -/
def zamanOf (i : Izaha) : Zaman3 := if i.adad < 0 then .madi else if i.adad = 0 then .hal else .mustaqbal

/-- **الثلاثةُ حاصرة** على الإزاحات (نظيرُ `Awwaliyyat.azmina_thalatha_hasira` على الأعداد الصحيحة). -/
theorem zaman_hasir (i : Izaha) :
    (i.adad < 0 ↔ zamanOf i = .madi) ∧ (i.adad = 0 ↔ zamanOf i = .hal) ∧ (0 < i.adad ↔ zamanOf i = .mustaqbal) := by
  unfold zamanOf
  rcases Int.lt_trichotomy i.adad 0 with h | h | h
  · have h2 : ¬ i.adad = 0 := by omega
    have h3 : ¬ 0 < i.adad := by omega
    simp [h, h2, h3]
  · simp [h]
  · have h1 : ¬ i.adad < 0 := by omega
    have h2 : ¬ i.adad = 0 := by omega
    simp [h, h1, h2]

/-- قلبُ الزمن: الماضي مستقبلًا والمستقبلُ ماضيًا والحالُ حالًا. -/
def qalb : Zaman3 → Zaman3
  | .madi => .mustaqbal
  | .hal => .hal
  | .mustaqbal => .madi

/-- **التناظرُ حول الآن:** عكسُ الإزاحة يقلب زمنها. -/
theorem aks_yaqlib (i : Izaha) : zamanOf i.aks = qalb (zamanOf i) := by
  unfold zamanOf Izaha.aks qalb
  rcases Int.lt_trichotomy i.adad 0 with h | h | h
  · have h'' : ¬ (-i.adad = 0) := by omega
    simp [h, h'']; omega
  · simp [h]
  · have h0 : ¬ (i.adad < 0) := by omega
    have h1 : ¬ (i.adad = 0) := by omega
    simp [h0, h1]; omega

theorem al_an_hal (u : Wahda) : zamanOf (alAn u) = .hal := by simp [zamanOf, alAn]

/-! ## ٣. أسماءُ الإزاحات (اللسان) -/

def alYawm : Izaha := ⟨0, .yawm⟩
/-- أمس: ناقصُ يوم. -/
def ams : Izaha := ⟨-1, .yawm⟩
/-- الغد: زائدُ يوم — «اليوم الذي يأتي بعد يومك» (س289554). -/
def ghad : Izaha := ⟨1, .yawm⟩
/-- «أوّل من …»: ناقصُ وحدة (س112333–112335: أمس، أوّل من أمس، أوّل من أوّل من أمس). -/
def awwalMin (i : Izaha) : Izaha := ⟨i.adad - 1, i.wahda⟩
/-- «بعد …»: زائدُ وحدة (الغد «ثاني يومك» س289556؛ بعد غد). -/
def bad (i : Izaha) : Izaha := ⟨i.adad + 1, i.wahda⟩
/-- «قبل … بكذا»: ناقصُ k من الوحدة (س112353: «قبل أمس بيوم؛ يريد من أول من أمس»). -/
def qabl (i : Izaha) (k : Int) : Izaha := ⟨i.adad - k, i.wahda⟩
/-- عامٌ أوّل: ناقصُ سنة (س70859–70861)؛ عامٌ قابل: زائدُ سنة (س212565). -/
def amAwwal : Izaha := ⟨-1, .sana⟩
def amQabil : Izaha := ⟨1, .sana⟩

theorem awwal_min_ams : awwalMin ams = ⟨-2, .yawm⟩ ∧ awwalMin (awwalMin ams) = ⟨-3, .yawm⟩ := by decide
theorem qabl_ams_biyawm : qabl ams 1 = awwalMin ams := by decide
theorem ghad_thani_yawmik : ghad = bad alYawm ∧ bad ghad = ⟨2, .yawm⟩ := by decide
/-- «بعد» و«أوّل من» متعاكسان على كلّ إزاحة. -/
theorem awwalMin_bad (i : Izaha) : awwalMin (bad i) = i ∧ bad (awwalMin i) = i := by
  simp [awwalMin, bad]

/-- أسماءُ الإزاحات (قولُ المالك: ناقص/زائد الوحدة؛ وأسماءُ اللسان حيث وُجدت) وأزمنتُها. -/
def asma : List (String × Izaha) :=
  [("الآن", alAn .saa), ("قبل ساعة", ⟨-1, .saa⟩), ("قبل ساعتين", ⟨-2, .saa⟩), ("بعد ساعة", ⟨1, .saa⟩),
   ("أوّل من أوّل من أمس", awwalMin (awwalMin ams)), ("أوّل من أمس", awwalMin ams), ("أمس", ams), ("اليوم", alYawm), ("الغد", ghad),
   ("بعد غد", bad ghad), ("بعد أسبوع", ⟨1, .usbu⟩), ("قبل أسبوع", ⟨-1, .usbu⟩), ("بعد شهر", ⟨1, .shahr⟩), ("قبل شهر", ⟨-1, .shahr⟩),
   ("عام أوّل", amAwwal), ("عام قابل", amQabil)]

theorem asma_azmina : asma.map (fun p => zamanOf p.2) =
    [.hal, .madi, .madi, .mustaqbal, .madi, .madi, .madi, .hal, .mustaqbal, .mustaqbal, .mustaqbal, .madi, .mustaqbal, .madi, .madi,
     .mustaqbal] := by decide

/-! ## ٤. انتقالُ الآن: كلُّ يوم يصير أمسًا -/

/-- الإزاحةُ نفسُها منظورًا إليها من آنٍ متأخّرٍ بـ k وحدات. -/
def markaz (k : Int) (i : Izaha) : Izaha := ⟨i.adad - k, i.wahda⟩

theorem markaz_sifr (i : Izaha) : markaz 0 i = i := by simp [markaz]
theorem markaz_markaz (k l : Int) (i : Izaha) : markaz k (markaz l i) = markaz (k + l) i := by
  simp [markaz]; omega
/-- الانتقالُ يحفظ الفروقَ (ومن ثَمّ الترتيب). -/
theorem markaz_yahfaz_farq (k : Int) (i j : Izaha) : (markaz k i).adad - (markaz k j).adad = i.adad - j.adad := by
  simp only [markaz]; omega
/-- **كلُّ يوم يصير أمسًا** (س112344): اليومُ من الغد أمسٌ. -/
theorem kull_yawm_yasir_amsan : markaz 1 alYawm = ams ∧ markaz 1 ghad = alYawm := by decide
/-- **وكلُّ أمسٍ مضى فلن يعود** (س112344–112345): لا انتقالٍ إلى الأمام يعيد أمسًا إلى الحال أو المستقبل. -/
theorem kull_ams_mada_lan_yaud (k : Int) (hk : 0 ≤ k) : zamanOf (markaz k ams) = .madi := by
  have h : -1 - k < 0 := by omega
  simp [zamanOf, markaz, ams, h]

/-! ## ٥. تحويلُ الوحدات حيث نصّ اللسان -/

/-- إلى أيّام: اليوم والأسبوع (7)؛ الشهرُ والسنةُ والساعةُ «لا حكم» بالأيام. -/
def ilaAyyam : Izaha → Option Int
  | ⟨n, .yawm⟩ => some n
  | ⟨n, .usbu⟩ => some (7 * n)
  | _ => none

/-- إلى أشهر: الشهر والسنة (12). -/
def ilaAshhur : Izaha → Option Int
  | ⟨n, .shahr⟩ => some n
  | ⟨n, .sana⟩ => some (12 * n)
  | _ => none

/-- إلى ساعات: الساعة، واليوم 24 (تعيين)، والأسبوع 168. -/
def ilaSaat : Izaha → Option Int
  | ⟨n, .saa⟩ => some n
  | ⟨n, .yawm⟩ => some (24 * n)
  | ⟨n, .usbu⟩ => some (168 * n)
  | _ => none

theorem usbu_sabat_ayyam : ilaAyyam ⟨1, .usbu⟩ = some 7 ∧ ilaAyyam ⟨-1, .usbu⟩ = some (-7) := by decide
theorem sana_ithna_ashar : ilaAshhur amQabil = some 12 ∧ ilaAshhur amAwwal = some (-12) := by decide
theorem yawm_24 : ilaSaat alYawm = some 0 ∧ ilaSaat ghad = some 24 ∧ ilaSaat ⟨1, .usbu⟩ = some 168 := by decide
/-- الشهرُ والسنةُ بالأيام لا حكم (لم ينصّ اللسان على عدد). -/
theorem shahr_bil_ayyam_la_hukm (n : Int) : ilaAyyam ⟨n, .shahr⟩ = none ∧ ilaAyyam ⟨n, .sana⟩ = none := by
  simp [ilaAyyam]
/-- **التحويلُ يحفظ الإشارة:** ما مضى يبقى ماضيًا بأيّ وحدة. -/
theorem tahwil_yahfaz_ishara (i : Izaha) (d : Int) (h : ilaAyyam i = some d) : zamanOf ⟨d, .yawm⟩ = zamanOf i := by
  obtain ⟨n, u⟩ := i
  cases u with
  | yawm => simp [ilaAyyam] at h; subst h; rfl
  | usbu =>
    simp [ilaAyyam] at h; subst h
    unfold zamanOf
    rcases Int.lt_trichotomy n 0 with hn | hn | hn
    · have a : 7 * n < 0 := by omega
      simp [a, hn]
    · subst hn; simp
    · have a : ¬ (7 * n < 0) := by omega
      have b : ¬ (7 * n = 0) := by omega
      have c : ¬ (n < 0) := by omega
      have d' : ¬ (n = 0) := by omega
      simp [a, b, c, d']
  | saa => simp [ilaAyyam] at h
  | shahr => simp [ilaAyyam] at h
  | sana => simp [ilaAyyam] at h

/-! ## ٦. الاستقامةُ والمحال (الكتاب س263–267) والجسرُ إلى الأزمنة الخمسة -/

/-- الأزمنةُ الخمسة إلى الثلاثة. -/
def zaman3Of5 : Zaman5 → Zaman3
  | .madiMunqati => .madi
  | .madiMuttasil => .madi
  | .hal => .hal
  | .mustaqbal => .mustaqbal
  | .mustaqbalMunaffas => .mustaqbal

/-- يستقيم الكلامُ إذا وافق زمنُ الفعل زمنَ الظرف. -/
def yastaqim (z : Zaman5) (i : Izaha) : Bool := zaman3Of5 z == zamanOf i

/-- «أتيتك أمس وسآتيك غدا» مستقيمٌ (س263؛ السينُ مستقبلٌ منفَّس — تعيين). -/
theorem mustaqim_hasan_ams_ghad : yastaqim .madiMunqati ams = true ∧ yastaqim .mustaqbalMunaffas ghad = true := by decide
/-- «أتيتك غدا وسآتيك أمس» و«سوف أشرب ماء البحر أمس» محالٌ (س264، 267). -/
theorem muhal_ghad_ams : yastaqim .madiMunqati ghad = false ∧ yastaqim .mustaqbalMunaffas ams = false := by decide
/-- **لا إزاحةَ تستقيم مع الماضي والمستقبل معًا** (نقضُ أوّل الكلام بآخره). -/
theorem la_yastaqim_maan (i : Izaha) : ¬ (yastaqim .madiMunqati i = true ∧ yastaqim .mustaqbalMunaffas i = true) := by
  simp [yastaqim, zaman3Of5]
  intro h; rw [← h]; decide

/-- إزاحةٌ موجبةٌ باليوم من الآن `now` تقع في المستقبل (منفَّسًا أو لا) على `Awwaliyyat.zaman5Of`. -/
theorem izaha_mustaqbal (now d : Nat) (m f : Bool) (hd : 0 < d) :
    zaman5Of now (now + d) m f = .mustaqbal ∨ zaman5Of now (now + d) m f = .mustaqbalMunaffas :=
  ((zaman5_hasira now (now + d) m f).2.2).1 (by omega)

/-- وإزاحةٌ سالبةٌ (لا تجاوز الآن) تقع في الماضي (منقطعًا أو متّصلًا). -/
theorem izaha_madi (now d : Nat) (m f : Bool) (hd : 0 < d) (hn : d ≤ now) :
    zaman5Of now (now - d) m f = .madiMunqati ∨ zaman5Of now (now - d) m f = .madiMuttasil :=
  ((zaman5_hasira now (now - d) m f).1).1 (by omega)

end Azmina
end Aql
