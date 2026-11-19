/-
  Nizam/Mudir.lean — نواةُ مدير الوكلاء (وكيل NTP): من البرومبت إلى القسمة، ثمّ القرار، ثمّ الخطّة على وكلاء Mashru القائمين،
  ثمّ النتيجة الجامعة. كلُّ ما هنا دوالُّ خالصةٌ يستدعيها التنفيذيُّ `mudir` (`Qari/Mudir.lean`) بأعيانها، فما بُرهن هنا هو ما يجري.

  **الطلب** (قولُ المالك 2026-11-19، 16:11 بتوقيت عمّان، بلفظه): «اعتبر ان نظام النظر والبيان محاكاة لقدرة Copilot calude ووفق هذا النظام
  يستطيع الوكيل في NTP ان يتلقى اي برومبت ويعطي إجابة او ينفذ امر وفق ntp المطور … ابني في mashru نظام مدير لوكلاء يحققون هذا الهدف ويكون
  فعالا بالاستجابة انت خبير نفذ انت مفوض ويجب ان تستعمل كل القدرات التي بنيناها في Mashru وتوظف كل امكاناته». والتصميمُ قرارُ البنّاء،
  ووثيقتُه `hawkama/مدير_الوكلاء.md`.

  **ما يُستعمل من Mashru** (مقروءٌ في الجلسة):
  * `Nizam.Talab.qisma` — قرارُ المالك ٢: «الأمر والالتماس والسؤال "لا حكم" بلا مقام». المقامُ هنا القناةُ التي جاء منها الطلب
    (`Qanat`): المالكُ مستعلٍ على الوكيل فطلبُه أمر، والوكيلُ النظيرُ مساوٍ فطلبُه التماس، والمجهولُ لا رتبةَ له فطلبُه «لا حكم» فلا يُنفَّذ.
    وتعيينُ القناة رتبةً قراءةُ البنّاء (س415 يجعل الرتبةَ حالَ المتكلّم والمخاطَب، والقناةُ شاهدُها في الجلسة).
  * `Nizam.tarkib` (`Nizam/Asas.lean`): القرارُ تركيبُ جسرين — القسمةِ ثمّ الترخيص — فلا ترخيصَ إلّا بترخيص ما قبله.
  * الوكلاء التنفيذيّون القائمون: `qari` (القارئ)، `tarkib` (القراءة بالعوامل)، `athar` (أثرُ العُقَد والقوّة)، `silsila` (سلسلةُ الشهادات)،
    `faahis` (الفاحص وسؤالُ المخزن بالدلالات الثلاث)، ومعالجُ NTP (`NTP.Wasl.hukm`، `NTP.Wasl.khawassOf`) يُستدعى في العمليّة نفسها.

  **ما يُبرهن هنا (لكلّ مدخل):**
  ١. القسمة: بلا مقامٍ لا أمر (`bila_maqam_la_tanfidh`)، والمالكُ وحده يأمر (`amr_iff_malik`).
  ٢. القرار: الأمرُ المحظور (دمجٌ، ختمٌ، حذفٌ، دفع) لا يُرخَّص من أيّ قناة (`mahzur_marfud`)، والمجهولُ مرفوضٌ باسمه لا مخمَّن
     (`majhul_marfud`)، والإيداعُ المقترح بأمر المالك وحده (`taallam_malik`).
  ٣. الخطّة: القرارُ المرفوض لا خطوةَ له (`rafd_la_khitta`)، فلا يُشغَّل وكيل؛ وكلُّ خطوةٍ قراءةٌ إلّا المتعلّم، وهو اقتراحٌ لا ختم
     (`khatwa_qiraa_aw_iqtirah`)؛ والمتعلّمُ لا يدخل خطّةً إلّا من قناة المالك (`mutaallim_malik`).
  ٤. النتيجة: خطأُ خطوةٍ لا يُخفيه نجاحُ غيرها (`khata_yaghlib`)، والنجاحُ الجامع نجاحُ كلّ خطوة (`najah_iff`)، وخروجٌ بغير صفرٍ خطأٌ
     (`khuruj_khata`)، والقرارُ المرفوض رفضٌ جامع (`rafd_jami`).
  ٥. التصديق: الإنشاءُ لا يُصدَّق ولا يُكذَّب (`insha_ghayr_qabil`)، والخبرُ بلا شاهد واقعٍ «لا حكم» على الواقع (`khabar_bila_shahid`).
  ٦. شواهدُ على برومبتات بأعيانها (`shawahid_qarar`، على الشاهد).

  **حدود (معلنة):** سجلُّ الأوامر (`sijillAwamir`) وقوالبُ السؤال تعيينُ البنّاء، يطابق اللفظَ مجرَّدًا من الحركات تطابقًا تامًّا، وليس حكمًا لغويًّا
  على صيغة («طِرْ» ليست في السجلّ فلا تُنفَّذ، ولا يُستنتج منها شيء). والقسمةُ من القناة لا من اللفظ. ونتيجةُ كلّ خطوةٍ تُقرأ من مخرج وكيلها
  بعلاماتٍ معلنة (`natijaKhatwa`)؛ فصدقُ ما يقوله الوكيل يبقى على وكيله وبراهينه، لا على المدير. وشبكةُ NTP المستعملة شاهدٌ مبنيّ
  (`NTP.Wasl.shabakaWasl`) لا مودَع.
  بلا sorry ولا axiom ولا native_decide.
