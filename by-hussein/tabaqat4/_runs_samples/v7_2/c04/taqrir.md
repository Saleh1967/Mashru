# Tabaqat4 — «جَلَسَ الرَّجُلُ عِنْدَهُ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 2bd2f00f588d76c294801b2784c3f5bca56a59e2f1d9527448e57b08dfb7f501
CODEPOINTS        = 25 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = 41972275fcbdcbdd150c374c39dc5ec3075d81a6 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:NOT_REACHED | ط4:NOT_REACHED
HUKM3             = None
WASM_SUMMARY      = مطابَق=4 ، مفحوص=1 ، مقيس=1 ، تقدير=4 ، بلا رتبة=4
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-2bd2f00f-000` | تقدير Hokom لـ«جَلَسَ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_PAST', 'final_root': ['ج', 'ل', 'س'], 'final_wazn': 'FA_A_LA', 'mood': 'NOT_APPLICABLE', 'directive': 'ACCEPT', 'lemma_surface': 'جَلَسَ', 'active_residuals': ['bab:mujarrad:imperfect_vowel_not_known', 'sami3i_required', 'transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-2bd2f00f-001` | تقدير Hokom لـ«الرَّجُلُ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'DEFER', 'lemma_surface': None, 'active_residuals': ['defer:root:root_path_not_opened_by_pre_root', 'defer:wazn:no_hypothesis_built', 'final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-2bd2f00f-002` | تقدير Hokom لـ«عِنْدَهُ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': ['ع', 'ن', 'د'], 'final_wazn': 'FI3L', 'mood': None, 'directive': 'ACCEPT', 'lemma_surface': None, 'active_residuals': ['bab:nominal:not_applicable', 'non_verbal_wazn']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-2bd2f00f-000` | «جَلَسَ»: 3 خلية [جَ=36, لَ=52, سَ=80] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-2bd2f00f-001` | «الرَّجُلُ»: 4 خلية [رْ=63, رَ=60, جُ=37, لُ=53] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-2bd2f00f-002` | «عِنْدَهُ»: 4 خلية [عِ=14, نْ=59, دَ=68, هُ=5] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [36, 52, 80, 63, 60, 37, 53, 116, 14, 59, 68, 5] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ٢ — المدلول وحده | `makhzan_W-2bd2f00f-000` | المخزن باللفظ «جلس»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `jidhr_W-2bd2f00f-000` | مرشَّح الجذر عند قارئ Mashru: «جلس» (مرشَّح لا هويّة ؛ المزيد والأدوات لا تُميَّز بعد) | مقيس | qari: fakk_ramz على ثلاث خانات حواملها سالمة — نطاق معلَن  |
| ٢ — المدلول وحده | `madlul_W-2bd2f00f-000` | «جَلَسَ» ↔ مدلول `d6_HFN_E_0f297baeea_V` (haqiqa=392431) — المصدر OWNER_MUDAA (by-hussein/mudaat (imda={'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18', 'hfn_sha256': '975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3', 'tarikh': '2026-10-28'})) | مطابَق | MADLUL_SOURCE=OWNER_MUDAA ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `makhzan_W-2bd2f00f-001` | المخزن (Mashru) باللفظ «الرجل»: 11 قول ؛ الأوّل: mutabaqa:الرجل:ولدا — سند 936c68e0c2c6@483390/PageV01P237/الرجل/قائل:غيره | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `madlul_W-2bd2f00f-001` | «الرَّجُلُ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |
| ٢ — المدلول وحده | `makhzan_W-2bd2f00f-002` | المخزن باللفظ «عنده»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-2bd2f00f-002` | «عِنْدَهُ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-2bd2f00f-000 | جَلَسَ | جَ=36 لَ=52 سَ=80 ؛ قارئ Mashru: AGREE | `d6_HFN_E_0f297baeea_V` by-hussein/mudaat (imda={'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18', 'hfn_sha256': '975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3', 'tarikh': '2026-10-28'}) ؛ بلا مودَع معلَن | NOT_REACHED | NOT_REACHED |
| W-2bd2f00f-001 | الرَّجُلُ | رْ=63 رَ=60 جُ=37 لُ=53 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |
| W-2bd2f00f-002 | عِنْدَهُ | عِ=14 نْ=59 دَ=68 هُ=5 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| جَلَسَ | FI3L/VERBAL_PAST | ['ج', 'ل', 'س'] | FA_A_LA | bab:mujarrad:imperfect_vowel_not_known؛ sami3i_required؛ transitivity_unknown؛ root_class_unknown | جلس | AGREE |
| الرَّجُلُ | ISM/LEXICAL_NOUN | None | None | defer:root:root_path_not_opened_by_pre_root؛ defer:wazn:no_hypothesis_built؛ final_root:null؛ final_wazn:null | — | — |
| عِنْدَهُ | ISM/LEXICAL_NOUN | ['ع', 'ن', 'د'] | FI3L | bab:nominal:not_applicable؛ non_verbal_wazn | — | ONE_SIDED |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | نعم | نعم | لا | نعم | لا | كلمة أو أكثر بلا مدلول ← المسار الإسناديّ (S5) لا يُبنى | W-2bd2f00f-000:MADLUL_SOURCE=OWNER_MUDAA؛ W-2bd2f00f-001:NO_SEALED_MADLUL؛ W-2bd2f00f-002:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | لا | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | OUT_OF_EXECUTED_PATH:جملة من 3 كلمات (المغلَّف: كلمتان) + PREREQ_MISSING: مدلولٌ أو خلايا ناقصة | OUT_OF_EXECUTED_PATH |
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
mashru_head = 41972275fcbdcbdd150c374c39dc5ec3075d81a6
mashru_tree_clean = False
mashru_status_porcelain = M by-hussein/mudaat/D6_COVERAGE.md
 M by-hussein/mudaat/MUDAAT_IMDA.md
 M by-hussein/mudaat/Mudaat.lean
 M by-hussein/mudaat/madlulat_export.tsv
 M by-hussein/mudaat/mudaat.json
 M by-hussein/tabaqat4/mudaat_prep.py
 M by-hussein/tabaqat4/t4/hfn_d6.py
?? by-hussein/mudaat/HOKOM_REPAIR_LIST.md
?? by-hussein/tabaqat4/_runs_samples/v7_2/
?? by-hussein/tabaqat4/corpus/
?? by-hussein/tabaqat4/scripts/
?? by-hussein/tabaqat4/t4/lookup_norm.json
?? by-hussein/tabaqat4/t4/wazn_to_form.json
?? prompts/
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
  ba813dbfaca1f8f4  TAQRIR_TASLIM.md
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
  57c8b323965995b9  _runs_samples/v7_2/c01/taqrir.json
  887e3466c782de7f  _runs_samples/v7_2/c01/taqrir.md
  6f2dcd9f8ca258fd  _runs_samples/v7_2/c02/taqrir.json
  1db58b67d392a55b  _runs_samples/v7_2/c02/taqrir.md
  3525f4bdb48a70fe  _runs_samples/v7_2/c03/taqrir.json
  e9a46f652c036c5c  _runs_samples/v7_2/c03/taqrir.md
  5c52091b16d75a79  _runs_samples/v7_c01/taqrir.json
  2e16b605328d15ad  _runs_samples/v7_c01/taqrir.md
  84ac83b07df3f757  _runs_samples/v7_c02/taqrir.json
  f6a13bb17e412eb9  _runs_samples/v7_c02/taqrir.md
  fb26f7d6fa6123f6  _runs_samples/v7_c03/taqrir.json
  465d6d2b82067631  _runs_samples/v7_c03/taqrir.md
  5f182609366697a4  _runs_samples/v7_c04/taqrir.json
  cbe6061882974b9e  _runs_samples/v7_c04/taqrir.md
  4ba9704510a09795  _runs_samples/v7_c05/taqrir.json
  a2baa0413b3926d6  _runs_samples/v7_c05/taqrir.md
  da25f1ec298fb81a  _runs_samples/v7_c06/taqrir.json
  95add5dc217ba48f  _runs_samples/v7_c06/taqrir.md
  f7a3f17dbac4ba06  _runs_samples/v7_c07/taqrir.json
  b70ba70fe5006c1a  _runs_samples/v7_c07/taqrir.md
  f2960748511e6b92  hokom_adapter.example.py
  661b835aaa96aff7  hokom_adapter.py
  e8b925ad401bcafc  mudaat_prep.py
  4c9d37d924c460d1  run.py
  46300c4604fcc2ea  scripts/v7_2_report.py
  e3b0c44298fc1c14  t4/__init__.py
  5b6da43bdb772d1a  t4/core.py
  9779a99c83029d71  t4/dal.py
  562584d2506ede05  t4/forms_map.json
  89fd39a9fda48fe4  t4/hfn_d6.py
  b1ada070c207a3d8  t4/hfn_map.json
  055a7405e75fe226  t4/itar_map.json
  0613d24f3568fb37  t4/lookup_norm.json
  d4207798fd61ea2d  t4/mushtaq_awzan.json
  e8662a21d29bfe8b  t4/qamus.json
  841d73f7a5f34fa7  t4/qari.py
  628ad9744fe6080e  t4/report.py
  0b5042fe24be9353  t4/wazn_to_form.json
  f06c2b1b46cdad96  tests/fixtures/mudaat_2noun.json
  31ff59b2f8b560ae  tests/fixtures/mudaat_collision.json
  6e4d2df940a8c1aa  tests/fixtures/mudaat_pending.json
  ac41ad56e418a318  tests/fixtures/mudaat_t21.json
  a39b69174c820217  tests/fixtures/mudaat_test.json
  fc6a3eb0caf583fb  tests/fixtures/taaqol_c02.json
  e21d48f1acc0977c  tests/fixtures/taaqol_conflict.json
  225125ed35cfec82  tests/test_conformance.py
  24bc704541437f8a  tests/test_tabaqat4.py
timestamp_utc = 2026-10-28T12:14:29.687799+00:00
```
