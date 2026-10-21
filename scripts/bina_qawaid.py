"""يولّد `Jisr/QawaidJadwal.lean` من جدول القواعد المودَع (`qawaid.tsv` في MUDAA_DIR) — صفُّه الأوّل: الأسماء الستّة.

التشغيل: python3 -I scripts/bina_qawaid.py <qawaid.tsv>          (يكتب Jisr/QawaidJadwal.lean)
         python3 -I scripts/bina_qawaid.py <qawaid.tsv> --stdout (يطبعه ولا يكتب؛ يستعمله tahaqquq/test_qawaid.py)

الخلايا `4·حامل + حالة`: الحاملُ موضعُ الحرف في جدول المخارج `Dal.hawamil` مقروءًا من `Dal/Makharij.lean` نصًّا (والهمزةُ على
الألف همزة)، والحالةُ من علامتها (فتحة 0، ضمّة 1، كسرة 2، سكون 3)؛ وحرفُ المدّ بلا علامةٍ بعد حركته (الألف بعد الفتحة، والواو بعد
الضمّة، والياء بعد الكسرة) ساكن؛ وما سوى ذلك بلا علامة يُرفض باسمه (لا تخمينَ لحركة).
"""
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARAKA = {"َ": 0, "ُ": 1, "ِ": 2, "ْ": 3}
MADD = {0: "ا", 1: "و", 2: "ي"}
HAMZA = {"أ": "ء", "إ": "ء", "ؤ": "ء", "ئ": "ء"}
WAJH = {"قصر": "qasr", "نقص": "naqs", "تمام": "tamam"}


def hawamil():
    src = open(os.path.join(ROOT, "Dal", "Makharij.lean"), encoding="utf-8").read()
    m = re.search(r"def hawamil : List Char :=\s*\[(.*?)\]", src, re.S)
    h = re.findall(r"'(.)'", m.group(1))
    if len(h) != 29:
        raise SystemExit(f"جدول المخارج: {len(h)} حاملًا لا 29")
    return h


def khalaya(sura, h):
    out = []
    i = 0
    while i < len(sura):
        ch = HAMZA.get(sura[i], sura[i])
        if ch not in h:
            raise SystemExit(f"«{sura}»: حرفٌ ليس في جدول المخارج: {sura[i]!r}")
        if i + 1 < len(sura) and sura[i + 1] in HARAKA:
            out.append(4 * h.index(ch) + HARAKA[sura[i + 1]])
            i += 2
        elif out and MADD.get(out[-1] % 4) == ch:
            out.append(4 * h.index(ch) + 3)
            i += 1
        else:
            raise SystemExit(f"«{sura}»: حرفٌ بلا علامةٍ وليس مدًّا بعد حركته: {sura[i]!r}")
    return out


def lean_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def safif(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l]
    hdr = lines[0].split("\t")
    want = ["qaida", "ism", "raf", "nasb", "jarr", "qasr", "shart", "daraja", "sanad"]
    if hdr != want:
        raise SystemExit(f"رأسُ الجدول {hdr} لا {want}")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


def daraja(cell):
    """«أ>ب=لفظ، …»: الوجهُ الأوّل أرجحُ من الثاني بلفظ مصدره (أشهر، أحسن، الأفصح)؛ و«—» لا درجة."""
    if cell == "—":
        return "[]"
    out = []
    for p in cell.split("، "):
        ab, lafz = p.split("=")
        a, b = ab.split(">")
        out.append(f"(.{WAJH[a]}, .{WAJH[b]}, {lean_str(lafz)})")
    return "[" + ", ".join(out) + "]"


def wallid(path):
    h = hawamil()
    basma = hashlib.sha256(open(path, "rb").read()).hexdigest()
    rows = [r for r in safif(path) if r["qaida"] == "الأسماء الستّة"]
    out = [
        "/-",
        "  Jisr/QawaidJadwal.lean — مولَّدٌ من جدول القواعد المودَع (`qawaid.tsv` في MUDAA_DIR؛ في `mudaat/sijill.json` باسم «جدول القواعد»)",
        "  بـ `python3 -I scripts/bina_qawaid.py <qawaid.tsv>`؛ لا يُحرَّر يدويًّا (يطابقه `tahaqquq/test_qawaid.py` بايتًا بحضور المودَع).",
        "  الخلايا `4·حامل + حالة` بجدول المخارج `Dal.hawamil` (فتحة 0، ضمّة 1، كسرة 2، سكون 3)، وحرفُ المدّ بعد حركته ساكن.",
        "  صفُّه الأوّل: الأسماء الستّة (`hawkama/خطة_الجبر_يقود.md` §١٠ج-1)؛ والقوانينُ منه في `Jisr/QawaidSitta.lean`.",
        "-/",
        "",
        "namespace Jisr",
        "namespace QawaidJadwal",
        "",
        "/-- بصمةُ الجدول (sha256) الذي وُلِّد منه هذا الملفّ: إصدارُ القاعدة (`Qaida.isdar`). -/",
        f"def basma : String := {lean_str(basma)}",
        "",
        "/-- وجوهُ الاسم: التمامُ بالحروف، والقصرُ بالألف في الأحوال كلّها، والنقصُ بالحركات (القاعدة العامّة). -/",
        "inductive Wajh | tamam | qasr | naqs",
        "deriving DecidableEq, Repr",
        "",
        "/-- صفٌّ من «الأسماء الستّة»: الاسم، وصورُ التمام رفعًا ونصبًا وجرًّا خلايا، والقصرُ، وشرطُ الصحبة، والدرجةُ بين الوجوه (الأوّلُ",
        "أرجحُ من الثاني بلفظ مصدره: «أشهر»، «أحسن»، «الأفصح»)، والسند. -/",
        "structure Saff where",
        "  ism : String",
        "  raf : List Nat",
        "  nasb : List Nat",
        "  jarr : List Nat",
        "  qasr : Bool",
        "  sahib : Bool",
        "  daraja : List (Wajh × Wajh × String)",
        "  sanad : String",
        "deriving DecidableEq, Repr",
        "",
        "/-- الصفوفُ بترتيب الجدول. -/",
        "def sitta : List Saff :=",
    ]
    items = []
    for r in rows:
        shart = r["shart"].split("، ")
        if not set(shart) <= {"إضافة", "صحبة"} or "إضافة" not in shart:
            raise SystemExit(f"{r['ism']}: شرطٌ غيرُ معروف {shart}")
        if r["qasr"] not in ("نعم", "لا"):
            raise SystemExit(f"{r['ism']}: القصر {r['qasr']!r}")
        cells = [khalaya(r[k], h) for k in ("raf", "nasb", "jarr")]
        items.append(
            "  ⟨" + ", ".join([
                lean_str(r["ism"]),
                *("[" + ", ".join(map(str, c)) + "]" for c in cells),
                "true" if r["qasr"] == "نعم" else "false",
                "true" if "صحبة" in shart else "false",
                daraja(r["daraja"]),
                lean_str(r["sanad"]),
            ]) + "⟩")
    out.append("  [" + items[0][2:] if items else "  [")
    for it in items[1:]:
        out[-1] += ","
        out.append("   " + it[2:])
    out[-1] += "]"
    out += ["", "end QawaidJadwal", "end Jisr", ""]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    text = wallid(sys.argv[1])
    if "--stdout" in sys.argv[2:]:
        sys.stdout.write(text)
    else:
        open(os.path.join(ROOT, "Jisr", "QawaidJadwal.lean"), "w", encoding="utf-8", newline="\n").write(text)
        print("كُتب Jisr/QawaidJadwal.lean")
