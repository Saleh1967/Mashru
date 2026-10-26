# Tabaqat4 — «ذَهَبَ وَلَدٌ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 1b4b30ab00a8a0d8c1ba54506de268d74d111043c1a061dad79e349ace632c10
CODEPOINTS        = 13 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = 8599238ffa77f9f7b92684eab5c350c7ad1035e1 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مبرهن على الشاهد | ط2:مبرهن على الشاهد | ط3:مبرهن على الشاهد | ط4:مبرهن على الشاهد
HUKM3             = .murakhkhas
WASM_SUMMARY      = مبرهن=1 ، مبرهن على الشاهد=8 ، مطابَق=4 ، مفحوص=2 ، مقيس=2 ، تقدير=3 ، بلا رتبة=1
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-1b4b30ab-000` | تقدير Hokom لـ«ذَهَبَ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_PAST', 'final_root': ['ذ', 'ه', 'ب'], 'final_wazn': 'FA_A_LA', 'mood': 'NOT_APPLICABLE', 'directive': 'ACCEPT', 'active_residuals': ['bab:mujarrad:imperfect_vowel_not_known', 'sami3i_required', 'transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-1b4b30ab-001` | تقدير Hokom لـ«وَلَدٌ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'active_residuals': ['defer:root:root_path_not_opened_by_pre_root', 'defer:wazn:no_hypothesis_built', 'final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-1b4b30ab-000` | «ذَهَبَ»: 3 خلية [ذَ=92, هَ=4, بَ=104] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-1b4b30ab-001` | «وَلَدٌ»: 4 خلية [وَ=112, لَ=52, د◌ُ=69, نْ(تنوين)=59] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_W-1b4b30ab-001` | قارئ Mashru يقرأ «وَلَدٌ» = [112, 52, 71] ≠ الجدول [112, 52, 69, 59] — WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) | مفحوص | مخرج qari (تنفيذ Mashru) ؛ الاختلاف يُعرَض ولا يُحسَم  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [92, 4, 104, 116, 112, 52, 71] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ١ — الدالّ وحده | `tabaqa1_kalimat` | خلايا الكلمات الـ2 كما بناها Mashru في الإطار (مطابقة البناء) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٢ — المدلول وحده | `makhzan_W-1b4b30ab-000` | المخزن (Mashru) باللفظ «ذهب»: 2 قول ؛ الأوّل: mutabaqa:ذهب:الذهاب في الأرض، — سند 936c68e0c2c6@655167/PageV01P309/ذهب/قائل:أبو عبيد | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `jidhr_W-1b4b30ab-000` | مرشَّح الجذر عند قارئ Mashru: «ذهب» (مرشَّح لا هويّة ؛ المزيد والأدوات لا تُميَّز بعد) | مقيس | qari: fakk_ramz على ثلاث خانات حواملها سالمة — نطاق معلَن  |
| ٢ — المدلول وحده | `madlul_W-1b4b30ab-000` | «ذَهَبَ» ↔ مدلول `dhahab` (haqiqa=10) — المصدر MASHRU_WITNESS (Jisr/Utur.lean:327) ؛ مودَع 936c68e0c2c6… | مطابَق | MADLUL_SOURCE=MASHRU_WITNESS ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `makhzan_W-1b4b30ab-001` | المخزن باللفظ «ولد»: لا مدخل — لا حكم (الغياب ليس امتناعًا) | **بلا رتبة** |  — MAKHZAN_NO_ENTRY |
| ٢ — المدلول وحده | `madlul_W-1b4b30ab-001` | «وَلَدٌ» ↔ مدلول `walad` (haqiqa=20) — المصدر MASHRU_WITNESS (Jisr/Utur.lean:326) | مطابَق | MADLUL_SOURCE=MASHRU_WITNESS ؛ حقول المدلول تُبرهَن في S7 (مضمَّنةً نصًّا إن كان مودَع مالك)  |
| ٢ — المدلول وحده | `tabaqa2_maani` | المدلولات الـ2 في الإطار (جميعُها مفحوصةٌ في مطابقة maani ، ومنها المفعول إن وُجد) ، و`dhahab.tim = true` (عَرَضٌ له زمان) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: فعل ماضٍ + فاعل منوَّن ← إطار Jisr.Mulhaqat.jaaRajul مُختارٌ **تقديرًا** من النمط «fiil|ism(tanwin)» (شاهد dhahabaWaladun (Jisr/Utur.lean:918)) | مقيس | اختيار الإطار من النمط (قسم + حركة الآخر ؛ المصدر HOKOM+SURFACE) — تقدير ؛ الحكم يُبرهَن في S7 شرطًا عليه (CONDITIONAL_ON_SELECTED_ITAR)  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_hukm` | حكم الإطار الثلاثي hukm3 = مرخَّص (.murakhkhas) ؛ ibtida3=true ؛ سلسلة الوصل [92, 4, 104, 116, 112, 52, 69, 59] | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_isnad` | الإسناد الدلالي: walad موضوعٌ ، قابليّة 10 محمولٌ ، نسبة إسنادية | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_ajza` | أجزاء الجملة الصغرى بالرتبة: [.mahkum, .hakim] (محكوم ثمّ حاكم) | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_kalam` | كلامٌ يُستغنى به بالسكوت: true | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_zaman` | زمن الحدث عند المرساة: some .madi (بإزاحة -1 ساعة معلَنة) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_mawdi` | موضع الجملة نسبةً إلى «هنا»: ⟨0, 0, 0⟩ | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_thabat` | نقل المرساة والحدث معًا بساعة لا يغيّر الزمن (thabat_naql_arad) | مبرهن | lean rc=0 ؛ axioms=['propext', 'Quot.sound']  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-1b4b30ab-000 | ذَهَبَ | ذَ=92 هَ=4 بَ=104 ؛ قارئ Mashru: AGREE | `dhahab` Jisr/Utur.lean:327 ؛ مودَع المخصص 936c68e0 | مبرهن على الشاهد | مبرهن على الشاهد |
| W-1b4b30ab-001 | وَلَدٌ | وَ=112 لَ=52 د◌ُ=69 نْ(تنوين)=59 ؛ قارئ Mashru: DISAGREE (WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة)) | `walad` Jisr/Utur.lean:326 ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| ذَهَبَ | FI3L/VERBAL_PAST | ['ذ', 'ه', 'ب'] | FA_A_LA | bab:mujarrad:imperfect_vowel_not_known؛ sami3i_required؛ transitivity_unknown؛ root_class_unknown | ذهب | AGREE |
| وَلَدٌ | ISM/LEXICAL_NOUN | None | None | defer:root:root_path_not_opened_by_pre_root؛ defer:wazn:no_hypothesis_built؛ final_root:null؛ final_wazn:null | — | — |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-1b4b30ab-001:QARI_DISAGREE:WAQF_VS_WASL: القارئ يوقف على آخر النصّ (حذف التنوين وتسكين) والجدول يُخرج صورة الوصل (تنوين = نون ساكنة) |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-1b4b30ab-000:MADLUL_SOURCE=MASHRU_WITNESS؛ W-1b4b30ab-001:MADLUL_SOURCE=MASHRU_WITNESS |
| S5_MAAN_ITAR | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | ITAR_SELECTED:Jisr.Mulhaqat.jaaRajul ؛ المصدر HOKOM+SURFACE ؛ CONDITIONAL_ON_SELECTED_ITAR |
| S6_AQL | نعم | نعم | نعم | نعم | نعم | نعم | نعم | Mirsat ⟨0, ⟨0,0,0⟩⟩ و Arad .fiil 10 (-1) .saa none — افتراضات معلَنة (ت3/ت4/ت5 من الشاهد) | MIRSAT_DEFAULT_ASSUMED؛ ARAD_IZAHA_DEFAULT_ASSUMED؛ LAZIM_BY_FRAME_NOT_BY_TEXT |
| S7_BURHAN | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |

## ٤. البرهان (Lean)

```
PASS1_RC = 0 ؛ PASS2_RC = 0
OBSERVED = {"hukm3": ".murakhkhas", "ibtida3": "true", "silsila": "[92, 4, 104, 116, 112, 52, 69, 59]", "ajza": "[.mahkum, .hakim]", "yastaghni": "true", "zaman": "some .madi", "mawdi": "⟨0, 0, 0⟩"}
tabaqa1_kalimat    passed=True axioms=[]
tabaqa2_maani      passed=True axioms=[]
tabaqa3_hukm       passed=True axioms=['propext']
tabaqa3_isnad      passed=True axioms=[]
tabaqa4_ajza       passed=True axioms=['propext']
tabaqa4_kalam      passed=True axioms=['propext']
tabaqa4_zaman      passed=True axioms=[]
tabaqa4_mawdi      passed=True axioms=[]
tabaqa4_thabat     passed=True axioms=['propext', 'Quot.sound']
FILES = {"pass1": "2ea9d4db61ba3eb9a77979bab0c4925db81cd28c97a577413767ac40f8ed547e", "pass2": "9776cfc89141b4fa3859b71e2d085acdc09ed34222e6ae97c62312d17f1a28e4"}
```

## ٥. ما لا يُدَّعى

- لا صحّة لغوية خارجية: ما يمرّ هنا مرّ على بنى Mashru كما عرّفها د. صالح ، لا على العربية كلّها.
- المدلول لا يُولَّد: كلمة بلا مدلول معرَّف في Mashru تتوقّف عند الطبقة الثانية بالاسم NO_SEALED_MADLUL.
- الأطر المنفَّذة في هذه الأداة (itar_map): [فعل+فاعل بأل]→darabaZayd ، [فعل+فاعل منوَّن]→jaaRajul ، [فعل+فاعل+مفعول بأل]→daraba ، وباب الجزاء ؛ ما عداها OUT_OF_EXECUTED_PATH باسم نمطه (ITAR_UNMAPPED).
- المرساة (الآن=0 ، هنا=⟨0,0,0⟩) وإزاحة الحدث (−1 ساعة) موروثتان من Shahid_Ahmad.lean ت3/ت4 ، افتراضٌ معلَن قابل للتغيير بوسيطَي --an/--izaha.
- الإسناد الدلالي ⟨مدلول_الفاعل ، qabiliyya(حقيقة_الفعل) ، isnadiyya⟩ قاعدةٌ بنيوية موروثة من الشاهد ، ليست استنتاجًا من النصّ.
- رتبة «مبرهن على الشاهد» تعني: نظرية by decide مرّت على هذه الجملة بعينها في Lean ، بمسلّمات ⊆ {propext, Classical.choice, Quot.sound}. ليست «مبرهن» عامًّا.
- اختيار الإطار (CONDITIONAL_ON_SELECTED_ITAR): الإطار مُختارٌ تقديرًا من النمط لا محسومًا من Mashru ؛ الحكم مشروطٌ به ؛ تعدّد الأنماط يُعرَض ولا يُرجَّح.

## ٦. هوية التشغيل
```
mashru_root = /Users/husseinhiyassat/mashru
mashru_head = 8599238ffa77f9f7b92684eab5c350c7ad1035e1
mashru_tree_clean = False
mashru_status_porcelain = M by-hussein/mudaat/Mudaat.lean
 M by-hussein/mudaat/mudaat.json
 M by-hussein/tabaqat4/mudaat_prep.py
 M by-hussein/tabaqat4/tests/test_tabaqat4.py
?? by-hussein/mudaat/D6_COVERAGE.md
?? by-hussein/mudaat/OWNER_QUESTIONS_v6.md
?? by-hussein/tabaqat4/_runs_samples/d6_c01/
?? by-hussein/tabaqat4/_runs_samples/d6_c02/
?? by-hussein/tabaqat4/_runs_samples/d6_c03/
?? by-hussein/tabaqat4/_runs_samples/d6_c04/
?? by-hussein/tabaqat4/t4/hfn_d6.py
?? by-hussein/tabaqat4/t4/hfn_map.json
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
  9a82d2bfd5e964b2  TAQRIR_TASLIM.md
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
  61dc29b6b47c0e5c  mudaat_prep.py
  4c9d37d924c460d1  run.py
  e3b0c44298fc1c14  t4/__init__.py
  5ccbf3f33a246046  t4/core.py
  9779a99c83029d71  t4/dal.py
  562584d2506ede05  t4/forms_map.json
  b2cb216f7dec22c1  t4/hfn_d6.py
  b1ada070c207a3d8  t4/hfn_map.json
  055a7405e75fe226  t4/itar_map.json
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
  82ebbd6c9bfac390  tests/test_tabaqat4.py
timestamp_utc = 2026-10-26T21:54:03.396607+00:00
```
