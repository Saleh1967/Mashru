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

## الإصدار 4 (2026-10-25 ، على Mashru@ed7c5d3248a1)

**ما تغيّر سلوكيًّا:** صور الأفعال في باب الجزاء صارت تأتي **تقديرًا من Hokom** (مقعدًا معلَنًا واحدًا) بدل كتابتها يدًا:
`--hokom` بلا `--forms` على جملةٍ شرطية ⇒ تُشتَقّ صورتا الشرط والجواب من `word_class_subclass+mood` عبر `t4/forms_map.json`
برتبة «تقدير» ومصدرٍ `HOKOM_TAQDIR` ، ولا تصير مدلولًا ولا حكمًا. و`--forms` اليدوي يغلب عند التعارض (`FORMS_CONFLICT_OWNER_VS_HOKOM`).

- **B1 (hokom_adapter.py — الأهمّ):** كُتب على موصل Hokom (venv بالـpin 8a23298076b4، قراءةٌ فقط، `PYTHONDONTWRITEBYTECODE=1`)؛
  `taqdir(surfaces)` يعيد {pin, word_class, word_class_subclass, final_root, final_wazn, mood, directive, active_residuals}؛
  الغائب `None` بسببه في residuals، لا تخمين. اشتقاق الصيغ في S5-ج بجدول `forms_map.json` الحاصر؛ غير المُعرَّف `FORMS_UNMAPPED:<القيمة>` وتوقّف.
  **اختباره:** T13 (الصيغتان من Hokom، hukm ⟨maqbul,maqbul⟩ مبرهنًا)، T14 (تعارض ⇒ المالك يغلب)، T15 (تُعرَض ولا تُستهلك: طبقتا 3/4 كتشغيلٍ بلا --hokom)، T16 (Hokom غير قابل للقراءة ⇒ HOKOM_ADAPTER_FAILED باسمه وبقيّة المراحل تكتمل).
- **B2 (التيرمنال):** `--open` (يفتح taqrir.html)، `--json` (يطبع taqrir.json)، سطرا `HOKOM=PRESENT:<pin>|ADAPTER_ABSENT|...` و`QARI=AGREE n/m|...`؛
  وأُصلحت صياغة S4 في مسار الجزاء («لا مدلول بنيويّ ؛ لا يمنع باب الجزاء»)؛ و`--split-punct` يقطع عند [.؟!] فقط بخيارٍ معلَن `SPLIT_ON_PUNCT_OWNER_OPTION`، وبدونه السلوك كما كان. **اختباره:** T17.
- **B3 (HTML):** كتلةُ «٢ج. تقدير Hokom مقابل قارئ Mashru» لكلّ كلمة (الصنف/الجذر/الوزن/البقايا + مرشَّح جذر القارئ + خانة AGREE/DISAGREE/ONE_SIDED تُعرَض ولا تُحسَم)، مع لوحة «تقدير». الرموز مترجَمة مع الأصل بين قوسين (قائم من v3).
- **B4:** T1–T18 تمرّ ملفًا ملفًا: **18/18 ran ، 0 NOT_RUN** (≈42 ث ، مع Lean وHokom).
- **B5:** إيداعٌ لكلّ بند على الفرع `by-hussein/tabaqat4`، بلا push.

**ما بقي وسببه (معلَنٌ):**
- **مطابقة الضابط J01–J39 الدقيقة** (BabJazaDawabit.lean) في التقرير **لم تُحسب**: حسابُها يعني تكرار منطق Mashru في بايثون (محظور) أو استعلامًا من Lean لم يُضَف؛ فالتقرير يذكر الحكم المبرهن ويحيل إلى الضابط بالاسم دون تعيين رقم الحالة. (اسم J16 في وثيقة T10 تعليقٌ لا حساب.)
- **bikam/kanaUD** (شبه الجملة والناسخ) غير مغلَّفَين في المسار الإسناديّ بعد.
- **قارئ Hokom** يُقرأ عبر venv subprocess؛ تغيّر واجهة `hokom_pipeline.hokom` يُسقط التقدير بـ `HOKOM_ADAPTER_FAILED` باسمه لا بقيمةٍ خاطئة.

