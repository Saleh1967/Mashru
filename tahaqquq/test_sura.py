"""نموُّ زمن الفاحص التنفيذيّ ليس تربيعيًّا (س1؛ قولُ المالك 2026-10-24، 18:07 «نفذ وفق افضل الممارسات»).

مخزنٌ مولَّد بـ N = 50,000 ادّعاء (لكلٍّ أصلُ وضعٍ واحد وقانونُ «مطابقة-من-الوضع» واحد على هيئة القاعدة) ثمّ بـ 2N. يقبله الفاحص
كلَّه («مرفوض 0، أخطاء 0»)، والسؤالُ الواحد عليه حكمٌ واحد. والتوقّع من معنى البحث لا من المخرج: بحثٌ في الجدول والمصفوفة ثابتُ الكلفة
للادّعاء، فمضاعفةُ المخزن تضاعف الزمنَ تقريبًا؛ وبحثٌ خطّيٌّ في الأصول (`find?`) أو في قائمة القوانين (`List`) يجعل كلفةَ الادّعاء
تابعةً لحجم المخزن، فتقارب النسبةُ أربعة.

١. الفحصُ كلُّه: نسبةُ زمن 2N إلى زمن N لا تزيد على 3.
٢. سؤالٌ واحد (يبني المخزن كلَّه بـ `Makhzan.udkhulA` ثمّ يسأله): النسبةُ نفسُها لا تزيد على 3.

الحدّ 3 يفصل بين الخطّيّ (2) والتربيعيّ (4)، ولا يثبت الخطّيّة: يمنع التربيعيّ وحده. والزمنُ زمنُ المعالج للعمليّة الابن (فرقُ
`resource.getrusage(RUSAGE_CHILDREN)`) لا زمنُ الساعة؛ والحجمان يُشغَّلان متناوبَين ثلاث مرّات، ويؤخذ أقلُّ زمنٍ لكلٍّ منهما، فيُنقص ذلك
أثرَ تغيّر حمل الآلة ولا يُلغيه (تنازعُ الذاكرة باقٍ؛ وتراوحت النسبةُ على الفرع 1.84–2.44). وتُطبع النسبتان. والحكمُ على النسبة لا على
الزمن المطلق.

الطفرتان: P463 (الفحصُ بـ `maqbul` على القائمة) وP464 (السؤالُ بـ `udkhul` على القائمة) لا تغيّران الدلالة (`maqbulA_eq`، `udkhulA_eq`)،
فلا يقتلهما إلّا هذا. ولذلك هو آخرُ اختبارات الطفرات في `bawwaba.IKHTIBARAT_TAFRAT`: لا يجري إلّا على طفرةٍ نجت ممّا قبله.
التشغيل: python3 -I tahaqquq/test_sura.py
"""
import os
import resource
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXE = os.path.join(ROOT, ".lake", "build", "bin", "faahis")
IKHTIBAR = os.path.join(ROOT, "mawsua", "sijill_ikhtibar.tsv")
N = 50000
HADD = 3


def mukhazzan_muwallad(path, n):
    with open(path, "w", encoding="utf-8") as f:
        f.write("isdar\tshahid-numuw\n")
        for i in range(n):
            f.write(f"qanun\tمطابقة-من-الوضع\twad:w{i}:m{i}\tmutabaqa:w{i}:m{i}\tمطابق\n")
        for i in range(n):
            f.write(f"asl\twad:w{i}:m{i}\tتقدير\taaaaaaaaaaaa@{i}\n")
        for i in range(n):
            f.write(f"iddia\tmutabaqa:w{i}:m{i}\tتقدير\ta=wad:w{i}:m{i}|q={i}\ts{i}\n")


def muaalij():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def tashghil(path, n, sual):
    """زمنُ المعالج لتشغيلٍ واحد، بعد التحقّق من مخرجه."""
    cmd = [EXE, "--sual", "mutabaqa:w7:", IKHTIBAR, path] if sual else [EXE, IKHTIBAR, path]
    c0 = muaalij()
    p = subprocess.run(cmd, capture_output=True, text=True)
    t = muaalij() - c0
    out = p.stdout.splitlines()
    if sual:
        assert p.returncode == 0 and out and out[0] == "حكم (1) بالقاعدة shahid-numuw:", out[:2]
    else:
        akhir = out[-1] if out else ""
        assert p.returncode == 0 and akhir.endswith(f"ادّعاءات {n}، مرفوض 0، أخطاء 0"), akhir
    return t


ok = 0
with tempfile.TemporaryDirectory() as d:
    a, b = os.path.join(d, "n.tsv"), os.path.join(d, "2n.tsv")
    mukhazzan_muwallad(a, N)
    mukhazzan_muwallad(b, 2 * N)
    for sual in (False, True):
        ta = tb = None
        for _ in range(3):
            x = tashghil(a, N, sual)
            y = tashghil(b, 2 * N, sual)
            ta = x if ta is None else min(ta, x)
            tb = y if tb is None else min(tb, y)
        nisba = tb / ta
        ism = "السؤال" if sual else "الفحص"
        print(f"{ism}: {ta:.2f} ث ← {tb:.2f} ث (زمن المعالج)، النسبة {nisba:.2f}")
        assert nisba <= HADD, f"النموّ تربيعيّ ({ism}): النسبة {nisba:.2f} فوق {HADD}"
        ok += 1

print(f"{ok}/2")
sys.exit(0)
