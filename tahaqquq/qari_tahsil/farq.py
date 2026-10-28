"""فروقُ القارئ بعد وصله بالتحصيل (Dal/QiraaTahsil.lean) عن القارئ قبله (main ‏09f7b27)، بأسبابها. عدُّ أداةٍ لا اختبار.

الكلماتُ ثلاثُ مجموعات، وأسبابُ الفروق بعدها:
- المستودع: كلُّ كلمةٍ مشكولةٍ متمايزة في ملفّات المستودع النصّيّة عند 09f7b27 (git ls-tree؛ .lean .py .json .md .tsv .txt .toml).
- العشوائيّة بالبذرة 20261029: رؤوسٌ من الحوامل ومقاعد الهمزة والخاصّة وحروفٍ خارج الجدول، بعد كلٍّ منها من صفرٍ إلى علامتين، وصدورٌ بألفٍ
  ولام. وتُعدّ في عمودين: بلا تطويلٍ، وفيها تطويل.
- الموجَّهة، لأنّ المولِّد العشوائيّ قلّما يولّد ما يفترق فيه القارئان: (أ) تطويلٌ مجرّد يُدرج قبل كلّ مقطعٍ وبعده في 1500 كلمةٍ من
  كلمات المستودع بالبذرة 20261030؛ (ب) كلُّ كلمةٍ من المستودع آخرُها واوٌ ثمّ ألف، تُبدَّل علاماتُ الواو (لا شيء، سكون، شدّة، شدّة
  وسكون، ضمّة) وآخرُها (ا، ى، ا ثمّ تطويل، ى ثمّ تطويل).
وسببُ رفض «حرف بلا حركة في غير آخر الكلمة» من مقاطع التحصيل (أداةُ `tahsil`): المقطعُ الفاسدُ قبل تطويل (في أيّ موضع)، أو أوّلَ الكلمة، أو
غيرُ ذلك، أو لا مقطعَ فاسدًا فالرفضُ من وسيط الشدّة بلا حركة. وسببُ اختلاف الخلايا فيما يقبلانه من نصّ الكلمة: ألفٌ آخرَها بعد واوٍ مشدَّدة،
أو ألفٌ أو مقصورةٌ بعد واوٍ يليها تطويلٌ مجرّد، أو تطويلٌ مجرّد، أو غيرُها.
يُقرأ كلٌّ منها بالقارئين في الوصل (`--khalaya`) وفي الوقف (`--qiyas`: الخلايا وحدها إن قبلاها)، ثمّ ما قبله أحدُهما في الوضع البشريّ
(الكلمةُ وحدها للوقف، وقبل «كَتَبَ» للوصل) لمقارنة الخلايا والملاحظات. ويُصنَّف كلُّ فرقٍ: يرفضانه (ونصُّ الرفض قد يختلف)، أو يرفضه
الجديد وحده بسببه، أو يقبله الجديد وحده بسبب رفض القديم، أو يقبلانه بخلايا أو ملاحظاتٍ مختلفة.

التشغيل: python3 -I tahaqquq/qari_tahsil/farq.py <qari القديم> <qari الجديد> <ملفّ المخرج .md>
والقديمُ يُبنى من 09f7b27: git worktree add <مجلّد> 09f7b27 && (cd <مجلّد> && lake build qari).
"""
import collections
import concurrent.futures as cf
import pathlib
import random
import re
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent.parent
ASAS = "09f7b27"
OLD, NEW, MAKHRAJ = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
SIJILL, MAKHZAN = str(JADHR / "mudaat/sijill.tsv"), str(JADHR / "mawsua/makhzan.tsv")

HAWAMIL = list("ءهاعحغخقكجشيضلنرطدتزسصظذثفبمو")
MAQAID = list("أإؤئ")
KHASSA = ["ة", "ى", "آ", "ٱ", "ـ"]
ALAMAT = ["َ", "ُ", "ِ", "ْ", "ً", "ٌ", "ٍ", "ّ"]
KHARIJ = ["ٰ", "ٓ", "ک"]
rng = random.Random(20261029)
TATWIL = "ـ"
MAQTA = re.compile(r"[^\u064b-\u0652][\u064b-\u0652]*")


