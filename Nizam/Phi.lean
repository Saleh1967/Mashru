/-
  Nizam/Phi.lean — Φ: التركيبُ الجامعُ المانع بالمنطق الثلاثيّ (المرحلة «ب» من قانون المواصفة).

  قرار المالك (2026-10-20، 00:23 بتوقيت عمّان): «(ب) Φ العامّة في Lean مع المنطق الثلاثيّ، تُعمِّم kull_ma_kull. موافق».
  ومصدرُ التصميم مرفقُ المالك «المبرهنة الجامعة المانعة للدالة الثنائية العودية Φ» (`Mashru_Fractal_Theorem_AR.md`، غيرُ مودَع): يقول
  في سطره 4 إنّه «حجة رياضية كاملة بالاستقراء على شجرة منتهية، وليست شهادة نجاح Lean»، وحكمُه ثنائيّ (حلٌّ أو لا حلّ). وهنا تُبنى
  حالةُ السلسلة منه بحكمٍ ثلاثيّ وتُبرهن في Lean:

  ١. **الحكمُ الثلاثيّ وطبقتاه** (`K3`: مرخَّص P، ممتنع N، لا حكم U): الربطُ `wa` (يكفي ممتنعٌ ليمتنع، ولا ترخيصَ إلّا بترخيص الطرفين)
     والفصلُ `aw`؛ وتمثيلُ القيمة الواحدة بطبقتين من البتّات (قبول، ردّ): الربطُ (∧، ∨) والفصلُ (∨، ∧) (`tabaqat_wa`، `tabaqat_aw`)،
     ولا تعارضَ بين الطبقتين والتمثيلُ حقنيّ (`tabaqat_la_taarud`). فـ«لا حكم» غيابُ البتّين معًا، لا ردّ.
  ٢. **الإسقاطُ الوجوديّ** `yujad`: مرخَّصٌ ⟺ امتدادٌ مرخَّص، وممتنعٌ ⟺ كلُّ امتدادٍ ممتنع (`yujad_P`، `yujad_N`، `yujad_map_P`،
     `yujad_map_N`)؛ والنطاقُ الفارغ ممتنع.
  ٣. **التركيبُ على منفذٍ مشترك** `tarkib`: ربطُ عاملين على قيمة المنفذ ثمّ إسقاطُها (`tarkib_P`، `tarkib_N`). **والسلسلة** `zanjir`:
     مرخَّصةٌ ⟺ مسارٌ في النطاق كلُّ عوامله مرخِّصة (`zanjir_P`)، وممتنعةٌ ⟺ في كلّ مسارٍ عاملٌ يمنع (`zanjir_N`) — بالاستقراء على طول
     السلسلة؛ وما سواهما «لا حكم».
  ٤. **ضرورةُ المنفذ** (على الشاهد؛ مثالُ المرفق في سطره 64): القانونُ a⊕b⊕c=0 على ثلاثة متغيّراتٍ ثنائيّة يقبل أربعةَ تكاليف، وربطُ
     إسقاطاته الزوجيّة يقبل الثمانية (`wajiha_daruriyya`): إسقاطُ متغيّرٍ مشتركٍ قبل الربط يزيد حلولًا زائفة.
  ٥. **العقدُ حالةٌ من Φ**: لكلّ عقد، حكمُ `hukmB` بمراتبه الثلاث هو حكمُ `phiAqd` — القانونُ (P/N) والمانعُ (P/N) مربوطان بـ`tarkib`
     عاملِ الجذر (المرشَّحُ P، وغيرُه U لا N) وعاملِ الشاهد (المشهودُ P، وغيرُه U) على منفذ الجذر، بنطاقٍ غيرِ فارغ يحوي كلَّ مرشَّح
     (`aqd_phi`). ويُبرهن من `kull_ma_kull` ومن `phi_P`/`phi_N`: المنفّذُ البتّيّ والمواصفةُ وΦ ثلاثتُها حكمٌ واحد. وعلى `Mashru` بنطاق
     الجذور 32768 (`jidhr_hadd`، `aqd_phi_mashru`)، وشاهدُه كَتَبَ ← «علم» ترادفًا P ولزومًا U (`kataba_phi`).

  30 مبرهنة بالمعيار الموحَّد (`Nizam/Asas.lean`): 13 لكلّ (`yujad_P`، `yujad_N`، `yujad_map_P`، `yujad_map_N`، `tarkib_P`، `tarkib_N`،
  `zanjir_P`، `zanjir_N`، `phi_P`، `phi_N`، `aqd_phi`، `jidhr_hadd`، `aqd_phi_mashru`)، و15 تعريفيّة (`tabaqat_wa`، `tabaqat_aw`،
  `tabaqat_la_taarud`، `wa_P`، `wa_N`، `aw_P`، `aw_N`، وعواملُ العقد الثمانية `amil*`)، و2 على الشاهد (`wajiha_daruriyya`، `kataba_phi`).
  طفراتُها `P272`–`P277` في `tahaqquq/tafrat.json` تُفشل `lake build` مباشرة؛ لا جدولَ خارجيًّا فلا مرآة بايثون.

  ما لا يُدّعى: Φ على شجرةٍ عامّة (حالةُ المرفق كلُّها) لم تُبنَ، ولا إعادةُ التجميع؛ ولا منفّذَ بتّيًّا لتركيب السلاسل بمصفوفات (طبقتا
  البتّات مبرهنتان على القيمة الواحدة وحدها)؛ ولا يُقارَن `bitjoin.py` المرفق ولا «1000 نظام قيود» فيه — لم يُشغَّلا هنا. ولا تشهد المبرهنة
  بصحّة قيدٍ لغويّ: تضمن أنّ الحكم هو حكمُ العوامل المعطاة بعينه.
  بلا sorry ولا axiom ولا native_decide.
