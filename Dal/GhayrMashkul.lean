import SLGE.Law
import Dal.Makharij
import Dal.QiraaTahsil
import A116.Tashkil

/-!
# غيرُ المشكول: كلُّ حرفٍ قيمةٌ من الـ116، والقانونُ يقرؤها بما قبلها وما بعدها، بترخيصٍ تدريجيٍّ مكتمل

**الطلب.** أمرُ المالك في الجلسة 2026-11-20 (11:42 بتوقيت عمّان): «نحتاج حل لغير المشكول … من خلال دالة خوارزمية تربط كل مكون على
اساس انه قيمة من الشيفرة تقرأ كواحد من 116 والدالة تقرأ القيمة وفق قانون الابتداء وقانون الوصل وقانون الفصل والوقف وتربط كل واحد من 116
وتربطه بما قبله وما بعده … بالترخيص الجبري التدريجي بالحد الأدنى المكتمل». والتصميمُ قرارُ البنّاء.

**الفكرة.** الحرفُ غيرُ المشكول حاملٌ ‎c‎ بلا حالة؛ فقيمتُه واحدةٌ من خلاياه الأربع ‎4c+s‎ (أو خليّتان إن كان مضعَّفًا لم تُرسم شدّتُه).
والقانونُ هو آلةُ ‎δ‎ نفسُها (`SLGE.Law`): حالتُها بعد كلّ خليّةٍ هي ما يحمله ما قبلها إلى ما بعدها، فـ«علاقةُ الخليّة بما قبلها» حالةُ
الدخول، و«بما بعدها» حالةُ الخروج، و«علاقةُ ما قبلها بما بعدها» انتقالُ ‎δ‎ عليها. والابتداءُ حالةُ ‎0‎، والوصلُ بين كلمتين رمزُ الحدّ
‎116‎، والفصلُ وقفٌ ثمّ ابتداء، والوقفُ قبولُ ‎Fwaqf‎ في الآخر.

**الدرجات** (كلُّ درجةٍ مرشِّحٌ لما قبلها، لا اختيارَ في أيّها):
1. **القانون في الكلمة** (`qiraat`): كلُّ تعيينٍ للخلايا على الهيكل لا تموت فيه الآلة. وهو **مكتمل**: لا يُسقط تعيينًا مرخَّصًا ولا يزيد
   غيرَ مرخَّص (`qiraat_eq`: هو التعييناتُ كلُّها مرشَّحةً بالقانون، لكلّ هيكل).
2. **القانون في الجملة** (`jumla`): ما بقي من قراءات الكلمة بعد ربطها بما قبلها وما بعدها: حالاتُ الدخول الممكنة من أوّل الجملة
   (`amam`)، وحالاتُ الخروج التي يُستكمل منها إلى الوقف (`khalf`). فالقراءةُ تبقى إن وصلت حالةً ممكنةً بحالةٍ مستكملة — وهذا
   **الحدُّ الأدنى المكتمل** على الشاهد: ما بقي جزءٌ من قراءةٍ تامّةٍ للجملة، وكلُّ قراءةٍ تامّةٍ للجملة أجزاؤها ممّا بقي.
3. **الوضع** (`wad`): ما بقي ممّا له صورةٌ في معجم التشكيل المختوم بعد قراءتها بالقارئ (`Dal.QiraaTahsil.qiraa`) في موضعها:
   موقوفًا عليها إن كانت آخرَ الجملة، وموصولةً إن لم تكن.

`tadarruj`: كلُّ درجةٍ بعضُ ما قبلها (لكلّ مدخل). والمخرجُ عدُّ كلّ درجةٍ وحركاتُ كلّ حرفٍ فيها، ولا يُختار من الباقي.

