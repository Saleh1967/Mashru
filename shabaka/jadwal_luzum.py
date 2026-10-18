"""جدولُ اللزوم من شبكة المعاجم: مقاييس اللغة (ابن فارس) ولسان العرب (ابن منظور)، المودَعان المختومان.

لا يقرأ إلّا المودَعين ببصمتيهما في mudaat/sijill.json (يُرفض أيّ ملفٍّ تغيّرت بصمته باسمه).
المخرجات (في MUDAA_DIR، لا في المستودع — المودَعات ومشتقّاتها لا تُرفع):
  jard_judhur.tsv  : جردُ الجذور في المعجمين بعدد حروفها (المقيس على المودَع كلّه).
  luzum_mujam.tsv  : القضايا الأولى المشهودة: juz (جزءُ التفسير)، taraduf (تفسيرٌ بلفظٍ واحد)،
                     luzum (لازمٌ بجملة تعليل)، kharij (نقيضٌ/ضدٌّ/خلاف)، asl (أصلُ ابن فارس) — لكلٍّ سطرُه.

القواعد المعلنة (تعيينات البنّاء، لا نصوصٌ من المعجمين؛ كلٌّ منها باسمه في المخرج):
  R1 التطبيع: تُحذف الحركات والتطويل؛ أ إ آ ؤ ئ ← ء؛ ى ← ي؛ ة ← ت (تاءُ زيادة).
  R2 الجذر من اللفظ — من المودَع لا من صرفٍ مفروض: «صيغةُ الجذر R» كلُّ لفظٍ يفسّره اللسانُ في مادّة R نفسِها
     («W: …» وW يحمل حروف R بترتيبها)، والجذرُ نفسُه. ولفظُ التفسير يُقرأ بأقلّ نزعٍ يوجد به صيغةً مشهودة
     (بلا نزع، ثمّ بنزع لاحقة ضمير، ثمّ سابقة و/ف/ب/ك/ل، ثمّ «ال»). صيغةٌ لجذرٍ واحد ← «متعيّن»؛ لأكثر ← «محتمل»
     بكلّ جذورها. فإن لم توجد صيغةُ تفسير فالورود (R2-ب): صورةٌ وردت في نصّ مادّة R نفسِها تحمل R وكلُّ زائدٍ عليها
     من «سألتمونيها». لا صيغة ولا ورود ← «لا جذر». المحتملُ ولا جذر لا يدخلان Lean (لا حكم).
     والزوائدُ في صيغ التفسير أيضًا من العشرة لا غير (سيبويه، الكتاب س18540–18564: «هذا باب علم حروف الزوائد وهي عشرة أحرف»: الهمزة
     والألف والهاء والياء والنون والتاء والسين والميم والواو واللام). والبحثُ بدرجة النزع أوّلًا (أداةُ التعريف لا تُعدّ نزعًا)، وفي الدرجة صيغُ التفسير قبل الورود ثمّ أقلُّ قلبًا.
  R2-ج «الأصلُ عدمُ الإعلال»: إذا بقي أكثرُ من مرشّح قُدّم أقلُّهم قلبًا لحرف العلّة («ريح» لـ ريح قبل روح)؛ والألفُ المنقلبة
     تساوي الواوَ والياء فتبقى محتملة («صار»). ولغةُ المعجم عن الدالّ («اسم»، «ابن» في الإسناد، «بالكسر»…) خارجُ التفسير (STOP_WASF)، وحروفُ المعاني (STOP_HARF)
     ولو بسابقة («وفي»، «فلما»)؛ والسابقةُ مع أداة التعريف («وال…»، «بال…»، «لل…») تُنزع قطعًا قبل المحاذاة.
  R3 تفسيرُ اللسان: في مادّة الجذر A جملةٌ «W: G» وW (كلمة أو كلمتان) من A بقاعدة R2 ← G مدلولُ W مطابقةً.
     جذورُ G المتعيّنة (غير A، وغير أدوات القائمة STOP): واحدٌ ← taraduf، أكثر ← juz لكلٍّ منها (أجزاءُ الحدّ).
     G يبدأ بنقيض/ضدّ/خلاف ← kharij لما بعده لا juz. وصيغةُ الختم («والله أعلم») تُحذف من G (FORMULA).
  R3-ب G معطوفاتٌ (2–4 كلمات، كلٌّ بعد الأولى بالواو، ولكلٍّ جذرٌ متعيّن: «عقلته وعرفته») ← taraduf لكلٍّ لا juz.
  R4 أصلُ ابن فارس: في أوّل مادّة الجذر «أصلٌ … يدلّ على X» أو «أصلٌ …، وهو X» أو «حروفُ A X» ← asl لجذور X المتعيّنة؛
     والجملةُ التي تنفي الأصل أو تحيل على غيره أو تعرّبه («ليست أصلا»، «كالذي قبله»، «فارسي»…) لا تُقرأ أصلًا (ASL_NAFY).
  R5 التعليل: جملةٌ في مادّة A فيها «لأن…» أو «سُمّي/سمّيت … بذلك/به/بها لـ…»، وفيها علامةُ تسميةٍ أو اشتقاق
     (سُمّي، اشتُقّ، ومنه، ومن الباب، ومن ذلك، قيل له… — TASMIYA؛ فـ«لأن» في الاحتجاج لا تكفي) ← luzum لجذور جملة السبب.
     واللفظُ المسمّى آخرُ لفظٍ من A قبل السبب (W). ولا لزومَ بغير جملة تعليل (لا يُستنتج اللزوم من الانتساب إلى الجذر).
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/jadwal_luzum.py [--check]
  --check: يعيد بناء الجدولين ويطابق بصمتيهما بما في MUDAA_DIR (قياسٌ قابلٌ للإعادة).
"""
import collections
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARAKAT = re.compile("[ً-ْـٰ]")
ZIYADA = set("ءاسلتمونيه")
STOP = set("""من الى على في عن ما لا ان او ثم قد كل بعض هو هي هم ذلك ذاك هذا هذه الذي التي الذين اذا اذ كان يكون
قال يقال قيل اي به بها له لها منه منها فيه فيها عليه عليها اليه معروف ايضا مثل نحو غير بين حتى لم لن الا انه
وهو وهي ولا كما فهو فهي عند واحد""".split())
# متغيّرا التفسير: «الشيء» و«فلان» خانةُ المعمول في الحدّ لا جزءٌ من المدلول (تعيين البنّاء، STOP_MUTAGHAYYIR)
STOP |= {"شيء", "الشيء", "فلان", "فلانا"}
# الأدوات بصور الهمزة (R1 يجعل الهمزة ء فلا تطابق صورها بلا همز)
STOP |= set("إلى أن إن أو أي إذا إذ أما إلا أيضا أنه إنه أنها إنها أنهم إنهم إنما أنما أين ألا أم".split())
STOP |= set("ليس ليست لست يعني وقيل بذاك وذاك كذا كذلك هنا".split())
# حروفُ المعاني (أبوابُ مغني اللبيب) لا جذرَ لها في التفسير (STOP_HARF)
STOP |= set("لما لو لولا كي إذن بل لكن ثم حيث متى أين كيف هل قد سوف".split())
# لغةُ المعجم عن الدالّ لا عن المدلول (STOP_WASF): «اسم» وصفُ اللفظ علمًا، و«ابن» في الإسناد إلى العلماء، وأسماءُ الحركات والحروف
STOP |= set("اسم أسماء واسم ابن بالكسر بالفتح بالضم بالتحريك بالتشديد بالتخفيف الواو الياء الألف الهمزة".split())
# صيغُ الختم في نصّ المعجم ليست من التفسير (FORMULA)
FORMULA = re.compile(r"[،,]?\s*و?الله\s+ءعلم.*$")
# R5: جملةُ التعليل تُقبل إذا كان فيها علامةُ تسميةٍ أو اشتقاق (TASMIYA)، لا كلُّ «لأن»
TASMIYA = re.compile(r"سمي|سميت|يسمي|تسمي|سموا|سموه|سمته|اشتق|مشتق|ومنه|ومن الباب|ومن ذلك|ومن هذا|قيل له|قيل لها")
METHA_N = ("نقيض", "ضد", "خلاف")
# أنماطُ النصّ المطبَّع (R1 يجعل «على» علي و«لأن» لءن)
TAALIL = re.compile(r"(لءن\S*|لان(?:ه|ها|هم)?\b|(?:سمي|سميت|يسمي|تسمي|سموا)\S*\s+(?:بذلك|به|بها)\s+ل(?=\S))(.*)")
YADULL = re.compile(r"[يت]دل\S*\s+(?:\S+\s+)?علي\s+(.+?)(?:[.،:;]|$)")
WAHUWA = re.compile(r"ءصل[^.،]{0,20}،\s*وهو\s+(.+?)(?:[.،:;]|$)")
# جملُ ابن فارس التي تنفي الأصل أو تحيل أو تعرّب لا تُقرأ أصلًا (ASL_NAFY)
ASL_NAFY = re.compile(r"ليس|ليست|لا وجه|فارسي|معرب|كالذي|مثل الذي|كالباب|قليل|لا ينقاس|ليس بشيء|مهمل")
METHA = ("نقيض", "ضد", "خلاف")


