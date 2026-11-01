import Aql.Qaida
import Nizam.WahdatJadwal
import SLGE.Root
import SLGE.Syllable

/-!
# الترخيصُ المتدرّج لكلّ ملفّ Lean، ووراثةُ جيناته الحسابيّة

قولُ المالك في الجلسة (2026-11-01، 19:11 بتوقيت عمّان):
«الخل ان كل module يجب ان يكون بالترخيص الجبري المتدرج فكل module يخضع لقانون الوراثة والتوريث ويدخل في ال slot machine  وهو حامل جيناته الحسابية»
ثمّ اختار من سؤالين متعدّدَي الخيارات نصُّ خياراتهما من البنّاء «كلُّ ملفّ Lean في المشروع» معنًى لـ module،
و«بعد الفرع الحاليّ في طلبٍ مستقلّ (موصى به)» ترتيبًا. ووصفُ الخيار الأوّل «لكلّ ملفٍّ رتبة، ولا يستورد إلّا ما دونها، وجيناتُه أعدادُه؛
وأكثرُ الملفّات ليس فيها آلة»، والخيارُ الموصى به كان «كلُّ آلةٍ في السلّم (موصى به)». ثمّ رسالتُه 20:05 (في `hawkama/الوراثة_الصنفية.md`
§١ بنصّها): «… يجب ان يرث كل lean ما ترخص قبله وكل اختبار ما قبله»؛ ووراثةُ الاختبارات منها لم تُبنَ (§٥ أ(5)).
ثمّ ردُّه 20:25 على مسوّدة التصميم: «Option a»، وقراءتُه §٥ أ من التصميم (الملفّات أوّلًا) قراءةُ البنّاء.

**البناء** (تعيينُ البنّاء، ينتظر إمضاءك):
- الملفّاتُ وحداتُ حزمة lake: مكتباتُ `lakefile.toml` (تسعُ مجلّدات و`Nabt.lean`) وجذورُ تنفيذيّاته؛ وخارجها `Audit.lean` و`AuditNabt.lean` وملفّاتُ
  `tahaqquq` الأربعة. والجدولُ مولَّدٌ من رؤوسها (`Nizam/WahdatJadwal.lean`)، ويطابقه محلّلُ رؤوس Lean نفسُه (`tahaqquq/test_wiratha.py`).
- كلُّ ملفٍّ يستورد من المشروع شيئًا قانونٌ في قاعدةٍ من `Aql/Qaida.lean`: مقدّماتُه ما يستورده من المشروع، ونتيجتُه هو. وما لا يستورد من المشروع
  شيئًا أصلٌ بالتعريف (`aslB`)، وليس قانونًا.
- رتبةُ الملفّ درجةُ اشتقاقه (`rutba_daraja`)، فالقاعدةُ متدرّجة (`mutadarrija`)، وما رتبتُه صفرٌ لا يُرخَّص إلّا أصلًا (`rutba_sifr_asl` من `Aql/Qaida.lean`).
- ترتيبُ البناء سلسلةٌ يقبلها فاحصُ القاعدة نفسُه (`Qaida.fahs`) فيُثبت كلَّ ملفّ (`bina_maqbul`)، فكلُّ ملفٍّ مرخَّص على أصولها
  (`kull_wahda_murakhkhasa`) — على هذا الجدول.
- وما لا يرث شيئًا قائمةٌ مسمّاة (`bilaWirth`، 53)، تطابقها رتبةُ الصفر على هذا الجدول (`bilaWirth_iff`). وملفٌّ جديدٌ يُعاد له توليدُ الجدول (يفحصه ١ و٢
  في الاختبار)، ثمّ لا يُبنى `bilaWirth_iff` إن لم يستورد من المشروع شيئًا حتى يُضاف اسمُه.
- **الأصلُ قرارُ المالك، ولم يُبنَ:** الأصلُ في `bina_maqbul` و`kull_wahda_murakhkhasa` ما رتبتُه صفرٌ كلُّه (`aslB`، بالتعريف)، ومنه ما تعدّه الوثيقةُ
  غيرَ أصل (`Jisr.BabFa` …). والمبنيُّ لقراره `rutba_sifr`: أيًّا كانت الأصولُ ‎`a`‎، ما رتبتُه صفرٌ لا يُرخَّص إلّا منها؛ فما يعدّه يتيمًا لا يُرخَّص حتى
  يُوصل بأبيه.
