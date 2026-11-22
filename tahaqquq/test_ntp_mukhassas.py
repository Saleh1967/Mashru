"""وكيلُ NTP على شبكة المخصّص المختوم (`Madlul/NTP/Mukhassas.lean`، وخطوةُ `NTP.Mukhassas` في «صنّف» من `mudir`؛ البوّابة ٥ت١٤).

**وسمُ التوقّعات.** ما في ٢ و٣ من النصّ المختوم ومن الجدول بقراءة بايثون مستقلّة هنا (لا بدوالّ Lean ولا بالمولِّد)؛ وما في ٤ أسطرٌ كتبها البنّاء
من تلك القراءة (القائلان وطريقُ العقدة)، فهو «مفحوص» على أسطره؛ و٥ مطابقةُ المحرّك بقراءة بايثون على عيّنةٍ محدّدة سلفًا (كلُّ لفظٍ رقمُه في
قائمة الألفاظ المفردة المرتّبة مضاعفٌ لـ 500)، لا على المودَع كلّه.

يفحص:
١. السجلّ: «شبكة NTP من المخصص» مختومٌ «معلومات-سابقة» باسم ملفّه ntp_mukhassas.tsv، وفي mudaat/jalb.py مولِّدٌ له من mukhassas.txt.
   وإن حضر المودَعان (MUDAA_DIR): بصمةُ الجدول بصمتُه المختومة، والمولِّدُ يعيده من المخصّص بايتًا.
٢. أسطرُ الشاهد في Lean (`NTP.Mukhassas.shahid`، العقدُ الأربع والأزواجُ الخمسة) أسطرٌ في الجدول بنصّها؛ ومن النصّ المختوم: عنوانُ كلّ عقدةٍ
   يبدأ عند إزاحته أو بعدها بقليل، ولفظُ كلّ زوجٍ في الأسطر الثلاثمئة محرفٍ بعد إزاحته.
٣. من الجدول ببايثون: «الفزع» بقائلَين مسمّيَين (أبو عبيد، أبو زيد) في عقدة 1312 وأبوها 1138 «كتاب النخل»؛ و«البلجة» بقائلٍ واحد (ثابت) في 25
   تحت 2 «كتاب خلق الإنسان»؛ والأعدادُ على المودَع كلّه تُطبع (العُقد، الأزواج، الألفاظ، وما له قائلان مسمّيان فأكثر).
٤. المحرّك: «صنّف الفزع» و«صنّف البلجة» بالمودَع: سطرُ القائلين، والعدّان، وطريقُ العقدة، وأوّلُ الجواب «لا حكم بالتواتر على الشجرة»؛ وبلا مودَع:
   «مودَعٌ غائب» والقرارُ لا يتغيّر.
٥. العيّنة: لكلّ لفظٍ فيها عددُ القائلين المسمّين وعددُ العُقد في جواب المحرّك هما عدّاهما ببايثون.
الطفرات: P1655 (`ghayrMusamma` بلا «بلا نسبة صريحة») وP1656 (الطريقُ لا يصعد) وP1657 (سلاسلُ القائلين مغلقة) يقتلها البناء
(`shahid_faza`، `shahid_masar`، `qail_maftuh`)؛ وP1658 (القارئُ يقلب اللفظ والقائل) يقتلها ٤ و٥؛ وP1659 («صنّف» بلا بدائل) يقتلها
test_mudir؛ وP1660 (المولِّدُ يُسقط الأب) يقتلها ١ مع المودَع.
التشغيل (بعد lake build): python3 -I tahaqquq/test_ntp_mukhassas.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MUDIR = os.path.join(ROOT, ".lake", "build", "bin", "mudir")
BILA = {"بلا نسبة صريحة", "غيره", "غير واحد"}
fashal, najah = [], 0


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def mudir(nass, mudaa):
    p = subprocess.run([MUDIR, "--qanat", "malik", nass], cwd=ROOT, capture_output=True, text=True, timeout=300,
                       env=dict(os.environ, MUDAA_DIR=mudaa))
    return p.returncode, p.stdout


def qism_mukhassas(out):
    return out.split("### ٢. NTP.Mukhassas", 1)[-1].split("## ما بقي باسمه", 1)[0]


def main():
    sj = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    m = [x for x in sj if x["milaf"] == "ntp_mukhassas.tsv"]
    tahaqqaq(len(m) == 1 and m[0]["hala"] == "مختوم" and m[0]["naw"] == "معلومات-سابقة" and m[0]["ism"] == "شبكة NTP من المخصص",
             f"١ قيدُ السجلّ: {m}")
    tahaqqaq('"ntp_mukhassas.tsv": (["mukhassas.txt"]' in open(os.path.join(ROOT, "mudaat", "jalb.py"), encoding="utf-8").read(),
             "١ لا مولِّدَ في jalb.py")
    d = os.environ.get("MUDAA_DIR") or os.path.join(ROOT, ".mudaa")
    p, pm = os.path.join(d, "ntp_mukhassas.tsv"), os.path.join(d, "mukhassas.txt")
    if not (os.path.exists(p) and os.path.exists(pm)):
        print(f"لم يُشغَّل على المودَع (ntp_mukhassas.tsv أو mukhassas.txt غائبٌ في {d}؛ mudaat/jalb.py يجلبهما)")
        bila_mudaa()
        return khatm()
    tahaqqaq(sha(p) == m[0]["sha256"], "١ بصمةُ الجدول ليست المختومة")
    with tempfile.TemporaryDirectory() as t:
        os.symlink(pm, os.path.join(t, "mukhassas.txt"))
        r = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_ntp_mukhassas.py"), t], capture_output=True, text=True)
        tahaqqaq(r.returncode == 0 and sha(os.path.join(t, "ntp_mukhassas.tsv")) == m[0]["sha256"], "١ المولِّدُ لا يعيد الجدولَ المختوم")

    rows = [l.rstrip("\n").split("\t") for l in open(p, encoding="utf-8")]
    J = {int(r[1]): r for r in rows if r[0] == "jins"}
    Z = [r for r in rows if r[0] == "zawj"]
    nass = open(pm, encoding="utf-8").read()

    # ٢: أسطرُ الشاهد في Lean
    lean = open(os.path.join(ROOT, "Madlul", "NTP", "Mukhassas.lean"), encoding="utf-8").read()
    shahid = lean.split("def shahid : Shabaka where", 1)[1].split("theorem", 1)[0]
    aj = re.findall(r'⟨(\d+), (none|some \d+), "([^"]+)", "([^"]+)", (\d+)⟩', shahid)
    az = re.findall(r'⟨(\d+), (\d+), "([^"]+)", "([^"]+)", (\d+)⟩', shahid)
    tahaqqaq(len(aj) == 4 and len(az) == 5, f"٢ عددُ أسطر الشاهد {len(aj)}/{len(az)}")
    for r, a, n, u, o in aj:
        satr = ["jins", r, "-" if a == "none" else a.split()[1], n, u, o]
        tahaqqaq(satr in rows, f"٢ عقدةُ الشاهد {r} ليست سطرًا في الجدول")
        tahaqqaq(u in nass[int(o):int(o) + len(u) + 40], f"٢ العنوانُ «{u}» ليس عند إزاحته {o} في المخصّص")
    for r, j, l, q, o in az:
        tahaqqaq(["zawj", r, j, l, q, o] in rows, f"٢ زوجُ الشاهد {r} ليس سطرًا في الجدول")
        tahaqqaq(l in nass[int(o):int(o) + 300], f"٢ اللفظُ «{l}» ليس بعد إزاحته {o} في المخصّص")

    # ٣: من الجدول
    def qailun(w):
        b = {w, w[2:]} if w.startswith("ال") else {w, "ال" + w}
        zs = [z for z in Z if z[3] in b]
        q = []
        for z in zs:
            if z[4] not in BILA and z[4] not in q:
                q.append(z[4])
        return zs, q, sorted({int(z[2]) for z in zs})
    zs, q, aj = qailun("الفزع")
    tahaqqaq(q == ["أبو عبيد", "أبو زيد"] and aj == [1312] and J[1312][2] == "1138" and J[1138][4] == "كتاب النخل", f"٣ الفزع {q} {aj}")
    zs, q, aj = qailun("البلجة")
    tahaqqaq(q == ["ثابت"] and aj == [25] and J[25][2] == "2" and J[2][4] == "كتاب خلق الإنسان", f"٣ البلجة {q} {aj}")
    alfaz = sorted({z[3] for z in Z})
    by = {}
    for z in Z:
        by.setdefault(z[3], set())
        if z[4] not in BILA:
            by[z[3]].add(z[4])
    ithnan = sum(1 for v in by.values() if len(v) >= 2)

    # ٤: المحرّك
    if not os.path.exists(MUDIR):
        fashal.append("٤ mudir غيرُ مبنيّ (lake build)")
        return khatm()
    c, out = mudir("صَنِّفْ الفَزَعَ", d)
    o = qism_mukhassas(out)
    tahaqqaq(c == 1 and o.lstrip().startswith("لا حكم بالتواتر على الشجرة (K = 2)"), f"٤ الفزع: خروج {c}")
    tahaqqaq("القائلون المسمّون (2): أبو عبيد، أبو زيد" in o, "٤ الفزع: سطرُ القائلين")
    tahaqqaq("العدّ بالسجلّ (NTP.adad): 2 — يُقبل به عند K = 2؛ والعدّ بالشجرة (Silsila.adadS): 1" in o, "٤ الفزع: العدّان")
    tahaqqaq("الطريق: كتاب النخل [كتاب 1138 @2656563] › الإفزاع والخوف [عنوان 1312 @3023496]" in o, "٤ الفزع: الطريق")
    c, out = mudir("صنف البلجة", d)
    o = qism_mukhassas(out)
    tahaqqaq("الطريق: كتاب خلق الإنسان [كتاب 2 @25218] › الحاجب [عنوان 25 @146681]" in o and "القائلون المسمّون (1): ثابت" in o,
             "٤ البلجة: الطريق والقائل")
    bila_mudaa()

    # ٥: العيّنة
    ayyina = [w for w in alfaz if " " not in w][::500]
    mutabaq = 0
    for w in ayyina:
        _, q, aj = qailun(w)
        c, out = mudir(f"صنف {w}", d)
        o = qism_mukhassas(out)
        ok = f"القائلون المسمّون ({len(q)})" in o and f"زوجًا في {len(aj)} عقدة" in o
        tahaqqaq(ok, f"٥ «{w}»: المحرّكُ لا يطابق ({len(q)} قائلًا، {len(aj)} عقدة)")
        mutabaq += ok
    print(f"المودَع: {len(J)} عقدة، {len(Z)} زوجًا، {len(alfaz)} لفظًا متمايزًا؛ له قائلان مسمّيان فأكثر بمطابقة اللفظ التامّة {ithnan} "
          f"(يُقبل بالسجلّ عند K = 2)، وبالشجرة 0 (NTP.Mukhassas.la_yuqbal_bi_shajara)؛ العيّنة: {mutabaq} من {len(ayyina)} لفظًا مطابَقًا")
    return khatm()


def bila_mudaa():
    if not os.path.exists(MUDIR):
        return
    with tempfile.TemporaryDirectory() as f:
        c, out = mudir("صنف الفزع", f)
        o = qism_mukhassas(out)
        tahaqqaq("مودَعٌ غائب" in o and "القرار: تنفيذ «صنّف» على «الفزع»" in out, "٤ بلا مودَع: «مودَعٌ غائب» والقرار")


def khatm():
    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        sys.exit(1)
    print(f"test_ntp_mukhassas: {najah} فحصًا نجح")


if __name__ == "__main__":
    main()
