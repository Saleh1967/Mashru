# Tabaqat4 — «كَتَبَ الطَّالِبُ الدَّرْسَ.»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 2ebb32be5fcb5050c8615a34939d2aaeeeb9be24de30c19181eaa563dbce7425
CODEPOINTS        = 28 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = e4c801ffe9171dadedcc3aae23051ea0953ae361 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = 964538402a4e2f52…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:NOT_REACHED | ط4:NOT_REACHED
WASM_SUMMARY      = مطابَق=3 ، بلا رتبة=3
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ١ — الدالّ وحده | `dal_W-2ebb32be-000` | «كَتَبَ»: 3 خلية [كَ=32, تَ=72, بَ=104] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-2ebb32be-001` | «الطَّالِبُ»: 5 خلية [طْ=67, طَ=64, اْ=11, لِ=54, بُ=105] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-2ebb32be-002` | «الدَّرْسَ»: 4 خلية [دْ=71, دَ=68, رْ=63, سَ=80] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ٢ — المدلول وحده | `madlul_W-2ebb32be-000` | «كَتَبَ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |
| ٢ — المدلول وحده | `madlul_W-2ebb32be-001` | «الطَّالِبُ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |
| ٢ — المدلول وحده | `madlul_W-2ebb32be-002` | «الدَّرْسَ»: لا مدلولَ معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: الكلمة ليست في qamus.json المقيَّد بتعريفات Mashru |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-2ebb32be-000 | كَتَبَ | كَ=32 تَ=72 بَ=104 | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |
| W-2ebb32be-001 | الطَّالِبُ | طْ=67 طَ=64 اْ=11 لِ=54 بُ=105 | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |
| W-2ebb32be-002 | الدَّرْسَ | دْ=71 دَ=68 رْ=63 سَ=80 | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | PUNCT_DROPPED_DECLARED:. |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_REQUESTED (--hokom غير مطلوب) |  |
| S4_MADLUL | نعم | نعم | لا | نعم | لا | نعم | لا | كلمة أو أكثر بلا مدلول ← S5 لا يُبنى | W-2ebb32be-000:NO_SEALED_MADLUL؛ W-2ebb32be-001:NO_SEALED_MADLUL؛ W-2ebb32be-002:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | لا | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | OUT_OF_EXECUTED_PATH:جملة من 3 كلمات (المغلَّف: كلمتان) + PREREQ_MISSING: مدلولٌ أو خلايا ناقصة | OUT_OF_EXECUTED_PATH |
| S6_AQL | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | PREREQ_MISSING (S5 لم يُنتج إطارًا) |  |
| S7_BURHAN | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | PREREQ_MISSING (S5 لم يُنتج إطارًا) |  |

## ٥. ما لا يُدَّعى

- لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.
- المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.
- أنواع الجمل المنفَّذة في هذه الأداة: [فعل ماضٍ + فاعل معرَّف بأل] و [فعل ماضٍ + فاعل منوَّن] فقط ؛ ما عداها OUT_OF_EXECUTED_PATH.
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.

## ٦. هوية التشغيل
```
mashru_root = /tmp/claude-0/-home-claude/df1a9f35-ff1b-5bad-8e6d-f9f037af0cec/scratchpad/m
mashru_head = e4c801ffe9171dadedcc3aae23051ea0953ae361
mashru_tree_clean = False
mashru_status_porcelain = ?? Shahid_Ahmad.lean
?? Shahid_Ahmad_T4.lean
?? jumla_kamila.json
lean_toolchain = leanprover/lean4:v4.34.1
qamus_sha256 = 964538402a4e2f52c5834a4fabc21637f71616df1709cf4ecff99732165a6c0e
  3f9e1575e875ee5f  run.py
  e3b0c44298fc1c14  t4/__init__.py
  8df5d9665aab77ca  t4/core.py
  1c3a62d0977528ec  t4/dal.py
  964538402a4e2f52  t4/qamus.json
  f72f898d7419c5d7  t4/report.py
timestamp_utc = 2026-10-24T10:57:35.198811+00:00
```
