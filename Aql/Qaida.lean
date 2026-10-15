/-
  Aql/Qaida.lean — قاعدة المحرّك: جبرٌ مرخَّص تدريجيًّا، واحد، له إصدار.

  السند: ج1 29 (العقلية ربطٌ مقيسٌ إلى قاعدة)، ج1 57 (تعدّد القواعد يُفقد اللون)،
  وقرار المالك (15 أكتوبر 2026): أن يكون الحكم كلّه جبريًّا مرخَّصًا.

  التصميم:
  * القاعدة = إصدار + قائمة قوانين مسمّاة. القانون: اسم، ومقدّمات، ونتيجة.
  * المرخَّص = ما كان أصلًا مودَعًا، أو نتيجةَ قانونٍ من القاعدة مقدّماته كلّها مرخَّصة.
  * البرهان = سلسلة خطوات (أصل، أو تطبيق قانون برقمه). `fahs` يفحصها آليًّا.
    مبرهنة `fahs_sahih`: ما قبله الفاحص مرخَّصٌ حقًّا. فكلّ ادّعاء في الجواب يحمل سلسلته،
    ويعيد فحصَها أيُّ أحدٍ بالفاحص نفسه — وهذا هو «الجواب المتتبَّع».
  * الجواب مفهرَس بالقاعدة في نوعه: `Jawab q` لا يحوي إلّا أحكامًا بالقاعدة q،
    فخلط قاعدتين في جواب واحد لا يُكتب أصلًا (ج1 57).
  * التدرّج: كلّ قانون مقدّماته أدنى رتبةً من نتيجته؛ فما كان في الرتبة صفر لا يكون إلّا أصلًا.
  بلا sorry ولا axiom ولا native_decide.
-/
namespace Qaida

variable {P : Type}

structure Qanun (P : Type) where
  ism        : String
  muqaddimat : List P
  natija     : P
deriving DecidableEq, Repr

structure Qaida (P : Type) where
  isdar   : String
  qawanin : List (Qanun P)

/-- المرخَّص في القاعدة q على أصولٍ A. -/
inductive Murakhkhas (q : Qaida P) (A : P → Prop) : P → Prop
  | asl {p : P} : A p → Murakhkhas q A p
  | qanun (r : Qanun P) : r ∈ q.qawanin →
      (∀ m ∈ r.muqaddimat, Murakhkhas q A m) → Murakhkhas q A r.natija

/-! ## البرهان سلسلةً، والفاحص -/

inductive Khatwa (P : Type)
  | asl (p : P)
  | qanun (i : Nat)

variable [DecidableEq P]

/-- خطوة واحدة على ما ثبت: تُقبل أو تُرفض. -/
def tatbiq (q : Qaida P) (aslB : P → Bool) (thabit : List P) : Khatwa P → Option (List P)
  | .asl p => if aslB p then some (thabit ++ [p]) else none
  | .qanun i =>
    match q.qawanin[i]? with
    | none => none
    | some r => if r.muqaddimat.all (fun m => decide (m ∈ thabit)) then some (thabit ++ [r.natija]) else none

/-- الفاحص: يمرّ على الخطوات بالترتيب. -/
def fahs (q : Qaida P) (aslB : P → Bool) : List P → List (Khatwa P) → Option (List P)
  | thabit, [] => some thabit
  | thabit, k :: ks =>
    match tatbiq q aslB thabit k with
    | none => none
    | some t => fahs q aslB t ks

theorem tatbiq_sahih (q : Qaida P) (aslB : P → Bool) (thabit out : List P) (k : Khatwa P)
    (hth : ∀ x ∈ thabit, Murakhkhas q (fun y => aslB y = true) x)
    (h : tatbiq q aslB thabit k = some out) :
    ∀ x ∈ out, Murakhkhas q (fun y => aslB y = true) x := by
  cases k with
  | asl p =>
    simp only [tatbiq] at h
    split at h
    · rename_i hp
      cases h
      intro x hx
      rcases List.mem_append.mp hx with hx | hx
      · exact hth x hx
      · simp at hx; subst hx; exact Murakhkhas.asl hp
    · cases h
  | qanun i =>
    simp only [tatbiq] at h
    split at h
    · cases h
    · rename_i r hr
      split at h
      · rename_i hall
        cases h
        intro x hx
        rcases List.mem_append.mp hx with hx | hx
        · exact hth x hx
        · simp at hx; subst hx
          refine Murakhkhas.qanun r (List.mem_of_getElem? hr) ?_
          intro m hm
          have := List.all_eq_true.mp hall m hm
          exact hth m (of_decide_eq_true this)
      · cases h