-/
import Nizam.Aqd

namespace Nizam
namespace Phi

open Nizam.Aqd

/-! ## ١. الحكمُ الثلاثيّ وطبقتاه -/

/-- مرخَّص، ممتنع، لا حكم. -/
inductive K3 | P | N | U
  deriving DecidableEq, Repr

namespace K3

/-- الربط: يكفي ممتنعٌ ليمتنع، ولا ترخيصَ إلّا بترخيص الطرفين. -/
def wa : K3 → K3 → K3
  | N, _ => N
  | _, N => N
  | P, P => P
  | _, _ => U

/-- الفصل: يكفي مرخِّصٌ ليُرخَّص، ولا امتناعَ إلّا بامتناع الطرفين. -/
def aw : K3 → K3 → K3
  | P, _ => P
  | _, P => P
  | N, N => N
  | _, _ => U

/-- طبقتا البتّات: (قبول، ردّ). -/
def tabaqat : K3 → Bool × Bool
  | P => (true, false)
  | N => (false, true)
  | U => (false, false)

end K3

open K3

theorem tabaqat_wa (x y : K3) :
    (wa x y).tabaqat = ((x.tabaqat.1 && y.tabaqat.1), (x.tabaqat.2 || y.tabaqat.2)) := by
  cases x <;> cases y <;> rfl

theorem tabaqat_aw (x y : K3) :
    (aw x y).tabaqat = ((x.tabaqat.1 || y.tabaqat.1), (x.tabaqat.2 && y.tabaqat.2)) := by
  cases x <;> cases y <;> rfl

/-- لا تعارضَ بين الطبقتين، والتمثيلُ حقنيّ. -/
theorem tabaqat_la_taarud (x : K3) : (x.tabaqat.1 && x.tabaqat.2) = false ∧
    ∀ y : K3, x.tabaqat = y.tabaqat → x = y := by
  cases x <;> refine ⟨rfl, fun y h => ?_⟩ <;> cases y <;> first | rfl | cases h

theorem wa_P (x y : K3) : wa x y = P ↔ x = P ∧ y = P := by cases x <;> cases y <;> simp [wa]
theorem wa_N (x y : K3) : wa x y = N ↔ x = N ∨ y = N := by cases x <;> cases y <;> simp [wa]
theorem aw_P (x y : K3) : aw x y = P ↔ x = P ∨ y = P := by cases x <;> cases y <;> simp [aw]
theorem aw_N (x y : K3) : aw x y = N ↔ x = N ∧ y = N := by cases x <;> cases y <;> simp [aw]

/-! ## ٢. الإسقاطُ الوجوديّ -/

/-- يُوجد امتدادٌ مرخَّص؟ وإلّا فهل كلُّ امتدادٍ ممتنع؟ (النطاقُ الفارغ: لا امتدادَ فممتنع.) -/
def yujad : List K3 → K3
  | [] => N
  | x :: xs => aw x (yujad xs)

