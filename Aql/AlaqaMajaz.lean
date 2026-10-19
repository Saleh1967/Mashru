/-
  Aql/AlaqaMajaz.lean — شرط شرعيّة العلاقة التي يستهلكها haml (QawaninDalala.lean) لإصدار .majaz:
  شاهدٌ من واقعٍ مختوم باسمها، لا Bool مجرّد. ومخالفةُ معلومةٍ مقيسةٍ (رياضية أو فيزيائية، نوعها
  maalumatSabiqa لا waqiMakhtum) لا تحقّق هذا الشرط أصلًا.

  السند: فجوةٌ أقرّها المالك صريحًا (2026-10-19) بعد نقدي مقترح «مصفوفة المحاذاة الارتكازية»
  (رضا-النبهاني) الذي حاول حقن مخالفة حقائق رياضية/فيزيائية بوّابةً سابقةً تُسقط رتبة الوضع، وبعد
  نقاشٍ في أساس ثلاث ملكاتٍ معرفيّة ميّز النبهاني بينها بثلاثة نصوص (الوضع بالنقل، ج3 729؛ الرياضيّ
  بالضرورة/عالميّته، ج1 789 و865؛ الحقيقة الخارجية بالحسّ المشهود، Aqliyya/Maratib/Hawass). سأل
  المالك عن سند عبارة «مدركه الحسّ والضرورة»، فقلتُ لا أجدها بالحرف؛ فأجاب: «لا يوجد عندي لكنّها
  فجوةٌ في النظام نحتاج علاجًا لها». هذا الملفّ علاجُها.

  haml مبرهنةٌ بالفعل ألّا تصدر .majaz قبل استنفاد الحقائق الثلاث (QawaninDalala.la_majaz_qabl_istinfad)،
  وبعد الاستنفاد التامّ (الثلاث .la) تتبع alaqa : Bool وحده (majaz_bad_istinfad). فالثغرة ليست في
  منطق haml؛ الثغرة أنّ alaqa عارٍ من اسمٍ أو شاهد — فلو حُسب خارج haml من مطابقةٍ آليّةٍ (كجدول
  مقارنةٍ ثابت) لا من مودَعٍ مختوم، لم يمنعه من الدخول شيء. هذا الملفّ يُسمّي الشرط الناقص (AlaqaMajaz،
  شاهدٌ لا Bool) ويبرهن أنّ علاقةً شاهدُها من مودَعٍ غير مختوم (نوعه maalumatSabiqa، وهو نوعُ جداول
  نظام الفيزياء/الرياضيات في Jamad.lean نفسِها: علميٌّ يُقيَّد مقيسًا لا شاهدَ واقع) لا تحقّق الشرط،
  فلا تُنتج .majaz عبر haml في أيّ تشكيلٍ للحقائق الثلاث.

  البناء يُعيد نسق Maratib.la_mafhum_bila_waqi وHawass.shahid_ghayr_mudaa_la_yuthir على alaqa بدل
  الشاهد الحسّيّ. لا جدول خارجيّ لهذه القطعة ولا مرآة بايثون، كـ SababShartMani.lean. بلا sorry ولا
  axiom ولا native_decide.
-/
import Aql.QawaninDalala
import Aql.Maratib

namespace AlaqaMajaz
open QawaninDalala Maratib

/-- علاقةٌ مجازيّةٌ مسمّاة (من علاقات ج3: سببيّة بأقسامها، مسببيّة، مشابهة...): اسمها، وشاهدُ واقعها —
    لا Bool مجرّد. -/
structure AlaqaMajaz where
  ism : String
  shahid : ShahidWaqi
deriving DecidableEq, Repr

/-- شرعيّةُ العلاقة: شاهدُها من مودَعٍ مسجَّلٍ نوعُه «واقعٌ مختوم» بعينه (الدستور م12؛ نسق
    Maratib.shuhudMutabara). -/
def mashrua (sijill : List (String × Idaa.Naw)) (a : AlaqaMajaz) : Bool :=
  sijill.any fun b => a.shahid.basma.startsWith b.1 && b.2 == .waqiMakhtum