-/
import Nizam.Talab
import Madlul.NTP.Wasl

set_option autoImplicit false

namespace Nizam.Mudir

/-! ## ١. القناةُ والقسمة -/

/-- قناةُ الطلب: مَن أرسله إلى المدير. -/
inductive Qanat | malik | wakil | majhul
  deriving DecidableEq, Repr

/-- رتبةُ المرسِل من الوكيل (المقام): المالكُ مستعلٍ، والوكيلُ النظيرُ مساوٍ، والمجهولُ بلا رتبة. -/
def rutbaOf : Qanat → Option Talab.Rutba
  | .malik => some .istila
  | .wakil => some .tasawi
  | .majhul => none

/-- قسمُ الطلب بصيغة «افعل»: قرارُ المالك ٢ بعينه (`Talab.qisma`) على مقام القناة. -/
def qismOf (q : Qanat) : Hukm Talab.Qism := Talab.qisma (rutbaOf q) .talabTahsil

theorem bila_maqam_la_qisma : qismOf .majhul = .laHukm := rfl

theorem amr_iff_malik (q : Qanat) : qismOf q = .murakhkhas .amr ↔ q = .malik := by
  cases q <;> simp [qismOf, rutbaOf, Talab.qisma, Talab.qismBiRutba]

/-! ## ٢. السجلّ: الأوامرُ المرخَّصة والمحظورة -/

/-- الأوامرُ التي يرخّصها المدير، كلٌّ على وكيلٍ قائم في Mashru. -/
inductive Amr
  | iqra      -- اقرأ: القارئ (الدال وحده والمخزن)
  | aarib     -- أعرب: القراءةُ بالعوامل ثمّ أثرُ العُقَد
  | tatabba   -- تتبّع: سلسلةُ الشهادات
  | isal      -- اسأل: المخزنُ بالدلالات الثلاث
  | ifhas     -- افحص: الفاحصُ على المخزن كلّه
  | sannif    -- صنّف: معالجُ NTP على شبكته
  | taallam   -- تعلّم: اقتراحُ إيداعٍ لا ختمُه
  | aard      -- اعرض: سجلُّ الأوامر
  deriving DecidableEq, Repr

/-- ما لا يرخّصه المدير أبدًا: سلطةُ المالك في الجلسة (CLAUDE.md، «السلطة»). -/
inductive Mahzur | idmaj | ikhtim | ihdhif | idfa
  deriving DecidableEq, Repr

inductive Fil | murakhkhas (a : Amr) | mahzur (m : Mahzur)
  deriving DecidableEq, Repr

/-- الحركاتُ والشدّةُ والسكونُ والألفُ الخنجريّة والتطويل: تُجرَّد قبل المطابقة. -/
def haraka (c : Char) : Bool := (c.toNat ≥ 0x064B && c.toNat ≤ 0x0652) || c.toNat == 0x0670 || c.toNat == 0x0640

/-- النصوصُ هنا قوائمُ محارف، لتُحسب الشواهدُ في النواة (`decide`). -/
def tajridL (s : List Char) : List Char := s.filter (fun c => !haraka c)

def tajrid (s : String) : String := String.ofList (tajridL s.toList)