/-- سلامة الفاحص: كلّ ما قبله مرخَّص حقًّا. -/
theorem fahs_sahih (q : Qaida P) (aslB : P → Bool) :
    ∀ (ks : List (Khatwa P)) (thabit out : List P),
    (∀ x ∈ thabit, Murakhkhas q (fun y => aslB y = true) x) →
    fahs q aslB thabit ks = some out →
    ∀ x ∈ out, Murakhkhas q (fun y => aslB y = true) x := by
  intro ks
  induction ks with
  | nil => intro thabit out hth h; simp [fahs] at h; subst h; exact hth
  | cons k ks ih =>
    intro thabit out hth h
    simp only [fahs] at h
    split at h
    · cases h
    · rename_i t ht
      exact ih t out (tatbiq_sahih q aslB thabit t k hth ht) h

/-! ## الجواب المتتبَّع، مفهرَسًا بالقاعدة -/

/-- ادّعاء مع سلسلته. -/
structure Iddia (P : Type) where
  qawl    : P
  silsila : List (Khatwa P)

/-- الادّعاء مقبول إن قبل الفاحصُ سلسلتَه من لا شيء، وكان القول بين ما ثبت. -/
def maqbul (q : Qaida P) (aslB : P → Bool) (c : Iddia P) : Bool :=
  match fahs q aslB [] c.silsila with
  | none => false
  | some out => decide (c.qawl ∈ out)

/-- كلّ ادّعاء مقبول مرخَّصٌ في القاعدة. -/
theorem maqbul_murakhkhas (q : Qaida P) (aslB : P → Bool) (c : Iddia P)
    (h : maqbul q aslB c = true) : Murakhkhas q (fun y => aslB y = true) c.qawl := by
  unfold maqbul at h
  split at h
  · cases h
  · rename_i out hout
    exact fahs_sahih q aslB c.silsila [] out (by simp) hout c.qawl (of_decide_eq_true h)

/-- الجواب بالقاعدة q: ادّعاءات، كلّها مقبولة بالفاحص على هذه القاعدة وحدها. -/
structure Jawab (q : Qaida P) (aslB : P → Bool) where
  iddiaat : List (Iddia P)
  kulluha : iddiaat.all (maqbul q aslB) = true

/-- ضمّ جوابين بالقاعدة نفسها جوابٌ بها. ولا دالّة تضمّ جوابين بقاعدتين. -/
def damm {q : Qaida P} {aslB : P → Bool} (a b : Jawab q aslB) : Jawab q aslB :=
  ⟨a.iddiaat ++ b.iddiaat, by simp [List.all_append, a.kulluha, b.kulluha]⟩

/-- كلّ قولٍ في الجواب مرخَّص. -/
theorem jawab_sahih {q : Qaida P} {aslB : P → Bool} (j : Jawab q aslB) :
    ∀ c ∈ j.iddiaat, Murakhkhas q (fun y => aslB y = true) c.qawl := by
  intro c hc
  exact maqbul_murakhkhas q aslB c (List.all_eq_true.mp j.kulluha c hc)

/-! ## الإصدار والتدرّج -/