/-- إسقاطُها إلى Bool ليُغذَّى به haml.alaqa — فقط إن شُرعت. -/
def alaqaOf (sijill : List (String × Idaa.Naw)) (a : AlaqaMajaz) : Bool :=
  mashrua sijill a

/-! ## ١. شاهدٌ من مودَعٍ غير «واقعٍ مختوم» لا يشرّع العلاقة -/

/-- **المعلومات السابقة لا تُشرِّع**: شاهدٌ من مودَعٍ كلُّه من نوعٍ آخر غير waqiMakhtum (كجداول نظام
    الفيزياء/الرياضيات — علميٌّ يُقيَّد مقيسًا، لا شاهدَ واقعٍ مختوم) لا يحقّق mashrua، أيًّا كانت
    العلاقة. -/
theorem mashrua_bila_waqi_makhtum
    (sijill : List (String × Idaa.Naw)) (hs : ∀ b ∈ sijill, b.2 ≠ .waqiMakhtum)
    (a : AlaqaMajaz) : mashrua sijill a = false := by
  simp only [mashrua, Bool.not_eq_true, List.any_eq_false]
  intro b hb
  have := hs b hb
  cases h : b.2 <;> simp_all

/-! ## ٢. فلا تنتج .majaz عبر haml — بعد الاستنفاد التامّ -/

/-- بعد استنفاد الحقائق الثلاث (الثلاث .la): علاقةٌ غيرُ مشرَّعةٍ تُنتج لا حكم، لا مجازًا (مركَّبةٌ
    من (١) ومن majaz_bad_istinfad المستوردة بلا تعديل). -/
theorem alaqaOf_ghayr_mashrua_la_hukm
    (sijill : List (String × Idaa.Naw)) (hs : ∀ b ∈ sijill, b.2 ≠ .waqiMakhtum)
    (a : AlaqaMajaz) (sabq : Bool) (qarina : Option NawHaqiqa) :
    haml .la .la .la sabq qarina (alaqaOf sijill a) = .laHukm := by
  have hfalse : alaqaOf sijill a = false := mashrua_bila_waqi_makhtum sijill hs a
  rw [hfalse]
  exact (majaz_bad_istinfad sabq qarina).2

/-! ## ٣. التجميع: في أيّ تشكيلٍ للحقائق الثلاث -/

/-- **النتيجة الجامعة**: علاقةٌ غيرُ مشرَّعةٍ (بلا شاهد واقعٍ مختوم) لا تُنتج .majaz عبر haml، أيًّا
    كانت شهادات الحقائق الثلاث — إمّا حقيقةٌ (إن شهدت واحدةٌ، la_majaz_qabl_istinfad المستوردة)، أو
    لا حكم (الباقي: ghayr_yuqif المستوردة، أو (٢) إن شهدت الثلاث كلّها بالسلب التامّ). -/
theorem alaqa_ghayr_mashrua_la_tunshi_majaz
    (sijill : List (String × Idaa.Naw)) (hs : ∀ b ∈ sijill, b.2 ≠ .waqiMakhtum)
    (a : AlaqaMajaz) (s1 s2 s3 : Shahada) (sabq : Bool) (qarina : Option NawHaqiqa) :
    haml s1 s2 s3 sabq qarina (alaqaOf sijill a) ≠ .majaz := by
  by_cases h : s1 = .naam ∨ s2 = .naam ∨ s3 = .naam
  · exact la_majaz_qabl_istinfad s1 s2 s3 sabq qarina (alaqaOf sijill a) h
  · by_cases hg : s1 = .ghayr ∨ s2 = .ghayr ∨ s3 = .ghayr
    · rw [ghayr_yuqif s1 s2 s3 sabq qarina (alaqaOf sijill a) h hg]
      decide
    · have e1 : s1 = .la := by rcases s1 with _ | _ | _ <;> simp_all
      have e2 : s2 = .la := by rcases s2 with _ | _ | _ <;> simp_all
      have e3 : s3 = .la := by rcases s3 with _ | _ | _ <;> simp_all
      subst e1; subst e2; subst e3
      rw [alaqaOf_ghayr_mashrua_la_hukm sijill hs a sabq qarina]
      decide

end AlaqaMajaz