def wahda():
    x = rng.random()
    ras = rng.choice(HAWAMIL) if x < 0.7 else rng.choice(MAQAID) if x < 0.78 else rng.choice(KHASSA) if x < 0.97 else rng.choice(KHARIJ)
    y = rng.random()
    al = [] if y < 0.2 else [rng.choice(ALAMAT[:4])] if y < 0.75 else [rng.choice(ALAMAT[4:7])] if y < 0.85 else \
        rng.sample(["ّ", rng.choice(ALAMAT[:4])], 2) if y < 0.97 else [rng.choice(ALAMAT[:4]), rng.choice(ALAMAT[:7])]
    return ras + "".join(al)


def kalima():
    return "".join(wahda() for _ in range(rng.randint(1, 6)))


def al_kalima():
    alif = rng.choice(["ا", "ٱ"])
    lam = "ل" + rng.choice(["", "", "ْ"])
    tali = rng.choice(HAWAMIL) + rng.choice(["َّ", "َّ", "َ", "ّ", "ُ"])
    return alif + lam + tali + "".join(wahda() for _ in range(rng.randint(0, 3)))


def kalimat_mustawda():
    pat = re.compile(r"[ء-ْـٰٱ]+")
    ls = subprocess.run(["git", "-C", str(JADHR), "ls-tree", "-r", "--name-only", ASAS], capture_output=True, text=True, check=True)
    ws = set()
    for f in ls.stdout.split("\n"):
        if not f.endswith((".lean", ".py", ".json", ".md", ".tsv", ".txt", ".toml")):
            continue
        b = subprocess.run(["git", "-C", str(JADHR), "show", f"{ASAS}:{f}"], capture_output=True).stdout
        try:
            t = b.decode("utf-8")
        except UnicodeDecodeError:
            continue
        ws.update(w for w in pat.findall(t) if re.search(r"[ً-ْ]", w))
    return sorted(ws)


def shaghghil(exe, wad, ws):
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "k.tsv"
        p.write_text("".join(f"{i}\t{w}\n" for i, w in enumerate(ws)), encoding="utf-8")
        r = subprocess.run([exe, wad, str(p)], capture_output=True, text=True)
    out = {}
    for line in r.stdout.split("\n"):
        if line:
            k, rest = line.split("\t", 1)
            out[int(k)] = rest
    return out


def sabab(rest):
    """سببُ الرفض بلا الكلمة ولا نصّ المقطع."""
    r = rest.split("\t", 1)[1]
    r = re.sub(r"^«[^»]*»: ", "", r)
    return re.sub(r"«.*", "", r).strip().rstrip(":").strip()


def bashari(exe, args):
    r = subprocess.run([exe, SIJILL, MAKHZAN] + args, capture_output=True, text=True)
    out, n = [], 0
    for line in r.stdout.split("\n"):
        if line.startswith("الكلمة: "):
            n += 1
            continue
        if line.startswith("الجملة"):
            break
        if n == 1 and (line.startswith("  ملاحظة:") or line.startswith("  الخلايا:") or line.startswith("  مرفوضة")):
            out.append(line)
    return out


def tatwil_mudraj(ws):
    """(أ) تطويلٌ مجرّدٌ قبل كلّ مقطعٍ وبعده."""
    out = set()
    for w in random.Random(20261030).sample(ws, min(1500, len(ws))):
        ms = MAQTA.findall(w)
        for k in range(len(ms) + 1):
            out.add("".join(ms[:k]) + TATWIL + "".join(ms[k:]))
    return out


def waw_alif(ws):
    """(ب) واوٌ ثمّ ألفٌ آخرَ الكلمة بعلامات الواو وأواخرَ مختلفة."""
    out = set()
    for w in ws:
        m = re.match(r"^(.+)و[\u064b-\u0652]*ا$", w)
        if m:
            for alamat in ["", "\u0652", "\u0651", "\u0651\u0652", "\u064f"]:
                for akhir in ["ا", "ى", "ا" + TATWIL, "ى" + TATWIL]:
                    out.add(m.group(1) + "و" + alamat + akhir)
    return out


repo = kalimat_mustawda()
s_repo = set(repo)
ashwai = sorted({kalima() for _ in range(20000)} | {al_kalima() for _ in range(4000)})
ashwai = [w for w in ashwai if w not in s_repo]
muwajjaha_t = sorted(tatwil_mudraj(repo) - s_repo - set(ashwai))
muwajjaha_w = sorted(waw_alif(repo) - s_repo - set(ashwai) - set(muwajjaha_t))
words = repo + ashwai + muwajjaha_t + muwajjaha_w
AMDA = ["المستودع", "عشوائيّة بلا تطويل", "عشوائيّة فيها تطويل", "موجَّهة: تطويل", "موجَّهة: واو وألف"]


