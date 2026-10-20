"""القياسُ المسجَّل مسبقًا (المرحلة «د» من قانون المواصفة): `hawkama/tasjil_qiyas_d.md` هو العقدُ، وهذا منفّذُه.

قولُ المالك (2026-10-20، 00:23 بتوقيت عمّان): «(د) القياس على QAC وMASAQ بتسجيلٍ مسبق قبل التشغيل. موافق».

ما يفعله، بالترتيب، ولا شيء غيره:
١. يتحقّق من بصمتي المرجعين المحجوبين في `mudaat/sijill.json` (MASAQ.csv وquranic-corpus-morphology-0.4.txt في MUDAA_DIR)
   قبل أن يقرأ منهما شيئًا؛ وتغيُّرُ بصمةٍ يوقفه باسمه.
٢. يقسم الآيات (6,236 في MASAQ) شطرين بالبذرة المختومة BADHRA: الشطرُ الأوّل للتشغيل الأوّل، والثاني محجوبٌ لتشغيلٍ مؤكِّد
   بتسجيلٍ لاحق (لا يُشغَّل إلّا بـ --shatr 2 --tasjil hawkama/<ملفٌّ أُضيف إلى main بعد هذا التسجيل>).
٣. يكتب كلماتِ الشطر (MASAQ: Word لكلّ (سورة، آية، Column5)) ملفًّا، ويشغّل `qari --qiyas` عليه.
٤. يحسب ف0–ف3 بقواعد العدّ المسجَّلة، ويكتب الخلاصة (`khulasa.json`) والتفصيل (`kalimat.tsv`) وعيّنتي الفحص المستقلّ
   معمّاتٍ وأحكامَها منفصلةً في مجلّد الإخراج.
ولا يبدأ إلّا على شجرةٍ نظيفة، HEAD فيها origin/main والتسجيلُ مدموج والوثيقةُ والسكربت كما دُمجا، بعد `lake build qari`، وببصمة
الشطر الأوّل المسجَّلة (`hirasat`، `iedad`).
لا يغيّر شيئًا في المستودع، ولا يقرأ المرجعين إلّا من MUDAA_DIR.

التشغيل: MUDAA_DIR=<مجلّد> python3 -I tahaqquq/qiyas_d.py <مجلّد الإخراج خارج المستودع> [--shatr 1]
"""
import argparse
import csv
import hashlib
import json
import math
import os
import random
import re
import subprocess
import sys
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BADHRA = 20261020
# بصمةُ قائمة آيات الشطر الأوّل («سورة:آية» مرتّبةً عدديًّا بالسورة ثمّ الآية، وكلُّ سطرٍ ينتهي بسطرٍ جديد) — مسجَّلةٌ في الوثيقة §٣؛ ويرفض السكربت التشغيل إن خالفتها.
SHATR1_SHA256 = "4210b6fb3fefc86d4d19be17b20bfe757e6d760417ac785d05c40e21e6a66e3b"
BADHRA_QAYYIS = 20261021
AYYINA_N = 100
BADHRA_AHLIYYA = 20261022
AYYINA_AHLIYYA_N = 10
AMTHILA_HADD = 25
MASAQ = "MASAQ.csv"
QAC = "quranic-corpus-morphology-0.4.txt"

# حروفُ الجذر في QAC (بكوالتر): «A» فيه همزةٌ (Alh، Amn)، لا ألف؛ والجذورُ الجوفاء بالواو والياء.
BUCKWALTER_JIDHR = {
    "A": "ء", "b": "ب", "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
    "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ", "E": "ع", "g": "غ", "f": "ف", "q": "ق", "k": "ك",
    "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "y": "ي",
}

MASAQ_IRAB = {"مرفوع": "الرفع", "منصوب": "النصب", "مجرور": "الجرّ"}
ALAMAT_QASIRA = {"الضمة", "الفتحة", "الكسرة"}
MAMNU = "الفتحة (ممنوع من الصرف)"


class Khalal(Exception):
    """خللٌ يوقف القياس باسمه."""