**الوسائطُ المعلنة** (رسمٌ لا قانون): الهمزاتُ كلُّها حاملُ الهمزة؛ والتاءُ المربوطة تاء؛ والمقصورةُ ألف؛ و«آ» همزةٌ مفتوحةٌ ثمّ ألف؛
وألفُ «ال» أوّلَ الكلمة همزةُ وصل: في الابتداء همزةٌ مفتوحة، وفي الوصل لا خليّةَ لها؛ ولامُ «ال» ساكنةٌ قبل الحرف بعدها أو مدغمةٌ فيه فيُضعَّف (خيارٌ واحدٌ للحرفين: لا لامَ بلا تضعيف)؛ والتضعيفُ
ممكنٌ في كلّ حرفٍ غيرِ الأوّل وغيرِ الألف؛ والألفُ المجرّدة أوّلَ الكلمة في غير «ال» همزةٌ بحركاتها (همزةُ قطعٍ لم تُرسم).
والتنوينُ لا يُرسم فلا يُقرأ. وفي الجملة: الكلمةُ بـ«ال» في غير الأوّل تتّصل بما قبلها بلا حدّ (همزةُ الوصل تسقط، كما في `Dal/Jumla.lean`)،
وغيرُها بعد الحدّ ‎116‎.
-/

namespace Dal
namespace GhayrMashkul

open SLGE.Law

/-! ## ١. الخيارات: كلُّ حرفٍ قيمةٌ من الـ116 -/

/-- خليّةٌ واحدة من الأربع: ‎4c+s‎. -/
def mufrad (c : Nat) : List (List Nat) := (List.range 4).map fun s => [4 * c + s]

/-- المضعَّف: ساكنٌ ثمّ متحرّكٌ من حامله. -/
def mudaaf (c : Nat) : List (List Nat) := (List.range 3).map fun s => [4 * c + 3, 4 * c + s]

/-- حاملُ الحرف (الوسائط المعلنة أعلاه)؛ `none` لغير الحرف. -/
def hamilOf (ch : Char) : Option Nat :=
  if ch == 'أ' || ch == 'إ' || ch == 'ؤ' || ch == 'ئ' || ch == 'ء' then some 0
  else if ch == 'ة' then some 18
  else if ch == 'ى' then some 2
  else match Dal.hawamil.idxOf? ch with
    | some i => some i
    | none => none

/-- خياراتُ الحرف في موضعه: `awwal` أوّلُ الكلمة (فلا تضعيف). -/
def khiyarat (c : Nat) (awwal : Bool) : List (List Nat) :=
  if c == 2 || awwal then mufrad c else mufrad c ++ mudaaf c

/-- خياراتُ الكلمة حرفًا حرفًا، أو اسمُ ما لم يُقرأ. `ibtida`: يُبتدأ بها. -/
def khiyaratKalima (w : List Char) (ibtida : Bool) : Except String (List (List (List Nat))) :=
  let harf (awwal : Bool) (ch : Char) : Except String (List (List Nat)) :=
    if ch == 'آ' then .ok [[0, 11]]
    else match hamilOf ch with
      | some c => .ok (khiyarat c awwal)
      | none => .error s!"«{ch}» ليس حرفًا من الحوامل"
  match w with
  | 'ا' :: 'ل' :: ch :: r@(_ :: _) => do
      -- لامُ «ال» خليّتُها في خيار الحرف بعدها: ساكنةً قبله بحالاته، أو مدغمةً فيه فيُضعَّف (لا لامَ بلا تضعيف، ولا تضعيفَ
      -- بعد لامٍ ساكنة). وقبل اللام الخياران خلايا واحدة، فلا يُعدّان قراءتين.
      let c ← match hamilOf ch with
        | some c => .ok c
        | none => .error s!"«{ch}» ليس حرفًا من الحوامل"
      let baad := (mufrad c).map (fun x => (4 * 13 + 3) :: x) ++ (if c == 13 || c == 2 then [] else mudaaf c)
      let rest ← r.mapM (harf false)
      .ok ((if ibtida then [[0]] else [[]]) :: [[]] :: baad :: rest)
  | ch :: r => do
      let h ← if ch == 'ا' then .ok (mufrad 0) else harf true ch
      let rest ← r.mapM (harf false)
      .ok (h :: rest)
  | [] => .error "كلمة فارغة"

/-! ## ٢. الدرجة الأولى: القانون في الكلمة -/