/-- علاماتُ الوقف بعد لفظ الأمر تُقصّ: «اقْرَأْ:» لفظُه «اقرأ». -/
def qassAlamat (s : List Char) : List Char :=
  (s.reverse.dropWhile (fun c => c == ':' || c == '،' || c == '؛' || c == ',')).reverse

/-- سجلُّ الأوامر: لفظُها مجرَّدًا وما يقابله (تعيين البنّاء). -/
def sijillAwamir : List (String × Fil) :=
  [("اقرأ", .murakhkhas .iqra), ("اقرا", .murakhkhas .iqra),
   ("أعرب", .murakhkhas .aarib), ("اعرب", .murakhkhas .aarib),
   ("تتبع", .murakhkhas .tatabba),
   ("اسأل", .murakhkhas .isal), ("اسال", .murakhkhas .isal),
   ("افحص", .murakhkhas .ifhas),
   ("صنف", .murakhkhas .sannif),
   ("تعلم", .murakhkhas .taallam),
   ("اعرض", .murakhkhas .aard),
   ("ادمج", .mahzur .idmaj), ("اختم", .mahzur .ikhtim), ("احذف", .mahzur .ihdhif), ("ادفع", .mahzur .idfa)]

def bahth (w : List Char) : Option Fil := (sijillAwamir.find? (·.1.toList == tajridL (qassAlamat w))).map (·.2)

/-- أثرُ الأمر: قراءةٌ لا تكتب، أو اقتراحٌ يكتب في مجلّد الاقتراحات وحده. -/
inductive Athar | qiraa | iqtirah
  deriving DecidableEq, Repr

def Amr.nawAthar : Amr → Athar
  | .taallam => .iqtirah
  | _ => .qiraa

/-- ما يرخّصه كلُّ قسم: الأمرُ كلَّ أمر، والالتماسُ ما يقرأ وحده، والسؤالُ (تسفّلٌ إلى الوكيل) لا شيء. -/
def ruhsa : Talab.Qism → Amr → Bool
  | .amr, _ => true
  | .iltimas, a => a.nawAthar == .qiraa
  | .sual, _ => false

/-! ## ٣. القرار -/

inductive Rafd
  | farigh                                   -- لا نصّ
  | bilaMaqam (a : Amr)                      -- أمرٌ بلا مقام (قناةٌ مجهولة)
  | ghayrMurakhkhas (q : Talab.Qism) (a : Amr) -- قسمٌ لا يرخّص هذا الأمر
  | mahzur (m : Mahzur)                      -- سلطةُ المالك في الجلسة
  | bilaHujja (a : Amr)                      -- أمرٌ يحتاج نصًّا ولا نصّ بعده
  deriving DecidableEq, Repr

inductive Qarar
  | tanfidh (a : Amr) (hujja : String)
  | qiraa (nass : String)
  | rafd (r : Rafd)
  deriving DecidableEq, Repr

/-- قسمةُ النصّ على المسافة (U+0020)، بلا كلماتٍ فارغة. -/
def qasm : List Char → List (List Char)
  | [] => [[]]
  | c :: cs =>
    if c == ' ' then [] :: qasm cs
    else match qasm cs with
      | w :: ws => (c :: w) :: ws
      | [] => [[c]]

def kalimat (s : List Char) : List (List Char) := (qasm s).filter (· ≠ [])

def wasl : List (List Char) → List Char
  | [] => []
  | [w] => w
  | w :: ws => w ++ ' ' :: wasl ws

/-- علامةُ الاستفهام والمسافةُ تُقصّان من آخر الحجّة. -/
def qassIstifham (s : List Char) : List Char :=
  (s.reverse.dropWhile (fun c => c == '؟' || c == '?' || c == ' ')).reverse

def yahtajHujja : Amr → Bool
  | .ifhas | .aard => false
  | _ => true

/-- الترخيصُ جسرٌ بعد القسمة (`Nizam.tarkib`): لا يُرخَّص أمرٌ إلّا بقسمٍ مرخَّصٍ يرخّصه. -/
def tarkhis (a : Amr) : Jisr Talab.Qism Amr := fun q =>
  if ruhsa q a then .murakhkhas a else .mumtani "قسمٌ لا يرخّص هذا الأمر"

