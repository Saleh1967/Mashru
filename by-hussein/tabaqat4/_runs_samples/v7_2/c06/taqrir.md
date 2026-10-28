# Tabaqat4 — «إِنْ تَجْتَهِدْ تَنْجَحْ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = d07e6c1b7ad261545a1b4476ac645343686cc92a491dfbbee83aedacec7cefad
CODEPOINTS        = 24 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = 41972275fcbdcbdd150c374c39dc5ec3075d81a6 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:مبرهن على الشاهد | ط4:NOT_APPLICABLE
HUKM3             = .maqbul
WASM_SUMMARY      = مبرهن على الشاهد=2 ، مطابَق=4 ، مفحوص=1 ، مقيس=1 ، تقدير=3 ، بلا رتبة=5
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-000` | تقدير Hokom لـ«إِنْ»: {'pin': '8a23298076b4', 'word_class': 'HARF', 'word_class_subclass': 'CLOSED_FUNCTION_WORD', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'lemma_surface': None, 'active_residuals': ['final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-001` | تقدير Hokom لـ«تَجْتَهِدْ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_IMPERFECT', 'final_root': ['ج', 'ه', 'د'], 'final_wazn': 'IFTA3ALA', 'mood': 'JUSSIVE', 'directive': 'ACCEPT', 'lemma_surface': None, 'active_residuals': ['transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-002` | تقدير Hokom لـ«تَنْجَحْ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_IMPERFECT', 'final_root': ['ن', 'ج', 'ح'], 'final_wazn': None, 'mood': 'JUSSIVE', 'directive': 'ACCEPT', 'lemma_surface': 'نَجَحَ', 'active_residuals': ['defer:wazn:unlicensed_but_structural_augment', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-000` | «إِنْ»: 2 خلية [إِ=2, نْ=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-001` | «تَجْتَهِدْ»: 5 خلية [تَ=72, جْ=39, تَ=72, هِ=6, دْ=71] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-002` | «تَنْجَحْ»: 4 خلية [تَ=72, نْ=59, جَ=36, حْ=19] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [2, 59, 116, 72, 39, 72, 6, 71, 116, 72, 59, 36, 19] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-000` | المخزن باللفظ «إن»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-000` | «إِنْ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-001` | المخزن باللفظ «تجتهد»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-001` | «تَجْتَهِدْ» ↔ مدلول `d6_HFN_E_e74708657a_V` (haqiqa=335660) — المصدر OWNER_MUDAA (by-hussein/mudaat (imda={'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18', 'hfn_sha256': '975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3', 'tarikh': '2026-10-28'})) | مطابَق | MADLUL_SOURCE=OWNER_MUDAA ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-002` | المخزن باللفظ «تنجح»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-002` | «تَنْجَحْ»: لا مدلولَ بنيويًّا (SLGE.Madlul) — لا في qamus (شواهد Mashru) ولا في مودَعات RATIFIED | **بلا رتبة** |  — NO_SEALED_MADLUL: لا يُولَّد ؛ يدخل بمودَعٍ أمضاه المالك (D5) أو شاهد Mashru |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: شرطية ، الأداة «إن» ، الشرط أوّلًا ؛ الصيغتان: شرط=mudariMajzum ، جواب=mudariMajzum ، لام القسم=false | مقيس | الأداة من قائمة BabJaza الحاصرة (مقيس) ؛ مصدر الصيغتين: HOKOM_TAQDIR (رتبتها تقدير) ؛ الحكم يُبرهَن في S7 مشروطًا بهما  |
| ٣ — معًا (الإطار والحكم) | `jaza_sinf` | صنف الأداة «إن» عند سيبويه (sinfOf): .jaza | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |
| ٣ — معًا (الإطار والحكم) | `jaza_hukm` | حكم باب الجزاء: في الكلام مقبول ، في الشعر مقبول — على الصيغتَين المعطاتَين | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-d07e6c1b-000 | إِنْ | إِ=2 نْ=59 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |
| W-d07e6c1b-001 | تَجْتَهِدْ | تَ=72 جْ=39 تَ=72 هِ=6 دْ=71 ؛ قارئ Mashru: AGREE | `d6_HFN_E_e74708657a_V` by-hussein/mudaat (imda={'man': 'DR_HUSSEIN', 'qanun': 'D6', 'hfn_release': 'release_v18', 'hfn_sha256': '975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3', 'tarikh': '2026-10-28'}) ؛ بلا مودَع معلَن | مبرهن على الشاهد | NOT_APPLICABLE |
| W-d07e6c1b-002 | تَنْجَحْ | تَ=72 نْ=59 جَ=36 حْ=19 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| إِنْ | HARF/CLOSED_FUNCTION_WORD | None | None | final_root:null؛ final_wazn:null | — | — |
| تَجْتَهِدْ | FI3L/VERBAL_IMPERFECT | ['ج', 'ه', 'د'] | IFTA3ALA | transitivity_unknown؛ root_class_unknown | — | ONE_SIDED |
| تَنْجَحْ | FI3L/VERBAL_IMPERFECT | ['ن', 'ج', 'ح'] | None | defer:wazn:unlicensed_but_structural_augment؛ final_wazn:null | — | ONE_SIDED |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | نعم | نعم | لا | نعم | لا | لا مدلول بنيويّ لكلمة أو أكثر ؛ لا يمنع باب الجزاء (S5-ج يحكم على صورة الجملة لا على المدلول) | W-d07e6c1b-000:NO_SEALED_MADLUL؛ W-d07e6c1b-001:MADLUL_SOURCE=OWNER_MUDAA؛ W-d07e6c1b-002:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | FORMS_SOURCE:HOKOM_TAQDIR؛ FORMS_FROM_HOKOM_TAQDIR: صورتا الفعلَين تقديرٌ من Hokom (لا يُستهلَك إلّا هنا مقعدًا معلَنًا) ؛ la_yuddaa |
| S6_AQL | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_APPLICABLE: باب الجزاء يحكم على صورة الجملة (كلام/شعر) ولا يبني Itar3 ولا Aql.Jumla ؛ لا طبقة رابعة له في Mashru | AQL_NOT_DEFINED_FOR_JAZA |
| S7_BURHAN | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  | CONDITIONAL_ON_SUPPLIED_FORMS: البرهان على الحكم مشروطٌ بصيغتَي الشرط والجواب المعطاتَين |

## ٤. البرهان (Lean)

```
PASS1_RC = 0 ؛ PASS2_RC = 0
OBSERVED = {"kalam": ".maqbul", "shir": ".maqbul", "sinf": ".jaza"}
jaza_hukm          passed=True axioms=[]
jaza_sinf          passed=True axioms=[]
FILES = {"pass1": "2c571ff3abecbd6e505c792371abdd8052de3c1c38984658f70c0329232596dc", "pass2": "0e39c11d854229167082e600d264bc8fcedda741cdaeb7383746536f9d83f39e"}
```

## ٥. ما لا يُدَّعى

- لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.
- المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.
- الأطر المنفَّذة في هذه الأداة (itar_map): [فعل+فاعل بأل]→darabaZayd ، [فعل+فاعل منوَّن]→jaaRajul ، [فعل+فاعل+مفعول بأل]→daraba ، وباب الجزاء ؛ ما عداها OUT_OF_EXECUTED_PATH باسم نمطه (ITAR_UNMAPPED).
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.
- MUDAAT_UNSEALED: بصمةُ mudaat.json ليست في mudaat/sijill.json — لا يُولَّد منه Mudaat.lean حتى يختمه المالك (B4)
- في باب الجزاء: صورتا فعل الشرط والجواب مُعطاتان من المالك (--forms) لا مقروءتان من السطح ؛ البرهان مشروط بهما ، وقراءة الصورة من السطح تنتظر مُنتِجًا (Hokom) برتبة تقدير.

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
  08973e667588e13a  _runs_samples/v7_2/c04/taqrir.json
  f493f0a4648b4c86  _runs_samples/v7_2/c04/taqrir.md
  773fa5d701c8fd2d  _runs_samples/v7_2/c05/taqrir.json
  4d2d36b23de3a12f  _runs_samples/v7_2/c05/taqrir.md
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
timestamp_utc = 2026-10-28T12:14:32.741131+00:00
```
