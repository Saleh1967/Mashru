/-
  Aql/SimAql.lean — SIM-AQL: نموذجٌ لقواعد العمليّة العقليّة كما يقرّرها «التفكير»، مبرهَنًا في Lean، وموصولًا بمحرّك الإجابة.

  الطلب: أمرُ المالك 2026-11-22 (17:14 بتوقيت عمّان): «انت خبير اعمل تطوير لmashru»، على ملفَّيه «SIM-AQL 0.1» (README، نواةٌ بايثون
  لم تُرفع شفرتُها) و«بروتوكول محاكاة العملية العقلية قبل ورود الشرع v0.1». وخطوتُهما التالية بنصّهما: «إن أردت البرهان فالبداية
  بصياغة INV-01 وجدول السقوف في Lean». فهذا الملفّ تلك البداية وما بعدها، على أسطر المودَعات المختومة لا على أرقام فقرات الملفّين.

  **السند** (أسطرٌ يطابقها `tahaqquq/test_sim_aql.py` بنصّها؛ ت = `tafkir.txt` المختوم f7fcc683…، ش٣ = `a2.txt` 8252ca52…):
  * ت18: «الإدراك الشعوري … ولكن هذا التمييز ليس فكراً ولا إدراكاً»؛ ت23: «وإنما هو تمييز غريزي ليس غير».
  * ت16: «الحس وحده لا يحصل منه فكر»؛ ت27: «فالذي يستعمل هو المعلومات فقط مع الحيلولة دون وجود الرأي».
  * ت48: «إذا تعارض القطعي والظني يؤخذ القطعي ويرد الظني»؛ «إذا كان البحث قطعياً … لا بد أن يتخلى عن كل رأي وكل إيمان سابق»؛
    «لا بد أن يتخلى عن كل رأي ظني سابق في الموضوع»؛ والموضوعيةُ «حصر البحث في الموضوع نفسه».
  * ت53: «والتخيل ليس تفكيراً، وحتى الفروض كلها … ليست تفكيراً»؛ ت58: ما يؤخذ «عن واقع مفروض وجوده أو متخيل وجوده، لا يعتبر فكراً».
  * ت55: «الحكم بوجود شيء خرج منه الصوت هو حكم قطعي»؛ «أثر الشيء جزء من وجوده»؛ ت56: «الصفة لما لا يحس لا يمكن نقلها بواسطة الحواس».
  * ت60: المغيبات «إن نقلت أو رويت عن المقطوع بصدق قوله … فإنها تعتبر من الفكر»؛ و«لا يشترط في ثبوت القول»؛ ت61: «وما عدا هذه الحالة
    فإن المغيبات ليست فكراً».
  * ت75: «الحقيقة هي مطابقة الفكر للواقع»؛ ت82: الحقائق «تتعلق بالوجود، لا بالكنه ولا بالصفات».
  * ت83: «والأسلوب يقرره نوع العمل»؛ ت86: الأسلوب «كيفية غير دائمة بعكس الطريقة فإنها كيفية دائمة»؛ ت88: الوسائل «قد يضلل عنها إذا جرى
    التفكير بها في معزل عن التفكير بالأسلوب الذي تنفذه»؛ ت92: «فالغاية من التفكير يجب أن تحدد».
  * ت100: «فالتفكير العميق هو التعمق في الحس والمعلومات والربط»؛ ت101: «فإن كل فكر مستنير هو تفكير عميق».
  * ت106: «فإن الجدية تقضي بأن يعمل لتحقيق ما يقصد إليه، وأن يكون عمله في مستوى ما يقصد إليه»؛ «فقول المرء إنه جاد في تفكيره لا يكفي».
  * ت145–146: شروطُ التفكير السياسي الخمسة (تتبّعُ الأخبار، معلوماتٌ عن ماهية الوقائع، عدمُ التجريد والتعميم، تمييزُ الخبر بتمحيصه، ربطُ
    الخبر بالمعلومات).
  * ش٣ 339: «فهذه ثلاث جهات للحكم على الأشياء: أحدها من حيث واقعها ما هو، والثاني من حيث ملاءمتها لطبع الإنسان»؛ وش٣ 353: المدحُ والذمّ
    «الحكم في شأنها للشرع وحده وليس للعقل».
  * ش٣ 729: «ومن هنا كانت طريق معرفة اللغة العربية هي النقل المتواتر وخبر الآحاد»؛ والآحاد «طريق تحصيل الظن به».

  **تصحيحٌ على SIM-AQL 0.1** (قراءةُ النصّ في الجلسة): README يقول «الأسلوب يقرره نوع الشيء» (`Registry.style_for(ObjectKind)`)؛ والنصّ
  ت83 «الأسلوب يقرره نوع العمل». فالأسلوبُ هنا في التفكير بالعمل (§٧)، لا في الحكم على الشيء؛ والحكمُ على الشيء تحكمه الطريقةُ الواحدة.
  وكذلك «الإدراك الشعوري يُحسب لجهة الملاءمة»: النصّ ت18 «ليس فكراً ولا إدراكاً» بلا قيدِ جهة، فلا يُخرج حكمًا في أيّ جهة (`saqf_shuur`).

  **قواعدُ هندسيّة** (اختيارُ البنّاء، لا نسبةَ لها إلى النصّ): ترتيبُ الرتب والالتقاءُ أدناها؛ ورتبةُ النتيجة أدنى سقوفها ومقدّماتها؛
  وسقوفُ أنواع الربط إلّا ما سُمّي سندُه؛ والتعارضُ بين متساويين تعليق؛ وسقفُ الملاءمة من الحسّ ظنّيّ.

  **ما يضمنه البناءُ نفسُه** (مبرهنٌ لكلّ حالة): الدافعُ يُختم في S0 فلا تقرؤه مرحلةٌ بعده (INV-01، `dafi_la_yuaththir`)، والوسمُ المدّعى
  لا يمرّ من S0 (INV-08، `wasm_la_yamnah`) — مبرهنتان بـ`rfl`: ضمانٌ بنيويّ، لا اكتشاف.
  ولا يدّعي الملفّ عقلًا في الماكينة (ت23: «العقل غير موجود إلا عند الإنسان»): هو نموذجٌ لقواعد العمليّة.
  بلا sorry ولا axiom ولا native_decide.
