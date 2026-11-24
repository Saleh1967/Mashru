"""يبني «جدول القسمة — القطعة الأولى (الكون والإنسان والحياة)» (qisma.tsv) بايتًا، ومنه `Madlul/QismaJadwal.lean`.

الطلب: قولُ المالك في الجلسة 2026-11-24 (14:02 بتوقيت عمّان): «… كما  تُودَع قسمة تغطي الكون والإنسان والحياةوتغطي («أحياء وأشياء»،
ثمّ الكواكب والجبال) جدولًا …»، ثمّ (21:10) «موافق انت خبير نفذ ومعك الأذن بالختم والايداع واعتماد المصادر».
الصفوفُ من نصّين مختومين بأسطرهما — الشخصية ج1 (a1.txt، 25a91560a646) والّلسان (lisan.txt، 34fa56710a5b) — ومن قول المالك نفسِه؛
وعمودُ `wasm` يقول أيَّها نصٌّ وأيَّها قولُ المالك وأيَّها تعيينُ البنّاء. ولا يُكتب الجدولُ إلّا وبصمتُه بصمتُه المختومة إن كان مختومًا،
وإن حضر المصدران في المجلّد فُحص أنّ كلَّ نصٍّ في سطره بعينه.

التشغيل: python3 -I scripts/bina_qisma.py <مجلّد المودَعات>      يكتب qisma.tsv
          python3 -I scripts/bina_qisma.py --lean                  يطبع Madlul/QismaJadwal.lean
"""
import hashlib
import json
import os
import sys

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A1 = "a1.txt 25a91560a646"
LS = "lisan.txt 34fa56710a5b"
MALIK = "المالك 2026-11-24 14:02"
N523 = "الفكرة الكلية عن الكون والإنسان والحياة"
N321 = "في الكون نفسه، في الموجودات: في الأرض والشمس والقمر والنجوم والحيوان والإنسان والدواب والإبل والجبال"
NGHAYB = "وحين يبحث فيما وراء الكون مما لا يقع تحت الحس"
NKAWKAB = "الكوكب والكوكبة: النجم"
NMALIK = "«أحياء وأشياء»، ثمّ الكواكب والجبال"
TAYIN_AB = "الأبُ تعيينُ البنّاء: موجودٌ في الكون"

# raqm, ism, ab, mahsus, sanad, nass, wasm
SUFUF = [
    (1, "الكون", "", "نعم", f"{A1}@523", N523, "نصّ"),
    (2, "الإنسان", "", "نعم", f"{A1}@523", N523, "نصّ"),
    (3, "الحياة", "", "نعم", f"{A1}@523", N523, "نصّ"),
    (4, "ما وراء الكون", "", "لا", f"{A1}@321", NGHAYB, "نصّ"),
    (5, "أحياء", "الكون", "نعم", MALIK, NMALIK, "قول المالك؛ " + TAYIN_AB),
    (6, "أشياء", "الكون", "نعم", MALIK, NMALIK, "قول المالك؛ " + TAYIN_AB),
    (7, "الأرض", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (8, "الشمس", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (9, "القمر", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (10, "الكواكب", "الكون", "نعم", MALIK, NMALIK, "قول المالك؛ " + TAYIN_AB),
    (11, "النجوم", "الكواكب", "نعم", f"{A1}@321؛ {LS}@24829", N321 + "؛ " + NKAWKAB, "نصّ؛ الأبُ من اللسان"),
    (12, "الحيوان", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (13, "الدواب", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (14, "الإبل", "الكون", "نعم", f"{A1}@321", N321, "نصّ"),
    (15, "الجبال", "الكون", "نعم", f"{A1}@321؛ {MALIK}", N321 + "؛ " + NMALIK, "نصّ وقول المالك"),
]
NUSUS = [("a1.txt", 523, N523), ("a1.txt", 321, N321), ("a1.txt", 321, NGHAYB), ("lisan.txt", 24829, NKAWKAB)]
MILAF = "qisma.tsv"


def nass():
    r = ["raqm\tism\tab\tmahsus\tsanad\tnass\twasm"]
    r += ["\t".join(str(x) for x in s) for s in SUFUF]
    return ("\n".join(r) + "\n").encode("utf-8")


def lean():
    q = lambda s: '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    r = ["/-! مولَّدٌ بـ `python3 -I scripts/bina_qisma.py --lean` من «جدول القسمة — القطعة الأولى» (qisma.tsv)؛ لا يُحرَّر يدويًّا.",
         f"  بصمةُ الجدول: {hashlib.sha256(nass()).hexdigest()} -/", "",
         "namespace Madlul.QismaJadwal", "",
         "/-- (الرقم، الاسم، الأب، محسوس). -/",
         "def sufuf : List (Nat × String × String × Bool) := ["]
    r += [f"  ({s[0]}, {q(s[1])}, {q(s[2])}, {'true' if s[3] == 'نعم' else 'false'})" + ("," if i < len(SUFUF) - 1 else "")
          for i, s in enumerate(SUFUF)]
    r += ["]", "", "end Madlul.QismaJadwal", ""]
    return "\n".join(r)


def makhtum():
    s = json.load(open(os.path.join(JADHR, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    return {m["milaf"]: m["sha256"] for m in s if m.get("hala") == "مختوم"}


def main(d):
    b = nass()
    h = hashlib.sha256(b).hexdigest()
    mk = makhtum().get(MILAF)
    if mk is not None and mk != h:
        print(f"مرفوض: {MILAF} بصمتُه {h[:12]} ليست بصمتَه المختومة ({mk[:12]})")
        return 1
    khata = 0
    for milaf, n, q in NUSUS:
        p = os.path.join(d, milaf)
        if os.path.exists(p):
            asatir = open(p, encoding="utf-8").read().split("\n")
            if q not in asatir[n - 1]:
                print(f"مرفوض: النصّ «{q}» ليس في {milaf} س{n}")
                khata = 1
    if khata:
        return 1
    open(os.path.join(d, MILAF), "wb").write(b)
    print(f"كُتب: {MILAF} {h[:12]}" + (" = المختوم" if mk else " (غير مختوم بعد)"))
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--lean"]:
        sys.stdout.write(lean())
        sys.exit(0)
    sys.exit(main(sys.argv[1]))