**الأعلام:**
```
TABAQAT4_SCOPE_TESTS_PASS = YES (18/18 ran ؛ 0 NOT_RUN) — على Mashru@ed7c5d3248a1
CORE_SANITY_PASS          = نعم على مقياس هذه الجولة = T1–T18 + T8 (Mashru لم تُمَسّ git قبل/بعد) + T18 (Hokom لم تُمَسّ). ملاحظة: bawwaba_local (byhussein) على فرع by-hussein/wasla لا على هذا الفرع ، فلم يُشغَّل هنا — لم أدّعِه.
FULL_TREE_BASELINE        = لم يُعَد تشغيل بوّابة الأمّ لهذه الجولة (تغييري بايثونٌ محض تحت tabaqat4/ خارج شجرة بناء Mashru) ؛ خطّ الأساس 1522/515/44 بآخر تشغيلٍ مؤكِّد سابق
MASHRU_HEAD               = ed7c5d3248a1
HOKOM_PIN                 = 8a23298076b4
MASHRU_TOUCHED            = NO (T8 git قبل/بعد) ؛ HOKOM_TOUCHED = NO (T18 git قبل/بعد ؛ تعديلاتُ cl16_root_wazn/* في Hokom سابقةٌ لجلستي ، لم أمسّها)
```

**بصمات ملفّات الإصدار 4:**
```
ce0ef76c15a6f38f  hokom_adapter.py
562584d2506ede05  t4/forms_map.json
dd173d0217a4c2b9  t4/core.py
8b4438a1eacdc7f2  run.py
628ad9744fe6080e  t4/report.py
2222d7c33950f7f7  tests/test_tabaqat4.py
```

## الإصدار 5 (2026-10-25 ، على Mashru@7a902672a330 ، Hokom@8a23298076b4)

**ما تغيّر سلوكيًّا:** فُكَّ السببان اللذان أسكتا جمل تعقّل الستّ: (أ) **اختيار الإطار** صار من النمط (قسمُ الكلمة + al/تنوين)
عبر `t4/itar_map.json` → إطار Mashru ذي شاهد Itar3 ، ثمّ `hukm3` (الحركةُ يحكمها hukm3 لا الاختيار ، فقلبُ الإعراب يُمسَك ممتنعًا)؛
(ب) **المعنى** صار يدخل من `by-hussein/mudaat` بإمضاء المالك (D5) مصدرًا ثانيًا بعد qamus ، يُضمَّن نصًّا في Jumla.lean. تقديرُ
Hokom/تعقّل **يختار** الإطار/النمط ولا **يحكم** (رتبة «تقدير» ، `CONDITIONAL_ON_SELECTED_ITAR`). Hokom وMashru لم يُمَسّا.

- **B6 (itar_map + S5):** `t4/itar_map.json` حاصر: `fiil|ism(al)`→darabaZayd ، `fiil|ism(tanwin)`→jaaRajul ، `fiil|ism(al)|ism(al)`→daraba
  (شواهدُها في Utur) ؛ `zaydQaim` مُعلَنٌ `UD_WITHOUT_ITAR3_WITNESS` ولا يُستعمل. النمطُ من قسم Hokom (إن حضر) وإلّا قسم المدلول + al/تنوين من السطح ؛
  `--taaqol` مصدرٌ بديل (عائلات P8) برتبة تقدير ، وتعارضُه مع Hokom `ITAR_SOURCE_CONFLICT` (Hokom يغلب). نمطٌ غير مُخرَّط → `ITAR_UNMAPPED`.
  **قبوله:** T20 (daraba مختار ، hukm3 مبرهَن ، 4 طبقات ، axioms⊆) ، T25 (ITAR_UNMAPPED) ، T26 (TAAQOL_P8 + ITAR_SOURCE_CONFLICT) — خضراء.
- **B7 (المودَعات D5):** `by-hussein/mudaat/` (mudaat.json ، Mudaat.lean يمرّ قائمًا بذاته ، MUDAAT_IMDA.md) ؛ `mudaat_prep.py` يجهّز PENDING من تشغيلٍ
  (الجذر من Hokom ، القول بسنده ، tim من القسم ؛ haqiqa/قابليّة للمالك ، لا تُقترَح)؛ S4 يحمّل RATIFIED فقط ، haqiqa≥1000 والمحجوزة/المصادِمة مرفوضة ،
  والمودَعات تُضمَّن نصًّا في Jumla.lean (لا استيرادَ وحدةٍ خارج مكتبة Mashru). **قبوله:** T21 (laHukm بقاعدة Mashru) ، T23 (PENDING لا يدخل) ، T24 (MUDAA_HAQIQA_COLLISION) — خضراء.
