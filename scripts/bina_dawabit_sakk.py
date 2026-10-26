"""يولّد Jisr/SakkJumlaDawabit.lean من حالات ضابط صكّ الجملة المجمَّدة (tahaqquq/dawabit/sakk/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه.
والجداولُ قيمُ المواصفة (tahaqquq/dawabit/sakk/wasf.md) بأعيانها، كُتبت قبل قراءة الحالات.
والمخرجُ يطابقه tahaqquq/test_sakk.py بايتًا.

التشغيل: python3 -I scripts/bina_dawabit_sakk.py [--check]
  بلا --check يكتب الملفّ؛ ومع --check يقارن ويخرج 1 إن اختلف.
"""
import hashlib
import json
import pathlib
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "sakk" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "SakkJumlaDawabit.lean"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
# القوّة
ADAT = {"لا_شيء": ".laShay", "لم": ".lam", "إن": ".in_"}
QAWL = {"لا_قول": ".laQawl", "قال": ".qala", "تقول_مستفهما": ".taqulMustafhim"}
MABAAD = {"لا_قول": ".laQawl", "إن_مكسورة": ".innaMaksura", "أن_مفتوحة": ".annaMaftuha", "مرفوع": ".marfu",
          "منصوب": ".mansub", "جملة_فعلية": ".jumlaFiliyya", "غير_معلن": ".ghayrMuallan"}
LUGHA = {"عامة": ".amma", "بنو_سليم": ".banuSulaym", "غير_معلن": ".ghayrMuallan"}
AWWAL = {"إثبات": ".ithbat", "نفي": ".nafy", "تعليق": ".taliq", "إنشاء": ".insha", "لا_حكم": ".laHukm"}
THANI = {"إثبات": ".ithbat", "نفي": ".nafy", "تعليق": ".taliq", "حكاية": ".hikaya", "ظن": ".zann",
         "لا_ثاني": ".laThani", "لا_حكم": ".laHukm"}
# السبب
DALL = {"مصدر_منصوب": ".masdarMansub", "لام_جارة": ".lamJarra", "لام_ناصبة": ".lamNasiba", "كي": ".kay",
        "حتى_منصوب": ".hattaMansub", "حتى_مرفوع": ".hattaMarfu", "فاء_منصوب": ".faMansub", "فاء_مرفوع": ".faMarfu",
        "أن_بلا_لام": ".anBilaLam", "لما": ".lamma", "بعد": ".baad", "قبل": ".qabl", "غير_ذلك": ".ghayrDhalik"}
SHURUT = {"مستوفاة": ".mustawfat", "فقد_الفاعل": ".faqdFail", "فقد_الوقت": ".faqdWaqt", "غير_معلن": ".ghayrMuallan",
          "لا_ينطبق": ".laYantabiq"}
ADAA = {"الأول_سبب_الثاني": ".sabab", "الأول_ليس_سببا": ".laysaSabab", "غير_معلن": ".ghayrMuallan",
        "لا_ينطبق": ".laYantabiq"}
SABAB = {"علة": ".illa", "سببية": ".sababiyya", "غير_مذكور": ".ghayrMadhkur", "لا_حكم": ".laHukm"}
# المرجع
LAFZ = {"أنا": ".ana", "أنت": ".anta", "هو": ".huwa", "هذا": ".hadha", "ذاك": ".dhaka"}
SIYAQ = {"متكلم_معين": ".mutakallimMuayyan", "مخاطب_معين": ".mukhatabMuayyan", "مفسر_واحد": ".mufassirWahid",
         "مفسران": ".mufassiran", "مشار_اليه_واحد": ".musharWahid", "مشار_اليهما": ".musharIthnan", "لا_شيء": ".laShay"}
MARJI = {"معين": ".muayyan", "محتمل": ".muhtamal", "لا_حكم": ".laHukm"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def qaima(jadwal, v, mawdi):
    """قيمةٌ واحدة ← قائمةٌ منها؛ أو قائمةُ بديلين (غموض) ← قائمةُ منشئات."""
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(jadwal, x, mawdi) for x in v) + "]"
    return "[" + qima(jadwal, v, mawdi) + "]"


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    q, s, m = [], [], []
    for h in halat:
        i, d, k = h["id"], h["dakhil"], h["kharij"]
        f = qima(FIA, h["fia"], i)
        if h["naw"] == "قوة":
            q.append(
                f"  ⟨{nass_lean(i)}, {f}, ⟨{qima(ADAT, d['adat'], i)}, {qima(QAWL, d['qawl'], i)}, "
                f"{qima(MABAAD, d['ma_baad_alqawl'], i)}, {qima(LUGHA, d['lugha'], i)}⟩, "
                f"{qaima(AWWAL, k['awwal'], i)}, {qaima(THANI, k['thani'], i)}⟩")
        elif h["naw"] == "سبب":
            s.append(
                f"  ⟨{nass_lean(i)}, {f}, ⟨{qima(DALL, d['dall'], i)}, {qima(SHURUT, d['shurut'], i)}, "
                f"{qima(ADAA, d['adaa'], i)}⟩, {qaima(SABAB, k['sabab'], i)}⟩")
        elif h["naw"] == "مرجع":
            m.append(
                f"  ⟨{nass_lean(i)}, {f}, ⟨{qima(LAFZ, d['lafz'], i)}, {qima(SIYAQ, d['siyaq'], i)}⟩, "
                f"{qaima(MARJI, k['marji'], i)}⟩")
        else:
            raise SystemExit(f"نوعٌ لا يُعرف «{h['naw']}» في {i}")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «صكّ الجملة» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/sakk/cases.json` بـ `python3 -I scripts/bina_dawabit_sakk.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والنطاق قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/sakk/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/sakk/tajmid.json`. والمثالُ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.SakkJumla\n\n"
        "namespace Jisr\nnamespace SakkJumla\nnamespace Dawabit\n\n"
        "inductive Fia\n  | mujib | hadd | kharij | umum | ghumud\n  deriving DecidableEq, Repr\n\n"
        "structure HalaQ where\n  ism : String\n  fia : Fia\n  dakhil : DakhilQ\n"
        "  /-- القيمةُ وحدها، أو البديلان في الغموض. -/\n  awwal : List Quwwa\n  thani : List Quwwa\n"
        "  deriving DecidableEq, Repr\n\n"
        "structure HalaS where\n  ism : String\n  fia : Fia\n  dakhil : DakhilS\n  sabab : List Sabab\n"
        "  deriving DecidableEq, Repr\n\n"
        "structure HalaM where\n  ism : String\n  fia : Fia\n  dakhil : DakhilM\n  marji : List Marji\n"
        "  deriving DecidableEq, Repr\n\n"
    )
    jism = ("def halatQ : List HalaQ := [\n" + ",\n".join(q) + "]\n\n"
            "def halatS : List HalaS := [\n" + ",\n".join(s) + "]\n\n"
            "def halatM : List HalaM := [\n" + ",\n".join(m) + "]\n\n")
    khatm = "end Dawabit\nend SakkJumla\nend Jisr\n"
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
