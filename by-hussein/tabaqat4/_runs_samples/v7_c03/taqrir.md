# Tabaqat4 — «الْعِلْمُ نُورٌ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 6999132cfbd2e7d7745e7790e4c801476193038931b74e704a238830bdb213b1
CODEPOINTS        = 15 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = d01309acac7ead03a18783237c9c4c1896a00ffb ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:NOT_REACHED | ط4:NOT_REACHED
HUKM3             = None
WASM_SUMMARY      = مطابَق=2 ، مفحوص=2 ، تقدير=3 ، بلا رتبة=3
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-6999132c-000` | تقدير Hokom لـ«الْعِلْمُ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': ['ع', 'ل', 'م'], 'final_wazn': 'FI3L', 'mood': None, 'directive': 'ACCEPT', 'lemma_surface': None, 'active_residuals': ['defer:bab:nominal_morphology_path', 'non_verbal_wazn']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-6999132c-001` | تقدير Hokom لـ«نُورٌ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'lemma_surface': None, 'active_residuals': ['defer:root:hollow_underlying_radical_unresolved', 'defer:wazn:no_hypothesis_built', 'final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-6999132c-000` | «الْعِلْمُ»: 4 خلية [لْ=55, عِ=14, لْ=55, مُ=109] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-6999132c-001` | «نُورٌ»: 4 خلية [نُ=57, وْ=115, ر◌ُ=61, نْ(تنوين)=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_W-6999132c-001` | قارئ Mashru يقرأ «نُورٌ» = [57, 115, 63] ≠ الجدول [57, 115, 61, 59] — WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) | مفحوص | مخرج qari (تنفيذ Mashru) ؛ الاختلاف يُعرَض ولا يُحسَم  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [0, 55, 14, 55, 109, 116, 57, 115, 63] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ٢ — المدلول وحده | `makhzan_W-6999132c-000` | المخزن (Mashru) باللفظ «العلم»: 4 قول ؛ الأوّل: mutabaqa:العلم:نقيض الجهل — سند 936c68e0c2c6@527055/PageV01P257/العلم/قائل:بلا نسبة صريحة | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `madlul_W-6999132c-000` | «الْعِلْمُ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |
| ٢ — المدلول وحده | `makhzan_W-6999132c-001` | المخزن باللفظ «نور»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-6999132c-001` | «نُورٌ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-6999132c-000 | الْعِلْمُ | لْ=55 عِ=14 لْ=55 مُ=109 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |
| W-6999132c-001 | نُورٌ | نُ=57 وْ=115 ر◌ُ=61 نْ(تنوين)=59 ؛ قارئ Mashru: DISAGREE (WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة)) | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| الْعِلْمُ | ISM/LEXICAL_NOUN | ['ع', 'ل', 'م'] | FI3L | defer:bab:nominal_morphology_path؛ non_verbal_wazn | — | ONE_SIDED |
| نُورٌ | ISM/LEXICAL_NOUN | None | None | defer:root:hollow_underlying_radical_unresolved؛ defer:wazn:no_hypothesis_built؛ final_root:null؛ final_wazn:null | — | — |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-6999132c-001:QARI_DISAGREE:WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | لا | نعم | لا | نعم | لا | كلمة أو أكثر بلا مدلول ← المسار الإسناديّ (S5) لا يُبنى | W-6999132c-000:NO_SEALED_MADLUL؛ W-6999132c-001:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | لا | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | OUT_OF_EXECUTED_PATH:جملة اسمية (تقديرًا من السطح: أوّلها اسمٌ بأل أو تنوين) + PREREQ_MISSING: مدلولٌ أو خلايا ناقصة | OUT_OF_EXECUTED_PATH |
| S6_AQL | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | PREREQ_MISSING (S5 لم يُنتج إطارًا) |  |
| S7_BURHAN | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | PREREQ_MISSING (S5 لم يُنتج إطارًا) |  |

## ٥. ما لا يُدَّعى

- لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.
- المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.
- الأطر المنفَّذة في هذه الأداة (itar_map): [فعل+فاعل بأل]→darabaZayd ، [فعل+فاعل منوَّن]→jaaRajul ، [فعل+فاعل+مفعول بأل]→daraba ، وباب الجزاء ؛ ما عداها OUT_OF_EXECUTED_PATH باسم نمطه (ITAR_UNMAPPED).
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.
- MUDAAT_UNSEALED: بصمةُ mudaat.json ليست في mudaat/sijill.json — لا يُولَّد منه Mudaat.lean حتى يختمه المالك (B4)

## ٦. هوية التشغيل
```
mashru_root = /Users/husseinhiyassat/mashru
mashru_head = d01309acac7ead03a18783237c9c4c1896a00ffb
mashru_tree_clean = False
mashru_status_porcelain = M by-hussein/.gitignore
 M by-hussein/mudaat/D6_COVERAGE.md
 M by-hussein/mudaat/MUDAAT_IMDA.md
 M by-hussein/mudaat/Mudaat.lean
 M by-hussein/mudaat/mudaat.json
 M by-hussein/tabaqat4/hokom_adapter.py
 M by-hussein/tabaqat4/mudaat_prep.py
 M by-hussein/tabaqat4/t4/core.py
 M by-hussein/tabaqat4/t4/hfn_d6.py
 M by-hussein/tabaqat4/tests/test_tabaqat4.py
?? by-hussein/mudaat/IDAA_COMMANDS.md
?? by-hussein/mudaat/alam.json
?? by-hussein/mudaat/madlulat_export.tsv
?? by-hussein/tabaqat4/_runs_samples/v7_c01/
?? by-hussein/tabaqat4/_runs_samples/v7_c02/
?? by-hussein/tabaqat4/t4/mushtaq_awzan.json
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
  1c67ca32f3db8cde  T19_TARQIA.md
  a25c277cbce00c81  TAQRIR_TASLIM.md
  9bfe0fd7fbeb82d3  _runs_samples/a/taqrir.json
  3b09a7123fe28090  _runs_samples/a/taqrir.md
  b48cae0c87c2d50f  _runs_samples/b/taqrir.json
  ccd354ab3c877df9  _runs_samples/b/taqrir.md
  f9ead96b162ef318  _runs_samples/c/taqrir.json
  17a3d7efc2b5e992  _runs_samples/c/taqrir.md
  0319a20e37379bdb  _runs_samples/c02_mudaat_fixture/taqrir.json
  bcb2f60441aafb6b  _runs_samples/c02_mudaat_fixture/taqrir.md
  f613a3f9b2d90ec3  _runs_samples/c02_no_mudaat/taqrir.json
  af7760dcf9d98496  _runs_samples/c02_no_mudaat/taqrir.md
  4b1c485dfadfe8db  _runs_samples/c02_ratified_dr_hussein/taqrir.json
  6ae83c8b2284dd33  _runs_samples/c02_ratified_dr_hussein/taqrir.md
  38da79671e57c95e  _runs_samples/d6_c01/taqrir.json
  a6f17cea4fb2f789  _runs_samples/d6_c01/taqrir.md
  b15b82935d80ea52  _runs_samples/d6_c02/taqrir.json
  d9809ec176d5de35  _runs_samples/d6_c02/taqrir.md
  df090cfc0561f618  _runs_samples/d6_c03/taqrir.json
  d163d6dee071e01b  _runs_samples/d6_c03/taqrir.md
  0f124441de0fe6c1  _runs_samples/d6_c04/taqrir.json
  9de712bb52ada58f  _runs_samples/d6_c04/taqrir.md
  60575e8eaed0ce15  _runs_samples/d6_c05/taqrir.json
  5070f6910ddc46c0  _runs_samples/d6_c05/taqrir.md
  a7e1240ff23e9dd8  _runs_samples/d6_c06/taqrir.json
  ba24d6f06569183e  _runs_samples/d6_c06/taqrir.md
  df40c21e76b6dfef  _runs_samples/d6_c07/taqrir.json
  389a7565b7b2c5aa  _runs_samples/d6_c07/taqrir.md
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
  5c52091b16d75a79  _runs_samples/v7_c01/taqrir.json
  2e16b605328d15ad  _runs_samples/v7_c01/taqrir.md
  84ac83b07df3f757  _runs_samples/v7_c02/taqrir.json
  f6a13bb17e412eb9  _runs_samples/v7_c02/taqrir.md
  f2960748511e6b92  hokom_adapter.example.py
  661b835aaa96aff7  hokom_adapter.py
  f95e0cb858b7ff89  mudaat_prep.py
  4c9d37d924c460d1  run.py
  e3b0c44298fc1c14  t4/__init__.py
  5b6da43bdb772d1a  t4/core.py
  9779a99c83029d71  t4/dal.py
  562584d2506ede05  t4/forms_map.json
  dd01969ae988cb19  t4/hfn_d6.py
  b1ada070c207a3d8  t4/hfn_map.json
  055a7405e75fe226  t4/itar_map.json
  d4207798fd61ea2d  t4/mushtaq_awzan.json
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
  225125ed35cfec82  tests/test_conformance.py
  25964755808800fd  tests/test_tabaqat4.py
timestamp_utc = 2026-10-28T04:28:42.776989+00:00
```