def basma(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tahaqquq_basamat(mdir, sijill_path=os.path.join(ROOT, "mudaat", "sijill.json")):
    """بصمةُ كلّ مرجعٍ كما خُتمت؛ وإلّا خللٌ باسمه."""
    sijill = json.load(open(sijill_path, encoding="utf-8"))["sijill"]
    for milaf in (MASAQ, QAC):
        rows = [r for r in sijill if r.get("milaf") == milaf]
        if len(rows) != 1 or rows[0].get("hala") != "مختوم" or rows[0].get("naw") != "مرجع-محجوب":
            raise Khalal(f"{milaf}: ليس مرجعًا محجوبًا مختومًا واحدًا في السجلّ")
        p = os.path.join(mdir, milaf)
        if not os.path.isfile(p):
            raise Khalal(f"{milaf}: غائبٌ عن MUDAA_DIR")
        if basma(p) != rows[0]["sha256"]:
            raise Khalal(f"{milaf}: تغيّرت بصمته عمّا خُتم")


def kalimat_masaq(path):
    """(سورة، آية، كلمة) ← {word، segs}؛ وصفوفٌ اختلفت فيها Word للكلمة الواحدة تُعدّ شذوذًا ولا تُقاس."""
    out = OrderedDict()
    shudhudh = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            k = (int(row["Sura_No"]), int(row["Verse_No"]), int(row["Column5"]))
            w = out.get(k)
            if w is None:
                w = out[k] = {"word": row["Word"], "segs": []}
            elif w["word"] != row["Word"]:
                shudhudh.append(k)
            w["segs"].append({
                "naw": row["Morph_type"], "murab": row["Invariable_Declinable"],
                "irab": row["Case_Mood"], "alama": row["Case_Mood_Marker"],
            })
    for k in set(shudhudh):
        out.pop(k, None)
    return out, sorted(set(shudhudh))


def kalimat_qac(path):
    """(سورة، آية، كلمة) ← قائمةُ القطع: (STEM/PREFIX/SUFFIX، الجذر أو None)."""
    out = OrderedDict()
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip() or line.startswith("LOCATION"):
                continue
            loc, _form, _tag, feats = line.rstrip("\n").split("\t")
            s, v, w, _seg = (int(x) for x in loc.strip("()").split(":"))
            fs = feats.split("|")
            m = re.search(r"(?:^|\|)ROOT:([^|]+)", feats)
            out.setdefault((s, v, w), []).append({"naw": fs[0], "jidhr": m.group(1) if m else None})
    return out


def jidhr_arabi(bw):
    """جذرُ QAC بالحروف العربيّة؛ وحرفٌ خارج الجدول خللٌ باسمه."""
    try:
        return "".join(BUCKWALTER_JIDHR[c] for c in bw)
    except KeyError as e:
        raise Khalal(f"حرفُ جذرٍ في QAC خارج جدول بكوالتر المسجَّل: {e}")


def basmat_shatr(ayat):
    """بصمةُ قائمة آياتٍ: «سورة:آية» مرتّبةً عدديًّا (السورة ثمّ الآية)، وكلُّ سطرٍ ينتهي بـ «\n»."""
    return hashlib.sha256("".join(f"{s}:{v}\n" for s, v in sorted(ayat)).encode()).hexdigest()


def shatr(ayat, badhra=BADHRA):
    """الآياتُ مرتّبةً، تُخلط بالبذرة، فالنصفُ الأوّل الشطرُ 1 والباقي الشطرُ 2."""
    ayat = sorted(set(ayat))
    idx = list(range(len(ayat)))
    random.Random(badhra).shuffle(idx)
    nisf = len(ayat) // 2
    return {ayat[i] for i in idx[:nisf]}, {ayat[i] for i in idx[nisf:]}


def mukhrij_qari(lines):
    """سطورُ `qari --qiyas` ← مفتاح ← حقول."""
    out = {}
    for line in lines:
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 3 and parts[1] == "RAFD":
            out[parts[0]] = {"hala": "RAFD", "sabab": parts[2]}
        elif len(parts) == 9 and parts[1] == "QABUL":
            out[parts[0]] = {"hala": "QABUL", "khalaya": parts[2], "kama": parts[3] == "1", "baad": parts[4] == "1",
                             "qanun": parts[5] == "1", "jidhr": parts[6], "haal": parts[7], "irab": parts[8]}
        else:
            raise Khalal(f"سطرٌ من القارئ بغير الصيغة المسجَّلة: {line!r}")
    return out


def wilson(k, n, z=1.96):
    """فترةُ ولسن 95% لنسبة k/n؛ ولا فترة لـ n = 0."""
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [max(0.0, round(c - h, 4)), min(1.0, round(c + h, 4))]


def miftah(k):
    return f"{k[0]}:{k[1]}:{k[2]}"


def tabaqa_jidhr(qsegs):
    """ف2: طبقةُ الكلمة في QAC — (i) قطعةٌ واحدة، (ii) أكثر — وجذرُها الثلاثيّ إن كان لها قطعةٌ واحدة ذاتُ جذرٍ ثلاثيٍّ صحيح
    (لا w ولا y فيه: المعتلُّ لا يُقاس، فالمحرّك لا يرشّح جذرًا لحامل ا ي و)؛ وإلّا None."""
    judhur = [s["jidhr"] for s in qsegs if s["jidhr"]]
    if len(judhur) != 1 or len(judhur[0]) != 3 or "w" in judhur[0] or "y" in judhur[0]:
        return None
    return ("i" if len(qsegs) == 1 else "ii"), jidhr_arabi(judhur[0])


def tabaqa_irab(msegs):
    """ف3: الكلمةُ في MASAQ قطعةٌ واحدة «معرب» بإعرابٍ من الثلاثة، وهي آخرُ قطعها (صفوفُ Other_i3rab لا تُعدّ قطعًا)؛
    فالطبقةُ «أ» إن كانت علامتُها حركةً قصيرة، و«ب» إن كانت «الفتحة (ممنوع من الصرف)»، و«ج» لما سواهما؛ وإلّا None."""
    qita = [s for s in msegs if s["naw"] in ("Prefix", "Stem", "Suffix")]
    murab = [s for s in qita if s["murab"] == "معرب" and s["irab"] in MASAQ_IRAB]
    if len(murab) != 1 or not qita or qita[-1] is not murab[0]:
        return None
    s = murab[0]
    t = "a" if s["alama"] in ALAMAT_QASIRA else ("b" if s["alama"] == MAMNU else "c")
    return t, MASAQ_IRAB[s["irab"]]


def hisab(masaq, qac, qari, ayat_shatr):
    """ف0–ف3 بقواعد العدّ المسجَّلة. masaq/qac من القارئين أعلاه، وqari من mukhrij_qari."""
    kalimat = [k for k in masaq if (k[0], k[1]) in ayat_shatr]
    n = len(kalimat)
    rafd = Counter(qari[miftah(k)]["sabab"] for k in kalimat if qari[miftah(k)]["hala"] == "RAFD")
    maqbula = [k for k in kalimat if qari[miftah(k)]["hala"] == "QABUL"]
    f0 = {"kalimat": n, "maqbula": len(maqbula), "marfuda": n - len(maqbula), "asbab_alrafd": dict(rafd.most_common())}

    # ف1: «على الخلايا» ∧ «بعد التسكين»؛ ويُعدّ كلُّ مكوّنٍ وحده أيضًا.
    fashl = []
    fashl_kama = fashl_baad = fashl_kilahuma = 0
    suwar_maqbula, suwar_fashl = set(), set()
    for k in maqbula:
        r = qari[miftah(k)]
        suwar_maqbula.add(masaq[k]["word"])
        fashl_kama += not r["kama"]
        fashl_baad += not r["baad"]
        fashl_kilahuma += not r["kama"] and not r["baad"]
        if not (r["kama"] and r["baad"]):
            fashl.append({"mawdi": miftah(k), "kalima": masaq[k]["word"], "ala_alkhalaya": int(r["kama"]),
                          "baad_altaskin": int(r["baad"])})
            suwar_fashl.add(masaq[k]["word"])
    f1 = {"maqbula": len(maqbula), "dalOK": len(maqbula) - len(fashl), "fashl": len(fashl),
          "fashl_ala_alkhalaya": fashl_kama, "fashl_baad_altaskin": fashl_baad, "fashl_kilahuma": fashl_kilahuma,
          "suwar_maqbula": len(suwar_maqbula), "suwar_fashl": len(suwar_fashl), "qaimat_alfashl": fashl}

    # ف2: مرشَّحُ الجذر مقابل جذر QAC، في الآيات التي تتساوى فيها عدّةُ الكلمات بين المرجعين.
    adad_m = Counter((k[0], k[1]) for k in masaq)
    adad_q = Counter((k[0], k[1]) for k in qac)
    ayat_mutasawiya = {a for a in ayat_shatr if adad_m[a] == adad_q[a] and adad_m[a] > 0}
    muahhal = []
    f2 = {"ayat_alshatr": len(ayat_shatr), "ayat_mutasawiya": len(ayat_mutasawiya),
          "laysa_fi_qac": 0, "i": {"n": 0, "wifaq": 0}, "ii": {"n": 0, "wifaq": 0}, "khilaf_amthila": {"i": [], "ii": []}}
    ahliyya = {miftah(k): ["-", "-"] for k in kalimat}
    for k in maqbula:
        if (k[0], k[1]) not in ayat_mutasawiya:
            continue
        if k not in qac:
            f2["laysa_fi_qac"] += 1
            continue
        r = qari[miftah(k)]
        t = tabaqa_jidhr(qac[k])
        if r["jidhr"] == "-" or t is None:
            continue
        tab, jq = t
        f2[tab]["n"] += 1
        ahliyya[miftah(k)][0] = tab
        muahhal.append((miftah(k), "f2:" + tab, "wifaq" if r["jidhr"] == jq else "khilaf", r["jidhr"], jq))
        if r["jidhr"] == jq:
            f2[tab]["wifaq"] += 1
        elif len(f2["khilaf_amthila"][tab]) < AMTHILA_HADD:
            f2["khilaf_amthila"][tab].append({"mawdi": miftah(k), "kalima": masaq[k]["word"], "murashshah": r["jidhr"],
                                              "qac": jq})
    for tab in ("i", "ii"):
        f2[tab]["nisba"] = round(f2[tab]["wifaq"] / f2[tab]["n"], 4) if f2[tab]["n"] else None
        f2[tab]["wilson95"] = wilson(f2[tab]["wifaq"], f2[tab]["n"])

    # ف3: حالُ الآخر إعرابًا مقابل Case_Mood في MASAQ.
    f3 = {t: {"n": 0, "wifaq": 0, "khilaf": 0, "la_hukm": 0} for t in ("a", "b", "c")}
    amthila = {t: [] for t in ("a", "b", "c")}
    for k in maqbula:
        t = tabaqa_irab(masaq[k]["segs"])
        if t is None:
            continue
        tab, im = t
        r = qari[miftah(k)]
        f3[tab]["n"] += 1
        ahliyya[miftah(k)][1] = tab
        natija_k = "la_hukm" if r["irab"] == "-" else ("wifaq" if r["irab"] == im else "khilaf")
        muahhal.append((miftah(k), "f3:" + tab, natija_k, r["irab"], im))
        if r["irab"] == "-":
            f3[tab]["la_hukm"] += 1
        elif r["irab"] == im:
            f3[tab]["wifaq"] += 1
        else:
            f3[tab]["khilaf"] += 1
            if len(amthila[tab]) < AMTHILA_HADD:
                amthila[tab].append({"mawdi": miftah(k), "kalima": masaq[k]["word"], "murashshah": r["irab"], "masaq": im})
    for tab in f3:
        hasm = f3[tab]["wifaq"] + f3[tab]["khilaf"]
        f3[tab]["nisbat_alwifaq_mimma_hukima"] = round(f3[tab]["wifaq"] / hasm, 4) if hasm else None
        f3[tab]["wilson95"] = wilson(f3[tab]["wifaq"], hasm)
    f3["khilaf_amthila"] = amthila
    return {"f0": f0, "f1": f1, "f2": f2, "f3": f3, "muahhal": muahhal, "ahliyya": ahliyya}


def ayyina_qayyis(muahhal, n=AYYINA_N, badhra=BADHRA_QAYYIS):
    """عيّنةُ الفحص المستقلّ الأولى (§٦): الأحكامُ (كلمةً في فرض) مرتّبةً نصًّا، ثمّ `random.Random(badhra).sample` بـ n منها.
    تُعيد (المعمّى: الموضع والفرض «f2»/«f3» وحدهما — لا الطبقة —، والأحكام: الصفوف كاملةً)."""
    m = sorted(muahhal)
    a = random.Random(badhra).sample(m, min(n, len(m)))
    return [(r[0], r[1].split(":")[0]) for r in a], a


def ayyina_ahliyya(ahliyya, n=AYYINA_AHLIYYA_N, badhra=BADHRA_AHLIYYA):
    """عيّنةُ الفحص المستقلّ الثانية (§٦): لكلّ طبقةٍ (f2:i، f2:ii، f3:a، f3:b، f3:c) ولغير المؤهَّلة (la) n كلمةً، من مواضعها
    مرتّبةً نصًّا بـ `random.Random(badhra).sample`، بالترتيب المذكور ومولِّدٍ واحد؛ ثمّ تُجمع بلا تكرار.
    تُعيد (المعمّى: المواضع وحدها مرتّبة، والأحكام: الموضع وطبقتاه في ف2 وف3 أو «-»)."""
    rng = random.Random(badhra)
    majmu = set()
    for tab in ("f2:i", "f2:ii", "f3:a", "f3:b", "f3:c", "la"):
        if tab == "la":
            ks = sorted(k for k, v in ahliyya.items() if v == ["-", "-"])
        else:
            h, t = tab.split(":")
            ks = sorted(k for k, v in ahliyya.items() if v[0 if h == "f2" else 1] == t)
        majmu.update(rng.sample(ks, min(n, len(ks))))
    a = sorted(majmu)
    return a, [(k, ahliyya[k][0], ahliyya[k][1]) for k in a]


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True)


