"""يعيد بناءَ «جدول الجنس — القطعة الأولى» (jins.tsv) و«جدول المثال — القطعة الأولى» (mithal.tsv) بايتًا كما خُتما (2026-11-17).

الصفوفُ صفوفُ `Nizam.Rabt.jinsMurashshah` و`mithalMurashshah`، والسندُ بسطره من اللسان والمخصّص المختومين، كما وصفها سجلُّ المودَعات؛
والبايتاتُ هي بايتاتُ أمر البنّاء الذي أنشأهما في جلسة الختم (منقولًا بنصّه من سجلّ تلك الجلسة). ولا يُكتب جدولٌ إلّا وبصمتُه بصمتُه
المختومة في `mudaat/sijill.json`؛ وإلّا رُفض باسمه ولم يُكتب شيء. وإن حضر lisan.txt في المجلّد فُحص أنّ كلَّ نصٍّ في سطره بعينه.

التشغيل: python3 -I scripts/bina_jadawil_rabt.py <مجلّد المودَعات>
"""
import hashlib
import json
import os
import sys

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

JADAWIL = {
    "jins.tsv": "jidhr\tqism\tsanad\tnass\twasm\n"
                "ولد\tإنسان\tlisan.txt 34fa56710a5b@69262؛ mukhassas.txt 936c68e0c2c6@446 (باب الحمل والولادة، تحت كتاب خلق الإنسان @383)"
                "\tالوليد: الصبي حين يولد\tالقسمُ تعيينُ البنّاء من النصّ\n"
                "دور\tجماد\tlisan.txt 34fa56710a5b@82798؛ mukhassas.txt 936c68e0c2c6@16542 (أسماء عامة المنازل والأوطان)"
                "\tوالدار: المحل\tالقسمُ تعيينُ البنّاء من النصّ\n",
    "mithal.tsv": "jidhr\tqabiliyya\tsanad\tnass\twasm\n"
                  "ذهب\tالسير\tlisan.txt 34fa56710a5b@13268\tالذهاب: السير والمرور\tنصُّ المعجم\n",
}
NUSUS = [(69262, "الوليد: الصبي حين يولد"), (82798, "والدار: المحل"), (13268, "الذهاب: السير والمرور")]


def makhtum():
    s = json.load(open(os.path.join(JADHR, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    return {m["milaf"]: m["sha256"] for m in s if m.get("hala") == "مختوم"}


def main(d):
    mk = makhtum()
    khata = 0
    for milaf, nass in JADAWIL.items():
        b = nass.encode("utf-8")
        h = hashlib.sha256(b).hexdigest()
        if mk.get(milaf) != h:
            print(f"مرفوض: {milaf} بصمتُه {h[:12]} ليست بصمتَه المختومة ({(mk.get(milaf) or 'غير مختوم')[:12]})")
            khata = 1
            continue
        open(os.path.join(d, milaf), "wb").write(b)
        print(f"كُتب: {milaf} {h[:12]} = المختوم")
    lisan = os.path.join(d, "lisan.txt")
    if os.path.exists(lisan):
        asatir = open(lisan, encoding="utf-8").read().split("\n")
        for n, q in NUSUS:
            if q not in asatir[n - 1]:
                print(f"مرفوض: النصّ «{q}» ليس في اللسان س{n}")
                khata = 1
    return khata


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
