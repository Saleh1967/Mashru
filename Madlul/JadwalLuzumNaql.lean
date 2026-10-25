/-
  Madlul/JadwalLuzumNaql.lean — النقلُ لصفوف جدول اللزوم: كلُّ صفٍّ قضيّةٌ منقولة (`Aql/Naql.lean`) بقائلها ودرجتها.

  قولُ المالك (2026-10-25، 23:07 بتوقيت عمّان)، جوابًا عن سؤال البنّاء: «موافق على إضافة المبرهنات الثلاث وفقlean واربط مع
  النقل وبعدها اكمل الربط وفق افضل الممارسات ليكون كل المشروع مترابط ومتناسق ومتكامل وفق افضل الممارسات».
  والفجوةُ معلنةٌ في رأس `Aql/Naql.lean`: «أعمدةُ المستخرِج (القائل/الدرجة/نوع الحقيقة …) أُجِّلت إلى مهمّةٍ تالية».

  السند (ج3، المودَع a2.txt):
  * س729: «طريق معرفة اللغة العربية هي النقل المتواتر وخبر الآحاد.» — فكلُّ أصلٍ يودعه الجدول نقلٌ له قائلٌ ودرجة.
  * س737: «وهذا اللزوم شرط وليس بموجب، يعني أن اللزوم بمجرده ليس هو السبب في حصول دلالة الالتزام، بل السبب هو إطلاق اللفظ، واللزوم شرط.»
  * س892: «فالأصل عدم النقل» — قاعدةُ نوع الحقيقة حيث لا علامة.

  التعيين (تعيينُ البنّاء، معلن):
  * القائلُ المعجمُ نفسُه باسمه في `mudaat/sijill.json` («لسان العرب»، «مقاييس اللغة»): نسبةٌ قائمة (البروتوكول خ٣ كما في
    `Aql/Naql.lean`). ولا يُقرأ من السطر قائلٌ أدنى (كـ«قال ابن الأعرابي»): ذلك حكمٌ على نصّ المصدر لم يُبنَ.
  * الدرجةُ للزوج المرتَّب (جذرُ المادّة، الجذرُ الآخر): `Naql.binaDaraja` على عدد المعجمين اللذين في الجدول صفٌّ لهما بهذا
    الزوج (البروتوكول خ٤: معجمان مختومان مختلفان فأكثر اتّفقا ← متعاضد). و«الاتّفاق» هنا اتّفاقُ الزوج لا نوعِ القضيّة: في «فهم ←
    علم» اللسانُ ترادفٌ (س236711) والمقاييسُ أصلٌ (س32736). وبلا صفٍّ للزوج لا درجة (`none`): الغيابُ ليس آحادًا.
  * الحدُّ الزمانيّ `none` (لا حكم): الصفُّ لا يحمل تاريخًا.
  * نوعُ الحقيقة `.wadLughawi` بقاعدة الأصل (س892)، لأنّ الصفّ لا يحمل علامةَ نقلٍ — والمستخرِجُ لا يستخرجها. فهو تعيينٌ لا قراءة.
  وهذه قطعةُ بنية: تُسند إلى كلّ صفٍّ حقولًا من حقوله (المعجم، الجذران) ولا تحكم على لفظٍ أو تركيبٍ من المصدر.

  المبرهن لكلّ جدول: كلُّ أصلٍ يودعه الجدول، وكلُّ التزامٍ وتضمّنٍ يُرخَّص به، وراءه صفٌّ نقلُه يصلح أصلًا لغويًّا
  (`asl_min_naql`، `iltizam_min_naql`، `tadammun_min_naql`)؛ والدرجةُ لا تكون متواترًا (`la_mutawatir`)، وتكون متعاضدًا إذا وفقط
  إذا شهد المعجمان (`mutadhafir_iff`)، ولا درجةَ إلّا بصفّ (`la_daraja_bila_saff`). وعلى الشاهد: «فهم ← علم» وحدها متعاضدة.
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

/-- نوعُ الحقيقة بقاعدة الأصل (ج3 س892)؛ تعيينٌ لا قراءة. -/
def nawAsl : Naql.NawNaql := .wadLughawi

/-- النقلُ لصفّ: قائلُه معجمُه، ودرجتُه درجةُ زوجه، ولا حدَّ زمانيًّا له، ونوعُه قاعدةُ الأصل. -/
def naqlOf (T : List Saff) (r : Saff) : Naql.Naql :=
  ⟨some (qailOf r.mujam), Naql.binaDaraja (mujamat T r.a r.b).length, none, nawAsl⟩

