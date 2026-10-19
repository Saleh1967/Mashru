/-
  Aql/AlaqaMajaz.lean — شرط شرعيّة العلاقة التي يستهلكها haml (QawaninDalala.lean) لإصدار .majaz:
  شاهدٌ من واقعٍ مختوم باسمها، لا Bool مجرّد؛ ومسجَّلٌ خصّيصًا لهويّة دعواها هي، لا لمجرّد مصدرٍ
  يشاركه غيرُها. ومخالفةُ معلومةٍ مقيسةٍ (رياضية أو فيزيائية، نوعها maalumatSabiqa لا waqiMakhtum)
  لا تحقّق هذا الشرط أصلًا.

  السند (البناء الأصل، 2026-10-19): فجوةٌ أقرّها المالك صريحًا بعد نقدي مقترح «مصفوفة المحاذاة
  الارتكازية» (رضا-النبهاني) الذي حاول حقن مخالفة حقائق رياضية/فيزيائية بوّابةً سابقةً تُسقط رتبة
  الوضع، وبعد نقاشٍ في أساس ثلاث ملكاتٍ معرفيّة ميّز النبهاني بينها بثلاثة نصوص (الوضع بالنقل، ج3
  729؛ الرياضيّ بالضرورة/عالميّته، ج1 789 و865؛ الحقيقة الخارجية بالحسّ المشهود، Aqliyya/Maratib/
  Hawass). سأل المالك عن سند عبارة «مدركه الحسّ والضرورة»، فقلتُ لا أجدها بالحرف؛ فأجاب: «لا يوجد
  عندي لكنّها فجوةٌ في النظام نحتاج علاجًا لها». هذا الملفّ علاجُها.

  haml مبرهنةٌ بالفعل ألّا تصدر .majaz قبل استنفاد الحقائق الثلاث (QawaninDalala.la_majaz_qabl_istinfad)،
  وبعد الاستنفاد التامّ (الثلاث .la) تتبع alaqa : Bool وحده (majaz_bad_istinfad). فالثغرة ليست في
  منطق haml؛ الثغرة أنّ alaqa عارٍ من اسمٍ أو شاهد — فلو حُسب خارج haml من مطابقةٍ آليّةٍ (كجدول
  مقارنةٍ ثابت) لا من مودَعٍ مختوم، لم يمنعه من الدخول شيء. البناء الأصل يُسمّي الشرط الناقص
  (AlaqaMajaz، شاهدٌ لا Bool) ويبرهن أنّ علاقةً شاهدُها من مودَعٍ غير مختوم (نوعه maalumatSabiqa،
  وهو نوعُ جداول نظام الفيزياء/الرياضيات في Jamad.lean نفسِها: علميٌّ يُقيَّد مقيسًا لا شاهدَ واقع)
  لا تحقّق الشرط، فلا تُنتج .majaz عبر haml في أيّ تشكيلٍ للحقائق الثلاث.

  تحديثٌ (2026-10-19، بإذن المالك: اختار «تخصيص التسجيل بالدعوى» من بين ثلاثة مسارات عُرضت عليه،
  ردًّا على تدقيقٍ خارجيٍّ ثانٍ بعد دمج هذا الملفّ في PR #41 — وافق الدخيل الأوّل، ثمّ دقّق ثانيةً
  فأضاف: اسمٌ نصّيٌّ وحده («سببيّة») لا يُعرِّف الدعوى تعريفًا كافيًا، لأنّ علاقتين مختلفتين قد
  تتسمّيان باسمٍ واحد؛ ونبّه ألّا يُعدَّل تعريف waqiMakhtum ولا تُصنَّف المصادر المختومة من جديد
  إرضاءً لمثالٍ، وألّا تُمسّ Qaida.lean أو QawaninDalala.lean): الشرط الأوّل (شاهدٌ من واقعٍ مختوم)
  كان كافيًا لسدّ حقن بوّابةٍ من معلوماتٍ مقيسة، لكنّه لا يمنع انتقال شاهدٍ اعتُمد لدعوى (ism=
  "سببية" مثلًا بين معنيين) إلى دعوى أخرى تشارك مصدره ونوعه فقط (ism نفسه بين معنيين مختلفين، أو
  معنيين متماثلين باسمٍ آخر). فهذا التحديث يضيف هويّةً للدعوى (DawaMajaz: الاسم، والمعنى الحقيقيّ،
  والمعنى المجازيّ — فهرسا Maana كما في QawaninDalala.Qadiyya) وقيدَ تسجيلٍ (QaydTasjil) يحمل هذه
  الهويّة لا البصمة والنوع وحدهما، ويعمّم مبرهنتَي haml لتأخذا سقوطَ mashrua حقيقةً مباشرة (hf) لا
  سببًا بعينه، فيُبنى عليهما من أيّ سببٍ — كمصدرٍ غير مختوم (مبرهنة الأصل) أو كشاهدٍ مسجَّلٍ لدعوى
  غيرها (la_intiqal، الجديدة). لا تعديل على waqiMakhtum ولا على Qaida.lean أو QawaninDalala.lean.
  لا AlaqaMajaz حقيقيّةٌ مسجَّلةٌ في المستودع بعدُ (بحثٌ شامل هذه الجلسة) — فالمبرهنات هنا، كما في
  البناء الأصل، على شاهدٍ عامّ مجرَّد، لا على مثالٍ معجميٍّ معتمد؛ تعميرُ أمثلةٍ حقيقيّةٍ عملٌ منفصل.

  بناؤه الأصل يُعيد نسق Maratib.la_mafhum_bila_waqi وHawass.shahid_ghayr_mudaa_la_yuthir على alaqa
  بدل الشاهد الحسّيّ. لا جدول خارجيّ لهذه القطعة ولا مرآة بايثون، كـ SababShartMani.lean. بلا sorry
  ولا axiom ولا native_decide.
