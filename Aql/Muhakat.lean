/-
  Aql/Muhakat.lean — محاكاةُ قواعد العمليّة العقليّة قبل ورود الشرع: جدولُ السقوف، والالتقاء، وسياجُ الرأي،
  وحارسُ النطاق، وعدمُ تدخّل الدافع (SIM-AQL، المرحلة ١ في Mashru).

  الطلب: قولُ المالك في الجلسة 2026-11-22 (17:22 بتوقيت عمّان): «MASHRU REPO لقد بنينا اساس لعمل المحاكاة الأفضل لتنفيذ
  خطوة التالية المقترحة: تشغيل النواة على مدخلات حقيقية في Mashru … وإن أردت البرهان فالبداية بصياغة INV-01 وجدول السقوف في
  Lean. ويوجد مثال لاية الدين اعمل pr على اية الدين انت مفوض وخبير نفذ ذلك». والتصميمُ قرارُ البنّاء، والنواةُ التي يشير
  إليها نواةُ بايثون بناها البنّاء في الجلسة نفسِها خارج المستودع (SIM-AQL 0.1)؛ لم يدخل منها إلّا ما أُعيد بناؤه هنا.

  السند (أرقامُ فقرات «التفكير» في تحويلٍ نصّيٍّ رفعه المالك في الجلسة، لا أسطرُ a3.txt؛ وما في Aql/Aqliyya.lean بأسطرها هو هو):
  * التفكير [38]، [65]: الحكمُ على وجود الشيء قطعيّ، وعلى حقيقته أو صفته ظنّيّ.
  * التفكير [82]–[84]: الأثرُ يدلّ على وجود المؤثّر لا على صفته («الصفة لما لا يحسّ لا يمكن نقلها بواسطة الحواس»).
  * التفكير [79]، [87]: ما يُصدر عن غير الواقع أو عن واقعٍ مفروض ليس فكرًا.
  * التفكير [90]–[92]: ما صحّ عن المقطوع بوجوده وصدقه قطعيَّ الثبوت قطعيَّ الدلالة يُؤخذ.
  * التفكير [70]: الرأيُ القطعيّ لا يُتخلّى عنه في البحث الظنّيّ، ويُتخلّى عن كلّ رأيٍ ظنّيّ؛ وفي البحث القطعيّ يُتخلّى
    عن كلّ رأيٍ وإيمانٍ سابق. «إذا تعارض القطعيّ والظنّيّ يؤخذ القطعيّ ويُردّ الظنّيّ».
  * التفكير [71]: الموضوعيّةُ حصرُ البحث في موضوعه، «لا يصحّ أن تفكّر في المصلحة ولا في الضرر».
  * الشخصيّة ج3 [339] (تحويلُ الجلسة): جهاتُ الحكم ثلاث — واقعُ الشيء، وملاءمتُه لطبع الإنسان، والمدحُ والذمّ؛ والثالثةُ للشرع.
  * التفكير [118]، [123]: الحقيقةُ انطباقُ الفكر على الواقع انطباقًا يقينيًّا، وتتعلّق «بالوجود، لا بالكنه ولا بالصفات».

  التعيين (البنّاء، معلَن):
  * القنواتُ سبع والجهاتُ ستّ كما في `Qanat` و`Jiha`؛ و«وجودُ صفةٍ معيّنة» قطعيّةً من الحسّ قولُ محمد محمد إسماعيل (الفكر الإسلامي)
    لا النبهاني، فهو هنا ظنّيٌّ من الحسّ إلّا بسياسةٍ مسمّاة (`saqf true`).
  * الالتقاءُ `iltiqa` أدنى الرتبتين: «النتيجةُ لا تعلو أضعفَ مقدّماتها» قاعدةٌ هندسيّة، لا نصّ.
  * الدافعُ (أصلٌ من الأربعة ومظهرٌ باسمه؛ التفكير [58]–[60]) يعيّن السؤالَ وحده، ولا تقرؤه دالّةُ الحكم.

  الوسم: «مبرهن» لما برهانُه لكلّ مدخل (بالحالات على أنواعٍ منتهية أو بالاستقراء على القوائم)، و«تعريفيّة» لما برهانُه
  `rfl` على التعريف، و«على الشاهد» لما برهانُه `decide` على مثال. بلا sorry ولا axiom ولا native_decide.