def qararAmr (q : Qanat) (a : Amr) (hujja : String) : Qarar :=
  match Nizam.tarkib (fun (_ : Talab.Madlul) => qismOf q) (tarkhis a) .talabTahsil with
  | .murakhkhas a' =>
    if yahtajHujja a' && hujja.isEmpty then .rafd (.bilaHujja a') else .tanfidh a' hujja
  | .laHukm => .rafd (.bilaMaqam a)
  | .mumtani _ =>
    match qismOf q with
    | .murakhkhas k => .rafd (.ghayrMurakhkhas k a)
    | _ => .rafd (.bilaMaqam a)

/-- القرار على برومبتٍ من قناة: الأمرُ بلفظه في السجلّ، أو قالبُ «ما معنى …» (سؤالٌ يقرأ)، أو القراءة. -/
def qararL (q : Qanat) (nass : List Char) : Qarar :=
  match kalimat nass with
  | [] => .rafd .farigh
  | w :: baqi =>
    match bahth w with
    | some (.mahzur m) => .rafd (.mahzur m)
    | some (.murakhkhas a) => qararAmr q a (String.ofList (qassIstifham (wasl baqi)))
    | none =>
      match baqi with
      | m :: x :: r =>
        if tajridL w == "ما".toList && tajridL m == "معنى".toList then
          .tanfidh .isal (String.ofList (qassIstifham (wasl (x :: r))))
        else .qiraa (String.ofList nass)
      | _ => .qiraa (String.ofList nass)

def qarar (q : Qanat) (nass : String) : Qarar := qararL q nass.toList

theorem farigh_marfud (q : Qanat) : qarar q "" = .rafd .farigh := by cases q <;> decide

theorem qararAmr_malik (a : Amr) (h : String) :
    qararAmr .malik a h = if yahtajHujja a && h.isEmpty then .rafd (.bilaHujja a) else .tanfidh a h := by
  cases a <;> rfl

theorem qararAmr_majhul (a : Amr) (h : String) : qararAmr .majhul a h = .rafd (.bilaMaqam a) := by
  cases a <;> rfl

/-- **بلا مقامٍ لا تنفيذ:** أمرٌ من قناةٍ مجهولة مرفوضٌ باسم المقام الناقص. -/
theorem bila_maqam_la_tanfidh (a : Amr) (h : String) (b : Amr) (x : String) :
    qararAmr .majhul a h ≠ .tanfidh b x := by
  rw [qararAmr_majhul]; intro e; cases e

theorem qararAmr_tanfidh (q : Qanat) (a b : Amr) (h x : String) (e : qararAmr q a h = .tanfidh b x) :
    b = a ∧ (q = .malik ∨ (q = .wakil ∧ a.nawAthar = .qiraa)) := by
  cases q <;> cases a <;> simp_all [qararAmr, Nizam.tarkib, Hukm.bind, qismOf, rutbaOf, Talab.qisma, Talab.qismBiRutba,
    tarkhis, ruhsa, Amr.nawAthar, yahtajHujja] <;> split at e <;> simp_all

/-- **المحظورُ مرفوضٌ من أيّ قناة.** -/
theorem mahzur_marfud (q : Qanat) (n : String) (w : List Char) (baqi : List (List Char)) (m : Mahzur)
    (hk : kalimat n.toList = w :: baqi) (hb : bahth w = some (.mahzur m)) : qarar q n = .rafd (.mahzur m) := by
  simp [qarar, qararL, hk, hb]

/-- **المجهولُ لا يُخمَّن:** لفظٌ ليس في السجلّ لا يصير أمرًا؛ فالقرارُ قراءةٌ للنصّ كما هو أو قالبُ «ما معنى». -/
theorem majhul_marfud (q : Qanat) (n : String) (w : List Char) (baqi : List (List Char))
    (hk : kalimat n.toList = w :: baqi) (hb : bahth w = none)
    (a : Amr) (x : String) (e : qarar q n = .tanfidh a x) : a = .isal := by
  simp only [qarar, qararL, hk, hb] at e
  split at e
  · split at e
    · cases e; rfl
    · cases e
  · cases e

