"""يولّد Jisr/AbniyaDawabit.lean من حالات ضابط أبنية اسمَي الفاعل والمفعول المجمَّدة (tahaqquq/dawabit/abniya/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_abniya.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_abniya.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "abniya" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "AbniyaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
BINA = {"فعل_مفتوح_العين": ".fataha", "فعل_مكسور_العين": ".kasra", "فعل_مضموم_العين": ".damma", "غير_ثلاثي": ".ghayrThulathi"}
TAADDI = {"متعد": ".mutaaddi", "لازم": ".lazim"}
MATLUB = {"اسم_فاعل": ".fail", "اسم_مفعول": ".mafool"}
SIGHA = {"فاعل": ".faail", "فعل_مكسور_العين": ".faiil_k", "أفعل": ".afal", "فعلان": ".falan", "فعل_ساكن_العين": ".fal_s",
         "فعيل": ".faiil", "فعل_مفتوح_العين": ".faal_f", "مفعول": ".mafuul", "مضارع_بميم_مكسور": ".mudariMaksur",
         "مضارع_بميم_مفتوح": ".mudariMaftuh"}
HUKM = {"مقبول": ".maqbul", "خطأ": ".khata", "لا_حكم": ".laHukm"}
DARAJA = {"قياس": ".qiyas", "أولى": ".awla", "قليل": ".qalil", "نقل": ".naql", "بلا_درجة": ".bila"}
HUQUL = ["fil", "taaddi", "matlub", "sigha"]


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
        if sorted(d) != sorted(HUQUL):
            raise SystemExit(f"حقولُ dakhil غيرُ حقول المواصفة في {i}")
        dakhil = (f"⟨{qima(BINA, d['fil'], i)}, {qima(TAADDI, d['taaddi'], i)}, {qima(MATLUB, d['matlub'], i)}, "
                  f"{qima(SIGHA, d['sigha'], i)}⟩")
        z = h.get("zawj")
        zawj = "none" if z is None else f"some {nass_lean(z)}"
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {qaima(HUKM, h['hukm'], i, 'hukm')}, "
                     f"{qaima(DARAJA, h['daraja'], i, 'daraja')}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط أبنية اسمَي الفاعل والمفعول المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/abniya/cases.json` بـ `python3 -I scripts/bina_dawabit_abniya.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/abniya/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/abniya/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.AbniyaDabit\n\n"
        "namespace Jisr\nnamespace Abniya\nnamespace Dawabit\n\n"
        "open Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend Abniya\nend Jisr\n"
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
