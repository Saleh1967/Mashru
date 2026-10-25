# Tabaqat4 — «إِنْ تَجْتَهِدْ تَنْجَحْ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = d07e6c1b7ad261545a1b4476ac645343686cc92a491dfbbee83aedacec7cefad
CODEPOINTS        = 24 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = ed7c5d3248a123945cfa3e8901a39f7f9ecdf394 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:مبرهن على الشاهد | ط4:NOT_APPLICABLE
HUKM3             = .maqbul
WASM_SUMMARY      = مبرهن على الشاهد=2 ، مطابَق=3 ، مفحوص=1 ، مقيس=1 ، تقدير=3 ، بلا رتبة=6
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-000` | تقدير Hokom لـ«إِنْ»: {'pin': '8a23298076b4', 'word_class': 'HARF', 'word_class_subclass': 'CLOSED_FUNCTION_WORD', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'active_residuals': ['final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-001` | تقدير Hokom لـ«تَجْتَهِدْ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_IMPERFECT', 'final_root': ['ج', 'ه', 'د'], 'final_wazn': 'IFTA3ALA', 'mood': 'JUSSIVE', 'directive': 'ACCEPT', 'active_residuals': ['transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-d07e6c1b-002` | تقدير Hokom لـ«تَنْجَحْ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_IMPERFECT', 'final_root': ['ن', 'ج', 'ح'], 'final_wazn': None, 'mood': 'JUSSIVE', 'directive': 'ACCEPT', 'active_residuals': ['defer:wazn:unlicensed_but_structural_augment', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-000` | «إِنْ»: 2 خلية [إِ=2, نْ=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-001` | «تَجْتَهِدْ»: 5 خلية [تَ=72, جْ=39, تَ=72, هِ=6, دْ=71] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-d07e6c1b-002` | «تَنْجَحْ»: 4 خلية [تَ=72, نْ=59, جَ=36, حْ=19] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [2, 59, 116, 72, 39, 72, 6, 71, 116, 72, 59, 36, 19] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-000` | المخزن باللفظ «إن»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-000` | «إِنْ»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به) |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-001` | المخزن باللفظ «تجتهد»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-001` | «تَجْتَهِدْ»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به) |
| ٢ — المدلول وحده | `makhzan_W-d07e6c1b-002` | المخزن باللفظ «تنجح»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-d07e6c1b-002` | «تَنْجَحْ»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به) |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: شرطية ، الأداة «إن» ، الشرط أوّلًا ؛ الصيغتان: شرط=mudariMajzum ، جواب=mudariMajzum ، لام القسم=false | مقيس | الأداة من قائمة BabJaza الحاصرة (مقيس) ؛ مصدر الصيغتين: HOKOM_TAQDIR (رتبتها تقدير) ؛ الحكم يُبرهَن في S7 مشروطًا بهما  |
| ٣ — معًا (الإطار والحكم) | `jaza_sinf` | صنف الأداة «إن» عند سيبويه (sinfOf): .jaza | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |
| ٣ — معًا (الإطار والحكم) | `jaza_hukm` | حكم باب الجزاء: في الكلام مقبول ، في الشعر مقبول — على الصيغتَين المعطاتَين | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-d07e6c1b-000 | إِنْ | إِ=2 نْ=59 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |
| W-d07e6c1b-001 | تَجْتَهِدْ | تَ=72 جْ=39 تَ=72 هِ=6 دْ=71 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |
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
| S4_MADLUL | نعم | نعم | لا | نعم | لا | نعم | لا | لا مدلول بنيويّ لكلمة أو أكثر ؛ لا يمنع باب الجزاء (S5-ج يحكم على صورة الجملة لا على المدلول) | W-d07e6c1b-000:NO_SEALED_MADLUL؛ W-d07e6c1b-001:NO_SEALED_MADLUL؛ W-d07e6c1b-002:NO_SEALED_MADLUL |
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
- أنواع الجمل المنفَّذة في هذه الأداة: [فعل ماضٍ + فاعل معرَّف بأل] و [فعل ماضٍ + فاعل منوَّن] فقط ؛ ما عداها OUT_OF_EXECUTED_PATH.
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.
- في باب الجزاء: صورتا فعل الشرط والجواب مُعطاتان من المالك (--forms) لا مقروءتان من السطح ؛ البرهان مشروط بهما ، وقراءة الصورة من السطح تنتظر مُنتِجًا (Hokom) برتبة تقدير.

## ٦. هوية التشغيل
```
mashru_root = /Users/husseinhiyassat/mashru
mashru_head = ed7c5d3248a123945cfa3e8901a39f7f9ecdf394
mashru_tree_clean = False
mashru_status_porcelain = M by-hussein/tabaqat4/run.py
 M by-hussein/tabaqat4/t4/core.py
 M by-hussein/tabaqat4/t4/report.py
 M by-hussein/tabaqat4/tests/test_tabaqat4.py
?? by-hussein/tabaqat4/.probe/
?? by-hussein/tabaqat4/.probe2/
?? by-hussein/tabaqat4/.probe3/
?? by-hussein/tabaqat4/_runs_samples/hokom_dhahaba/
?? by-hussein/tabaqat4/_runs_samples/hokom_jaza/
?? by-hussein/tabaqat4/hokom_adapter.py
?? by-hussein/tabaqat4/t4/forms_map.json
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
  88db76563189cf36  TAQRIR_TASLIM.md
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
  8baee02ae514993a  _runs_samples/j1/taqrir.json
  680ebabcf5d2af69  _runs_samples/j1/taqrir.md
  c22fbfcbf53b44bb  _runs_samples/j2/taqrir.json
  2203715078a615db  _runs_samples/j2/taqrir.md
  f2960748511e6b92  hokom_adapter.example.py
  ce0ef76c15a6f38f  hokom_adapter.py
  8b4438a1eacdc7f2  run.py
  e3b0c44298fc1c14  t4/__init__.py
  dd173d0217a4c2b9  t4/core.py
  52e44fb0ea84e9d2  t4/dal.py
  562584d2506ede05  t4/forms_map.json
  e8662a21d29bfe8b  t4/qamus.json
  841d73f7a5f34fa7  t4/qari.py
  628ad9744fe6080e  t4/report.py
  2222d7c33950f7f7  tests/test_tabaqat4.py
timestamp_utc = 2026-10-25T05:14:29.784180+00:00
```
