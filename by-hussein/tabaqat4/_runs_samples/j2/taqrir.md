# Tabaqat4 — «إِنْ تَجْتَهِدْ تَنْجَحُ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 05216315837875cd711787de8ef11a3a2383424155b85430184c6deb322e42bc
CODEPOINTS        = 24 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = d2533c39bb42b710248beebb0129f178fc7cbd76 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:مبرهن على الشاهد | ط4:NOT_APPLICABLE
HUKM3             = .qabih
WASM_SUMMARY      = مبرهن على الشاهد=2 ، مطابَق=3 ، مقيس=1 ، بلا رتبة=3
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ١ — الدالّ وحده | `dal_W-05216315-000` | «إِنْ»: 2 خلية [إِ=2, نْ=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-05216315-001` | «تَجْتَهِدْ»: 5 خلية [تَ=72, جْ=39, تَ=72, هِ=6, دْ=71] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-05216315-002` | «تَنْجَحُ»: 4 خلية [تَ=72, نْ=59, جَ=36, حُ=17] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ٢ — المدلول وحده | `madlul_W-05216315-000` | «إِنْ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |
| ٢ — المدلول وحده | `madlul_W-05216315-001` | «تَجْتَهِدْ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |
| ٢ — المدلول وحده | `madlul_W-05216315-002` | «تَنْجَحُ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: شرطية ، الأداة «إن» ، الشرط أوّلًا ؛ الصيغتان المعطاتان: شرط=mudariMajzum ، جواب=mudariMarfu ، لام القسم=false | مقيس | الأداة من قائمة BabJaza الحاصرة (مقيس) ؛ الصيغتان معطاتان (رأي) ؛ الحكم يُبرهَن في S7 مشروطًا بهما  |
| ٣ — معًا (الإطار والحكم) | `jaza_sinf` | صنف الأداة «إن» عند سيبويه (sinfOf): .jaza | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |
| ٣ — معًا (الإطار والحكم) | `jaza_hukm` | حكم باب الجزاء: في الكلام قبيح ، في الشعر مقبول — على الصيغتَين المعطاتَين | مبرهن على الشاهد | lean rc=0 ؛ axioms=[] ؛ مشروط بالصيغ المعطاة  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-05216315-000 | إِنْ | إِ=2 نْ=59 | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |
| W-05216315-001 | تَجْتَهِدْ | تَ=72 جْ=39 تَ=72 هِ=6 دْ=71 | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |
| W-05216315-002 | تَنْجَحُ | تَ=72 نْ=59 جَ=36 حُ=17 | NO_SEALED_MADLUL | مبرهن على الشاهد | NOT_APPLICABLE |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_REQUESTED (--hokom غير مطلوب) |  |
| S4_MADLUL | نعم | نعم | لا | نعم | لا | نعم | لا | كلمة أو أكثر بلا مدلول ← S5 لا يُبنى | W-05216315-000:NO_SEALED_MADLUL؛ W-05216315-001:NO_SEALED_MADLUL؛ W-05216315-002:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | FORMS_SUPPLIED_NOT_READ: صور الفعلَين معطاة من المالك لا مقروءة من السطح |
| S6_AQL | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_APPLICABLE: باب الجزاء يحكم على صورة الجملة (كلام/شعر) ولا يبني Itar3 ولا Aql.Jumla ؛ لا طبقة رابعة له في Mashru | AQL_NOT_DEFINED_FOR_JAZA |
| S7_BURHAN | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  | CONDITIONAL_ON_SUPPLIED_FORMS: البرهان على الحكم مشروطٌ بصيغتَي الشرط والجواب المعطاتَين |

## ٤. البرهان (Lean)

```
PASS1_RC = 0 ؛ PASS2_RC = 0
OBSERVED = {"kalam": ".qabih", "shir": ".maqbul", "sinf": ".jaza"}
jaza_hukm          passed=True axioms=[]
jaza_sinf          passed=True axioms=[]
FILES = {"pass1": "403fb5ed829f48fc40abec73991100906eb1c8f6a271ad3d7686d521b82f0884", "pass2": "0d3b4559e78f859b3895ec52b99bbbeaa38bd1354970337424e6a90bb059bd39"}
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
mashru_root = /tmp/claude-0/-home-claude/df1a9f35-ff1b-5bad-8e6d-f9f037af0cec/scratchpad/m
mashru_head = d2533c39bb42b710248beebb0129f178fc7cbd76
mashru_tree_clean = False
mashru_status_porcelain = ?? Shahid_Ahmad.lean
?? Shahid_Ahmad_T4.lean
?? jumla_kamila.json
lean_toolchain = leanprover/lean4:v4.34.1
qamus_sha256 = e8662a21d29bfe8b0a1fe38d5b9a724bb6f43e60ef3d57770e721d8f8a5b6b20
  00f8605e4007470e  README.md
  46a83fc6aab1969b  TAQRIR_TASLIM.md
  7c80bdec79ce67a9  _runs_samples/a/taqrir.json
  77dbb464e8b92d33  _runs_samples/a/taqrir.md
  b48cae0c87c2d50f  _runs_samples/b/taqrir.json
  ccd354ab3c877df9  _runs_samples/b/taqrir.md
  f9ead96b162ef318  _runs_samples/c/taqrir.json
  17a3d7efc2b5e992  _runs_samples/c/taqrir.md
  004b78e048c32207  _runs_samples/e/taqrir.json
  d426e555157e1287  _runs_samples/e/taqrir.md
  b07e7812be3909a4  _runs_samples/f/taqrir.json
  7ee9a3f8c8eacd1e  _runs_samples/f/taqrir.md
  f2960748511e6b92  hokom_adapter.example.py
  db220690335d14ef  run.py
  e3b0c44298fc1c14  t4/__init__.py
  25da699a3f28fa09  t4/core.py
  1c3a62d0977528ec  t4/dal.py
  e8662a21d29bfe8b  t4/qamus.json
  2593ad5e16f6c048  t4/report.py
  27052856c95f7e63  tests/test_tabaqat4.py
timestamp_utc = 2026-10-25T04:45:08.536075+00:00
```