-/
import Aql.QawaninDalala
import Aql.Maratib

namespace AlaqaMajaz
open QawaninDalala Maratib

/-- هويّة الدعوى المجازيّة: اسم العلاقة (كالسببيّة والمشابهة)، ومعناها الحقيقيّ والمجازيّ —
    فهرسا Maana كما في Qadiyya. لا تتماثل دعويان إلّا بتماثل الثلاثة معًا؛ فاسمٌ واحدٌ بين معنيين
    مختلفين دعويان لا دعوى. -/
structure DawaMajaz where
  ism    : String
  haqiqi : Nat
  majazi : Nat
deriving DecidableEq, Repr

/-- علاقةٌ مجازيّةٌ مسمّاة (من علاقات ج3: سببيّة بأقسامها، مسببيّة، مشابهة...): هويّةُ دعواها،
    وشاهدُ واقعها — لا Bool مجرّد. -/
structure AlaqaMajaz where
  dawa   : DawaMajaz
  shahid : ShahidWaqi
deriving DecidableEq, Repr

/-- قيدُ تسجيلٍ: بصمةُ مودَعٍ ونوعُه (الدستور م12)، وهويّةُ الدعوى الوحيدة التي اعتُمد شاهدًا لها.
    لا يُقرأ قيدٌ شاهدًا لدعوى غير التي سُجِّل لها، ولو شارك بصمةً ونوعًا. -/
structure QaydTasjil where
  basma : String
  naw   : Idaa.Naw
  dawa  : DawaMajaz
deriving DecidableEq, Repr

/-- شرعيّةُ العلاقة: شاهدُها من مودَعٍ مسجَّلٍ نوعُه «واقعٌ مختوم» بعينه (نسق Maratib.shuhudMutabara)،
    مسجَّلٍ خصّيصًا لهويّة دعواها هي. -/
def mashrua (sijill : List QaydTasjil) (a : AlaqaMajaz) : Bool :=
  sijill.any fun q => a.shahid.basma.startsWith q.basma && q.naw == .waqiMakhtum && q.dawa == a.dawa

/-- إسقاطُها إلى Bool ليُغذَّى به haml.alaqa — فقط إن شُرعت. -/
def alaqaOf (sijill : List QaydTasjil) (a : AlaqaMajaz) : Bool :=
  mashrua sijill a

/-! ## ١. شاهدٌ من مودَعٍ غير «واقعٍ مختوم» لا يشرّع العلاقة -/

/-- **المعلومات السابقة لا تُشرِّع**: شاهدٌ من مودَعٍ كلُّه من نوعٍ آخر غير waqiMakhtum (كجداول نظام
    الفيزياء/الرياضيات — علميٌّ يُقيَّد مقيسًا، لا شاهدَ واقعٍ مختوم) لا يحقّق mashrua، أيًّا كانت
    العلاقة أو دعواها. -/
theorem mashrua_bila_waqi_makhtum
    (sijill : List QaydTasjil) (hs : ∀ q ∈ sijill, q.naw ≠ .waqiMakhtum)
    (a : AlaqaMajaz) : mashrua sijill a = false := by
  simp only [mashrua, Bool.not_eq_true, List.any_eq_false]
  intro q hq
  have := hs q hq
  cases h : q.naw <;> simp_all

/-! ## ٢. ولا انتقال شهادةٍ من دعوى إلى أخرى -/

/-- **عدم انتقال الشهادة بين دعويين**: سجلٌّ لا يحمل قيدًا لهويّة دعوى العلاقة بعينها لا يشرِّعها،
    ولو طابق شاهدُها بصمةً ونوعًا قيدَ دعوى أخرى تمامًا. فلا تُقبل علاقةٌ باعتماد شاهدٍ اعتُمد
    لغيرها، ولو اشترك المصدر والنوع. -/
