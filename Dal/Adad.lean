/-
  Dal/Adad.lean — عددُ سلسلة الخلايا: ترقيمٌ تقابليٌّ لكلّ سلسلةٍ منتهية، والوصلُ عمليّةٌ على الأعداد.

  قولُ المالك (2026-10-21، 20:35 بتوقيت عمّان)، في آخر تحليلٍ لصقه عن «ترميزٍ يحفظ العمليات»: «انت يجب انت تعمل بمنطق رقمي وفق
  الطريقة العقلية ححل واستنتج وطبق». والصيغةُ من ذلك التحليل نفسِه: F(w) = Σ_{j<n} 116^j + Σ_i dᵢ·116^(n−1−i)، وقانونُ الوصل
  F(uv) = 116^|v|·F(u) + F(v) — وقال إنّه فحصه حسابيًّا ولم يُبرهَن في Lean. وهنا يُبرهَن على خلايا Mashru (`4·حامل + حالة` بترتيب
  `Dal.hawamil`)؛ فأعدادُ أمثلته («كَ» 84، «كَتَبَ» 1,144,809) على ترتيب حوامل مستودعٍ آخر لم أقرأه، ولا تنتقل إلى هنا (`kataba_wasl`).

  الصيغتان واحدة: F(w) = Σ (dᵢ+1)·116^(n−1−i)، أي كلُّ خانةٍ d تُعدّ d+1 فلا منزلةَ صفر؛ فيُحسب من آخر السلسلة (`adadR` على المقلوب).

  ما يُبرهَن:
  ١. **الوصل** (`adad_wasl`): عددُ الموصول من عددَي الجزأين وطولِ الثاني وحده.
  ٢. **التقابل على المجال** (الخلايا أقلّ من 116): لا يجمع سلسلتين في عدد (`adad_inj`)، ولكلّ عددٍ سلسلةٌ في المجال تعود إليه
     (`adad_fakk`، `fakk_majal`)، والفكُّ يعيد السلسلة (`fakk_adad`). وخارجَ المجال (حدُّ الكلمة 116 فما فوق) لا تقابل، فمن يستعمل العددَ
     رمزًا يحرس المجال أوّلًا.
  ٣. **أثرُ تبديل خانةٍ في موضعها** (`adad_tabdil`): يتغيّر العددُ بفرق الخانتين في منزلتها وحده؛ وتبديلُ الحركة وحدها فرقُ حالتين لا يتعلّق
     بترتيب الحوامل («كَتَبَ» ← «كُتِبَ»: 13,688، `kataba_kutiba`).
  ٤. **لماذا d+1** (`bila_tul_yajma`): الطيُّ بالأساس 116 بلا إزاحةٍ يجمع «أَبُو» (أوّلُها «ءَ» خليّةُ 0) و«بُو» في عددٍ واحد، وعددُهما هنا مختلف.

  14 مبرهنة بالمعيار الموحَّد (`Nizam/Asas.lean`): 11 لكلّ (`adadR_append`، `adad_wasl`، `adadR_inj`، `adad_inj`، `fakkR_adadR`،
  `adadR_fakkR`، `fakkR_majal`، `fakk_adad`، `adad_fakk`، `fakk_majal`، `adad_tabdil`)، ولا تعريفيّة، و3 على الشاهد (`kataba_wasl`،
  `kataba_kutiba`، `bila_tul_yajma`). طفراتُها P414–P415 في `tahaqquq/tafrat.json` تُفشل `lake build`؛ وأعدادُ «كَتَبَ» و«كُتِبَ» فيهما يحسبها
  `tahaqquq/test_qawaid.py` §٤ من صورتيهما اليدويّتين بصيغة التحليل بحدّيها، مستقلًّا عن `adadR`.
  لا يُدّعى: أنّ هذا العددَ عددُ الشهادة (لا يحمل همزةَ الوصل ولا «ال» ولا حدودَ الكلمات)؛ ولا أنّ وصلَ خليّتين مرخَّصٌ لغةً — الوصلُ
  هنا حسابٌ على الأعداد، والترخيصُ لقانون الدالّ.
  بلا sorry ولا axiom ولا native_decide.
