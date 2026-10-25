"""يولّد Jisr/NafyFilDawabit.lean من حالات ضابط نفي الفعل المجمَّدة (tahaqquq/dawabit/nafy/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_nafy.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_nafy.py [--check]
  بلا --check يكتب الملفّ؛ ومع --check يقارن ويخرج 1 إن اختلف.
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "nafy" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "NafyFilDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
JIHA = {"نفي": ".nafy", "إثبات": ".ithbat"}
HAL = {"حال": ".hal", "غير_واقع": ".ghayrWaqi", "غير_معلن": ".ghayrMuallan"}
SIYAQ = {"قسم": ".qasam", "جواب_هل": ".jawabHal", "غير_معلن": ".ghayrMuallan"}
YALI = {"فعل": ".fil", "اسم_ثم_فعل": ".ismThummaFil", "اسم": ".ism"}
DARAJA = {"مقبول": ".maqbul", "مرجوح": ".marjuh", "قبيح": ".qabih", "خطأ": ".khata", "لا_حكم": ".laHukm"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def darajat(v, mawdi):
    """قيمةٌ واحدة أو قائمةُ بديلين (غموض) ← قائمةُ منشئات."""
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(DARAJA, x, mawdi) for x in v) + "]"
    return "[" + qima(DARAJA, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    nafy, wali = [], []
    for h in halat:
        i, d, k = h["id"], h["dakhil"], h["kharij"]
        if h["naw"] == "نفي":
            s = k["suwar"]
            if s == "لا_حكم":
                suwar = "none"
            elif isinstance(s, list) and s:
                suwar = "some [" + ", ".join(nass_lean(x) for x in s) + "]"
            else:
                raise SystemExit(f"suwar ليست قائمةً ولا «لا_حكم» في {i}")
            nafy.append(
                f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, "
                f"⟨{qima(JIHA, d['jiha'], i)}, {nass_lean(d['sura'])}, {qima(HAL, d['hal'], i)}, "
                f"{qima(SIYAQ, d['siyaq'], i)}⟩, {suwar}⟩")
        elif h["naw"] == "ولي":
            shir = "none" if k["shir"] == "غير_مسؤول" else "some " + darajat(k["shir"], i)
            wali.append(
                f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {nass_lean(d['harf'])}, {qima(YALI, d['yali'], i)}, "
                f"{darajat(k['kalam'], i)}, {shir}⟩")
        else:
            raise SystemExit(f"نوعٌ لا يُعرف «{h['naw']}» في {i}")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «نفي الفعل» وحروفِ الفعل المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/nafy/cases.json` بـ `python3 -I scripts/bina_dawabit_nafy.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلّ من النطاق وحده قبل الشفرة (`tahaqquq/dawabit/nafy/tajmid.json`). والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.NafyFil\n\n"
        "namespace Jisr\nnamespace NafyFil\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure HalaNafy where\n  ism : String\n  fia : Fia\n  sual : Sual\n"
        "  /-- `none`: «لا_حكم». -/\n  suwar : Option (List String)\n  deriving DecidableEq, Repr\n\n"
        "structure HalaWali where\n  ism : String\n  fia : Fia\n  harf : String\n  yali : Yali\n"
        "  /-- القيمةُ وحدها، أو البديلان في الغموض. -/\n  kalam : List Daraja\n"
        "  /-- `none`: «غير_مسؤول». -/\n  shir : Option (List Daraja)\n  deriving DecidableEq, Repr\n\n"
    )
    jism = ("def halatNafy : List HalaNafy := [\n" + ",\n".join(nafy) + "]\n\n"
            "def halatWali : List HalaWali := [\n" + ",\n".join(wali) + "]\n\n")
    khatm = "end Dawabit\nend NafyFil\nend Jisr\n"
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