theorem la_intiqal
    (sijill : List QaydTasjil) (a : AlaqaMajaz) (hd : ∀ q ∈ sijill, q.dawa ≠ a.dawa) :
    mashrua sijill a = false := by
  simp only [mashrua, Bool.not_eq_true, List.any_eq_false]
  intro q hq
  have := hd q hq
  simp_all

/-! ## ٣. فلا تنتج .majaz عبر haml — بعد الاستنفاد التامّ، لأيّ سببٍ سقطت به mashrua -/

/-- بعد استنفاد الحقائق الثلاث (الثلاث .la): علاقةٌ سقطت شرعيّتُها (alaqaOf = false، بأيّ سببٍ —
    مصدرٍ غير مختوم أو شاهدٍ لدعوى غيرها) تُنتج لا حكم، لا مجازًا (مركَّبةٌ من majaz_bad_istinfad
    المستوردة بلا تعديل). -/
theorem alaqaOf_ghayr_mashrua_la_hukm
    (sijill : List QaydTasjil) (a : AlaqaMajaz) (hf : alaqaOf sijill a = false)
    (sabq : Bool) (qarina : Option NawHaqiqa) :
    haml .la .la .la sabq qarina (alaqaOf sijill a) = .laHukm := by
  rw [hf]
  exact (majaz_bad_istinfad sabq qarina).2

/-! ## ٤. التجميع: في أيّ تشكيلٍ للحقائق الثلاث -/

/-- **النتيجة الجامعة**: علاقةٌ سقطت شرعيّتُها (بأيّ سببٍ) لا تُنتج .majaz عبر haml، أيًّا كانت
    شهادات الحقائق الثلاث — إمّا حقيقةٌ (إن شهدت واحدةٌ، la_majaz_qabl_istinfad المستوردة)، أو
    لا حكم (الباقي: ghayr_yuqif المستوردة، أو (٣) إن شهدت الثلاث كلّها بالسلب التامّ). -/
theorem alaqa_ghayr_mashrua_la_tunshi_majaz
    (sijill : List QaydTasjil) (a : AlaqaMajaz) (hf : alaqaOf sijill a = false)
    (s1 s2 s3 : Shahada) (sabq : Bool) (qarina : Option NawHaqiqa) :
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
      rw [alaqaOf_ghayr_mashrua_la_hukm sijill a hf sabq qarina]
      decide

/-! ## ٥. من السبب إلى منع المجاز طرفًا لطرف: لكلّ سببٍ لسقوط الشرعيّة مبرهنةٌ تمرّ بـ alaqaOf نفسِها

(٣) و(٤) تأخذان «alaqaOf … = false» فرضًا؛ فلا تربطان alaqaOf بـ mashrua. هاتان تربطانهما: تشتقّان ذلك الفرض من السبب
عبر تعريف alaqaOf نفسِه، فلو انفصلت alaqaOf عن mashrua (كأن تُعيد true دائمًا) سقط برهانهما. -/

/-- **بلا واقعٍ مختوم لا مجاز**: سجلٌّ لا قيدَ فيه من نوع waqiMakhtum لا يُنتج .majaz عبر haml في أيّ تشكيل. -/
theorem bila_waqi_makhtum_la_majaz
    (sijill : List QaydTasjil) (hs : ∀ q ∈ sijill, q.naw ≠ .waqiMakhtum)
    (a : AlaqaMajaz) (s1 s2 s3 : Shahada) (sabq : Bool) (qarina : Option NawHaqiqa) :
    haml s1 s2 s3 sabq qarina (alaqaOf sijill a) ≠ .majaz :=
  alaqa_ghayr_mashrua_la_tunshi_majaz sijill a (mashrua_bila_waqi_makhtum sijill hs a) s1 s2 s3 sabq qarina

/-- **شاهدُ دعوى أخرى لا يُنتج مجازًا**: سجلٌّ لا قيدَ فيه لهويّة دعوى العلاقة بعينها لا يُنتج .majaz عبر haml في أيّ
    تشكيل، ولو طابق شاهدُها بصمةً ونوعًا قيدَ دعوى أخرى. -/
theorem dawa_ukhra_la_majaz
    (sijill : List QaydTasjil) (a : AlaqaMajaz) (hd : ∀ q ∈ sijill, q.dawa ≠ a.dawa)
    (s1 s2 s3 : Shahada) (sabq : Bool) (qarina : Option NawHaqiqa) :
    haml s1 s2 s3 sabq qarina (alaqaOf sijill a) ≠ .majaz :=
  alaqa_ghayr_mashrua_la_tunshi_majaz sijill a (la_intiqal sijill a hd) s1 s2 s3 sabq qarina

end AlaqaMajaz
