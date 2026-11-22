"""SIM-AQL في Lean (`Aql/SimAql.lean`) وموصولًا بـ«صنّف» في mudir (`NTP.Mukhassas.halaWujud`/`halaMadmun`)؛ البوّابة ٥ت١٥.

يفحص:
١. السجلّ: «التفكير — نصّ المكتبة الشاملة» مختومٌ «معلومات-سابقة» (tafkir.txt)، وفي mudaat/jalb.py رابطُه مثبَّتًا بإيداع؛ وإن حضر:
   بصمتُه المختومة.
٢. السند: كلُّ نقلٍ في رأس Aql/SimAql.lean على صورة «* تN: «…»» أو «* ش٣ N: «…»» (وما يليه في البند نفسِه) موجودٌ بنصّه في السطر N من
   المودَع (ت = tafkir.txt، ش٣ = a2.txt)؛ و«…» داخل النقل حذفٌ، فكلُّ قطعةٍ منه في السطر بترتيبها. وعددُ النقول المفحوصة مطبوع،
   ولا يقلّ عن 20 (بُني الملفّ على 25 نقلًا).
٣. التصحيح المعلن على SIM-AQL 0.1: ت83 فيه «والأسلوب يقرره نوع العمل»، وليس في الكتاب كلِّه «يقرره نوع الشيء».
٤. المحرّك: «صنّف الفزع» بالمودَع: سطرُ SIM-AQL فيه وجودُ القول «تصديقٌ جازم (قطعيّ)» ومضمونُه «خبرٌ لغويّ آحاد» «ظنٌّ راجح (ظنّيّ)».
الطفرات: P1661–P1667 في Lean يقتلها البناء (saqf_athar، siyaj_zanni_qati، qati_yaghlib، jazim_wujud، amiq_ratib،
bila_amal_la_jadd، simaql_madmun_zann)؛ وP1668 (الفاحصُ يقبل كلَّ نقل) يقتلها فحصُ الفاحص في ٢ (نقلٌ محرَّفٌ بكلمة يُرفض).
التشغيل (بعد lake build): python3 -I tahaqquq/test_sim_aql.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MUDIR = os.path.join(ROOT, ".lake", "build", "bin", "mudir")
fashal, najah = [], 0


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def nuqul(ras):
    """(المصدر، السطر، النقل) من بنود الرأس: «* تN: …» و«ش٣ N: …» داخل البند، بالنقول المحصورة بين «».
    كلُّ وسمٍ يحكم ما بعده حتى الوسم التالي."""
    out = []
    bunud = re.split(r"\n  \* ", ras)
    for b in bunud[1:]:
        b = re.sub(r"\s+", " ", b.split("\n\n")[0])
        for m in re.finditer(r"و?(ت|ش٣ )(\d+)(?:–\d+)?:(.*?)(?=(?:؛|،|\.)\s*و?(?:ت|ش٣ )\d+(?:–\d+)?:|$)", b):
            masdar = "tafkir.txt" if m.group(1) == "ت" else "a2.txt"
            for q in re.findall(r"«([^«»]+)»", m.group(3)):
                out.append((masdar, int(m.group(2)), q))
    return out


def fi_satrih(asatir, masdar, n, q):
    """النقلُ في السطر n من المودَع: قطعُه (المفصولةُ بـ«…») فيه بترتيبها."""
    satr = asatir[masdar][n - 1] if 0 < n <= len(asatir[masdar]) else ""
    mawdi = 0
    for x in (x.strip() for x in q.split("…")):
        if not x:
            continue
        i = satr.find(x, mawdi)
        if i < 0:
            return False
        mawdi = i + len(x)
    return True


def main():
    sj = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    m = [x for x in sj if x["milaf"] == "tafkir.txt"]
    tahaqqaq(len(m) == 1 and m[0]["hala"] == "مختوم" and m[0]["naw"] == "معلومات-سابقة", f"١ قيدُ السجلّ {m}")
    jalb = open(os.path.join(ROOT, "mudaat", "jalb.py"), encoding="utf-8").read()
    tahaqqaq('"tafkir.txt": "https://raw.githubusercontent.com/Saleh1967/alghanem-constitution/f75a43b9f4ed3df059f1feb832f48d96e6f846ba/'
             in jalb, "١ لا رابطَ مثبَّتًا في jalb.py")
    d = os.environ.get("MUDAA_DIR") or os.path.join(ROOT, ".mudaa")
    p = {f: os.path.join(d, f) for f in ("tafkir.txt", "a2.txt")}
    if not all(os.path.exists(x) for x in p.values()):
        print(f"لم يُشغَّل على المودَع (tafkir.txt أو a2.txt غائبٌ في {d}؛ mudaat/jalb.py يجلبهما)")
        return khatm()
    tahaqqaq(hashlib.sha256(open(p["tafkir.txt"], "rb").read()).hexdigest() == m[0]["sha256"], "١ بصمةُ tafkir.txt")
    asatir = {f: open(x, encoding="utf-8").read().split("\n") for f, x in p.items()}

    ras = open(os.path.join(ROOT, "Aql", "SimAql.lean"), encoding="utf-8").read().split("-/", 1)[0]
    sanad = ras.split("**السند**", 1)[1].split("**تصحيحٌ", 1)[0]
    nq = nuqul(sanad)
    for masdar, n, q in nq:
        tahaqqaq(fi_satrih(asatir, masdar, n, q), f"٢ «{q[:50]}» ليس في {masdar}:{n}")
    tahaqqaq(len(nq) >= 20, f"٢ النقولُ المفحوصة {len(nq)} أقلُّ من 20")
    # فحصُ الفاحص: نقلٌ محرَّفٌ بكلمة (ت18 «ولا» ← «بل») يُرفض، ونقلٌ في غير سطره يُرفض، والصحيحُ يُقبل.
    tahaqqaq(not fi_satrih(asatir, "tafkir.txt", 18, "الإدراك الشعوري … ولكن هذا التمييز ليس فكراً بل إدراكاً"), "٢ الفاحصُ قبل نقلًا محرَّفًا")
    tahaqqaq(not fi_satrih(asatir, "tafkir.txt", 19, "ولكن هذا التمييز ليس فكراً ولا إدراكاً"), "٢ الفاحصُ قبل نقلًا في غير سطره")
    tahaqqaq(fi_satrih(asatir, "tafkir.txt", 18, "الإدراك الشعوري … ولكن هذا التمييز ليس فكراً ولا إدراكاً"), "٢ الفاحصُ ردّ نقلًا صحيحًا")

    t = asatir["tafkir.txt"]
    tahaqqaq("والأسلوب يقرره نوع العمل" in t[82], "٣ ت83 لا يقول «يقرره نوع العمل»")
    tahaqqaq(not any("يقرره نوع الشيء" in l for l in t), "٣ في الكتاب «يقرره نوع الشيء»")

    pm = os.path.join(d, "ntp_mukhassas.tsv")
    if os.path.exists(MUDIR) and os.path.exists(pm):
        r = subprocess.run([MUDIR, "--qanat", "malik", "صنف الفزع"], cwd=ROOT, capture_output=True, text=True, timeout=300,
                           env=dict(os.environ, MUDAA_DIR=d))
        tahaqqaq("SIM-AQL (Aql.SimAql.think): وجودُ القول في المودَع المختوم: تصديقٌ جازم (قطعيّ)؛ "
                 "ومضمونُه (كنهٌ بتصنيف، خبرٌ لغويّ آحاد): ظنٌّ راجح (ظنّيّ)" in r.stdout, "٤ سطرُ SIM-AQL في «صنّف الفزع»")
    else:
        fashal.append("٤ mudir غيرُ مبنيّ أو ntp_mukhassas.tsv غائب")
    print(f"النقول: {len(nq)} في مواضعها من tafkir.txt وa2.txt")
    return khatm()


def khatm():
    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        sys.exit(1)
    print(f"test_sim_aql: {najah} فحصًا نجح")


if __name__ == "__main__":
    main()