-/

namespace Dal
namespace Adad

/-- عددُ السلسلة من آخرها: الخانةُ الأولى من القائمة أدنى منزلة، وكلُّ خانةٍ d تُعدّ d+1. -/
def adadR : List Nat → Nat
  | [] => 0
  | d :: l => d + 1 + 116 * adadR l

/-- **عددُ السلسلة**: F(w) = Σ (dᵢ+1)·116^(n−1−i). -/
def adad (w : List Nat) : Nat := adadR w.reverse

theorem adadR_append : ∀ (a b : List Nat), adadR (a ++ b) = adadR a + 116 ^ a.length * adadR b
  | [], b => by simp [adadR]
  | d :: a, b => by
    simp only [List.cons_append, adadR, List.length_cons, adadR_append a b, Nat.pow_succ]
    have : 116 ^ a.length * 116 * adadR b = 116 * (116 ^ a.length * adadR b) := by
      rw [Nat.mul_comm (116 ^ a.length) 116, Nat.mul_assoc]
    rw [this, Nat.mul_add]; omega

/-- **قانونُ الوصل:** F(u ++ v) = 116^|v|·F(u) + F(v). -/
theorem adad_wasl (u v : List Nat) : adad (u ++ v) = 116 ^ v.length * adad u + adad v := by
  unfold adad
  rw [List.reverse_append, adadR_append, List.length_reverse]
  omega

theorem adadR_inj : ∀ (a b : List Nat), (∀ x ∈ a, x < 116) → (∀ x ∈ b, x < 116) → adadR a = adadR b → a = b
  | [], [], _, _, _ => rfl
  | [], e :: b, _, _, h => by simp [adadR] at h <;> omega
  | d :: a, [], _, _, h => by simp [adadR] at h <;> omega
  | d :: a, e :: b, ha, hb, h => by
    simp only [adadR] at h
    have hd := ha d List.mem_cons_self
    have he := hb e List.mem_cons_self
    have hde : d = e := by omega
    subst hde
    have hab : adadR a = adadR b := by omega
    rw [adadR_inj a b (fun x hx => ha x (List.mem_cons_of_mem _ hx)) (fun x hx => hb x (List.mem_cons_of_mem _ hx)) hab]

/-- **لا يجمع سلسلتين في المجال في عددٍ واحد.** -/
theorem adad_inj (u v : List Nat) (hu : ∀ x ∈ u, x < 116) (hv : ∀ x ∈ v, x < 116) (h : adad u = adad v) : u = v := by
  have := adadR_inj u.reverse v.reverse (fun x hx => hu x (List.mem_reverse.mp hx))
    (fun x hx => hv x (List.mem_reverse.mp hx)) h
  exact List.reverse_inj.mp this

/-! ## الفكّ: لكلّ عددٍ سلسلتُه -/

/-- الفكُّ من آخر السلسلة، بوقودٍ يكفيه العددُ نفسُه. -/
def fakkR : Nat → Nat → List Nat
  | 0, _ => []
  | f + 1, n => if n = 0 then [] else (n - 1) % 116 :: fakkR f ((n - 1) / 116)

def fakk (n : Nat) : List Nat := (fakkR n n).reverse