- **B8:** T1–T18 + T20–T27 ملفًا ملفًا: **26/26 ran ، 0 NOT_RUN** (≈57 ث). (ملفّات «T19» المذكورة في الأمر غير موجودة على هذا الفرع — أُعلِن.)
- **B9:** إيداعٌ لكلّ بند ؛ عيّنتا C02 (بمودَعات الاختبار → EXECUTED ؛ وبدونها → OUT كما كان) ؛ ورقة الإمضاء.

**ما بقي وسببه (معلَنٌ):**
- **مودَعات RATIFIED = صفر**: mudaat.json فيه PENDING فقط (كتب/طالب/درس ، جُهّزت من تشغيل فعليّ)؛ لا تدخل Lean حتى يُمضي المالك الخانات الثلاث (D5). عيّنة C02 التنفيذيّة استعملت **fixture اختبار** مُعلَنةً أنّها ليست إمضاءً.
- **ITAR_AMBIGUOUS غيرُ مُستثار**: بمفاتيح النمط القاطعة (قسم+al/تنوين) لا ينشأ تعدّدٌ ؛ الحارس باقٍ للخلايا غير المقروءة (يسبقه توقّفُ الدالّ عادةً) ؛ لم يُشغَّل اختبارٌ له — أُعلِن.
- **الأطر المغلَّفة** = darabaZayd/jaaRajul/daraba + باب الجزاء ؛ bikam/kanaUD/lamYafalUD/lanYafalUD لها شواهد في Utur ولم تُدرَج في itar_map بعد (أنماطها تحتاج قراءةَ أدواتٍ/حروفِ جرّ من السطح) — تبقى OUT_OF_EXECUTED_PATH باسمها.

**الأعلام:**
```
TABAQAT4_SCOPE_TESTS_PASS = YES (26/26 ran ؛ 0 NOT_RUN) — Mashru@7a902672a330
CORE_SANITY_PASS          = نعم (T22: بصمة شجرة Hokom قبل=بعد ؛ T8/T22: Mashru نظيف ، لا كتابة خارج by-hussein)
FULL_TREE_BASELINE        = لم يُعَد تشغيل بوّابة الأمّ (تغييري بايثونٌ محض خارج شجرة البناء) ؛ 1522/515/44 بآخر تشغيلٍ سابق
HOKOM_TREE_SHA_BEFORE     = 5ddc0c35a9324c6f6fcee36f6229751f
HOKOM_TREE_SHA_AFTER      = 5ddc0c35a9324c6f6fcee36f6229751f   (متطابقتان ؛ Hokom لم يُمَسّ)
MASHRU_HEAD               = 7a902672a330 ؛ HOKOM_PIN = 8a23298076b4
```

## الإصدار 5.1 (2026-10-26) — تصحيحات لا تغيّر حكمًا

- **G4 (استشهاد خاطئ)**: شاهد إطار `Mulhaqat.daraba` كان `bimafulayn (Utur.lean:1032)` وهو خطأ (bimafulayn إطاره mafulaynUD ، أربع خانات).
  الصحيح `darabaFata (Utur.lean:1102–1103)` («ضَرَبَ الْفَتَى الْوَلَدَ» ، `ud := Mulhaqat.daraba` ، ثلاث كلمات ، إسناده ⟨الفاعل ، qabiliyya حقيقة الفعل ، isnadiyya⟩)
  — يوافق قاعدة الإسناد المطبَّقة ، فالحكم كان سليمًا والاستشهادُ وحده خطأً. صُحِّح في `itar_map.json` ، وأُضيف توكيدُه في T20 (`darabaFata` في shahid_mashru).
- **نصوص بالية في التقرير** (لا تغيّر حكمًا): `tabaqa1_kalimat` صار «خلايا الكلمات الـN» (كانت «الكلمتَين»)؛ `tabaqa2_maani` صار «المدلولات الـN ... جميعُها مفحوصةٌ ومنها المفعول»
  (كان «المدلولان»)؛ و«ما لا يُدَّعى» صار يسرد أطر itar_map الثلاثة + باب الجزاء (كان «نوعان فقط»).
- `_runs_samples/c02_*` أُعيد توليدها على الرأس المودَع بشجرةٍ نظيفة (identity.mashru_tree_clean=true).
- المجموعة: **26/26 ran ، 0 NOT_RUN** بعد التصحيح. (الإمضاء الحقيقيّ يبقى الفرقَ الوحيد: `imda.man=DR_HUSSEIN` بدل `FIXTURE_TEST` ، ينتظر إمضاءك في MUDAAT_IMDA.)