-/
import Aql.Aqliyya

set_option autoImplicit false

namespace Aql
namespace SimAql

/-! ## ١. الرتب: ليس فكرًا < ظنّيّ < قطعيّ (قاعدة هندسية) -/

inductive Rutba | laFikr | zanni | qati
  deriving DecidableEq, Repr

def Rutba.n : Rutba → Nat
  | .laFikr => 0 | .zanni => 1 | .qati => 2

/-- الالتقاء: أدنى الرتبتين. -/
def iltiqa (a b : Rutba) : Rutba := if a.n ≤ b.n then a else b

theorem iltiqa_l (a b : Rutba) : (iltiqa a b).n ≤ a.n := by
  unfold iltiqa; split <;> omega

theorem iltiqa_r (a b : Rutba) : (iltiqa a b).n ≤ b.n := by
  unfold iltiqa; split <;> omega

theorem iltiqa_comm (a b : Rutba) : iltiqa a b = iltiqa b a := by
  cases a <;> cases b <;> rfl

def iltiqaKull : List Rutba → Rutba := List.foldr iltiqa .qati

theorem iltiqaKull_adna : ∀ (rs : List Rutba), ∀ r ∈ rs, (iltiqaKull rs).n ≤ r.n
  | [], _, h => by simp at h
  | x :: xs, r, h => by
    simp only [iltiqaKull, List.foldr_cons] at *
    rcases List.mem_cons.1 h with rfl | h'
    · exact iltiqa_l _ _
    · exact Nat.le_trans (iltiqa_r _ _) (iltiqaKull_adna xs r h')

/-! ## ٢. الجهة والقناة وجدول السقوف -/

/-- جهاتُ الحكم: الوجود، والصفة، والكنه (ت82)، والملاءمة، والمدح والذمّ (ش٣ 339). -/
inductive Jiha | wujud | sifa | kunh | mulaama | madhDhamm
  deriving DecidableEq, Repr

/-- قنواتُ ما يُبنى عليه الحكم. -/
inductive Qanat
  | hiss                                          -- ت55
  | athar                                         -- ت55–56: الحسّ بالأثر
  | naql (masdarMaqtu thubutQati : Bool)          -- ت60–61: المغيّب منقولًا
  | khabarLugha (mutawatir : Bool)                -- ش٣ 729: المتواتر والآحاد
  | fard | takhayyul                              -- ت53، ت58
  | shuur                                         -- ت18، ت23: الإدراك الشعوري
  deriving DecidableEq, Repr

/-- **جدولُ السقوف.** -/
def saqf : Jiha → Qanat → Rutba
  | _, .fard => .laFikr
  | _, .takhayyul => .laFikr
  | _, .shuur => .laFikr
  | .wujud, .hiss => .qati
  | _, .hiss => .zanni
  | .wujud, .athar => .qati
  | _, .athar => .laFikr
  | _, .naql m q => if m then (if q then .qati else .zanni) else .laFikr
  | _, .khabarLugha t => if t then .qati else .zanni

theorem saqf_fard (j : Jiha) : saqf j .fard = .laFikr := by cases j <;> rfl
theorem saqf_takhayyul (j : Jiha) : saqf j .takhayyul = .laFikr := by cases j <;> rfl
/-- الإدراكُ الشعوريّ لا يُخرج فكرًا في أيّ جهة (ت18). -/
theorem saqf_shuur (j : Jiha) : saqf j .shuur = .laFikr := by cases j <;> rfl
/-- الأثرُ ينقل الوجود لا الصفة ولا الكنه (ت55–56). -/
theorem saqf_athar : saqf .wujud .athar = .qati ∧ saqf .sifa .athar = .laFikr ∧ saqf .kunh .athar = .laFikr :=
  ⟨rfl, rfl, rfl⟩
/-- الصفةُ والكنهُ من الحسّ لا تبلغان القطع (ت82). -/
theorem saqf_hiss_sifa : saqf .sifa .hiss = .zanni ∧ saqf .kunh .hiss = .zanni := ⟨rfl, rfl⟩
/-- المغيّبُ عن غير المقطوع بوجوده وصدقه ليس فكرًا (ت61)، وعنه بثبوتٍ ظنّيّ فكرٌ ظنّيّ (ت60). -/
theorem saqf_ghayb (j : Jiha) (q : Bool) :
    saqf j (.naql false q) = .laFikr ∧ saqf j (.naql true false) = .zanni := by
  cases j <;> exact ⟨rfl, rfl⟩
/-- خبرُ الآحاد في اللغة ظنّ (ش٣ 729). -/
theorem saqf_ahad (j : Jiha) : saqf j (.khabarLugha false) = .zanni := by cases j <;> rfl

/-- الموافقةُ مع `Aql.martaba` القائمة (التفكير 65 في a3.txt): الوجودُ عن حسٍّ قطعيّ، والحقيقةُ أو الصفةُ ظنّيّ. -/
theorem muwafaqa_martaba :
    (saqf .wujud .hiss = .qati ∧ Aql.martaba .wujud true = .qati) ∧
    (saqf .sifa .hiss = .zanni ∧ Aql.martaba .haqiqaAwSifa true = .zanni) := ⟨⟨rfl, rfl⟩, ⟨rfl, rfl⟩⟩

/-- أنواعُ الربط وسقوفُها. -/
inductive NawRabt | wujudAnHissAwAthar | wad | tasnif | tajriba | istinbat
  deriving DecidableEq, Repr

def saqfRabt : NawRabt → Rutba
  | .wujudAnHissAwAthar => .qati   -- ت55
  | .wad => .qati                  -- ش٣ 729: الوضعُ يُسلَّم به؛ ويحدّه سقفُ قناته (المتواتر/الآحاد)
  | .tasnif => .zanni              -- قاعدة هندسية (بروتوكول SIM-AQL §3: عضويّةُ الجنس ظنّيّة)
  | .tajriba => .zanni             -- ت44: «الطريقة العلمية ظنية»
  | .istinbat => .qati             -- قاعدة هندسية: لا سقفَ له إلّا مقدّماتُه

/-! ## ٣. الحالة والمراحل -/

/-- رأيٌ سابق: نصُّه ورتبتُه، وهل يناقض القضيّةَ المبحوثة (يعطيه المودَع أو المستدعي). -/
structure Rai where
  nass : String
  rutba : Rutba
  yunaqid : Bool
  deriving DecidableEq, Repr

/-- الحالة σ: الدافعُ، والقضيّة بجهتها وقناتها ونوعِ ربطها، والمعلوماتُ السابقة (رتبُها)، والآراءُ السابقة، ونوعُ البحث، والوسمُ المدّعى. -/
structure Hala where
  dafi : String
  qawl : String
  jiha : Jiha
  qanat : Qanat
  rabt : NawRabt
  maalumat : List Rutba
  ara : List Rai
  bahthQati : Bool
  wasm : Option Rutba
  deriving Repr

/-- ما بعد S0: لا دافعَ فيه ولا وسم. -/
structure Talab where
  qawl : String
  jiha : Jiha
  qanat : Qanat
  rabt : NawRabt
  maalumat : List Rutba
  ara : List Rai
  bahthQati : Bool
  deriving Repr

inductive Illa | kharijNitaq | laysaFikran | bilaMaalumat | taarudMutasawi
  deriving DecidableEq, Repr

inductive Tasdiq | jazim | zannRajih
  deriving DecidableEq, Repr

inductive Natija
  | hukm (qawl : String) (jiha : Jiha) (rutba : Rutba) (tasdiq : Tasdiq)
  | mardud (qawl : String) (bi : String)     -- رُدّ الظنّيّ بقطعيٍّ سابق (ت48)
  | taliq (illa : Illa)
  | man (illa : Illa)
  deriving DecidableEq, Repr

/-- S0: يُختم الدافعُ والوسم؛ لا يمرّان إلى ما بعده (ت48: الموضوعية حصرُ البحث في موضوعه). -/
def s0 (h : Hala) : Talab := ⟨h.qawl, h.jiha, h.qanat, h.rabt, h.maalumat, h.ara, h.bahthQati⟩

/-- S8: المدحُ والذمّ للشرع وحده (ش٣ 339، 353). -/
def s8 (t : Talab) : Except Illa Talab := if t.jiha = .madhDhamm then .error .kharijNitaq else .ok t

/-- البوّابة: ما سقفُه «ليس فكرًا» لا يدخل. -/
def bawwaba (t : Talab) : Except Illa Talab := if saqf t.jiha t.qanat = .laFikr then .error .laysaFikran else .ok t

/-- S4: لا تصوّرَ بلا معلوماتٍ سابقة (ت16). -/
def s4 (t : Talab) : Except Illa Talab := if t.maalumat.isEmpty then .error .bilaMaalumat else .ok t

/-- S3: قاعدةُ الرأي السابق (ت48): في البحث القطعيّ يُترك كلُّ رأي، وفي الظنّيّ يُبقى القطعيُّ وحده. -/
def siyajRai (bahthQati : Bool) (ar : List Rai) : List Rai :=
  if bahthQati then [] else ar.filter (·.rutba == .qati)

/-- S6: الرتبةُ أدنى سقف الجهة والقناة وسقف الربط ورتب المقدّمات. -/
def s6 (t : Talab) : Rutba := iltiqaKull (saqf t.jiha t.qanat :: saqfRabt t.rabt :: t.maalumat)

/-- S7: التصديقُ الجازم للوجود القطعيّ وحده. -/
def s7 (j : Jiha) (r : Rutba) : Tasdiq := if j = .wujud ∧ r = .qati then .jazim else .zannRajih

def khatar : Illa → Natija
  | .kharijNitaq => .man .kharijNitaq
  | .laysaFikran => .man .laysaFikran
  | e => .taliq e

/-- **الطريقة: تركيبٌ ثابت للمراحل** (ت86: «كيفية دائمة»). -/
def think (h : Hala) : Natija :=
  match s8 (s0 h) >>= bawwaba >>= s4 with
  | .error e => khatar e
  | .ok t =>
    let r := s6 t
    match (siyajRai t.bahthQati t.ara).find? (·.yunaqid) with
    | some rai => if r = .qati then .taliq .taarudMutasawi else .mardud t.qawl rai.nass
    | none => .hukm t.qawl t.jiha r (s7 t.jiha r)

/-! ## ٤. الثوابت -/

/-- **INV-01: الدافعُ لا يؤثّر** — أيًّا كان. -/
theorem dafi_la_yuaththir (h : Hala) (d : String) : think { h with dafi := d } = think h := rfl

/-- **INV-08: الوسمُ لا يمنح رتبة.** -/
theorem wasm_la_yamnah (h : Hala) (w : Option Rutba) : think { h with wasm := w } = think h := rfl

theorem think_ok (h : Hala) {t : Talab} (ht : s8 (s0 h) >>= bawwaba >>= s4 = .ok t) :
    think h = match (siyajRai t.bahthQati t.ara).find? (·.yunaqid) with
      | some rai => if s6 t = .qati then .taliq .taarudMutasawi else .mardud t.qawl rai.nass
      | none => .hukm t.qawl t.jiha (s6 t) (s7 t.jiha (s6 t)) := by
  unfold think; rw [ht]

/-- **INV-05: المدحُ والذمّ ممنوعٌ قبل الشرع.** -/
theorem madh_mamnu (h : Hala) (hj : h.jiha = .madhDhamm) : think h = .man .kharijNitaq := by
  simp [think, s0, s8, hj, khatar, bind, Except.bind]

/-- **INV-11 وINV-02: الفرضُ والتخيّلُ والإدراكُ الشعوريّ ليست فكرًا** (ما لم تكن الجهةُ مدحًا وذمًّا فتُمنع قبلها). -/
theorem laysa_fikran (h : Hala) (hj : h.jiha ≠ .madhDhamm) (hq : saqf h.jiha h.qanat = .laFikr) :
    think h = .man .laysaFikran := by
  simp [think, s0, s8, hj, bawwaba, hq, khatar, bind, Except.bind]

theorem fard_takhayyul_shuur (h : Hala) (hj : h.jiha ≠ .madhDhamm)
    (hq : h.qanat = .fard ∨ h.qanat = .takhayyul ∨ h.qanat = .shuur) : think h = .man .laysaFikran := by
  apply laysa_fikran h hj
  rcases hq with hq | hq | hq <;> rw [hq]
  · exact saqf_fard _
  · exact saqf_takhayyul _
  · exact saqf_shuur _

/-- **INV-12: الحسُّ وحده لا يحصل منه فكر** — يُعلَّق الحكم. -/
theorem hiss_wahdahu (h : Hala) (hj : h.jiha ≠ .madhDhamm) (hq : saqf h.jiha h.qanat ≠ .laFikr)
    (hm : h.maalumat = []) : think h = .taliq .bilaMaalumat := by
  simp [think, s0, s8, hj, bawwaba, hq, s4, hm, khatar, bind, Except.bind]

/-- **INV-03: لا تصديقَ جازمًا إلّا لحكمٍ بالوجود قطعيّ.** -/
theorem jazim_wujud (h : Hala) (q : String) (j : Jiha) (r : Rutba)
    (hh : think h = .hukm q j r .jazim) : j = .wujud ∧ r = .qati := by
  unfold think at hh
  split at hh
  · rename_i e _
    cases e <;> simp [khatar] at hh
  · split at hh
    · simp only at hh; split at hh <;> simp at hh
    · simp only [Natija.hukm.injEq] at hh
      obtain ⟨_, hj, hr, h4⟩ := hh
      subst hj hr
      unfold s7 at h4
      split at h4
      · assumption
      · simp at h4

/-- **رتبةُ النتيجة لا تزيد على سقفها ولا على مقدّماتها** (قاعدة هندسية). -/
theorem s6_adna (t : Talab) :
    (s6 t).n ≤ (saqf t.jiha t.qanat).n ∧ (s6 t).n ≤ (saqfRabt t.rabt).n ∧ ∀ m ∈ t.maalumat, (s6 t).n ≤ m.n := by
  refine ⟨iltiqaKull_adna _ _ (by simp), iltiqaKull_adna _ _ (by simp), fun m hm => iltiqaKull_adna _ _ (by simp [hm])⟩

/-! ## ٥. قاعدةُ الرأي السابق والتعارض (ت27، ت48) -/

/-- **INV-04أ:** في البحث القطعيّ يُترك كلُّ رأيٍ سابق. -/
theorem siyaj_qati (ar : List Rai) : siyajRai true ar = [] := rfl

/-- **INV-04ب:** في البحث الظنّيّ لا يبقى إلّا القطعيّ … -/
theorem siyaj_zanni_qati (ar : List Rai) : ∀ x ∈ siyajRai false ar, x.rutba = .qati := by
  intro x hx; simp [siyajRai] at hx; exact hx.2

/-- **INV-04ج:** … ولا يُترك قطعيٌّ فيه. -/
theorem siyaj_zanni_yubqi (ar : List Rai) : ∀ x ∈ ar, x.rutba = .qati → x ∈ siyajRai false ar := by
  intro x hx hq; simp [siyajRai, hx, hq]

/-- **INV-13: إذا تعارض القطعيّ والظنّيّ يؤخذ القطعيّ ويُردّ الظنّيّ** (ت48). -/
theorem qati_yaghlib (h : Hala) {t : Talab} (ht : s8 (s0 h) >>= bawwaba >>= s4 = .ok t) (rai : Rai)
    (hf : (siyajRai t.bahthQati t.ara).find? (·.yunaqid) = some rai) (hr : s6 t ≠ .qati) :
    think h = .mardud t.qawl rai.nass := by
  rw [think_ok h ht, hf]; simp [hr]

/-- والقطعيّان المتعارضان: تعليقٌ (قاعدة هندسية). -/
theorem qatiyyan_taliq (h : Hala) {t : Talab} (ht : s8 (s0 h) >>= bawwaba >>= s4 = .ok t) (rai : Rai)
    (hf : (siyajRai t.bahthQati t.ara).find? (·.yunaqid) = some rai) (hr : s6 t = .qati) :
    think h = .taliq .taarudMutasawi := by
  rw [think_ok h ht, hf]; simp [hr]

/-! ## ٦. الحقيقة، والعمق والاستنارة (ت75، ت82، ت100–101) -/

/-- الحقيقة: حكمٌ بالوجود قطعيٌّ عن حسٍّ أو أثر (ت75 «مطابقة الفكر للواقع» المنقول بالإحساس؛ ت82). -/
def haqiqa (h : Hala) : Bool :=
  match think h with
  | .hukm _ .wujud .qati _ => h.qanat == .hiss || h.qanat == .athar
  | _ => false

theorem haqiqa_wujud (h : Hala) (hh : haqiqa h = true) : ∃ q t, think h = .hukm q .wujud .qati t := by
  unfold haqiqa at hh
  split at hh
  · rename_i q t heq; exact ⟨q, t, heq⟩
  · cases hh

/-- طبقاتُ المعلومات: العميقُ يضمّ طبقةً بعد طبقة (ت100)، والسطحيُّ الأولى وحدها. -/
def amiq {M : Type} (tabaqa : Nat → List M) : Nat → List M
  | 0 => tabaqa 0
  | k + 1 => amiq tabaqa k ++ tabaqa (k + 1)

def sathi {M : Type} (tabaqa : Nat → List M) : List M := amiq tabaqa 0

/-- المستنير: العميقُ مضافًا إليه ما حول الواقع وما يتعلّق به (ت101). -/
def mustanir {M : Type} (tabaqa : Nat → List M) (hawl : List M) (k : Nat) : List M := amiq tabaqa k ++ hawl

/-- **INV-09: المعلوماتُ تتّسع بالعمق ولا تنقص.** -/
theorem amiq_ratib {M : Type} (tabaqa : Nat → List M) : ∀ k l, k ≤ l → ∀ x ∈ amiq tabaqa k, x ∈ amiq tabaqa l := by
  intro k l hkl
  induction hkl with
  | refl => exact fun x hx => hx
  | step _ ih => intro x hx; simp [amiq, ih x hx]

/-- **«كل فكر مستنير هو تفكير عميق»** (ت101). -/
theorem mustanir_amiq {M : Type} (tabaqa : Nat → List M) (hawl : List M) (k : Nat) :
    ∀ x ∈ amiq tabaqa k, x ∈ mustanir tabaqa hawl k := by
  intro x hx; simp [mustanir, hx]

theorem sathi_amiq {M : Type} (tabaqa : Nat → List M) (k : Nat) : ∀ x ∈ sathi tabaqa, x ∈ amiq tabaqa k :=
  amiq_ratib tabaqa 0 k (Nat.zero_le _)

/-! ## ٧. التفكير بالعمل: الغاية والجدّيّة، والأسلوب والوسيلة (ت83–92، ت106) -/

/-- الغاية: محدّدةٌ مرئيّة (ت92)، ومستواها؛ والأعمالُ المادّيّة بمستوياتها؛ والدعوى. -/
structure Amal where
  ghaya : Option Nat          -- none: غيرُ محدّدة
  mariyya : Bool              -- «مرئية للبصر أو مرئية للبصيرة»
  aamal : List Nat
  iddiaJidd : Bool            -- «قول المرء إنه جاد»
  deriving Repr

/-- **الجدّيّة** (ت106): غايةٌ محدّدة مرئيّة، وعملٌ مادّيٌّ في مستواها؛ والدعوى لا تدخل. -/
def jadd (a : Amal) : Bool :=
  match a.ghaya with
  | none => false
  | some g => a.mariyya && a.aamal.any (· ≥ g)

theorem iddia_la_yakfi (a : Amal) (b : Bool) : jadd { a with iddiaJidd := b } = jadd a := rfl

theorem bila_ghaya_la_jadd (a : Amal) (h : a.ghaya = none) : jadd a = false := by simp [jadd, h]

theorem bila_amal_la_jadd (a : Amal) (h : a.aamal = []) : jadd a = false := by
  unfold jadd; split <;> simp [h]

/-- عملٌ دون مستوى الغاية ليس جدًّا. -/
theorem dun_almustawa (a : Amal) (g : Nat) (hg : a.ghaya = some g) (h : ∀ x ∈ a.aamal, x < g) : jadd a = false := by
  unfold jadd; rw [hg]
  simp only [Bool.and_eq_false_iff, List.any_eq_false, decide_eq_true_eq]
  exact Or.inr fun x hx => Nat.not_le.2 (h x hx)

/-- سجلُّ الأساليب والوسائل: الأسلوبُ لنوع العمل (ت83)، والوسيلةُ لأسلوبها (ت88). -/
structure Sijill where
  asalib : String → List String
  wasail : String → List String

structure Khitta where
  amal : String
  uslub : String
  wasail : List String
  deriving Repr

def khittaSahiha (s : Sijill) (k : Khitta) : Bool :=
  (s.asalib k.amal).contains k.uslub && k.wasail.all fun w => (s.wasail k.uslub).contains w

/-- **لا وسيلةَ إلّا لأسلوب الخطّة، ولا أسلوبَ إلّا لنوع عملها.** -/
theorem khitta_sahiha (s : Sijill) (k : Khitta) (h : khittaSahiha s k = true) :
    k.uslub ∈ s.asalib k.amal ∧ ∀ w ∈ k.wasail, w ∈ s.wasail k.uslub := by
  simp [khittaSahiha] at h
  exact ⟨h.1, h.2⟩

/-! ## ٨. التفكير السياسي: الشروطُ الخمسة (ت145–146) -/

structure Siyasi where
  tatabbu : Bool       -- أوّلًا: تتبّعُ الوقائع والأخبار
  maalumat : Bool      -- ثانيًا: معلوماتٌ عن ماهية الوقائع
  adamTajrid : Bool    -- ثالثًا: عدمُ تجريد الوقائع من ظروفها وعدمُ تعميمها
  tamyiz : Bool        -- رابعًا: تمييزُ الخبر بتمحيصه
  rabt : Bool          -- خامسًا: ربطُ الخبر بالمعلومات
  deriving Repr

def naqis (s : Siyasi) : List String :=
  [("تتبّع الأخبار", s.tatabbu), ("المعلومات عن ماهية الوقائع", s.maalumat),
   ("عدم التجريد والتعميم", s.adamTajrid), ("تمييز الخبر بتمحيصه", s.tamyiz),
   ("ربط الخبر بالمعلومات", s.rabt)].filterMap fun (n, b) => if b then none else some n

def siyasi (s : Siyasi) : Except (List String) Unit := if naqis s = [] then .ok () else .error (naqis s)

/-- **لا ناقصَ إلّا إن نقص شرط، ويُسمّى الناقص** (فيُعلَّق الحكمُ السياسيّ باسمه). -/
theorem siyasi_kamil (s : Siyasi) :
    naqis s = [] ↔ (s.tatabbu && s.maalumat && s.adamTajrid && s.tamyiz && s.rabt) = true := by
  rcases s with ⟨a, b, c, d, e⟩
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

theorem siyasi_taliq (s : Siyasi) (h : naqis s ≠ []) : siyasi s = .error (naqis s) := by
  simp [siyasi, h]

/-! ## ٩. الوصف (لمحرّك الإجابة) -/

def ismRutba : Rutba → String
  | .laFikr => "ليس فكرًا" | .zanni => "ظنّيّ" | .qati => "قطعيّ"

def ismIlla : Illa → String
  | .kharijNitaq => "خارج النطاق قبل الشرع (ش٣ 339، 353)"
  | .laysaFikran => "ليس فكرًا (ت53، ت58، ت18)"
  | .bilaMaalumat => "بلا معلوماتٍ سابقة (ت16)"
  | .taarudMutasawi => "تعارضُ متساويين"

def wasf : Natija → String
  | .hukm _ _ r .jazim => s!"تصديقٌ جازم ({ismRutba r})"
  | .hukm _ _ r .zannRajih => s!"ظنٌّ راجح ({ismRutba r})"
  | .mardud _ b => s!"مردودٌ بالقطعيّ «{b}» (ت48)"
  | .taliq e => s!"تعليق: {ismIlla e}"
  | .man e => s!"منع: {ismIlla e}"

/-! ## ١٠. الشواهد -/

def halaShahid : Hala :=
  ⟨"جوع", "خرج صوتٌ من شيء", .wujud, .hiss, .wujudAnHissAwAthar, [.qati], [], true, some .zanni⟩

/-- الحكمُ بوجود شيءٍ خرج منه الصوت قطعيّ (ت55)، والدافعُ «جوع» والوسمُ «ظنّيّ» لا يغيّرانه. -/
theorem shahid_sawt :
    think halaShahid = .hukm "خرج صوتٌ من شيء" .wujud .qati .jazim ∧ haqiqa halaShahid = true := by decide

/-- صفتُه من أثره ليست فكرًا (ت56). -/
theorem shahid_sifa_athar : think { halaShahid with jiha := .sifa, qanat := .athar } = .man .laysaFikran := by decide

/-- في بحثٍ ظنّيّ، حكمٌ ظنّيّ يناقضه رأيٌ قطعيٌّ سابق: يُردّ (ت48)؛ ورأيٌ ظنّيٌّ سابق يناقضه: يُترك ولا يُردّ به. -/
theorem shahid_rai :
    think { halaShahid with jiha := .sifa, bahthQati := false, ara := [⟨"رأي قطعي", .qati, true⟩] } =
      .mardud "خرج صوتٌ من شيء" "رأي قطعي" ∧
    think { halaShahid with jiha := .sifa, bahthQati := false, ara := [⟨"رأي ظني", .zanni, true⟩] } =
      .hukm "خرج صوتٌ من شيء" .sifa .zanni .zannRajih := by decide

end SimAql
end Aql