-/
import Aql.Aqliyya

namespace Aql.Muhakat

/-! ## ١. الجهاتُ والقنواتُ والرتب -/

/-- جهةُ الحكم (التفكير [38]؛ ج3 [339]). -/
inductive Jiha | wujud | wujudSifa | sifa | kunh | mulaama | madhDhamm
  deriving DecidableEq, Repr

/-- قناةُ التلقّي (التفكير [81]–[92]). `nass`: نصٌّ بعينه، وجودُه محسوسٌ ومضمونُه خبر. -/
inductive Qanat | hiss | athar | mutawatir | ahad | nass | fard | takhayyul
  deriving DecidableEq, Repr

/-- الرتبُ سلسلةٌ: ليس فكرًا < ظنّيّ < قطعيّ. -/
inductive Rutba | laFikr | zanni | qati
  deriving DecidableEq, Repr

def Rutba.val : Rutba → Nat
  | .laFikr => 0
  | .zanni => 1
  | .qati => 2

/-- الالتقاء: أدنى الرتبتين (قاعدةٌ هندسيّة). -/
def iltiqa (a b : Rutba) : Rutba := if a.val ≤ b.val then a else b

/-- سقفُ الرتبة بالجهة والقناة. `ismail`: سياسةٌ مسمّاة تجعل وجودَ الصفة من الحسّ قطعيًّا (قولُ محمد إسماعيل). -/
def saqf (ismail : Bool) : Jiha → Qanat → Rutba
  | _, .fard => .laFikr
  | _, .takhayyul => .laFikr
  | .madhDhamm, _ => .laFikr
  | .wujud, .hiss => .qati
  | .wujud, .athar => .qati
  | .wujud, .mutawatir => .qati
  | .wujud, _ => .zanni
  | .wujudSifa, .hiss => if ismail then .qati else .zanni
  | .wujudSifa, .mutawatir => .qati
  | .wujudSifa, _ => .zanni
  | .sifa, .athar => .laFikr
  | .kunh, .athar => .laFikr
  | .sifa, .mutawatir => .qati
  | .kunh, .mutawatir => .qati
  | .sifa, _ => .zanni
  | .kunh, _ => .zanni
  | .mulaama, _ => .zanni

/-! ## ٢. جدولُ السقوف: خواصُّه لكلّ مدخل (مبرهن) -/

/-- الفرضُ والتخيّل ليسا فكرًا، في كلّ جهةٍ وكلّ سياسة (التفكير [79]، [87]). -/
theorem saqf_fard (p : Bool) (j : Jiha) : saqf p j .fard = .laFikr ∧ saqf p j .takhayyul = .laFikr := by
  cases j <;> exact ⟨rfl, rfl⟩

/-- المدحُ والذمّ لا يحكم فيهما العقلُ قبل الشرع، من أيّ قناة (ج3 [339]). -/
theorem saqf_madh_dhamm (p : Bool) (q : Qanat) : saqf p .madhDhamm q = .laFikr := by
  cases q <;> rfl

/-- الصفةُ والكنهُ من الحسّ ظنّيّان، في كلّ سياسة (التفكير [38]). -/
theorem saqf_sifa_hiss (p : Bool) : saqf p .sifa .hiss = .zanni ∧ saqf p .kunh .hiss = .zanni :=
  ⟨rfl, rfl⟩

/-- الأثرُ لا ينقل الصفةَ ولا الكنه (التفكير [83]–[84]). -/
theorem saqf_athar_sifa (p : Bool) : saqf p .sifa .athar = .laFikr ∧ saqf p .kunh .athar = .laFikr :=
  ⟨rfl, rfl⟩

/-- الوجودُ من الحسّ أو الأثر قطعيّ (التفكير [38]، [82]). -/
theorem saqf_wujud_hissi (p : Bool) : saqf p .wujud .hiss = .qati ∧ saqf p .wujud .athar = .qati :=
  ⟨rfl, rfl⟩

/-- لا يبلغ القطعَ من قناةٍ غيرِ الحسّ والأثر والمتواتر شيءٌ، في كلّ جهةٍ وكلّ سياسة. -/
theorem qati_qanat (p : Bool) (j : Jiha) (q : Qanat) (h : saqf p j q = .qati) :
    q = .hiss ∨ q = .athar ∨ q = .mutawatir := by
  cases j <;> cases q <;> cases p <;> simp_all [saqf]

