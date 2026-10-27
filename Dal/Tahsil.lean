import Nizam.Shahada
import Dal.Makharij

/-!
# تحصيلُ النصّ ومحاذاتُه، بشهادةٍ على كلّ مقطع (الطبقة ١)

**الطلب.** رسالةُ المالك 2026-10-27 (ما حُفظ منها بنصّه وما بقي بمعناه في رأس `Nizam/Shahada.lean`)، وأوّلُ أولويّاتها إغلاقُ تحصيل
النصّ ومحاذاته قبل أيّ ترقيةٍ دلاليّة. والتصميمُ وقواعدُ التصنيف قرارُ البنّاء، ومواصفتُها التي كتب منها مؤلّفٌ مستقلٌّ العرّافَ في
`tahaqquq/tahsil/wasf.md`.

**ما كان.** القارئ (`Qari/Main.lean`، `tahlil`) يحوّل الكلمة خلايا بحلقةٍ أمريّة لا تحفظ موضعًا. فيُسقط ما لا خليّةَ له: التطويلَ، وألفَ
التنوين، واللامَ المدغمة، وألفَ الجماعة، وألفَ الوصل أوّلَ الكلمة. ويبدّل: ى ألفًا، وة تاءً في الوصل وهاءً في الوقف. والجسرُ إلى NABT
(`Jisr/Nabt.lean`) يقول: «مواضع المصدر مواضع خلايا معلنة؛ ليست إحداثيات بايت أو محارف Unicode مستنتجة».

**ما صار هنا.**
- **القطعُ بلا فقد:** النصُّ قائمةُ نقاط رمز، ويُقطع مقاطعَ (رأسٌ ثمّ أطولُ متتاليةٍ من العلامات بعده)؛ وضمُّ المقاطع هو النصُّ نفسُه
  (`qatta_flatten`)، ولا مقطعَ فارغ (`qatta_ghayr_farigh`)، وما بعد الرأس علاماتٌ كلُّه (`qatta_alamat`)، ورأسُ كلّ مقطعٍ بعد الأوّل
  ليس علامة (`qatta_ras`).
- **المحاذاة:** لكلّ مقطعٍ موضعُه `[a, b)` بنقاط الرمز؛ والمواضعُ متّصلةٌ تغطّي النصّ (`tahsil_tughatti`)، وكلُّ موضعٍ صالحٌ في مصدر NABT
  (`Nabt.UnitDiscovery.validSpan`) وذرّاتُه هي المقطعُ بعينه (`mawdi_sahih`).
- **التصنيف:** لكلّ مقطعٍ حكمٌ من ثلاثة: مرخَّصٌ بصنفه وخلاياه، أو معلَّقٌ باسم القاعدة الناقصة، أو مدخلٌ فاسدٌ باسم سببه (`tasnif`). فما لم
  تُبنَ قاعدتُه (همزةُ الوصل، والتنوين، والتاءُ المربوطة، والألفُ المقصورة والممدودة، وألفا التنوين والجماعة، ولامُ التعريف المدغمة،
  والحرفُ الأخيرُ بلا حركة، والشدّةُ بلا حركة، والتطويلُ بعلامة) يبقى ظاهرًا باسمه، ولا يُسقط ولا يُبدَّل.
- **سلامةُ المرخَّص:** خلايا المقطع المرخَّص تُفكّ بجدول المخارج المعلَن (`Dal.harf`) إلى رأسه (والمقعدُ همزة) وحالةِ علامته، وفي المشدَّد
  خليّةٌ ساكنةٌ من الحامل نفسِه قبلها، والمقطعُ كلُّه رأسٌ وحركةٌ وشدّةٌ على الأكثر (`tasnif_salim`). وهذا المعنى (`SahihL`) تعريفُ البنّاء.
- **الشهادة:** لكلّ مقطعٍ انتقالٌ مشهود بعقد `Nizam/Shahada.lean` (`shahada`)، وحكمُ الفاحص عليه هو حكمُ التصنيف: مرخَّص، أو تعليقٌ
  باسم القاعدة، أو مدخلٌ فاسدٌ باسم سببه (`shahada_hukm`). والعقدُ مطبَّقٌ على قواعد الترخيص الأربع (`qaida`، `shahada_tahsil_salima`).
  وصدقُ الشواهد وصحّةُ المدخل في `qaida` معرَّفان من `tasnif` و`tahsil` أنفسهما؛ فـ`shahada_tahsil_salima` تُلبس `tasnif_salim`
  و`mawdi_sahih` صورةَ العقد، ولا تزيد عليهما شاهدًا مستقلًّا. والشاهدُ المستقلُّ العرّافُ في `tahaqquq/test_tahsil.py`.
- **محاذاةُ الخلايا:** كلُّ خليّةٍ في مقطعٍ مرخَّص مقرونةٌ بموضع مقطعها بنقاط الرمز، وحاملُها رأسُه (`khalaya_muhadhat`).

**حدُّه.**
- لا وصلَ ولا وقف ولا إعرابَ ولا معجم: الطبقةُ تقطع وتحاذي وترمّز الحرفَ المحرّك وحرفَ المدّ وحدهما.
- الفاصلُ بين الكلمات U+0020 وحده، ولا تطبيعَ لـ Unicode: الصورُ المركّبة والعلاماتُ القرآنيّة خارج الثماني حروفٌ ليست في الجدول.
- المقعدُ يُرمَّز همزةً، فتسقط صورتُه من الخلايا وتبقى في الموضع. وترتيبُ الشدّة والحركة في المقطع لا تحمله الخلايا.
- مواضعُ غموض المواصفة كتب فيها مؤلّفُ العرّاف قراءتَه في `tahaqquq/tahsil/NOTES.md`، وقرأها البنّاءُ قبل كتابة هذا الملفّ. وهذا الملفّ يوافقها
  فيها اختيارًا، فاتّفاقُهما هناك ليس شاهدًا مستقلًّا. ومنها: علامتان من جنسٍ واحد متعارضتان، والشدّةُ مع السكون خليّتان ساكنتان، وحدُّ
  الكلمة غيرُ شامل، وخلايا الكلمة غيرِ المرخَّصة مضمومة.
- البدائلُ فارغةٌ في هذه الطبقة.

