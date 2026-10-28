"""جمعُ أقسام البند ٦ على CI (قرار المالك 2026-10-28: اختار من سؤالٍ متعدّد الخيارات «الاثنان (موصى به)»، ونصُّ الخيار من البنّاء).

كلُّ وظيفةٍ من وظائف «tafrat» تُجري `bawwaba.py --tafrat-faqat --qism i/n` فتطبع «١ البناء: نجح» وسطرَ «٦ الطفرات (القسم i من n):
قُتلت x من y»، ثمّ تُلحق خطوتُها في bawwaba.yml «رمز الخروج: c». وهذا السكربت يحكم بأنّ الأقسامَ تامّة: كلُّ مخرجٍ فيه السطورُ الثلاثة
مرّةً والرمزُ 0 ومخرجُ خطئه فارغ، وكلُّ قسمٍ من 1 إلى n حاضرٌ مرّةً بـn واحد، ومجموعُ y عددُ الطفرات في tahaqquq/tafrat.json،
وكلُّ طفرةٍ قُتلت — فلا يُعدّ البند ٦ ناجحًا وقسمٌ منه لم يجرِ (كأن تنقص المصفوفةُ في bawwaba.yml عن n). ثمّ يجمع العدد.
وحدُّه: أثرٌ بقي من محاولةٍ سابقةٍ لقسمٍ لم يرفع في الجارية لا يُميَّز هنا؛ تحرسه خطوةُ «jam» بنتيجة وظائف tafrat نفسِها (needs).

التشغيل: python3 -I tahaqquq/jam_tafrat.py <مجلّد> — فيه مجلّدٌ لكلّ قسمٍ فيه tafrat_out.txt (وtafrat_err.txt إن وُجد)،
كما يضعها actions/download-artifact. الخروج 0 إن تمّت الأقسامُ وقُتلت كلُّ طفرة، وإلّا 2، ويُسمّى السبب.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMAT = re.compile(r"^٦ الطفرات \(القسم ([0-9]+) من ([0-9]+)\): قُتلت ([0-9]+) من ([0-9]+)(?:، وغيرُ محسومة ([0-9]+))?$", re.M)


def jam(makhrajat, kull):
    """makhrajat: أزواجُ (مخرج، مخرجُ خطأ) للأقسام نصوصًا؛ kull: عددُ الطفرات. يردّ (سطرُ التقرير، قائمةُ العيوب)."""
    uyub, aqsam = [], {}
    for k, (nass, khata) in enumerate(makhrajat):
        if nass.splitlines().count("١ البناء: نجح") != 1:
            uyub.append(f"المخرج {k + 1}: ليس فيه «١ البناء: نجح» مرّةً واحدة")
        if re.findall(r"^رمز الخروج: (-?[0-9]+)$", nass, re.M) != ["0"]:
            uyub.append(f"المخرج {k + 1}: رمزُ الخروج ليس 0 مرّةً واحدة")
        if khata.strip():
            uyub.append(f"المخرج {k + 1}: مخرجُ خطئه غيرُ فارغ")
        m = NAMAT.findall(nass)
        if len(m) != 1:
            uyub.append(f"المخرج {k + 1}: {len(m)} سطرًا للبند ٦ بقسمه (المطلوب واحد)")
            continue
        i, n, qutilat, min_, ghayr = (int(x) if x else 0 for x in m[0])
        if (i, n) in aqsam:
            uyub.append(f"القسم {i} من {n} مكرَّر")
        aqsam[(i, n)] = (qutilat, min_, ghayr)
    adad = {n for _, n in aqsam}
    if len(adad) > 1:
        uyub.append("الأقسامُ بأعدادٍ مختلفة: " + "، ".join(str(n) for n in sorted(adad)))
    n = max(adad) if adad else 0
    naqis = [i for i in range(1, n + 1) if (i, n) not in aqsam]
    if not aqsam:
        uyub.append("لا قسم")
    elif naqis:
        uyub.append(f"أقسامٌ لم تجرِ من {n}: " + "، ".join(str(i) for i in naqis))
    qutilat = sum(v[0] for v in aqsam.values())
    majmu = sum(v[1] for v in aqsam.values())
    ghayr = sum(v[2] for v in aqsam.values())
    if majmu != kull:
        uyub.append(f"مجموعُ الأقسام {majmu} طفرةً، وفي tafrat.json {kull}")
    if qutilat + ghayr != majmu:
        uyub.append(f"عاشت {majmu - qutilat - ghayr} طفرة")
    if ghayr:
        uyub.append(f"غيرُ محسومة {ghayr}")
    satr = f"٦ الطفرات ({len(aqsam)} قسمًا من {n}): قُتلت {qutilat} من {majmu}" + (f"، وغيرُ محسومة {ghayr}" if ghayr else "")
    return satr, uyub


def main():
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("الاستعمال: python3 -I tahaqquq/jam_tafrat.py <مجلّد مخرجات الأقسام>", file=sys.stderr)
        sys.exit(2)
    with open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8") as f:
        kull = len(json.load(f))
    makhrajat = []
    for d in sorted(os.listdir(sys.argv[1])):
        p = os.path.join(sys.argv[1], d, "tafrat_out.txt")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            nass = f.read()
        e = os.path.join(sys.argv[1], d, "tafrat_err.txt")
        khata = ""
        if os.path.exists(e):
            with open(e, encoding="utf-8") as f:
                khata = f.read()
        makhrajat.append((nass, khata))
    satr, uyub = jam(makhrajat, kull)
    print(satr)
    for nass, _ in makhrajat:
        for m in NAMAT.finditer(nass):
            print("  " + m.group(0))
    if uyub:
        print("\n".join(uyub), file=sys.stderr)
    for _, khata in makhrajat:
        if khata.strip():
            print(khata, file=sys.stderr)
    sys.exit(2 if uyub else 0)


if __name__ == "__main__":
    main()
