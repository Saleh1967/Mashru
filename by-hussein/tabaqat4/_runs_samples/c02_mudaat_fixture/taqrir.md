# Tabaqat4 — «كَتَبَ الطَّالِبُ الدَّرْسَ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = f91733a1e61dfedbe1b8a6a6916a8e06c261a8ba0e212fd9c64cd760a08d4367
CODEPOINTS        = 27 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = 7a902672a330c61ff1bade2de1414bec9934eaaa ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مبرهن على الشاهد | ط2:مبرهن على الشاهد | ط3:مبرهن على الشاهد | ط4:مبرهن على الشاهد
HUKM3             = .murakhkhas
WASM_SUMMARY      = مبرهن=1 ، مبرهن على الشاهد=8 ، مطابَق=6 ، مفحوص=1 ، مقيس=2 ، تقدير=1 ، بلا رتبة=2
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ١ — الدالّ وحده | `dal_W-f91733a1-000` | «كَتَبَ»: 3 خلية [كَ=32, تَ=72, بَ=104] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-f91733a1-001` | «الطَّالِبُ»: 5 خلية [طْ=67, طَ=64, اْ=11, لِ=54, بُ=105] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-f91733a1-002` | «الدَّرْسَ»: 4 خلية [دْ=71, دَ=68, رْ=63, سَ=80] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [32, 72, 104, 67, 64, 11, 54, 105, 71, 68, 63, 80] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ١ — الدالّ وحده | `tabaqa1_kalimat` | خلايا الكلمتَين كما بناها Mashru في الإطار الثلاثي (مطابقة البناء) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٢ — المدلول وحده | `makhzan_W-f91733a1-000` | المخزن باللفظ «كتب»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `jidhr_W-f91733a1-000` | مرشَّح الجذر عند قارئ Mashru: «كتب» (مرشَّح لا هويّة ؛ المزيد والأدوات لا تُميَّز بعد) | مقيس | qari: fakk_ramz على ثلاث خانات حواملها سالمة — نطاق معلَن  |
| ٢ — المدلول وحده | `madlul_W-f91733a1-000` | «كَتَبَ» ↔ مدلول `kataba_m` (haqiqa=1001) — المصدر OWNER_MUDAA (by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'})) | مطابَق | MADLUL_SOURCE=OWNER_MUDAA ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `makhzan_W-f91733a1-001` | المخزن باللفظ «الطالب»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-f91733a1-001` | «الطَّالِبُ» ↔ مدلول `talib_m` (haqiqa=1002) — المصدر OWNER_MUDAA (by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'})) | مطابَق | MADLUL_SOURCE=OWNER_MUDAA ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `makhzan_W-f91733a1-002` | المخزن (Mashru) باللفظ «الدرس»: 1 قول ؛ الأوّل: mutabaqa:الدرس:أثر — سند 936c68e0c2c6@2896932/PageV03P300/الدرس/قائل:صاحب العين | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `madlul_W-f91733a1-002` | «الدَّرْسَ» ↔ مدلول `dars_m` (haqiqa=1003) — المصدر OWNER_MUDAA (by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'})) | مطابَق | MADLUL_SOURCE=OWNER_MUDAA ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `tabaqa2_maani` | المدلولان في الإطار ، و`kataba_m.tim = true` (عَرَضٌ له زمان) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: فعل ماضٍ + فاعل + مفعول (كلاهما بأل) ← إطار Jisr.Mulhaqat.daraba مُختارٌ **تقديرًا** من النمط «fiil|ism(al)|ism(al)» (شاهد bimafulayn (Jisr/Utur.lean:1032)) | مقيس | اختيار الإطار من النمط (قسم + حركة الآخر ؛ المصدر MADLUL_QISM+SURFACE) — تقدير ؛ الحكم يُبرهَن في S7 شرطًا عليه (CONDITIONAL_ON_SELECTED_ITAR)  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_hukm` | حكم الإطار الثلاثي hukm3 = مرخَّص (.murakhkhas) ؛ ibtida3=true ؛ سلسلة الوصل [32, 72, 104, 67, 64, 11, 54, 105, 71, 68, 63, 80] | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_isnad` | الإسناد الدلالي: talib_m موضوعٌ ، قابليّة 1001 محمولٌ ، نسبة إسنادية | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_ajza` | أجزاء الجملة الصغرى بالرتبة: [.mahkum, .hakim] (محكوم ثمّ حاكم) | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_kalam` | كلامٌ يُستغنى به بالسكوت: true | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_zaman` | زمن الحدث عند المرساة: some .madi (بإزاحة -1 ساعة معلَنة) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_mawdi` | موضع الجملة نسبةً إلى «هنا»: ⟨0, 0, 0⟩ | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_thabat` | نقل المرساة والحدث معًا بساعة لا يغيّر الزمن (thabat_naql_arad) | مبرهن | lean rc=0 ؛ axioms=['propext', 'Quot.sound']  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-f91733a1-000 | كَتَبَ | كَ=32 تَ=72 بَ=104 ؛ قارئ Mashru: AGREE | `kataba_m` by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'}) ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |
| W-f91733a1-001 | الطَّالِبُ | طْ=67 طَ=64 اْ=11 لِ=54 بُ=105 ؛ قارئ Mashru: AGREE | `talib_m` by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'}) ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |
| W-f91733a1-002 | الدَّرْسَ | دْ=71 دَ=68 رْ=63 سَ=80 ؛ قارئ Mashru: AGREE | `dars_m` by-hussein/mudaat (imda={'man': 'FIXTURE_TEST', 'tarikh': '2026-10-25'}) ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_REQUESTED (--hokom غير مطلوب) |  |
| S4_MADLUL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-f91733a1-000:MADLUL_SOURCE=OWNER_MUDAA؛ W-f91733a1-001:MADLUL_SOURCE=OWNER_MUDAA؛ W-f91733a1-002:MADLUL_SOURCE=OWNER_MUDAA |
| S5_MAAN_ITAR | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | ITAR_SELECTED:Jisr.Mulhaqat.daraba ؛ المصدر MADLUL_QISM+SURFACE ؛ CONDITIONAL_ON_SELECTED_ITAR |
| S6_AQL | نعم | نعم | نعم | نعم | نعم | نعم | نعم | Mirsat ⟨0, ⟨0,0,0⟩⟩ و Arad .fiil 1001 (-1) .saa none — افتراضات معلَنة (ت3/ت4/ت5 من الشاهد) | MIRSAT_DEFAULT_ASSUMED؛ ARAD_IZAHA_DEFAULT_ASSUMED؛ LAZIM_BY_FRAME_NOT_BY_TEXT |
| S7_BURHAN | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |

## ٤. البرهان (Lean)

```
PASS1_RC = 0 ؛ PASS2_RC = 0
OBSERVED = {"hukm3": ".murakhkhas", "ibtida3": "true", "silsila": "[32, 72, 104, 67, 64, 11, 54, 105, 71, 68, 63, 80]", "ajza": "[.mahkum, .hakim]", "yastaghni": "true", "zaman": "some .madi", "mawdi": "⟨0, 0, 0⟩"}
tabaqa1_kalimat    passed=True axioms=[]
tabaqa2_maani      passed=True axioms=[]
tabaqa3_hukm       passed=True axioms=['propext']
tabaqa3_isnad      passed=True axioms=[]
tabaqa4_ajza       passed=True axioms=['propext']
tabaqa4_kalam      passed=True axioms=['propext']
tabaqa4_zaman      passed=True axioms=[]
tabaqa4_mawdi      passed=True axioms=[]
tabaqa4_thabat     passed=True axioms=['propext', 'Quot.sound']
FILES = {"pass1": "1a9cb1cf14fd29c9f9c84b546d2ed9b3a1b5d015c94b0f30b5e6a6139bdb21ac", "pass2": "1b7754fb116898e7bf4b035bb17efea50e58f57c8a42b6d5ea21e5d3a537c685"}
```

## ٥. ما لا يُدَّعى

- لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.
- المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.
- أنواع الجمل المنفَّذة في هذه الأداة: [فعل ماضٍ + فاعل معرَّف بأل] و [فعل ماضٍ + فاعل منوَّن] فقط ؛ ما عداها OUT_OF_EXECUTED_PATH.
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.
- اختيار الإطار (CONDITIONAL_ON_SELECTED_ITAR): الإطار مُختارٌ تقديرًا من النمط لا محسومًا من Mashru ؛ الحكم مشروطٌ به ؛ تعدّد الأنماط يُعرَض ولا يُرجَّح.