**المبرهنات** (31، بالمعيار الموحَّد في `Nizam/Asas.lean`):
- لكلّ (26): `hamilOf_harf`، `qatta_flatten`، `qatta_ghayr_farigh`، `qatta_alamat`، `qatta_ras`، `filterMap_hala_le`، `harfMaddOf_salim`،
  `harfHarakaOf_salim`، `tasnif_salim`، `binaMin_nass`، `tahsil_nass`، `tahsil_flatten`، `mem_tahsil_qatta`، `binaMin_hukm`، `tahsil_hukm`،
  `binaMin_tughatti`، `tahsil_tughatti`، `binaMin_muhadha`، `tahsil_muhadha`، `tughatti_mem`، `mawdi_sahih`، `tahsil_salim`، `ismSinf_ne`،
  `shahada_hukm`، `shahada_tahsil_salima`، `khalaya_muhadhat`.
- تعريفيّة (1): `fakk_khaliyaMin`.
- على الشاهد (4): `harf_sifr`، `shahid_kataba`، `shahid_shams`، `shahid_muallaq`.
-/

namespace Dal.Tahsil

open Nabt.UnitDiscovery
open Nizam.Shahada (Naqla Muqaddima Hawiyya Natija Naw Hal)

/-! ## ١. الثوابت -/

def shadda : Char := '\u0651'

/-- حالةُ العلامة: فتحة، ضمّة، كسرة، سكون. -/
def halaAlama (c : Char) : Option HalaIsm :=
  if c == '\u064E' then some .fatha
  else if c == '\u064F' then some .damma
  else if c == '\u0650' then some .kasra
  else if c == '\u0652' then some .sukun
  else none

def tanwin (c : Char) : Bool := c == '\u064B' || c == '\u064C' || c == '\u064D'

/-- علامةُ حركة: إحدى الأربع أو التنوينات الثلاثة. -/
def harakaB (c : Char) : Bool := (halaAlama c).isSome || tanwin c

/-- العلامات الثماني. -/
def alama (c : Char) : Bool := harakaB c || c == shadda

/-- مقاعدُ الهمزة. -/
def maqaid : List Char := ['أ', 'إ', 'ؤ', 'ئ']

/-- الخاصّة: التاء المربوطة، والألف المقصورة، والممدودة، وألف الوصل، والتطويل، والفراغ. -/
def khassa : List Char := ['ة', 'ى', 'آ', 'ٱ', 'ـ', ' ']

/-- الحاملُ من جدول المخارج المعلَن (`Dal.hawamil`)؛ والمقعدُ همزة. -/
def hamilOf (r : Char) : Option Hamil :=
  if r ∈ maqaid then some 0 else (List.finRange 29).find? (fun h => harf h == r)

/-- ما يُفكّ إليه الرأس: المقعدُ همزة، وغيرُه هو. -/
def raddHarf (r : Char) : Char := if r ∈ maqaid then 'ء' else r

theorem harf_sifr : harf 0 = 'ء' := by decide

/-- **الحاملُ يُفكّ إلى رأسه:** حرفُ الحامل في الجدول هو الرأس، والمقعدُ همزة. -/
theorem hamilOf_harf {r : Char} {h : Hamil} (e : hamilOf r = some h) : harf h = raddHarf r := by
  unfold hamilOf at e
  unfold raddHarf
  by_cases hm : r ∈ maqaid
  · rw [ite_eq_left hm, Option.some.injEq] at e
    subst e
    rw [ite_eq_left hm, harf_sifr]
  · rw [ite_eq_right hm] at e
    have := List.find?_some e
    simp only [beq_iff_eq] at this
    rw [ite_eq_right hm, this]

/-! ## ٢. القطع بلا فقد -/

/-- رأسٌ ثمّ أطولُ متتاليةٍ من العلامات بعده: يُبنى من الآخر، فالحرفُ يُضمّ إلى المقطع بعده إن بدأ ذلك بعلامة. -/
def qatta : List Char → List (List Char)
  | [] => []
  | c :: cs =>
    match qatta cs with
    | [] => [[c]]
    | s :: ss => if s.head?.any alama then (c :: s) :: ss else [c] :: s :: ss

/-- **بلا فقد:** ضمُّ المقاطع هو النصّ. -/
theorem qatta_flatten : ∀ t : List Char, (qatta t).flatten = t
  | [] => rfl
  | c :: cs => by
    have ih := qatta_flatten cs
    simp only [qatta]
    split
    · rename_i h; rw [h] at ih; simp at ih; simp [ih]
    · rename_i s ss h
      rw [h] at ih
      split <;> simp [← ih]

theorem qatta_ghayr_farigh : ∀ t : List Char, ∀ s ∈ qatta t, s ≠ []
  | [] => by simp [qatta]
  | c :: cs => by
    have ih := qatta_ghayr_farigh cs
    simp only [qatta]
    split
    · simp
    · rename_i s ss h
      rw [h] at ih
      split
      · intro x hx
        rcases List.mem_cons.1 hx with rfl | hx
        · simp
        · exact ih x (List.mem_cons_of_mem _ hx)
      · intro x hx
        rcases List.mem_cons.1 hx with rfl | hx
        · simp
        · exact ih x hx

/-- ما بعد الرأس علاماتٌ كلُّه. -/
theorem qatta_alamat : ∀ t : List Char, ∀ s ∈ qatta t, ∀ x ∈ s.tail, alama x = true
  | [] => by simp [qatta]
  | c :: cs => by
    have ih := qatta_alamat cs
    simp only [qatta]
    split
    · simp
    · rename_i s ss h
      rw [h] at ih
      split
      · rename_i hs
        intro x hx
        rcases List.mem_cons.1 hx with rfl | hx
        · intro y hy
          simp only [List.tail_cons] at hy
          cases s with
          | nil => simp at hy
          | cons z zs =>
            rcases List.mem_cons.1 hy with rfl | hy
            · simpa using hs
            · exact ih _ List.mem_cons_self y hy
        · exact ih x (List.mem_cons_of_mem _ hx)
      · intro x hx
        rcases List.mem_cons.1 hx with rfl | hx
        · simp
        · exact ih x hx

/-- **المقطعُ أطولُ ما يمكن:** رأسُ كلّ مقطعٍ بعد الأوّل ليس علامة. -/
theorem qatta_ras : ∀ t : List Char, ∀ s ∈ (qatta t).tail, (s.head?.any alama) = false
  | [] => by simp [qatta]
  | c :: cs => by
    have ih := qatta_ras cs
    simp only [qatta]
    split
    · simp
    · rename_i s ss h
      rw [h] at ih
      split
      · exact ih
      · rename_i hs
        intro x hx
        rcases List.mem_cons.1 hx with rfl | hx
        · simpa using hs
        · exact ih x hx

/-! ## ٣. السياق والتصنيف -/

