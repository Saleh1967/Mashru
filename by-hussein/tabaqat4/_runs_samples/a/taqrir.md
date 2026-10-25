# Tabaqat4 — «ذَهَبَ الْوَلَدُ»

```
SCHEMA            = Tabaqat4Record:v1
TEXT_SHA256       = 34c9ac0fff60bc73c9ed17b600b1c133d2f0c83d5b47427e921bb533853450e2
CODEPOINTS        = 16 ؛ NFC_EQ_INPUT=True
MASHRU_HEAD       = d2533c39bb42b710248beebb0129f178fc7cbd76 ؛ TREE_CLEAN=False
LEAN_TOOLCHAIN    = leanprover/lean4:v4.34.1
QAMUS_SHA256      = e8662a21d29bfe8b…
TABAQAT_STATE     = ط1:مبرهن على الشاهد | ط2:مبرهن على الشاهد | ط3:مبرهن على الشاهد | ط4:مبرهن على الشاهد
HUKM3             = .murakhkhas
WASM_SUMMARY      = مبرهن=1 ، مبرهن على الشاهد=8 ، مطابَق=4 ، مفحوص=1 ، مقيس=2 ، تقدير=2
```

## ١. ما الذي عرفه Mashru — طبقةً طبقة

| الطبقة | الادّعاء | القيمة (مترجمة) | الرتبة | البرهان / سبب الغياب |
|---|---|---|---|---|
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
| W-34c9ac0f-000 | ذَهَبَ | ذَ=92 هَ=4 بَ=104 | `dhahab` Jisr/Utur.lean:327 ؛ مودَع المخصص 936c68e0 | مبرهن على الشاهد | مبرهن على الشاهد |
| W-34c9ac0f-001 | الْوَلَدُ | لْ=55 وَ=112 لَ=52 دُ=69 | `walad` Jisr/Utur.lean:326 ؛ بلا مودَع معلَن | مبرهن على الشاهد | مبرهن على الشاهد |

## ٣. المراحل — الأسئلة السبعة

| المرحلة | بدأ الاستدعاء؟ | اكتمل؟ | وجد؟ | أنتج؟ | قُبل؟ | حُفظ؟ | استهلكه التالي؟ | السبب | البقايا |
|---|---|---|---|---|---|---|---|---|---|
| S0_HAWIYYA | نعم | نعم | نعم | نعم | نعم | نعم | —(لم يُقَس) |  |  |
| S1_TAQTI | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S2_DAL | نعم | نعم | نعم | نعم | نعم | نعم | نعم |  |  |
| S3_HOKOM_TAQDIR | لا | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | —(لم يُقَس) | NOT_REQUESTED (--hokom غير مطلوب) |  |
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
  54143f4dc3a3022e  t4/core.py
  52e44fb0ea84e9d2  t4/dal.py
  e8662a21d29bfe8b  t4/qamus.json
  841d73f7a5f34fa7  t4/qari.py
  2593ad5e16f6c048  t4/report.py
  27052856c95f7e63  tests/test_tabaqat4.py
timestamp_utc = 2026-10-25T04:48:22.057319+00:00
```