/-! ## ٢. المبرهن لكلّ جدول -/

/-- كلُّ صفٍّ نقلُه يصلح أصلًا لغويًّا: له قائلٌ، ولم يثبت خروجُه عن الحدّ. -/
theorem naql_yasluh (T : List Saff) (r : Saff) : Naql.yasluhuAslanLughawiyyan (naqlOf T r) = true :=
  Naql.yasluhu_idha_qail_wa_la_nafy _ none (by simp) _ _

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

/-- ولا درجةَ إلّا بصفٍّ للزوج في الجدول. -/
theorem la_daraja_bila_saff (T : List Saff) (a b : String) :
    darajaSila T a b = none ↔ ¬ ∃ r ∈ T, r.a = a ∧ r.b = b := by
  have hm : ∀ r : Saff, r.mujam = .lisan ∨ r.mujam = .maqayis := fun r => by cases r.mujam <;> simp
  constructor
  · intro h ⟨r, hr, ha, hb⟩
    have hy : yashhad T a b r.mujam = true := by
      simp only [yashhad, List.any_eq_true, Bool.and_eq_true, beq_iff_eq]
      exact ⟨r, hr, ⟨rfl, ha⟩, hb⟩
    rcases hm r with hl | hl <;> rw [hl] at hy <;>
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

/-- كلُّ أصلٍ يودعه الجدول وراءه صفٌّ منه نقلُه يصلح أصلًا لغويًّا، ولزوجه درجة. -/
theorem asl_min_naql (T : List Saff) (p : Qadiyya) (h : aslB T p = true) :
    ∃ r ∈ T, p ∈ aslOf T r ∧ Naql.yasluhuAslanLughawiyyan (naqlOf T r) = true ∧ darajaSila T r.a r.b ≠ none := by
  obtain ⟨r, hr, hp⟩ := (aslB_iff T p).mp h
  exact ⟨r, hr, hp, naql_yasluh T r, fun hn => (la_daraja_bila_saff T r.a r.b).mp hn ⟨r, hr, rfl, rfl⟩⟩

/-- **اللزومُ شرطٌ منقول** (ج3 س737، س729): كلُّ التزامٍ مرخَّصٍ في قاعدة الجدول وراءه صفُّ تعليلٍ نقلُه يصلح أصلًا لغويًّا. -/
theorem iltizam_min_naql (T : List Saff) {l k : Nat}
    (h : Murakhkhas (qaidaOf T) (fun p => aslB T p = true) (.iltizam l k)) :
    ∃ r ∈ T, r.naw = .luzum ∧ Naql.yasluhuAslanLughawiyyan (naqlOf T r) = true := by
  obtain ⟨r, hr, hn⟩ := iltizam_min_taalil T h
  exact ⟨r, hr, hn, naql_yasluh T r⟩

/-- وكلُّ تضمّنٍ مرخَّصٍ وراءه صفُّ حدٍّ أو أصلٍ نقلُه يصلح أصلًا لغويًّا. -/
theorem tadammun_min_naql (T : List Saff) {l j : Nat}
    (h : Murakhkhas (qaidaOf T) (fun p => aslB T p = true) (.tadammun l j)) :
    ∃ r ∈ T, (r.naw = .juz ∨ r.naw = .asl) ∧ Naql.yasluhuAslanLughawiyyan (naqlOf T r) = true := by
  obtain ⟨r, hr, hn⟩ := tadammun_min_juz T h
  exact ⟨r, hr, hn, naql_yasluh T r⟩

/-! ## ٣. على الشاهد -/

/-- درجاتُ صلات الشبكة في الجدول: «فهم ← علم» متعاضدة (اللسان س236711 والمقاييس س32736)، وسائرُها آحاد، والعكسُ «علم ← فهم» بلا درجة. -/
theorem shahid_daraja :
    darajaSila jadwal "فهم" "علم" = some .mutadhafir ∧
    [("كتب", "علم"), ("درس", "كتب"), ("عقل", "فهم"), ("قلم", "كتب"), ("عقل", "طلب")].all
      (fun p => darajaSila jadwal p.1 p.2 == some .ahad) = true ∧
    darajaSila jadwal "علم" "فهم" = none := by decide

/-- والمتعاضدُ من صفوف الجدول الثلاثين صفّان: سطرا «فهم ← علم» في المعجمين. -/
theorem shahid_mutadhafir :
    ((jadwal.filter fun r => (naqlOf jadwal r).daraja == .mutadhafir).map fun r => (r.mujam, r.satr)) =
      [(.lisan, 236711), (.maqayis, 32736)] := by decide

end JadwalLuzum