def fasil (s : List Char) : Bool := s.head? == some ' '

/-- سياقُ المقطع في كلمته: ما قبله فيها، وهل ذلك أوّلُها، وما بعده فيها. -/
structure Siyaq where
  sabiq : Option (List Char)
  sabiqAwwal : Bool
  lahiq : Option (List Char)
  deriving DecidableEq, Repr

inductive Sinf
  | fasil
  | tatwil
  | harfMadd
  | harfHaraka
  deriving DecidableEq, Repr

inductive Hukm
  /-- مرخَّص: صنفُه وخلاياه. -/
  | L (sinf : Sinf) (khalaya : List Khaliya)
  /-- معلَّق: اسمُ القاعدة الناقصة. -/
  | P (ism : String)
  /-- مدخلٌ فاسد: اسمُ السبب. -/
  | F (ism : String)
  deriving DecidableEq, Repr

def khaliyaMin (h : Hamil) (s : HalaIsm) : Khaliya := ⟨h, s.ila⟩

/-! شروطُ القواعد بأسمائها (بترتيب المواصفة). -/

/-- ٣: الرأسُ ليس حاملًا ولا مقعدًا ولا خاصًّا. -/
def ghayrMaruf (r : Char) : Bool := (hamilOf r).isNone && !(khassa.contains r)
/-- ٤: أكثرُ من شدّة، أو أكثرُ من علامة حركة. -/
def mutaarida (ms : List Char) : Bool := ms.count shadda > 1 || (ms.filter harakaB).length > 1
/-- ٦: ألفٌ أو ألفُ وصلٍ أوّلَ الكلمة. -/
def alifAwwal (c : Siyaq) (r : Char) : Bool := (r == 'ا' || r == 'ٱ') && c.sabiq.isNone
/-- ١٢: ألفٌ مجرّدة بعد فتحتين. -/
def alifTanwin (c : Siyaq) (r : Char) (ms : List Char) : Bool :=
  r == 'ا' && ms.isEmpty && c.sabiq.any (fun p => p.tail.contains '\u064B')
/-- ١٣: ألفٌ مجرّدة آخرَ الكلمة بعد واوٍ مجرّدةٍ أو ساكنة. -/
def alifJamaa (c : Siyaq) (r : Char) (ms : List Char) : Bool :=
  r == 'ا' && ms.isEmpty && c.lahiq.isNone && (c.sabiq == some ['و'] || c.sabiq == some ['و', '\u0652'])
/-- ١٤: شدّةٌ بلا علامة حركة. -/
def shaddaBilaHaraka (ms : List Char) : Bool := ms.contains shadda && !(ms.any harakaB)
/-- ١٥أ: ا أو و أو ي مجرّدةٌ في غير أوّل الكلمة. -/
def madd (c : Siyaq) (r : Char) : Bool := (r == 'ا' || r == 'و' || r == 'ي') && c.sabiq.isSome
/-- ١٥ب: لامٌ بعد ألفٍ هي أوّلُ الكلمة، وبعدها مشدَّد. -/
def lamTarif (c : Siyaq) (r : Char) : Bool :=
  r == 'ل' && c.sabiqAwwal && c.sabiq.any (fun p => p.head? == some 'ا' || p.head? == some 'ٱ') &&
    c.lahiq.any (fun n => n.tail.contains shadda)

/-- ١٦: الحرفُ المحرَّك. -/
def harfHarakaOf (r : Char) (ms : List Char) : Hukm :=
  match hamilOf r, (ms.filterMap halaAlama).head? with
  | some h, some s =>
    .L .harfHaraka (if ms.contains shadda then [khaliyaMin h .sukun, khaliyaMin h s] else [khaliyaMin h s])
  | _, _ => .F "خلل داخلي"

/-- ١٥أ: حرفُ المدّ. -/
def harfMaddOf (r : Char) : Hukm :=
  match hamilOf r with
  | some h => .L .harfMadd [khaliyaMin h .sukun]
  | none => .F "خلل داخلي"

/-- **التصنيف:** أوّلُ قاعدةٍ تنطبق، بترتيب المواصفة (`tahaqquq/tahsil/wasf.md`، القواعد ١–١٦). -/
def tasnifRas (c : Siyaq) (r : Char) (ms : List Char) : Hukm :=
  if r == ' ' then (if ms.isEmpty then .L .fasil [] else .F "علامة على فاصل")
  else if alama r then .F "علامة بلا حامل"
  else if ghayrMaruf r then .F "حرف ليس في جدول المخارج"
  else if mutaarida ms then .F "علامتان متعارضتان"
  else if r == 'ـ' then (if ms.isEmpty then .L .tatwil [] else .P "قاعدة التطويل بعلامة")
  else if alifAwwal c r then (if ms.any harakaB then .F "ألف محرّكة في أوّل الكلمة" else .P "قاعدة همزة الوصل")
  else if r == 'ٱ' then .P "قاعدة همزة الوصل"
  else if r == 'آ' then .P "قاعدة الألف الممدودة"
  else if r == 'ة' then .P "قاعدة التاء المربوطة"
  else if r == 'ى' then .P "قاعدة الألف المقصورة"
  else if ms.any tanwin then .P "قاعدة التنوين"
  else if alifTanwin c r ms then .P "قاعدة ألف التنوين"
  else if alifJamaa c r ms then .P "قاعدة ألف الجماعة"
  else if shaddaBilaHaraka ms then .P "قاعدة الشدّة بلا حركة"
  else if ms.isEmpty then
    (if madd c r then harfMaddOf r
    else if lamTarif c r then .P "قاعدة لام التعريف المدغمة"
    else if c.lahiq.isNone then .P "قاعدة الحرف الأخير بلا حركة"
    else .F "حرف بلا حركة في غير آخر الكلمة")
  else harfHarakaOf r ms

def tasnif (c : Siyaq) : List Char → Hukm
  | [] => .F "مقطع فارغ"
  | r :: ms => tasnifRas c r ms

/-! ## ٤. سلامةُ المرخَّص -/

/-- الخليّةُ مفكوكةً بجدول المخارج: حرفُ حاملها وحالتُها. -/
def fakkKhaliya (k : Khaliya) : Char × Hala := (harf k.hamil, k.hala)