/-- كلُّ تعيينٍ للخيارات (المواصفة). -/
def taayinat : List (List (List Nat)) → List (List (List Nat))
  | [] => [[]]
  | o :: os => o.flatMap fun x => (taayinat os).map (x :: ·)

/-- **القراءات:** تعييناتٌ لا تموت فيها الآلة من الحالة ‎q‎، وآخرُها مقبولٌ بـ‎F‎. تُقطع حيث تموت الآلة. -/
def qiraat (F : Nat → Bool) : Nat → List (List (List Nat)) → List (List (List Nat))
  | q, [] => if F q then [[]] else []
  | q, o :: os => o.flatMap fun x =>
      if run q x = 96 then [] else (qiraat F (run q x) os).map (x :: ·)

/-- الخلايا المتتابعة لتعيين. -/
def khalaya (r : List (List Nat)) : List Nat := r.flatten

theorem run_khalaya_cons (q : Nat) (x : List Nat) (r : List (List Nat)) :
    run q (khalaya (x :: r)) = run (run q x) (khalaya r) := by
  simp [khalaya, run_append]

/-- **الاكتمال والصحّة معًا** (لكلّ هيكلٍ ولكلّ حالة): القراءاتُ هي التعييناتُ كلُّها مرشَّحةً بالقانون، بترتيبها. -/
theorem qiraat_eq (F : Nat → Bool) (hF : F 96 = false) :
    ∀ os q, qiraat F q os = (taayinat os).filter (fun r => F (run q (khalaya r))) := by
  intro os
  induction os with
  | nil => intro q; by_cases h : F q <;> simp [qiraat, taayinat, khalaya, run, h]
  | cons o os ih =>
    intro q
    simp only [qiraat, taayinat, List.filter_flatMap]
    congr 1
    funext x
    rw [List.filter_map]
    by_cases hx : run q x = 96
    · simp only [hx, ite_true]
      symm
      rw [List.eq_nil_iff_forall_not_mem]
      intro r hr
      simp only [List.mem_map, List.mem_filter, Function.comp, run_khalaya_cons, hx, run_dead, hF] at hr
      obtain ⟨_, ⟨_, h⟩, _⟩ := hr
      exact Bool.false_ne_true h
    · simp only [hx, ite_false, ih]
      congr 1
      apply List.filter_congr
      intro r _
      simp [Function.comp, run_khalaya_cons]

/-- كلُّ قراءةٍ مقبولةٌ بالقانون. -/
theorem qiraa_murakhkhasa (F : Nat → Bool) (hF : F 96 = false) (os) (q) (r) (h : r ∈ qiraat F q os) :
    F (run q (khalaya r)) = true := by
  rw [qiraat_eq F hF] at h
  exact (List.mem_filter.mp h).2

/-- وكلُّ تعيينٍ يقبله القانون قراءة: لا يُسقَط مرخَّص. -/
theorem qiraa_tamma (F : Nat → Bool) (hF : F 96 = false) (os) (q) (r) (hr : r ∈ taayinat os)
    (h : F (run q (khalaya r)) = true) : r ∈ qiraat F q os := by
  rw [qiraat_eq F hF]
  exact List.mem_filter.mpr ⟨hr, h⟩

/-- حيٌّ: لم تمت الآلة (للكلمة داخلَ الجملة، يُحكم على آخرها بما بعدها). -/
def hayy (q : Nat) : Bool := q != 96

theorem hayy_96 : hayy 96 = false := rfl

/-! ## ٣. الدرجة الثانية: القانون في الجملة (الربطُ بما قبل وما بعد) -/

/-- الحالاتُ الممكنة كلُّها (الآلةُ مغلقةٌ دون ‎97‎: `fin_close`). -/
def halat : List Nat := List.range 96

/-- كلمةُ الجملة: خياراتُها، وهل تتّصل بما قبلها بلا حدّ (همزةُ وصل). -/
structure Kalima where
  khiyar : List (List (List Nat))
  wasl : Bool
  deriving Repr