/-- **الإيداعُ المقترح بأمر المالك وحده.** -/
theorem taallam_malik (q : Qanat) (n x : String) (e : qarar q n = .tanfidh .taallam x) : q = .malik := by
  simp only [qarar, qararL] at e
  split at e
  · cases e
  · split at e
    · cases e
    · rcases qararAmr_tanfidh q _ _ _ _ e with ⟨rfl, h | ⟨_, h⟩⟩
      · exact h
      · cases h
    · split at e
      · split at e
        · cases e
        · cases e
      · cases e

/-! ## ٤. الوكلاءُ والخطّة -/

/-- الوكلاء: تنفيذيّاتُ Mashru القائمة، ومعالجُ NTP والمتعلّمُ في العمليّة نفسها. -/
inductive Wakil | qari | tarkib | athar | silsila | faahis | faahisSual | muallij | mutaallim
  deriving DecidableEq, Repr

def Wakil.ism : Wakil → String
  | .qari => "qari" | .tarkib => "tarkib" | .athar => "athar" | .silsila => "silsila"
  | .faahis => "faahis" | .faahisSual => "faahis --sual" | .muallij => "NTP.Wasl" | .mutaallim => "mutaallim"

def Wakil.nawAthar : Wakil → Athar
  | .mutaallim => .iqtirah
  | _ => .qiraa

structure Khatwa where
  wakil : Wakil
  hujja : String
  deriving DecidableEq, Repr

/-- الدلالاتُ الثلاث في المخزن (ج3 س737): المطابقةُ والتضمّنُ والالتزام، بادئاتُ قضايا الفاحص (`Faahis.qadiyyaIsm`). -/
def dalalat : List String := ["mutabaqa:", "tadammun:", "iltizam:"]

def khittaAmr : Amr → String → List Khatwa
  | .iqra, x => [⟨.qari, x⟩]
  | .aarib, x => [⟨.tarkib, x⟩, ⟨.athar, x⟩]
  | .tatabba, x => [⟨.silsila, x⟩]
  | .isal, x => dalalat.map fun d => ⟨.faahisSual, d ++ tajrid x⟩
  | .ifhas, _ => [⟨.faahis, ""⟩]
  | .sannif, x => [⟨.muallij, tajrid x⟩]
  | .taallam, x => [⟨.athar, x⟩, ⟨.mutaallim, x⟩]
  | .aard, _ => []

def khitta : Qarar → List Khatwa
  | .tanfidh a x => khittaAmr a x
  | .qiraa n => [⟨.athar, n⟩]
  | .rafd _ => []

/-- **المرفوضُ لا خطوةَ له.** -/
theorem rafd_la_khitta (r : Rafd) : khitta (.rafd r) = [] := rfl

theorem khittaAmr_all (a : Amr) (x : String) :
    (khittaAmr a x).all (fun k => k.wakil != .mutaallim || a == .taallam) = true := by
  cases a <;> simp [khittaAmr, dalalat]

theorem khittaAmr_mutaallim (a : Amr) (x : String) (k : Khatwa) (hk : k ∈ khittaAmr a x) (hw : k.wakil = .mutaallim) :
    a = .taallam := by
  have := List.all_eq_true.1 (khittaAmr_all a x) k hk
  simp [hw] at this
  exact this

/-- **كلُّ خطوةٍ قراءةٌ إلّا المتعلّم، وهو اقتراح.** -/
theorem khatwa_qiraa_aw_iqtirah (k : Khatwa) : k.wakil.nawAthar = .qiraa ∨ k.wakil = .mutaallim := by
  cases h : k.wakil <;> simp [Wakil.nawAthar]

/-- **المتعلّمُ لا يدخل خطّةً إلّا من قناة المالك.** -/
theorem mutaallim_malik (q : Qanat) (n : String) (k : Khatwa) (hk : k ∈ khitta (qarar q n)) (hw : k.wakil = .mutaallim) :
    q = .malik := by
  cases e : qarar q n with
  | tanfidh a x =>
    rw [e] at hk
    have := khittaAmr_mutaallim a x k hk hw
    subst this
    exact taallam_malik q n x e
  | qiraa m => rw [e] at hk; simp [khitta] at hk; subst hk; simp at hw
  | rafd r => rw [e] at hk; simp [khitta] at hk

/-! ## ٥. النتيجة -/