/-- **صحّةُ مخرج القاعدة:** ما يعنيه كلُّ صنفٍ مرخَّص في مقطعه وخلاياه. -/
def SahihL : Sinf → List Char → List Khaliya → Prop
  | .fasil, s, ks => s = [' '] ∧ ks = []
  | .tatwil, s, ks => s = ['ـ'] ∧ ks = []
  | .harfMadd, s, ks => ∃ r, s = [r] ∧ (r = 'ا' ∨ r = 'و' ∨ r = 'ي') ∧ ks.map fakkKhaliya = [(r, 3)]
  | .harfHaraka, s, ks => ∃ r ms st, s = r :: ms ∧ ms.filterMap halaAlama = [st] ∧
      (∀ x ∈ ms, x = shadda ∨ (halaAlama x).isSome) ∧ ms.count shadda ≤ 1 ∧
      ks.map fakkKhaliya = (if ms.contains shadda then [(raddHarf r, 3)] else []) ++ [(raddHarf r, st.ila)]

theorem filterMap_hala_le : ∀ l : List Char, (l.filterMap halaAlama).length ≤ (l.filter harakaB).length
  | [] => by simp
  | x :: xs => by
    have ih := filterMap_hala_le xs
    cases hx : halaAlama x with
    | none =>
      rw [List.filterMap_cons, hx]
      by_cases hb : harakaB x
      · rw [List.filter_cons_of_pos hb]; simp only [List.length_cons]; omega
      · rw [List.filter_cons_of_neg hb]; exact ih
    | some s =>
      have hb : harakaB x = true := by simp [harakaB, hx]
      rw [List.filterMap_cons, hx, List.filter_cons_of_pos hb]
      simp only [List.length_cons]
      omega

theorem fakk_khaliyaMin (h : Hamil) (s : HalaIsm) : fakkKhaliya (khaliyaMin h s) = (harf h, s.ila) := rfl

theorem harfMaddOf_salim (r : Char) (ks : List Khaliya) (hr : r = 'ا' ∨ r = 'و' ∨ r = 'ي')
    (h : harfMaddOf r = .L .harfMadd ks) : SahihL .harfMadd [r] ks := by
  unfold harfMaddOf at h
  cases hh : hamilOf r with
  | none => rw [hh] at h; cases h
  | some hr' =>
    rw [hh] at h
    cases h
    have hharf := hamilOf_harf hh
    have hrad : raddHarf r = r := by
      unfold raddHarf
      rcases hr with h1 | h1 | h1 <;> subst h1 <;> decide
    refine ⟨r, rfl, hr, ?_⟩
    simp only [List.map_cons, List.map_nil, fakk_khaliyaMin, hharf, hrad]
    rfl

theorem harfHarakaOf_salim (r : Char) (ms : List Char) (sinf : Sinf) (ks : List Khaliya)
    (hm : ∀ x ∈ ms, alama x = true) (n4 : mutaarida ms = false) (n11 : ms.any tanwin = false)
    (h : harfHarakaOf r ms = .L sinf ks) : SahihL sinf (r :: ms) ks := by
  unfold harfHarakaOf at h
  cases hh : hamilOf r with
  | none => rw [hh] at h; cases h
  | some hr =>
    cases hst : (ms.filterMap halaAlama).head? with
    | none => rw [hh, hst] at h; cases h
    | some st =>
      rw [hh, hst] at h
      cases h
      simp only [mutaarida, Bool.or_eq_false_iff, decide_eq_false_iff_not, gt_iff_lt, Nat.not_lt] at n4
      have hlen : (ms.filterMap halaAlama).length ≤ 1 := by
        have := filterMap_hala_le ms
        omega
      have hfm : ms.filterMap halaAlama = [st] := by
        cases hl : ms.filterMap halaAlama with
        | nil => rw [hl] at hst; cases hst
        | cons y ys =>
          rw [hl] at hst hlen
          simp only [List.head?_cons, Option.some.injEq] at hst
          subst hst
          cases ys with
          | nil => rfl
          | cons _ _ => simp at hlen
      have hall : ∀ x ∈ ms, x = shadda ∨ (halaAlama x).isSome := by
        intro x hx
        have hax := hm x hx
        simp only [alama, harakaB, Bool.or_eq_true, beq_iff_eq] at hax
        rcases hax with (hax | hax) | hax
        · exact Or.inr hax
        · have : ms.any tanwin = true := List.any_eq_true.2 ⟨x, hx, hax⟩
          rw [n11] at this; cases this
        · exact Or.inl hax
      refine ⟨r, ms, st, rfl, hfm, hall, n4.1, ?_⟩
      have hharf := hamilOf_harf hh
      split <;> simp [fakk_khaliyaMin, hharf, HalaIsm.ila]