theorem fakkR_adadR : ∀ (a : List Nat), (∀ x ∈ a, x < 116) → ∀ f, adadR a ≤ f → fakkR f (adadR a) = a
  | [], _, f, _ => by cases f <;> simp [fakkR, adadR]
  | d :: a, ha, f, hf => by
    have hd := ha d List.mem_cons_self
    obtain ⟨f', rfl⟩ : ∃ f', f = f' + 1 := ⟨f - 1, by simp only [adadR] at hf; omega⟩
    simp only [adadR] at hf ⊢
    simp only [fakkR]
    have hne : ¬ (d + 1 + 116 * adadR a = 0) := by omega
    have hm : (d + 1 + 116 * adadR a - 1) % 116 = d := by omega
    have hq : (d + 1 + 116 * adadR a - 1) / 116 = adadR a := by omega
    simp only [hne, ↓reduceIte]
    rw [hm, hq, fakkR_adadR a (fun x hx => ha x (List.mem_cons_of_mem _ hx)) f' (by omega)]

theorem adadR_fakkR : ∀ (f n : Nat), n ≤ f → adadR (fakkR f n) = n
  | 0, n, h => by simp [fakkR, adadR]; omega
  | f + 1, n, h => by
    simp only [fakkR]
    split
    · rename_i h0; simp [adadR, h0]
    · rename_i h0
      simp only [adadR]
      rw [adadR_fakkR f ((n - 1) / 116) (by omega)]
      omega

theorem fakkR_majal : ∀ (f n : Nat), ∀ x ∈ fakkR f n, x < 116
  | 0, _, x, hx => by simp [fakkR] at hx
  | f + 1, n, x, hx => by
    simp only [fakkR] at hx
    split at hx
    · simp at hx
    · rcases List.mem_cons.mp hx with h | h
      · rw [h]; exact Nat.mod_lt _ (by decide)
      · exact fakkR_majal f _ x h

/-- **الفكُّ يعيد السلسلة** ما كانت خلاياها في المجال. -/
theorem fakk_adad (w : List Nat) (hw : ∀ x ∈ w, x < 116) : fakk (adad w) = w := by
  unfold fakk adad
  rw [fakkR_adadR w.reverse (fun x hx => hw x (List.mem_reverse.mp hx)) _ (Nat.le_refl _), List.reverse_reverse]

/-- **الشمول:** كلُّ عددٍ عددُ سلسلة. -/
theorem adad_fakk (n : Nat) : adad (fakk n) = n := by
  unfold adad fakk
  rw [List.reverse_reverse, adadR_fakkR n n (Nat.le_refl _)]

/-- وسلسلتُه في المجال. -/
theorem fakk_majal (n : Nat) : ∀ x ∈ fakk n, x < 116 := by
  intro x hx
  exact fakkR_majal n n x (List.mem_reverse.mp hx)

/-- **أثرُ تبديل خانةٍ في موضعها:** بين `a ++ d :: b` و`a ++ e :: b` فرقُ (e − d)·116^|b| (مكتوبًا بلا طرحٍ في ℕ). -/
theorem adad_tabdil (a b : List Nat) (d e : Nat) :
    adad (a ++ e :: b) + 116 ^ b.length * d = adad (a ++ d :: b) + 116 ^ b.length * e := by
  have k : ∀ x, adad (a ++ x :: b) = 116 ^ b.length * (116 * adad a + (x + 1)) + adad b := by
    intro x
    rw [show a ++ x :: b = (a ++ [x]) ++ b by simp, adad_wasl, adad_wasl]
    simp [adad, adadR]
  rw [k e, k d, Nat.mul_add, Nat.mul_add, Nat.mul_add, Nat.mul_add]
  omega

/-! ## على الشاهد -/

/-- «كَتَبَ» بخلايا Mashru (`Nizam.Aqd.kataba`: ك 8، ت 18، ب 26 بالفتحة) عددُها 452,621؛ وهو وصلُ «كَ» (33) و«تَبَ» (8,573) بقانون الوصل. -/
theorem kataba_wasl :
    adad [32, 72, 104] = 452621 ∧ adad [32] = 33 ∧ adad [72, 104] = 8573 ∧ 116 ^ 2 * 33 + 8573 = 452621 := by decide

/-- «كُتِبَ» (ضمّةٌ ثمّ كسرة) تزيد على «كَتَبَ» بـ 1·116² + 2·116 = 13,688. -/
theorem kataba_kutiba : adad [33, 74, 104] = adad [32, 72, 104] + 13688 := by decide

/-- **الطيُّ بلا إزاحةٍ يجمع**: «أَبُو» [0، 105، 115] و«بُو» [105، 115] عددٌ واحدٌ بالأساس 116 وحده (الهمزةُ المفتوحة خليّةُ 0)، وعددان
مختلفان بـ `adad`. -/
theorem bila_tul_yajma :
    [0, 105, 115].foldl (fun n d => 116 * n + d) 0 = [105, 115].foldl (fun n d => 116 * n + d) 0 ∧
    adad [0, 105, 115] ≠ adad [105, 115] := by decide

end Adad
end Dal