## الإصدار 5.1b (2026-10-26) — إغلاق بندَي v5.1 المتروكَين

### ١ — T22: بصمة المحتوى (sha256) لا الميتاداتا (شرط المالك)
الخوارزم الجديد: `HOKOM_TREE_SHA256` = sha256 لنصّ القائمة المرتّبة «<مسار نسبيّ>⇥<sha256 المحتوى>\n» لكلّ ملفّ تحت HOKOM_ROOT
(بما فيه المخفيّة ، باستثناء `.git/` — مُعلَن) ؛ 15949 ملفًّا ، ~3.4 ثانية (مقيس). القديم كان `path+size+mtime`.
T22 يحسبها قبل المجموعة وبعدها ويوجب التطابق ، ويفشل باسم الملفّ إن تعذّرت قراءته (`HOKOM_FILE_UNREADABLE:<ملف>`) لا يتجاوزه.
```
HOKOM_TREE_SHA256_BEFORE = 478fd4dd27d30a61ead730de2a2df1206c19cb98475a4f339c960fd7342ac8c3   (sha256 المحتوى)
HOKOM_TREE_SHA256_AFTER  = 478fd4dd27d30a61ead730de2a2df1206c19cb98475a4f339c960fd7342ac8c3
الخوارزم                  = sha256 للمحتوى ؛ القديم كان path+size+mtime (قيمته 5ddc0c35… ، لم تعد تُستعمل)
```

### ٢ — G1: أنماط itar_map لم تُنفَّذ — وسببها (قائمة حاصرة من جدول أمر v5 ؛ نُفّذ منها darabaZayd/jaaRajul/daraba)
```
bikam (جار+مجرور ، شاهد fiDar :922)              لم أصل إليه ؛ ومعه مانعٌ قائم: إسناده .alaqa a b .idafiyya يحتاج alaqat (a,b) مودَعة ، وبلا إيداعها ISNAD_RULE_UNDECLARED (لا يُبرهَن) ؛ ونمط [harf|ism] لم يُدرَج في itar_map.
kanaUD (كان+اسم+خبر ، شاهد kanaAlWalad :944)      لم أصل إليه ؛ تمييز «كان» ناسخًا وبناء إسناد [اسم+خبر] على الناسخ لم يُبنَ.
lamYafalUD / lanYafalUD (:1052 ، :1107)          لم أصل إليه ؛ «لم/لن» ليستا من أدوات الشرط (مسار الجزاء) ، وإطاراهما مُعطَيان بدالّة (v : Kalima) ونمطهما [أداة+مضارع+فاعل] لم يُدرَج في itar_map.
الحال (darabaZayd + ml hal ، شاهد dhahabaAlWaladMusrian :980)   لم أصل إليه ؛ الملحق (jisr.ml = حال) يحتاج بناء حقل ml في الإطار (لا يبنيه _lean_file الحاليّ) ، ونمط [فعل+فاعل+حال منصوب] لم يُدرَج.
zaydQaim (مبتدأ+خبر)                             مُعلَن UD_WITHOUT_ITAR3_WITNESS في itar_map (لا شاهد Itar3 في المستودع) — يبقى كما هو ، لا يُستعمل.
```

## الإصدار 5.2 (2026-10-26) — إمضاء المالك الحقيقيّ للمودَعات الثلاثة (D5)

أمضى المالك (DR_HUSSEIN) الخانات الثلاث لكلمات «كتب/طالب/درس» ، فحوّلتُها من PENDING إلى RATIFIED في
`by-hussein/mudaat/mudaat.json`:

```
كَتَبَ   → ism_lean=kataba_m ، haqiqa=1001 ، tim=true  ، قابليّات=[]      ، imda={DR_HUSSEIN, 2026-10-26}
الطَّالِبُ → ism_lean=talib_m  ، haqiqa=1002 ، tim=false ، قابليّات=[1001] ، imda={DR_HUSSEIN, 2026-10-26}
الدَّرْسَ  → ism_lean=dars_m   ، haqiqa=1003 ، tim=false ، قابليّات=[]      ، imda={DR_HUSSEIN, 2026-10-26}
```

