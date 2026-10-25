/-
  Madlul/JadwalLuzumNaql.lean — النقلُ لصفوف جدول اللزوم: كلُّ صفٍّ قضيّةٌ منقولة (`Naql.Naql` من `Aql/Naql.lean`).

  قولُ المالك في الجلسة (2026-10-25، 23:07 بتوقيت عمّان من بيانات الرسالة):
  «موافق على إضافة المبرهنات الثلاث وفقlean واربط مع النقل وبعدها اكمل الربط وفق افضل الممارسات ليكون كل المشروع مترابط ومتناسق ومتكامل وفق افضل الممارسات»
  وصدرُ رسالته نصُّ سؤال البنّاء ألصقه:
  "build the two gaps as a separate PR: adding the three theorems to Audit.lean, and linking Naql to the dependency-table rows?"
  والثلاثُ هي التي سمّاها جوابُ البنّاء قبل السؤال. والفجوةُ معلنةٌ في رأس `Aql/Naql.lean`: أعمدةُ القائل والدرجة ونوع الحقيقة أُجِّلت.

  السند (ج3، المودَع a2.txt):
  * س729: «طريق معرفة اللغة العربية هي النقل المتواتر وخبر الآحاد.» والآحادُ فيه:
    «كالألفاظ المروية المعنعنة عن الأدباء الباحثين عن اللغة، كالخليل، والأصمعي، ونحوهما.»
    والحدُّ فيه «حتى القرن الرابع الهجري»، وفي س868 «قبل القرن الرابع الهجري».
  * س892: «إذا احتمل النقل من الحقيقة اللغوية إلى الشرعية أو العرفية، أو عدم النقل، فالأصل عدم النقل».

  التعيين (تعيينُ البنّاء، معلن):
  * القائلُ المعجمُ نفسُه باسمه في `mudaat/sijill.json`: نسبةٌ قائمة بالبروتوكول خ٣ كما في `Aql/Naql.lean` (ووثيقةُ البروتوكول ليست في
    المستودع). ولا يُقرأ من السطر قائلٌ أدنى، كقولِ اللسان في سطر صفٍّ قائم: «وقال اللحياني» (س24031) — ذلك حكمٌ على نصّ المصدر لم يُبنَ.
  * الدرجةُ للزوج المرتَّب (جذرُ المادّة، الجذرُ الآخر): `Naql.binaDaraja` على عدد المعجمين اللذين في الجدول صفٌّ لهما بهذا الزوج
    (البروتوكول خ٤ كما في `Aql/Naql.lean`). والاتّفاقُ اتّفاقُ الزوج لا نوعِ القضيّة: في فهم ← علم اللسانُ ترادفٌ (س236711) والمقاييسُ
    أصلٌ (س32736). واستقلالُ المعجمين لم يُفحص؛ وسطرُ المقاييس نفسُه يروي: «كذا يقولون أهل اللغة». وبلا صفٍّ للزوج لا درجة (`none`).
  * الحدُّ الزمانيّ بقراءتين، والقرارُ للمالك (`QiraaHadd`): لعصر القائل الذي في الحقل — وهو المعجم — كما يقول `NawNaql.mustahdathBadAlHadd`
    («قائله بعد الحدّ الزمانيّ»)، بسنة وفاة صاحبه في رأس المودَع (`011.AuthorDIED`: اللسان 711، المقاييس 395)؛ أو لعصر المنقول عنه،
    والمعجمُ ناقلٌ بنصّ س729، ولا تاريخَ للمنقول عنه في الصفّ فلا حكم. وسنةُ الوفاة مقياسًا لعصر القائل تعيين.
  * نوعُ الحقيقة: `mustahdathBadAlHadd` حيث أثبت الحدُّ الخروج، وإلّا `wadLughawi`. وس892 لا ينفي إلّا الشرعيّة والعرفيّة؛ ونفيُ المجاز
    والمعرَّب والصياغة تعيينٌ بلا سند — والمستخرِجُ لا يُخرج علامةَ النقل عمودًا، وإن كان `ASL_NAFY` يُسقط من أصول ابن فارس ما فيه
    «فارسي» أو «معرب» (`shabaka/jadwal_luzum.py`).
  * والقطعةُ تُسند إلى كلّ صفٍّ حقولًا بقاعدةٍ ثابتة من معجمه وجذريه، لا من قراءة لفظه؛ فعددتُها قطعةَ بنيةٍ خارج الضابط المجمَّد
    (البند 2أ في CLAUDE.md). وهذه قراءةُ البنّاء: المنهجُ يسمّي من قطع البنية «الفاحص، والمخزن، والأدوات» وحدها.

  المبرهنات:
  (تكميمًا لا تصنيفًا؛ وتصنيفُها بالمعيار الموحَّد في CLAUDE.md)
  * لكلّ جدول: `la_mutawatir`، و`yashhad_saff`، و`mutadhafir_iff` (متعاضدٌ إذا وفقط إذا شهد المعجمان)، و`la_daraja_bila_saff`، و`daraja_jisr` (درجةُ
    `naqlOf` لصفٍّ في الجدول هي درجةُ زوجه)، و`yasluh_iff` (يصلح أصلًا لغويًّا إلّا صفُّ اللسان في قراءة عصر القائل)، و`naw_hadd`.
  * لهذا الجدول: `iltizam_jadwal_yasluh` (كلُّ التزامٍ مرخَّصٍ فيه وراءه صفُّ تعليلٍ يصلح نقلُه في القراءتين).
  * على الشاهد: `shahid_daraja`، `shahid_qiraatan`، `shahid_luzum_maqayis`، `shahid_fahm_juz_lisan`.
  بلا sorry ولا axiom ولا native_decide.