/-- نتيجةُ الخطوة: حكمٌ صدر (مرخَّصٌ أو ممتنع)، أو لا حكم (معلَّقٌ باسمه)، أو مدخلٌ مرفوضٌ باسمه، أو خطأُ تنفيذ. -/
inductive Natija | najah | laHukm | rafd | khata
  deriving DecidableEq, Repr

def Natija.thiql : Natija → Nat
  | .najah => 0 | .laHukm => 1 | .rafd => 2 | .khata => 3

def ashadd (a b : Natija) : Natija := if b.thiql > a.thiql then b else a

/-- النتيجةُ الجامعة: أشدُّ نتائج الخطوات. -/
def jam (l : List Natija) : Natija := l.foldl ashadd .najah

theorem thiql_ashadd (a b : Natija) : (ashadd a b).thiql = max a.thiql b.thiql := by
  unfold ashadd; split <;> omega

theorem thiql_foldl (l : List Natija) (a : Natija) :
    (l.foldl ashadd a).thiql = l.foldl (fun m x => max m x.thiql) a.thiql := by
  induction l generalizing a with
  | nil => rfl
  | cons x xs ih => simp only [List.foldl, ih, thiql_ashadd]

theorem foldl_max_ge (l : List Natija) (m : Nat) : m ≤ l.foldl (fun m x => max m x.thiql) m := by
  induction l generalizing m with
  | nil => exact Nat.le_refl _
  | cons x xs ih => exact Nat.le_trans (Nat.le_max_left _ _) (ih _)

theorem foldl_max_mem (l : List Natija) (m : Nat) (x : Natija) (hx : x ∈ l) :
    x.thiql ≤ l.foldl (fun m x => max m x.thiql) m := by
  induction l generalizing m with
  | nil => cases hx
  | cons y ys ih =>
    rcases List.mem_cons.1 hx with rfl | h
    · exact Nat.le_trans (Nat.le_max_right _ _) (foldl_max_ge ys _)
    · exact ih _ h

theorem thiql_khata (n : Natija) (h : n.thiql ≥ 3) : n = .khata := by cases n <;> simp_all [Natija.thiql]

theorem thiql_le_3 (l : List Natija) (m : Nat) (hm : m ≤ 3) : l.foldl (fun m x => max m x.thiql) m ≤ 3 := by
  induction l generalizing m with
  | nil => exact hm
  | cons x xs ih => apply ih; cases x <;> simp [Natija.thiql] <;> omega

/-- **خطأُ خطوةٍ لا يُخفيه نجاحُ غيرها.** -/
theorem khata_yaghlib (l : List Natija) (h : Natija.khata ∈ l) : jam l = .khata := by
  apply thiql_khata
  unfold jam; rw [thiql_foldl]
  exact foldl_max_mem l _ _ h

/-- **النجاحُ الجامع نجاحُ كلّ خطوة.** -/
theorem najah_iff (l : List Natija) : jam l = .najah ↔ ∀ x ∈ l, x = .najah := by
  constructor
  · intro h x hx
    have h1 : (jam l).thiql = 0 := by rw [h]; rfl
    unfold jam at h1; rw [thiql_foldl] at h1
    have := foldl_max_mem l Natija.najah.thiql x hx
    cases x <;> simp_all [Natija.thiql]
  · intro h
    unfold jam
    induction l with
    | nil => rfl
    | cons x xs ih =>
      have hx : x = .najah := h x (by simp)
      subst hx
      simpa [List.foldl, ashadd, Natija.thiql] using ih (fun y hy => h y (by simp [hy]))

/-- خطواتٌ بدائل (أسئلةُ الدلالات الثلاث): يكفي حكمٌ واحد، والخطأُ يغلب. -/
def jamBadil (l : List Natija) : Natija :=
  if l.contains .khata then .khata else if l.contains .najah then .najah else jam l

theorem khata_yaghlib_badil (l : List Natija) (h : Natija.khata ∈ l) : jamBadil l = .khata := by
  simp [jamBadil, List.contains_iff_mem, h]

theorem badil_najah (l : List Natija) (h1 : Natija.najah ∈ l) (h2 : Natija.khata ∉ l) : jamBadil l = .najah := by
  simp [jamBadil, h1, h2]

/-- النتيجةُ الجامعة للقرار: المرفوضُ رفض، والسؤالُ بالدلالات بدائل، وإلّا أشدُّ الخطوات. -/
def natijaJamia (qr : Qarar) (l : List Natija) : Natija :=
  match qr with
  | .rafd _ => .rafd
  | .tanfidh .isal _ => jamBadil l
  | _ => jam l