/-- ولا يبلغ القطعَ في الصفة أو الكنه إلّا المتواتر. -/
theorem sifa_qati_mutawatir (p : Bool) (j : Jiha) (hj : j = .sifa ∨ j = .kunh) (q : Qanat)
    (h : saqf p j q = .qati) : q = .mutawatir := by
  rcases hj with rfl | rfl <;> cases q <;> simp_all [saqf]

/-- السياسةُ المسمّاة لا تغيّر إلّا خانةً واحدة: وجودَ الصفة من الحسّ. -/
theorem siyasa_khana_wahida (j : Jiha) (q : Qanat) (h : ¬ (j = .wujudSifa ∧ q = .hiss)) :
    saqf true j q = saqf false j q := by
  cases j <;> cases q <;> simp_all [saqf]

/-! ## ٣. الوراثة: الجدولُ يوافق `Aql.martaba` القائمة (مبرهن)

  `Aql.martaba : NawHukm → Bool → Martaba` (Aql/Aqliyya.lean §٦) تقسم الحكمَ وجودًا أو حقيقةً وصفة، والحسَّ حاضرًا أو غائبًا.
  فهي الجدولُ هنا مقصورًا: الوجودُ على `.wujud`، والحقيقةُ والصفةُ على `.sifa`، والحسُّ الحاضر على `.hiss` والغائبُ على `.ahad`. -/

def minMartaba : Martaba → Rutba
  | .qati => .qati
  | .zanni => .zanni

def jihaOf : NawHukm → Jiha
  | .wujud => .wujud
  | .haqiqaAwSifa => .sifa

def qanatOf : Bool → Qanat
  | true => .hiss
  | false => .ahad

theorem saqf_yuwafiq_martaba (p : Bool) (n : NawHukm) (hiss : Bool) :
    minMartaba (martaba n hiss) = saqf p (jihaOf n) (qanatOf hiss) := by
  cases n <;> cases hiss <;> rfl

/-! ## ٤. الالتقاء: النتيجةُ لا تعلو أضعفَ مقدّماتها (مبرهن) -/

theorem iltiqa_la_yazid (a b : Rutba) : (iltiqa a b).val ≤ a.val ∧ (iltiqa a b).val ≤ b.val := by
  unfold iltiqa; split <;> omega

theorem iltiqa_comm (a b : Rutba) : iltiqa a b = iltiqa b a := by
  cases a <;> cases b <;> rfl

theorem iltiqa_assoc (a b c : Rutba) : iltiqa (iltiqa a b) c = iltiqa a (iltiqa b c) := by
  cases a <;> cases b <;> cases c <;> rfl

/-- رتبةُ الحكم: سقفُ جهته وقناته ملتقيًا برتب مقدّماته. -/
def rutbaHukm (p : Bool) (j : Jiha) (q : Qanat) (ms : List Rutba) : Rutba :=
  ms.foldl iltiqa (saqf p j q)

theorem foldl_iltiqa_le (ms : List Rutba) (r : Rutba) :
    (ms.foldl iltiqa r).val ≤ r.val ∧ ∀ m ∈ ms, (ms.foldl iltiqa r).val ≤ m.val := by
  induction ms generalizing r with
  | nil => simp
  | cons x xs ih =>
    obtain ⟨h1, h2⟩ := ih (iltiqa r x)
    obtain ⟨hx1, hx2⟩ := iltiqa_la_yazid r x
    refine ⟨by simp only [List.foldl]; omega, ?_⟩
    intro m hm
    simp only [List.foldl]
    rcases List.mem_cons.mp hm with rfl | hm
    · omega
    · exact h2 m hm

/-- لا يعلو الحكمُ سقفَه. -/
theorem rutba_la_taalu_saqf (p : Bool) (j : Jiha) (q : Qanat) (ms : List Rutba) :
    (rutbaHukm p j q ms).val ≤ (saqf p j q).val :=
  (foldl_iltiqa_le ms _).1

/-- ولا يعلو أيَّ مقدّمةٍ من مقدّماته. -/
theorem rutba_la_taalu_muqaddima (p : Bool) (j : Jiha) (q : Qanat) (ms : List Rutba) :
    ∀ m ∈ ms, (rutbaHukm p j q ms).val ≤ m.val :=
  (foldl_iltiqa_le ms _).2