/-- قراءاتُ الكلمة الحيّة من حالة ‎q‎ (بلا قبولٍ في آخرها). -/
def hayya (k : Kalima) (q : Nat) : List (List (List Nat)) := qiraat hayy q k.khiyar

/-- الحالةُ بعد الحدّ بين كلمتين في الوصل. -/
def hadd (q : Nat) : Nat := δ q 116

/-- **الانتقالُ إلى ما بعد الكلمة ‎i‎:** إلى الكلمة التالية بلا حدّ إن كانت موصولةً بهمزة وصل، وإلّا بالحدّ؛ والأخيرةُ لا انتقال. -/
def baad (ks : List Kalima) (i q : Nat) : Nat :=
  match ks[i + 1]? with
  | some k => if k.wasl then q else hadd q
  | none => q

/-- **أمام:** حالاتُ الدخول الممكنة لكلّ كلمة من أوّل الجملة (الأولى من الابتداء ‎0‎). -/
def amam (ks : List Kalima) : List (List Nat) :=
  (List.range ks.length).foldl (fun A i =>
    let S := A.getLastD [0]
    if i + 1 = ks.length then A
    else A ++ [((S.flatMap fun q => (hayya (ks.getD i ⟨[], false⟩) q).map fun r =>
              baad ks i (run q (khalaya r))).eraseDups.filter (· != 96))]) [[0]]

/-- **خلف:** لكلّ كلمةٍ الحالاتُ التي يُستكمل منها إلى الوقف قبلها (تُعدّ من الآخر). -/
def khalf (ks : List Kalima) : List (List Nat) :=
  (List.range ks.length).reverse.foldl (fun B i =>
    let k := ks.getD i ⟨[], false⟩
    if i + 1 = ks.length then [halat.filter fun q => (qiraat Fwaqf q k.khiyar).length != 0]
    else (halat.filter fun q => (hayya k q).any fun r => (B.headD []).contains (baad ks i (run q (khalaya r)))) :: B) []

/-- ما يبقى من قراءات الكلمة ‎i‎ في الجملة: من حالةٍ ممكنةٍ قبلها إلى حالةٍ يُستكمل منها بعدها. -/
def baqiya (ks : List Kalima) (i : Nat) (S bNext : List Nat) : List (List (List Nat)) :=
  let k := ks.getD i ⟨[], false⟩
  ((S.flatMap fun q =>
      if i + 1 = ks.length then qiraat Fwaqf q k.khiyar
      else (hayya k q).filter fun r => bNext.contains (baad ks i (run q (khalaya r))))).eraseDups

/-- **الدرجة الثانية** لجملةٍ موصولةٍ موقوفٍ على آخرها: لكلّ كلمةٍ ما بقي من قراءاتها. -/
def jumla (ks : List Kalima) : List (List (List (List Nat))) :=
  let A := amam ks
  let B := khalf ks
  (List.range ks.length).map fun i => baqiya ks i (A.getD i []) (B.getD (i + 1) [])

/-- الباقي من قراءات الكلمة الأخيرة مقبولٌ بالوقف من حالةٍ ممكنة (لكلّ مدخل). -/
theorem baqiya_akhir (ks : List Kalima) (i : Nat) (S bNext : List Nat) (hi : i + 1 = ks.length) (r)
    (h : r ∈ baqiya ks i S bNext) : ∃ q ∈ S, Fwaqf (run q (khalaya r)) = true := by
  simp only [baqiya, hi, ite_true] at h
  obtain ⟨q, hq, hr⟩ := List.mem_flatMap.mp (List.mem_eraseDups.mp h)
  exact ⟨q, hq, qiraa_murakhkhasa Fwaqf rfl _ _ _ hr⟩

