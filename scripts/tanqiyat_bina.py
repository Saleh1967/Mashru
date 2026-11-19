"""تنقيةُ المبنيّ القديم: يحذف من `.lake/build/lib/lean` و`.lake/build/ir` ما كان لوحدةٍ لا ملفَّ مصدرٍ لها في الشجرة.

سببُه (ما ضُبطتُ عليه 2026-11-16): `Dal/QanunAdad.olean` بقي في `.lake` بعد حذف مصدره فأرضى `lake env lean Audit.lean` محلّيًّا
وسقط CI النظيف؛ وcache في CI يعيد `.lake` من تشغيلٍ سابق (restore-keys) فيحمل العيبَ نفسَه. فالمبنيُّ بلا مصدرٍ ليس شاهدًا ويُحذف
قبل البناء (خطوةٌ في bawwaba.yml) وقبل البوّابة محلّيًّا؛ وtest_tadqiq_tamm.py يرفض بقاءه.

التشغيل: python3 -I scripts/tanqiyat_bina.py          (يحذف ويطبع ما حُذف)
         python3 -I scripts/tanqiyat_bina.py --check  (يطبع ولا يحذف؛ يخرج 1 إن وُجد شيء)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAJALLAT = (os.path.join(".lake", "build", "lib", "lean"), os.path.join(".lake", "build", "ir"))


def wahda(rel):
    """مسارُ الوحدة من مسار الأثر النسبيّ: المجلّدُ واسمُ الملفّ إلى أوّل نقطة (أسماءُ الوحدات بلا نقاط؛ والامتداداتُ تتسلسل:
    `.olean.hash`، `.c.o.export.trace`، `.setup.json` …)، أو None لاسمٍ يبدأ بنقطة."""
    d, f = os.path.split(rel)
    ism = f.split(".", 1)[0]
    return os.path.join(d, ism) if ism else None


def qadim():
    out = []
    for majal in MAJALLAT:
        base = os.path.join(ROOT, majal)
        if not os.path.isdir(base):
            continue
        for dp, _, fs in os.walk(base):
            for f in fs:
                p = os.path.join(dp, f)
                w = wahda(os.path.relpath(p, base))
                if w is not None and not os.path.isfile(os.path.join(ROOT, w + ".lean")):
                    out.append(p)
    return sorted(out)


def main():
    fahs = "--check" in sys.argv[1:]
    q = qadim()
    for p in q:
        print(("قديم: " if fahs else "حُذف: ") + os.path.relpath(p, ROOT))
        if not fahs:
            os.remove(p)
    print(f"تنقيةُ المبنيّ: {len(q)} أثرًا بلا مصدر" + ("" if fahs else " حُذفت"))
    return 1 if (fahs and q) else 0


if __name__ == "__main__":
    sys.exit(main())
