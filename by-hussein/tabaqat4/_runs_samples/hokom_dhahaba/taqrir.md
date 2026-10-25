# Tabaqat4 — «ذَهَبَ الْوَلَدُ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 34c9ac0fff60bc73c9ed17b600b1c133d2f0c83d5b47427e921bb533853450e2
CODEPOINTS        = 16 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = ed7c5d3248a123945cfa3e8901a39f7f9ecdf394 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مبرهن على الشاهد | ط2:مبرهن على الشاهد | ط3:مبرهن على الشاهد | ط4:مبرهن على الشاهد
HUKM3             = .murakhkhas
WASM_SUMMARY      = مبرهن=1 ، مبرهن على الشاهد=8 ، مطابَق=4 ، مفحوص=1 ، مقيس=2 ، تقدير=4
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
| ٠ — تقدير Hokom | `hokom_W-34c9ac0f-000` | تقدير Hokom لـ«ذَهَبَ»: {'pin': '8a23298076b4', 'word_class': 'FI3L', 'word_class_subclass': 'VERBAL_PAST', 'final_root': ['ذ', 'ه', 'ب'], 'final_wazn': 'FA_A_LA', 'mood': 'NOT_APPLICABLE', 'directive': 'ACCEPT', 'active_residuals': ['bab:mujarrad:imperfect_vowel_not_known', 'sami3i_required', 'transitivity_unknown', 'root_class_unknown']} | تقدير | pin=8a23298076b4  |
| ٠ — تقدير Hokom | `hokom_W-34c9ac0f-001` | تقدير Hokom لـ«الْوَلَدُ»: {'pin': '8a23298076b4', 'word_class': 'ISM', 'word_class_subclass': 'LEXICAL_NOUN', 'final_root': None, 'final_wazn': None, 'mood': None, 'directive': 'ACCEPT', 'active_residuals': ['defer:root:assimilated_fa_unresolved', 'defer:wazn:no_hypothesis_built', 'final_root:null', 'final_wazn:null']} | تقدير | pin=8a23298076b4  |
| ١ — الدالّ وحده | `dal_W-34c9ac0f-000` | «ذَهَبَ»: 3 خلية [ذَ=92, هَ=4, بَ=104] | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `dal_W-34c9ac0f-001` | «الْوَلَدُ»: 4 خلية [لْ=55, وَ=112, لَ=52, دُ=69] ، بأل التعريف (همزة وصل) | مطابَق | ترميز بجدول Dal/Makharij.lean (n=4·حامل+حالة) ؛ يُبرهَن على مستوى الجملة في S7  |
| ١ — الدالّ وحده | `qari_jumla` | الجملة في الوصل عند قارئ Mashru: مرخَّصة موقوفًا على آخرها — لها تقطيع (jumla_murakhkhasa) ؛ السلسلة [92, 4, 104, 55, 112, 52, 69] | مفحوص | آلة الجملة Msent في qari (تنفيذ Mashru ، لا نظرية في ملفنا)  |
| ١ — الدالّ وحده | `tabaqa1_kalimat` | خلايا الكلمتَين كما بناها Mashru في الإطار الثلاثي (مطابقة البناء) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٢ — المدلول وحده | `makhzan_W-34c9ac0f-000` | المخزن (Mashru) باللفظ «ذهب»: 2 قول ؛ الأوّل: mutabaqa:ذهب:الذهاب في الأرض، — سند 936c68e0c2c6@655167/PageV01P309/ذهب/قائل:أبو عبيد | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `jidhr_W-34c9ac0f-000` | مرشَّح الجذر عند قارئ Mashru: «ذهب» (مرشَّح لا هويّة ؛ المزيد والأدوات لا تُميَّز بعد) | مقيس | qari: fakk_ramz على ثلاث خانات حواملها سالمة — نطاق معلَن  |
| ٢ — المدلول وحده | `madlul_W-34c9ac0f-000` | «ذَهَبَ» ↔ مدلول Mashru `dhahab` (ذهب — عَرَضٌ فعليّ (tim=true) ، لازم بنيويًّا (إطار بلا خانة مفعول)) — Jisr/Utur.lean:327 ؛ مودَع: المخصص 936c68e0c2c6… PageV01P309–310 | مطابَق | مطابقة اسمية بين السطح وتعريف Mashru ؛ حقوله تُبرهَن في S7  |
| ٢ — المدلول وحده | `makhzan_W-34c9ac0f-001` | المخزن (Mashru) باللفظ «الولد»: 1 قول ؛ الأوّل: mutabaqa:الولد:وهي التي تسمى الخولاء وحده أبو — سند 936c68e0c2c6@4668608/PageV05P051/الولد/قائل:بلا نسبة صريحة | تقدير | وسم Mashru المحسوب نفسه (qari: «وسمه المحسوب: تقدير») ؛ معنى معجمي لا مدلول بنيوي  |
| ٢ — المدلول وحده | `madlul_W-34c9ac0f-001` | «الْوَلَدُ» ↔ مدلول Mashru `walad` (ولد — ذاتٌ ، خاصّة 21 ، علاقة (1,30) ، قابليّات [10,11]) — Jisr/Utur.lean:326 ؛ بلا مودَع معجمي معلَن | مطابَق | مطابقة اسمية بين السطح وتعريف Mashru ؛ حقوله تُبرهَن في S7  |
| ٢ — المدلول وحده | `tabaqa2_maani` | المدلولان في الإطار ، و`dhahab.tim = true` (عَرَضٌ له زمان) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٣ — معًا (الإطار والحكم) | `naw_jumla` | نوع الجملة: فعل ماضٍ + فاعل معرَّف بأل ← إطار Jisr.Mulhaqat.darabaZayd (شاهد Mashru: dhahabaAlWalad (Jisr/Utur.lean:914)) | مقيس | اختيار الإطار بشروط سطحية (قسم المدلول الأوّل ، أل/تنوين الثاني) — حكمه يُبرهَن في S7  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_hukm` | حكم الإطار الثلاثي hukm3 = مرخَّص (.murakhkhas) ؛ ibtida3=true ؛ سلسلة الوصل [92, 4, 104, 55, 112, 52, 69] | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٣ — معًا (الإطار والحكم) | `tabaqa3_isnad` | الإسناد الدلالي: walad موضوعٌ ، قابليّة 10 محمولٌ ، نسبة إسنادية | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_ajza` | أجزاء الجملة الصغرى بالرتبة: [.mahkum, .hakim] (محكوم ثمّ حاكم) | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_kalam` | كلامٌ يُستغنى به بالسكوت: true | مبرهن على الشاهد | lean rc=0 ؛ axioms=['propext']  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_zaman` | زمن الحدث عند المرساة: some .madi (بإزاحة -1 ساعة معلَنة) | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_mawdi` | موضع الجملة نسبةً إلى «هنا»: ⟨0, 0, 0⟩ | مبرهن على الشاهد | lean rc=0 ؛ axioms=[]  |
| ٤ — العقل (المرساة والإسناد) | `tabaqa4_thabat` | نقل المرساة والحدث معًا بساعة لا يغيّر الزمن (thabat_naql_arad) | مبرهن | lean rc=0 ؛ axioms=['propext', 'Quot.sound']  |

## ٢. الفصل الرباعي لكل كلمة

| المرساة | الكلمة | ١ الدالّ (خلايا) | ٢ المدلول | ٣ الحكم | ٤ العقل |
|---|---|---|---|---|---|
| W-34c9ac0f-000 | ذَهَبَ | ذَ=92 هَ=4 بَ=104 ؛ قارئ Mashru: AGREE | `dhahab` Jisr/Utur.lean:327 ؛ مودَع المخصص 936c68e0 | مبرهن على الشاهد | مبرهن على الشاهد |
| W-34c9ac0f-001 | الْوَلَدُ | لْ=55 وَ=112 لَ=52 دُ=69 ؛ قارئ Mashru: AGREE | `walad` Jisr/Utur.lean:326 ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |

## ٢ج. تقدير Hokom مقابل قارئ Mashru (تُعرَض ولا تُحسَم ؛ رتبة Hokom «تقدير» ، لا مدلولَ ولا حكم)

| الكلمة | صنف Hokom | جذر Hokom | وزن Hokom | بقايا Hokom | مرشَّح جذر القارئ | المقارنة |
|---|---|---|---|---|---|---|
| ذَهَبَ | FI3L/VERBAL_PAST | ['ذ', 'ه', 'ب'] | FA_A_LA | bab:mujarrad:imperfect_vowel_not_known؛ sami3i_required؛ transitivity_unknown؛ root_class_unknown | ذهب | AGREE |
| الْوَلَدُ | ISM/LEXICAL_NOUN | None | None | defer:root:assimilated_fa_unresolved؛ defer:wazn:no_hypothesis_built؛ final_root:null؛ final_wazn:null | — | — |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | نعم | نعم | نعم | نعم | نعم | نعم | لا | رتبة تقدير ؛ يُعرَض ولا يُستهلك في S4..S7 |  |
| S4_MADLUL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  | W-34c9ac0f-001:MADLUL_SOURCE_UNDECLARED_IN_MASHRU |
| S5_MAAN_ITAR | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S6_AQL | نعم | نعم | نعم | نعم | نعم | نعم | نعم | Mirsat ⟨0, ⟨0,0,0⟩⟩ و Arad .fiil 10 (-1) .saa none — افتراضات معلَنة (ت3/ت4/ت5 من الشاهد) | MIRSAT_DEFAULT_ASSUMED؛ ARAD_IZAHA_DEFAULT_ASSUMED؛ LAZIM_BY_FRAME_NOT_BY_TEXT |
| S7_BURHAN | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |

## ٤. البرهان (Lean)

```
PASS1_RC = 0 ؛ PASS2_RC = 0
OBSERVED = {"hukm3": ".murakhkhas", "ibtida3": "true", "silsila": "[92, 4, 104, 55, 112, 52, 69]", "ajza": "[.mahkum, .hakim]", "yastaghni": "true", "zaman": "some .madi", "mawdi": "⟨0, 0, 0⟩"}
tabaqa1_kalimat    passed=True axioms=[]
tabaqa2_maani      passed=True axioms=[]
tabaqa3_hukm       passed=True axioms=['propext']
tabaqa3_isnad      passed=True axioms=[]
tabaqa4_ajza       passed=True axioms=['propext']
tabaqa4_kalam      passed=True axioms=['propext']
tabaqa4_zaman      passed=True axioms=[]
tabaqa4_mawdi      passed=True axioms=[]
tabaqa4_thabat     passed=True axioms=['propext', 'Quot.sound']
FILES = {"pass1": "4fe5fa06c4c156e7d2d073a85f60f38f84603c7a09867cc86e76218098a42203", "pass2": "c1d3cb620a9bc97880500cfeb4e591ac5aa7f7d72ad40f270f9aeed86b2ab53e"}
```

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
timestamp_utc = 2026-10-25T05:14:23.643479+00:00
```
