"""يولّد Jisr/HamlJinsDawabit.lean من حالات ضابط «الحمل من الجنس» المجمَّدة (tahaqquq/dawabit/haml_jins/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_haml_jins.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_haml_jins.py [--check]
  بلا --check يكتب الملفّ؛ ومع --check يقارن ويخرج 1 إن اختلف.
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "haml_jins" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "HamlJinsDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
JINS = {"إنسان": "some .insan", "حيوان": "some .hayawan", "نبات": "some .nabat", "جماد": "some .jamad", "غائب": "none"}
QAB = {"السير": "some .sayr", "الركض": "some .rakd", "الجري": "some .jary", "الزحف": "some .zahf", "القفز": "some .qafz",
       "غائب": "none"}
NISBA = {"إسنادية": ".isnadiyya", "إضافية": ".idafiyya"}
HUKM = {"مرخَّص": ".murakhkhas", "لا_حكم": ".laHukm", "ممتنع": ".mumtani", "لا_جنس": ".laJins", "لا_مثال": ".laMithal"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def ahkam(v, mawdi):
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(HUKM, x, mawdi) for x in v) + "]"
    return "[" + qima(HUKM, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d = h["id"], h["dakhil"]
        sutur.append(
            f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {qima(JINS, d['jins'], i)}, {qima(QAB, d['mithal_qab'], i)}, "
            f"{qima(NISBA, d['nisba'], i)}, {ahkam(h['kharij']['hukm'], i)}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «الحمل من الجنس» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/haml_jins/cases.json` بـ `python3 -I scripts/bina_dawabit_haml_jins.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدر قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/haml_jins/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/haml_jins/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.HamlJinsDabit\n\n"
        "namespace Jisr\nnamespace QabiliyyaJins\nnamespace Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dabit\nend QabiliyyaJins\nend Jisr\n"
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