WATHIQA = "hawkama/tasjil_qiyas_d.md"
SCRIPT = "tahaqquq/qiyas_d.py"


def hirasat(root, out, n_shatr, tasjil):
    """حراساتُ ما قبل القياس بترتيبها؛ تُعيد رسالةَ الرفض أو None:
    الإخراجُ خارج المستودع؛ الشجرةُ نظيفة؛ HEAD = origin/main؛ الوثيقةُ في HEAD؛ والوثيقةُ والسكربت كما كانا في آخر إيداعٍ غيّر الوثيقة
    (إيداعِ التسجيل)؛ والشطرُ الثاني بـ `--tasjil` يسمّي ملفًّا (blob) في `hawkama/` غيرَ هذه الوثيقة، أُضيف إلى origin/main بعد إيداع التسجيل."""
    out = os.path.abspath(out)
    if out == root or out.startswith(root + os.sep):
        return "مجلّد الإخراج داخل المستودع: مرفوض (المودَعات ومشتقّاتُها لا تُرفع)"
    if git(root, "status", "--porcelain").stdout.strip():
        return "الشجرة غير نظيفة: لا يُقاس إلّا على إيداعٍ كما هو"
    head = git(root, "rev-parse", "HEAD").stdout.strip()
    if not head or head != git(root, "rev-parse", "origin/main").stdout.strip():
        return "HEAD ليس origin/main: لا يُقاس إلّا على main بعد دمج التسجيل"
    if git(root, "cat-file", "-e", f"HEAD:{WATHIQA}").returncode:
        return "التسجيل المسبق غير مدموج في main"
    t0 = git(root, "log", "-1", "--format=%H", "HEAD", "--", WATHIQA).stdout.strip()
    if git(root, "diff", "--quiet", t0, "HEAD", "--", WATHIQA, SCRIPT).returncode:
        return "الوثيقة أو السكربت تغيّرا بعد إيداع التسجيل: هذا تسجيلٌ جديد"
    if n_shatr == 2:
        # هذه الوثيقةُ نفسُها تُرفض بـ t1 ≠ t0 أدناه (أُضيفت في إيداع التسجيل أو قبله).
        ok = bool(tasjil) and tasjil.startswith("hawkama/")
        ok = ok and git(root, "cat-file", "-t", f"origin/main:{tasjil}").stdout.strip() == "blob"
        if ok:
            t1 = git(root, "log", "--diff-filter=A", "-1", "--format=%H", "origin/main", "--", tasjil).stdout.strip()
            ok = bool(t1) and t1 != t0 and git(root, "merge-base", "--is-ancestor", t0, t1).returncode == 0
        if not ok:
            return "الشطرُ الثاني محجوبٌ لتشغيلٍ مؤكِّد: يلزم --tasjil hawkama/<ملفُّ تسجيلٍ أُضيف إلى origin/main بعد هذا التسجيل>"
    return None


