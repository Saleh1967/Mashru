"""مولِّدُ `Aql/WaqiJadwal.lean` من دفعة «الواقع المختوم» (waqi_NNN.tsv): الصفوفُ بأعمدة الحكم وحدها، وبصمةُ الملفّ.

لا يُحرَّر المولَّد يدويًّا. والمخرجُ الخامّ ووقتُ المشاهدة وأمرُها لا تدخل Lean (لا يأخذها الحكم)؛ تبقى في المودَع ويطابقها
الاختبار `tahaqquq/test_waqi.py`.

التشغيل:  python3 -I scripts/bina_waqi.py <waqi_001.tsv>  > Aql/WaqiJadwal.lean
"""
import hashlib
import sys

WAJH = {"قياس": ".qiyas", "حكاية": ".hikaya"}


def lit(s):
    """سلسلةُ Lean حرفيّة: يُهرَّب الخطّ المائل وعلامةُ التنصيص؛ وما سواهما يُرفض إن كان محرفَ تحكّم."""
    if any(ord(c) < 32 for c in s):
        raise SystemExit(f"مرفوض: محرفُ تحكّمٍ في «{s}»")
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def wallid(data):
    lines = data.decode("utf-8").split("\n")
    head = lines[0].split("\t")
    col = {k: i for i, k in enumerate(head)}
    out = ["/-",
           "  Aql/WaqiJadwal.lean — مولَّدٌ بـ `python3 -I scripts/bina_waqi.py <waqi_001.tsv>` من دفعة «الواقع المختوم»؛ لا يُحرَّر يدويًّا.",
           "  أعمدةُ الحكم وحدها (الموضع، الحاسّة، المصدر، الشيء، الخاصّة، القيمة، الوجه)؛ وبصمةُ الملفّ كاملًا.",
           "-/",
           "import Aql.Waqi",
           "",
           "namespace Waqi.Jadwal",
           "",
           "/-- بصمةُ sha256 لملفّ الدفعة كما رُصد. -/",
           f'def basma : String := "{hashlib.sha256(data).hexdigest()}"',
           "",
           "/-- صفوفُ الدفعة. -/",
           "def jadwal : List Mushahada := ["]
    rows = [l.split("\t") for l in lines[1:] if l]
    for n, r in enumerate(rows):
        w = WAJH.get(r[col["wajh"]])
        if w is None:
            raise SystemExit(f"مرفوض: وجهٌ مجهول في الصفّ {r[0]}")
        sep = "," if n + 1 < len(rows) else ""
        out.append(f"  ⟨{int(r[col['raqm']])}, {lit(r[col['hassa']])}, {lit(r[col['masdar']])}, {lit(r[col['mawdu']])}, "
                   f"{lit(r[col['sifa']])}, {lit(r[col['qima']])}, {w}⟩{sep}")
    out += ["]", "", "end Waqi.Jadwal", ""]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.stdout.write(wallid(open(sys.argv[1], "rb").read()))
