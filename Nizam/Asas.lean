/-
  Nizam/Asas.lean — النواةُ المبرهنةُ للمنظومة الموحّدة (م0 في `hawkama/البروتوكول.md`؛ قرار المالك 2026-10-18، 19:39: «نفذ»).
  لا تستورد شيئًا: كلُّ جسرٍ في الطبقات (أطلسها `Nizam/atlas.tsv`) يُصاغ عليها؛ وتركيبُ المحرّك سلسلةً واحدةً عليها هو م1.

  ثلاثُ دعاوى مركزيّة في البروتوكول، تُبرهن هنا لكلّ طبقةٍ ولكلّ قاعدة، لا على مثال:
  ١. الجسورُ تتركّب في سلسلةٍ واحدة (`tarkib` تجميعيّ وله محايد)، والسلامةُ تتركّب معها (`salama_tatarakkab`).
  ٢. «شرطُ الإمكان»: لا ترخيصَ في طبقةٍ إلّا وقد رُخّص ما قبلها (`la_tarkhis_bila_ma_qablahu`)، و«لا حكم» يسري ولا
     ينقلب امتناعًا ولا ترخيصًا (`la_hukm_yasri`)، والممتنعُ يسري باسمه (`mumtani_yasri`).
  ٣. تحويلُ الاستقراء إلى مبرهنة بحدّ النبهاني للقاعدة الكلّيّة (ج3 س1034–س1037: «الحكم الكلي المنطبق على جزئياته»،
     «تندرج جزئياته تحتها»، «إلا أن يرد نص شرعي على خلاف ما في القاعدة … وتلغى القاعدة»): القاعدةُ تصدق على المودَع
     بمخالفاتها المشهودة استثناءً (`tasduq_bi_mukhalifat`)، وهذه أصغرُ استثناءٍ يُصدِقها (`mukhalifat_dunya`)؛
     والدعوى لا تُطلق على اللغة بل على المودَع المسمّى (الدستور م17).
  ومعها القياسُ بأركانه (ج3 س845): لا إلحاقَ بلا علّةٍ لها دليل (`la_ilhaq_bila_illa`)، ولا بمجرّد الشبه (س829، س870).
  بلا sorry ولا axiom ولا native_decide.
-/

namespace Nizam

/-! ## ١. الحكم الثلاثيّ والجسر -/

/-- مخرجُ كلّ طبقة: مرخَّصٌ بقيمته، أو لا حكم (غيابُ الشاهد)، أو ممتنعٌ باسم سببه. -/
inductive Hukm (α : Type) where
  | murakhkhas (a : α)
  | laHukm
  | mumtani (sabab : String)
  deriving DecidableEq, Repr

namespace Hukm
def bind {α β : Type} : Hukm α → (α → Hukm β) → Hukm β
  | murakhkhas a, f => f a
  | laHukm, _ => laHukm
  | mumtani s, _ => mumtani s
end Hukm

/-- الجسرُ من طبقةٍ إلى التي تليها. -/
abbrev Jisr (α β : Type) := α → Hukm β

def huwiyya {α : Type} : Jisr α α := Hukm.murakhkhas

/-- تركيبُ جسرين: الثاني لا يعمل إلّا على ما رخّصه الأوّل. -/
def tarkib {α β γ : Type} (f : Jisr α β) (g : Jisr β γ) : Jisr α γ := fun a => (f a).bind g

theorem tarkib_huwiyya_yamin {α β : Type} (f : Jisr α β) : tarkib f huwiyya = f := by
  funext a; unfold tarkib huwiyya; cases f a <;> rfl

theorem tarkib_huwiyya_yasar {α β : Type} (f : Jisr α β) : tarkib huwiyya f = f := by
  funext a; rfl

/-- التركيبُ تجميعيّ: سلسلةُ الطبقات واحدةٌ أيًّا كان تجميعُها. -/
theorem tarkib_tajmii {α β γ δ : Type} (f : Jisr α β) (g : Jisr β γ) (h : Jisr γ δ) :
    tarkib (tarkib f g) h = tarkib f (tarkib g h) := by
  funext a; unfold tarkib; cases f a <;> rfl

