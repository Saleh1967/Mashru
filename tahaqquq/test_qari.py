"""اختبارات القارئ (qari). التوقّعات مكتوبة باليد من قانون المالك (SLGE/Law.lean: شواهد bint وqaltu وhajja) ومن
جدول المخارج (Dal/Makharij.lean) وقواعد التحليل المعلنة في Qari/Main.lean، لا من مخرج القارئ.

١. «بِنْتْ»: الخلايا ب/كسرة(106) ن/سكون(59) ت/سكون(75)؛ موقوفًا عليها مرخَّصة، في الوصل ممتنعة؛ مقطع واحد CVCC.
٢. «قَالْتُ»: ممتنعة في الحالين (مدّ ثمّ ساكن غير مدغم) ولا مقاطع تُطبع.
٣. «حَاجَّ»: الشدّة ساكن ثمّ متحرّك؛ مرخَّصة؛ CVVC · CV.
٤. «كِتَابٌ»: التنوين نون ساكنة؛ CV · CVV · CVC؛ ملاحظة التنوين تُطبع.
٥. «الْهَمَلَّعُ»: همزة الوصل تُصلح بفتحة (isAl=true)؛ أوّل خلية ء/فتحة(0)؛ وفي المخزن (العيّنة) مطابقة واحدة:
   «الهملع → السريع» بسند فيه «قائل:أبو زيد»، وسمها «تقدير»، والمعنى معلومة، ولا مفهوم.
٦. «اكْتُبْ»: همزة الوصل بضمّة لأنّ الثالث مضموم (isAl=false)؛ أوّل خلية ء/ضمّة(1).
٧. الرفض باسمه: «مَدْرَسَة» (تاء مربوطة)، «كتب» (حرف بلا حركة)، «اَكل» (ألف محرّكة في الأوّل)، «مُسْتَشْفَى» (ألف مقصورة).
٨. المخزن الكامل مختوم (makhzan_kamil.sha256)، وفيه «الْبَيْتُ» له ثلاث مطابقات.
الجملة في الوصل (Dal/Jumla.lean على آلة المالك Msent وHamza.lean؛ التوقّعات محسوبة باليد من δ في SLGE/Law.lean):
٩. «قَالَ اكْتُبْ»: بعد متحرّك تسقط الهمزة بلا إصلاح؛ السلسلة 28 11 52 35 73 107؛ مرخَّصة؛ كلمة صوتية واحدة CVV·CVC·CVC.
١٠. «قَالُوا اكْتُبُوا»: الألف الفارقة لا تُنطق؛ بعد مدٍّ يُحذف المدّ (115 تسقط)؛ السلسلة 28 11 53 35 73 105 115؛ CVV·CVC·CV·CVV.
١١. «قُمْ اللَّيْلَ»: لام التعريف مدغمة (لا خلية)، وهمزة «أل» بفتحة؛ بعد ساكنٍ مُغلِق يُحرَّك بالكسر (111 → 110)؛
    السلسلة 29 110 55 52 47 52؛ CV·CVC·CVC·CV.
١٢. «مِنْ بَيْتٍ»: لا همزة وصل فحدّ الكلمة |؛ كلمتان صوتيّتان [CVC] [CVC·CVC].
١٣. الرفض باسمه في الجملة: «بِنْتْ عَظِيمٌ» الكلمة 1 لا توصل (آخرها ساكنان)؛ «قَالَ الْوَلَد لَهُ» الحرف الأخير بلا حركة في غير
    آخر الجملة فلا تُركَّب.
١٤. «الرَّجُلُ»: اللام مدغمة فالهمزة بفتحة (0) ثمّ ر/سكون(63) ر/فتحة(60)؛ و«الْرَّجُلُ» (لام ساكنة ثمّ مشدّد) ممتنعة بالقانون.
١٥. «قُمْ اكَتَبَ»: ألف مجرّدة قبل متحرّك ليست همزة وصل فتُرفض باسمها؛ والإدغام يعبر حدّ الكلمة في آلة المالك (δ: 6+k ثمّ 116 ← 38+k):
    «حَاجْ جَاءَ» مرخَّصة [CVVC] [CVV·CV]، و«حَاجْ قَالَ» تموت عند الكلمة 2.
التشغيل: python3 -I tahaqquq/test_qari.py
"""
import hashlib
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE = os.path.join(ROOT, ".lake", "build", "bin", "qari")
SIJILL = os.path.join(ROOT, "mudaat", "sijill.tsv")


