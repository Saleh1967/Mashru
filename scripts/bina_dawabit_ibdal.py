"""يولّد Jisr/IbdalAlfiyyaDawabit.lean من حالات ضابط «الإبدال: الواوُ والياءُ في الكلمة» المجمَّدة (tahaqquq/dawabit/ibdal/cases.json).

لا حكمَ هنا ولا تصحيح: كلُّ قيمةٍ تُنقل إلى منشئها في Lean بجدولٍ ثابت، وما لا منشئَ له يُرفض باسمه. والكلمةُ تُقرأ خلايا بالقارئ
نفسِه (`qari --khalaya`، في الوصل)، لا بقراءةٍ ثانية هنا؛ وما رفضه القارئ يُكتب `none` ويُعدّ في `Dabit.rafd`. وكلمةٌ يقرؤها القارئ
أكثرَ من كلمةٍ واحدة تُرفض هنا باسمها (المجالُ كلمةٌ واحدة). والمخرجُ يطابقه tahaqquq/test_ibdal.py بايتًا.

التشغيل (بعد `lake build qari`): python3 -I scripts/bina_dawabit_ibdal.py [--check]
"""
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
HALAT = JADHR / "tahaqquq" / "dawabit" / "ibdal" / "cases.json"
MAKHRAJ = JADHR / "Jisr" / "IbdalAlfiyyaDawabit.lean"
QARI = JADHR / ".lake" / "build" / "bin" / "qari"

FIA = {"موجب": ".mujib", "حد": ".hadd", "خارج": ".kharij", "عموم": ".umum", "غموض": ".ghumud"}
QIMA = {"ممنوع": ".mamnu", "غير_ممنوع": ".ghayrMamnu", "لا_حكم": ".laHukm"}


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
        return "[" + ", ".join(qima(QIMA, x, mawdi) for x in v) + "]"
    return "[" + qima(QIMA, v, mawdi) + "]"


def khalaya(halat):
    """خلايا الكلمات من القارئ: {المعرّف: كلمةٌ بلغة Lean أو None}."""
    if not QARI.exists():
        raise SystemExit(f"القارئ غيرُ مبنيّ: {QARI.relative_to(JADHR)} (lake build qari)")
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "kalimat.tsv"
        p.write_text("".join(f"{h['id']}\t{h['kalima']}\n" for h in halat), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(p)], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("القارئ خرج بغير صفر: " + r.stderr[-400:])
    natija = {}
    for satr in r.stdout.splitlines():
        ajza = satr.split("\t")
        if len(ajza) == 3 and ajza[1] == "QABUL":
            kalimat = ajza[2].split("|")
            if len(kalimat) != 1:
                raise SystemExit(f"{ajza[0]}: قرأها القارئ {len(kalimat)} كلمات، والمجالُ كلمةٌ واحدة")
            c, wasl, al = kalimat[0].split(";")
            natija[ajza[0]] = (f"some ⟨[{', '.join(c.split(','))}], {'true' if wasl == '1' else 'false'}, "
                               f"{'true' if al == '1' else 'false'}⟩")
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
        sutur.append(f"  -- {i} «{h['kalima']}»\n"
                     f"  ⟨{nass_lean(i)}, {qima(FIA, h['fia'], i)}, {k}, {ahkam(h['hukm'], i)}, {zawj}⟩")
    ras = (
        "/-\n"
        "# حالاتُ ضابط «الإبدال: الواوُ والياءُ في الكلمة» المجمَّدة — مولَّد\n\n"
        "مولَّدٌ من `tahaqquq/dawabit/ibdal/cases.json` بـ `python3 -I scripts/bina_dawabit_ibdal.py`؛ لا يُحرَّر يدويًّا.\n"
        f"بصمةُ الحالات: `{basma}`.\n"
        "كتبها مؤلّفٌ مستقلٌّ إجرائيًّا من المواصفة والمصدرين (الألفيّةُ، والكتابُ للفهم)، وفي سياقه ما حُقن آليًّا، وطبع بحثُه الأوّلُ "
        "أسطرًا من الكتاب خارج أبواب الإبدال (`tahaqquq/dawabit/ibdal/taalif.md` و`mulhaq_1.md`)؛ "
        "وجُمّدت ببصمتها في `tahaqquq/dawabit/ibdal/tajmid.json` ودُفعت قبل إيداع الشفرة. والكلمةُ خلايا كما قرأها القارئ (`qari --khalaya`)، "
        "و`none` ما رفضه؛ والسندُ في الملفّ المصدر.\n"
        "-/\n"
        "import Jisr.IbdalAlfiyyaDabit\n\n"
        "namespace Jisr.IbdalAlfiyya.Dabit\n\n"
    )
    jism = "def halat : List Hala := [\n" + ",\n".join(sutur) + "]\n\n"
    khatm = "end Jisr.IbdalAlfiyya.Dabit\n"
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