theorem yujad_P : ∀ l : List K3, yujad l = P ↔ ∃ x ∈ l, x = P
  | [] => by simp [yujad]
  | x :: xs => by
    simp only [yujad, aw_P, yujad_P xs, List.mem_cons, exists_eq_or_imp]

theorem yujad_N : ∀ l : List K3, yujad l = N ↔ ∀ x ∈ l, x = N
  | [] => by simp [yujad]
  | x :: xs => by
    simp only [yujad, aw_N, yujad_N xs, List.mem_cons, forall_eq_or_imp]

/-- الإسقاطُ على صورةِ نطاق: مرخَّصٌ ⟺ قيمةٌ في النطاق صورتُها مرخَّصة. -/
theorem yujad_map_P {β : Type} (f : β → K3) : ∀ l : List β, yujad (l.map f) = P ↔ ∃ b ∈ l, f b = P
  | [] => by simp [yujad]
  | b :: l => by
    simp only [List.map, yujad, aw_P, yujad_map_P f l, List.mem_cons, exists_eq_or_imp]

/-- والإسقاطُ على صورةِ نطاق ممتنعٌ ⟺ كلُّ قيمةٍ في النطاق صورتُها ممتنعة. -/
theorem yujad_map_N {β : Type} (f : β → K3) : ∀ l : List β, yujad (l.map f) = N ↔ ∀ b ∈ l, f b = N
  | [] => by simp [yujad]
  | b :: l => by
    simp only [List.map, yujad, aw_N, yujad_map_N f l, List.mem_cons, forall_eq_or_imp]

/-! ## ٣. التركيبُ على منفذٍ مشترك، والسلسلة -/

/-- عاملٌ بين قيمتي منفذين. -/
abbrev Aamil (α β : Type) := α → β → K3

/-- ربطُ عاملين على قيمة المنفذ المشترك ثمّ إسقاطُها على نطاقه. -/
def tarkib {α β γ : Type} (dom : List β) (R : Aamil α β) (S : Aamil β γ) : Aamil α γ :=
  fun a c => yujad (dom.map fun b => wa (R a b) (S b c))

theorem tarkib_P {α β γ : Type} (dom : List β) (R : Aamil α β) (S : Aamil β γ) (a : α) (c : γ) :
    tarkib dom R S a c = P ↔ ∃ b ∈ dom, R a b = P ∧ S b c = P := by
  simp only [tarkib, yujad_map_P, wa_P]

theorem tarkib_N {α β γ : Type} (dom : List β) (R : Aamil α β) (S : Aamil β γ) (a : α) (c : γ) :
    tarkib dom R S a c = N ↔ ∀ b ∈ dom, R a b = N ∨ S b c = N := by
  simp only [tarkib, yujad_map_N, wa_N]

/-- عاملُ الهويّة: المنفذُ يمرّ كما هو. -/
def huwiyya {σ : Type} [DecidableEq σ] : Aamil σ σ := fun a c => if a = c then P else N

/-- السلسلة: عواملُ متتابعةٌ على منفذٍ واحدِ النوع، تُركَّب من اليسار. -/
def zanjir {σ : Type} [DecidableEq σ] (dom : List σ) : List (Aamil σ σ) → Aamil σ σ
  | [] => huwiyya
  | R :: Rs => tarkib dom R (zanjir dom Rs)

/-- مسارٌ مرخَّص: قيمٌ للمنافذ من النطاق، وكلُّ عاملٍ على مساره مرخِّص. -/
inductive MasarP {σ : Type} (dom : List σ) : List (Aamil σ σ) → σ → σ → Prop
  | nil (a : σ) : MasarP dom [] a a
  | cons {R : Aamil σ σ} {Rs : List (Aamil σ σ)} {a b c : σ} :
      b ∈ dom → R a b = P → MasarP dom Rs b c → MasarP dom (R :: Rs) a c

/-- كلُّ مسارٍ ممتنع: في كلّ مسارٍ من النطاق عاملٌ يمنع. -/
def KullMardud {σ : Type} (dom : List σ) : List (Aamil σ σ) → σ → σ → Prop
  | [], a, c => a ≠ c
  | R :: Rs, a, c => ∀ b ∈ dom, R a b = N ∨ KullMardud dom Rs b c

