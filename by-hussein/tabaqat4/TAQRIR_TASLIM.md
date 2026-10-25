# تقرير تسليم — tabaqat4 (الإصدار الأوّل ، مكتوب خارج جهاز المالك)

```
WRITTEN_BY        = Claude (جلسة حسين) على نسخة Mashru@e4c801ff في بيئة سحابية — ليس وكيل Mac
DELIVERY_FORM     = أرشيف tabaqat4.tar.gz يُفَكّ في /Users/husseinhiyassat/mashru/by-hussein/
WRITES_TO         = by-hussein/tabaqat4/ فقط (أو --out)
MASHRU_TOUCHED    = NO (T8 يقيسه بـ git status قبل/بعد)
PYTHON            = stdlib ؛ لا pip ؛ PYTHONDONTWRITEBYTECODE=1
```

## ما تغيّر سلوكيًّا

قبل: لا طريقة لتمرير جملة على Mashru إلّا بكتابة ملف Lean يدًا (كما في Shahid_Ahmad.lean).
بعد: `python3 by-hussein/tabaqat4/run.py "<جملة مشكولة>"` → S0..S8 → ثلاثة تقارير + ملفَا Lean مولَّدان + مخرجات lean الخام ، وكلّ ادّعاء برتبته من سلّم Mashru.

## ما أُنجز واختباره

| البند | الاختبار | الحالة هنا | الحالة المتوقَّعة على جهازك |
|---|---|---|---|
| S0 رفض غير المشكول ، NFC ، sha | T4 | PASS | PASS |
| S2 الدالّ بجدول Makharij.lean (أل قمرية/شمسية ، شدّة ، تنوين ، مدّ ، همزات) — مطابق لشواهد Utur.lean (dhahaba, alWalad, waladun, adDar, dhahiban) | T2, T3 + فحص يدوي | PASS | PASS |
| S4 المدلول من qamus.json المقيَّد بتعريفات Mashru ؛ الغائب NO_SEALED_MADLUL | T2, T6 | PASS | PASS |
| S5 النوعان المغلَّفان ؛ OUT_OF_EXECUTED_PATH بالاسم لغيرهما | T3 | PASS | PASS |
| S6/S7 توليد Lean (طبقة ٤) — تمّ فحصه على Aql.Isnad المبنيّة هنا: #eval وparse وaxioms | فحص مباشر | PASS | PASS |
| S7 كامل (Jisr.Utur + Aql.Isnad) على «ذَهَبَ الْوَلَدُ» | T1 | PASS (بُنيت Jisr.Utur هنا بعد الكتابة ؛ hukm3=.murakhkhas ؛ 9 نظريات ، axioms ⊆ {propext, Quot.sound}) | PASS |
| T5 إفساد خلية (دُ→دَ 69→68) يغيّر hukm3 | T5 | PASS (hukm3=.mumtani كما يتوقّع Utur.lean:958 ؛ ويُعلَن HUKM3_NOT_MURAKHKHAS) | PASS |
| T7 ثبات JSON بين تشغيلَين | T7 | PASS | PASS |
| T8 شجرة Mashru لم تُمَسّ | T8 | PASS | PASS |

```
TABAQAT4_SCOPE_TESTS_PASS            = YES (8/8 ran ؛ 0 NOT_RUN) — على نسختي ؛ يُعاد على جهازك
FULL_TREE                            = لا شجرة اختبارات أخرى في TOOL_ROOT
```

## ما بقي وسببه

```
R1  إعادة T1..T8 على جهازك   أوّل ما تفعله: python3 -I by-hussein/tabaqat4/tests/test_tabaqat4.py (نسختي من Mashru = e4c801ff ؛ إن اختلف HEAD عندك فالاختلاف يُعلَن في identity)
R2  hokom_adapter.py          غير مكتوب — واجهته في hokom_adapter.example.py ؛ يربطه وكيل Mac بموصل by-hussein القائم (قراءة فقط ، pin 8a232980)
R3  أنواع الجمل               نوعان فقط ؛ bikam (جار ومجرور) و kanaUD (كان) لهما شواهد في Mashru ولم يُغلَّفا — إسنادهما في الشاهد غير عامّ
R4  qamus.json                9 كلمات من شواهد Mashru ؛ لا توسّع إلّا بإيداع مدلولات جديدة (قرار مالك ، Q-3/Q-4)
R5  الهمزات                   أ/إ/ؤ/ئ → ء بتحويل معلَن ؛ آ → ءَ اْ ؛ ة و ى تُرفَض باسمها (Dal.kh? يرفضها أيضًا)
R6  parse مخرجات #eval        يعتمد على صيغة Repr الحالية ؛ تغيّرها في Lean يُسقط S7 بـ LEAN_PASS1_UNPARSED لا بقيمة خاطئة
```

