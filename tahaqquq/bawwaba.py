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
  ٤ب. نصُّ كلّ طفرة (قرار المالك 2026-10-19 16:16، مكمّلًا لـ٤أ): «min» غيرُ فارغٍ يقع في ملفّه مرّةً واحدة (بعدّ المتداخل)،
      والطفرةُ تغيّر الملفَّ خارج التعليق (Lean: «--» و«/- -/» متداخلًا؛ بايثون: التعليق والتوثيق؛ sh: «#»)، والملفُّ داخل
      المستودع بامتدادٍ معروف، والاسمُ غيرُ مكرَّر. يجري مع --bila-tafrat أيضًا.
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


# ٤ب. نصُّ الطفرة (قرار المالك 2026-10-19 16:16، مكمّلًا لـ٤أ): «min» يقع في ملفّه مرّةً واحدة، والطفرةُ تغيّر شيئًا خارج
# التعليق. سببُه: P152 وقع «min»ها أوّلًا في تعليقٍ فعاشت، و`replace(min, ila, 1)` يصيب أوّلَ موضعٍ وحده — فإن تكرّر النصّ
# أو انتقل إلى تعليقٍ صارت الطفرةُ تفحص غيرَ ما سُمّيت له وهي «مقتولة» أو «حيّة» لغير سببها.

LUGHAT_BILA_TAALIQ = {".tsv", ".json"}


def _taaliq_lean(s):
    """مواضعُ التعليق في نصّ Lean: «--» إلى آخر السطر، و«/- … -/» متداخلًا؛ خارج النصوص والحروف والنصوص المُدرَجة (s!/m!/f!)."""
    n, spans = len(s), []
    harf = re.compile(r"'(?:\\(?:u\{[0-9a-fA-F]+\}|x[0-9a-fA-F]{2}|.)|[^\\'\n])'")

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
            elif s[i] == '"':
                i = nass(i, i > 1 and s[i - 1] == "!" and (s[i - 2].isalnum() or s[i - 2] == "_"))
            elif s[i] == "'" and not (i > 0 and (s[i - 1].isalnum() or s[i - 1] in "_'!?.")) and harf.match(s, i):
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
    """مواضعُ التعليق في نصّ بايثون: رموزُ COMMENT، والنصُّ القائمُ جملةً وحده (التوثيق) — من tokenize نفسِه."""
    import io
    import tokenize
    bidayat = [0]
    for satr in s.splitlines(keepends=True):
        bidayat.append(bidayat[-1] + len(satr))
    mawdi = lambda rc: bidayat[rc[0] - 1] + rc[1]
    try:
        rumuz = [t for t in tokenize.generate_tokens(io.StringIO(s).readline) if t.type != tokenize.NL]
    except (tokenize.TokenError, SyntaxError) as e:
        raise ValueError(f"تعذّر ترميز بايثون: {e}")
    fasl = (tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER)
    spans, sabiq = [], None
    for k, t in enumerate(rumuz):
        if t.type == tokenize.COMMENT:
            spans.append((mawdi(t.start), mawdi(t.end)))
            continue
        if t.type == tokenize.STRING and (sabiq is None or sabiq in fasl):
            lahiq = next((u.type for u in rumuz[k + 1:] if u.type != tokenize.COMMENT), tokenize.ENDMARKER)
            if lahiq in fasl:
                spans.append((mawdi(t.start), mawdi(t.end)))
        sabiq = t.type
    return spans


def _taaliq_sh(s):
    """مواضعُ التعليق في نصّ sh: «#» في أوّل كلمةٍ إلى آخر السطر، خارج الاقتباس."""
    n, i, spans = len(s), 0, []
    while i < n:
        c = s[i]
        if c == "\\":
            i += 2
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
        elif c == "#" and (i == 0 or s[i - 1] in " \t\n;|&()"):
            j = s.find("\n", i)
            j = n if j < 0 else j
            spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


def mawadi_taaliq(s, imtidad):
    """مواضعُ التعليق [بداية، نهاية) في نصٍّ بلغة امتداده؛ وامتدادٌ لا تُعرف فيه قاعدةُ التعليق يُرفض باسمه."""
    if imtidad == ".lean":
        return _taaliq_lean(s)
    if imtidad == ".py":
        return _taaliq_py(s)
    if imtidad == ".sh":
        return _taaliq_sh(s)
    if imtidad in LUGHAT_BILA_TAALIQ:
        return []
    raise ValueError(f"امتدادٌ لا تُعرف فيه قاعدةُ التعليق: {imtidad or '(بلا امتداد)'}")


def bila_taaliq(s, imtidad):
    """النصُّ وكلُّ تعليقٍ فيه مسافةٌ واحدة."""
    qita, i = [], 0
    for a, b in mawadi_taaliq(s, imtidad):
        qita += [s[i:a], " "]
        i = b
    return "".join(qita + [s[i:]])


def mawadi(s, min_):
    """مواضعُ «min» في النصّ كلُّها، المتداخلةُ منها أيضًا."""
    out, i = [], s.find(min_)
    while i >= 0:
        out.append(i)
        i = s.find(min_, i + 1)
    return out


def ayb_tafra(t, root):
    """عيبُ نصّ الطفرة نصًّا مسمًّى، أو None إن سلمت: الحقولُ نصوص، والملفُّ داخل المستودع، و«min» غيرُ فارغٍ ويقع مرّةً
    واحدة، والطفرةُ تغيّر الملفَّ خارج التعليق (تعليقُ الأصل والمطفَّر يُطرح ثمّ يُقارَن الباقيان)."""
    if not all(isinstance(t.get(k), str) for k in ("ism", "milaf", "min", "ila")):
        return "قيدٌ بلا ism أو milaf أو min أو ila نصّيّ"
    milaf = t["milaf"]
    if os.path.isabs(milaf) or ".." in milaf.replace("\\", "/").split("/"):
        return f"الملفّ خارج المستودع: {milaf}"
    if not t["min"]:
        return "«min» فارغ"
    try:
        with open(os.path.join(root, milaf), encoding="utf-8") as f:
            s = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return f"تعذّرت قراءة {milaf}: {e}"
    m = mawadi(s, t["min"])
    if len(m) != 1:
        return f"«min» يقع في {milaf} {len(m)} مرّة لا مرّةً واحدة"
    imtidad = os.path.splitext(milaf)[1]
    try:
        asl = bila_taaliq(s, imtidad)
    except ValueError as e:
        return f"تعذّر تعيين التعليق في {milaf}: {e}"
    mutaffar = s[:m[0]] + t["ila"] + s[m[0] + len(t["min"]):]
    try:
        if bila_taaliq(mutaffar, imtidad) == asl:
            return "الطفرة لا تغيّر إلّا تعليقًا"
    except ValueError:
        pass                                # المطفَّر لا يُقرأ تعليقُه: تغييرٌ في الشيفرة لا في التعليق
    return None


def uyub_tafrat(tafrat, root):
    """عيوبُ القائمة: كلُّ اسمٍ مكرَّر، وكلُّ طفرةٍ معيبةٍ نصًّا — «اسم: عيب»."""
    uyub, raa = [], set()
    for t in tafrat:
        ism = t.get("ism") if isinstance(t, dict) else None
        if isinstance(ism, str) and ism in raa:
            uyub.append(f"{ism}: اسمٌ مكرَّر")
        raa.add(ism)
        ayb = ayb_tafra(t, root) if isinstance(t, dict) else "قيدٌ ليس كائنًا"
        if ayb:
            uyub.append(f"{ism}: {ayb}")
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
            path = os.path.join(dst, t["milaf"])
            s = open(path, encoding="utf-8").read()
            if t["min"] not in s:
                alive.append(f"{t['ism']} (الاقتباس غاب: عدّل الطفرة مع الكود)")
                shutil.rmtree(tmp)
                continue
            open(path, "w", encoding="utf-8").write(s.replace(t["min"], t["ila"], 1))
            code, _ = run(["lake", "build"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_bawwaba.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "mawsua/test_mawsua.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "mudaat/test_idaa.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_qari.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_awamil.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_aqsam.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_ajnas.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_jamad.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_shabaka.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_hawass.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_awwaliyyat.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_azmina.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_makan.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_mirsat.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_isnad.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_jisrdal.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_nisab_asnaf.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_luzum.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_fard116.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_atlas.py"], cwd=dst)
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