-/
import Madlul.JadwalLuzum
import Aql.Naql

namespace JadwalLuzum
open Qaida QawaninDalala

/-! ## ١. القائلُ والدرجة -/

/-- القائلُ: المعجمُ باسمه في سجلّ المودَعات. -/
def qailOf : Mujam → String
  | .lisan => "لسان العرب"
  | .maqayis => "مقاييس اللغة"

def kullMujam : List Mujam := [.lisan, .maqayis]

/-- يشهد المعجمُ للزوج (a ← b): في الجدول صفٌّ منه جذرُ مادّته a وجذرُه الآخر b. -/
def yashhad (T : List Saff) (a b : String) (m : Mujam) : Bool :=
  T.any fun r => r.mujam == m && r.a == a && r.b == b

def mujamat (T : List Saff) (a b : String) : List Mujam := kullMujam.filter (yashhad T a b)

/-- درجةُ نقل الزوج: لا درجةَ بلا شاهد، وإلّا `binaDaraja` على عدد المعجمين. -/
def darajaSila (T : List Saff) (a b : String) : Option Naql.Daraja :=
  match (mujamat T a b).length with
  | 0 => none
  | n => some (Naql.binaDaraja n)

/-! ## ٢. الحدُّ الزمانيّ بقراءتيه، ونوعُ الحقيقة -/

/-- سنةُ وفاة صاحب المعجم في رأس المودَع المختوم (`011.AuthorDIED`)؛ يطابقها `test_luzum.py` على المودَع. -/
def wafat : Mujam → Nat
  | .lisan => 711
  | .maqayis => 395

/-- الحدُّ من سنةٍ هجريّة: داخلٌ قبل القرن الرابع، وخارجٌ بعده، و«لا حكم» فيه — بين س729 («حتى») وس868 («قبل»). -/
def haddMinSana (s : Nat) : Option Bool :=
  if s ≤ 300 then some true else if s > 400 then some false else none

/-- قراءتا حقل الحدّ: لعصر القائل الذي في الحقل، أو لعصر المنقول عنه. والقرارُ للمالك. -/
inductive QiraaHadd | asrQail | asrManqul
  deriving DecidableEq, Repr

def haddOf : QiraaHadd → Mujam → Option Bool
  | .asrQail, m => haddMinSana (wafat m)
  | .asrManqul, _ => none

/-- نوعُ الحقيقة: مستحدَثٌ بعد الحدّ حيث أثبت الحدُّ الخروج، وإلّا قاعدةُ الأصل. -/
def nawOf (q : QiraaHadd) (m : Mujam) : Naql.NawNaql :=
  if haddOf q m = some false then .mustahdathBadAlHadd else .wadLughawi

/-- النقلُ لصفٍّ في قراءةٍ للحدّ: قائلُه معجمُه، ودرجتُه بعدد معجمَي زوجه، وحدُّه ونوعُه بالقراءة. -/
def naqlOf (q : QiraaHadd) (T : List Saff) (r : Saff) : Naql.Naql :=
  ⟨some (qailOf r.mujam), Naql.binaDaraja (mujamat T r.a r.b).length, haddOf q r.mujam, nawOf q r.mujam⟩

