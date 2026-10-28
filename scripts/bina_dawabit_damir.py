"""يولّد Jisr/DamirDawabit.lean من حالات ضابط الضمير المجمَّدة (tahaqquq/dawabit/damir/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_damir.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_damir.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "damir" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "DamirDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
AMIL = {"فعل_لواحد": ".filWahid", "فعل_لاثنين": ".filIthnayn", "ظن": ".zann", "كان": ".kana", "اسم": ".ism",
        "لا_عامل": ".laAmil"}
MAWQI = {"يلي_العامل": ".yali", "بعد_إلا": ".badIlla", "ابتداء": ".ibtida"}
RUTBA = {"متكلم": ".mutakallim", "مخاطب": ".mukhatab", "غائب": ".ghaib"}
QABL = {"متكلم": "some .mutakallim", "مخاطب": "some .mukhatab", "غائب": "some .ghaib", "لا_شيء": "none"}
SHAKL = {"متصل": ".muttasil", "منفصل": ".munfasil"}
HUKM = {"مقبول": ".maqbul", "خطأ": ".khata", "لا_حكم": ".laHukm"}
DARAJA = {"راجح": ".rajih", "مرجوح": ".marjuh", "سواء": ".sawa", "بلا_درجة": ".bila"}
HUQUL = ["amil", "mawqi", "qablahu", "rutba", "shakl", "darura"]


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
        dakhil = (f"⟨{qima(AMIL, d['amil'], i)}, {qima(MAWQI, d['mawqi'], i)}, {qima(QABL, d['qablahu'], i)}, "
                  f"{qima(RUTBA, d['rutba'], i)}, {qima(SHAKL, d['shakl'], i)}, {mantiqi(d['darura'], i)}⟩")
        z = h.get("zawj")
        zawj = "none" if z is None else f"some {nass_lean(z)}"
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {qaima(HUKM, h['hukm'], i, 'hukm')}, "
                     f"{qaima(DARAJA, h['daraja'], i, 'daraja')}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط الضمير المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/damir/cases.json` بـ `python3 -I scripts/bina_dawabit_damir.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/damir/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/damir/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.DamirDabit\n\n"
        "namespace Jisr\nnamespace Damir\nnamespace Dawabit\n\n"
        "open Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend Damir\nend Jisr\n"
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