/-- **سلامةُ المرخَّص:** مقطعٌ ما بعد رأسه علامات، يرخّصه التصنيف بصنفٍ وخلايا ⇒ صحيحٌ بمعنى صنفه. -/
theorem tasnif_salim (c : Siyaq) (s : List Char) (sinf : Sinf) (ks : List Khaliya)
    (hm : ∀ x ∈ s.tail, alama x = true) (h : tasnif c s = .L sinf ks) : SahihL sinf s ks := by
  match s, hm, h with
  | [], _, h => cases h
  | r :: ms, hm, h =>
    simp only [List.tail_cons] at hm
    change tasnifRas c r ms = _ at h
    unfold tasnifRas at h
    by_cases h1 : (r == ' ') = true
    · rw [ite_eq_left h1] at h
      by_cases h1a : ms.isEmpty = true
      · rw [ite_eq_left h1a] at h
        cases h
        simp only [beq_iff_eq] at h1
        simp only [List.isEmpty_iff] at h1a
        subst h1; subst h1a; exact ⟨rfl, rfl⟩
      · rw [ite_eq_right h1a] at h; cases h
    rw [ite_eq_right h1] at h
    by_cases h2 : alama r = true
    · rw [ite_eq_left h2] at h; cases h
    rw [ite_eq_right h2] at h
    by_cases h3 : ghayrMaruf r = true
    · rw [ite_eq_left h3] at h; cases h
    rw [ite_eq_right h3] at h
    by_cases h4 : mutaarida ms = true
    · rw [ite_eq_left h4] at h; cases h
    rw [ite_eq_right h4] at h
    by_cases h5 : (r == 'ـ') = true
    · rw [ite_eq_left h5] at h
      by_cases h5a : ms.isEmpty = true
      · rw [ite_eq_left h5a] at h
        cases h
        simp only [beq_iff_eq] at h5
        simp only [List.isEmpty_iff] at h5a
        subst h5; subst h5a; exact ⟨rfl, rfl⟩
      · rw [ite_eq_right h5a] at h; cases h
    rw [ite_eq_right h5] at h
    by_cases h6 : alifAwwal c r = true
    · rw [ite_eq_left h6] at h
      by_cases h6a : ms.any harakaB = true
      · rw [ite_eq_left h6a] at h; cases h
      · rw [ite_eq_right h6a] at h; cases h
    rw [ite_eq_right h6] at h
    by_cases h7 : (r == 'ٱ') = true
    · rw [ite_eq_left h7] at h; cases h
    rw [ite_eq_right h7] at h
    by_cases h8 : (r == 'آ') = true
    · rw [ite_eq_left h8] at h; cases h
    rw [ite_eq_right h8] at h
    by_cases h9 : (r == 'ة') = true
    · rw [ite_eq_left h9] at h; cases h
    rw [ite_eq_right h9] at h
    by_cases h10 : (r == 'ى') = true
    · rw [ite_eq_left h10] at h; cases h
    rw [ite_eq_right h10] at h
    by_cases h11 : ms.any tanwin = true
    · rw [ite_eq_left h11] at h; cases h
    rw [ite_eq_right h11] at h
    by_cases h12 : alifTanwin c r ms = true
    · rw [ite_eq_left h12] at h; cases h
    rw [ite_eq_right h12] at h
    by_cases h13 : alifJamaa c r ms = true
    · rw [ite_eq_left h13] at h; cases h
    rw [ite_eq_right h13] at h
    by_cases h14 : shaddaBilaHaraka ms = true
    · rw [ite_eq_left h14] at h; cases h
    rw [ite_eq_right h14] at h
    by_cases h15 : ms.isEmpty = true
    · rw [ite_eq_left h15] at h
      by_cases h15a : madd c r = true
      · rw [ite_eq_left h15a] at h
        have hms : ms = [] := by simpa using h15
        subst hms
        have hr : r = 'ا' ∨ r = 'و' ∨ r = 'ي' := by
          simp only [madd, Bool.and_eq_true, Bool.or_eq_true, beq_iff_eq] at h15a
          rcases h15a.1 with (h1 | h1) | h1
          · exact Or.inl h1
          · exact Or.inr (Or.inl h1)
          · exact Or.inr (Or.inr h1)
        cases sinf with
        | harfMadd => exact harfMaddOf_salim r ks hr h
        | _ => unfold harfMaddOf at h; split at h <;> cases h
      rw [ite_eq_right h15a] at h
      by_cases h15b : lamTarif c r = true
      · rw [ite_eq_left h15b] at h; cases h
      rw [ite_eq_right h15b] at h
      by_cases h15c : c.lahiq.isNone = true
      · rw [ite_eq_left h15c] at h; cases h
      · rw [ite_eq_right h15c] at h; cases h
    rw [ite_eq_right h15] at h
    exact harfHarakaOf_salim r ms sinf ks hm (by simpa using h4) (by simpa using h11) h

/-! ## ٥. البناء: المقاطعُ بمواضعها وسياقاتها وأحكامها -/

structure Maqta where
  i : Nat
  a : Nat
  b : Nat
  nass : List Char
  siyaq : Siyaq
  hukm : Hukm
  deriving Repr

def lahiqMin : List (List Char) → Option (List Char)
  | n :: _ => if fasil n then none else some n
  | [] => none

def binaMin : Nat → Nat → Option (List Char) → Bool → List (List Char) → List Maqta
  | _, _, _, _, [] => []
  | i, k, p, pa, s :: rest =>
    let c : Siyaq := ⟨p, pa, lahiqMin rest⟩
    ⟨i, k, k + s.length, s, c, tasnif c s⟩ ::
      binaMin (i + 1) (k + s.length) (if fasil s then none else some s) (if fasil s then false else p.isNone) rest

/-- **التحصيل:** مقاطعُ النصّ بمواضعها وسياقاتها وأحكامها. -/
def tahsil (t : List Char) : List Maqta := binaMin 0 0 none false (qatta t)

theorem binaMin_nass (i k : Nat) (p : Option (List Char)) (pa : Bool) (ss : List (List Char)) :
    (binaMin i k p pa ss).map (·.nass) = ss := by
  induction ss generalizing i k p pa with
  | nil => rfl
  | cons s rest ih => simp [binaMin, ih]

theorem tahsil_nass (t : List Char) : (tahsil t).map (·.nass) = qatta t := binaMin_nass _ _ _ _ _

/-- **التحصيلُ بلا فقد:** ضمُّ نصوص المقاطع هو النصّ. -/
theorem tahsil_flatten (t : List Char) : ((tahsil t).map (·.nass)).flatten = t := by
  rw [tahsil_nass, qatta_flatten]

theorem mem_tahsil_qatta {t : List Char} {m : Maqta} (h : m ∈ tahsil t) : m.nass ∈ qatta t := by
  rw [← tahsil_nass]; exact List.mem_map_of_mem h

theorem binaMin_hukm (i k : Nat) (p : Option (List Char)) (pa : Bool) (ss : List (List Char)) :
    ∀ m ∈ binaMin i k p pa ss, m.hukm = tasnif m.siyaq m.nass := by
  induction ss generalizing i k p pa with
  | nil => simp [binaMin]
  | cons s rest ih =>
    intro m hm
    simp only [binaMin, List.mem_cons] at hm
    rcases hm with rfl | hm
    · rfl
    · exact ih _ _ _ _ m hm

theorem tahsil_hukm (t : List Char) : ∀ m ∈ tahsil t, m.hukm = tasnif m.siyaq m.nass :=
  binaMin_hukm _ _ _ _ _

/-- المواضعُ متّصلةٌ من k إلى n، وكلُّ موضعٍ غيرُ فارغ. -/
def tughatti : Nat → List Maqta → Nat → Prop
  | k, [], n => k = n
  | k, m :: ms, n => m.a = k ∧ m.a < m.b ∧ tughatti m.b ms n

theorem binaMin_tughatti (i k : Nat) (p : Option (List Char)) (pa : Bool) (ss : List (List Char))
    (hne : ∀ s ∈ ss, s ≠ []) : tughatti k (binaMin i k p pa ss) (k + (ss.map List.length).sum) := by
  induction ss generalizing i k p pa with
  | nil => simp [binaMin, tughatti]
  | cons s rest ih =>
    simp only [binaMin]
    have hs : s.length > 0 := List.length_pos_iff.2 (hne s (List.mem_cons_self))
    refine ⟨rfl, ?_, ?_⟩
    · show k < k + s.length
      omega
    · rw [List.map_cons, List.sum_cons, ← Nat.add_assoc]
      exact ih _ _ _ _ (fun x hx => hne x (List.mem_cons_of_mem _ hx))

