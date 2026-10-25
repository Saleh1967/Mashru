# Tabaqat4 — «مَاتَ مَالِكٌ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = e0a352522d8273e049b22b0fdbcbbed22c2c9618f9f51f171faa4764798af8c4
CODEPOINTS        = 13 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = ed7c5d3248a123945cfa3e8901a39f7f9ecdf394 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مطابَق | ط2:PARTIAL_OR_BLOCKED | ط3:NOT_REACHED | ط4:NOT_REACHED
HUKM3             = None
WASM_SUMMARY      = مطابَق=2 ، مفحوص=2 ، تقدير=2 ، بلا رتبة=4
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-e0a35252-000` | تقدير Hokom لـ«مَاتَ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'active_residuals': ['defer:root:hollow_underlying_radical_unresolved', 'residual:mim:root_extraction_failed', 'defer:relicensing:proposed_root_extraction_incomplete', 'defer:wazn:relicensing_did_not_accept', 'final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-e0a35252-001` | تقدير Hokom لـ«مَالِكٌ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': ['م', 'ل', 'ك'], 'final_wazn': 'FA3IL', 'mood': None, 'directive': 'ACCEPT', 'active_residuals': ['defer:bab:nominal_morphology_path', 'no_masdar_candidate', 'transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-e0a35252-000` | «مَاتَ»: 3 خلية [مَ=108, اْ=11, تَ=72] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-e0a35252-001` | «مَالِكٌ»: 5 خلية [مَ=108, اْ=11, لِ=54, ك◌ُ=33, نْ(تنوين)=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_W-e0a35252-001` | قارئ Mashru يقرأ «مَالِكٌ» = [108, 11, 54, 35] ≠ الجدول [108, 11, 54, 33, 59] — WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) | مفحوص | مخرج qari (تنفيذ Mashru) ؛ الاختلاف يُعرَض ولا يُحسَم  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [108, 11, 72, 116, 108, 11, 54, 35] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ٢ — المدلول وحده | `makhzan_W-e0a35252-000` | المخزن باللفظ «مات»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-e0a35252-000` | «مَاتَ»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به) |
| ٢ — المدلول وحده | `makhzan_W-e0a35252-001` | المخزن باللفظ «مالك»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-e0a35252-001` | «مَالِكٌ»: لا مدلولَ بنيويًّا (SLGE.Madlul) معرَّفًا لها في Mashru (ولا يُولَّد) | **بلا رتبة** |  — NO_SEALED_MADLUL: لا تعريف SLGE.Madlul لها في مصدر Mashru (qamus.json المقيَّد به) |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-e0a35252-000 | مَاتَ | مَ=108 اْ=11 تَ=72 ؛ قارئ Mashru: AGREE | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |
| W-e0a35252-001 | مَالِكٌ | مَ=108 اْ=11 لِ=54 ك◌ُ=33 نْ(تنوين)=59 ؛ قارئ Mashru: DISAGREE (WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة)) | NO_SEALED_MADLUL | NOT_REACHED | NOT_REACHED |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| مَاتَ | ISM/LEXICAL_NOUN | None | None | defer:root:hollow_underlying_radical_unresolved؛ residual:mim:root_extraction_failed؛ defer:relicensing:proposed_root_extraction_incomplete؛ defer:wazn:relicensing_did_not_accept؛ final_root:null؛ final_wazn:null | — | — |
| مَالِكٌ | ISM/LEXICAL_NOUN | ['م', 'ل', 'ك'] | FA3IL | defer:bab:nominal_morphology_path؛ no_masdar_candidate؛ transitivity_unknown؛ root_class_unknown | — | ONE_SIDED |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-e0a35252-001:QARI_DISAGREE:WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | لا | نعم | لا | نعم | لا | كلمة أو أكثر بلا مدلول ← المسار الإسناديّ (S5) لا يُبنى | W-e0a35252-000:NO_SEALED_MADLUL؛ W-e0a35252-001:NO_SEALED_MADLUL |
| S5_MAAN_ITAR | نعم | نعم | لا | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | PREREQ_MISSING: مدلولٌ أو خلايا ناقصة ؛ نوع الجملة لم يُقدَّر |  |
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
  82e43798dea870f1  _runs_samples/hokom_jaza/taqrir.json
  5944f11393085bf1  _runs_samples/hokom_jaza/taqrir.md
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
timestamp_utc = 2026-10-25T05:14:32.879254+00:00
```
