"""بناءُ «جدول الربط — القطعة الأولى» (معنًى ← قضيّة واقع) ومحتواه في المخزن، آليًّا من جدولين مختومين.

القرار: قولُ المالك في الجلسة 2026-10-29 (02:05 بتوقيت عمّان): «إيداع جدول ربطٍ مختوم بين المعنى وقضيّة الواقع، حتى يظهر
أول «مفهوم» حقيقيّ … انت مفوض بشكل مطلق … نفذ واكمل البرهان استعدادا للاطلاق التجريبي». والتصميمُ قرارُ البنّاء.

المصدران (لا يختار البنّاءُ صفًّا):
  * «جدول التعريفات — القطعة الأولى» (taarifat.tsv، «وضع»، 74cbcf139ae6…): لكلّ لفظٍ رقمُ صفّه وعمودُ «صفوف الواقع الشاهدة».
    يُقرأ هنا من `TAARIFAT` في scripts/bina_taarifat.py بإيداعه الأخير af645dd (2026-10-22 02:54) — قبل الختم (07:51)، فهو
    القائمةُ التي وُلّد منها الملفّ المختوم (قراءةُ البنّاء؛ ويطابقها الاختبار على الملفّ حين يحضر في MUDAA_DIR).
  * «الواقع المختوم — الدفعة الأولى» (waqi_001.tsv، «واقع-مختوم»، e29bf2a9ef07…): قضايا صفوفه (الشيء، الخاصّة، القيمة) من
    Aql/WaqiJadwal.lean المولَّد منه.

القواعد:
  * المعنى: «ما عرّفه جدول التعريفات في صفّه <ر>» — اسمٌ لمدلول الصفّ المختوم، لا شرحٌ من البنّاء.
  * لكلّ لفظٍ له صفوفُ واقعٍ شاهدة: سطرُ ربطٍ لكلّ صفٍّ منها بقضيّته، بلا تكرار القضيّة الواحدة (صفّا Python 41 و42 قضيّةٌ واحدة).
  * اللفظُ الذي فيه «:» لا تحمله صيغةُ القضيّة في المخزن (`qadiyyaMin` تقسم على «:»)، فيُترك باسمه في المخرج ولا يُربط.
  * الحكمُ (معلومة أو مفهوم) لا يقرّره هذا السكربت: يقرّره `Waqi.hukm` على الصفوف المختومة (قياسٌ، أو روايتان من مصدرين).

المخرج:
  * ملفُّ الربط (المودَع): سطرٌ لكلّ ربط «المعنى⇥الشيء⇥الخاصّة⇥القيمة»، بلا رأس — فبايتاتُه هي أسطرُ `shahid` في السجلّ بعينها،
    وبصمتُه تُفحص من السجلّ نفسه بلا مودَع (mudaat/idaa.py).
  * mawsua/makhzan_waqi.tsv: لكلّ لفظٍ مربوط أصلُ «wad:<اللفظ>:<المعنى>» بسنده في جدول التعريفات (سطرُه في الملفّ = رقمُ الصفّ + 1،
    بعد سطر الرأس)، وقانونُ المطابقة من الوضع، وادّعاءُ المطابقة.

التشغيل (من جذر المستودع):
  python3 -I scripts/bina_ribt.py --ribt <مسار ملفّ الربط>   يكتبه (يرفض الكتابة فوق ملفٍّ مختلف)
  python3 -I scripts/bina_ribt.py --makhzan                    يكتب mawsua/makhzan_waqi.tsv
  python3 -I scripts/bina_ribt.py --lean                       يكتب Aql/WaqiRibtJadwal.lean
  python3 -I scripts/bina_ribt.py --check                      يطابق المخزن وملفَّ Lean وأسطر shawahid في mudaat/sijill.json بالمولَّد
"""
import hashlib
import importlib.util
import json
import os
import re
import sys

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAARIFAT_BASMA = "74cbcf139ae6a3ffd582d79210fd178a722c37057055fc18f8f6de3056f4465c"
WAQI_BASMA = "e29bf2a9ef074fb021ce4f0dbcfa42a4e480e7b8e604b39bb664011d2c65dbc4"
ISM_RIBT = "جدول الربط — القطعة الأولى (المعنى ← قضيّة الواقع)"
MAKHZAN = os.path.join(JADHR, "mawsua", "makhzan_waqi.tsv")
LEAN = os.path.join(JADHR, "Aql", "WaqiRibtJadwal.lean")
NASS = r'"((?:[^"\\]|\\.)*)"'
SAFF = re.compile(r"⟨1, (\d+), " + ", ".join([NASS] * 5) + r", \.(\w+)⟩")


