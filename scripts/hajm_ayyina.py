"""أحجامُ العيّنة في `hawkama/معايير_القياس.md` §٢.٤: لكلّ عتبة T وعددِ أخطاءٍ e، أقلُّ عددٍ محسومٍ n يكون فيه الحدُّ الأدنى لفترة
ولسن 95% لنسبة (n − e)/n فوق T. صيغةُ ولسن وz = 1.96 كما في `tahaqquq/qiyas_d.py` (`wilson`). ولعمود e = 0 صيغةٌ مغلقة يطابقها
الحسابُ: الحدُّ الأدنى عند الصفر n/(n + z²)، فـ n > T·z²/(1 − T).
التشغيل: python3 -I scripts/hajm_ayyina.py
"""
from math import sqrt, floor

Z = 1.96
ATABAT = (0.85, 0.90, 0.95, 0.98, 0.99)
AKHTA = (0, 1, 2)


def adna(k, n, z=Z):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - r) / d


def aqall(t, e):
    n = e + 1
    while adna(n - e, n) <= t:
        n += 1
    return n


if __name__ == "__main__":
    print("العتبة\t" + "\t".join(f"أخطاء {e}" for e in AKHTA) + "\tالصيغة المغلقة (e=0)")
    for t in ATABAT:
        row = [aqall(t, e) for e in AKHTA]
        mughlaqa = floor(t * Z * Z / (1 - t)) + 1
        assert row[0] == mughlaqa, (t, row[0], mughlaqa)
        print(f"{t:.0%}\t" + "\t".join(f"{n:,}" for n in row) + f"\t{mughlaqa:,}")