/-! ## ٢. السلامة وشرط الإمكان -/

/-- الجسرُ سليمٌ بين شرطَي طبقتيه: ما صحّ في الأولى لا يُرخَّص منه في الثانية إلّا صحيح. -/
def Salim {α β : Type} (P : α → Prop) (Q : β → Prop) (f : Jisr α β) : Prop :=
  ∀ a b, P a → f a = .murakhkhas b → Q b

/-- السلامةُ تتركّب: برهانُ كلّ جسرٍ وحده يكفي لبرهان السلسلة كلّها. -/
theorem salama_tatarakkab {α β γ : Type} {P : α → Prop} {Q : β → Prop} {R : γ → Prop}
    {f : Jisr α β} {g : Jisr β γ} (hf : Salim P Q f) (hg : Salim Q R g) : Salim P R (tarkib f g) := by
  intro a c hp h
  unfold tarkib at h
  cases hfa : f a with
  | murakhkhas b => rw [hfa] at h; exact hg b c (hf a b hp hfa) h
  | laHukm => rw [hfa] at h; cases h
  | mumtani s => rw [hfa] at h; cases h

/-- شرطُ الإمكان: لا ترخيصَ في السلسلة إلّا بترخيص الطبقة السابقة بعينه. -/
theorem la_tarkhis_bila_ma_qablahu {α β γ : Type} (f : Jisr α β) (g : Jisr β γ) (a : α) (c : γ)
    (h : tarkib f g a = .murakhkhas c) : ∃ b, f a = .murakhkhas b ∧ g b = .murakhkhas c := by
  unfold tarkib at h
  cases hfa : f a with
  | murakhkhas b => rw [hfa] at h; exact ⟨b, rfl, h⟩
  | laHukm => rw [hfa] at h; cases h
  | mumtani s => rw [hfa] at h; cases h

/-- «لا حكم» يسري: غيابُ الشاهد في طبقةٍ لا يصير فوقها ترخيصًا ولا امتناعًا. -/
theorem la_hukm_yasri {α β γ : Type} (f : Jisr α β) (g : Jisr β γ) (a : α) (h : f a = .laHukm) :
    tarkib f g a = .laHukm := by
  unfold tarkib; rw [h]; rfl

/-- والممتنعُ يسري باسم سببه نفسه. -/
theorem mumtani_yasri {α β γ : Type} (f : Jisr α β) (g : Jisr β γ) (a : α) (s : String)
    (h : f a = .mumtani s) : tarkib f g a = .mumtani s := by
  unfold tarkib; rw [h]; rfl

/-! ## ٣. القاعدة الكلّيّة: تحويل الاستقراء إلى مبرهنةٍ على المودَع (ج3 س1034–س1037) -/

/-- القاعدة: لفظٌ كلّيّ تندرج تحته الجزئيّات، وحكمٌ منسوبٌ إليه، واستثناءٌ هو ما ورد النقلُ بخلافه. -/
structure QaidaKulliya (α : Type) where
  kulli : α → Bool
  hukm : α → Bool
  istithna : List α

variable {α : Type} [DecidableEq α]

/-- صدقُ القاعدة على مودَع: كلُّ مشهودٍ مندرجٍ غيرِ مستثنى يأخذ الحكم. -/
def tasduq (q : QaidaKulliya α) (m : List α) : Bool :=
  m.all fun x => !q.kulli x || decide (x ∈ q.istithna) || q.hukm x

