"""يولّد Jisr/BaqiJazaDawabit.lean من حالات ضابط بقيّة أبواب الجزاء المجمَّدة (tahaqquq/dawabit/jaza2/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_jaza2.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_jaza2.py [--check]
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "jaza2" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "BaqiJazaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
QABL = {"لا_شيء": ".laShay", "ناسخ": ".nasikh", "ناسخ_مشغول": ".nasikhMashghul", "حرف_ابتداء": ".harfIbtida",
        "حرف_ابتداء_مفصول": ".harfIbtidaMafsul", "إذا_فجائية": ".idhaFujaiyya", "إذا_مضمر_بعدها": ".idhaMudmar",
        "لا": ".la", "لكن": ".lakin", "حرف_جر": ".harfJarr", "مضاف": ".mudaf", "همزة": ".hamza", "قسم": ".qasam",
        "مبتدأ_ثم_قسم": ".mubtadaQasam"}
ADAT = {"من": ".man", "ما": ".ma", "أي": ".ayy", "مهما": ".mahma", "متى": ".mata", "حيثما": ".haythuma", "أين": ".ayna",
        "أنى": ".anna", "إن": ".inn", "كلما": ".kullama", "الذي": ".alladhi", "كل": ".kull", "أن": ".an", "أما": ".amma",
        "طلب_أمر": ".talabAmr", "طلب_نهي": ".talabNahy", "طلب_استفهام": ".talabIstifham", "طلب_تمن": ".talabTamanni",
        "طلب_عرض": ".talabArd", "معنى_أمر": ".manaAmr", "خبر_واجب": ".khabarWajib"}
SHART = {"مضارع": ".mudari", "ماض": ".madi", "لا_ينطبق": ".laYantabiq"}
FIL = {"فعل_الشرط": ".shart", "الجواب": ".jawab", "بين_المجزومين": ".baynMajzumayn", "بعد_الجواب": ".baadJawab",
       "جواب_الطلب": ".jawabTalab"}
RABIT = {"بلا": ".bila", "فاء": ".fa", "واو": ".waw", "ثم": ".thumma", "أو": ".aw"}
SURA = {"مجزوم": ".majzum", "مرفوع": ".marfu", "منصوب": ".mansub", "ماض": ".madi", "منفي_بلم": ".manfiLam",
        "منفي_بلا_مجزوم": ".manfiLaMajzum"}
MANA = {"جزاء": ".jaza", "صلة": ".sila", "حال": ".hal", "بدل": ".badal", "شركة": ".shirka", "ابتداء": ".ibtida",
        "غير_معلن": ".ghayrMuallan"}
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
        if k["kalam"] == "غير_مسؤول":
            raise SystemExit(f"«غير_مسؤول» في الكلام في {i}")
        shir = "none" if k["shir"] == "غير_مسؤول" else "some " + darajat(k["shir"], i)
        dakhil = (f"⟨{qima(QABL, d['qabl'], i)}, {qima(ADAT, d['adat'], i)}, {qima(SHART, d['shart'], i)}, "
                  f"{qima(FIL, d['fil'], i)}, {qima(RABIT, d['rabit'], i)}, {qima(SURA, d['sura'], i)}, "
                  f"{qima(MANA, d['mana'], i)}⟩")
        sutur.append(f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {dakhil}, {darajat(k['kalam'], i)}, {shir}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط بقيّة أبواب الجزاء المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/jaza2/cases.json` بـ `python3 -I scripts/bina_dawabit_jaza2.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ من المواصفة والنطاق قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/jaza2/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/jaza2/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.BaqiJaza\n\n"
        "namespace Jisr\nnamespace BaqiJaza\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure Hala where\n  ism : String\n  fia : Fia\n  dakhil : Dakhil\n"
        "  /-- القيمةُ وحدها، أو البديلان في الغموض. -/\n  kalam : List Daraja\n"
        "  /-- `none`: «غير_مسؤول». -/\n  shir : Option (List Daraja)\n  deriving DecidableEq, Repr\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dawabit\nend BaqiJaza\nend Jisr\n"
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
