"""يولّد Jisr/TawlidDawabit.lean من حالات ضابط «نواة التوليد» المجمَّدة (tahaqquq/dawabit/nawat_tawlid/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والمخرجُ يطابقه tahaqquq/test_tawlid.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_tawlid.py [--check]
  بلا --check يكتب الملفّ؛ ومع --check يقارن ويخرج 1 إن اختلف.
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "nawat_tawlid" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "TawlidDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "صورة": ".sura", "غموض": ".ghumud"}
JADHR_ = {"ك-س-ر": '"ك-س-ر"', "ع-ل-م": '"ع-ل-م"', "غائب": '"غائب"'}
AMIL = {"الفاعلية": ".failiyya", "المفعولية": ".mafuliyya", "السببية": ".sababiyya", "المطاوعة": ".mutawaa",
        "الزمان_والمكان": ".zamanMakan", "الآلة": ".ala", "المبالغة": ".mubalagha"}
JINS = {"إنسان": "some .insan", "حيوان": "some .hayawan", "نبات": "some .nabat", "جماد": "some .jamad", "غائب": "none"}
SHART = {"الحياة": ".hayat", "العقل": ".aql", "الإدراك": ".idrak", "حركة": ".haraka", "قوة_مؤثرة": ".quwwaMuaththira",
         "المادية": ".maddiyya", "التماسك_الجزئي": ".tamasukJuzi", "القابلية_للتصور": ".qabiliyyaTasawwur",
         "الصلابة_النسبية": ".salabaNisbiyya", "التحيز_المكاني_أو_الزماني": ".tahayyuz"}
QAYD = {"صلب": "some (some .sulb)", "لا": "some none", "لا_حكم": "none"}
HUKM = {"مرخَّص": ".murakhkhas", "لا_حكم": ".laHukm", "ممتنع": ".mumtani", "لا_نواة": ".laNawat", "لا_جنس": ".laJins"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def sigha(v, mawdi):
    if v == "لا_حكم":
        return "none"
    return "some " + nass_lean(v)


def mawruth(v, mawdi):
    if not isinstance(v, list):
        raise SystemExit(f"الموروث ليس قائمةً في {mawdi}")
    return "[" + ", ".join(qima(SHART, x, mawdi) for x in v) + "]"


def ahkam(v, mawdi):
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(HUKM, x, mawdi) for x in v) + "]"
    return "[" + qima(HUKM, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    sutur = []
    for h in halat:
        i, d, k = h["id"], h["dakhil"], h["kharij"]
        sutur.append(
            f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {qima(JADHR_, d['jadhr'], i)}, {qima(AMIL, d['amil'], i)}, "
            f"{qima(JINS, d['jins'], i)}, {sigha(k['sigha'], i)}, {mawruth(k['mawruth'], i)}, {qima(QAYD, k['qayd'], i)}, "
            f"{ahkam(k['hukm'], i)}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «نواة التوليد» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/nawat_tawlid/cases.json` بـ `python3 -I scripts/bina_dawabit_tawlid.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدر قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/nawat_tawlid/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/nawat_tawlid/tajmid.json`. والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.TawlidDabit\n\n"
        "namespace Jisr\nnamespace Tawlid\nnamespace Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dabit\nend Tawlid\nend Jisr\n"
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