/-- **التغطية:** مواضعُ المقاطع متّصلةٌ تبدأ من 0 وتنتهي بطول النصّ، ولا موضعَ فارغ. -/
theorem tahsil_tughatti (t : List Char) : tughatti 0 (tahsil t) t.length := by
  have := binaMin_tughatti 0 0 none false (qatta t) (qatta_ghayr_farigh t)
  rwa [← List.length_flatten, qatta_flatten, Nat.zero_add] at this

theorem binaMin_muhadha (i k : Nat) (p : Option (List Char)) (pa : Bool) (ss : List (List Char))
    (pre : List Char) (hpre : pre.length = k) :
    ∀ m ∈ binaMin i k p pa ss, ((pre ++ ss.flatten).drop m.a).take (m.b - m.a) = m.nass ∧
      m.b ≤ (pre ++ ss.flatten).length := by
  induction ss generalizing i k p pa pre with
  | nil => simp [binaMin]
  | cons s rest ih =>
    intro m hm
    simp only [binaMin, List.mem_cons] at hm
    rcases hm with rfl | hm
    · subst hpre
      simp only [List.flatten_cons, List.length_append]
      refine ⟨?_, by omega⟩
      show List.take (pre.length + s.length - pre.length) (List.drop pre.length (pre ++ (s ++ rest.flatten))) = s
      rw [List.drop_left, Nat.add_sub_cancel_left, List.take_left]
    · have := ih (i + 1) (k + s.length) _ _ (pre ++ s) (by simp [hpre]) m hm
      simpa [List.append_assoc] using this

/-- **المحاذاة بنقاط الرمز:** ذرّاتُ النصّ في موضع المقطع هي المقطعُ بعينه، والموضعُ داخل النصّ. -/
theorem tahsil_muhadha (t : List Char) :
    ∀ m ∈ tahsil t, (t.drop m.a).take (m.b - m.a) = m.nass ∧ m.b ≤ t.length := by
  intro m hm
  have := binaMin_muhadha 0 0 none false (qatta t) [] rfl m hm
  simpa [qatta_flatten] using this

theorem tughatti_mem {k n : Nat} : ∀ {ms : List Maqta}, tughatti k ms n → ∀ m ∈ ms, m.a < m.b
  | [], _, _, hm => by simp at hm
  | m' :: ms, h, m, hm => by
    simp only [tughatti] at h
    rcases List.mem_cons.1 hm with rfl | hm
    · exact h.2.1
    · exact tughatti_mem h.2.2 m hm

/-- موضعُ المقطع في مصدر NABT. -/
def mawdi (src : Source Char) (m : Maqta) : Span :=
  ⟨src.sourceId, src.revision, src.scopeId, src.atomizationId, m.a, m.b⟩

/-- **الموضعُ في مصدر NABT:** صالحٌ، وذرّاتُه المقطع. -/
theorem mawdi_sahih (src : Source Char) :
    ∀ m ∈ tahsil src.atoms, validSpan src (mawdi src m) = true ∧ spanAtoms src (mawdi src m) = m.nass := by
  intro m hm
  have ⟨hat, hle⟩ := tahsil_muhadha src.atoms m hm
  have hlt := tughatti_mem (tahsil_tughatti src.atoms) m hm
  refine ⟨?_, hat⟩
  unfold validSpan
  exact decide_eq_true ⟨rfl, rfl, rfl, rfl, hlt, hle⟩

/-- **التصنيفُ سليمٌ على المقاطع:** كلُّ مقطعٍ مرخَّصٍ في التحصيل صحيحٌ بمعنى صنفه. -/
theorem tahsil_salim (t : List Char) :
    ∀ m ∈ tahsil t, ∀ sinf ks, m.hukm = .L sinf ks → SahihL sinf m.nass ks := by
  intro m hm sinf ks h
  rw [tahsil_hukm t m hm] at h
  exact tasnif_salim _ _ _ _ (qatta_alamat t _ (mem_tahsil_qatta hm)) h

/-! ## ٦. الشهادة لكلّ مقطع -/

def ismSinf : Sinf → String
  | .fasil => "Dal.Tahsil.fasil"
  | .tatwil => "Dal.Tahsil.tatwil"
  | .harfMadd => "Dal.Tahsil.harfMadd"
  | .harfHaraka => "Dal.Tahsil.harfHaraka"

def madkhalSalim : String := "مدخل سليم"

theorem ismSinf_ne (s : Sinf) : ismSinf s ≠ madkhalSalim ∧ ismSinf s ≠ "" := by cases s <;> decide

def khalayaOf : Hukm → List Khaliya
  | .L _ ks => ks
  | _ => []

/-- هويّةُ القاعدة: صنفُ المرخَّص؛ وفي المعلَّق والفاسد التصنيفُ نفسُه، واسمُ القاعدة الناقصة أو السببِ في المقدّمة. -/
def qaidaOf : Hukm → Hawiyya
  | .L s _ => ⟨ismSinf s, 1⟩
  | .P _ => ⟨"Dal.Tahsil.tasnif", 1⟩
  | .F _ => ⟨"Dal.Tahsil.tasnif", 1⟩

/-- المقدّماتُ بشواهدها: صحّةُ المدخل وقاعدةُ الصنف في المرخَّص، والقاعدةُ الناقصةُ بلا سندٍ في المعلَّق، وسببُ الفساد في الفاسد. -/
def muqaddimatOf : Hukm → List Muqaddima
  | .L s _ => [⟨madkhalSalim, .madkhal, .mashhud, "Dal.Tahsil.tasnif"⟩, ⟨ismSinf s, .shart, .mashhud, "Dal.Tahsil.tasnif"⟩]
  | .P ism => [⟨madkhalSalim, .madkhal, .mashhud, "Dal.Tahsil.tasnif"⟩, ⟨ism, .shart, .ghayrMafhus, ""⟩]
  | .F ism => [⟨ism, .madkhal, .manfi, "Dal.Tahsil.tasnif"⟩]

def haddTabaqa : String :=
  "الطبقة ١: قطع ومحاذاة بنقاط الرمز وخلايا الحرف المحرّك وحرف المدّ؛ لا وصل ولا وقف ولا إعراب"

/-- **الانتقالُ المشهود للمقطع:** مصدرُه وموضعُه، والمدخلُ (السياقُ والمقطع) والمخرجُ (الخلايا)، وهويّةُ القاعدة، ومقدّماتُها،
    وحدُّ الدعوى. -/