/-- والباقي من غير الأخيرة يصل حالةً ممكنةً قبلها بحالةٍ يُستكمل منها بعدها، والآلةُ فيه حيّة (لكلّ مدخل). -/
theorem baqiya_wasat (ks : List Kalima) (i : Nat) (S bNext : List Nat) (hi : i + 1 ≠ ks.length) (r)
    (h : r ∈ baqiya ks i S bNext) :
    ∃ q ∈ S, run q (khalaya r) ≠ 96 ∧ bNext.contains (baad ks i (run q (khalaya r))) = true := by
  simp only [baqiya, hi, ite_false] at h
  obtain ⟨q, hq, hr⟩ := List.mem_flatMap.mp (List.mem_eraseDups.mp h)
  have h1 := List.mem_filter.mp hr
  refine ⟨q, hq, ?_, h1.2⟩
  have := qiraa_murakhkhasa hayy rfl _ _ _ h1.1
  simpa [hayy] using this

/-- **الدرجة الأولى في الجملة:** قراءاتُ الكلمة الحيّة من كلّ حالةٍ تبلغها الجملةُ قبلها (القانونُ وما قبلها، بلا ما بعدها). -/
def amamiyya (ks : List Kalima) (i : Nat) (S : List Nat) : List (List (List Nat)) :=
  (S.flatMap fun q => hayya (ks.getD i ⟨[], false⟩) q).eraseDups

theorem Fwaqf_hayy (q : Nat) (h : Fwaqf q = true) : hayy q = true := by
  have : q ≠ 96 := by intro e; subst e; exact absurd h (by decide)
  simp [hayy, this]

/-- **التدرّج في الجملة** (لكلّ مدخل): ما بقي بما بعدها بعضُ ما بلغته بما قبلها. -/
theorem baqiya_min_amamiyya (ks : List Kalima) (i : Nat) (S bNext : List Nat) (r)
    (h : r ∈ baqiya ks i S bNext) : r ∈ amamiyya ks i S := by
  unfold baqiya at h; unfold amamiyya
  obtain ⟨q, hq, hr⟩ := List.mem_flatMap.mp (List.mem_eraseDups.mp h)
  refine List.mem_eraseDups.mpr (List.mem_flatMap.mpr ⟨q, hq, ?_⟩)
  by_cases hi : i + 1 = ks.length
  · simp only [hi, ite_true] at hr
    unfold hayya
    rw [qiraat_eq hayy rfl]
    rw [qiraat_eq Fwaqf rfl] at hr
    have h1 := List.mem_filter.mp hr
    exact List.mem_filter.mpr ⟨h1.1, Fwaqf_hayy _ h1.2⟩
  · simp only [hi, ite_false] at hr
    exact (List.mem_filter.mp hr).1

/-! ## ٤. الدرجة الثالثة: الوضع (معجم التشكيل) -/

def harakat : List Char := ['َ', 'ُ', 'ِ', 'ْ', 'ّ', 'ً', 'ٌ', 'ٍ', 'ٰ']

def tajrid (w : List Char) : List Char := w.filter fun c => !harakat.contains c

/-- خلايا صورةٍ مشكولةٍ بالقارئ في موضعها (`akhir`: موقوفًا عليها؛ بلا همزة الوصل، كما يقرؤها `qiraa`)؛ `none` إن رفضها القارئ.
فالمنوَّنُ في الوصل نونُه خليّة، فلا يوافق هيكلًا لا نونَ فيه. -/
def khalayaSura (akhir : Bool) (f : String) : Option (List Nat) :=
  match Dal.QiraaTahsil.qiraa f.toList akhir with
  | .ok q => some (q.khalaya.map (·.raqm))
  | .error _ => none

/-- خلايا القراءة بلا خليّة همزة الوصل (لتُقابَل بما يقرؤه القارئ). -/
def khalayaBilaWasl (al : Bool) (r : List (List Nat)) : List Nat :=
  if al then khalaya (r.drop 1) else khalaya r

/-- **الدرجة الثالثة:** ما بقي ممّا خلاياه خلايا صورةٍ من صور هيكله في المعجم. -/
def wad (mj : A116.Tashkil.Mujam) (w : List Char) (al akhir : Bool) (rs : List (List (List Nat))) :
    List (List (List Nat)) :=
  let h := tajrid w
  -- الألفُ المجرّدة أوّلَ غير «ال» همزةٌ لم يُرسم مقعدُها (الوسيطُ أعلاه): فهيكلُها في المعجم بمقعدَيها أيضًا.
  let hayakil := match h with
    | 'ا' :: r => if al then [h] else [h, 'أ' :: r, 'إ' :: r]
    | _ => [h]
  let suwar := (hayakil.flatMap fun k => A116.Tashkil.marashshahun mj (String.ofList k)).filterMap (khalayaSura akhir)
  rs.filter fun r => suwar.contains (khalayaBilaWasl al r)