def basma(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sijill():
    d = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    return {v["milaf"]: v for v in (d.values() if isinstance(d, dict) else d)}


def norm(s):
    s = HARAKAT.sub("", s)
    s = re.sub("[أإآؤئ]", "ء", s)
    return s.replace("ى", "ي").replace("ة", "ت")


STOP = {norm(w) for w in STOP}


def satr(line):
    """نصُّ السطر بلا علامات OpenITI."""
    return re.sub(r"^(### \$ |### \| |# |~~)", "", line).strip()


# ---------------- الجرد ----------------

def bab_huruf(ism):
    """حرفُ الباب في اللسان (ترتيبُه على آخر حرفٍ من الجذر): «ب»، «حرف الهمزة»، «فصل الثاء المثلثة»، «و- ي».
    None لما ليس بابَ حرف (المقدّمة، العنوانُ الخالي) فلا يُفحص العنوانُ عليه."""
    t = norm(ism.strip())
    if t.startswith("حرف الهمزت"):
        return {"ء"}
    if t.startswith("فصل الثاء"):
        return {"ث"}
    if re.fullmatch(r"و\s*-\s*ي", t):
        return {"و", "ي", "ا"}
    if re.fullmatch(r"[\u0621-\u064A]", t):
        return {t}
    return None


def mawadd_lisan(lines):
    """مادّةٌ لكلّ «### $ R:» مقبول (jadhr_sahih، وآخرُ حرفٍ منه حرفُ بابه — ترتيبُ ابن منظور على أواخر الجذور):
    (جذر، سطر البدء، أسطر). والعنوانُ المرفوض («وفي حديث أنس: …» في باب الباء) سطرٌ من مادّته لا يقطعها."""
    out, cur, bab = [], None, None
    for i, ln in enumerate(lines, 1):
        mb = re.match(r"^### \| (.*)$", ln)
        if mb:
            bab = bab_huruf(mb.group(1))
        m = re.match(r"^### \$ ([^:\s]+):", ln)
        if m and jadhr_sahih(norm(m.group(1))) and (bab is None or norm(m.group(1))[-1] in bab):
            cur = [norm(m.group(1)), i, []]
            out.append(cur)
        elif m:  # عنوانٌ مرفوض (سطرٌ من وسط المادّة عُلّم بعلامة العنوان): يبقى في مادّته
            pass
        elif ln.startswith("### "):
            cur = None
        if cur is not None:
            cur[2].append((i, ln))
    return out


def mawadd_maqayis(lines):
    """مادّةٌ لكلّ «### | (R)»؛ والعناوين بلا قوسين تُعدّ وتُترك باسمها."""
    out, cur, bila = [], None, 0
    for i, ln in enumerate(lines, 1):
        if ln.startswith("### "):
            m = re.match(r"^### \| \(([^)\s]+)\)\s*$", ln)
            if m:
                cur = [norm(m.group(1)), i, []]
                out.append(cur)
                continue
            if not re.match(r"^### \| \[", ln):
                bila += 1
            cur = None
        elif cur is not None:
            cur[2].append((i, ln))
    return out, bila


# ---------------- الجذر من اللفظ (R2) ----------------

LAWAHIQ = ("تموه", "تما", "تم", "تن", "هما", "كما", "هم", "هن", "ها", "كم", "كن", "نا", "وا", "ته", "تها", "ه", "ك", "ي", "ت")


def jadhr_sahih(r):
    """عنوانُ جذرٍ مقبول: 2–5 حروفٍ عربيّة، ولا ألفَ فيه إلّا آخرَ ثلاثيٍّ (المعتلّ الآخر المكتوب بالألف في اللسان:
    بغا، سوا، فتا — آخرُه حرفُ علّةٍ غيرُ معيَّن). وما سوى ذلك ممّا فيه ألف (قال، خالد، عطاء…) أسطرٌ من وسط المادّة
    عُلّمت بعلامة العنوان، تُعدّ مرفوضةً باسمها."""
    if not (2 <= len(r) <= 5 and re.fullmatch("[\u0621-\u064A]+", r)):
        return False
    return "ا" not in r or (len(r) == 3 and r.index("ا") == 2)


def bila_tarif(w, n):
    """أداةُ التعريف «ال» في أوّل اللفظ حرفا زيادة لا حرفا جذر، والألفُ وحدها في أوّله زائدة (ألف الوصل)."""
    if w.startswith("ال") and len(w) - 2 >= n:
        return w[2:]
    if w.startswith("ا"):
        return w[1:]
    return w


# مواضعُ الزوائد (قراءةُ البنّاء لباب علم حروف الزوائد، الكتاب س18541–18564، معلنة — ZIYADA_MAWADI):
#   الهمزة أوّلًا (أفعل) أو آخرًا؛ الألف حيث شاءت؛ الهاء آخرًا («لتبين بها الحركة … الندبة»)؛ الياء أوّلًا ووسطًا وآخرًا؛
#   النون أوّلًا ووسطًا وآخرًا (فعلان، زعفران، قلنسوة)؛ التاء أوّلًا (تفعل، تجفاف) ووسطًا (عفريت) وآخرًا (طلحة)؛
#   السين في «استفعل» وحدها («وأما السين فتزاد في استفعل»)؛ الميم أوّلًا وحدها («وأما الميم فتزاد أولا في مفعول»)؛
#   الواو وسطًا وآخرًا (حوقل، قعود، بهلول)؛ اللام آخرًا (عبدل). وكافُ الضمير آخرًا.
MAWDI = {
    "ء": "ب_ا", "ا": "بوا", "ه": "ا", "ي": "بوا", "ن": "بوا", "ت": "بوا", "س": "ب", "م": "ب", "و": "وا", "ل": "ا", "ك": "ا",
}


def zawaid_faqat(R, w):
    """W يحمل R وكلُّ حرفٍ زائدٍ عليه من حروف سيبويه العشرة في موضعٍ يجيزه بابُه (MAWDI: ب سابقةٌ، و وسطٌ، ا لاحقة)،
    والسينُ السابقةُ لا تكون إلّا في «است…». والألفُ وأداةُ التعريف في أوّل اللفظ زائدتان (bila_tarif)."""
    w = bila_tarif(w, len(R))
    i, pos = 0, []
    for j, c in enumerate(w):
        if i < len(R) and (c == R[i] or (R[i] in "ويا" and c in "ويا")):
            pos.append(j)
            i += 1
    if i < len(R):
        return False
    first, last = pos[0], pos[-1]
    for j, c in enumerate(w):
        if j in pos:
            continue
        mawdi = "ب" if j < first else ("ا" if j > last else "و")
        if c not in MAWDI or mawdi not in MAWDI[c]:
            return False
        if c == "س" and mawdi == "ب" and not (j + 1 < len(w) and w[j + 1] == "ت"):
            return False
    return True


def ilal(R, w):
    """عددُ حروف العلّة في R التي قابلها في W حرفٌ غيرُها (قلب)، بالمحاذاة الجشعة نفسِها."""
    w = bila_tarif(w, len(R))
    i, n = 0, 0
    for c in w:
        if i < len(R) and (c == R[i] or (R[i] in "ويا" and c in "ويا")):
            n += c != R[i]
            i += 1
    return n


def ilal_adna(cands, w):
    """R2-ج «الأصلُ عدمُ الإعلال»: من المرشّحين أقلُّهم قلبًا؛ والتساوي يبقى محتملًا بكلّ المتساوين."""
    cs = list(cands)
    m = min(ilal(R, w) for R in cs)
    return [R for R in cs if ilal(R, w) == m]


def yahmil(R, w):
    """W يحمل حروف R بترتيبها (وحرفُ العلّة في R يقابل ا/و/ي)."""
    it = iter(w)
    return all(any(c == x or (c in "ويا" and x in "ويا") for x in it) for c in R)


def nuzu(t):
    """صورُ اللفظ بترتيب النزع: بلا نزع، ثمّ لاحقة، ثمّ سابقة (مرّتين)، ثمّ «ال»، ومركّباتها — أقلُّها نزعًا أوّلًا."""
    seen, out = set(), []

    def add(x, k):
        if len(x) >= 2 and x not in seen:
            seen.add(x)
            out.append((k, x))
    # السابقةُ وأداةُ التعريف معًا («وال…»، «فال…»، «بال…»، «كال…»، «لل…») قاطعةٌ: لا قراءةَ لها حروفَ جذر
    m0 = re.match(r"^([وف]?[بكل]?)(ال|ل(?=ل))(.{2,})$", t)
    if m0 and m0.group(1):
        t = m0.group(3) if m0.group(2) == "ال" else t[len(m0.group(1)):]
    add(t, 0)
    for suf in LAWAHIQ:  # لاحقتان على الأكثر (تاءُ التأنيث ثمّ ضمير: «معرفتك»)
        if t.endswith(suf) and len(t) - len(suf) >= 2:
            t1 = t[: -len(suf)]
            add(t1, 1)
            for suf2 in LAWAHIQ:
                if t1.endswith(suf2) and len(t1) - len(suf2) >= 2:
                    add(t1[: -len(suf2)], 2)
    level = [(0, t)] + [(k, x) for k, x in list(out) if k >= 1]
    for _ in range(2):
        nxt = []
        for k, x in level:
            if len(x) > 3 and x[0] in "وفبكل":
                add(x[1:], k + 1)
                nxt.append((k + 1, x[1:]))
        level += nxt
    for k, x in list(out):
        for p in ("ال", "لل"):
            if x.startswith(p) and len(x) - len(p) >= 2:
                add(x[2:], k + 1)
    out.sort(key=lambda kx: kx[0])
    return out


class Jadhr:
    def __init__(self, mawadd):
        self.roots = {R for R, _, _ in mawadd if jadhr_sahih(R)}
        self.siyagh = collections.defaultdict(set)
        for R in self.roots:
            self.siyagh[R].add(R)
        for R, _, body in mawadd:
            if R not in self.roots:
                continue
            for _, s, _ in jumal(body):
                for mm in re.finditer(r"((?:[\u0621-\u064A\u064B-\u0652]+ ?){1,2}): ", s):
                    for w in mm.group(1).split():
                        hamala = [f for _, f in nuzu(norm(w)) if len(f) >= len(R) and zawaid_faqat(R, f)]
                        if hamala:  # أكثرُ الصور نزعًا ممّا يحمل حروف R: الصيغةُ المجرّدة من السوابق واللواحق
                            self.siyagh[hamala[-1]].add(R)
        # R2-ب الورود: صورةٌ وردت في نصّ مادّة R نفسِها، تحمل R وزوائدُها من سألتمونيها — احتياطٌ بعد صيغ التفسير
        self.wurud = collections.defaultdict(set)
        for R, _, body in mawadd:
            if R not in self.roots:
                continue
            for _, ln in body:
                for w in kalimat(satr(ln)):
                    w = norm(w)
                    if len(w) < len(R) or w in self.siyagh:
                        continue
                    for _, f in reversed(nuzu(w)):
                        if len(f) >= len(R) and zawaid_faqat(R, f):
                            self.wurud[f].add(R)
                            break
        self.cache = {}

    def mursh(self, tok):
        tok = norm(tok)
        if tok in self.cache:
            return self.cache[tok]
        res = frozenset()
        suwar = nuzu(tok)
        harf = len(tok) <= 5 and tok[0] in "وفبكل" and tok[1:] in STOP  # «وفي»، «فلما»: سابقةٌ وحرف
        if tok not in STOP and not harf and not any(f in STOP for _, f in suwar):
            # درجةُ النزع بلا أداة التعريف أوّلًا (أقلُّها)؛ وفي الدرجة: صيغُ التفسير قبل الورود، ثمّ أقلُّ قلبًا (R2-ج)
            daraja = collections.defaultdict(list)
            for k, f in suwar:
                daraja[k - (1 if ("ال" + f) in tok else 0)].append(f)
            for kk in sorted(daraja):
                for tab in (self.siyagh, self.wurud):
                    kulfa = {}
                    for f in daraja[kk]:
                        for R in tab.get(f, ()):
                            kulfa[R] = min(kulfa.get(R, 9), ilal(R, f))
                    if kulfa:
                        m = min(kulfa.values())
                        res = frozenset(R for R, c in kulfa.items() if c == m)
                        break
                if res:
                    break
        self.cache[tok] = res
        return res


def kalimat(s):
    return re.findall(r"[ء-يـً-ْ]+", s)


# ---------------- الاستخراج ----------------

def norm_map(s):
    """التطبيع R1 مع خريطة المواضع إلى النصّ الأصل (الحذفُ حرفًا حرفًا والإبدالُ حرفٌ بحرف)."""
    out, idx = [], []
    for i, c in enumerate(s):
        if HARAKAT.match(c):
            continue
        out.append(norm(c))
        idx.append(i)
    return "".join(out), idx


def jumal(lines_with_no):
    """تجمع أسطر المادّة نصًّا متّصلًا، ثمّ تقطّعه جملًا على . ؛ — لكلّ جملةٍ (سطرُ بدئها، نصُّها، دالّةُ سطرِ موضعٍ فيها)."""
    buf, starts = "", []
    if not lines_with_no:
        return []
    for no, ln in lines_with_no:
        t = satr(ln)
        if not t or t.startswith("Page") or t.startswith("PageV"):
            continue
        starts.append((len(buf) + 1, no))
        buf += " " + re.sub(r"ms\d+|«\d+»|PageV\d+P\d+", " ", t)
    out, pos = [], 0
    for part in re.split(r"(?<=[.؛])", buf):
        lead = len(part) - len(part.lstrip())
        base = pos + lead

        def satr_at(k, base=base):
            return max((n for (o, n) in starts if o <= base + k), default=lines_with_no[0][0])
        if part.strip():
            out.append((satr_at(0), part.strip(), satr_at))
        pos += len(part)
    return out


def tasnif(J, toks, self_root, majma=None):
    """جذور الكلمات: (متعيّنة بترتيبها بلا تكرار، عدد المحتملة). majma (اختياريّ) تُلحق به الكلماتُ المحتملة بمرشّحيها."""
    muayyan, muhtamal = [], 0
    for t in toks:
        c = J.mursh(t) - {self_root}
        if len(c) == 1:
            r = next(iter(c))
            if r not in muayyan:
                muayyan.append(r)
        elif len(c) > 1:
            muhtamal += 1
            if majma is not None:
                majma.append((self_root, norm(t), tuple(sorted(c))))
    return muayyan, muhtamal


def qanun_sigha(tok, R):
    """الصيغةُ المجرّدة للّفظ من جذره R: أكثرُ صوره نزعًا ممّا يحمل حروف R (كبناء صيغ التفسير في Jadhr)."""
    hamala = [f for _, f in nuzu(norm(tok)) if len(f) >= len(R) and zawaid_faqat(R, f)]
    return hamala[-1] if hamala else norm(tok)


def tasnif_siyagh(J, toks, self_root):
    """كـ tasnif، مع صيغة كلّ كلمةٍ متعيّنة: [(الجذر، الصيغة)] بلا تكرار جذر."""
    out, seen = [], set()
    for t in toks:
        c = J.mursh(t) - {self_root}
        if len(c) == 1:
            r = next(iter(c))
            if r not in seen:
                seen.add(r)
                out.append((r, qanun_sigha(t, r)))
    return out


def lisan_qadaya(J, mawadd, hiss=None, majma=None):
    """hiss (اختياريّ): قائمةٌ تُلحق بها مشاهداتُ المعنى (A، صيغة W، صيغُ A في حدّ التفسير، القضيّة، B، صيغة B، السطر):
    مفتاحُ سيبويه (الكتاب س247–251): «اتفاق اللفظين واختلاف المعنيين … وجدت عليه من الموجدة ووجدت إذا أردت وجدان
    الضالة» — المعنى يتعيّن بالصيغة ومصدرها، فصيغُ الجذر المتجاورة في حدّ تفسيرٍ واحد معنًى واحد."""
    rows, ihsa = [], collections.Counter()
    for A, start, body in mawadd:
        for no, s, satr_at in jumal(body):
            # R5 التعليل
            ns, imap = norm_map(s)
            m = TAALIL.search(ns)
            if m and TASMIYA.search(ns):
                pre = ns[: m.start()]
                hamil = [norm(t) for t in kalimat(pre) if A in J.mursh(t)]
                if hamil:
                    mu, mh = tasnif(J, kalimat(m.group(2))[:8], A)
                    ihsa["taalil_jumla"] += 1
                    for B in mu:
                        rows.append(("lisan", A, hamil[-1], "luzum", B, satr_at(imap[m.start()]), s[:160]))
            # R3 التفسير «W: G»
            for mm in re.finditer(r"(?:^|[،,\s])((?:[ء-يً-ْ]+ ?){1,2}): ([^:]+?)(?=$|[.؛]| [ء-يً-ْ]+:)", s):
                W, G = mm.group(1).split(), mm.group(2)
                if not any(A in J.mursh(w) for w in W):
                    continue
                gt = kalimat(FORMULA.sub("", norm(G)))
                if not gt:
                    continue
                w_raw = next(w for w in W if A in J.mursh(w))
                wn = norm(w_raw)
                k_w = mm.start(1) + mm.group(1).index(w_raw)
                ihsa["tafsir"] += 1
                if norm(gt[0]).lstrip("و") in METHA_N and len(gt) > 1:
                    mu, _ = tasnif(J, gt[1:4], A)
                    for B in mu[:1]:
                        rows.append(("lisan", A, wn, "kharij", B, satr_at(k_w), s[:160]))
                    continue
                mu, mh = tasnif(J, gt[:8], A, majma)
                ihsa["muhtamal_kalimat"] += mh
                if hiss is not None:
                    bnd = max(s.rfind(c, 0, k_w) for c in ".؛:")
                    hadd = tuple(sorted({qanun_sigha(t, A) for t in kalimat(s[bnd + 1:mm.end(1)]) if A in J.mursh(t)}))
                    wf = qanun_sigha(w_raw, A)
                    sig = dict(tasnif_siyagh(J, gt[:8], A))
                    matuf = len(gt) >= 2 and len(gt) <= 4 and all(norm(t).startswith("و") for t in gt[1:]) and len(mu) == len(gt)
                    naw_h = "taraduf" if (matuf or len(mu) == 1) else "juz"
                    for B in mu:
                        hiss.append((A, wf, hadd, naw_h, B, sig.get(B, B), satr_at(k_w)))
                matufat = len(gt) >= 2 and len(gt) <= 4 and all(norm(t).startswith("و") for t in gt[1:]) and len(mu) == len(gt)
                if matufat:  # R3-ب: معطوفاتٌ مترادفة لا أجزاءُ حدّ
                    for B in mu:
                        rows.append(("lisan", A, wn, "taraduf", B, satr_at(k_w), s[:160]))
                    continue
                if len(mu) == 1:
                    rows.append(("lisan", A, wn, "taraduf", mu[0], satr_at(k_w), s[:160]))
                else:
                    for B in mu:
                        rows.append(("lisan", A, wn, "juz", B, satr_at(k_w), s[:160]))
    return rows, ihsa


def maqayis_qadaya(J, mawadd):
    rows, ihsa = [], collections.Counter()
    for A, start, body in mawadd:
        js = jumal(body)
        if not js:
            continue
        no0, s0, _ = js[0]
        n0 = norm(s0)
        m = YADULL.search(n0) or WAHUWA.search(n0)
        if ASL_NAFY.search(n0) and not YADULL.search(n0):
            ihsa["asl_manfi"] += 1
            phrase = ""
        elif m:
            ihsa["asl_yadull"] += 1
            phrase = m.group(1)
        else:
            m2 = re.match(r"^(?:ال\S+\s+(?:و\S+\s+){1,4})(?!ءصل|ءصيل|كلم|ليس)(.+?)(?:[.،]|$)", n0)
            phrase = m2.group(1) if m2 else ""
            if phrase:
                ihsa["asl_mubashir"] += 1
        if phrase:
            mu, _ = tasnif(J, kalimat(phrase)[:6], A)
            for B in mu:
                rows.append(("maqayis", A, A, "asl", B, no0, s0[:160]))
        for no, s, satr_at in js:
            ns, imap = norm_map(s)
            mt = TAALIL.search(ns)
            if mt and not TASMIYA.search(ns):
                mt = None
            hamil = [t for t in kalimat(ns[: mt.start()]) if A in J.mursh(t)] if mt else []
            if hamil:
                ihsa["taalil_jumla"] += 1
                mu, _ = tasnif(J, kalimat(mt.group(2))[:8], A)
                for B in mu:
                    rows.append(("maqayis", A, hamil[-1], "luzum", B, satr_at(imap[mt.start()]), s[:160]))
    return rows, ihsa


def hawami(rows, A, ahad=True):
    """جيرانُ A بالقضايا المتعيّنة (اتّجاهُ A→B، ومعكوسًا إن طُلب) مع شاهد كلٍّ: (قضيّة، معجم، سطر)."""
    out = collections.defaultdict(list)
    for r in rows:
        if r[1] == A:
            out[r[4]].append((r[3], r[0], int(r[5])))
        elif not ahad and r[4] == A:
            out[r[1]].append(("~" + r[3], r[0], int(r[5])))
    return out


def masar(rows, a, b, ahad=True, hadd=4, tajannub=()):
    """أقصرُ سلسلةٍ من a إلى b على القضايا المتعيّنة (بحثٌ عرضيّ)، مع شاهد كلّ خطوة."""
    adj = collections.defaultdict(dict)
    for r in rows:
        if r[1] in tajannub or r[4] in tajannub:
            continue
        adj[r[1]].setdefault(r[4], (r[3], r[0], int(r[5])))
        if not ahad:
            adj[r[4]].setdefault(r[1], ("~" + r[3], r[0], int(r[5])))
    prev, front = {a: None}, [a]
    for _ in range(hadd):
        nxt = []
        for u in front:
            for v, sh in sorted(adj[u].items()):
                if v not in prev:
                    prev[v] = (u, sh)
                    nxt.append(v)
        front = nxt
        if b in prev:
            break
    if b not in prev:
        return None
    path, v = [], b
    while prev[v] is not None:
        u, sh = prev[v]
        path.append((u, v) + sh)
        v = u
    return list(reversed(path))


def asas(rows, S, budhur=2000, bidhra=20261018, nafidha=100):
    """قياسُ كثافة الصلات المباشرة بين جذور S مقابل خطّ أساسٍ عشوائيٍّ مطابَق الدرجة (نافذةُ رتبةٍ ±nafidha)."""
    import random
    E, deg = set(), collections.Counter()
    for r in rows:
        a, b = r[1], r[4]
        if a != b and frozenset((a, b)) not in E:
            E.add(frozenset((a, b)))
            deg[a] += 1
            deg[b] += 1

    def kathafa(s):
        return sum(1 for i in range(len(s)) for j in range(i + 1, len(s)) if frozenset((s[i], s[j])) in E)
    rk = sorted(deg, key=lambda r: (deg[r], r))
    pos = {r: i for i, r in enumerate(rk)}
    random.seed(bidhra)
    res = []
    for _ in range(budhur):
        res.append(kathafa([rk[random.randint(max(0, pos[x] - nafidha), min(len(rk) - 1, pos[x] + nafidha))] for x in S]))
    obs = kathafa(S)
    return obs, sum(1 for v in res if v >= obs) / budhur, collections.Counter(res)


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    S = sijill()
    paths = {}
    for f in ("lisan.txt", "maqayis.txt"):
        p = os.path.join(D, f)
        if not os.path.exists(p):
            sys.exit(f"المودَع {f} غائب عن MUDAA_DIR")
        if basma(p) != S[f]["sha256"] or S[f]["hala"] != "مختوم":
            sys.exit(f"رُفض {f}: بصمته لا تطابق السجلّ أو غير مختوم")
        paths[f] = p
    L = open(paths["lisan.txt"], encoding="utf-8").read().split("\n")
    M = open(paths["maqayis.txt"], encoding="utf-8").read().split("\n")
    ml = mawadd_lisan(L)
    mm, bila = mawadd_maqayis(M)

    jard = []
    for name, md in (("lisan", ml), ("maqayis", mm)):
        c = collections.Counter(len(r) for r, _, _ in md)
        for k in sorted(c):
            jard.append((name, k, c[k]))
    J = Jadhr(ml)
    rl, il = lisan_qadaya(J, ml)
    rq, iq = maqayis_qadaya(J, mm)
    rows = rl + rq

    def tsv(rows):
        return "".join("\t".join(str(x).replace("\t", " ") for x in r) + "\n" for r in rows)
    t1 = "mujam\tharf\tadad\n" + tsv(jard)
    t2 = "mujam\tA\tW\tqadiyya\tB\tsatr\tnass\n" + tsv(rows)
    o1, o2 = os.path.join(D, "jard_judhur.tsv"), os.path.join(D, "luzum_mujam.tsv")
    if "--asas" in sys.argv:
        S = sys.argv[sys.argv.index("--asas") + 1:]
        obs, p, dist = asas(rows, S)
        print("الصلات المباشرة:", obs, "من", len(S) * (len(S) - 1) // 2, "| P(عشوائيّ ≥ المشاهد) =", p, "| التوزيع:", sorted(dist.items()))
        sys.exit(0)
    if "--masar" in sys.argv:
        i = sys.argv.index("--masar")
        names = sys.argv[i + 1:]
        for a in names:
            for b in names:
                if a != b:
                    print(a, "→", b, ":", masar(rows, a, b), "| غير موجَّه:", masar(rows, a, b, ahad=False))
        sys.exit(0)
    if "--check" in sys.argv:
        ok = all(os.path.exists(o) and hashlib.sha256(t.encode()).hexdigest() == basma(o) for o, t in ((o1, t1), (o2, t2)))
        print("--check:", "مطابق" if ok else "غير مطابق")
        sys.exit(0 if ok else 2)
    open(o1, "w", encoding="utf-8").write(t1)
    open(o2, "w", encoding="utf-8").write(t2)
    print("مواد اللسان:", len(ml), "| مواد المقاييس:", len(mm), "| عناوين المقاييس بلا قوسين:", bila)
    print("الجرد:", jard)
    print("إحصاء اللسان:", dict(il), "| إحصاء المقاييس:", dict(iq))
    print("القضايا:", dict(collections.Counter((r[0], r[3]) for r in rows)))
    print("بصمة luzum_mujam.tsv:", hashlib.sha256(t2.encode()).hexdigest())


if __name__ == "__main__":
    main()
