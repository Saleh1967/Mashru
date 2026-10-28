"""يولّد Faahis/SijillMakhtum.lean من mudaat/sijill.tsv (سجلّ المودَعات المختوم الذي يولّده mudaat/idaa.py)، أسطرًا بنصّها.

الحزمة P1-ج من hawkama/خطة_الإطلاق_التجريبي.md: السجلُّ الممرَّر إلى faahis وqari يُطابَق بهذه الأسطر قبل التحميل، فسجلٌّ غيرُه يُرفض باسمه
إلّا بـ--ikhtibar المعلَن. لا يُحرَّر الملفّ المولَّد يدويًّا.
التشغيل: python3 -I scripts/bina_sijill_makhtum.py [--check]
"""
import json
import os
import sys

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV = os.path.join(JADHR, "mudaat", "sijill.tsv")
OUT = os.path.join(JADHR, "Faahis", "SijillMakhtum.lean")


def wallid():
    asatir = open(TSV, encoding="utf-8").read().split("\n")
    if asatir and asatir[-1] == "":
        asatir = asatir[:-1]
    body = ",\n".join("  " + json.dumps(l, ensure_ascii=False) for l in asatir)
    return ("/-\n  Faahis/SijillMakhtum.lean — مولَّدٌ بـ `python3 -I scripts/bina_sijill_makhtum.py` من `mudaat/sijill.tsv`؛ لا يُحرَّر يدويًّا.\n"
            "  أسطرُ سجلّ المودَعات المختوم بنصّها: السلطةُ المعتمدة للفاحص والقارئ (الحزمة P1-ج).\n-/\n\n"
            "/-- أسطرُ `mudaat/sijill.tsv` بترتيبها. -/\n"
            f"def sijillMakhtum : List String := [\n{body}\n]\n")


if __name__ == "__main__":
    nass = wallid()
    if "--check" in sys.argv[1:]:
        ok = open(OUT, encoding="utf-8").read() == nass
        print("مطابق" if ok else "SIJILL_MAKHTUM_GHAYR_MUTABIQ: أعد التوليد")
        sys.exit(0 if ok else 1)
    open(OUT, "w", encoding="utf-8").write(nass)
    print(OUT)