/-! ## ٣. المبرهن لكلّ جدول -/

/-- الدرجةُ لا تكون متواترًا لأيّ جدولٍ وزوج. -/
theorem la_mutawatir (T : List Saff) (a b : String) : darajaSila T a b ≠ some .mutawatir := by
  unfold darajaSila
  split
  · simp
  · intro h
    exact Naql.la_mutawatir_min_al_add _ (Option.some.inj h)

/-- متعاضدٌ إذا وفقط إذا شهد المعجمان كلاهما للزوج. -/
theorem mutadhafir_iff (T : List Saff) (a b : String) :
    darajaSila T a b = some .mutadhafir ↔ yashhad T a b .lisan = true ∧ yashhad T a b .maqayis = true := by
  cases h1 : yashhad T a b .lisan <;> cases h2 : yashhad T a b .maqayis <;>
    simp [darajaSila, mujamat, kullMujam, List.filter, h1, h2, Naql.binaDaraja]

/-- يشهد معجمُ كلِّ صفٍّ لزوجه. -/
theorem yashhad_saff (T : List Saff) (r : Saff) (hr : r ∈ T) : yashhad T r.a r.b r.mujam = true := by
  simp only [yashhad, List.any_eq_true, Bool.and_eq_true, beq_iff_eq]
  exact ⟨r, hr, ⟨rfl, rfl⟩, rfl⟩

/-- ولا درجةَ إلّا بصفٍّ للزوج في الجدول. -/
theorem la_daraja_bila_saff (T : List Saff) (a b : String) :
    darajaSila T a b = none ↔ ¬ ∃ r ∈ T, r.a = a ∧ r.b = b := by
  constructor
  · intro h ⟨r, hr, ha, hb⟩
    have hy := yashhad_saff T r hr
    rw [ha, hb] at hy
    cases hm : r.mujam <;> rw [hm] at hy <;>
      cases h2 : yashhad T a b .lisan <;> cases h3 : yashhad T a b .maqayis <;>
      simp_all [darajaSila, mujamat, kullMujam, List.filter]
  · intro h
    have h1 : yashhad T a b .lisan = false := by
      simp only [yashhad, List.any_eq_false]
      intro r hr hc
      simp only [Bool.and_eq_true, beq_iff_eq] at hc
      exact h ⟨r, hr, hc.1.2, hc.2⟩
    have h2 : yashhad T a b .maqayis = false := by
      simp only [yashhad, List.any_eq_false]
      intro r hr hc
      simp only [Bool.and_eq_true, beq_iff_eq] at hc
      exact h ⟨r, hr, hc.1.2, hc.2⟩
    simp [darajaSila, mujamat, kullMujam, List.filter, h1, h2]

/-- درجةُ `naqlOf` لصفٍّ في الجدول هي درجةُ زوجه بعينها (فلا حسابان للدرجة). -/
theorem daraja_jisr (q : QiraaHadd) (T : List Saff) (r : Saff) (hr : r ∈ T) :
    darajaSila T r.a r.b = some (naqlOf q T r).daraja := by
  have hy := yashhad_saff T r hr
  cases hm : r.mujam <;> rw [hm] at hy <;>
    cases h2 : yashhad T r.a r.b .lisan <;> cases h3 : yashhad T r.a r.b .maqayis <;>
    simp_all [darajaSila, naqlOf, mujamat, kullMujam, List.filter]

/-- يصلح نقلُ الصفّ أصلًا لغويًّا (`Naql.yasluhuAslanLughawiyyan`) إلّا صفَّ اللسان في قراءة عصر القائل. -/
theorem yasluh_iff (q : QiraaHadd) (T : List Saff) (r : Saff) :
    Naql.yasluhuAslanLughawiyyan (naqlOf q T r) = true ↔ ¬ (q = .asrQail ∧ r.mujam = .lisan) := by
  cases q <;> cases hm : r.mujam <;>
    simp [Naql.yasluhuAslanLughawiyyan, naqlOf, haddOf, haddMinSana, wafat, hm]

