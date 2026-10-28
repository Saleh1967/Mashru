"""يولّد Jisr/IsharaDawabit.lean من حالات ضابط أسماء الإشارة المجمَّدة (tahaqquq/dawabit/ishara/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_ishara.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_ishara.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "ishara" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "IsharaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
ASL = {"ذا": ".dha", "ذي": ".dhi", "ذه": ".dhih", "تي": ".ti", "ته": ".tih", "تا": ".ta", "ذان": ".dhan", "تان": ".tan",
       "ذين": ".dhayn", "تين": ".tayn", "أولاء": ".ulaa", "أولى": ".ula", "هنا": ".huna", "ثم": ".thamma"}
MUSHAR = {"مفرد_مذكر": ".mufradMudhakkar", "مفرد_مؤنث": ".mufradMuannath", "مثنى_مذكر": ".muthannaMudhakkar",
          "مثنى_مؤنث": ".muthannaMuannath", "جمع_مذكر": ".jamMudhakkar", "جمع_مؤنث": ".jamMuannath", "مكان": ".makan"}
MAWDI = {"رفع": ".raf", "نصب": ".nasb", "جر": ".jarr"}
BUD = {"قريب": ".qarib", "بعيد": ".baid"}
HUKM = {"مقبول": ".maqbul", "خطأ": ".khata", "لا_حكم": ".laHukm"}
HUQUL = ["asl", "mushar", "mawdi", "bud", "ha", "lam", "kaf"]


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def mantiqi(k, mawdi):
    if not isinstance(k, bool):
        raise SystemExit(f"قيمةٌ ليست منطقيّة: «{k}» في {mawdi}")
    return "true" if k else "false"


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def hukm(h, i):
    if isinstance(h, list):
        if len(h) < 2:
            raise SystemExit(f"hukm قائمةٌ دون بديلين في {i}")
        return "[" + ", ".join(qima(HUKM, x, i) for x in h) + "]"
    return "[" + qima(HUKM, h, i) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d = h["id"], h["dakhil"]
        if sorted(d) != sorted(HUQUL):
            raise SystemExit(f"حقولُ dakhil غيرُ حقول المواصفة في {i}")
        dakhil = (f"⟨{qima(ASL, d['asl'], i)}, {qima(MUSHAR, d['mushar'], i)}, {qima(MAWDI, d['mawdi'], i)}, "
                  f"{qima(BUD, d['bud'], i)}, {mantiqi(d['ha'], i)}, {mantiqi(d['lam'], i)}, {mantiqi(d['kaf'], i)}⟩")
        z = h.get("zawj")
        zawj = "none" if z is None else f"some {nass_lean(z)}"
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {hukm(h['hukm'], i)}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط أسماء الإشارة المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/ishara/cases.json` بـ `python3 -I scripts/bina_dawabit_ishara.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/ishara/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/ishara/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.IsharaDabit\n\n"
        "namespace Jisr\nnamespace Ishara\nnamespace Dawabit\n\n"
        "open Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend Ishara\nend Jisr\n"
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