- **الجيناتُ الحسابيّة** (قراءةُ البنّاء): لكلّ ملفٍّ حساباتُه الصنفيّة (`SLGE.Hisab`): اسمُ كلٍّ، وعددُ أصنافه، وثابتُه (`jinatKhassa`). وجيناتُه كلُّها
  الخاصّةُ مع جينات ما يستورده (`jinat`)، فكلُّ ملفٍّ يحمل جيناتِ ما يستورده (`jinat_tuwarrath`، و`jinatKull_tuwarrath` على هذا الجدول). والاسمُ
  وأعدادُه من الثابت نفسِه (`jin!`)، وأنّ `jinatKhassa` هي حساباتُ كلّ ملفٍّ في البيئة بعينها يفحصه `tahaqquq/test_wiratha.py`.

**حدُّه:** «يدخل في ال slot machine» هنا أنّ ترتيبَ البناء سلسلةٌ يقبلها فاحصُ المحرّك (`Qaida.fahs`)، لا آلةً من `SLGE.Machine`. والترخيصُ صياغةُ ترتيب
البناء في قاعدة المحرّك: يصدق على كلّ جدولِ استيرادٍ بلا دَور مع هذه الأصول، وLean يمنع الدَّور؛ فليس شاهدًا على محتوى الملفّات. والوراثةُ هنا
وراثةُ الاستيراد والجينات، لا اشتقاقُ حساب آلةٍ من حساب أبيها (§٥ ب من التصميم، لم يُبنَ). والجدولُ استيرادُ الرؤوس، لا ما يستعمله الملفّ فعلًا.
-/

namespace Nizam
namespace Wiratha
open Qaida WahdatJadwal

/-- عددُ الملفّات. -/
def N : Nat := wahdat.length

/-- اسمُ وحدة الملفّ بموضعه. -/
def ism (i : Nat) : String := (wahdat.getD i ("", [])).1

/-- ما يستورده الملفّ من المشروع، بمواضعه. -/
def istirad (i : Nat) : List Nat := (wahdat.getD i ("", [])).2

/-- رتبةُ الملفّ. -/
def rutba (i : Nat) : Nat := rutbaJadwal.getD i 0

/-- قانونُ كلّ ملفٍّ يستورد من المشروع: مقدّماتُه ما يستورده، ونتيجتُه هو. -/
def qawanin : List (Qanun Nat) :=
  (List.range N).filterMap fun i => if istirad i = [] then none else some ⟨ism i, istirad i, i⟩

/-- قاعدةُ الملفّات. -/
def qaida : Qaida Nat := ⟨"WahdatJadwal", qawanin⟩

/-- الأصلُ: ملفٌّ في الجدول لا يستورد من المشروع شيئًا. -/
def aslB (i : Nat) : Bool := decide (i < N) && (istirad i).isEmpty

/-- سلسلةُ البناء: لكلّ ملفٍّ بترتيبه خطوةٌ — أصلٌ، أو قانونُه برقمه في القاعدة. -/
def silsila : List (Khatwa Nat) :=
  tartib.map fun i => if istirad i = [] then .asl i else .qanun ((List.range i).countP fun j => istirad j ≠ [])

/-- **الرتبةُ درجةُ الاشتقاق:** 0 لما لا يستورد من المشروع شيئًا، وإلّا واحدٌ فوق أعلى ما يستورده — على الجدول. -/
theorem rutba_daraja : ∀ i < N, rutba i = (istirad i).foldr (fun j a => max a (rutba j + 1)) 0 := by
  decide +kernel

/-- **القاعدةُ متدرّجة:** لكلّ قانونٍ مقدّماتٌ، وكلُّ مقدّمةٍ أدنى رتبةً من نتيجته — على الجدول. -/
theorem mutadarrija : Mutadarrija qaida rutba := by
  unfold Mutadarrija; decide +kernel

/-- **البناءُ سلسلةٌ مقبولة:** فاحصُ القاعدة يقبل ترتيبَ البناء خطوةً خطوة، ويُثبت به الملفّاتِ كلَّها — على الجدول. -/
theorem bina_maqbul : fahs qaida aslB [] silsila = some tartib ∧ ∀ i < N, i ∈ tartib := by
  decide +kernel

/-- **كلُّ ملفٍّ مرخَّص** في القاعدة على أصولها (`aslB`: ما رتبتُه صفر) — على هذا الجدول. -/
theorem kull_wahda_murakhkhasa : ∀ i < N, Murakhkhas qaida (fun p => aslB p = true) i := by
  intro i hi
  exact fahs_sahih qaida aslB silsila [] tartib (by simp) bina_maqbul.1 i (bina_maqbul.2 i hi)

