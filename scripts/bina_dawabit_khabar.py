"""يولّد Jisr/KhabarDawabit.lean من حالات ضابط الخبر المجمَّدة (tahaqquq/dawabit/khabar/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_khabar.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_khabar.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "khabar" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "KhabarDawabit.lean"

LA = {"لا_ينطبق": ".la"}
FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
BINYA = {"مبتدأ_وخبر": ".mubtadaKhabar", "وصف_ومرفوعه": ".wasfMarfu"}
JINS = {"ذات": ".dhat", "معنى": ".maana", **LA}
KHABAR = {"مفرد_جامد": ".mufradJamid", "مفرد_مشتق": ".mufradMushtaq", "جملة_اسمية": ".jumlaIsmiyya", "جملة_فعلية": ".jumlaFiliyya",
          "ظرف_مكان": ".zarfMakan", "ظرف_زمان": ".zarfZaman", "جار_مجرور": ".jarMajrur", **LA}
RABIT = {"ضمير": ".damir", "اسم_اشارة": ".ishara", "اعادة_المبتدأ": ".iada", "عموم": ".umum", "هي_المبتدأ": ".hiya",
         "لا_رابط": ".laRabit", **LA}
MARFU = {"مستكن": ".mustakin", "بارز": ".bariz", "ظاهر": ".zahir", "لا_شيء": ".laShay", **LA}
JARYAN = {"لصاحبه": ".lisahibihi", "لغيره": ".lighayrihi", **LA}
IFADA = {"مفيد": ".mufid", "غير_مفيد": ".ghayrMufid", **LA}
ITIMAD = {"استفهام": ".istifham", "نفي": ".nafy", "لا_اعتماد": ".laItimad", **LA}
ADAD = {"مفرد": ".mufrad", "مثنى": ".muthanna", "جمع": ".jam", **LA}
TAHLIL = {"فاعل_اغنى": ".failAghna", "خبر_مقدم": ".khabarMuqaddam", **LA}
HUKM = {"مقبول": ".maqbul", "خطأ": ".khata", "لا_حكم": ".laHukm"}
DARAJA = {"قليل": ".qalil", "بتأويل": ".bitawil", "بلا_درجة": ".bila"}
HUQUL = [("binya", BINYA), ("jins", JINS), ("khabar", KHABAR), ("rabit", RABIT), ("marfu", MARFU), ("jaryan", JARYAN),
         ("ifada", IFADA), ("itimad", ITIMAD), ("wasf_adad", ADAD), ("marfu_adad", ADAD), ("tahlil", TAHLIL)]


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def qaima(jadwal, h, i, ism):
    if isinstance(h, list):
        if len(h) < 2:
            raise SystemExit(f"{ism} قائمةٌ دون بديلين في {i}")
        return "[" + ", ".join(qima(jadwal, x, i) for x in h) + "]"
    return "[" + qima(jadwal, h, i) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d = h["id"], h["dakhil"]
        if sorted(d) != sorted(k for k, _ in HUQUL):
            raise SystemExit(f"حقولُ dakhil غيرُ حقول المواصفة في {i}")
        dakhil = "⟨" + ", ".join(qima(j, d[k], i) for k, j in HUQUL) + "⟩"
        z = h.get("zawj")
        zawj = "none" if z is None else f"some {nass_lean(z)}"
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {qaima(HUKM, h['hukm'], i, 'hukm')}, "
                     f"{qaima(DARAJA, h['daraja'], i, 'daraja')}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط الخبر المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/khabar/cases.json` بـ `python3 -I scripts/bina_dawabit_khabar.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/khabar/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/khabar/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.KhabarDabit\n\n"
        "namespace Jisr\nnamespace Khabar\nnamespace Dawabit\n\n"
        "open Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend Khabar\nend Jisr\n"
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
