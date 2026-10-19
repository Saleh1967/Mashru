"""اختبارات بوّابة الإيداع (mudaat/idaa.py). كلّها على نسخة مؤقّتة من السجلّ؛ السجلّ الحقيقيّ لا يُمسّ.
التوقّعات مكتوبة من القواعد:
  ١. السجلّ الحقيقيّ سليم، وsijill.tsv مطابق للمولَّد: 15 مختومة (معاجم حزمة v11 الأربعة، وكتاب سيبويه كما أعلنه
     المالك في حزمة slge-closed، وجدول العوامل المئة كما ختمه المالك في حزمة slge-closed-v13 بتوليد
     SLGE/AwamilTable.lean منه، وقطر الندى ومغني اللبيب والألفية والجنى الداني ببصماتها في wad/MANIFEST.json
     بحزمة المالك نفسها — أُضيفت 2026-10-15؛ وجدول الأجناس — القطعة الأولى، نوعه «معلومات-سابقة»، خُتم بإذن المالك
     في الجلسة 2026-10-16 «موافق على الايداع» — فصار العدد 11؛ ثمّ القطعة الثانية (عُقَد الآباء والجماد) ونظام الفيزياء ونظام
     الرياضيات، ثلاثتها «معلومات-سابقة» بإذنه في الجلسة نفسها (13:26) «أعدّهما … اختمهما بإذنك … موافق» — فصار العدد 14؛ ثمّ جدول
     العلاقات (شبكة الأجناس والأفعال والصفات) «معلومات-سابقة» بإذنه (14:39) «أُعدّه وتختمه بإذنك كالسابق. موافق» — فصار العدد 15؛
     ثمّ كتب النبهاني الأربعة (الشخصية الإسلامية ج1 وج3، التفكير، سرعة البديهة) «معلومات-سابقة»، كانت مرشّحةً منذ 2026-10-15
     بإذن المالك المؤجَّل بقوله «ليس الآن»، ثمّ خُتمت بإذنه الصريح في الجلسة 2026-10-17 (12:14 بتوقيت عمّان) «أوافق ان تنفذ
     الختم وفق افضل الممارسات» — فصار العدد 19؛ ثمّ «المدوّنة القرآنية الصرفية QAC 0.4» «مرجعًا محجوبًا» بإذنه 2026-10-19 (20:18
     «نعم تأذن بختم QAC 0.4 … ووقع»، و21:43 «ابحث … في المستودع») — فصار العدد 20) و8 مرشّحة (جدولا الحواسّ الخمس وأوّليات العقل والأزمنة والتجاور المكانيّ
     والمرساة والرابطة الإسنادية والجسر إلى الدالّ والنِّسَب الثلاث على الأصناف، المسجَّلة مرشّحةً حتّى يأذن المالك بختمها.
     تصحيحٌ: كانت هذه الفقرة تقول «9 مرشّحة» بذكر خمس جداولٍ فقط قبل هذا التعديل، وهو عددٌ لم يطابق الاثني عشر الفعليّين
     حتّى قبل ختم كتب النبهاني — الجداول الثلاثة الأخرى (الرابطة الإسنادية، الجسر إلى الدالّ، النِّسَب على الأصناف) أُضيفت
     للسجلّ بعد كتابة هذه الفقرة بعددها القديم ولم تُحدَّث معها؛ العددُ هنا بالعدّ المباشر على السجلّ الحقيقيّ، لا بالنقل).
  ٢. ختمٌ بلا --idhn يُرفض (خروج 3)، والسجلّ لا يتغيّر بايتًا.
  ٣. نوعٌ خارج الأربعة يُرفض (خروج 3).
  ٤. ختمٌ بإذن يُضاف «مختوم» ببصمة sha256 للبايتات كما هي (تُحسب هنا بـ hashlib مباشرة)، ويدخل sijill.tsv.
  ٥. لا تنظيف: ملفّان يختلفان بالتطويل وحده لهما بصمتان مختلفتان؛ وختم الثاني بالاسم نفسه يُرفض (تغيّر المودَع).
  ٦. بصمة مسجّلة لا تُختم باسم آخر.
  ٧. سجلّ فيه «مختوم» بلا إذن يفشل في fahs.
التشغيل: python3 -I mudaat/test_idaa.py
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "idaa.py")


def run(*a):
    p = subprocess.run([sys.executable, "-I", TOOL, *a], capture_output=True, text=True)
    return p.returncode, p.stdout


ok = 0
code, out = run("fahs")
# مرشح 9: أُضيف «جدول اللزوم من شبكة المعاجم» (luzum_mujam.tsv) مرشّحًا 2026-10-18 — لا ختمَ جديد (المختوم 19 لم يتغيّر)
# مختوم 20: خُتمت «المدوّنة القرآنية الصرفية QAC 0.4» «مرجعًا محجوبًا» بإذن المالك 2026-10-19 (20:18 و21:43 بتوقيت عمّان)
assert code == 0 and "مختوم 20، مرشح 9، أخطاء 0" in out, out
ok += 1

tmp = tempfile.mkdtemp()
try:
    sj = os.path.join(tmp, "sijill.json")
    shutil.copy(os.path.join(HERE, "sijill.json"), sj)
    shutil.copy(os.path.join(HERE, "sijill.tsv"), os.path.join(tmp, "sijill.tsv"))
    f1 = os.path.join(tmp, "bab1.txt")
    f2 = os.path.join(tmp, "bab2.txt")
    open(f1, "w", encoding="utf-8").write("باب الهمزة\n")
    open(f2, "w", encoding="utf-8").write("بـاب الهمزة\n")
    before = open(sj, "rb").read()

    code, out = run("sajjil", f1, "--ism", "شاهد", "--naw", "معلومات-سابقة", "--sijill", sj)
    assert code == 3 and "إذن" in out and open(sj, "rb").read() == before, out
    ok += 1

    code, out = run("sajjil", f1, "--ism", "شاهد", "--naw", "كتاب", "--idhn", "المالك", "--sijill", sj)
    assert code == 3 and "نوع مجهول" in out and open(sj, "rb").read() == before, out
    ok += 1

    code, out = run("sajjil", f1, "--ism", "شاهد", "--naw", "معلومات-سابقة", "--idhn", "المالك في الاختبار", "--sijill", sj)
    b1 = hashlib.sha256(open(f1, "rb").read()).hexdigest()
    s = json.load(open(sj, encoding="utf-8"))["sijill"]
    assert code == 0 and s[-1]["sha256"] == b1 and s[-1]["hala"] == "مختوم", out
    assert f"mudaa\t{b1}\tمعلومات-سابقة\tشاهد\n" in open(os.path.join(tmp, "sijill.tsv"), encoding="utf-8").read()
    ok += 1

    b2 = hashlib.sha256(open(f2, "rb").read()).hexdigest()
    assert b1 != b2
    code, out = run("sajjil", f2, "--ism", "شاهد", "--naw", "معلومات-سابقة", "--idhn", "المالك", "--sijill", sj)
    assert code == 3 and "تغيّر" in out, out
    ok += 1

    code, out = run("sajjil", f1, "--ism", "اسم-آخر", "--naw", "معلومات-سابقة", "--idhn", "المالك", "--sijill", sj)
    assert code == 3 and "مسجّلة باسم" in out, out
    ok += 1

    s = json.load(open(sj, encoding="utf-8"))["sijill"]
    s[-1]["idhn"] = ""
    json.dump({"sijill": s}, open(sj, "w", encoding="utf-8"), ensure_ascii=False)
    code, out = run("fahs", "--sijill", sj)
    assert code == 1 and "بلا إذن" in out, out
    ok += 1
finally:
    shutil.rmtree(tmp)

print(f"{ok}/7")