**أثرُه (يُبطل صراحةً سطرَي «ما بقي» أعلاه: «مودَعات RATIFIED = صفر» و«الإمضاء الحقيقيّ يبقى الفرقَ الوحيد»):**
- `by-hussein/mudaat/Mudaat.lean` أُعيد توليدُه من الثلاثة ويمرّ قائمًا بذاته (`lake env lean` ، exit 0).
- عيّنة `_runs_samples/c02_ratified_dr_hussein/` على المودَع الحقيقيّ (لا fixture): **EXECUTED** ، الطبقات الأربع «مبرهن على الشاهد» ،
  `hukm3=.murakhkhas` ، `MADLUL_SOURCE=OWNER_MUDAA` ، شاهد `darabaFata (Jisr/Utur.lean:1102–1103)` ، المسلّمات كلّها ⊆ {propext, Classical.choice, Quot.sound} ، `imda.man=DR_HUSSEIN`.
  فلم يَعُد بين هذا التقرير والتقرير المعتدّ به فرقٌ في مصدر المعنى.

**بنيةٌ أُصلحت (regression من إضافة `load_default_mudaat`):** كانت تهيئةُ `self.claims`/`self.la_yuddaa` واقعةً داخل `_load_mudaat` ،
فإن لم يُستدعَ (المسار الخالي) بقيا غير مهيَّأين → `AttributeError` في `_s2`. نُقلت التهيئةُ إلى `__init__` قبل `self.stages`.
والقارئُ الافتراضيّ `by-hussein/mudaat/mudaat.json` يُحمَّل في `run.py` (CLI) بـ`load_default_mudaat=True` ، والاختباراتُ تمرّر `False` لتبقى محكومةً بـfixtureها.

**الأعلام (5.2):**
```
TABAQAT4_SCOPE_TESTS_PASS = YES (26/26 ran ؛ 0 NOT_RUN)
C02_REAL_DEPOSIT          = EXECUTED ؛ 4 طبقات «مبرهن على الشاهد» ؛ hukm3=.murakhkhas ؛ OWNER_MUDAA ؛ DR_HUSSEIN ؛ axioms⊆المسموح
HOKOM_TREE_SHA256         = 478fd4dd27d30a61ead730de2a2df1206c19cb98475a4f339c960fd7342ac8c3  (15949 ملفًّا ؛ قبل=بعد ؛ لم يُمَسّ)
ISOLATION                 = كلّ التغييرات تحت by-hussein/ (mudaat.json ، Mudaat.lean ، t4/core.py ، tests ، _runs_samples/c02_*) — لا شيء خارجها
```

## الإصدار 6 (2026-10-27) — قانون الإيداع بالجملة D6 (HFN + المقاييس)

**ما تغيّر سلوكيًّا:** مصدرٌ ثالثٌ للمعنى — بعد qamus (شاهد Mashru) والمودَع اليدويّ (D5) — هو **D6**: مودَعٌ يُعدّ
`RATIFIED_BY_RULE` إذا اجتمعت شروطه الستّة من HFN release_v18 + المقاييس + Hokom. المصادر الثلاثة READ_ONLY ولم تُمَسّ.
AWN لم يُقرأ (T34). لا كاش ولا بايتكود تحت HFN. القانون D6 بنصّه في `OWNER_QUESTIONS_v6` و`t4/hfn_map.json`.

**B10 — قياس التغطية (ungarnished):**
```
SURFACES_MEASURED = 14   (من سبع جملٍ مستردَّة فعلًا من _runs_samples ؛ «C01–C07» والنصّ الطويل غير موجودَين نصًّا — OWNER_QUESTIONS_v6 س1)
D6_FULL           = 3    (ذَهَبَ 745695 ، كَتَبَ 1050082 ، مَالِكٌ 891697)
D6_PENDING        = 11   : D6_HOKOM_ROOT_NULL=5 ، D6_HOKOM_NOT_ACCEPT(DEFER)=2 ، D6_NO_HFN_UNIT=4 (منها حرف)
                          ROOT_MISMATCH=0 ، AMBIGUOUS=0 ، NO_SANAD=0
```
القرار الذي يحسمه القياس: **أكبر مصدر تأجيل هو Hokom لا HFN** (7/11). و«كَتَبَ الطَّالِبُ الدَّرْسَ» لا يُمضيها D6 كاملةً —
الفعلُ وحده ؛ الاسمان DEFER (وهما اللذان أُمضيا يدًا في v5.2). التفصيل في `mudaat/D6_COVERAGE.md`.

