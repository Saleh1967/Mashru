"""يولّد Jisr/BabJazaDawabit.lean من حالات ضابط باب الجزاء المجمَّدة (tahaqquq/dawabit/jaza/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_jaza.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_jaza.py [--check]
  بلا --check يكتب الملفّ؛ ومع --check يقارن ويخرج 1 إن اختلف.
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "jaza" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "BabJazaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum"}
TARTIB = {"شرط_أولا": ".shartAwwalan", "جواب_أولا": ".jawabAwwalan"}
SHART = {"مضارع_مجزوم": ".mudariMajzum", "مضارع_مرفوع": ".mudariMarfu", "ماض": ".madi"}
JAWAB = {
    "مضارع_مجزوم": ".mudariMajzum", "مضارع_مرفوع": ".mudariMarfu", "ماض": ".madi",
    "فاء_اسمية": ".faIsmiyya", "فاء_مضارع_مرفوع": ".faMudariMarfu", "فاء_مضارع_مجزوم": ".faMudariMajzum",
    "فاء_غيرهما": ".faGhayr", "إذا_اسمية": ".idhaIsmiyya", "فاء_إذا": ".faIdha", "اسمية": ".ismiyya",
    "واو": ".waw", "ثم": ".thumma", "لام_قسم": ".lamQasam",
}
DARAJA = {"مقبول": ".maqbul", "قبيح": ".qabih", "خطأ": ".khata", "لا_حكم": ".laHukm"}


def qima(jadwal, k, mawdi):
    if k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        d, k, i = h["dakhil"], h["kharij"], h["id"]
        lam = "true" if d["lam_qasam"] is True else "false" if d["lam_qasam"] is False else None
        if lam is None:
            raise SystemExit(f"lam_qasam ليس منطقيًّا في {i}")
        shir = "none" if k["shir"] == "غير_مسؤول" else "some " + qima(DARAJA, k["shir"], i)
        sutur.append(
            f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, "
            f"⟨{nass_lean(d['adat'])}, {qima(TARTIB, d['tartib'], i)}, {lam}, "
            f"{qima(SHART, d['shart'], i)}, {qima(JAWAB, d['jawab'], i)}⟩, "
            f"{qima(DARAJA, k['kalam'], i)}, {shir}⟩"
        )
    ras = (
        "/-\n"
        "# حالاتُ ضابط «هذا باب الجزاء» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/jaza/cases.json` بـ `python3 -I scripts/bina_dawabit_jaza.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلّ من الباب وحده قبل الشفرة (`tahaqquq/dawabit/jaza/tajmid.json`). والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.BabJaza\n\n"
        "namespace Jisr\nnamespace BabJaza\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum\n  deriving DecidableEq, Repr\n\n"
        "structure Hala where\n  ism : String\n  fia : Fia\n  jumla : Jumla\n  kalam : Daraja\n"
        "  /-- `none`: «غير_مسؤول». -/\n  shir : Option Daraja\n  deriving DecidableEq, Repr\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend BabJaza\nend Jisr\n"
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