theorem rafd_jami (r : Rafd) (l : List Natija) : natijaJamia (.rafd r) l = .rafd := rfl

/-- **الخطأُ يغلب في كلّ قرار.** -/
theorem khata_jami (qr : Qarar) (l : List Natija) (h : Natija.khata ∈ l) (hr : ∀ r, qr ≠ .rafd r) :
    natijaJamia qr l = .khata := by
  cases qr with
  | rafd r => exact absurd rfl (hr r)
  | qiraa n => exact khata_yaghlib l h
  | tanfidh a x =>
    cases a <;> first | exact khata_yaghlib_badil l h | exact khata_yaghlib l h

/-- فيه النصّ `p`؟ -/
def fihiL (p : List Char) : List Char → Bool
  | [] => p.isEmpty
  | c :: cs => p.isPrefixOf (c :: cs) || fihiL p cs

def fihi (s p : String) : Bool := fihiL p.toList s.toList

def bada (s p : String) : Bool := p.toList.isPrefixOf s.toList

/-- نتيجةُ الخطوة من خروج وكيلها ومخرجه، بعلاماتٍ معلنة من مخرجه (مقروءةٍ في الجلسة):
    الخروجُ بغير صفرٍ خطأ؛ والقارئُ «مرفوضة باسمها» رفض؛ وtarkib «RAFD» رفضٌ و«لا_حكم» لا حكم؛ وathar وsilsila «مدخل_فاسد» رفضٌ
    و«معلق» لا حكم؛ وسؤالُ الفاحص «لا حكم:» لا حكم؛ وما سوى ذلك حكمٌ صدر. -/
def natijaKhatwa (w : Wakil) (khuruj : Nat) (makhraj : String) : Natija :=
  if khuruj ≠ 0 then .khata else
  match w with
  | .qari => if fihi makhraj "مرفوضة باسمها" then .rafd else .najah
  | .tarkib => if fihi makhraj "\tRAFD\t" then .rafd else if fihi makhraj "\tلا_حكم" then .laHukm else .najah
  | .athar | .silsila =>
    if fihi makhraj "\tJUMLA\tمدخل_فاسد" || fihi makhraj "\tJUMLA\t1\tمدخل_فاسد" then .rafd
    else if fihi makhraj "\tJUMLA\tمعلق" || fihi makhraj "\tJUMLA\t1\tمعلق" || fihi makhraj "\tJUMLA\tلا_حكم" then .laHukm
    else .najah
  | .faahisSual => if bada makhraj "لا حكم" then .laHukm else .najah
  | .faahis | .mutaallim => .najah
  | .muallij => if bada makhraj "لا حكم" || fihi makhraj "لا جنس" then .laHukm else .najah

/-- **الخروجُ بغير صفرٍ خطأٌ** أيًّا كان المخرج. -/
theorem khuruj_khata (w : Wakil) (k : Nat) (s : String) (h : k ≠ 0) : natijaKhatwa w k s = .khata := by
  simp [natijaKhatwa, h]

/-! ## ٦. التصديق -/

/-- حكمُ التصديق على جملةٍ من قوّتها في `athar` (`Jisr.SakkJumla`): الخبرُ يُسأل عن واقعه، والإنشاءُ لا يُسأل. -/
inductive Tasdiq
  | laHukmBilaShahid   -- خبر: لا شاهدَ واقعٍ مودَع في هذه الخطّة، فلا حكم على الواقع (الغيابُ ليس تكذيبًا)
  | ghayrQabil         -- إنشاء: لا يُصدَّق ولا يُكذَّب
  | laHukm             -- القوّةُ نفسها لا حكم
  deriving DecidableEq, Repr

def tasdiqOf (quwwa : String) : Tasdiq :=
  if bada quwwa "إنشاء" then .ghayrQabil
  else if bada quwwa "خبر" then .laHukmBilaShahid
  else .laHukm

theorem insha_ghayr_qabil (q : String) (h : bada q "إنشاء" = true) : tasdiqOf q = .ghayrQabil := by
  simp [tasdiqOf, h]