**B11 — hfn_map.json ودالّة haqiqa:** `t4/hfn_map.json` جدول حاصر (حقل ← ملف/عمود/قاعدة). **haqiqa:** الفرع الثاني
(SHA256_DERIVED) مُعلَنًا، لأنّ release_v18 لا معرّفَ عدديًّا ثابتًا فيه (المعرّفات `HFN-E-<hex>`): `100000 + int(sha256("release_v18:"+pos+":"+lu_id),16)%10^6`.
الذواتُ بلا مفهوم في HFN: تُطابَق عبر وحدتها المعجمية (اسم فاعل/مصدر) — سؤال B11 في `OWNER_QUESTIONS_v6` س3.

**B12 — mudaat_prep.py --d6:** مطبَّق ومشغَّل. أضاف `ذهب`/`مالك` (RATIFIED_BY_RULE) ، وأعلن `كتب` → D6_SHADOWED_BY_MANUAL
(اليدويّ غلب) ، ولم يمسّ المودَعات اليدوية الثلاث (كتب/طالب/درس بقيت RATIFIED/DR_HUSSEIN/2026-10-26). `Mudaat.lean` أُعيد توليده
من RATIFIED+RATIFIED_BY_RULE ويمرّ `lake env lean` قائمًا بذاته (EXIT=0). كلّ حقل من عمودٍ مسمّى ؛ `qabiliyyat=[]` (س2).

**B13 — الاختبارات: 33/33 ran ، 0 NOT_RUN** (26 سابقة + T28–T34) ، و`test_conformance.py` 2/2.
```
T28 تجميد المصادر (HFN+maqayis+Hokom) قبل=بعد = PASS
T29 D6 كامل على «ذَهَبَ» (الوحدة بمعرّفها في lexical_units ، haqiqa دالّة ثابتة) = PASS
T30 ROOT_MISMATCH (fixture) بلا رقم = PASS
T31 AMBIGUOUS_UNIT:2 (fixture) بلا ترجيح = PASS
T32 ثبات haqiqa ونطاقها ≥100000 = PASS
T33 اليدويّ يُظلِّل D6 (SHADOWED_BY_MANUAL) = PASS
T34 AWN لم يُقرأ (تغليف open) = PASS
```

**B14 — العيّنات:** `_runs_samples/d6_c01..d6_c07` للجمل السبع بـ`--hokom`:
```
d6_c01 ذَهَبَ الْوَلَدُ        ط1..4 مبرهن على الشاهد ؛ hukm3=.murakhkhas
d6_c02 كَتَبَ الطَّالِبُ الدَّرْسَ  ط1..4 مبرهن على الشاهد ؛ hukm3=.murakhkhas  (المودَعات اليدوية)
d6_c03 الْعِلْمُ نُورٌ         ط1 مطابَق ؛ ط2 PARTIAL (لا مدلول) ؛ hukm3=None
d6_c04 ذَهَبَ وَلَدٌ           ط1..4 مبرهن على الشاهد ؛ hukm3=.murakhkhas
d6_c05 ذَهَبَ الْوَلَدَ         ط1..4 مبرهن على الشاهد ؛ hukm3=.mumtani (مفعولٌ في موضع الفاعل)
d6_c06 إِنْ تَجْتَهِدْ تَنْجَحْ   ط3 مبرهن على الشاهد ؛ hukm3=.maqbul (جزاء)
d6_c07 مَاتَ مَالِكٌ           ط1 مطابَق ؛ ط2 PARTIAL ؛ hukm3=None (مَاتَ جذرُه None عند Hokom)
```
العيّناتُ تجري عبر qamus/المودَعات اليدوية ؛ وحدةُ D6 الجديدة الوحيدة ذاتُ معنًى مستقلّ (`مَالِكٌ`) لا إطارَ جملةٍ لها في هذا
الكوربوس ، فلا تظهر مدلولُ D6 في برهان جملةٍ هنا — معلَن.

**البصمات (قبل=بعد) و MASHRU_HEAD:**
```
HOKOM_TREE_SHA256    = 478fd4dd27d30a61ead730de2a2df1206c19cb98475a4f339c960fd7342ac8c3  (15949 ملفًّا ؛ قبل=بعد)
HFN_V18_TREE_SHA256  = 7d4caf662c1c8a8069a91fcb8a8c59d880e0670198bdb72f20dc7c525205b069  (46 ملفًّا ؛ قبل=بعد)
HFN_MANIFEST_SHA256  = 975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3
MAQAYIS_DB_SHA256    = 35c7062dd5edf40304670d18e1c6527dad04c7f13d2b2212b95519e19997897f   (قبل=بعد)
MASHRU_HEAD          = 8599238 ؛ HOKOM_PIN = 8a23298076b4 ؛ HFN_RELEASE = release_v18
ISOLATION            = لا شيء خارج by-hussein/ (git status --untracked-files=all)
```