/-- **التدرّج:** كلُّ درجةٍ بعضُ ما قبلها — الوضعُ لا يزيد على القانون (لكلّ مدخل). -/
theorem tadarruj (mj : A116.Tashkil.Mujam) (w : List Char) (al akhir : Bool) (rs : List (List (List Nat))) :
    ∀ r ∈ wad mj w al akhir rs, r ∈ rs := by
  intro r h
  exact (List.mem_filter.mp h).1

/-- درجاتُ كلمةٍ في جملة. -/
structure Darajat where
  kalima : List Char
  al : Bool
  ula : List (List (List Nat))
  thaniya : List (List (List Nat))
  thalitha : List (List (List Nat))

/-- الكلمةُ بـ«ال» (همزةُ وصلٍ أوّلَها). -/
def bilAl (w : List Char) : Bool :=
  match w with
  | 'ا' :: 'ل' :: _ :: _ :: _ => true
  | _ => false

/-- **الجملةُ غيرُ المشكولة بدرجاتها** (موصولةً، موقوفًا على آخرها)؛ أو اسمُ ما لم يُقرأ من حروفها. -/
def darajatJumla (mj : A116.Tashkil.Mujam) (ws : List (List Char)) : Except String (List Darajat) := do
  let ws := ws.map tajrid
  let os ← (List.range ws.length).mapM fun i => khiyaratKalima (ws.getD i []) (i == 0)
  let ks := (List.range ws.length).map fun i => (⟨os.getD i [], i != 0 && bilAl (ws.getD i [])⟩ : Kalima)
  let A := amam ks
  let B := khalf ks
  .ok ((List.range ws.length).map fun i =>
    let w := ws.getD i []
    let d2 := baqiya ks i (A.getD i []) (B.getD (i + 1) [])
    ⟨w, bilAl w, amamiyya ks i (A.getD i []), d2, wad mj w (bilAl w) (i + 1 == ws.length) d2⟩)

/-! ## ٥. العرض: الحرفُ بحركته -/

/-- علامةُ الحالة. -/
def alama (s : Nat) : String :=
  if s == 0 then "َ" else if s == 1 then "ُ" else if s == 2 then "ِ" else "ْ"

/-- الحرفُ بخياره: بلا خليّة كما رُسم، وبخليّةٍ علامتُها (والألفُ مدٌّ بلا علامة)، وبخليّتين شدّةٌ وعلامة. -/
def harfBi (ch : Char) : List Nat → String
  | [] => ch.toString
  | [a] => if ch == 'ا' || ch == 'ى' then ch.toString else ch.toString ++ alama (a % 4)
  | [_, b] => if ch == 'آ' then "آ" else ch.toString ++ "ّ" ++ alama (b % 4)
  | _ => ch.toString

/-- الحرفُ ‎i‎ في سياقه: الألفُ أوّلَ الكلمة همزةً تُكتب بمقعدها (إ مع الكسرة، وأ مع غيرها)، والواوُ والياءُ الساكنتان بعد حركتهما مدٌّ
بلا علامة؛ وما سوى ذلك `harfBi`. -/
def harfFi (w : List Char) (r : List (List Nat)) (i : Nat) : String :=
  let ch := w.getD i ' '
  let x := r.getD i []
  let qabl := ((r.getD (i - 1) []).getLast?).filter fun _ => i ≠ 0
  let al := match w with | 'ا' :: 'ل' :: _ :: _ :: _ => true | _ => false
  let thalith := r.getD 2 []
  if al && i == 1 then (if thalith.head? == some (4 * 13 + 3) && w.getD 2 ' ' != 'ل' then "لْ" else "ل")
  else if al && i == 2 && thalith.head? == some (4 * 13 + 3) && ch != 'ل' then
    (match thalith with | [_, b] => ch.toString ++ alama (b % 4) | _ => ch.toString)
  else
  match x with
  | [a] =>
    if i == 0 && ch == 'ا' && a / 4 == 0 then (if a % 4 == 2 then "إ" else "أ") ++ alama (a % 4)
    else if a % 4 == 3 && ((ch == 'و' && qabl.map (· % 4) == some 1) || (ch == 'ي' && qabl.map (· % 4) == some 2)) then ch.toString
    else harfBi ch x
  | _ => harfBi ch x