/-- **السلسلةُ جامعةٌ مانعة للترخيص**: مرخَّصةٌ ⟺ مسارٌ كلُّ عوامله مرخِّصة. -/
theorem zanjir_P {σ : Type} [DecidableEq σ] (dom : List σ) :
    ∀ (Rs : List (Aamil σ σ)) (a c : σ), zanjir dom Rs a c = P ↔ MasarP dom Rs a c
  | [], a, c => by
    simp only [zanjir, huwiyya]
    constructor
    · intro h; split at h
      · rename_i e; subst e; exact .nil a
      · cases h
    · intro h; cases h; simp
  | R :: Rs, a, c => by
    simp only [zanjir]
    rw [tarkib_P]
    constructor
    · rintro ⟨b, hb, h1, h2⟩; exact .cons hb h1 ((zanjir_P dom Rs b c).mp h2)
    · intro h
      cases h with
      | cons hb h1 h2 => exact ⟨_, hb, h1, (zanjir_P dom Rs _ c).mpr h2⟩

/-- **والسلسلةُ جامعةٌ مانعة للامتناع**: ممتنعةٌ ⟺ كلُّ مسارٍ فيه عاملٌ يمنع. فما سواهما «لا حكم». -/
theorem zanjir_N {σ : Type} [DecidableEq σ] (dom : List σ) :
    ∀ (Rs : List (Aamil σ σ)) (a c : σ), zanjir dom Rs a c = N ↔ KullMardud dom Rs a c
  | [], a, c => by
    simp only [zanjir, huwiyya, KullMardud]
    split
    · rename_i e; simp [e]
    · rename_i e; simp [e]
  | R :: Rs, a, c => by
    simp only [zanjir, KullMardud]
    rw [tarkib_N]
    constructor
    · intro h b hb
      rcases h b hb with h | h
      · exact Or.inl h
      · exact Or.inr ((zanjir_N dom Rs b c).mp h)
    · intro h b hb
      rcases h b hb with h | h
      · exact Or.inl h
      · exact Or.inr ((zanjir_N dom Rs b c).mpr h)

/-! ## ٤. ضرورةُ المنفذ (على الشاهد) -/

/-- التكاليفُ الثمانية لثلاثة متغيّراتٍ ثنائيّة. -/
def thulathiyyat : List (Bool × Bool × Bool) :=
  [false, true].flatMap fun a => [false, true].flatMap fun b => [false, true].map fun c => (a, b, c)

/-- القانونُ الثلاثيّ: a ⊕ b ⊕ c = 0. -/
def xor3 (t : Bool × Bool × Bool) : Bool := !(t.1 ^^ t.2.1 ^^ t.2.2)

/-- **ضرورةُ المنفذ**: الإسقاطاتُ الزوجيّة للقانون الثلاثيّ تُبيح كلَّ زوج، فربطُها يقبل التكاليف الثمانية، والقانونُ نفسُه أربعة —
    فإسقاطُ متغيّرٍ مشتركٍ قبل الربط يزيد حلولًا زائفة. -/
theorem wajiha_daruriyya :
    (thulathiyyat.filter fun t =>
        (thulathiyyat.any fun u => xor3 u && u.1 == t.1 && u.2.1 == t.2.1) &&
        (thulathiyyat.any fun u => xor3 u && u.2.1 == t.2.1 && u.2.2 == t.2.2) &&
        (thulathiyyat.any fun u => xor3 u && u.1 == t.1 && u.2.2 == t.2.2)).length = 8 ∧
    (thulathiyyat.filter xor3).length = 4 := by decide

/-! ## ٥. العقدُ حالةٌ من Φ (تعميمُ `kull_ma_kull`) -/

/-- عاملُ القانون: مرخِّصٌ أو ممتنع. -/
def amilQanun (A : Aqd) (x : List Nat) : K3 := if A.qanun x then P else N
/-- عاملُ المانع: يمنع المدلولَ إن رُفع بتُّه، وإلّا رخّص. -/
def amilMani (A : Aqd) (x : List Nat) (m : Nat) : K3 := if (A.mani x).testBit m then N else P
/-- عاملُ الجذر: المرشَّحُ مرخِّص، وغيرُه «لا حكم» لا ممتنع. -/
def amilJidhr (A : Aqd) (x : List Nat) (r : Nat) : K3 := if A.jidhr x = some r then P else U
/-- عاملُ الشاهد: الجذرُ المشهودُ له بالمدلول مرخِّص، وغيرُه «لا حكم» — الغيابُ ليس امتناعًا. -/
def amilShahid (A : Aqd) (x : List Nat) (r m : Nat) : K3 := if (mustawa A x r).testBit m then P else U