**لم يُنفَّذ (بأسمائه وسببه):**
- **كوربوس C01–C07 والنصّ الطويل**: غير موجودَين نصًّا في المستودع ؛ قِستُ على المستردّ فعلًا (14 سطحًا لا ~50). OWNER_QUESTIONS_v6 س1.
- **qabiliyyat من valence.csv**: `valence.csv` يربط الحدثَ بالمفهوم لا الذاتَ بالحدث ؛ لا عمودَ يعطي قابليّةَ الذات ⇒ `qabiliyyat=[]`
  في كلّ مودَع D6. OWNER_QUESTIONS_v6 س2 (أكبر فجوة).
- **khawass / alaqat في D6**: لا عمودَ HFN يعطيهما ⇒ `[]` معلَن.
- **سند المخصّص عبر qari في D6**: استعملتُ سند المقاييس فقط في القياس ؛ مسار المخصّص (makhzan) لم يُدمَج في D6.
- **مدلول D6 في برهان جملة**: لا عيّنة تُظهره (انظر B14).
- **fixtures/hfn_*.json على القرص**: اختبارا T30/T31 يبنيان HFN بمقتطفاتٍ في الذاكرة (`HFN.from_records`) لا بملفّات fixture.

## الإصدار 7 (2026-10-28) — D6-ب (مشتقّات ومضارع) ، D7 (جوامد وأعلام تُجهَّز) ، قناة الإيداع