def masdarOf(i):
    w = words[i]
    if i < len(repo):
        return AMDA[0]
    if i < len(repo) + len(ashwai):
        return AMDA[2] if TATWIL in w else AMDA[1]
    return AMDA[3] if i < len(repo) + len(ashwai) + len(muwajjaha_t) else AMDA[4]


TAHSIL = str(JADHR / ".lake/build/bin/tahsil")
BILA = "حرف بلا حركة في غير آخر الكلمة"


def maqati(ws):
    """مقاطعُ كلّ كلمةٍ في التحصيل (أداةُ `tahsil`): (موضعُ البدء، الحكم L|P|F، الاسم، نصُّ المقطع)."""
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "t.tsv"
        p.write_text("".join(f"{i}\t{' '.join(str(ord(c)) for c in w)}\n" for i, w in enumerate(ws)), encoding="utf-8")
        r = subprocess.run([TAHSIL, str(p)], capture_output=True, text=True, check=True)
    out = collections.defaultdict(list)
    for line in r.stdout.split("\n"):
        f = line.split("\t")
        if len(f) > 7 and f[1] == "M":
            k, a, b = int(f[0]), int(f[3]), int(f[4])
            out[k].append((a, f[5], f[7], ws[k][a:b]))
    return out


def sabab_bila(ms):
    """سببُ «حرف بلا حركة في غير آخر الكلمة» في التحصيل: ما يلي المقطعَ الفاسد (تطويل) أوّلًا، ثمّ موضعُه من كلمته."""
    for j, (a, hk, ism, nass) in enumerate(ms):
        if hk == "F" and ism == BILA:
            if j + 1 < len(ms) and ms[j + 1][3].startswith(TATWIL):
                return "قبل تطويل"
            if j == 0:
                return "أوّلَ الكلمة"
            return "غير ذلك"
    return "شدّةٌ بلا حركة في غير آخر الكلمة (وسيط)"


def sabab_khalaya(w):
    """سببُ اختلاف الخلايا فيما يقبله القارئان: ألفٌ آخرَ الكلمة بعد واوٍ مشدَّدة، أو ألفٌ بعد واوٍ يليها تطويل، أو تطويلٌ مجرّد،
    أو غيرُها."""
    if re.search("و[\u0651\u0652]*\u0651[\u0651\u0652]*[اى]" + TATWIL + "*$", w):
        return "ألفٌ آخرَ الكلمة بعد واوٍ مشدَّدة"
    if re.search("و\u0652?[اى]" + TATWIL + "+$", w):
        return "ألفٌ أو مقصورةٌ بعد واوٍ يليها تطويلٌ مجرّد"
    return "تطويلٌ مجرّد في الكلمة" if TATWIL in w else "غير ذلك"


asnaf = collections.Counter()
amthila = collections.defaultdict(list)
maqbul = {}
bila = []
for wad, ism in [("--khalaya", "الوصل"), ("--qiyas", "الوقف")]:
    o, n = shaghghil(OLD, wad, words), shaghghil(NEW, wad, words)
    maqbul[ism] = [i for i in range(len(words)) if o[i].startswith("QABUL") or n[i].startswith("QABUL")]
    for i, w in enumerate(words):
        a, b = o[i], n[i]
        ka, kb = a.split("\t", 1)[0], b.split("\t", 1)[0]
        masdar = masdarOf(i)
        if ka == "RAFD" and kb == "RAFD":
            sinf = "يرفضانه" + ("" if sabab(a) == sabab(b) else "، ونصُّ الرفض مختلف")
        elif ka == "QABUL" and kb == "RAFD":
            sinf = "يرفضه الجديد وحده: " + sabab(b)
            if sabab(b) == BILA:
                bila.append((ism, i))
        elif ka == "RAFD" and kb == "QABUL":
            sinf = "يقبله الجديد وحده، والقديمُ رفضه: " + sabab(a)
        else:
            xa = a.split("\t")[1] if wad == "--qiyas" else a
            xb = b.split("\t")[1] if wad == "--qiyas" else b
            if xa == xb:
                continue
            sinf = "يقبلانه بخلايا مختلفة: " + sabab_khalaya(w)
        if sinf.startswith("يرفضانه"):
            continue
        asnaf[(ism, sinf, masdar)] += 1
        if len(amthila[(ism, sinf, masdar)]) < 2:
            amthila[(ism, sinf, masdar)].append((w, a[:90], b[:90]))

