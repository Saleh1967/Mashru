"""محاكاةُ قواعد العمليّة العقليّة قبل الشرع على آية الدَّين (البقرة ٢٨٢) من مودَع التنزيل المختوم — مرآةُ `Aql/Muhakat.lean`.

الطلب: قولُ المالك 2026-11-22 (17:22): «… تشغيل النواة على مدخلات حقيقية في Mashru … ويوجد مثال لاية الدين اعمل pr على اية الدين».

ما يقرؤه (بصماتُها من `mudaat/sijill.json`، ويُرفض الملفُّ باسمه إن خالفت):
  quran-simple-enhanced.txt (وضع)، lisan.txt وmaqayis.txt (معلومات-سابقة). ولا يقرأ QAC ولا MASAQ (مرجعان محجوبان للقياس وحده).

القواعد (تعيين البنّاء، معلَن):
  T1 الآية: السطرُ 289 من المودَع (سبعُ آياتٍ للفاتحة ثمّ ٢٨٢)، ويُحرس بصدره «يَا أَيُّهَا الَّذِينَ آمَنُوا إِذَا تَدَايَنتُم».
  T2 الجمل: ما بين علامات `<sel>` في السطر نفسِه (علامةٌ في المودَع، لا تقطيعٌ من البنّاء)؛ والكلماتُ ما بين المسافات.
  T3 الجذر: مرشَّحو `Jadhr.mursh` من `shabaka/jadwal_luzum.py` على موادّ اللسان (R1–R2 هناك: الجذرُ من صيغ التفسير ثمّ الورود في
     المادّة نفسِها، لا صرفٌ مفروض). مرشَّحٌ واحد `murashshah_wahid`، وأكثرُ `murashshahun`، ولا شيء `la_murashshah`. والمرشَّحُ
     الواحد ليس جذرًا معيَّنًا: لم يُقس على مرجع (QAC محجوبٌ لقياسٍ بتسجيلٍ مسبق لم يُكتب)، وفي الآية منه ما يخالف المعروف
     («آمَنُوا» ← مني، «بِدَيْنٍ» ← بدن؛ قراءةُ البنّاء بالعين، لا قياس).
  T4 شاهدُ الوضع: لكلّ مرشَّحٍ واحد سطرُ عنوانه في اللسان («### $ R:»)، وفي المقاييس («### | (R)») إن وُجد. نقلٌ آحادٌ لكلٍّ،
     ولم يُفحص استقلالُ المعجمين، فلا تواتر.
  T5 الأسئلة الثلاثة على كلّ جملة (`Aql.Muhakat` §٨): وجودُها في المودَع (وجود، حسّ)؛ حكمُ ما فيها من أمرٍ ونهي (مدح وذمّ)؛ معنى كلّ
     كلمةٍ بالوضع (صفة، آحاد) بمقدّماتٍ: شاهدٌ لكلّ معجم ← ظنّيّ، ولا شاهد ← ليس فكرًا («لا حكم»).
  T6 الدافع: أربعةُ دوافع (أصولُ `Aql.Muhakat.Asl`)، والأسئلةُ لا تُختار بالدافع هنا، فيُحكم على المدخل نفسِه بكلٍّ منها؛ ويُطبع
     أنّ المخرجَ واحدٌ بايتًا (INV-01 على المدخل الحقيقيّ).

التشغيل: MUDAA_DIR=<مجلّد> python3 -I scripts/muhakat_dayn.py [--natija] [--tafsil]
  بلا وسيط: الملخّصُ JSON (أعدادٌ وبصمات، بلا نصّ الآية: المودَعُ لا يُرفع ولا مشتقُّه النصّيّ).
  --tafsil: سطرٌ لكلّ كلمة (للفحص اليدويّ؛ لا يُودَع).
  الخروج: 0، أو 2 بخطأٍ مسمًّى (مودَعٌ غائب أو بصمةٌ مخالفة أو صدرٌ لا يطابق).
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "shabaka"))
import jadwal_luzum as jl  # noqa: E402

SATR = 289
# بترتيب علامات المودَع نفسه: الشدّةُ قبل الحركة (U+0651 ثمّ الحركة). يُعاد ترتيبُ هذا الثابت وحده، ولا تطبيعَ لبايتات المودَع.
def shadda_awwalan(t):
    out = list(t)
    for i in range(len(out) - 1):
        if out[i] in "\u064e\u064f\u0650" and out[i + 1] == "\u0651":
            out[i], out[i + 1] = out[i + 1], out[i]
    return "".join(out)


SADR = shadda_awwalan("يَا أَيُّهَا الَّذِينَ آمَنُوا إِذَا تَدَايَنتُم")
DAWAFI = (("hajaUdwiyya", "الجوع"), ("baqa", "التملّك"), ("naw", "الحنان"), ("tadayyun", "التقديس"))

# ---------------- مرآةُ Aql/Muhakat.lean ----------------
RUTBA = {"laFikr": 0, "zanni": 1, "qati": 2}


def saqf(ismail, j, q):
    if q in ("fard", "takhayyul") or j == "madhDhamm":
        return "laFikr"
    if j == "wujud":
        return "qati" if q in ("hiss", "athar", "mutawatir") else "zanni"
    if j == "wujudSifa":
        if q == "hiss":
            return "qati" if ismail else "zanni"
        return "qati" if q == "mutawatir" else "zanni"
    if j in ("sifa", "kunh"):
        if q == "athar":
            return "laFikr"
        return "qati" if q == "mutawatir" else "zanni"
    return "zanni"  # mulaama


def iltiqa(a, b):
    return a if RUTBA[a] <= RUTBA[b] else b


def hukm(ismail, jiha, qanat, ms):
    if jiha == "madhDhamm":
        return "kharijNitaq"
    r = saqf(ismail, jiha, qanat)
    for m in ms:
        r = iltiqa(r, m)
    return r


def haqiqa(j, q, r):
    return j == "wujud" and r == "qati" and q in ("hiss", "athar")


# ---------------- المودَعات ----------------

class Khata(Exception):
    pass


def mudaa(dir_, milaf):
    p = os.path.join(dir_, milaf)
    if not os.path.isfile(p):
        raise Khata(f"غائب: {milaf}")
    b = jl.sijill().get(milaf, {}).get("sha256")
    if b is None or jl.basma(p) != b:
        raise Khata(f"بصمةٌ مخالفة: {milaf}")
    return p


def aya(dir_):
    with open(mudaa(dir_, "quran-simple-enhanced.txt"), encoding="utf-8") as f:
        lines = f.read().split("\n")
    s = lines[SATR - 1]
    if not s.startswith(SADR):
        raise Khata(f"صدرُ السطر {SATR} لا يطابق")
    return s


def jumal(s):
    return [j.split() for j in s.split("<sel>") if j.strip()]


def unwan(dir_):
    with open(mudaa(dir_, "lisan.txt"), encoding="utf-8") as f:
        lisan = f.read().split("\n")
    with open(mudaa(dir_, "maqayis.txt"), encoding="utf-8") as f:
        maqayis = f.read().split("\n")
    ml = jl.mawadd_lisan(lisan)
    mq, _ = jl.mawadd_maqayis(maqayis)
    satrL = {}
    for R, i, _ in ml:
        satrL.setdefault(R, i)
    satrQ = {}
    for R, i, _ in mq:
        satrQ.setdefault(R, i)
    return jl.Jadhr(ml), satrL, satrQ, lisan


# ---------------- المحاكاة ----------------

def kalima(J, satrL, satrQ, w):
    rs = sorted(J.mursh(w))
    if len(rs) == 1:
        R = rs[0]
        shuhud = [("lisan", satrL[R])] + ([("maqayis", satrQ[R])] if R in satrQ else [])
        return {"hala": "murashshah_wahid", "jadhr": R, "shuhud": shuhud, "ms": ["zanni"] * len(shuhud)}
    return {"hala": "murashshahun" if rs else "la_murashshah", "jadhr": None, "shuhud": [], "ms": ["laFikr"],
            "murashshahun": rs}


def muhakat(dafi, js, J, satrL, satrQ):
    """الدافعُ معاملٌ لا يُقرأ (T6): المخرجُ دالّةٌ في الجمل والمعجمين وحدها."""
    out = []
    for n, ws in enumerate(js, 1):
        wujud = hukm(False, "wujud", "hiss", [])
        row = {"jumla": n, "wujud": wujud, "haqiqa": haqiqa("wujud", "hiss", wujud),
               "hukm_shari": hukm(False, "madhDhamm", "nass", []), "kalimat": []}
        for w in ws:
            k = kalima(J, satrL, satrQ, w)
            k["mana"] = hukm(False, "sifa", "ahad", k["ms"])
            row["kalimat"].append(k)
        out.append(row)
    return out


def basmaJ(x):
    return hashlib.sha256(json.dumps(x, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def mulakhkhas(dir_):
    s = aya(dir_)
    js = jumal(s)
    J, satrL, satrQ, _ = unwan(dir_)
    natayij = {d[0]: muhakat(d, js, J, satrL, satrQ) for d in DAWAFI}
    basamat = {k: basmaJ(v) for k, v in natayij.items()}
    r = natayij[DAWAFI[0][0]]
    ks = [k for row in r for k in row["kalimat"]]
    adad = {h: sum(k["hala"] == h for k in ks) for h in ("murashshah_wahid", "murashshahun", "la_murashshah")}
    return {
        "aya": "البقرة 282", "satr": SATR,
        "basmat_mudaat": {m: jl.sijill()[m]["sha256"] for m in ("quran-simple-enhanced.txt", "lisan.txt", "maqayis.txt")},
        "jumal": len(js), "kalimat": len(ks), "halat_jadhr": adad,
        "shuhud_maqayis": sum(any(s_[0] == "maqayis" for s_ in k["shuhud"]) for k in ks),
        "mana": {h: sum(k["mana"] == h for k in ks) for h in ("qati", "zanni", "laFikr")},
        "wujud_qati_haqiqa": sum(row["wujud"] == "qati" and row["haqiqa"] for row in r),
        "hukm_shari_kharij": sum(row["hukm_shari"] == "kharijNitaq" for row in r),
        "inv01_basma_wahida": len(set(basamat.values())) == 1,
        "basmat_mukhrajat": basamat,
    }, natayij


def main(argv):
    dir_ = os.environ.get("MUDAA_DIR", os.path.expanduser("~/mudaa_dir"))
    try:
        m, natayij = mulakhkhas(dir_)
    except Khata as e:
        print(f"خطأ: {e}", file=sys.stderr)
        return 2
    if "--tafsil" in argv:
        s = aya(dir_)
        for row, ws in zip(natayij[DAWAFI[0][0]], jumal(s)):
            for w, k in zip(ws, row["kalimat"]):
                print(f"{row['jumla']}\t{w}\t{k['hala']}\t{k['jadhr'] or ','.join(k.get('murashshahun', []))}\t"
                      f"{';'.join(f'{a}:{b}' for a, b in k['shuhud'])}\t{k['mana']}")
        return 0
    print(json.dumps(m, ensure_ascii=False, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
