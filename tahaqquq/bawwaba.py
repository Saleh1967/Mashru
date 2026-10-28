"""بوّابة التحقّق: لا يُقال «تمّ» قبل أن تمرّ كلّها. تعيد 0 إن مرّت، و2 مع السبب إن لم تمرّ.

البنود، بترتيبها (الدستور م2–م4، م8):
  ١. lake build ينجح.
  ٢. لا sorry ولا axiom ولا native_decide في ملفّات Lean (خارج التعليقات).
  ٣. Audit.lean يُبنى، وكلّ مبرهنة فيه مسلّماتها من الثلاث: propext، Classical.choice، Quot.sound.
  ٤. عدد المبرهنات المدقّقة لا ينقص عن خطّ الأساس في khatt_asas.json (نقصه حذفٌ يحتاج إذنًا).
      غياب الملفّ أو تلفه أو بطلان العدد فشلٌ مسمّى، لا خطّ أساسٍ صفريّ بديل.
  ٤أ. قائمة الطفرات لا تنقص عن الأساس: كلّ «ism» في tafrat.json عند نقطة التقاء HEAD بالمرجع (TAFRAT_ASAS_REF، وإلّا
      origin/main) حاضرٌ في القائمة الحاليّة، أو مسجَّلٌ في tahaqquq/tafrat_mahdhufa.json بسببٍ وإذن (قرار المالك 2026-10-19:
      دمجان أسقطا طفرات main بلا تعارضٍ ظاهر، ولا شيء كان يكشفه). تعذُّر الأساس فشلٌ مسمّى لا تخطٍّ صامت.
  ٤ب. نصُّ كلّ طفرة. القاعدتان بإذن المالك (2026-10-19 16:16، مكمّلتين لـ٤أ): «min» غيرُ فارغٍ يقع في ملفّه مرّةً واحدة
      (بعدّ المتداخل)، ولا يقع في تعليق. وتنفيذُ «في تعليق» قراءةُ البنّاء: موضعُ «min» في تعليق الأصل أو في بياضٍ بينه، أو
      أثرُ الطفرة لا يتعدّى التعليقَ والأسطرَ الفارغة وبياضَ أواخر الأسطر؛ ويُستثنى رفعُ تعليقٍ بحذف علامته متى أمكن مسحُ
      الناتج وتغيّر ما خارج التعليق. Lean: «--» و«/- -/» متداخلًا؛ بايثون: التعليق والتوثيق (إلّا توثيقَ وحدةٍ يُستعمل
      فيها `__doc__` اسمًا حرًّا)؛ sh: «#». والاستثناءُ وما فوق القاعدتين (الملفُّ داخل المستودع بمساره الحقيقيّ، وامتدادُه
      معروف، والاسمُ غيرُ مكرَّر) اعتُمدت بتوجيهٍ رفعه المالك 2026-10-19 18:02 وأمر بتنفيذه. يجري مع --bila-tafrat أيضًا،
      والبند ٦ لا يكتب طفرةً معيبة. وسلامةُ الماسحات مفحوصةٌ (test_bawwaba.py) لا مبرهنة.
  ٤ج. سجلُّ «ما ضُبطتُ عليه» في CLAUDE.md لا ينقص (قرار المالك 2026-10-21، 12:15–12:16: «موافق على الاصلاح»، ثمّ خيارُ «الاثنان:
      ابنِ فحص البوّابة أيضًا (موصى به)»، و«موصى به» وسمُ البنّاء): كلُّ بندٍ فيه عند الأساس (نقطةِ التقاء ٤أ) حاضرٌ الآن بنصّه، أو
      بصمتُه (sha256 لنصّه) مسجَّلةٌ في tahaqquq/dabt_maadhun.json بسببٍ وإذن — فالإذنُ لنسخةٍ بعينها لا يُعفي ما بعدها، وحقلُ الإذن
      يراجعه المالك في الطلب لا الحارس. سببُه: ثماني دمجاتٍ لـ main في فروعٍ على GitHub (4b4db8f، 43d9179، 5d278a1، dfa7701، 9edde9c،
      b66e004، 79056cf، d3ca615؛ بمسح الدمجات كلّها، `git rev-list --merges --all`) حلّت تعارضَ آخر الملفّ بطرف الفرع فأسقطت من الفرع
      ستّةَ بنودٍ من طرف main، وبلغ فقدُ أربعةٍ منها main. فالتصحيحُ يُضاف بندًا
      جديدًا، وتعديلُ بندٍ قائم يُعدّ غيابًا له. وغيابُ عنوان القسم في الأساس، أو تعذُّرُ الأساس أو قراءتِه، فشلٌ مسمّى.
  ٥. اختبارات بايثون (shabaka/test_shabaka.py) تمرّ، إن وُجد المودَع (MUDAA_MUKHASSAS).
  ٥أ. اختبارات خطّ الأساس والتثبيت (tahaqquq/test_bawwaba.py): رفض JSON التالف وحفظ الحدّ، وفحص بديل تثبيت Lean.
  ٥ب. اختبارات المخزن (mawsua/test_mawsua.py): الفاحص التنفيذيّ المبنيّ من Lean يقبل المخزن ويرفض الفاسد.
  ٥ج. بوّابة الإيداع (mudaat/test_idaa.py): لا ختم بلا إذن ولا نوع، ولا تنظيف؛ وإن عُيّن MUDAA_DIR
      طوبقت بصمات ما حضر من المودَعات فيه.
  ٥هـ. القارئ (tahaqquq/test_qari.py): من النصّ المشكول إلى الخلايا والقانون والمقاطع والمخزن.
  ٥و. العوامل (tahaqquq/test_awamil.py): Jisr/AwamilJadwal.lean مطابقٌ لمودَعه إن حضر (MUDAA_AWAMIL أو MUDAA_DIR).
  ٥ز. نقول الأقسام (tahaqquq/test_aqsam.py): اقتباسات Jisr/AqsamAwamil.lean في أسطرها من المودَعات إن حضرت (MUDAA_DIR).
  ٥ح. جدول الأجناس (tahaqquq/test_ajnas.py): المودَع ajnas.tsv ببصمته، ومطابقة جدول Madlul/Tayin.lean له، وشجرة المخصّص إن حضرت.
  ٥ط. القطعة الثانية والنظامان (tahaqquq/test_jamad.py): ajnas_jamad.tsv وnizam_fizya.tsv وnizam_riyadiyyat.tsv ببصماتها، ومطابقة
      Madlul/Wiratha.lean وMadlul/Jamad.lean لها (الشجرة والثوابت وأسماء القوانين) إن حضرت.
  ٥ي. جدول العلاقات (tahaqquq/test_shabaka.py): alaqat.tsv ببصمته، ومطابقة شبكة Madlul/Shabaka.lean له وقرار «السائل شراب» إن حضر.
  ٥ك. جدول الحواسّ الخمس (tahaqquq/test_hawass.py): hawass.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Madlul/Hawass.lean له إن حضر.
  ٥ل. جدول أوّليات العقل (tahaqquq/test_awwaliyyat.py): awwaliyyat.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Awwaliyyat.lean له إن حضر.
  ٥م. جدول الأزمنة (tahaqquq/test_azmina.py): azmina.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Azmina.lean له إن حضر.
  ٥ن. جدول التجاور المكانيّ (tahaqquq/test_makan.py): makan.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Makan.lean له إن حضر.
  ٥س. جدول المرساة (tahaqquq/test_mirsat.py): mirsat.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Mirsat.lean له إن حضر.
  ٥ع. جدول الرابطة الإسنادية (tahaqquq/test_isnad.py): isnad.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Isnad.lean له إن حضر.
  ٥ف. جدول الجسر إلى الدالّ (tahaqquq/test_jisrdal.py): jisr_dal.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Jisr/JisrDal.lean له إن حضر.
  ٥ق. جدول النِّسَب على الأصناف (tahaqquq/test_nisab_asnaf.py): nisab_asnaf.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Jisr/NisabAsnaf.lean له إن حضر.
  ٥ر. جدول اللزوم من شبكة المعاجم (tahaqquq/test_luzum.py): نصّ Madlul/JadwalLuzum*.lean، والعيّنة المضمَّنة دائمًا، والمقاييس واللسان
      ببصمتيهما ومطابقة جدول Lean لاختيار المولِّد إن حضرا (MUDAA_DIR).
  ٥ش. فرضية الـ116 (tahaqquq/test_fard116.py): مرآةُ آلة الجذر على أعداد SLGE/Root.lean، وحالاتٌ يدويّة دائمًا؛ وإعادةُ المخرج ومطابقةُ
      Madlul/Fard116Data.lean وMadlul/Fard116Shawahid.lean له بالبايت إن حضر المودَعان.
  ٥ت. أطلس الجسور (tahaqquq/test_atlas.py): كلّ وحدة Lean مسجَّلة بطبقتها في Nizam/atlas.tsv، ووصلُها بالمحرّك مطابقٌ لرسم الاستيراد.
  ٥ث. حوادث الدمج (tahaqquq/test_hawadith.py): على تاريخ git الحقيقيّ، ٤أ يسمّي ما أسقطه 767e09b (7) وfeb12a8 (4)، و٤ج يسمّي بنودَ
      «ما ضُبطتُ عليه» التي أسقطتها الدمجاتُ الثماني؛ بلا تاريخٍ لا يُشغَّل.
  ٥ذ. منفّذ القياس المسجَّل (tahaqquq/test_qiyas_d.py): qiyas_d.py ووضعُ القياس في القارئ على بياناتٍ مصنوعة وكلماتٍ باليد، لا على المرجعين
      (التسجيل المسبق hawkama/tasjil_qiyas_d.md).
  ٥ض. جدول القواعد، صفُّ الأسماء الستّة (tahaqquq/test_qawaid.py): خلايا Jisr/QawaidJadwal.lean (مولَّد) والمولِّدُ نفسُه على صورٍ يدويّة،
      ونصُّ Jisr/QawaidSitta.lean، وأعدادُ القوانين في Nizam/QawaidB.lean (`qawaninB_qiyam`) وأعدادُ «كَتَبَ»/«كُتِبَ» في Dal/Adad.lean
      محسوبةً من الصور اليدوية بصيغة التحليل بحدّيها، دائمًا؛ وqawaid.tsv ببصمته (مرشّح أو مختوم) ومطابقةُ المولَّد له بايتًا واقتباساتُه في
      أسطرها إن حضر.
  ٥ظ. الواقع المختوم والتعريفات (tahaqquq/test_waqi.py): المولِّدُ على جدولٍ يدويّ، وقواعدُ الاستخراج، ورفضُ الحاسّة الفاشلة بلا كتابة،
      ومرآةُ الحكم بأحكامٍ يدويّة قبل الختم وبعده، ونصُّ قاعدة الحكم في Aql/Waqi.lean، دائمًا؛ وwaqi_001.tsv وtaarifat.tsv ببصمتيهما
      (مرشّحين أو مختومين)، والمولَّدُ بايتًا، وكلُّ صفٍّ من سجلّ الحواسّ، والمخرجاتُ الخامّة ببصماتها، وإعادةُ المشاهدات الحتميّة، وأعدادُ
      Aql/WaqiShawahid.lean، والتعريفاتُ مستخرجةً ثانيةً من مصادرها (وثلاثٌ بنصٍّ يدويّ)، إن حضرا.
  ٥ص. ضابطُ باب الجزاء المجمَّد (tahaqquq/test_jaza.py؛ hawkama/منهج_الضوابط.md في طلبه): بصماتُ التجميد، والمولَّدُ بايتًا، وآخرُ نتيجةٍ
      لبصمة الشفرة الحاليّة بأعداد مبرهنتها، وأعدادُ المجال من الحالات نفسها، دائمًا؛ والأسانيدُ في أسطرها إن حضر الكتاب.
  ٥ص٢. ضابطُ نفي الفعل وحروفِ الفعل المجمَّد (tahaqquq/test_nafy.py؛ الكتاب س9755–9787): مثلُ ٥ص على Jisr/NafyFil.lean.
  ٥ص٣. ضابطُ باب الفاء المجمَّد (tahaqquq/test_fa.py؛ الكتاب س8914–9049): مثلُ ٥ص على Jisr/BabFa.lean.
  ٥ص٤. ضابطُ مجاري أواخر الكلم المجمَّد (tahaqquq/test_majari.py؛ الكتاب س111–233): مثلُ ٥ص على Jisr/MajariKalim.lean.
  ٥ص٥. ضابطُ الوقف على أواخر الكلم المتحرّكة المجمَّد (tahaqquq/test_waqf.py؛ الكتاب س17782–17859): مثلُ ٥ص على Dal/WaqfSibawayhi.lean.
  ٥ص٦. ضابطُ بقيّة أبواب الجزاء المجمَّد (tahaqquq/test_jaza2.py؛ الكتاب س9305–9652): مثلُ ٥ص على Jisr/BaqiJaza.lean.
  ٥ص٧. ضابطُ «من النصّ إلى الإطار» المجمَّد لستّة أشكالٍ من ل1 (tahaqquq/test_nass.py؛ القطر والألفية في الأسماء الستّة): مثلُ ٥ص على Jisr/NassItar.lean،
      والمولَّدُ خلاياه من القارئ (`qari --khalaya`)، ووضعُ الإطار في القارئ (`qari --itar`) بتوقّعٍ يدويّ.
  ٥ر٢. شبكةُ الدلالة (tahaqquq/test_tasis.py): الإغلاقُ بالتعريف على صفوف Madlul/JadwalLuzumData.lean بتنفيذٍ مستقلّ (الدورُ فهم–عقل،
      والإغلاقُ من «كتب»، والأساسُ الأدنى)، ومبرهناتُ Madlul/TasisDalala.lean مدقّقة، ومرآةُ الجدول الكامل shabaka/tasis_dalala.py بتوقّعاتٍ
      يدويّة على الصفوف الثلاثين، دائمًا؛ والاقتباساتُ في أسطرها إن حضر المودَع.
  ٥ص٨. ضابطُ «صكّ الجملة» المجمَّد (tahaqquq/test_sakk.py؛ الكتاب والمغني والقطر والألفية والشخصيّة ج1 وج3): مثلُ ٥ص على
      Jisr/SakkJumla.lean، وذهبُ NABT الخمسُ والعشرون منقولًا يدويًّا يطابق dhahab25، وبملفّ NABT نفسِه إن حضر.
  ٥ت٢. تحصيلُ النصّ ومحاذاتُه (tahaqquq/test_tahsil.py؛ Dal/Tahsil.lean والأداة tahsil): على عرّافٍ مستقلٍّ كتبه مؤلّفٌ لم يقرأ إلّا المواصفة
      (tahaqquq/tahsil/) — بصماتُ المواصفة والعرّاف وحالاته، وحالاتُ الحدود المشتقّةُ باليد، و7000 نصٍّ عشوائيّ، وحكمُ الفاحص على شهادة كلّ
      مقطع، وخلايا القارئ (`qari --khalaya`) على الكلمات المرخَّصة، وأسماءُ الأحكام في المواصفة، دائمًا.
  ٥ت٣. هيكلُ الإنتروبيا (tahaqquq/test_intrubiya.py؛ Jisr/Intrubiya.lean وJisr/IntrubiyaShahada.lean وscripts/intrubiya.py): تعدادٌ صريحٌ لكلمات
      الطول 3 وتجميعٌ حتى 4 يساويان أعدادَ lawCount المنسوخة من Lean، والشهادةُ المولَّدة بالبايت ومتباينتاها بأعدادٍ صحيحة، والمقدِّراتُ على
      توزيعاتٍ باليد، والنقلُ بالجسر قبل الآلة، وجدولُ nabtBridge، والتحصيلُ على كلماتٍ خلاياها باليد، دائمًا؛ وعلى المودَع إن حضر في MUDAA_DIR.
  ٥خ. تمامُ التدقيق (tahaqquq/test_tadqiq_tamm.py؛ 2026-10-26؛ مقترحُ البنّاء بأمر المالك العامّ، يسري بعد دمج طلبه): كلُّ مبرهنةٍ عامّةٍ
      في وحدات المشروع (SLGE وDal وMadlul وJisr وAql وNizam وFaahis وQari؛ تصريحٌ تسبق اسمَه في سطره theorem أو lemma) لها `#print axioms`
      في Audit.lean خارج التعليقات — من ملفّات `.ilean` التي يكتبها lake build؛ فالبند ٣ يعدّ ما في Audit.lean، وهذا يمنع أن تُبنى مبرهنةٌ
      ولا تُدقَّق.
  ٥غ. سرعة الفاحص (tahaqquq/test_sura.py؛ س1، 2026-10-24): مضاعفةُ مخزنٍ مولَّد لا تزيد زمنَ المعالج على ثلاثة أضعاف، للفحص وللسؤال —
      يمنع البحثَ الخطّيّ في الأصول أو القوانين (التربيعيّ)، ولا يثبت الخطّيّة. وهو آخرُ IKHTIBARAT_TAFRAT.
  ٦. كلّ طفرة في tafrat.json تُقتل: تُفشل البناء بخطأ Lean في ملفٍّ وسطر (`KHATA_BINA`) أو تُفشل اختبارًا برمزٍ موجب. طفرة تعيش = اختبارٌ مرآة.
     وخروجُ البناء بغير صفرٍ بلا خطأٍ مسمّى (قتلُ المعالج لنفاد الذاكرة؛ وكذلك خطأُ استيرادٍ أو ملفٍّ مفقود بلا سطر — لا طفرةَ اليوم تمسّ
     `import` أو lakefile) أو اختبارٌ قُتل بإشارة: «غيرُ محسومة»، تفشل بها البوّابة باسمها. وحدُّه: اختبارٌ رمزُه موجبٌ قتلٌ ولو كان سببُه
     نفادَ ذاكرةٍ في عمليّةٍ تابعة له أو MemoryError (لا يُشترط سطرُ FAIL/ERROR).
التشغيل: python3 -I tahaqquq/bawwaba.py [--bila-tafrat]
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
# القتلُ بالبناء يُثبته خطأُ Lean في ملفٍّ وسطر؛ وخروجُ lake بغير صفرٍ بلا هذا (قتلُ المعالج لنفاد الذاكرة يُخرجه هكذا) حالٌ ثالثة: لا قتلٌ
# ولا حياة. وكذلك اختبارٌ قُتل بإشارة (رمزٌ سالب). قاعدةٌ واحدة يقرؤها tafrat_juz.py أيضًا.
KHATA_BINA = r"^error: (\S+?):\d+"


def ghayr_mahsum_bina(code, out):
    """سببُ كون خروج `lake build` غيرَ محسوم، أو None: غيرُ صفريّ بلا خطأٍ في ملفٍّ وسطر."""
    if code != 0 and not re.search(KHATA_BINA, out, re.M):
        return f"lake build خرج {code} بلا خطأٍ في ملفٍّ مسمّى"
    return None


def ghayr_mahsum_ikhtibar(x, code):
    """سببُ كون خروج اختبارٍ غيرَ محسوم، أو None: قُتل بإشارة."""
    if code < 0:
        return f"{x} قُتل بالإشارة {-code}"
    return None


# اختباراتُ البند ٦ بترتيبها بعد lake build: قائمةٌ واحدة يقرؤها tafrat_juz.py أيضًا، فلا تفترق الأداتان.
IKHTIBARAT_TAFRAT = (
    "tahaqquq/test_bawwaba.py",
    "mawsua/test_mawsua.py",
    "mudaat/test_idaa.py",
    "tahaqquq/test_qari.py",
    "tahaqquq/test_awamil.py",
    "tahaqquq/test_aqsam.py",
    "tahaqquq/test_ajnas.py",
    "tahaqquq/test_jamad.py",
    "tahaqquq/test_shabaka.py",
    "tahaqquq/test_hawass.py",
    "tahaqquq/test_awwaliyyat.py",
    "tahaqquq/test_azmina.py",
    "tahaqquq/test_makan.py",
    "tahaqquq/test_mirsat.py",
    "tahaqquq/test_isnad.py",
    "tahaqquq/test_jisrdal.py",
    "tahaqquq/test_nisab_asnaf.py",
    "tahaqquq/test_luzum.py",
    "tahaqquq/test_fard116.py",
    "tahaqquq/test_atlas.py",
    "tahaqquq/test_hawadith.py",
    "tahaqquq/test_qiyas_d.py",
    "tahaqquq/test_qawaid.py",
    "tahaqquq/test_waqi.py",
    "tahaqquq/test_nabt_vendor.py",
    "tahaqquq/test_nabt_cli.py",
    "tahaqquq/test_nabt_bridge.py",
    "tahaqquq/test_nabt_runner.py",
    "tahaqquq/test_jaza.py",
    "tahaqquq/test_nafy.py",
    "tahaqquq/test_fa.py",
    "tahaqquq/test_majari.py",
    "tahaqquq/test_waqf.py",
    "tahaqquq/test_jaza2.py",
    "tahaqquq/test_nass.py",
    "tahaqquq/test_sakk.py",
    "tahaqquq/test_tadqiq_tamm.py",
    "tahaqquq/test_tasis.py",
    "tahaqquq/test_tahsil.py",
    "tahaqquq/test_intrubiya.py",
    # آخرُها عمدًا: نموُّ الزمن (س1) لا يقتل إلّا طفرةً لا تغيّر الدلالة (P466، P467)، فلا يجري إلّا على ما نجا ممّا قبله.
    "tahaqquq/test_sura.py",
)


def run(cmd, cwd=ROOT, timeout=1800):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def strip_comments(src):
    src = re.sub(r"/-.*?-/", "", src, flags=re.S)
    return re.sub(r"--.*", "", src)


def load_baseline(path):
    with open(path, encoding="utf-8") as f:
        base = json.load(f)
    if (not isinstance(base, dict)
            or type(base.get("mubarhanat")) is not int
            or base["mubarhanat"] < 0):
        raise ValueError("mubarhanat يجب أن يكون عددًا صحيحًا غير سالب")
    return base["mubarhanat"]


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout


def asmaa_tafrat(text):
    """أسماءُ الطفرات من نصّ tafrat.json؛ ما ليس قائمةَ قيودٍ لكلٍّ منها «ism» نصّيٌّ يُرفض باسمه."""
    data = json.loads(text)
    if not isinstance(data, list) or not all(isinstance(t, dict) and isinstance(t.get("ism"), str) for t in data):
        raise ValueError("tafrat.json يجب أن يكون قائمةً، لكلّ قيدٍ فيها «ism» نصّيّ")
    return [t["ism"] for t in data]


def mahdhufa_maadhuna(text):
    """سجلُّ الحذف المأذون (tahaqquq/tafrat_mahdhufa.json): قائمةُ {ism، sabab، idhn} لا حقلَ فيها فارغ."""
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("tafrat_mahdhufa.json يجب أن يكون قائمة")
    for t in data:
        if not isinstance(t, dict) or not all(isinstance(t.get(k), str) and t[k].strip() for k in ("ism", "sabab", "idhn")):
            raise ValueError(f"قيدُ حذفٍ بلا ism أو sabab أو idhn: {t}")
    return [t["ism"] for t in data]


def tafrat_naqisa(asas, hali, mahdhufa):
    """طفراتُ الأساس الغائبةُ عن القائمة الحاليّة بلا قيدِ حذفٍ مأذون — كلٌّ منها حذفٌ صامت."""
    return sorted(set(asas) - set(hali) - set(mahdhufa))


UNWAN_DABT = "## ما ضُبطتُ عليه"


def bunud_dabt(text):
    """بنودُ قسم «ما ضُبطتُ عليه»: من السطر التالي لعنوانه إلى العنوان التالي «## » أو آخر الملفّ. البندُ سطرٌ أوّلُه «- » وما يليه
    حتّى البند التالي؛ والأسطرُ الفارغة لا تدخل، وبياضُ أواخر الأسطر يُقصّ. وكلُّ سطرٍ غيرِ فارغ لا يبدأ بـ«- » (تتمّةٌ ببياض، أو
    فقرةٌ، أو «### ») يُلحق بالبند قبله، فيُعدّ تغييرًا له — خطأٌ نحو الفشل لا نحو المرور. وغيابُ العنوان خطأٌ مسمّى (ValueError)."""
    lines = [line.rstrip() for line in text.split("\n")]
    if UNWAN_DABT not in lines:
        raise ValueError(f"لا عنوانَ «{UNWAN_DABT}» في CLAUDE.md")
    bunud, cur = [], None
    for line in lines[lines.index(UNWAN_DABT) + 1:]:
        if line.startswith("## "):
            break
        if line.startswith("- "):
            if cur is not None:
                bunud.append("\n".join(cur))
            cur = [line]
        elif line and cur is not None:
            cur.append(line)
    if cur is not None:
        bunud.append("\n".join(cur))
    return bunud


def basma_band(band):
    """بصمةُ البند: sha256 لنصّه كما يقرؤه `bunud_dabt`."""
    return hashlib.sha256(band.encode("utf-8")).hexdigest()


def dabt_maadhun(text):
    """سجلُّ الإذن (tahaqquq/dabt_maadhun.json): قائمةُ {basma، awwal، sabab، idhn} — basma بصمةُ نسخة البند المأذونِ تغييرُها أو
    حذفُها (64 خانةً ستّ‑عشريّة)، وawwal سطرُها الأوّل للقارئ — لا حقلَ فيها فارغ."""
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("dabt_maadhun.json يجب أن يكون قائمة")
    for t in data:
        if not isinstance(t, dict) or not all(isinstance(t.get(k), str) and t[k].strip() for k in ("basma", "awwal", "sabab", "idhn")):
            raise ValueError(f"قيدُ إذنٍ بلا basma أو awwal أو sabab أو idhn: {t}")
        if not re.fullmatch(r"[0-9a-f]{64}", t["basma"]):
            raise ValueError(f"basma ليست sha256: {t['basma']}")
    return [t["basma"] for t in data]


def dabt_naqis(asas, hali, maadhun):
    """بنودُ الأساس التي ليست في الحاليّ بنصّها ولا إذنَ لبصمتها — أسطرُها الأولى بترتيبها في الأساس."""
    hali, maadhun = set(hali), set(maadhun)
    return [b.split("\n")[0] for b in asas if b not in hali and basma_band(b) not in maadhun]


# ٤ب. نصُّ الطفرة. القاعدتان بإذن المالك (2026-10-19 16:16، مكمّلتين لـ٤أ): «min» يقع في ملفّه مرّةً واحدة، ولا يقع في
# تعليق. سببُهما: P152_joinTrailing_bila_fasil وقع «min»ها أوّلًا في تعليقٍ فعاشت، و`replace(min, ila, 1)` يصيب أوّلَ موضعٍ
# وحده — فإن تكرّر النصّ أو وقع في تعليقٍ صارت الطفرةُ تفحص غيرَ ما سُمّيت له. والتعليقُ يُفحص بوجهين (قراءةُ البنّاء): موضعُ
# «min» في تعليق الأصل أو في بياضٍ بين تعليقه، أو أثرُ الطفرة لا يتعدّى التعليق (يُطرح التعليق من الأصل والمطفَّر ويُقارن
# الباقيان بلا أسطرٍ فارغة ولا بياضِ أواخر — `musawwa`)؛ ورفعُ التعليق بحذف علامته يُقبل متى أمكن مسحُ الناتج وتغيّر ما
# خارج التعليق (التوجيه: «إذا كان الأثر تغييرًا تنفيذيًا حقيقيًا»؛ الفحصُ هنا نحويّ، والأثرُ السلوكيّ يحكم به البند ٦ بالقتل).
# وما فوق القاعدتين: الحقولُ نصوص، والملفُّ داخل المستودع (المطلقُ و«..» مرفوضان، والحكمُ على المسار الحقيقيّ فلا هروبَ
# برابطٍ رمزيّ)، وامتدادُه ممّا تُعرف فيه قاعدةُ التعليق (.lean .py .sh، وبلا تعليق .tsv .json؛ وما سواها مرفوضٌ باسمه)،
# والاسمُ غيرُ مكرَّر بلا استثناء. اعتُمدت هي والاستثناءُ بتوجيهٍ رفعه المالك (2026-10-19 18:02) وأمر بتنفيذه.
# وسلامةُ الماسحات «مفحوصة» (tahaqquq/test_bawwaba.py بطفراته) لا «مبرهنة»: كفايتُها لكلّ صيغةٍ آتية غيرُ مبرهنة.
# حدودُ الماسحات (معلنة): Lean — النصوصُ المُدرَجة بلا «!» (throwError "…{…}…") لا يُعرف إدراجُها، فنصٌّ فيها يُغلق داخل
# إدراجٍ يُرفض الملفُّ «نصٌّ لم يُغلق» (فشلٌ مسمّى لا قبولٌ صامت). sh — لا يُعرف من الإسناد إلّا «#» في أوّل كلمة والاقتباس
# بأنواعه والـheredoc. بايثون — التوثيقُ جملةُ نصٍّ قائمة (من ast)، إلّا توثيقَ الوحدة إن استُعمل `__doc__` اسمًا حرًّا فيها.

LUGHAT_BILA_TAALIQ = {".tsv", ".json"}


def _taaliq_lean(s):
    """مواضعُ التعليق في نصّ Lean: «--» إلى آخر السطر، و«/- … -/» متداخلًا؛ خارج النصوص (والخامِ منها r#"…"#)، والحروف،
    والأسماء «…»، والنصوص المُدرَجة (s!/m!/f!)."""
    n, spans = len(s), []
    harf = re.compile(r"'(?:\\(?:u\{[0-9a-fA-F]+\}|x[0-9a-fA-F]{2}|.)|[^\\'\n])'")
    kham = re.compile(r'r(#*)"')

    def ism_qabl(i):
        return i > 0 and (s[i - 1].isalnum() or s[i - 1] in "_'!?.")

    def nass(i, mudraj):            # s[i] == '"'؛ يعيد ما بعد الإغلاق
        j = i + 1
        while j < n:
            c = s[j]
            if c == "\\":
                j += 2
            elif c == '"':
                return j + 1
            elif c == "{" and mudraj:
                j = shifra(j + 1, True)
            else:
                j += 1
        raise ValueError("نصٌّ لم يُغلق")

    def shifra(i, ila_qaws):        # يمسح الشيفرة حتّى «}» المقابلة (ila_qaws) أو آخر الملفّ
        umq = 0
        while i < n:
            m = kham.match(s, i) if s[i] == "r" and not ism_qabl(i) else None
            if s.startswith("/-", i):
                j, d = i + 2, 1
                while j < n and d:
                    if s.startswith("/-", j):
                        d, j = d + 1, j + 2
                    elif s.startswith("-/", j):
                        d, j = d - 1, j + 2
                    else:
                        j += 1
                if d:
                    raise ValueError("تعليقٌ كتليّ لم يُغلق")
                spans.append((i, j))
                i = j
            elif s.startswith("--", i):
                j = s.find("\n", i)
                j = n if j < 0 else j
                spans.append((i, j))
                i = j
            elif m:
                ghalq = '"' + m.group(1)
                j = s.find(ghalq, m.end())
                if j < 0:
                    raise ValueError("نصٌّ خامٌ لم يُغلق")
                i = j + len(ghalq)
            elif s[i] == "«":
                j = s.find("»", i + 1)
                if j < 0:
                    raise ValueError("اسمٌ «…» لم يُغلق")
                i = j + 1
            elif s[i] == '"':
                i = nass(i, i > 1 and s[i - 1] == "!" and (s[i - 2].isalnum() or s[i - 2] == "_"))
            elif s[i] == "'" and not ism_qabl(i) and harf.match(s, i):
                i = harf.match(s, i).end()
            elif s[i] == "{":
                umq, i = umq + 1, i + 1
            elif s[i] == "}":
                if umq == 0 and ila_qaws:
                    return i + 1
                umq, i = max(umq - 1, 0), i + 1
            else:
                i += 1
        if ila_qaws:
            raise ValueError("إدراجٌ في نصٍّ لم يُغلق")
        return i

    shifra(0, False)
    return spans


def _taaliq_py(s):
    """مواضعُ التعليق في نصّ بايثون: رموزُ COMMENT (tokenize)، والنصُّ القائمُ جملةً وحده — التوثيق (ast)؛ إلّا توثيقَ
    الوحدة إن استُعمل `__doc__` اسمًا حرًّا فيها، فهو سلوكٌ لا تعليق."""
    import ast
    import io
    import tokenize
    bidayat = [0]                           # tokenize وast يعدّان الأسطر بـ«\n» وحده
    for satr in s.split("\n"):
        bidayat.append(bidayat[-1] + len(satr) + 1)
    asturb = [satr.encode("utf-8") for satr in s.split("\n")]

    def mawdi(satr, amud):                  # tokenize: عمودٌ بالحروف
        return bidayat[satr - 1] + amud

    def mawdi_b(satr, bayt):                # ast: عمودٌ بالبايتات
        return bidayat[satr - 1] + len(asturb[satr - 1][:bayt].decode("utf-8"))

    try:
        rumuz = list(tokenize.generate_tokens(io.StringIO(s, newline="\n").readline))
        shajara = ast.parse(s)
    except (tokenize.TokenError, SyntaxError, ValueError) as e:
        raise ValueError(f"تعذّر تحليل بايثون: {e}")
    spans = [(mawdi(*t.start), mawdi(*t.end)) for t in rumuz if t.type == tokenize.COMMENT]
    doc_mustamal = any(isinstance(u, ast.Name) and u.id == "__doc__" for u in ast.walk(shajara))   # اسمٌ حرّ لا صفة
    for u in ast.walk(shajara):
        if isinstance(u, ast.Expr) and isinstance(u.value, ast.Constant) and isinstance(u.value.value, str):
            if doc_mustamal and isinstance(shajara, ast.Module) and shajara.body and shajara.body[0] is u:
                continue
            spans.append((mawdi_b(u.lineno, u.col_offset), mawdi_b(u.end_lineno, u.end_col_offset)))
    return sorted(spans)


def _taaliq_sh(s):
    """مواضعُ التعليق في نصّ sh: «#» في أوّل كلمةٍ إلى آخر السطر، خارج الاقتباس ('…'، "…"، $'…') وأجسام الـheredoc."""
    n, i, spans, muallaq = len(s), 0, [], []
    heredoc = re.compile(r"<<(-?)\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\2")
    aqwas, ghalq = [], {}    # «$(» يُغلق داخل الكلمة؛ وغيرُه عاملٌ يبدأ بعده تعليق
    while i < n:
        c = s[i]
        m = heredoc.match(s, i) if c == "<" and not s.startswith("<<<", i) else None
        if s.startswith("<<<", i):
            i += 3
        elif s.startswith("$(", i):
            aqwas.append("$(")
            i += 2
        elif c == "(":
            aqwas.append("(")
            i += 1
        elif c == ")":
            ghalq[i] = aqwas.pop() if aqwas else "("
            i += 1
        elif m:
            muallaq.append((m.group(3), bool(m.group(1))))
            i = m.end()
        elif c == "\n" and muallaq:
            i += 1
            for kalima, tab in muallaq:      # أجسامُ الـheredoc بترتيبها حتّى سطر الإغلاق
                while True:
                    if i >= n:
                        raise ValueError(f"heredoc لم يُغلق: {kalima}")
                    j = s.find("\n", i)
                    j = n if j < 0 else j
                    satr = s[i:j]
                    i = min(j + 1, n)
                    if (satr.lstrip("\t") if tab else satr) == kalima:
                        break
            muallaq = []
        elif c == "\\":
            i += 2
        elif c == "$" and s.startswith("$'", i):
            j = i + 2
            while j < n and s[j] != "'":
                j += 2 if s[j] == "\\" else 1
            if j >= n:
                raise ValueError("اقتباسٌ $'…' لم يُغلق")
            i = j + 1
        elif c == "'":
            j = s.find("'", i + 1)
            if j < 0:
                raise ValueError("اقتباسٌ مفردٌ لم يُغلق")
            i = j + 1
        elif c == '"':
            j = i + 1
            while j < n and s[j] != '"':
                j += 2 if s[j] == "\\" else 1
            if j >= n:
                raise ValueError("اقتباسٌ مزدوجٌ لم يُغلق")
            i = j + 1
        elif c == "#" and (i == 0 or s[i - 1] in " \t\n;|&(" or ghalq.get(i - 1) == "("):
            j = s.find("\n", i)
            j = n if j < 0 else j
            spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


# الأنواعُ المدعومة لملفّ الطفرة، حاصرةً (التوجيه: «حصر امتدادات ملفات الطفرات» — «موافق، مع تعريف واضح للأنواع المدعومة» (س194)):
# امتدادٌ له ماسحُ تعليق، أو امتدادٌ لا تعليق فيه. يُقارن الامتدادُ بحروفه كما هي («.LEAN» غيرُ «.lean»)، وما سواها مرفوضٌ باسمه.
LUGHAT_TAALIQ = {".lean": _taaliq_lean, ".py": _taaliq_py, ".sh": _taaliq_sh}
ANWA_MADUMA = frozenset(LUGHAT_TAALIQ) | frozenset(LUGHAT_BILA_TAALIQ)


def mawadi_taaliq(s, imtidad):
    """مواضعُ التعليق [بداية، نهاية) في نصٍّ بلغة امتداده؛ وامتدادٌ ليس في ANWA_MADUMA يُرفض باسمه."""
    if imtidad in LUGHAT_TAALIQ:
        return LUGHAT_TAALIQ[imtidad](s)
    if imtidad in LUGHAT_BILA_TAALIQ:
        return []
    raise ValueError(f"امتدادٌ لا تُعرف فيه قاعدةُ التعليق: {imtidad or '(بلا امتداد)'}")


def bila_taaliq(s, mawadi_t):
    """النصُّ وكلُّ تعليقٍ فيه مسافةٌ واحدة."""
    qita, i = [], 0
    for a, b in mawadi_t:
        qita += [s[i:a], " "]
        i = b
    return "".join(qita + [s[i:]])


def musawwa(t):
    """الباقي بعد طرح التعليق بلا أسطرٍ فارغة ولا بياضٍ في أواخر الأسطر — ويبقى بياضُ أوائلها (إزاحةُ بايثون معنى)."""
    return "\n".join(l.rstrip() for l in t.split("\n") if l.strip())


def mawadi(s, min_):
    """مواضعُ «min» في النصّ كلُّها، المتداخلةُ منها أيضًا."""
    out, i = [], s.find(min_)
    while i >= 0:
        out.append(i)
        i = s.find(min_, i + 1)
    return out


def masar_tafra(t, root):
    """مسارُ ملفّ الطفرة الحقيقيّ إن كان داخل root، وإلّا None (المسار المطلق و«..» والرابطُ الرمزيّ إلى الخارج)."""
    milaf = t["milaf"]
    if os.path.isabs(milaf) or ".." in milaf.replace("\\", "/").split("/"):
        return None
    jidhr = os.path.realpath(root)
    p = os.path.realpath(os.path.join(root, milaf))
    return p if os.path.commonpath([jidhr, p]) == jidhr and p != jidhr else None


def ayb_tafra(t, root):
    """عيبُ نصّ الطفرة نصًّا مسمًّى، أو None إن سلمت (القاعدتان وما فوقهما: انظر رأس ٤ب)."""
    if not isinstance(t, dict) or not all(isinstance(t.get(k), str) for k in ("ism", "milaf", "min", "ila")):
        return "قيدٌ بلا ism أو milaf أو min أو ila نصّيّ"
    milaf = t["milaf"]
    try:
        p = masar_tafra(t, root)
    except ValueError as e:
        return f"مسارٌ لا يُقرأ: {e}"
    if p is None:
        return f"الملفّ خارج المستودع: {milaf}"
    if not t["min"]:
        return "«min» فارغ"
    try:
        with open(p, encoding="utf-8") as f:
            s = f.read()
    except (OSError, ValueError) as e:              # UnicodeDecodeError فرعٌ من ValueError
        return f"تعذّرت قراءة {milaf}: {e}"
    m = mawadi(s, t["min"])
    if len(m) != 1:
        return f"«min» يقع في {milaf} {len(m)} مرّة لا مرّةً واحدة"
    imtidad = os.path.splitext(milaf)[1]
    try:
        tm = mawadi_taaliq(s, imtidad)
    except ValueError as e:
        return f"تعذّر تعيين التعليق في {milaf}: {e}"
    bad, nih = m[0], m[0] + len(t["min"])
    fi_t = [False] * len(s)
    for a, b in tm:
        fi_t[a:b] = [True] * (b - a)
    # «min» في تعليق: كلُّ حرفٍ منه في تعليقٍ أو بياضٌ بين تعليقين، وفيه حرفُ تعليقٍ واحدٌ على الأقلّ
    fi_taaliq = any(fi_t[bad:nih]) and all(fi_t[i] or s[i].isspace() for i in range(bad, nih))
    mutaffar = s[:bad] + t["ila"] + s[nih:]
    try:
        sawa = musawwa(bila_taaliq(mutaffar, mawadi_taaliq(mutaffar, imtidad))) == musawwa(bila_taaliq(s, tm))
    except ValueError:
        sawa = None     # المطفَّر لا يُمسح (أفسد تعليقًا أو نصًّا): الحكمُ بالموضع وحده
    if fi_taaliq and sawa is not False:
        return "«min» يقع في تعليق"
    if sawa:
        return "الطفرة لا تغيّر إلّا تعليقًا"
    # تغيّرت الشيفرة: ومنه رفعُ تعليقٍ بحذف علامته متى أمكن مسحُ الناتج؛ أو أُفسدت بنيتُها من موضعٍ خارج التعليق
    return None


def uyub_tafrat(tafrat, root):
    """عيوبُ القائمة: كلُّ اسمٍ مكرَّر، وكلُّ طفرةٍ معيبةٍ نصًّا — «اسم: عيب»."""
    uyub, raa = [], set()
    for t in tafrat:
        ism = t.get("ism") if isinstance(t, dict) else None
        if isinstance(ism, str):
            if ism in raa:
                uyub.append(f"{ism}: اسمٌ مكرَّر")
            raa.add(ism)
        ayb = ayb_tafra(t, root)
        if ayb:
            uyub.append(f"{ism if isinstance(ism, str) else repr(ism)}: {ayb}")
    return uyub


def main():
    fails, report = [], []
    code, out = run(["lake", "build"])
    report.append(f"١ البناء: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("lake build فشل:\n" + out[-1500:])

    bad = []
    for d in ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari"):
        for root, _, fs in os.walk(os.path.join(ROOT, d)):
            for f in fs:
                if f.endswith(".lean"):
                    src = strip_comments(open(os.path.join(root, f), encoding="utf-8").read())
                    for w in ("sorry", "native_decide"):
                        if re.search(rf"\b{w}\b", src):
                            bad.append(f"{f}: {w}")
                    if re.search(r"^\s*axiom\s", src, re.M):
                        bad.append(f"{f}: axiom")
    report.append(f"٢ المحظورات: {len(bad)}")
    if bad:
        fails.append("محظورات: " + "، ".join(bad))

    code, out = run(["lake", "env", "lean", "Audit.lean"])
    lines = [l for l in out.splitlines() if "depends on axioms" in l or "does not depend" in l]
    nonstd = []
    for l in lines:
        m = re.search(r"\[(.*)\]", l)
        if m and not set(x.strip() for x in m.group(1).split(",")) <= ALLOWED:
            nonstd.append(l)
    report.append(f"٣ التدقيق: {len(lines)} مبرهنة، خارج المسموح {len(nonstd)}")
    if code != 0 or nonstd:
        fails.append("التدقيق: " + ("\n".join(nonstd) or out[-800:]))

    base_p = os.path.join(ROOT, "tahaqquq", "khatt_asas.json")
    try:
        baseline = load_baseline(base_p)
    except (OSError, ValueError) as e:
        report.append("٤ خطّ الأساس: تعذّرت قراءة khatt_asas.json")
        fails.append(f"خطّ الأساس khatt_asas.json غير صالح: {e}")
    else:
        report.append(f"٤ خطّ الأساس: {baseline} ← الآن {len(lines)}")
        if len(lines) < baseline:
            fails.append(f"نقص عدد المبرهنات المدقّقة من {baseline} إلى {len(lines)}")

    # ٤أ. قائمة الطفرات لا تنقص عن الأساس إلّا بقيدٍ مأذون (قرار المالك 2026-10-19). الأساسُ نقطةُ التقاء HEAD بالمرجع
    # (TAFRAT_ASAS_REF، وإلّا origin/main): في CI على الطلب هو قاعدةُ الدمج نفسُها، فيُكشف ما أسقطه دمجٌ بلا تعارض.
    marja = os.environ.get("TAFRAT_ASAS_REF") or "origin/main"
    try:
        code, mb = git("merge-base", "HEAD", marja)
        asas_sha = mb.strip()
        if code != 0 or not asas_sha:
            raise ValueError(f"تعذّر حساب نقطة التقاء HEAD بـ{marja} (اجلب {marja} أو عيّن TAFRAT_ASAS_REF)")
        code, txt = git("show", f"{asas_sha}:tahaqquq/tafrat.json")
        if code != 0:
            raise ValueError(f"تعذّرت قراءة tafrat.json عند {asas_sha[:7]}")
        asas = asmaa_tafrat(txt)
        with open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8") as f:
            hali = asmaa_tafrat(f.read())
        mp = os.path.join(ROOT, "tahaqquq", "tafrat_mahdhufa.json")
        mahdhufa = []
        if os.path.exists(mp):
            with open(mp, encoding="utf-8") as f:
                mahdhufa = mahdhufa_maadhuna(f.read())
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        report.append("٤أ قائمة الطفرات: لم تُقارَن بالأساس")
        fails.append(f"حراسة قائمة الطفرات: {e}")
    else:
        naqisa = tafrat_naqisa(asas, hali, mahdhufa)
        report.append(f"٤أ قائمة الطفرات: الأساس {asas_sha[:7]} ({len(asas)}) ← الآن {len(hali)}؛ غائبٌ بلا إذن {len(naqisa)}")
        if naqisa:
            fails.append("طفراتٌ في الأساس غابت بلا قيدٍ في tahaqquq/tafrat_mahdhufa.json: " + "، ".join(naqisa))

    # ٤ب. نصُّ كلّ طفرة: مرّةً واحدة في ملفّها، وتغييرٌ خارج التعليق، واسمٌ غير مكرَّر (يجري مع --bila-tafrat أيضًا).
    try:
        with open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8") as f:
            tafrat_kull = json.load(f)
        if not isinstance(tafrat_kull, list):
            raise ValueError("tafrat.json ليس قائمة")
    except (OSError, ValueError) as e:
        report.append("٤ب نصوص الطفرات: لم تُفحص")
        fails.append(f"نصوص الطفرات: {e}")
    else:
        uyub = uyub_tafrat(tafrat_kull, ROOT)
        report.append(f"٤ب نصوص الطفرات: {len(tafrat_kull)} طفرة، معيبةٌ {len(uyub)}")
        if uyub:
            fails.append("طفراتٌ معيبةُ النصّ:\n" + "\n".join(uyub))

    # ٤ج. سجلُّ «ما ضُبطتُ عليه» لا ينقص عن الأساس نفسِه (قرار المالك 2026-10-21): كلُّ بندٍ فيه حاضرٌ الآن بنصّه أو مأذون.
    try:
        code, mb = git("merge-base", "HEAD", marja)
        asas_d_sha = mb.strip()
        if code != 0 or not asas_d_sha:
            raise ValueError(f"تعذّر حساب نقطة التقاء HEAD بـ{marja} (اجلب {marja} أو عيّن TAFRAT_ASAS_REF)")
        code, txt = git("show", f"{asas_d_sha}:CLAUDE.md")
        if code != 0:
            raise ValueError(f"تعذّرت قراءة CLAUDE.md عند {asas_d_sha[:7]}")
        asas_d = bunud_dabt(txt)
        cp = os.path.join(ROOT, "CLAUDE.md")
        hali_d = []   # لا CLAUDE.md فلا بنود: يُسمّى كلُّ بندٍ في الأساس
        if os.path.exists(cp):
            with open(cp, encoding="utf-8") as f:
                hali_d = bunud_dabt(f.read())
        mp = os.path.join(ROOT, "tahaqquq", "dabt_maadhun.json")
        maadhun_d = []
        if os.path.exists(mp):
            with open(mp, encoding="utf-8") as f:
                maadhun_d = dabt_maadhun(f.read())
    except (OSError, ValueError, subprocess.SubprocessError) as e:
        report.append("٤ج سجلّ ما ضُبطتُ عليه: لم يُقارَن بالأساس")
        fails.append(f"حراسة سجلّ ما ضُبطتُ عليه: {e}")
    else:
        naqis_d = dabt_naqis(asas_d, hali_d, maadhun_d)
        report.append(f"٤ج سجلّ ما ضُبطتُ عليه: الأساس {asas_d_sha[:7]} ({len(asas_d)} بندًا) ← الآن {len(hali_d)}؛ "
                      f"غائبٌ أو مغيَّرٌ بلا إذن {len(naqis_d)}")
        if naqis_d:
            fails.append("بنودٌ في «ما ضُبطتُ عليه» عند الأساس غابت أو تغيّرت بلا قيدٍ ببصمتها في tahaqquq/dabt_maadhun.json: "
                         + "؛ ".join(b[:100] for b in naqis_d))

    code, out = run([sys.executable, "-I", "tahaqquq/test_bawwaba.py"])
    report.append(f"٥أ اختبارات خطّ الأساس والتثبيت: {'مرّت' if code == 0 else 'فشلت'}")
    if code != 0:
        fails.append("اختبارات خطّ الأساس والتثبيت فشلت:\n" + out[-800:])

    mudaa = os.environ.get("MUDAA_MUKHASSAS")
    if mudaa and os.path.exists(mudaa):
        code, out = run([sys.executable, "-I", "shabaka/test_shabaka.py", mudaa])
        report.append(f"٥ اختبارات الشبكة: {out.strip().splitlines()[-1] if out.strip() else '?'}")
        if code != 0:
            fails.append("اختبارات الشبكة فشلت:\n" + out[-800:])
    else:
        report.append("٥ اختبارات الشبكة: لم تُشغَّل (المودَع غير حاضر؛ عيّن MUDAA_MUKHASSAS)")

    code, out = run([sys.executable, "-I", "mawsua/test_mawsua.py"])
    report.append(f"٥ب اختبارات المخزن: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات المخزن فشلت:\n" + out[-800:])

    code, out = run([sys.executable, "-I", "mudaat/test_idaa.py"])
    report.append(f"٥ج بوّابة الإيداع: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات الإيداع فشلت:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_qari.py"])
    report.append(f"٥هـ القارئ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات القارئ فشلت:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_awamil.py"])
    report.append(f"٥و العوامل: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار العوامل فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_aqsam.py"])
    report.append(f"٥ز نقول الأقسام: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار نقول الأقسام فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_ajnas.py"])
    report.append(f"٥ح جدول الأجناس: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأجناس فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_jamad.py"])
    report.append(f"٥ط القطعة الثانية والنظامان: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار القطعة الثانية والنظامين فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_shabaka.py"])
    report.append(f"٥ي جدول العلاقات: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول العلاقات فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_hawass.py"])
    report.append(f"٥ك جدول الحواسّ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الحواسّ فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_awwaliyyat.py"])
    report.append(f"٥ل جدول الأوّليات: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأوّليات فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_azmina.py"])
    report.append(f"٥م جدول الأزمنة: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأزمنة فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_makan.py"])
    report.append(f"٥ن جدول التجاور المكانيّ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول التجاور المكانيّ فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_mirsat.py"])
    report.append(f"٥س جدول المرساة: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول المرساة فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_isnad.py"])
    report.append(f"٥ع جدول الرابطة الإسنادية: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الرابطة الإسنادية فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_jisrdal.py"])
    report.append(f"٥ف جدول الجسر إلى الدالّ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الجسر إلى الدالّ فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nisab_asnaf.py"])
    report.append(f"٥ق جدول النِّسَب على الأصناف: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول النِّسَب على الأصناف فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_luzum.py"])
    report.append(f"٥ر جدول اللزوم: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول اللزوم فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_fard116.py"])
    report.append(f"٥ش فرضية الـ116: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار فرضية الـ116 فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_atlas.py"])
    report.append(f"٥ت أطلس الجسور: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار أطلس الجسور فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_hawadith.py"])
    report.append(f"٥ث {out.strip().splitlines()[-1] if out.strip() else 'حوادث الدمج: ?'}")
    if code != 0:
        fails.append("اختبار حادثتي الدمج فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_qiyas_d.py"])
    report.append(f"٥ذ منفّذ القياس المسجَّل: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار منفّذ القياس المسجَّل فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_qawaid.py"])
    report.append(f"٥ض جدول القواعد (الأسماء الستّة): {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول القواعد فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_waqi.py"])
    report.append(f"٥ظ الواقع المختوم والتعريفات: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار الواقع المختوم فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nabt_vendor.py"])
    report.append(f"٥ NABT تثبيت المصدر: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("اختبار تثبيت مصدر NABT فشل:\n" + out[-1500:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nabt_cli.py"])
    report.append(f"٥ NABT واجهة التشغيل: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("اختبار واجهة NABT فشل:\n" + out[-1500:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nabt_bridge.py"])
    report.append(f"٥ NABT الجسر التنفيذي: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("اختبار جسر NABT فشل:\n" + out[-1500:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nabt_runner.py"])
    report.append(f"٥ NABT منفّذ التحقق: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("اختبار منفّذ تحقق NABT فشل:\n" + out[-1500:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_jaza.py"])
    report.append(f"٥ص {out.strip().splitlines()[-1] if out.strip() else 'ضابط باب الجزاء: ?'}")
    if code != 0:
        fails.append("اختبار ضابط باب الجزاء فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nafy.py"])
    report.append(f"٥ص٢ {out.strip().splitlines()[-1] if out.strip() else 'ضابط نفي الفعل: ?'}")
    if code != 0:
        fails.append("اختبار ضابط نفي الفعل فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_fa.py"])
    report.append(f"٥ص٣ {out.strip().splitlines()[-1] if out.strip() else 'ضابط باب الفاء: ?'}")
    if code != 0:
        fails.append("اختبار ضابط باب الفاء فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_majari.py"])
    report.append(f"٥ص٤ {out.strip().splitlines()[-1] if out.strip() else 'ضابط مجاري أواخر الكلم: ?'}")
    if code != 0:
        fails.append("اختبار ضابط مجاري أواخر الكلم فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_waqf.py"])
    report.append(f"٥ص٥ {out.strip().splitlines()[-1] if out.strip() else 'ضابط الوقف: ?'}")
    if code != 0:
        fails.append("اختبار ضابط الوقف فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_jaza2.py"])
    report.append(f"٥ص٦ {out.strip().splitlines()[-1] if out.strip() else 'ضابط بقيّة أبواب الجزاء: ?'}")
    if code != 0:
        fails.append("اختبار ضابط بقيّة أبواب الجزاء فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_nass.py"])
    report.append(f"٥ص٧ {out.strip().splitlines()[-1] if out.strip() else 'ضابط من النصّ إلى الإطار: ?'}")
    if code != 0:
        fails.append("اختبار ضابط من النصّ إلى الإطار فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_sakk.py"])
    report.append(f"٥ص٨ {out.strip().splitlines()[-1] if out.strip() else 'ضابط صكّ الجملة: ?'}")
    if code != 0:
        fails.append("اختبار ضابط صكّ الجملة فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_tasis.py"])
    report.append(f"٥ر٢ {out.strip().splitlines()[-1] if out.strip() else 'شبكة الدلالة: ?'}")
    if code != 0:
        fails.append("اختبار شبكة الدلالة فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_tahsil.py"])
    report.append(f"٥ت٢ {out.strip().splitlines()[-1] if out.strip() else 'التحصيل: ?'}")
    if code != 0:
        fails.append("اختبار التحصيل فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_intrubiya.py"])
    report.append(f"٥ت٣ {out.strip().splitlines()[-1] if out.strip() else 'الإنتروبيا: ?'}")
    if code != 0:
        fails.append("اختبار هيكل الإنتروبيا فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_tadqiq_tamm.py"])
    report.append(f"٥خ {out.strip().splitlines()[-1] if out.strip() else 'تمامُ التدقيق: ?'}")
    if code != 0:
        fails.append("اختبار تمام التدقيق فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_sura.py"])
    report.append(f"٥غ سرعة الفاحص (نموٌّ غير تربيعيّ): {' · '.join(out.strip().splitlines()) if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار نموّ زمن الفاحص فشل:\n" + out[-800:])
    mdir = os.environ.get("MUDAA_DIR")
    if mdir and os.path.isdir(mdir):
        code, out = run([sys.executable, "-I", "mudaat/idaa.py", "tahaqqaq", mdir])
        report.append(f"٥د بصمات المودَعات الحاضرة: {out.count('مطابق')} مطابق، {out.count('تغيّر')} تغيّر")
        if code != 0:
            fails.append("مودَع تغيّرت بصمته:\n" + out)

    if "--bila-tafrat" not in sys.argv:
        tafrat = json.load(open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8"))
        alive, ghayr = [], []
        for t in tafrat:
            tmp = tempfile.mkdtemp()
            dst = os.path.join(tmp, "p")
            # تُنسخ مخرجات البناء (.lake) أيضًا ليكون بناء الطفرة تدريجيًّا لا من الصفر
            shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns("__pycache__", "mustakshif", "jalsa_haqiqiyya_out"))
            # لا كتابةَ بطفرةٍ معيبة: يُحكم على المستودع نفسِه (النسخُ يحوّل الرابطَ الرمزيّ ملفًّا)، ثمّ على النسخة
            ayb = ayb_tafra(t, ROOT) or ayb_tafra(t, dst)
            if ayb:
                ism = t.get("ism") if isinstance(t, dict) else repr(t)
                alive.append(f"{ism} (٤ب: {ayb})")
                shutil.rmtree(tmp)
                continue
            path = masar_tafra(t, dst)
            s = open(path, encoding="utf-8").read()
            open(path, "w", encoding="utf-8").write(s.replace(t["min"], t["ila"], 1))
            code, out = run(["lake", "build"], cwd=dst)
            sabab_ghayr = ghayr_mahsum_bina(code, out)
            for x in IKHTIBARAT_TAFRAT:
                if code != 0:
                    break
                code, _ = run([sys.executable, "-I", x], cwd=dst)
                sabab_ghayr = ghayr_mahsum_ikhtibar(x, code)
            if sabab_ghayr:
                ghayr.append(f"{t['ism']} ({sabab_ghayr})")
            elif code == 0:
                alive.append(t["ism"])
            shutil.rmtree(tmp)
        report.append(f"٦ الطفرات: قُتلت {len(tafrat) - len(alive) - len(ghayr)} من {len(tafrat)}"
                      + (f"، وغيرُ محسومة {len(ghayr)}" if ghayr else ""))
        if alive:
            fails.append("طفرات عاشت: " + "، ".join(alive))
        if ghayr:
            fails.append("طفرات غيرُ محسومة (لا قتلٌ ولا حياة؛ تُعاد): " + "، ".join(ghayr))
    else:
        report.append("٦ الطفرات: تُركت بطلب (--bila-tafrat)")

    print("\n".join(report), flush=True)   # التقرير أوّلًا ثمّ الأسباب، بترتيبٍ واحد حين يُجمع المخرجان (2>&1) في الخطّاف
    if fails:
        print("\n".join(fails), file=sys.stderr, flush=True)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