omit [DecidableEq P] in
/-- إضافة قوانين في إصدار لاحق لا تُسقط ما رُخِّص في السابق. -/
theorem ziyada_la_tusqit (q q' : Qaida P) (A : P → Prop)
    (hsub : ∀ r ∈ q.qawanin, r ∈ q'.qawanin) {p : P} (h : Murakhkhas q A p) : Murakhkhas q' A p := by
  induction h with
  | asl ha => exact Murakhkhas.asl ha
  | qanun r hr _ ih => exact Murakhkhas.qanun r (hsub r hr) ih

/-- القاعدة متدرّجة: مقدّمات كلّ قانون أدنى رتبةً من نتيجته، ولا قانون بلا مقدّمة. -/
def Mutadarrija (q : Qaida P) (rutba : P → Nat) : Prop :=
  ∀ r ∈ q.qawanin, r.muqaddimat ≠ [] ∧ ∀ m ∈ r.muqaddimat, rutba m < rutba r.natija

omit [DecidableEq P] in
/-- في القاعدة المتدرّجة، ما رتبته صفر لا يُرخَّص إلّا أصلًا مودَعًا. -/
theorem rutba_sifr_asl (q : Qaida P) (rutba : P → Nat) (A : P → Prop)
    (hq : Mutadarrija q rutba) {p : P} (h : Murakhkhas q A p) (h0 : rutba p = 0) : A p := by
  cases h with
  | asl ha => exact ha
  | qanun r hr _ =>
    obtain ⟨hne, hlt⟩ := hq r hr
    obtain ⟨m, hm⟩ := List.exists_mem_of_ne_nil _ hne
    have := hlt m hm
    omega

/-- التدرّج الضعيف: لا قانون بلا مقدّمة، ولا قانون نتيجته في الرتبة صفر، ومقدّماته لا تعلو نتيجته.
    يكفي لحفظ الرتبة صفر للأصول، ويسمح بقوانين تنقل داخل الرتبة الواحدة (كتعدية الاحتواء). -/
def MutadarrijaDaifa (q : Qaida P) (rutba : P → Nat) : Prop :=
  ∀ r ∈ q.qawanin, r.muqaddimat ≠ [] ∧ 0 < rutba r.natija ∧ ∀ m ∈ r.muqaddimat, rutba m ≤ rutba r.natija

omit [DecidableEq P] in
theorem mutadarrija_daifa (q : Qaida P) (rutba : P → Nat) (h : Mutadarrija q rutba) :
    MutadarrijaDaifa q rutba := by
  intro r hr
  obtain ⟨hne, hlt⟩ := h r hr
  refine ⟨hne, ?_, fun m hm => Nat.le_of_lt (hlt m hm)⟩
  obtain ⟨m, hm⟩ := List.exists_mem_of_ne_nil _ hne
  have := hlt m hm
  omega

omit [DecidableEq P] in
/-- وفي القاعدة المتدرّجة ضعيفًا أيضًا، ما رتبته صفر لا يُرخَّص إلّا أصلًا. -/
theorem rutba_sifr_asl_daifa (q : Qaida P) (rutba : P → Nat) (A : P → Prop)
    (hq : MutadarrijaDaifa q rutba) {p : P} (h : Murakhkhas q A p) (h0 : rutba p = 0) : A p := by
  cases h with
  | asl ha => exact ha
  | qanun r hr _ =>
    obtain ⟨_, hpos, _⟩ := hq r hr
    omega

/-! ## شاهد: قاعدة صغيرة بقانون واحد «الإنسان ⊢ الحيوان» (تضمّن)، وأصل «الإنسان» -/

def qShahid : Qaida String := ⟨"شاهد-1", [⟨"تضمّن-الإنسان", ["الإنسان"], "الحيوان"⟩]⟩
def aslShahid (p : String) : Bool := p == "الإنسان"

/-- سلسلة صحيحة: أصل ثم القانون رقم 0 — يقبلها الفاحص. -/
theorem shahid_maqbul : maqbul qShahid aslShahid ⟨"الحيوان", [.asl "الإنسان", .qanun 0]⟩ = true := by decide

/-- القانون قبل مقدّمته — يرفضها الفاحص. -/
theorem shahid_marfud_tartib : maqbul qShahid aslShahid ⟨"الحيوان", [.qanun 0, .asl "الإنسان"]⟩ = false := by decide

/-- أصلٌ غير مودَع — يرفضه الفاحص. -/
theorem shahid_marfud_asl : maqbul qShahid aslShahid ⟨"الحيوان", [.asl "الحيوان"]⟩ = false := by decide

end Qaida
