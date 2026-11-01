"""يولّد Jisr/TahlilDawabit.lean من حالات ضابط «قراءة الجملة بالعوامل» المجمَّدة (tahaqquq/dawabit/tahlil/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه. والجملةُ تُقرأ خلايا بالقارئ
نفسِه (`qari --khalaya`، `tahlil` في الوصل)، لا بقراءةٍ ثانية هنا؛ وما رفضه القارئ يُكتب `none` ويُعدّ في `Dabit.rafd`.
والمخرجُ يطابقه tahaqquq/test_tahlil.py بايتًا.

التشغيل (بعد `lake build qari`): python3 -I scripts/bina_dawabit_tahlil.py [--check]
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "tahlil" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "TahlilDawabit.lean"
QARI = JADHR / ".lake" / "build" / "bin" / "qari"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
HUKM = {"مقبول": ".murakhkhas", "خطأ": ".mumtani", "لا_حكم": ".laHukm"}
DAWR = {"رابط": ".rabit", "جازم": ".jazim", "ناصب": ".nasib", "نافية": ".nafiya", "فعل": ".fil", "فاعل": ".fail",
        "مفعول_به": ".maful", "مبتدأ": ".mubtada", "خبر": ".khabar", "حرف_جر": ".harfJarr", "مجرور": ".majrur",
        "مضاف_إليه": ".mudafIlayh"}


def qima(jadwal, k, mawdi):
    if not isinstance(k, str) or k not in jadwal:
        raise SystemExit(f"قيمةٌ لا منشئَ لها: «{k}» في {mawdi}")
    return jadwal[k]


def nass_lean(s):
    if not isinstance(s, str) or '"' in s or "\\" in s or "\n" in s:
        raise SystemExit(f"نصٌّ لا يُنقل حرفيًّا إلى سلسلة Lean: «{s}»")
    return '"' + s + '"'


def ahkam(v, mawdi):
    if isinstance(v, list):
        if len(v) < 2:
            raise SystemExit(f"قائمةُ بديلين أقلُّ من اثنين في {mawdi}")
        return "[" + ", ".join(qima(HUKM, x, mawdi) for x in v) + "]"
    return "[" + qima(HUKM, v, mawdi) + "]"


def adwar(v, mawdi):
    if not isinstance(v, list) or not v:
        raise SystemExit(f"أدوارٌ ليست قائمة في {mawdi}")
    utur = v if isinstance(v[0], list) else [v]
    if isinstance(v[0], list) and len(v) < 2:
        raise SystemExit(f"قائمةُ قراءتين أقلُّ من اثنين في {mawdi}")
    return "[" + ", ".join("[" + ", ".join(qima(DAWR, d, mawdi) for d in u) + "]" for u in utur) + "]"


def khalaya(halat):
    """خلايا الجمل من القارئ: {المعرّف: قائمةُ كلماتٍ بلغة Lean أو None}."""
    if not QARI.exists():
        raise SystemExit(f"القارئ غيرُ مبنيّ: {QARI.relative_to(JADHR)} (lake build qari)")
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "jumal.tsv"
        p.write_text("".join(f"{h['id']}\t{h['nass']}\n" for h in halat), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(p)], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("القارئ خرج بغير صفر: " + r.stderr[-400:])
    natija = {}
    for satr in r.stdout.splitlines():
        ajza = satr.split("\t")
        if len(ajza) == 3 and ajza[1] == "QABUL":
            kalimat = []
            for w in ajza[2].split("|"):
                c, wasl, al = w.split(";")
                kalimat.append(f"⟨[{', '.join(c.split(','))}], {'true' if wasl == '1' else 'false'}, "
                               f"{'true' if al == '1' else 'false'}⟩")
            natija[ajza[0]] = "some [" + ", ".join(kalimat) + "]"
        elif len(ajza) == 3 and ajza[1] == "RAFD":
            natija[ajza[0]] = None
        else:
            raise SystemExit(f"سطرٌ من القارئ لا يُفهم: «{satr}»")
    if sorted(natija) != sorted(h["id"] for h in halat):
        raise SystemExit("القارئ لم يُخرج سطرًا لكلّ حالة")
    return natija


def wallid(bayt):
    halat = json.loads(bayt.decode("utf-8"))
    basma = hashlib.sha256(bayt).hexdigest()
    kh = khalaya(halat)
    sutur = []
    for h in halat:
        i = h["id"]
        k = kh[i] if kh[i] is not None else "none"
        zawj = "none" if h.get("zawj") is None else "some " + nass_lean(h["zawj"])
        sutur.append(f"  -- {i} «{h['nass']}»\n"
                     f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {k},\n"
                     f"   {ahkam(h['hukm'], i)}, {adwar(h['adwar'], i)}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «قراءة الجملة بالعوامل» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/tahlil/cases.json` بـ `python3 -I scripts/bina_dawabit_tahlil.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والقطر قبل الشفرة، وفي سياقه ما حُقن آليًّا (`tahaqquq/dawabit/tahlil/taalif.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/tahlil/tajmid.json`. والكلماتُ خلايا كما قرأها القارئ (`qari --khalaya`)، "
        "و`none` ما رفضه؛ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.TahlilDabit\n\n"
        "namespace Jisr\nnamespace Tahlil\nnamespace Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Dabit\nend Tahlil\nend Jisr\n"
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
