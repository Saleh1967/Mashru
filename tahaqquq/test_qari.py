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

print(f"{ok}/8")
