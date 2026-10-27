"""فروقُ القارئ بعد وصله بالتحصيل (Dal/QiraaTahsil.lean) عن القارئ قبله (main ‏09f7b27)، بأسبابها. عدُّ أداةٍ لا اختبار.

الكلماتُ: كلُّ كلمةٍ مشكولةٍ متمايزة في ملفّات المستودع النصّيّة عند 09f7b27 (git ls-tree؛ .lean .py .json .md .tsv .txt .toml)، وكلماتٌ
عشوائيّة بالبذرة 20261029 (رؤوسٌ من الحوامل ومقاعد الهمزة والخاصّة وحروفٍ خارج الجدول، بعد كلٍّ منها من صفرٍ إلى علامتين، وصدورٌ بألفٍ ولام).
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


repo = kalimat_mustawda()
s_repo = set(repo)
ashwai = sorted({kalima() for _ in range(20000)} | {al_kalima() for _ in range(4000)})
words = repo + [w for w in ashwai if w not in s_repo]
asnaf = collections.Counter()
amthila = collections.defaultdict(list)
maqbul = {}
for wad, ism in [("--khalaya", "الوصل"), ("--qiyas", "الوقف")]:
    o, n = shaghghil(OLD, wad, words), shaghghil(NEW, wad, words)
    maqbul[ism] = [i for i in range(len(words)) if o[i].startswith("QABUL") or n[i].startswith("QABUL")]
    for i, w in enumerate(words):
        a, b = o[i], n[i]
        ka, kb = a.split("\t", 1)[0], b.split("\t", 1)[0]
        masdar = "المستودع" if i < len(repo) else "عشوائيّة"
        if ka == "RAFD" and kb == "RAFD":
            sinf = "يرفضانه" + ("" if sabab(a) == sabab(b) else "، ونصُّ الرفض مختلف")
        elif ka == "QABUL" and kb == "RAFD":
            sinf = "يرفضه الجديد وحده: " + sabab(b)
        elif ka == "RAFD" and kb == "QABUL":
            sinf = "يقبله الجديد وحده، والقديمُ رفضه: " + sabab(a)
        else:
            xa = a.split("\t")[1] if wad == "--qiyas" else a
            xb = b.split("\t")[1] if wad == "--qiyas" else b
            if xa == xb:
                continue
            sinf = "يقبلانه بخلايا مختلفة"
        if sinf.startswith("يرفضانه"):
            continue
        asnaf[(ism, sinf, masdar)] += 1
        if len(amthila[(ism, sinf)]) < 4:
            amthila[(ism, sinf)].append((w, a[:90], b[:90]))


def bashari_farq(arg):
    i, ism = arg
    w = words[i]
    args = [w] if ism == "الوقف" else [w, "كَتَبَ"]
    a, b = bashari(OLD, args), bashari(NEW, args)
    ra, rb = any(x.startswith("  مرفوضة") for x in a), any(x.startswith("  مرفوضة") for x in b)
    if ra or rb or a == b:
        return None
    return (ism, w, [x for x in a if x not in b], [x for x in b if x not in a])


mulahazat = collections.Counter()
amthila_m = collections.defaultdict(list)
with cf.ThreadPoolExecutor(4) as ex:
    for r in ex.map(bashari_farq, [(i, ism) for ism in ("الوقف", "الوصل") for i in maqbul[ism]]):
        if r:
            ism, w, qadim, jadid = r
            k = (ism, " | ".join(re.sub(r"\(\d+\)", "", x).strip() for x in qadim) + " ⟶ " + " | ".join(x.strip() for x in jadid))
            mulahazat[k] += 1
            if len(amthila_m[k]) < 3:
                amthila_m[k].append(w)

sutur = [f"# فروقُ القارئ بعد وصله بالتحصيل عن القارئ في {ASAS}", "",
         f"عدُّ أداةٍ (`tahaqquq/qari_tahsil/farq.py`) بلا وسم: {len(words)} كلمةً — {len(repo)} مشكولةٌ متمايزة من ملفّات المستودع عند {ASAS}، "
         f"و{len(words) - len(repo)} عشوائيّة (البذرة 20261029). ما يرفضانه كلاهما لا يُعدّ هنا (ونصُّ الرفض صار بأسماء التحصيل).", "",
         "## الخلايا: القبولُ والرفض", "", "| الوضع | الصنف | المستودع | عشوائيّة |", "|---|---|---|---|"]
for (ism, sinf) in sorted({(k[0], k[1]) for k in asnaf}):
    sutur.append(f"| {ism} | {sinf} | {asnaf[(ism, sinf, 'المستودع')]} | {asnaf[(ism, sinf, 'عشوائيّة')]} |")
sutur += ["", "### أمثلة (الكلمة، القديم، الجديد)", ""]
for (ism, sinf), v in sorted(amthila.items()):
    sutur.append(f"- {ism} — {sinf}:")
    for w, a, b in v:
        sutur.append(f"  - `{w}` — القديم `{a}` — الجديد `{b}`")
sutur += ["", "## الخلايا والملاحظات في الوضع البشريّ (ما قبلاه كلاهما)", "",
          f"على {len(maqbul['الوقف'])} كلمةً في الوقف و{len(maqbul['الوصل'])} في الوصل قبلها أحدُهما.", ""]
if not mulahazat:
    sutur.append("لا فرق.")
for (ism, k), v in sorted(mulahazat.items(), key=lambda x: -x[1]):
    sutur.append(f"- {ism}، {v}: {k} — مثل: {'، '.join('`' + w + '`' for w in amthila_m[(ism, k)])}")
MAKHRAJ.write_text("\n".join(sutur) + "\n", encoding="utf-8")
print(f"{len(words)} كلمةً؛ الأصناف: {sum(asnaf.values())}؛ فروقُ الوضع البشريّ: {sum(mulahazat.values())}")