/-- الكلمةُ مشكولةً بقراءتها. -/
def nass (w : List Char) (r : List (List Nat)) : String :=
  String.join ((List.range (min w.length r.length)).map (harfFi w r))

/-- حركاتُ الحرف ‎i‎ في القراءات. -/
def harakatFi (rs : List (List (List Nat))) (w : List Char) (i : Nat) : List String :=
  (rs.map fun r => harfFi w r i).eraseDups

/-! ## ٦. على الشاهد -/

/-- «كتب» وحدها مبتدأً بها موقوفًا عليها: القانونُ يرخّص 138 قراءةً (لا يُختار منها)، منها «كَتَبَ» و«كُتُبْ»،
ولا يرخّص «كْتَبَ» (ابتداءٌ بساكن). -/
theorem kataba_qanun :
    let rs := qiraat Fwaqf 0 ((khiyaratKalima ['ك', 'ت', 'ب'] true).toOption.getD [])
    rs.length = 138 ∧ [[32], [72], [104]] ∈ rs ∧ [[33], [73], [107]] ∈ rs ∧ [[35], [72], [104]] ∉ rs := by
  decide +kernel

/-- «قال»: الألفُ لا تكون إلّا مدًّا بعد فتحة — فالقافُ مفتوحةٌ في القراءات السبع كلّها. -/
theorem qala_alif :
    let rs := qiraat Fwaqf 0 ((khiyaratKalima ['ق', 'ا', 'ل'] true).toOption.getD [])
    rs.length = 7 ∧ rs.all (fun r => r.head? == some [28]) = true := by
  decide +kernel

/-- «الى»: الألفُ المجرّدة أوّلَها همزةٌ متحرّكة (لا يُبتدأ بساكن)، واللامُ مفتوحةٌ قبل المقصورة مدًّا، مفردةً أو مضعَّفة: 3 × 2 = 6،
منها «إِلَى». -/
theorem ila_hamza :
    let rs := qiraat Fwaqf 0 ((khiyaratKalima ['ا', 'ل', 'ى'] true).toOption.getD [])
    rs.length = 6 ∧ [[2], [52], [11]] ∈ rs := by
  decide +kernel

/-- **الدرجاتُ الثلاث على «كتب الكتاب»** بشواهد المعجم (`A116.Tashkil.mujam`): «كتب» 138 ← 117 بما بعدها (لا تسكنُ الباءُ قبل لامٍ ساكنةٍ أو طاءٍ مضعَّفة) ← 3 في الوضع
(«كَتَبَ، كُتُبِ، كُتِبَ»؛ والمنوَّنُ «كُتُبٌ» لا يوافق في الوصل، فنونُه خليّة)؛ و«الكتاب» 84 ← 84 ← 3 («الْكِتَابَ، الْكِتَابُ، الْكِتَابِ»). لا يُختار من الباقي. -/
theorem kataba_alkitab :
    (match darajatJumla A116.Tashkil.mujam [['ك', 'ت', 'ب'], ['ا', 'ل', 'ك', 'ت', 'ا', 'ب']] with
     | .ok ds => ds.map (fun d => (d.ula.length, d.thaniya.length, d.thalitha.map (nass d.kalima)))
     | .error _ => []) =
    [(138, 117, ["كَتَبَ", "كُتُبِ", "كُتِبَ"]), (84, 84, ["الْكِتَابَ", "الْكِتَابُ", "الْكِتَابِ"])] := by
  decide +kernel

end GhayrMashkul
end Dal