**B0 — مواكبة main:** الفرعُ أُعيد وضعُه (rebase) على `origin/main`. **تنبيه:** main تقدّم إلى `09f7b27` (PR #92) لا `108a255`
كما في الأمر — أُعلِن ولم يُختلَق الرقم ؛ أُعيد الوضع على الرأس الحقيقيّ. 21 إيداعًا كلُّها تحت `by-hussein/` طُبِّقت بلا تعارض.
`lake build Jisr.Utur Aql.Isnad Jisr.BabJaza Jisr.BabJazaDawabit qari` نجح (123 عملًا) ؛ T19 42/42 + Conf PASS ؛ المجموعة 33/33.
`_hfn_v19_draft/` (شاهد المالك) أُضيف إلى `by-hussein/.gitignore`. **MASHRU_HEAD بعد rebase = `d01309a`** (رأس الفرع).

**ما تغيّر سلوكيًّا:** (أ) **D6-ب** — المشتقّات (اسم فاعل/مفعول) تُرسَّم بحقيقة حدثها (`haqiqa_event` ، الفعلُ ومشتقّه واحد) و`tim=false`
و`qism=ism_mushtaq` ؛ والمضارع يُطابَق بلِيمة Hokom الماضية (`lemma_surface`) ضدّ events ، وغيابُها `D6_LEMMA_ABSENT`. (ب) **D7** — الجوامد
والأعلام تُجهَّز PENDING بمرجع المخصّص (باب/كتاب بسطره) وخانات المالك فارغة ؛ لا تُبنى في HFN. (ج) **قناة الإيداع** — سندُ D6 يُحال إلى
النصّ المختوم (`7f71af0d@موضع`) لا `maqayis.db` ؛ و`Mudaat.lean` لا يُولَّد إلّا من نسخةٍ مختومة (وإلّا `MUDAAT_UNSEALED`).

**تنبيه بيئيّ حاكم (OWNER_ALERT):** النصّ المختوم للمقاييس/المخصّص **غيرُ حاضرٍ في هذه البيئة** (بُحث بـ`find`: لا maqayis.txt/mukhassas.txt ؛
`MUDAA_DIR=/path/to/mudaat` نائب). فبقاعدة B4 نفسها («تعذّر تعيين الموضع ⇒ D6_NO_SANAD لا الإحالة إلى db») **لا يُرسَّم مودَعُ D6 في هذه
البيئة**. أُبقي سندُ `maqayis.db` للمعاينة (`db_preview`) وحدها ، مَوسومًا ، لا يُودَع.

**B2 — التصنيف السباعيّ (الكوربوس المسترد ، 14 سطحًا):**
```
الوضع              COVERED_WITNESS  COVERED_MANUAL  HARF  D6_EVENT  D6_MUSHTAQ  D6_PENDING  D7_JAMID  D7_ALAM
db_preview (أهليّة)      4               3            1       1(تنجح)   1(مالك)      1(تجتهد)      3         0
sealed (واقع البيئة)     4               3            1       0         0           2            3         1(مالك)
```
db_preview: تَنْجَحْ→D6_EVENT (لِيمة Hokom نَجَحَ) ، مَالِكٌ→D6_MUSHTAQ + D7_ALAM_READING_POSSIBLE ، تَجْتَهِدْ→D6_LEMMA_ABSENT.
sealed: تَنْجَحْ→D6_NO_SANAD_SEALED_ABSENT ، مَالِكٌ→D7_ALAM. D7_JAMID: العلم/نور/مات (ومنها «مات» أجوفٌ يقرؤه Hokom ISM بجذر null — لا يُرقَّع).

**البصمات الرباعية (قبل=بعد):**
```
HOKOM_TREE_SHA256   = 478fd4dd…7342ac8c3  قبل=بعد ✓
HFN_V18_TREE_SHA256 = 7d4caf66…205b069    قبل=بعد ✓
MAQAYIS_DB_SHA256   = 35c7062d…997897f    قبل=بعد ✓
MUDAA_DIR           = غائبٌ في البيئة (نائب) — قراءةً لا كتابة ؛ لا بصمة
MASHRU_HEAD         = d01309a (بعد rebase على 09f7b27) ؛ خارج by-hussein = لا شيء
```

**لكلّ بند:**
- **B1 (مشتقّات):** `hfn_d6.haqiqa_event` + `d6_kind`/`qism`/`tim` ؛ مَالِكٌ/سَاكِنٌ مشتقّان أهليّةً. اختباره T35 (سَاكِنٌ) ، T40 (مالك + flag).
- **B2 (مضارع):** `hokom_adapter` يُصدّر `lemma_surface` ؛ المضارع يُطابَق بها. اختباره T36 (تنجح D6_EVENT ، تجتهد D6_LEMMA_ABSENT).
- **B3 (D7):** `t4/mushtaq_awzan.json` (FA3IL/MAF3UL بترميز Hokom) ، `mudaat/alam.json` (قائمة أوّليّة) ، `prep_v7` يجهّز D7 بمرجع `ajnas_mukhassas` ، و`MUDAAT_IMDA.md` (D7 ، haqiqa فارغ). اختباره T37 (البيت D7_JAMID ، محمد D7_ALAM juzi).
- **B4 (القناة):** `mudaat.json` مراجع فقط (T38 = 0 نصّ معجميّ >20 حرفًا) ، `madlulat_export.tsv` ، `IDAA_COMMANDS.md` (أمرا الختم للمالك ، لم يُشغَّلا) ، بوّابة `mudaat_sealed` ⇒ `MUDAAT_UNSEALED`. اختباره T38 ، T39.
- **B5 (الاختبارات):** T1–T41 + conformance = **40/40 ran ، 0 NOT_RUN** + Conf 2/2.
- **B6:** `_runs_samples/v7_c01..c07` (الجمل السبع ، تجري عبر qamus/اليدويّ) ، وهذا القسم.

**لم يُنفَّذ (بأسمائه وسببه):**
- **رَسْمُ مودَعات D6 (RATIFIED_BY_RULE)**: مُعطَّلٌ بيئيًّا — النصّ المختوم للمقاييس غائب ⇒ لا سند مختوم (B4). الأهليّة في `db_preview`.
- **سند المخصّص عبر qari في D7**: استُعمل مرجع `ajnas_mukhassas` (عناوين الأبواب) ؛ وأكثرُ الجوامد لا ترد عنوانًا (بيت/نور: 0) ⇒ `mukhassas_ref=null`. النصّ الخام للمخصّص غائب.
- **qabiliyyat / khawass / alaqat في D6/D7**: `[]` (لا عمود HFN ولا إمضاء). D7 خاناتُ المالك فارغة عمدًا.
- **الكوربوس C01–C07 والنصّ الطويل**: غير موجودَين نصًّا (كـ v6 س1) ؛ قِستُ على 14 سطحًا مستردًّا.
- **تمييز المصدر عن الجامد بالوزن**: ترميز Hokom `FA3L` يُشترَك بين بيت (جامد) ودرس (مصدر) ⇒ مصادرُ تقع في D7_JAMID. حدٌّ معلَن.
- **ختم أيّ مصدر / madlulat_export**: لم يُشغَّل `sajjil` (م9) ؛ أمرا الختم في `IDAA_COMMANDS.md` للمالك.