def taarifat():
    spec = importlib.util.spec_from_file_location("bina_taarifat", os.path.join(JADHR, "scripts", "bina_taarifat.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.TAARIFAT


def waqi():
    nass = open(os.path.join(JADHR, "Aql", "WaqiJadwal.lean"), encoding="utf-8").read()
    if f'def basma : String := "{WAQI_BASMA}"' not in nass:
        sys.exit("مرفوض: Aql/WaqiJadwal.lean ليس مولَّدًا من الدفعة المختومة")
    out = {}
    for m in SAFF.finditer(nass):
        f = [json.loads('"' + x + '"') for x in m.groups()[1:6]]
        out[int(m.group(1))] = (f[2], f[3], f[4], m.group(7))
    return out


def maana(i):
    return f"ما عرّفه جدول التعريفات في صفّه {i}"


def bina():
    """(أسطر الربط، [(رقم الصفّ، اللفظ)] المربوطة، [(رقم، لفظ)] المتروكة لـ«:»)"""
    w = waqi()
    ribt, marbut, matruk = [], [], []
    for i, (lafz, _m, _a, _b, _w, shawahid) in enumerate(taarifat(), 1):
        sufuf = [int(s) for s in shawahid.split(",") if s]
        if not sufuf:
            continue
        if ":" in lafz:
            matruk.append((i, lafz))
            continue
        marbut.append((i, lafz))
        seen = set()
        for s in sufuf:
            q = w[s][:3]
            if q in seen:
                continue
            seen.add(q)
            r = (maana(i),) + q
            if any("\t" in x or "\n" in x or not x for x in r):
                sys.exit(f"مرفوض: الصفّ {s} لا يُكتب سطرًا")
            ribt.append(r)
    return ribt, marbut, matruk


def bayt(ribt):
    return "".join("\t".join(r) + "\n" for r in ribt).encode("utf-8")


def makhzan(marbut):
    l = ["# محتوى «جدول الربط — القطعة الأولى»: مولَّدٌ بـ scripts/bina_ribt.py؛ لا يُحرَّر يدويًّا.",
         "# الأصلُ وضعٌ من جدول التعريفات المختوم (سندُه سطرُ اللفظ في taarifat.tsv)؛ والربطُ بالواقع في سجلّ المودَعات وحده.",
         "isdar\tribt-waqi-0.1"]
    for k, (i, lafz) in enumerate(marbut):
        wad, mut = f"wad:{lafz}:{maana(i)}", f"mutabaqa:{lafz}:{maana(i)}"
        sanad = f"{TAARIFAT_BASMA[:12]}@{i + 1}"
        l += [f"qanun\tمطابقة-من-الوضع\t{wad}\t{mut}\tمطابق",
              f"asl\t{wad}\tتقدير\t{sanad}",
              f"iddia\t{mut}\tتقدير\ta={wad}|q={k}\t{sanad}"]
    return "\n".join(l) + "\n"


def lean(ribt):
    body = ",\n".join("  (" + ", ".join(json.dumps(x, ensure_ascii=False) for x in r) + ")" for r in ribt)
    return ("/-\n  Aql/WaqiRibtJadwal.lean — مولَّدٌ بـ `python3 -I scripts/bina_ribt.py --lean` من الجدولين المختومين؛ لا يُحرَّر يدويًّا.\n"
            "  أسطرُ «جدول الربط — القطعة الأولى» (المعنى، الشيء، الخاصّة، القيمة) بترتيبها، وهي حقلُ shawahid في قيده بـ mudaat/sijill.json.\n-/\n\n"
            "namespace Waqi.Ribt\n\n/-- أسطرُ الربط. -/\n"
            f"def ribt : List (String × String × String × String) := [\n{body}\n]\n\nend Waqi.Ribt\n")


def main():
    ribt, marbut, matruk = bina()
    a = sys.argv[1:]
    if "--ribt" in a:
        p = a[a.index("--ribt") + 1]
        b = bayt(ribt)
        if os.path.exists(p) and open(p, "rb").read() != b:
            sys.exit(f"مرفوض: {p} موجودٌ ببايتاتٍ أخرى؛ لا يُعاد كتابتُه")
        open(p, "wb").write(b)
        print(f"{p}: {len(ribt)} ربطًا لـ{len(marbut)} لفظًا، بصمته {hashlib.sha256(b).hexdigest()}")
    elif "--makhzan" in a:
        open(MAKHZAN, "w", encoding="utf-8").write(makhzan(marbut))
        print(MAKHZAN)
    elif "--lean" in a:
        open(LEAN, "w", encoding="utf-8").write(lean(ribt))
        print(LEAN)
    elif "--check" in a:
        e = []
        if open(LEAN, encoding="utf-8").read() != lean(ribt):
            e.append("Aql/WaqiRibtJadwal.lean لا يطابق المولَّد")
        if open(MAKHZAN, encoding="utf-8").read() != makhzan(marbut):
            e.append("makhzan_waqi.tsv لا يطابق المولَّد")
        s = json.load(open(os.path.join(JADHR, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
        r = [m for m in s if m["ism"] == ISM_RIBT]
        if len(r) != 1 or [tuple(x) for x in r[0].get("shawahid", [])] != ribt:
            e.append("أسطر shawahid في sijill.json لا تطابق المولَّد")
        print("مطابق" if not e else "\n".join(e))
        sys.exit(1 if e else 0)
    else:
        sys.exit(__doc__)
    if matruk:
        print("متروكٌ لـ«:» في لفظه: " + "، ".join(f"{i} «{l}»" for i, l in matruk))


if __name__ == "__main__":
    main()