/-- والنوعُ مستحدَثٌ بعد الحدّ إذا وفقط إذا أثبت الحدُّ الخروج. -/
theorem naw_hadd (q : QiraaHadd) (T : List Saff) (r : Saff) :
    (naqlOf q T r).naw = .mustahdathBadAlHadd ↔ (naqlOf q T r).fiAlHadd = some false := by
  simp only [naqlOf, nawOf]
  split <;> simp_all

/-! ## ٤. لهذا الجدول، وعلى الشاهد -/

/-- صفوفُ التعليل في الجدول كلُّها من المقاييس (س26425 وحده). -/
theorem shahid_luzum_maqayis :
    (jadwal.filter fun r => r.naw == .luzum).map (fun r => (r.mujam, r.satr)) = [(.maqayis, 26425)] := by decide

/-- كلُّ التزامٍ مرخَّصٍ في قاعدة هذا الجدول وراءه صفُّ تعليلٍ يصلح نقلُه أصلًا لغويًّا في القراءتين. -/
theorem iltizam_jadwal_yasluh {l k : Nat}
    (h : Murakhkhas (qaidaOf jadwal) (fun p => aslB jadwal p = true) (.iltizam l k)) :
    ∃ r ∈ jadwal, r.naw = .luzum ∧ ∀ q, Naql.yasluhuAslanLughawiyyan (naqlOf q jadwal r) = true := by
  obtain ⟨r, hr, hn⟩ := iltizam_min_taalil jadwal h
  have hall : ∀ r ∈ jadwal, r.naw = .luzum → r.mujam = .maqayis := by decide
  refine ⟨r, hr, hn, fun q => (yasluh_iff q jadwal r).2 ?_⟩
  rw [hall r hr hn]
  simp

/-- درجاتُ الأزواج المرتَّبة بين جذور الشبكة في الجدول، وهي سبعةٌ لا غير: فهم ← علم متعاضدة (اللسان س236711 والمقاييس س32736)،
    والستّةُ الباقية آحاد؛ والعكسُ علم ← فهم بلا درجة. -/
theorem shahid_daraja :
    let sh := ["كتب", "درس", "قلم", "علم", "فهم", "طلب", "عقل"]
    ((jadwal.filter fun r => sh.contains r.a && sh.contains r.b).map fun r => (r.a, r.b)).eraseDups =
      [("كتب", "علم"), ("درس", "كتب"), ("عقل", "فهم"), ("فهم", "علم"), ("فهم", "عقل"), ("قلم", "كتب"), ("عقل", "طلب")] ∧
    darajaSila jadwal "فهم" "علم" = some .mutadhafir ∧
    [("كتب", "علم"), ("درس", "كتب"), ("عقل", "فهم"), ("فهم", "عقل"), ("قلم", "كتب"), ("عقل", "طلب")].all
      (fun p => darajaSila jadwal p.1 p.2 == some .ahad) = true ∧
    darajaSila jadwal "علم" "فهم" = none := by decide

/-- القراءتان على الجدول: في عصر القائل يصلح نقلُ صفوف المقاييس الثلاثةَ عشرَ وحدها، وفي عصر المنقول عنه يصلح الثلاثون. -/
theorem shahid_qiraatan :
    (jadwal.filter fun r => Naql.yasluhuAslanLughawiyyan (naqlOf .asrQail jadwal r)).length = 13 ∧
    (jadwal.filter fun r => Naql.yasluhuAslanLughawiyyan (naqlOf .asrQail jadwal r)).all (·.mujam == .maqayis) = true ∧
    (jadwal.filter fun r => Naql.yasluhuAslanLughawiyyan (naqlOf .asrManqul jadwal r)).length = 30 := by decide

/-- وأجزاءُ «الفهم» في الجدول (عرف، قلب) من اللسان وحده (س236711)؛ فلا يصلح نقلُها في قراءة عصر القائل. -/
theorem shahid_fahm_juz_lisan :
    (jadwal.filter fun r => r.a == "فهم" && r.naw == .juz).map (fun r => (r.mujam, r.b, r.satr)) =
      [(.lisan, "عرف", 236711), (.lisan, "قلب", 236711)] ∧
    (jadwal.filter fun r => r.a == "فهم" && r.naw == .juz).all
      (fun r => !Naql.yasluhuAslanLughawiyyan (naqlOf .asrQail jadwal r)) = true := by decide

end JadwalLuzum
