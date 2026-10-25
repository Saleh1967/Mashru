"""يولّد Dal/WaqfSibawayhiDawabit.lean من حالات ضابط الوقف المجمَّدة (tahaqquq/dawabit/waqf/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_waqf.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_waqf.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "waqf" / "cases.json"
MAKHRAJ = JADHR / "Dal" / "WaqfSibawayhiDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
AKHIR = {"حرف_صحيح": ".sahih", "هاء_تأنيث": ".haTaanith", "تاء_جمع": ".taJam", "تاء_ملحقة": ".taMulhaqa",
         "ياء_قبلها_كسرة": ".yaBaadKasra"}
TANWIN = {"منون": "true", "غير_منون": "false"}
QABL = {"متحرك": "true", "ساكن": "false"}
HARAKA = {"رفع_أو_ضم": ".raf", "نصب_أو_فتح": ".nasb", "جر_أو_كسر": ".jarr"}
WAJH = {"ألف": ".alif", "واو_أو_ياء": ".wawAwYa", "إسكان": ".iskan", "إشمام": ".ishmam", "روم": ".rawm", "تضعيف": ".tadif",
        "هاء": ".ha", "تاء": ".ta", "حذف_الياء": ".hadhfYa", "إثبات_الياء": ".ithbatYa"}
DARAJA = {"مقبول": ".maqbul", "لغة": ".lugha", "خطأ": ".khata", "لا_حكم": ".laHukm"}


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
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, ⟨{qima(AKHIR, d['akhir'], i)}, {qima(TANWIN, d['tanwin'], i)}, "
                     f"{qima(QABL, d['qabl_akhir'], i)}, {qima(HARAKA, d['haraka'], i)}, {qima(WAJH, d['wajh'], i)}⟩, "
                     f"{darajat(k['kalam'], i)}, {shir}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط الوقف على أواخر الكلم المتحرّكة في الوصل المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/waqf/cases.json` بـ `python3 -I scripts/bina_dawabit_waqf.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلّ من البابين وحدهما قبل الشفرة (`tahaqquq/dawabit/waqf/tajmid.json`). والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Dal.WaqfSibawayhi\n\n"
        "namespace Dal\nnamespace WaqfSibawayhi\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure Hala where\n  ism : String\n  fia : Fia\n  kalima : Kalima\n"
        "  /-- القيمةُ وحدها، أو البديلان في الغموض. -/\n  kalam : List Daraja\n"
        "  /-- `none`: «غير_مسؤول». -/\n  shir : Option (List Daraja)\n  deriving DecidableEq, Repr\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend WaqfSibawayhi\nend Dal\n"
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