## عيبان وُجدا بالاختبار هنا وأُصلحا قبل التسليم

```
D1  Mulhaqat.darabaZayd و rakkib بلا تأهيل namespace → LEAN_PASS1_FAILED ؛ أُصلح إلى Jisr.Mulhaqat.* و Dal.rakkib
D2  qamus مفاتيحه السطح التامّ فلم يجد «الْوَلَدَ» → صور الإعراب أُدرجت قائمةً حاصرةً صريحة (لا بقاعدة حذف حركة)
```

## تشغيلات نموذجية مرفقة (_runs_samples/)

```
a  ذَهَبَ الْوَلَدُ      الأربع مبرهن على الشاهد ، hukm3=.murakhkhas
f  ذَهَبَ وَلَدٌ        الأربع مبرهن على الشاهد ، hukm3=.murakhkhas (إطار jaaRajul)
e  ذَهَبَ الْوَلَدَ      الأربع مبرهن على الشاهد ، hukm3=.mumtani (+HUKM3_NOT_MURAKHKHAS)
b  كَتَبَ الطَّالِبُ الدَّرْسَ   ط1 مطابَق ؛ ط2 NO_SEALED_MADLUL ×3 ؛ OUT_OF_EXECUTED_PATH:3 كلمات
c  الْعِلْمُ نُورٌ        ط1 مطابَق ؛ OUT_OF_EXECUTED_PATH:جملة اسمية
```

## الإصدار 3 (2026-10-25 ، على Mashru@d2533c3)

```
+ S5-ج  باب الجزاء (Jisr/BabJaza.lean ، PR #80): [أداة + فعل الشرط + الجواب] → hukm ⟨كلام ، شعر⟩ مبرهنًا by decide ، مشروطًا بصيغتَين يعلنهما المالك (--forms ، رتبة رأي)
        T9  إِنْ تَجْتَهِدْ تَنْجَحْ   → ⟨maqbul, maqbul⟩ ؛ T10 إِنْ تَجْتَهِدْ تَنْجَحُ → ⟨qabih, maqbul⟩ (= J16 في الضابط المجمَّد) ؛ T11 بلا --forms → JAZA_FORMS_UNDECLARED
        الطبقة الرابعة NOT_APPLICABLE (الباب يحكم على الصورة لا يبني Aql.Jumla)
+ S2-ب  قارئ Mashru (qari) شاهدًا ثانيًا على الخلايا: AGREE/DISAGREE/QARI_ONLY ، كلّ اختلاف باسمه ولا يُحسَم
        T12: ذَهَبَ الْوَلَدُ AGREE بعد إسقاط همزة الابتداء (0) ؛ ذَهَبَ وَلَدٌ DISAGREE WAQF_VS_WASL ([112,52,71] وقفًا ↔ [112,52,69,59] وصلًا) ؛ ساكنةً QARI_ONLY (ة→هاء ساكنة بقرار مودَع)
+ S4-أ  المخزن عبر qari: الأقوال بسندها (المخصّص@offset/Page) برتبة «تقدير» كما يسمّيها Mashru ، ومرشَّح الجذر «مقيس» ؛ الغائب MAKHZAN_NO_ENTRY
TABAQAT4_SCOPE_TESTS_PASS = YES (12/12 ran ؛ 0 NOT_RUN) — على Mashru@d2533c3 هنا
D-A المحفوظ من المحادثة: نسخة الوكيل الأولى (محذوفة) كانت تبرهن على dhahabaAlWalad لا على المدخل — EVIDENCE_IN_CHAT_ONLY
```

ما لم يُفعَل في الإصدار 3: hokom_adapter.py ما زال غير مكتوب (الصيغ في باب الجزاء تُعطى يدًا بدل أن تأتي تقديرًا من Hokom) ؛ bikam/kanaUD غير مغلَّفَين ؛ qari يُقرأ من نصّه لا من JSON (يُسقط S2-ب بـ QARI_UNPARSED عند تغيّر صياغته ، لا بقيمة خاطئة).

## بصمات الملفات (الإصدار 3)
  d79658ffd610b631  ./README.md
  7630a7d8c0ae717b  ./TAQRIR_TASLIM.md
  f2960748511e6b92  ./hokom_adapter.example.py
  db220690335d14ef  ./run.py
  e3b0c44298fc1c14  ./t4/__init__.py
  54143f4dc3a3022e  ./t4/core.py
  52e44fb0ea84e9d2  ./t4/dal.py
  e8662a21d29bfe8b  ./t4/qamus.json
  841d73f7a5f34fa7  ./t4/qari.py
  58b9972beedfc9dd  ./t4/report.py
  c8824b550b68564f  ./tests/test_tabaqat4.py