## ٦. هوية التشغيل
```
mashru_root = /Users/husseinhiyassat/mashru
mashru_head = 7a902672a330c61ff1bade2de1414bec9934eaaa
mashru_tree_clean = False
mashru_status_porcelain = M by-hussein/tabaqat4/run.py
 M by-hussein/tabaqat4/t4/core.py
 M by-hussein/tabaqat4/tests/test_tabaqat4.py
?? by-hussein/mudaat/
?? by-hussein/tabaqat4/_runs_samples/c02_mudaat_fixture/
?? by-hussein/tabaqat4/mudaat_prep.py
?? by-hussein/tabaqat4/t4/itar_map.json
?? by-hussein/tabaqat4/tests/fixtures/
lean_toolchain = leanprover/lean4:v4.34.1
qamus_sha256 = e8662a21d29bfe8b0a1fe38d5b9a724bb6f43e60ef3d57770e721d8f8a5b6b20
  de985e5dc22af7d6  .probe/taqrir.json
  8d65f3d3687bf373  .probe/taqrir.md
  360ae7218775e45f  .probe2/taqrir.json
  4f8f1ed737fe6d0c  .probe2/taqrir.md
  9037019c41395f78  .probe3/s1/taqrir.json
  3f90c6f4fa81f710  .probe3/s1/taqrir.md
  f5f95c91bae45479  .probe3/s2/taqrir.json
  d78a04bbf927c397  .probe3/s2/taqrir.md
  d79658ffd610b631  README.md
  7bc9b2c5fb95ed87  TAQRIR_TASLIM.md
  9bfe0fd7fbeb82d3  _runs_samples/a/taqrir.json
  3b09a7123fe28090  _runs_samples/a/taqrir.md
  b48cae0c87c2d50f  _runs_samples/b/taqrir.json
  ccd354ab3c877df9  _runs_samples/b/taqrir.md
  f9ead96b162ef318  _runs_samples/c/taqrir.json
  17a3d7efc2b5e992  _runs_samples/c/taqrir.md
  004b78e048c32207  _runs_samples/e/taqrir.json
  d426e555157e1287  _runs_samples/e/taqrir.md
  18fdbbe78ce6d566  _runs_samples/f/taqrir.json
  eb416e28e51b9d30  _runs_samples/f/taqrir.md
  888a5fdc898eb1f9  _runs_samples/hokom_dhahaba/taqrir.json
  7556fdb769ed4ca4  _runs_samples/hokom_dhahaba/taqrir.md
  82e43798dea870f1  _runs_samples/hokom_jaza/taqrir.json
  5944f11393085bf1  _runs_samples/hokom_jaza/taqrir.md
  2d6411a73c177bb1  _runs_samples/hokom_split/s1/taqrir.json
  8015fc6b8f9daf83  _runs_samples/hokom_split/s1/taqrir.md
  29a06c8880c9d751  _runs_samples/hokom_split/s2/taqrir.json
  3a78eda9458d2c3d  _runs_samples/hokom_split/s2/taqrir.md
  0ed16ed1e9bbd688  _runs_samples/hokom_split/s3/taqrir.json
  dcb6fc2d91a58fa4  _runs_samples/hokom_split/s3/taqrir.md
  8baee02ae514993a  _runs_samples/j1/taqrir.json
  680ebabcf5d2af69  _runs_samples/j1/taqrir.md
  c22fbfcbf53b44bb  _runs_samples/j2/taqrir.json
  2203715078a615db  _runs_samples/j2/taqrir.md
  f2960748511e6b92  hokom_adapter.example.py
  ce0ef76c15a6f38f  hokom_adapter.py
  ad1e0638ae88b80a  mudaat_prep.py
  4c9d37d924c460d1  run.py
  e3b0c44298fc1c14  t4/__init__.py
  a938082db362c6d4  t4/core.py
  52e44fb0ea84e9d2  t4/dal.py
  562584d2506ede05  t4/forms_map.json
  ad73696a12c57518  t4/itar_map.json
  e8662a21d29bfe8b  t4/qamus.json
  841d73f7a5f34fa7  t4/qari.py
  628ad9744fe6080e  t4/report.py
  f06c2b1b46cdad96  tests/fixtures/mudaat_2noun.json
  31ff59b2f8b560ae  tests/fixtures/mudaat_collision.json
  6e4d2df940a8c1aa  tests/fixtures/mudaat_pending.json
  ac41ad56e418a318  tests/fixtures/mudaat_t21.json
  a39b69174c820217  tests/fixtures/mudaat_test.json
  fc6a3eb0caf583fb  tests/fixtures/taaqol_c02.json
  e21d48f1acc0977c  tests/fixtures/taaqol_conflict.json
  a593628c9fa63428  tests/test_tabaqat4.py
timestamp_utc = 2026-10-25T20:48:34.975948+00:00
```