theorem amilQanun_P (A : Aqd) (x : List Nat) : amilQanun A x = P ↔ A.qanun x = true := by
  cases h : A.qanun x <;> simp [amilQanun, h]
theorem amilQanun_N (A : Aqd) (x : List Nat) : amilQanun A x = N ↔ A.qanun x = false := by
  cases h : A.qanun x <;> simp [amilQanun, h]
theorem amilMani_P (A : Aqd) (x : List Nat) (m : Nat) : amilMani A x m = P ↔ (A.mani x).testBit m = false := by
  cases h : (A.mani x).testBit m <;> simp [amilMani, h]
theorem amilMani_N (A : Aqd) (x : List Nat) (m : Nat) : amilMani A x m = N ↔ (A.mani x).testBit m = true := by
  cases h : (A.mani x).testBit m <;> simp [amilMani, h]
theorem amilJidhr_P (A : Aqd) (x : List Nat) (r : Nat) : amilJidhr A x r = P ↔ A.jidhr x = some r := by
  by_cases h : A.jidhr x = some r <;> simp [amilJidhr, h]
/-- الجذرُ غيرُ المرشَّح لا يمنع. -/
theorem amilJidhr_ghayr_N (A : Aqd) (x : List Nat) (r : Nat) : amilJidhr A x r ≠ N := by
  by_cases h : A.jidhr x = some r <;> simp [amilJidhr, h]
theorem amilShahid_P (A : Aqd) (x : List Nat) (r m : Nat) :
    amilShahid A x r m = P ↔ (mustawa A x r).testBit m = true := by
  cases h : (mustawa A x r).testBit m <;> simp [amilShahid, h]
/-- غيابُ الشاهد لا يمنع. -/
theorem amilShahid_ghayr_N (A : Aqd) (x : List Nat) (r m : Nat) : amilShahid A x r m ≠ N := by
  cases h : (mustawa A x r).testBit m <;> simp [amilShahid, h]

/-- **Φ على العقد**: القانونُ والمانعُ مربوطان بتركيبِ عاملِ الجذر وعاملِ الشاهد على منفذ الجذر (`tarkib` بعينه، ونطاقُه نطاقُ الجذور). -/
def phiAqd (A : Aqd) (x : List Nat) (m : Nat) (judhur : List Nat) : K3 :=
  wa (amilQanun A x) (wa (amilMani A x m)
    (tarkib judhur (fun (_ : Unit) r => amilJidhr A x r) (fun r (_ : Unit) => amilShahid A x r m) () ()))

theorem phi_P (A : Aqd) (x : List Nat) (m : Nat) (judhur : List Nat)
    (hd : ∀ r, A.jidhr x = some r → r ∈ judhur) :
    phiAqd A x m judhur = P ↔ Murakhkhas A x m := by
  simp only [phiAqd, wa_P, tarkib_P, amilQanun_P, amilMani_P, amilJidhr_P, amilShahid_P, mustawa_iff, Murakhkhas]
  constructor
  · rintro ⟨hq, hn, r, _, hj, hs⟩; exact ⟨hq, hn, r, hj, hs⟩
  · rintro ⟨hq, hn, r, hj, hs⟩; exact ⟨hq, hn, r, hd r hj, hj, hs⟩

theorem phi_N (A : Aqd) (x : List Nat) (m : Nat) (judhur : List Nat) (hne : judhur ≠ []) :
    phiAqd A x m judhur = N ↔ Mumtani A x m := by
  simp only [phiAqd, Mumtani, wa_N, tarkib_N, amilQanun_N, amilMani_N]
  have hy : ¬ ∀ r ∈ judhur, amilJidhr A x r = N ∨ amilShahid A x r m = N := by
    intro h
    cases judhur with
    | nil => exact hne rfl
    | cons r _ =>
      rcases h r (by simp) with h1 | h1
      · exact amilJidhr_ghayr_N A x r h1
      · exact amilShahid_ghayr_N A x r m h1
  constructor
  · rintro (h | h | h)
    · exact Or.inl h
    · exact Or.inr h
    · exact absurd h hy
  · rintro (h | h)
    · exact Or.inl h
    · exact Or.inr (Or.inl h)

