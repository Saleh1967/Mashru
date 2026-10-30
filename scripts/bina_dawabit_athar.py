"""يولّد Nizam/AtharDawabit.lean من حالات ضابط «أثر العُقَد» المجمَّدة (tahaqquq/dawabit/athar/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه. والجملةُ تُنقل نصًّا كما كُتبت،
والمحرّكُ يقرؤها في Lean (`Nizam.Athar.Dabit.natijaHala`)، فلا قراءةَ هنا. والمخرجُ يطابقه tahaqquq/test_athar_dabit.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_athar.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "athar" / "cases.json"
MAKHRAJ = JADHR / "Nizam" / "AtharDawabit.lean"

NAW = {"قوة": ".quwwa", "قيد": ".qayd"}
FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
QUWWA = {"إثبات": ".ithbat", "نفي": ".nafy", "تعليق": ".taliq", "إنشاء": ".insha", "لا_حكم": ".laHukm"}
QAYD = {"صفة": ".sinf .sifa", "شرط": ".sinf .shart", "غاية": ".sinf .ghaya", "عدد": ".sinf .adad", "لا_قيد": ".laQayd",
        "لا_حكم": ".laHukm"}
HAQL = {"قوة": ("quwwa", QUWWA), "قيد": ("qayd", QAYD)}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def qiyam(jadwal, v, mawdi):
    """المتوقَّع: قيمةٌ واحدة، أو قائمةٌ من اثنتين فأكثر."""
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(jadwal, x, mawdi) for x in v) + "]"
    return "[" + qima(jadwal, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i = h["id"]
        naw = h["naw"]
        if naw not in HAQL:
            raise SystemExit(f"نوعٌ لا منشئَ له: «{naw}» في {i}")
        haql, jadwal = HAQL[naw]
        kharij = h.get("kharij")
        if not isinstance(kharij, dict) or set(kharij) != {haql}:
            raise SystemExit(f"المخرجُ في {i} ليس حقلَ نوعه «{haql}» وحده")
        taw = qiyam(jadwal, kharij[haql], i)
        quwwa, qayd = (taw, "[]") if haql == "quwwa" else ("[]", taw)
        zawj = "none" if h.get("zawj") is None else "some " + nass_lean(h["zawj"])
        sutur.append(f"  -- {i}\n"
                     f"  ⟨{nass_lean(i)}, {NAW[naw]}, {qima(FIA, h['fia'], i)}, {nass_lean(h['nass'])},\n"
                     f"   {quwwa}, {qayd}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «أثر العُقَد» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/athar/cases.json` بـ `python3 -I scripts/bina_dawabit_athar.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والنطاق، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/athar/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/athar/tajmid.json`. والجملةُ نصُّها كما كُتبت؛ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Nizam.AtharDabit\n\n"
        "namespace Nizam.Athar\nnamespace Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dabit\nend Nizam.Athar\n"
    return (ras + jism + khatm).encode("utf-8")


def main():
    natija = wallid(HALAT.read_bytes())
    if "--check" in sys.argv[1:]:
        if not MAKHRAJ.exists() or MAKHRAJ.read_bytes() != natija:
            print(f"{MAKHRAJ.relative_to(JADHR)} ليس مخرجَ المولِّد بايتًا")
            return 1
        print("مطابق")
        return 0
    MAKHRAJ.write_bytes(natija)
    print(f"كُتب {MAKHRAJ.relative_to(JADHR)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