/-- INV-03: الصفةُ والكنهُ من الحسّ لا يبلغان القطع، أيًّا كانت المقدّمات. -/
theorem sifa_hiss_la_qati (p : Bool) (j : Jiha) (hj : j = .sifa ∨ j = .kunh) (ms : List Rutba) :
    rutbaHukm p j .hiss ms ≠ .qati := by
  intro h
  have hle := rutba_la_taalu_saqf p j .hiss ms
  rw [h] at hle
  rcases hj with rfl | rfl <;> simp [saqf, Rutba.val] at hle

/-! ## ٥. الحقيقة: وجودٌ قطعيٌّ عن حسٍّ أو أثر (التفكير [118]، [123]) -/

def haqiqa (j : Jiha) (q : Qanat) (r : Rutba) : Bool :=
  j == .wujud && r == .qati && (q == .hiss || q == .athar)

theorem haqiqa_wujud (j : Jiha) (q : Qanat) (r : Rutba) (h : haqiqa j q r = true) :
    j = .wujud ∧ r = .qati ∧ (q = .hiss ∨ q = .athar) := by
  cases j <;> cases q <;> cases r <;> simp_all [haqiqa]

/-- ما جاء بالنقل، ولو متواترًا، ليس «حقيقةً» بهذا المعنى: الحقيقةُ عن حسٍّ أو أثر. -/
theorem naql_laysa_haqiqa (j : Jiha) (r : Rutba) :
    haqiqa j .mutawatir r = false ∧ haqiqa j .ahad r = false ∧ haqiqa j .nass r = false := by
  cases j <;> cases r <;> exact ⟨rfl, rfl, rfl⟩

/-! ## ٦. سياجُ الرأي (التفكير [69]–[70]) -/

inductive NawMadda | maaluma | ray | fard
  deriving DecidableEq, Repr

structure Madda where
  naw : NawMadda
  rutba : Rutba
  deriving DecidableEq, Repr

/-- ما يدخل Γ: المعلومةُ دائمًا؛ والرأيُ القطعيّ في البحث الظنّيّ وحده؛ ولا فرضَ (الفروضُ في Δ). -/
def yadkhul (bahthQati : Bool) (m : Madda) : Bool :=
  match m.naw with
  | .maaluma => true
  | .ray => !bahthQati && m.rutba == .qati
  | .fard => false

def siyaj (bahthQati : Bool) (ms : List Madda) : List Madda := ms.filter (yadkhul bahthQati)

/-- لا رأيَ ظنّيًّا في Γ، في كلّ بحث. -/
theorem siyaj_la_ray_zanni (b : Bool) (ms : List Madda) (m : Madda) (hm : m ∈ siyaj b ms)
    (hr : m.naw = .ray) : m.rutba = .qati ∧ b = false := by
  simp only [siyaj, List.mem_filter, yadkhul, hr] at hm
  obtain ⟨_, h⟩ := hm
  cases b <;> cases hq : m.rutba <;> simp_all

/-- ولا رأيَ أصلًا في البحث القطعيّ. -/
theorem siyaj_qati_bila_ray (ms : List Madda) (m : Madda) (hm : m ∈ siyaj true ms) : m.naw ≠ .ray := by
  intro hr
  exact absurd (siyaj_la_ray_zanni true ms m hm hr).2 (by decide)

/-- والرأيُ القطعيّ يُبقى في البحث الظنّيّ. -/
theorem siyaj_yabqi_qati (ms : List Madda) (m : Madda) (hm : m ∈ ms) (hr : m.naw = .ray)
    (hq : m.rutba = .qati) : m ∈ siyaj false ms := by
  simp [siyaj, yadkhul, hr, hq, hm]

/-- ولا فرضَ في Γ. -/
theorem siyaj_la_fard (b : Bool) (ms : List Madda) (m : Madda) (hm : m ∈ siyaj b ms) : m.naw ≠ .fard := by
  intro hf
  simp [siyaj, yadkhul, hf] at hm

/-- والمعلومةُ تدخل دائمًا. -/
theorem siyaj_yabqi_maaluma (b : Bool) (ms : List Madda) (m : Madda) (hm : m ∈ ms)
    (hn : m.naw = .maaluma) : m ∈ siyaj b ms := by
  simp [siyaj, yadkhul, hn, hm]

