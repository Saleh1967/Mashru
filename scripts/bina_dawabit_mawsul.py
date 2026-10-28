"""يولّد Jisr/MawsulDawabit.lean من حالات ضابط الموصول المجمَّدة (tahaqquq/dawabit/mawsul/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_mawsul.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_mawsul.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "mawsul" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "MawsulDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
LAFZ = {"الذي": ".alladhi", "التي": ".allati", "اللذان": ".alladhani", "اللتان": ".allatani", "اللذين": ".alladhayni",
        "اللتين": ".allatayni", "اللذيان": ".alladhiyani", "اللتيان": ".allatiyani", "الذين": ".alladhina", "اللذون": ".alladhuna",
        "الألى": ".alula", "اللائي": ".allai", "اللاتي": ".allati_j", "اللات": ".allat", "اللاء": ".allaa", "من": ".man", "ما": ".ma",
        "أي": ".ayy", "أل": ".al", "ذو": ".dhu", "ذات": ".dhat", "ذوات": ".dhawat", "ذا": ".dha"}
SIMA = {"مفرد_مذكر": ".mufradMudhakkar", "مفرد_مؤنث": ".mufradMuannath", "مثنى_مذكر": ".muthannaMudhakkar",
        "مثنى_مؤنث": ".muthannaMuannath", "جمع_مذكر": ".jamMudhakkar", "جمع_مؤنث": ".jamMuannath"}
AIDSIMA = {**{k: "some " + v for k, v in SIMA.items()}, "لا_عائد": "none"}
MAWDI = {"رفع": ".raf", "نصب": ".nasb", "جر": ".jarr"}
LUGHA = {"غير_مذكورة": ".ghayrMadhkura", "طيئ": ".tayyi"}
QABL = {"ما_الاستفهامية": ".maIstifham", "من_الاستفهامية": ".manIstifham", "غيرهما": ".ghayruhuma"}
SILA = {"جملة_خبرية": ".jumlaKhabariyya", "جملة_إنشائية": ".jumlaInshaiyya", "ظرف_تام": ".zarfTamm", "ظرف_ناقص": ".zarfNaqis",
        "جار_مجرور_تام": ".jarrTamm", "جار_مجرور_ناقص": ".jarrNaqis", "وصف_صريح": ".wasfSarih", "اسم_تفضيل": ".ismTafdil",
        "فعل_معرب": ".filMurab", "لا_صلة": ".laSila"}
AID = {"ظاهر": ".zahir", "مستتر": ".mustatir", "محذوف": ".mahdhuf", "لا_عائد": ".laAid"}
HUKM = {"مقبول": ".maqbul", "خطأ": ".khata", "لا_حكم": ".laHukm"}
DARAJA = {"قليل": ".qalil", "نزر": ".nazr", "لغة": ".lugha", "بلا_درجة": ".bila"}
HUQUL = ["mawsul", "marji", "mawdi", "tashdid", "lugha", "qabl", "mulgha", "sila", "aid", "aid_sima"]


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
        if sorted(d) != sorted(HUQUL):
            raise SystemExit(f"حقولُ dakhil غيرُ حقول المواصفة في {i}")
        dakhil = (f"⟨{qima(LAFZ, d['mawsul'], i)}, {qima(SIMA, d['marji'], i)}, {qima(MAWDI, d['mawdi'], i)}, "
                  f"{mantiqi(d['tashdid'], i)}, {qima(LUGHA, d['lugha'], i)}, {qima(QABL, d['qabl'], i)}, {mantiqi(d['mulgha'], i)}, "
                  f"{qima(SILA, d['sila'], i)}, {qima(AID, d['aid'], i)}, {qima(AIDSIMA, d['aid_sima'], i)}⟩")
        z = h.get("zawj")
        zawj = "none" if z is None else f"some {nass_lean(z)}"
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {qaima(HUKM, h['hukm'], i, 'hukm')}, "
                     f"{qaima(DARAJA, h['daraja'], i, 'daraja')}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط الموصول المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/mawsul/cases.json` بـ `python3 -I scripts/bina_dawabit_mawsul.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/mawsul/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/mawsul/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.MawsulDabit\n\n"
        "namespace Jisr\nnamespace Mawsul\nnamespace Dawabit\n\n"
        "open Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend Mawsul\nend Jisr\n"
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
