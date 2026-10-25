"""يولّد Jisr/MajariKalimDawabit.lean من حالات ضابط مجاري أواخر الكلم المجمَّدة (tahaqquq/dawabit/majari/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_majari.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_majari.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "majari" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "MajariKalimDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
SINF = {"اسم_متمكن": ".ismMutamakkin", "اسم_لا_ينصرف": ".ismLaYansarif", "اسم_لا_ينصرف_معرف": ".ismLaYansarifMuarraf",
        "مثنى": ".muthanna", "جمع_مذكر": ".jamMudhakkar", "جمع_مؤنث": ".jamMuannath", "مضارع": ".mudari",
        "مضارع_ساكن_الآخر": ".mudariSakin", "مضارع_اثنين": ".mudariIthnayn", "مضارع_جمع": ".mudariJam",
        "مضارع_مخاطبة": ".mudariMukhataba", "مضارع_نسوة": ".mudariNiswa", "ماض": ".madi", "أمر": ".amr",
        "غير_متمكن": ".ghayrMutamakkin"}
MAWDI = {"رفع": ".raf", "نصب": ".nasb", "جر": ".jarr", "جزم": ".jazm", "بلا_عامل": ".bilaAmil"}
ALAMA = {"ضمة": ".damma", "فتحة": ".fatha", "كسرة": ".kasra", "سكون": ".sukun", "ألف": ".alif", "واو": ".waw",
         "ياء": ".ya", "ثبات_النون": ".thubutNun", "حذف_النون": ".hadhfNun", "حذف_الآخر": ".hadhfAkhir"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def jawab(k, i):
    a = k["alama"]
    if a == "لا_يكون":
        return ".laYakun"
    if a == "لا_حكم":
        return ".laHukm"
    if not isinstance(a, list) or not a:
        raise SystemExit(f"alama ليست قائمةً ولا «لا_يكون» ولا «لا_حكم» في {i}")
    b = k.get("bina")
    if not isinstance(b, bool):
        raise SystemExit(f"bina ليست منطقيّةً في {i}")
    return f".alamat [{', '.join(qima(ALAMA, x, i) for x in a)}] {'true' if b else 'false'}"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d, k = h["id"], h["dakhil"], h["kharij"]
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, ⟨{qima(SINF, d['sinf'], i)}, {nass_lean(d['lafz'])}, "
                     f"{qima(MAWDI, d['mawdi'], i)}⟩, {jawab(k, i)}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «هذا باب مجارى أواخر الكلم من العربية» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/majari/cases.json` بـ `python3 -I scripts/bina_dawabit_majari.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والباب قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/majari/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/majari/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.MajariKalim\n\n"
        "namespace Jisr\nnamespace MajariKalim\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure Hala where\n  ism : String\n  fia : Fia\n  kalima : Kalima\n  mutawaqqa : Jawab\n  deriving DecidableEq, Repr\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend MajariKalim\nend Jisr\n"
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