def shahada (src : Source Char) (m : Maqta) : Naqla (Siyaq × List Char) (List Khaliya) :=
  ⟨src, mawdi src m, (m.siyaq, m.nass), khalayaOf m.hukm, qaidaOf m.hukm, muqaddimatOf m.hukm, [], haddTabaqa⟩

def natijaOf : Hukm → Natija
  | .L _ _ => .murakhkhas
  | .P ism => .muallaq [ism]
  | .F ism => .madkhalFasid ism

/-- **حكمُ الفاحص هو حكمُ التصنيف** على كلّ مقطعٍ في التحصيل. -/
theorem shahada_hukm (src : Source Char) (m : Maqta) (hm : m ∈ tahsil src.atoms) :
    Nizam.Shahada.hukm (shahada src m) = natijaOf m.hukm := by
  have hv := (mawdi_sahih src m hm).1
  cases hh : m.hukm with
  | L s ks =>
    show Nizam.Shahada.hukm (shahada src m) = .murakhkhas
    rw [Nizam.Shahada.murakhkhas_iff]
    refine ⟨?_, ?_⟩
    · simp only [Nizam.Shahada.Naqla.marbut, shahada, hv, hh, qaidaOf, Bool.true_and, Bool.not_eq_true']
      simpa using (ismSinf_ne s).2
    · intro q hq
      simp only [shahada, hh, muqaddimatOf, List.mem_cons, List.not_mem_nil, or_false] at hq
      rcases hq with rfl | rfl <;> rfl
  | P ism =>
    have hb : (shahada src m).marbut = true := by
      simp only [Nizam.Shahada.Naqla.marbut, shahada, hv, hh, qaidaOf, Bool.true_and, Bool.not_eq_true']
      decide
    simp only [Nizam.Shahada.hukm, hb, ite_true, natijaOf]
    simp [Nizam.Shahada.hukmMarbut, Nizam.Shahada.awwalNaqid, Nizam.Shahada.naqisa, Nizam.Shahada.naqisaMadkhal, shahada,
      hh, muqaddimatOf, Muqaddima.halFiil, Nizam.Shahada.naqid, madkhalSalim]
  | F ism =>
    have hb : (shahada src m).marbut = true := by
      simp only [Nizam.Shahada.Naqla.marbut, shahada, hv, hh, qaidaOf, Bool.true_and, Bool.not_eq_true']
      decide
    simp only [Nizam.Shahada.hukm, hb, ite_true, natijaOf]
    simp [Nizam.Shahada.hukmMarbut, Nizam.Shahada.awwalNaqid, shahada, hh, muqaddimatOf, Muqaddima.halFiil,
      Nizam.Shahada.naqid]

/-! ## ٧. العقدُ مطبَّقًا على قواعد الترخيص الأربع -/

/-- **القاعدة بمعناها:** المدخلُ صحيحٌ إذا كان موضعُه صالحًا وذرّاتُه المقطعَ، وكان المقطعُ بسياقه مقطعَ ذلك الموضع في تحصيل المصدر
    (مطابقةُ المصدر والمقام)؛ والمقدّمتان صحّةُ المدخل (لا سببَ فساد) وانطباقُ الصنف؛ والمخرجُ صحيحٌ بمعنى الصنف (`SahihL`). -/
def qaida (s : Sinf) : Nizam.Shahada.Qaida (Siyaq × List Char) (List Khaliya) where
  hawiyya := ⟨ismSinf s, 1⟩
  asma := [(madkhalSalim, .madkhal), (ismSinf s, .shart)]
  tatbiq x := khalayaOf (tasnif x.1 x.2)
  sahihMadkhal src sp x := validSpan src sp = true ∧ spanAtoms src sp = x.2 ∧
    ∃ m ∈ tahsil src.atoms, m.a = sp.start ∧ m.b = sp.stop ∧ m.nass = x.2 ∧ m.siyaq = x.1
  sadiq ism x := (ism = madkhalSalim → ∀ e, tasnif x.1 x.2 ≠ .F e) ∧
    (ism = ismSinf s → ∃ ks, tasnif x.1 x.2 = .L s ks)
  sahihMakhraj src sp x y := spanAtoms src sp = x.2 ∧ SahihL s x.2 y
  aqd := by
    intro src sp x hin hs _
    obtain ⟨_, hat, m, hm, _, _, hn, _⟩ := hin
    obtain ⟨ks, hks⟩ := (hs (ismSinf s, .shart) (by simp) (by simp)).2 rfl
    refine ⟨hat, ?_⟩
    simp only [hks, khalayaOf]
    have hal := qatta_alamat src.atoms _ (mem_tahsil_qatta hm)
    rw [hn] at hal
    exact tasnif_salim _ _ _ _ hal hks

/-- **الشواهدُ التنفيذيّة للعقد:** كلُّ مقطعٍ مرخَّصٍ في تحصيل المصدر شهادتُه أمينةٌ لقاعدة صنفه، صادقةُ الشواهد، صحيحةُ المدخل؛
    فمخرجُها صحيحٌ بعقد القاعدة — من `Nizam.Shahada.shahada_salima` نفسِها. -/
theorem shahada_tahsil_salima (src : Source Char) (m : Maqta) (hm : m ∈ tahsil src.atoms) (s : Sinf)
    (ks : List Khaliya) (hh : m.hukm = .L s ks) :
    (qaida s).sahihMakhraj src (mawdi src m) (m.siyaq, m.nass) (shahada src m).makhraj := by
  have hk := tahsil_hukm src.atoms m hm
  have ⟨hv, hat⟩ := mawdi_sahih src m hm
  have hmur : Nizam.Shahada.hukm (shahada src m) = .murakhkhas := by
    rw [shahada_hukm src m hm, hh]
    rfl
  have hne := ismSinf_ne s
  refine Nizam.Shahada.shahada_salima (qaida s) (shahada src m) ?_ ?_ ?_ hmur
  · refine ⟨by simp [shahada, hh, qaidaOf, qaida], ?_, ?_⟩
    · show khalayaOf m.hukm = khalayaOf (tasnif m.siyaq m.nass)
      rw [← hk]
    · simp [shahada, qaida, hh, muqaddimatOf]
  · intro q hq
    simp only [shahada, hh, muqaddimatOf, List.mem_cons, List.not_mem_nil, or_false] at hq
    rcases hq with rfl | rfl
    · refine ⟨fun _ => ⟨fun _ e h2 => ?_, fun e => absurd e.symm hne.1⟩, fun e => by cases e⟩
      show False
      change tasnif m.siyaq m.nass = _ at h2
      rw [← hk, hh] at h2; cases h2
    · refine ⟨fun _ => ⟨fun e => absurd e hne.1, fun _ => ⟨ks, ?_⟩⟩, fun e => by cases e⟩
      show tasnif m.siyaq m.nass = _
      rw [← hk, hh]
  · exact ⟨hv, hat, m, hm, rfl, rfl, rfl, rfl⟩

/-! ## ٨. محاذاةُ الخلايا، والكلمات -/

/-- كلُّ خليّةٍ مرخَّصةٍ مقرونةً بموضع مقطعها بنقاط الرمز. -/
def khalayaMuhadhat (t : List Char) : List (Khaliya × Nat × Nat) :=
  (tahsil t).flatMap fun m => (khalayaOf m.hukm).map fun k => (k, m.a, m.b)

/-- **محاذاةُ الخلايا:** كلُّ خليّةٍ في تيّار الخلايا لها موضعُ مقطعٍ في النصّ، ذرّاتُه المقطع، ورأسُه حرفُ حاملها (والمقعدُ همزة). -/
theorem khalaya_muhadhat (t : List Char) :
    ∀ x ∈ khalayaMuhadhat t, ∃ m ∈ tahsil t, m.a = x.2.1 ∧ m.b = x.2.2 ∧
      (t.drop m.a).take (m.b - m.a) = m.nass ∧ ∃ r ∈ m.nass.head?, harf x.1.hamil = raddHarf r := by
  intro x hx
  simp only [khalayaMuhadhat, List.mem_flatMap, List.mem_map] at hx
  obtain ⟨m, hm, k, hk, rfl⟩ := hx
  refine ⟨m, hm, rfl, rfl, (tahsil_muhadha t m hm).1, ?_⟩
  cases hh : m.hukm with
  | P _ => rw [hh] at hk; cases hk
  | F _ => rw [hh] at hk; cases hk
  | L s ks =>
    rw [hh] at hk
    have hs := tahsil_salim t m hm s ks hh
    have hkm : fakkKhaliya k ∈ ks.map fakkKhaliya := List.mem_map_of_mem hk
    cases s with
    | fasil => rw [hs.2] at hk; cases hk
    | tatwil => rw [hs.2] at hk; cases hk
    | harfMadd =>
      obtain ⟨r, hr, hmem, hmap⟩ := hs
      refine ⟨r, by simp [hr], ?_⟩
      rw [hmap, List.mem_singleton] at hkm
      have hk1 : harf k.hamil = r := congrArg Prod.fst hkm
      have hrad : raddHarf r = r := by
        unfold raddHarf
        rcases hmem with h | h | h <;> subst h <;> decide
      rw [hk1, hrad]
    | harfHaraka =>
      obtain ⟨r, ms, st, hr, _, _, _, hmap⟩ := hs
      refine ⟨r, by simp [hr], ?_⟩
      rw [hmap] at hkm
      have : (fakkKhaliya k).1 = raddHarf r := by
        simp only [List.mem_append, List.mem_singleton] at hkm
        rcases hkm with hkm | hkm
        · split at hkm
          · simp only [List.mem_singleton] at hkm
            rw [hkm]
          · cases hkm
        · rw [hkm]
      exact this

structure Kalima where
  a : Nat
  b : Nat
  murakhkhasa : Bool
  khalaya : List Khaliya
  deriving Repr

def mL : Hukm → Bool
  | .L _ _ => true
  | _ => false

def kalimaMin (ms : List Maqta) : Option Kalima :=
  match ms.head?, ms.getLast? with
  | some f, some l =>
    let ks := ms.flatMap (fun m => khalayaOf m.hukm)
    some ⟨f.a, l.b, ms.all (fun m => mL m.hukm) && !ks.isEmpty, ks⟩
  | _, _ => none

/-- الكلماتُ: أطولُ المتتاليات من المقاطع التي ليس رأسُها الفراغ. -/
def kalimat (t : List Char) : List Kalima :=
  let gs := (tahsil t).foldl (fun (acc : List (List Maqta)) m =>
    if fasil m.nass then [] :: acc
    else match acc with
      | g :: gs => (g ++ [m]) :: gs
      | [] => [[m]]) [[]]
  gs.reverse.filterMap kalimaMin

/-! ## ٩. شواهد -/

/-- «كَتَبَ»: ثلاثةُ مقاطع مرخَّصة متّصلة، وخلاياها 32 و72 و104 بترميز المالك. -/
theorem shahid_kataba :
    (tahsil "كَتَبَ".toList).map (fun m => (m.a, m.b, m.hukm)) =
      [(0, 2, .L .harfHaraka [⟨8, 0⟩]), (2, 4, .L .harfHaraka [⟨18, 0⟩]), (4, 6, .L .harfHaraka [⟨26, 0⟩])] ∧
    ((tahsil "كَتَبَ".toList).flatMap (fun m => khalayaOf m.hukm)).map Dal.n = [32, 72, 104] := by
  decide

/-- «ٱلشَّمْسُ»: همزةُ الوصل ولامُ التعريف المدغمة معلَّقتان باسميهما، والباقي مرخَّص، ولا شيءَ يُسقط. -/
theorem shahid_shams :
    (tahsil "ٱلشَّمْسُ".toList).map (fun m => m.hukm) =
      [.P "قاعدة همزة الوصل", .P "قاعدة لام التعريف المدغمة", .L .harfHaraka [⟨10, 3⟩, ⟨10, 0⟩],
       .L .harfHaraka [⟨27, 3⟩], .L .harfHaraka [⟨20, 1⟩]] := by
  decide

/-- «كِتَابًا» و«ذَهَبُوا»: التنوينُ وألفُه وألفُ الجماعة معلَّقةٌ بأسمائها؛ وحرفٌ بلا حركةٍ وسطَ الكلمة مدخلٌ فاسد. -/
theorem shahid_muallaq :
    ((tahsil "كِتَابًا".toList).map (fun m => m.hukm)).drop 3 = [.P "قاعدة التنوين", .P "قاعدة ألف التنوين"] ∧
    ((tahsil "ذَهَبُوا".toList).map (fun m => m.hukm)).drop 3 = [.L .harfMadd [⟨28, 3⟩], .P "قاعدة ألف الجماعة"] ∧
    ((tahsil "كتَبَ".toList).map (fun m => m.hukm)).head? = some (.F "حرف بلا حركة في غير آخر الكلمة") := by
  decide

end Dal.Tahsil