theorem tasduq_iff (q : QaidaKulliya α) (m : List α) :
    tasduq q m = true ↔ ∀ x ∈ m, q.kulli x = true → x ∉ q.istithna → q.hukm x = true := by
  unfold tasduq
  simp only [List.all_eq_true, Bool.or_eq_true, Bool.not_eq_true', decide_eq_true_eq]
  constructor
  · intro h x hx hk hi
    rcases h x hx with (h1 | h1) | h1
    · rw [hk] at h1; cases h1
    · exact absurd h1 hi
    · exact h1
  · intro h x hx
    by_cases hk : q.kulli x = true
    · by_cases hi : x ∈ q.istithna
      · exact Or.inl (Or.inr hi)
      · exact Or.inr (h x hx hk hi)
    · exact Or.inl (Or.inl (by simpa using hk))

/-- المخالفاتُ المشهودة: مندرجٌ في المودَع لا يأخذ الحكم. -/
def mukhalifat (q : QaidaKulliya α) (m : List α) : List α :=
  m.filter fun x => q.kulli x && !q.hukm x

/-- كلُّ قاعدةٍ تصدق على مودَعها إذا كانت مخالفاتُها المشهودةُ استثناءها. -/
theorem tasduq_bi_mukhalifat (q : QaidaKulliya α) (m : List α) :
    tasduq { q with istithna := mukhalifat q m } m = true := by
  rw [tasduq_iff]
  intro x hx hk hi
  by_cases hh : q.hukm x = true
  · exact hh
  · exfalso; apply hi
    unfold mukhalifat
    simp only [List.mem_filter]
    exact ⟨hx, by simp_all⟩

/-- وهي أصغرُ استثناءٍ يُصدِقها: كلُّ استثناءٍ يُصدِق القاعدة يحوي المخالفاتِ المشهودة كلَّها.
    فالاستقراءُ لا يُخفي مخالفًا، ولا يُعدّ مخالفًا ما ليس مخالفًا. -/
theorem mukhalifat_dunya (q : QaidaKulliya α) (m : List α) (E : List α)
    (h : tasduq { q with istithna := E } m = true) : ∀ x ∈ mukhalifat q m, x ∈ E := by
  intro x hx
  unfold mukhalifat at hx
  simp only [List.mem_filter, Bool.and_eq_true, Bool.not_eq_true'] at hx
  obtain ⟨hm, hk, hh⟩ := hx
  rw [tasduq_iff] at h
  by_cases hE : x ∈ E
  · exact hE
  · have := h x hm hk hE
    simp_all

/-! ## ٤. القياس بأركانه (ج3 س845، س868–س870) -/

/-- العلّةُ وصفٌ له دليلٌ في النقل (وإلّا فهو شبهٌ لا علّة). -/
structure Illa (α : Type) where
  wasf : α → Bool
  dalil : List String

/-- القياس: أصلٌ وحكمُه وعلّةٌ جامعة؛ وحكمُ الفرع ثمرتُه لا ركنُه. -/
structure Qiyas (α β : Type) where
  asl : α
  hukmAsl : β
  illa : Illa α

/-- الإلحاق: يُرخَّص حكمُ الأصل للفرع إن كانت للعلّة دليلٌ وتحقّقت في الأصل والفرع؛ وبلا دليلٍ لا حكم. -/
def ilhaq {β : Type} (q : Qiyas α β) (far : α) : Hukm β :=
  if q.illa.dalil = [] then .laHukm
  else if q.illa.wasf q.asl && q.illa.wasf far then .murakhkhas q.hukmAsl else .laHukm

omit [DecidableEq α] in
/-- لا إلحاقَ بلا علّةٍ لها دليل، ولا بعلّةٍ لم تتحقّق في الفرع: «لا يأتي قياس حكم على حكم لمجرد التشابه» (س870). -/
theorem la_ilhaq_bila_illa {β : Type} (q : Qiyas α β) (far : α) (b : β) (h : ilhaq q far = .murakhkhas b) :
    q.illa.dalil ≠ [] ∧ q.illa.wasf q.asl = true ∧ q.illa.wasf far = true ∧ b = q.hukmAsl := by
  unfold ilhaq at h
  split at h
  · cases h
  · rename_i hd
    split at h
    · rename_i hw
      simp only [Bool.and_eq_true] at hw
      cases h
      exact ⟨hd, hw.1, hw.2, rfl⟩
    · cases h

end Nizam
