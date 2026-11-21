"""شبكةُ NTP من المخصّص المختوم: جدولٌ مشتقٌّ يقرؤه وكيلُ `NTP.Mukhassas` في `mudir` (`Madlul/NTP/Mukhassas.lean`).

السند: أمرُ المالك 2026-11-21 (13:57 بتوقيت عمّان) «انت مفوض بجعل mashru يعمل بشكل متكامل … لتحقيق أقصى النتائج من ntp»، ومعه
الإذنُ بختم المودَعات واعتماد الجداول. والمادّةُ مخرجُ `shabaka/mukhassas_shabaka.py` على `mukhassas.txt` المختوم (`936c68e0…`) بعينه:
يعيد ‎`shabaka/out/{ajnas,azwaj}.json` المودَعين في المستودع بايتًا (قيس 2026-11-21)، فلا قاعدةَ استخراجٍ جديدة هنا — تحويلُ صيغةٍ فقط.

المخرج `ntp_mukhassas.tsv` (UTF-8، أسطرٌ تنتهي بـLF، بلا رأس)، ستّةُ حقولٍ في كلّ سطر:
  jins <TAB> رقمُ العقدة <TAB> رقمُ الأب أو «-» <TAB> نوعُ العنوان <TAB> العنوان <TAB> إزاحةُ المحرف في mukhassas.txt
  zawj <TAB> رقمُ الزوج <TAB> رقمُ العقدة <TAB> اللفظ <TAB> القائل <TAB> إزاحةُ المحرف
بترتيب المخرج نفسه (العقدُ ثمّ الأزواج)؛ وما في حقله TAB أو LF يُرفض باسمه (لا يُصلَح).
التشغيل: python3 -I scripts/bina_ntp_mukhassas.py <مجلّد فيه mukhassas.txt>   (يكتب ntp_mukhassas.tsv فيه)
"""
import json
import os
import subprocess
import sys
import tempfile

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def haql(x):
    s = str(x)
    if "\t" in s or "\n" in s:
        raise ValueError(f"حقلٌ فيه TAB أو LF: {s[:40]!r}")
    return s


def nass(ajnas, azwaj):
    out = []
    for j in ajnas:
        out.append("\t".join(haql(x) for x in ("jins", j["id"], "-" if j["parent"] is None else j["parent"], j["naw"], j["title"], j["off"])))
    for z in azwaj:
        out.append("\t".join(haql(x) for x in ("zawj", z["id"], z["jins"], z["lafz"], z["qail"], z["off"])))
    return "".join(l + "\n" for l in out)


def main(argv):
    d = argv[0]
    src = os.path.join(d, "mukhassas.txt")
    with tempfile.TemporaryDirectory() as t:
        r = subprocess.run([sys.executable, "-I", os.path.join(JADHR, "shabaka", "mukhassas_shabaka.py"), src, t],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-400:] + r.stderr[-400:])
            return 1
        ajnas = json.load(open(os.path.join(t, "ajnas.json"), encoding="utf-8"))["ajnas"]
        azwaj = json.load(open(os.path.join(t, "azwaj.json"), encoding="utf-8"))
    b = nass(ajnas, azwaj).encode("utf-8")
    open(os.path.join(d, "ntp_mukhassas.tsv"), "wb").write(b)
    print(f"ntp_mukhassas.tsv: {len(ajnas)} عقدة، {len(azwaj)} زوجًا")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