/-- **العقدُ حالةٌ من Φ** (تعميمُ `kull_ma_kull`): لكلّ عقدٍ ودالٍّ ومدلول، ولكلّ نطاقِ جذورٍ غيرِ فارغ يحوي كلَّ مرشَّح، فمراتبُ `hukmB`
    الثلاث هي مراتبُ Φ على العوامل الأربعة بعينها. -/
theorem aqd_phi (A : Aqd) (x : List Nat) (m : Nat) (judhur : List Nat)
    (hd : ∀ r, A.jidhr x = some r → r ∈ judhur) (hne : judhur ≠ []) :
    ((∃ q, hukmB A x m = .murakhkhas q) ↔ phiAqd A x m judhur = P) ∧
    ((∃ s, hukmB A x m = .mumtani s) ↔ phiAqd A x m judhur = N) ∧
    (hukmB A x m = .laHukm ↔ phiAqd A x m judhur = U) := by
  have K := kull_ma_kull A x m
  have hP := phi_P A x m judhur hd
  have hN := phi_N A x m judhur hne
  refine ⟨K.1.trans hP.symm, K.2.1.trans hN.symm, ?_⟩
  rw [K.2.2.1]
  constructor
  · rintro ⟨h1, h2⟩
    cases e : phiAqd A x m judhur
    · exact absurd (hP.mp e) h1
    · exact absurd (hN.mp e) h2
    · rfl
  · intro e
    constructor
    · intro h; rw [hP.mpr h] at e; cases e
    · intro h; rw [hN.mpr h] at e; cases e

/-- **نطاقُ جذور Mashru**: كلُّ مرشَّحٍ دون 32768 (حقولُ خمسة بتّاتٍ ثلاثة). -/
theorem jidhr_hadd (n : JadwalLuzum.Naw) (x : List Nat) (r : Nat) (h : (Mashru n).jidhr x = some r) : r < 32768 := by
  obtain ⟨hs, hr⟩ := jidhr_salim n x r h
  have hl : x.length = 3 := by
    simp only [Mashru] at h
    split at h
    · rename_i hc; exact hc.1
    · cases h
  match x, hl with
  | [a, b, c], _ =>
    subst hr
    have ha := (hs (Jisr.JisrDal.harf a) (by simp)).1
    have hb := (hs (Jisr.JisrDal.harf b) (by simp)).1
    have hc := (hs (Jisr.JisrDal.harf c) (by simp)).1
    simp only [List.map, ramz32, List.foldl]
    omega

/-- **عقدُ Mashru حالةٌ من Φ** بنطاق الجذور 32768. -/
theorem aqd_phi_mashru (n : JadwalLuzum.Naw) (x : List Nat) (m : Nat) :
    ((∃ q, hukmB (Mashru n) x m = .murakhkhas q) ↔ phiAqd (Mashru n) x m (List.range 32768) = P) ∧
    ((∃ s, hukmB (Mashru n) x m = .mumtani s) ↔ phiAqd (Mashru n) x m (List.range 32768) = N) ∧
    (hukmB (Mashru n) x m = .laHukm ↔ phiAqd (Mashru n) x m (List.range 32768) = U) :=
  aqd_phi (Mashru n) x m (List.range 32768)
    (fun r h => List.mem_range.mpr (jidhr_hadd n x r h)) (by simp)

/-- **شاهدان** (على الشاهد بنقلٍ عبر `aqd_phi_mashru`): كَتَبَ ← «علم» ترادفًا مرخَّصٌ في Φ، ولزومًا «لا حكم» — الغيابُ ليس امتناعًا. -/
theorem kataba_phi :
    phiAqd (Mashru .taraduf) kataba (ramzNass "علم") (List.range 32768) = P ∧
    phiAqd (Mashru .luzum) kataba (ramzNass "علم") (List.range 32768) = U := by
  refine ⟨(aqd_phi_mashru .taraduf kataba _).1.mp ?_, (aqd_phi_mashru .luzum kataba _).2.2.mp (kataba_luzum_la_hukm _)⟩
  obtain ⟨q, hq, _⟩ := kataba_ilm_taraduf
  exact ⟨q, hq⟩

end Phi
end Nizam