/-- **ما رتبتُه صفرٌ لا يُرخَّص إلّا أصلًا:** أيًّا كانت الأصولُ ‎`a`‎ (قرارُ المالك)، كلُّ ملفٍّ مرخَّصٍ عليها رتبتُه صفرٌ منها. -/
theorem rutba_sifr (a : Nat → Bool) (i : Nat) (h : Murakhkhas qaida (fun p => a p = true) i) (h0 : rutba i = 0) :
    a i = true :=
  rutba_sifr_asl qaida rutba _ mutadarrija h h0

/-- ما لا يرث من المشروع شيئًا: كلُّ ملفٍّ رتبتُه صفر. أيُّها أصلٌ وأيُّها يتيمٌ يُوصل بأبيه قرارُ المالك (`hawkama/الوراثة_الصنفية.md`). -/
def bilaWirth : List String := [
  "Aql.Qaida", "Aql.WaqiRibtJadwal",
  "Dal.Adad", "Dal.AqsamAlism", "Dal.AqsamAllafz", "Dal.Khaliya", "Dal.WaqfSibawayhi",
  "Faahis.SijillMakhtum",
  "Jisr.AqsamDalMadlul", "Jisr.AwamilJadwal", "Jisr.AwamilUslub", "Jisr.BabFa", "Jisr.BaqiJaza", "Jisr.MajariKalim",
  "Jisr.QawaidJadwal", "Jisr.TartibMamul",
  "Madlul.AqsamAlmadlul", "Madlul.Dalala", "Madlul.Fard116Data", "Madlul.IshtirakData", "Madlul.JadwalLuzumNaw", "Madlul.NahtData",
  "Nabt.ArabicCoverage", "Nabt.BookCoverage", "Nabt.Cell", "Nabt.ClassicalBoundaryAffixes", "Nabt.ClassicalGemination",
  "Nabt.ClassicalHamza", "Nabt.ClassicalLanguageEvidence", "Nabt.ClassicalReferenceReadings", "Nabt.ClassicalWeak",
  "Nabt.Derivation", "Nabt.LearnedModelData", "Nabt.MaqayisRules", "Nabt.Obligations", "Nabt.PhonologicalModes",
  "Nabt.ProductiveForms", "Nabt.Program", "Nabt.PropertyEvidence", "Nabt.RationalInquiry", "Nabt.RecursiveLicensedAlgebra",
  "Nabt.RuleLearning", "Nabt.SemanticInference", "Nabt.Shakhsiyya3Rules", "Nabt.Transition",
  "Nizam.Asas", "Nizam.Damj", "Nizam.Qiyas", "Nizam.WahdatJadwal",
  "SLGE.AwamilTable", "SLGE.Core", "SLGE.MadlulAwwalan", "SLGE.TarkibLit"]

/-- **ما لا يرث مسمًّى:** رتبةُ الملفّ صفرٌ إذا وفقط إذا كان اسمُه في `bilaWirth` — على هذا الجدول. فملفٌّ جديدٌ لا يستورد من المشروع
شيئًا، بعد إعادة توليد الجدول (يفحصها الاختبار)، لا يُبنى معه هذا حتى يُضاف اسمُه. -/
theorem bilaWirth_iff : (∀ i < N, (rutba i = 0 ↔ ism i ∈ bilaWirth)) ∧ ∀ m ∈ bilaWirth, ∃ i < N, ism i = m := by
  decide +kernel

/-! ## الجيناتُ الحسابيّة -/

/-- جينٌ حسابيّ: اسمُ الحساب الصنفيّ، وعددُ أصنافه، وثابتُ طوله. -/
abbrev Jin := String × Nat × Nat