def iedad(mdir, n_shatr, sijill_path=None, basmat_shatr1=SHATR1_SHA256):
    """البصماتُ أوّلًا، ثمّ القراءة، ثمّ الشطران وبصمةُ الأوّل؛ تُعيد (masaq، shudhudh، qac، ayat)."""
    tahaqquq_basamat(mdir, *([sijill_path] if sijill_path else []))
    masaq, shudhudh = kalimat_masaq(os.path.join(mdir, MASAQ))
    qac = kalimat_qac(os.path.join(mdir, QAC))
    s1, s2 = shatr([(k[0], k[1]) for k in masaq])
    if basmat_shatr(s1) != basmat_shatr1:
        raise Khalal("بصمةُ الشطر الأوّل تخالف المسجَّلة في الوثيقة §٣")
    return masaq, shudhudh, qac, (s1 if n_shatr == 1 else s2)


def main(argv):
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("out")
    ap.add_argument("--shatr", type=int, choices=(1, 2), default=1)
    ap.add_argument("--tasjil")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        print(__doc__)
        return 2
    mdir = os.environ.get("MUDAA_DIR")
    rafd = hirasat(ROOT, a.out, a.shatr, a.tasjil) or (None if mdir else "MUDAA_DIR غير معيَّن")
    if rafd:
        print(rafd)
        return 2
    b = subprocess.run(["lake", "build", "qari"], cwd=ROOT, capture_output=True, text=True)
    if b.returncode != 0:
        raise Khalal("lake build qari فشل:\n" + (b.stdout + b.stderr)[-2000:])
    qari_bin = os.path.join(ROOT, ".lake", "build", "bin", "qari")
    masaq, shudhudh, qac, ayat = iedad(mdir, a.shatr)
    out = os.path.abspath(a.out)
    os.makedirs(os.path.join(out, "ahkam"), exist_ok=True)
    madkhal = os.path.join(out, "madkhal.tsv")
    with open(madkhal, "w", encoding="utf-8") as f:
        for k, w in masaq.items():
            if (k[0], k[1]) in ayat:
                f.write(f"{miftah(k)}\t{w['word']}\n")
    p = subprocess.run([qari_bin, "--qiyas", madkhal], capture_output=True, text=True, timeout=7200)
    if p.returncode != 0:
        raise Khalal("qari --qiyas فشل:\n" + p.stderr[-2000:])
    qari = mukhrij_qari(p.stdout.splitlines())
    natija = hisab(masaq, qac, qari, ayat)
    muamma1, ahkam1 = ayyina_qayyis(natija.pop("muahhal"))
    muamma2, ahkam2 = ayyina_ahliyya(natija.pop("ahliyya"))
    for ism, rows in (("ayyina_qayyis.tsv", muamma1), ("ahkam/ayyina_qayyis_ahkam.tsv", ahkam1),
                      ("ayyina_ahliyya.tsv", [(k,) for k in muamma2]), ("ahkam/ayyina_ahliyya_ahkam.tsv", ahkam2)):
        with open(os.path.join(out, ism), "w", encoding="utf-8") as f:
            for row in rows:
                f.write("\t".join(row) + "\n")
    natija.update({
        "shudhudh_masaq": [miftah(k) for k in shudhudh], "shatr": a.shatr, "badhra": BADHRA,
        "basmat_alshatr1": SHATR1_SHA256, "iltizam": git(ROOT, "rev-parse", "HEAD").stdout.strip(),
        "basmat_qari": basma(qari_bin), "basmat_alwathiqa": basma(os.path.join(ROOT, WATHIQA)),
        "basmat_alskript": basma(os.path.join(ROOT, SCRIPT)),
        "tasjil": None if a.shatr == 1 else {"milaf": a.tasjil, "basma": basma(os.path.join(ROOT, a.tasjil))},
    })
    with open(os.path.join(out, "khulasa.json"), "w", encoding="utf-8") as f:
        json.dump(natija, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out, "kalimat.tsv"), "w", encoding="utf-8") as f:
        for line in p.stdout.splitlines():
            f.write(line + "\n")
    f0, f1 = natija["f0"], natija["f1"]
    print(f"الشطر {a.shatr}: {f0['kalimat']} كلمة، قُبل ترميزُها {f0['maqbula']}، وقُبل في ف1 {f1['dalOK']}، وفشل {f1['fashl']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Khalal as e:
        print(f"خلل: {e}")
        sys.exit(1)