/-! ## ٧. الدافعُ وحارسُ النطاق (INV-01، INV-05) -/

/-- أصولُ الطاقة الحيويّة (التفكير [58]–[60]). -/
inductive Asl | hajaUdwiyya | baqa | naw | tadayyun
  deriving DecidableEq, Repr

structure Dafi where
  asl : Asl
  mazhar : String

/-- سؤالٌ: جهةٌ وقناة. -/
structure Sual where
  jiha : Jiha
  qanat : Qanat
  deriving DecidableEq, Repr

/-- الجواب: خارجَ النطاق قبل الشرع، أو رتبةٌ بالتقاء السقف والمقدّمات. -/
inductive Jawab | kharijNitaq | bi (r : Rutba)
  deriving DecidableEq, Repr

/-- الحكم: دالّةٌ في السؤال والمقدّمات وحدها؛ ونوعُها لا يأخذ الدافع (التفكير [71]: حصرُ البحث في موضوعه). -/
def hukm (p : Bool) (s : Sual) (ms : List Rutba) : Jawab :=
  if s.jiha = .madhDhamm then .kharijNitaq else .bi (rutbaHukm p s.jiha s.qanat ms)

/-- المحاكاة: الدافعُ يعيّن السؤال (`ikhtiyar`)، ثمّ يُحكم. -/
def muhakat (p : Bool) (ikhtiyar : Dafi → Sual) (d : Dafi) (ms : List Rutba) : Jawab :=
  hukm p (ikhtiyar d) ms

/-- INV-01 (تعريفيّة): الدافعُ لا يغيّر الحكمَ إلّا بتغيير السؤال؛ فدافعان اختارا سؤالًا واحدًا جوابُهما واحد. -/
theorem dafi_la_yughayyir (p : Bool) (ikhtiyar : Dafi → Sual) (d₁ d₂ : Dafi) (ms : List Rutba)
    (h : ikhtiyar d₁ = ikhtiyar d₂) : muhakat p ikhtiyar d₁ ms = muhakat p ikhtiyar d₂ ms := by
  simp [muhakat, h]

/-- INV-05 (مبرهن): كلُّ سؤالٍ من جهة المدح والذمّ خارجَ النطاق، أيًّا كانت قناتُه ومقدّماته. -/
theorem madh_dhamm_kharij (p : Bool) (q : Qanat) (ms : List Rutba) :
    hukm p ⟨.madhDhamm, q⟩ ms = .kharijNitaq := by
  simp [hukm]

/-- وما سواها لا يخرج من النطاق. -/
theorem ghayr_madh_dakhil (p : Bool) (s : Sual) (ms : List Rutba) (h : s.jiha ≠ .madhDhamm) :
    hukm p s ms = .bi (rutbaHukm p s.jiha s.qanat ms) := by
  simp [hukm, h]

/-! ## ٨. شواهدُ آية الدَّين (على الشاهد)

  أسئلةٌ ثلاثة على كلّ جملةٍ من الآية (البقرة ٢٨٢) في مودَع التنزيل المختوم؛ ويجريها على كلماتها `scripts/muhakat_dayn.py`:
  * وجودُ الجملة في المودَع: جهةُ الوجود من الحسّ (البايتاتُ مقروءةٌ ببصمتها) ← قطعيّ، وحقيقةٌ بالمعنى أعلاه.
  * حكمُ الكتابة أو الإشهاد: جهةُ المدح والذمّ ← خارجَ النطاق قبل الشرع.
  * معنى اللفظ بالوضع: جهةُ الصفة من نقلٍ آحاد (شاهدٌ معجميٌّ واحد أو اثنان لم يُفحص استقلالُهما) ← ظنّيّ. -/

def suWujudNass : Sual := ⟨.wujud, .hiss⟩
def suHukmKitaba : Sual := ⟨.madhDhamm, .nass⟩
def suManaLafz : Sual := ⟨.sifa, .ahad⟩

theorem shahid_dayn :
    hukm false suWujudNass [] = .bi .qati ∧
    haqiqa suWujudNass.jiha suWujudNass.qanat .qati = true ∧
    hukm false suHukmKitaba [] = .kharijNitaq ∧
    hukm false suManaLafz [.zanni, .zanni] = .bi .zanni ∧
    hukm false suManaLafz [.laFikr] = .bi .laFikr := by
  decide

end Aql.Muhakat