def qari(words, store="makhzan.tsv"):
    p = subprocess.run([EXE, SIJILL, os.path.join(ROOT, "mawsua", store)] + words, capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    blocks, cur = {}, None
    for l in p.stdout.splitlines():
        if l.startswith("الكلمة: "):
            cur = l[len("الكلمة: "):]
            blocks[cur] = []
        elif l.startswith("الجملة في الوصل"):
            cur = "الجملة"
            blocks[cur] = [l]
        else:
            blocks[cur].append(l)
    return blocks


ok = 0
b = qari(["بِنْتْ", "قَالْتُ", "حَاجَّ", "كِتَابٌ", "الْهَمَلَّعُ", "اكْتُبْ", "مَدْرَسَة", "كتب", "اَكل", "مُسْتَشْفَى"])

o = b["بِنْتْ"]
assert o[0] == "  الخلايا: ب/كسرة(106) ن/سكون(59) ت/سكون(75)", o[0]
assert any("موقوفًا عليها مرخَّصة؛ في الوصل ممتنعة" in l for l in o), o
assert any(l.startswith("  المقاطع (1): CVCC") for l in o), o
ok += 1

o = b["قَالْتُ"]
assert any("موقوفًا عليها ممتنعة؛ في الوصل ممتنعة" in l for l in o) and not any("المقاطع" in l for l in o), o
ok += 1

o = b["حَاجَّ"]
assert o[0] == "  الخلايا: ح/فتحة(16) ا/سكون(11) ج/سكون(39) ج/فتحة(36)", o[0]
assert any(l.startswith("  المقاطع (2): CVVC · CV") for l in o), o
ok += 1

o = b["كِتَابٌ"]
assert o[0] == "  الخلايا: ك/كسرة(34) ت/فتحة(72) ا/سكون(11) ب/ضمّة(105) ن/سكون(59)", o[0]
assert any("التنوين نون ساكنة" in l for l in o) and any(l.startswith("  المقاطع (3): CV · CVV · CVC") for l in o), o
ok += 1

o = b["الْهَمَلَّعُ"]
assert o[0].startswith("  الخلايا: ء/فتحة(0) ل/سكون(55) ه/فتحة(4)"), o[0]
assert any("isAl=true" in l for l in o), o
assert "    المنطوق (مطابقة/تضمّن): 1" in o, o
assert any("mutabaqa:الهملع:السريع" in l and l.rstrip().endswith("تقدير") for l in o), o
assert any("قائل:أبو زيد" in l for l in o) and any("المعنى «السريع»: معلومة" in l for l in o), o
assert "    المفهوم (التزام): لا مدخل في المخزن — لا حكم." in o, o
ok += 1

o = b["اكْتُبْ"]
assert o[0].startswith("  الخلايا: ء/ضمّة(1) ك/سكون(35)") and any("isAl=false" in l for l in o), o
ok += 1

assert b["مَدْرَسَة"][0].startswith("  مرفوضة باسمها: تاء مربوطة"), b["مَدْرَسَة"]
assert b["كتب"][0].startswith("  مرفوضة باسمها: حرف بلا حركة"), b["كتب"]
assert b["اَكل"][0].startswith("  مرفوضة باسمها: ألف محرّكة في أوّل الكلمة"), b["اَكل"]
assert b["مُسْتَشْفَى"][0].startswith("  مرفوضة باسمها: ألف مقصورة"), b["مُسْتَشْفَى"]
ok += 1

raw = open(os.path.join(ROOT, "mawsua", "makhzan_kamil.tsv"), "rb").read()
assert hashlib.sha256(raw).hexdigest() == open(os.path.join(ROOT, "mawsua", "makhzan_kamil.sha256")).read().strip()
o = qari(["الْبَيْتُ"], store="makhzan_kamil.tsv")["الْبَيْتُ"]
assert "    المنطوق (مطابقة/تضمّن): 3" in o, o
ok += 1

# ٩
b = qari(["قَالَ", "اكْتُبْ"])
j = b["الجملة"]
assert "  الوصل عند الكلمة 2 «اكْتُبْ»: سقطت همزة الوصل بعد متحرّك بلا إصلاح (wasl_after_mover)" in j, j
assert "  السلسلة: ق/فتحة(28) ا/سكون(11) ل/فتحة(52) ك/سكون(35) ت/ضمّة(73) ب/سكون(107)" in j, j
assert any(l.startswith("  القانون (آلة الجملة Msent): مرخَّصة") for l in j), j
assert any(l.startswith("  الكلمات الصوتية (1): [CVV · CVC · CVC]") for l in j), j
ok += 1

# ١٠
b = qari(["قَالُوا", "اكْتُبُوا"])
o = b["قَالُوا"]
assert o[0] == "  الخلايا: ق/فتحة(28) ا/سكون(11) ل/ضمّة(53) و/سكون(115)", o[0]
assert any("الألف الفارقة" in l for l in o), o
j = b["الجملة"]
assert "  الوصل عند الكلمة 2 «اكْتُبُوا»: سقطت همزة الوصل وحُذف المدّ قبلها لالتقاء الساكنين (wasl_after_madd)" in j, j
assert "  السلسلة: ق/فتحة(28) ا/سكون(11) ل/ضمّة(53) ك/سكون(35) ت/ضمّة(73) ب/ضمّة(105) و/سكون(115)" in j, j
assert any(l.startswith("  القانون (آلة الجملة Msent): مرخَّصة") for l in j), j
assert any(l.startswith("  الكلمات الصوتية (1): [CVV · CVC · CV · CVV]") for l in j), j
ok += 1

# ١١
b = qari(["قُمْ", "اللَّيْلَ"])
o = b["اللَّيْلَ"]
assert o[0] == "  الخلايا: ء/فتحة(0) ل/سكون(55) ل/فتحة(52) ي/سكون(47) ل/فتحة(52)", o[0]
assert any("لام التعريف مدغمة" in l for l in o) and any("isAl=true" in l for l in o), o
j = b["الجملة"]
assert any(l.startswith("  الوصل عند الكلمة 2 «اللَّيْلَ»: سقطت همزة الوصل وحُرّك الساكن قبلها بالكسر") for l in j), j
assert "  السلسلة: ق/ضمّة(29) م/كسرة(110) ل/سكون(55) ل/فتحة(52) ي/سكون(47) ل/فتحة(52)" in j, j
assert any(l.startswith("  القانون (آلة الجملة Msent): مرخَّصة") for l in j), j
assert any(l.startswith("  الكلمات الصوتية (1): [CV · CVC · CVC · CV]") for l in j), j
ok += 1

# ١٢
j = qari(["مِنْ", "بَيْتٍ"])["الجملة"]
assert not any(l.startswith("  الوصل عند") for l in j), j
assert "  السلسلة: م/كسرة(110) ن/سكون(59) | ب/فتحة(104) ي/سكون(47) ت/كسرة(74) ن/سكون(59)" in j, j
assert any(l.startswith("  القانون (آلة الجملة Msent): مرخَّصة") for l in j), j
assert any(l.startswith("  الكلمات الصوتية (2): [CVC] [CVC · CVC]") for l in j), j
ok += 1

# ١٣
j = qari(["بِنْتْ", "عَظِيمٌ"])["الجملة"]
assert any(l.startswith("  القانون (آلة الجملة Msent): الكلمة 1 «بِنْتْ» لا توصل بما بعدها") for l in j), j
assert not any(l.startswith("  الكلمات الصوتية") for l in j), j
b = qari(["قَالَ", "الْوَلَد", "لَهُ"])
assert b["الْوَلَد"][0].startswith("  مرفوضة باسمها: الحرف الأخير بلا حركة في غير آخر الجملة"), b["الْوَلَد"]
assert b["الجملة"][0].endswith("لم تُركَّب — فيها كلمة مرفوضة باسمها"), b["الجملة"]
ok += 1

# ١٤
b = qari(["الرَّجُلُ", "الْرَّجُلُ"])
o = b["الرَّجُلُ"]
assert o[0] == "  الخلايا: ء/فتحة(0) ر/سكون(63) ر/فتحة(60) ج/ضمّة(37) ل/ضمّة(53)", o[0]
assert any("isAl=true" in l for l in o) and any("موقوفًا عليها مرخَّصة؛ في الوصل مرخَّصة" in l for l in o), o
o = b["الْرَّجُلُ"]
assert o[0] == "  الخلايا: ء/فتحة(0) ل/سكون(55) ر/سكون(63) ر/فتحة(60) ج/ضمّة(37) ل/ضمّة(53)", o[0]
assert any("موقوفًا عليها ممتنعة؛ في الوصل ممتنعة" in l for l in o), o
ok += 1

# ١٥
b = qari(["قُمْ", "اكَتَبَ"])
assert b["اكَتَبَ"][0].startswith("  مرفوضة باسمها: ألف مجرّدة قبل متحرّك"), b["اكَتَبَ"]
assert b["الجملة"][0].endswith("لم تُركَّب — فيها كلمة مرفوضة باسمها"), b["الجملة"]
j = qari(["حَاجْ", "جَاءَ"])["الجملة"]
assert "  السلسلة: ح/فتحة(16) ا/سكون(11) ج/سكون(39) | ج/فتحة(36) ا/سكون(11) ء/فتحة(0)" in j, j
assert any(l.startswith("  القانون (آلة الجملة Msent): مرخَّصة") for l in j), j
assert any(l.startswith("  الكلمات الصوتية (2): [CVVC] [CVV · CV]") for l in j), j
j = qari(["حَاجْ", "قَالَ"])["الجملة"]
assert any(l.startswith("  القانون (آلة الجملة Msent): ممتنعة عند الكلمة 2 «قَالَ»") for l in j), j
ok += 1

print(f"{ok}/15")