theorem khabar_bila_shahid (q : String) (h1 : bada q "إنشاء" = false) (h2 : bada q "خبر" = true) :
    tasdiqOf q = .laHukmBilaShahid := by
  simp [tasdiqOf, h1, h2]

theorem shawahid_tasdiq :
    tasdiqOf "خبرٌ مثبت" = .laHukmBilaShahid ∧ tasdiqOf "إنشاء" = .ghayrQabil ∧ tasdiqOf "لا حكم" = .laHukm := by
  decide

/-! ## ٧. معالجُ NTP في المدير -/

/-- أسماءُ عُقَد الشبكة المبنيّة (`NTP.Wasl.shabakaWasl`) بلفظها مجرَّدًا (تعيين البنّاء). -/
def uqdaMin (x : String) : Option Nat :=
  let t := tajrid x
  if t == "الولد" || t == "ولد" then some NTP.Wasl.nWalad
  else if t == "الزيتون" || t == "زيتون" then some NTP.nZayt
  else if t == "الحجر" || t == "حجر" then some NTP.Wasl.nHajar
  else if t == "الماء" || t == "ماء" then some NTP.nMa
  else if t == "الإنسان" || t == "الانسان" || t == "إنسان" || t == "انسان" then some NTP.nIns
  else if t == "النبات" || t == "نبات" then some NTP.nNabat
  else none

def ismQism : Option Madlul.Tayin.Qism → String
  | some .jamad => "جماد" | some .nabat => "نبات" | some .hayawan => "حيوان" | some .insan => "إنسان"
  | none => "لا حكم"

def ismHukm : Jisr.QabiliyyaJins.HukmMujarrad → String
  | .murakhkhas => "مرخَّص" | .laHukm => "لا حكم" | .mumtani => "ممتنع" | .laJins => "لا جنس" | .laMithal => "لا مثال"

/-- مخرجُ المعالج: القسمُ بالوراثة، وحكمُ «يسير» إسناديًّا (`NTP.Wasl.hukm` بعتبة التواتر 2 ووقود 4، كشواهدها). -/
def tasnifNTP (x : String) : String :=
  match uqdaMin x with
  | none => s!"لا حكم: لا عقدةَ «{tajrid x}» في الشبكة المبنيّة (NTP.Wasl.shabakaWasl). الغيابُ ليس امتناعًا."
  | some n =>
    s!"العقدة «{tajrid x}» ({n})\tالقسم بالوراثة: {ismQism (Madlul.Tayin.sannif (NTP.Wasl.khawassOf NTP.Wasl.shabakaWasl 4 n))}" ++
    s!"\tحملُ «يسير» إسناديًّا: {ismHukm (NTP.Wasl.hukm NTP.Wasl.shabakaWasl 2 4 n .sayr .isnadiyya)}" ++
    "\tالشبكةُ شاهدٌ مبنيّ لا مودَع"

/-! ## ٨. شواهد -/

theorem shawahid_qarar :
    qarar .malik "اقْرَأْ كَتَبَ الطَّالِبُ" = .tanfidh .iqra "كَتَبَ الطَّالِبُ" ∧
    qarar .majhul "اقْرَأْ كَتَبَ" = .rafd (.bilaMaqam .iqra) ∧
    qarar .wakil "تَعَلَّمْ الْمَاءُ سَائِلٌ" = .rafd (.ghayrMurakhkhas .iltimas .taallam) ∧
    qarar .wakil "أَعْرِبْ كَتَبَ" = .tanfidh .aarib "كَتَبَ" ∧
    qarar .malik "ادْمُجْ الفرع" = .rafd (.mahzur .idmaj) ∧
    qarar .malik "اقْرَأْ:" = .rafd (.bilaHujja .iqra) ∧
    qarar .majhul "ما معنى البلجة؟" = .tanfidh .isal "البلجة" ∧
    qarar .malik "طِرْ إِلَى الْقَمَرِ" = .qiraa "طِرْ إِلَى الْقَمَرِ" := by
  decide

theorem shahid_tasnif :
    tasnifNTP "الزَّيْتُونُ" = "العقدة «الزيتون» (" ++ toString NTP.nZayt ++ ")\tالقسم بالوراثة: نبات\tحملُ «يسير» إسناديًّا: لا حكم\tالشبكةُ شاهدٌ مبنيّ لا مودَع" := by
  decide +kernel

end Nizam.Mudir
