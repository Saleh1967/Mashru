"""يولّد Jisr/BabFaDawabit.lean من حالات ضابط باب الفاء المجمَّدة (tahaqquq/dawabit/fa/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_fa.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_fa.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "fa" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "BabFaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
SADR = {"واجب": ".wajib", "نفي_بلم": ".nafyLam", "نفي_بما_مضارع": ".nafyMaMudari", "نفي_بما_ماض": ".nafyMaMadi",
        "نفي_بلا": ".nafyLa", "نفي_اسمي": ".nafyIsmi", "نهي": ".nahy", "أمر": ".amr", "استفهام": ".istifham", "عرض": ".ard",
        "تمن": ".tamanni", "ظن": ".zann", "تشبيه_بنفي": ".tashbihNafy", "دعاء": ".dua"}
MANA = {"سبب": ".sabab", "شركة": ".shirka", "قطع": ".qat", "غير_معلن": ".ghayrMuallan"}
IRAB = {"نصب": ".nasb", "رفع": ".raf", "جزم": ".jazm"}
DARAJA = {"مقبول": ".maqbul", "ضعيف": ".daif", "قبيح": ".qabih", "خطأ": ".khata", "لا_حكم": ".laHukm"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def darajat(v, mawdi):
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(DARAJA, x, mawdi) for x in v) + "]"
    return "[" + qima(DARAJA, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d, k = h["id"], h["dakhil"], h["kharij"]
        shir = "none" if k["shir"] == "غير_مسؤول" else "some " + darajat(k["shir"], i)
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, ⟨{qima(SADR, d['sadr'], i)}, {qima(MANA, d['mana'], i)}, "
                     f"{qima(IRAB, d['irab'], i)}⟩, {darajat(k['kalam'], i)}, {shir}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «هذا باب الفاء» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/fa/cases.json` بـ `python3 -I scripts/bina_dawabit_fa.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلّ من الباب وحده قبل الشفرة (`tahaqquq/dawabit/fa/tajmid.json`). والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.BabFa\n\n"
        "namespace Jisr\nnamespace BabFa\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure Hala where\n  ism : String\n  fia : Fia\n  jumla : Jumla\n"
        "  /-- القيمةُ وحدها، أو البديلان في الغموض. -/\n  kalam : List Daraja\n"
        "  /-- `none`: «غير_مسؤول». -/\n  shir : Option (List Daraja)\n  deriving DecidableEq, Repr\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend BabFa\nend Jisr\n"
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
