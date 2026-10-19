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
  ٥ث. حادثتا الدمج (tahaqquq/test_hawadith.py): على تاريخ git الحقيقيّ، ٤أ يسمّي ما أسقطه 767e09b (7) وfeb12a8 (4)؛ بلا تاريخٍ لا يُشغَّل.
  ٦. كلّ طفرة في tafrat.json تُقتل: تُفشل البناء أو تُفشل اختبارات المخزن. طفرة تعيش = اختبارٌ مرآة.
التشغيل: python3 -I tahaqquq/bawwaba.py [--bila-tafrat]
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
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
    report.append(f"٥ث {out.strip().splitlines()[-1] if out.strip() else 'حادثتا الدمج: ?'}")
    if code != 0:
        fails.append("اختبار حادثتي الدمج فشل:\n" + out[-800:])
    mdir = os.environ.get("MUDAA_DIR")
    if mdir and os.path.isdir(mdir):
        code, out = run([sys.executable, "-I", "mudaat/idaa.py", "tahaqqaq", mdir])
        report.append(f"٥د بصمات المودَعات الحاضرة: {out.count('مطابق')} مطابق، {out.count('تغيّر')} تغيّر")
        if code != 0:
            fails.append("مودَع تغيّرت بصمته:\n" + out)

    if "--bila-tafrat" not in sys.argv:
        tafrat = json.load(open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8"))
        alive = []
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
            code, _ = run(["lake", "build"], cwd=dst)
            for x in IKHTIBARAT_TAFRAT:
                if code != 0:
                    break
                code, _ = run([sys.executable, "-I", x], cwd=dst)
            if code == 0:
                alive.append(t["ism"])
            shutil.rmtree(tmp)
        report.append(f"٦ الطفرات: قُتلت {len(tafrat) - len(alive)} من {len(tafrat)}")
        if alive:
            fails.append("طفرات عاشت: " + "، ".join(alive))
    else:
        report.append("٦ الطفرات: تُركت بطلب (--bila-tafrat)")

    print("\n".join(report), flush=True)   # التقرير أوّلًا ثمّ الأسباب، بترتيبٍ واحد حين يُجمع المخرجان (2>&1) في الخطّاف
    if fails:
        print("\n".join(fails), file=sys.stderr, flush=True)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