mq = maqati([words[i] for _, i in bila])
for j, (ism, i) in enumerate(bila):
    masdar = masdarOf(i)
    k = (ism, "يرفضه الجديد وحده: " + BILA, masdar)
    asnaf[k] -= 1
    k2 = (ism, f"يرفضه الجديد وحده: {BILA} ({sabab_bila(mq[j])})", masdar)
    asnaf[k2] += 1
    if len(amthila[k2]) < 2:
        amthila[k2].append((words[i], "", ""))
for k in [k for k in list(asnaf) if asnaf[k] == 0]:
    del asnaf[k]
for k in [k for k in list(amthila) if BILA in k[1] and "(" not in k[1]]:
    del amthila[k]


def bashari_farq(arg):
    i, ism = arg
    w = words[i]
    args = [w] if ism == "الوقف" else [w, "كَتَبَ"]
    a, b = bashari(OLD, args), bashari(NEW, args)
    ra, rb = any(x.startswith("  مرفوضة") for x in a), any(x.startswith("  مرفوضة") for x in b)
    if ra or rb or a == b:
        return None
    return (ism, w, [x for x in a if x not in b], [x for x in b if x not in a], masdarOf(i))


mulahazat = collections.Counter()
amthila_m = collections.defaultdict(list)
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(bashari_farq, [(i, ism) for ism in ("الوقف", "الوصل") for i in maqbul[ism]]):
        if r:
            ism, w, qadim, jadid, masdar = r
            k = (ism, masdar, sabab_khalaya(w))
            mulahazat[k] += 1
            if len(amthila_m[k]) < 3:
                amthila_m[k].append((w, " | ".join(re.sub(r"\(\d+\)", "", x).strip() for x in qadim) + " ⟶ " +
                                     " | ".join(x.strip() for x in jadid)))

adad = collections.Counter(masdarOf(i) for i in range(len(words)))
sutur = [f"# فروقُ القارئ بعد وصله بالتحصيل عن القارئ في {ASAS}", "",
         f"عدُّ أداةٍ (`tahaqquq/qari_tahsil/farq.py`) بلا وسم: {len(words)} كلمةً — "
         + "، ".join(f"{m} {adad[m]}" for m in AMDA)
         + ". ما يرفضانه كلاهما لا يُعدّ هنا (ونصُّ الرفض صار بأسماء التحصيل أو الوسائط).", "",
         "## الخلايا: القبولُ والرفض", "", "| الوضع | الصنف | " + " | ".join(AMDA) + " |", "|---|---|" + "---|" * len(AMDA)]
for (ism, sinf) in sorted({(k[0], k[1]) for k in asnaf}):
    sutur.append(f"| {ism} | {sinf} | " + " | ".join(str(asnaf[(ism, sinf, m)]) for m in AMDA) + " |")
sutur += ["", "### أمثلة (الكلمة، القديم، الجديد)", ""]
for (ism, sinf, masdar), v in sorted(amthila.items()):
    sutur.append(f"- {ism} — {sinf} — {masdar}:")
    for w, a, b in v:
        sutur.append(f"  - `{w}`" + (f" — القديم `{a}` — الجديد `{b}`" if a else ""))
sutur += ["", "## الخلايا والملاحظات في الوضع البشريّ (ما قبلاه كلاهما)", "",
          f"على {len(maqbul['الوقف'])} كلمةً في الوقف و{len(maqbul['الوصل'])} في الوصل قبلها أحدُهما.", ""]
if not mulahazat:
    sutur.append("لا فرق.")
for (ism, masdar, k), v in sorted(mulahazat.items()):
    sutur.append(f"- {ism}، {masdar}، {k}: {v}")
    for w, farq in amthila_m[(ism, masdar, k)]:
        sutur.append(f"  - `{w}`: {farq}")
MAKHRAJ.write_text("\n".join(sutur) + "\n", encoding="utf-8")
print(f"{len(words)} كلمةً؛ الأصناف: {sum(asnaf.values())}؛ فروقُ الوضع البشريّ: {sum(mulahazat.values())}")