/-- جينُ الحساب الصنفيّ ‎`x`‎: اسمُه وعددُ أصنافه وثابتُه، كلُّها من الثابت نفسِه، فلا يفترق الاسمُ عن أعداده. -/
macro "jin!" x:ident : term => `(($(Lean.quote x.getId.toString), ($x).Q.m, ($x).K))

/-- جيناتُ الملفّ الخاصّة: حساباتُه الصنفيّة. -/
def jinatKhassa (m : String) : List Jin :=
  if m = "SLGE.Root" then
    [jin! SLGE.Law.HisabJadhr.hisabJadhr, jin! SLGE.Law.HisabZaid.hisabZaid]
  else if m = "SLGE.Law" then
    [jin! SLGE.Law.HisabKalima.hisabWaqf, jin! SLGE.Law.HisabKalima.hisabWasl, jin! SLGE.Law.HisabJumla.hisabJumla]
  else if m = "SLGE.Syllable" then
    [jin! SLGE.Law.HisabMaqta.hisabWaqf, jin! SLGE.Law.HisabMaqta.hisabWasl]
  else []

/-- جيناتُ الملفّ بالوراثة بوقود ‎`k`‎: الخاصّةُ، ثمّ جيناتُ ما يستورده بوقود ‎`k − 1`‎. -/
def jinat : Nat → Nat → List Jin
  | 0, i => jinatKhassa (ism i)
  | k + 1, i => jinatKhassa (ism i) ++ (istirad i).flatMap (jinat k)

/-- جيناتُ الملفّ كلُّها: بوقودٍ رتبتُه. -/
def jinatKull (i : Nat) : List Jin := jinat (rutba i) i

/-- **الخاصّةُ تبقى:** جيناتُ الملفّ الخاصّة في جيناته بأيّ وقود. -/
theorem jinat_khassa (k i : Nat) : ∀ g ∈ jinatKhassa (ism i), g ∈ jinat k i := by
  intro g hg
  cases k with
  | zero => exact hg
  | succ k => exact List.mem_append_left _ hg

/-- **التوريث:** جيناتُ ما يستورده الملفّ بوقود ‎`k`‎ في جيناته بوقود ‎`k + 1`‎. -/
theorem jinat_tuwarrath (k i j : Nat) (hj : j ∈ istirad i) : ∀ g ∈ jinat k j, g ∈ jinat (k + 1) i := by
  intro g hg
  exact List.mem_append_right _ (List.mem_flatMap.mpr ⟨j, hj, hg⟩)

/-- **الوقودُ لا يُسقط:** ما في الجينات بوقود ‎`k`‎ فيها بوقود ‎`k + 1`‎. -/
theorem jinat_ratib : ∀ k i, ∀ g ∈ jinat k i, g ∈ jinat (k + 1) i := by
  intro k
  induction k with
  | zero =>
    intro i g hg
    exact List.mem_append_left _ hg
  | succ k ih =>
    intro i g hg
    show g ∈ jinatKhassa (ism i) ++ (istirad i).flatMap (jinat (k + 1))
    have hg' : g ∈ jinatKhassa (ism i) ++ (istirad i).flatMap (jinat k) := hg
    rcases List.mem_append.mp hg' with h | h
    · exact List.mem_append_left _ h
    · obtain ⟨j, hj, hg2⟩ := List.mem_flatMap.mp h
      exact List.mem_append_right _ (List.mem_flatMap.mpr ⟨j, hj, ih j g hg2⟩)

theorem jinat_ratib_le (i : Nat) {k k' : Nat} (h : k ≤ k') : ∀ g ∈ jinat k i, g ∈ jinat k' i := by
  induction h with
  | refl => exact fun g hg => hg
  | step _ ih => exact fun g hg => jinat_ratib _ i g (ih g hg)

/-- كلُّ ما يستورده الملفّ أدنى منه رتبةً — على الجدول. -/
theorem istirad_adna : ∀ i < N, ∀ j ∈ istirad i, rutba j < rutba i := by
  decide +kernel

/-- **كلُّ ملفٍّ يحمل جيناتِ ما يستورده كلَّها:** على الجدول، بالتدرّج. -/
theorem jinatKull_tuwarrath (i : Nat) (hi : i < N) (j : Nat) (hj : j ∈ istirad i) :
    ∀ g ∈ jinatKull j, g ∈ jinatKull i := by
  intro g hg
  have hlt := istirad_adna i hi j hj
  obtain ⟨k, hk⟩ : ∃ k, rutba i = k + 1 := ⟨rutba i - 1, by omega⟩
  unfold jinatKull at hg ⊢
  rw [hk]
  exact jinat_tuwarrath k i j hj g (jinat_ratib_le j (by omega) g hg)

/-- **الشاهد:** آلاتُ المالك السبع في ثلاثة ملفّات بحساباتها، وأصنافُها وثوابتُها مقروءةٌ منها. -/
theorem shahid_jinat :
    jinatKhassa "SLGE.Root" = [("SLGE.Law.HisabJadhr.hisabJadhr", 5, 1), ("SLGE.Law.HisabZaid.hisabZaid", 10, 2)] ∧
    jinatKhassa "SLGE.Law" = [("SLGE.Law.HisabKalima.hisabWaqf", 13, 2), ("SLGE.Law.HisabKalima.hisabWasl", 13, 2),
      ("SLGE.Law.HisabJumla.hisabJumla", 13, 3)] ∧
    jinatKhassa "SLGE.Syllable" = [("SLGE.Law.HisabMaqta.hisabWaqf", 8, 2), ("SLGE.Law.HisabMaqta.hisabWasl", 8, 2)] := by
  decide +kernel

end Wiratha
end Nizam
