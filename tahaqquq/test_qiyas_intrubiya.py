"""القياسُ المسجَّل لهيكل الإنتروبيا (scripts/qiyas_intrubiya.py؛ hawkama/tasjil_qiyas_intrubiya.md).

يفحص بلا مودَع، وتوقّعاتُه مستقلّة:
١. الشطر: القائمةُ من البذرة 20261029 بحجم 3118 من 6236، وبصمتُها هي المسجَّلة في الوثيقة (تُحسب هنا بلا السكربت).
٢. الحراسات: الوثيقةُ تسمّي السبعَ كلَّها؛ والنتيجةُ إن أُودعت تحمل البصماتِ المسجَّلةَ وبصمةَ الوثيقة نفسَها. ومطابقةُ الملفّات وقتَ التشغيل
   حراسةُ السكربت لا هذا الاختبار: فالتحصيلُ يتغيّر بعد التسجيل (dal/tahsil-wasl) ولا يُبطل نتيجةً قيست قبله.
٣. المقادير على كلماتٍ باليد: كلمةٌ واحدة في A وفي B → CE_B من صيغة كريشيفسكي–تروفيموف بعدد الحيّ من law.json مباشرةً؛ وكلمةٌ في B لم تُرَ
   حالاتُها في A → CE_B = متوسّطُ log₂|حيّ|، فالمعرفةُ صفر؛ ونسبةُ الردّ بكلمةٍ يردّها القانون.
٤. حكمُ الفروض حول حدودها بفارق 10⁻⁴ (الحدُّ نفسُه لا يُفحص بالأعداد العشريّة: 3.0 − 2.9 > 0.10 فيها).
الطفرات: P1310 (البذرة، ١)، P1311 (التنعيم، ٣)، P1312 (عتبة ف2، ٤)، P1313 (السعة، ٣). وحراساتُ السكربت (`hirasat`) بلا طفرةٍ هنا: فحصُها هنا
يُبطله تغييرُ التحصيل بعد التسجيل؛ وشاهدُها التشغيلُ نفسُه، إذ تحمل النتيجةُ البصماتِ التي طابقتها.
التشغيل: python3 -I tahaqquq/test_qiyas_intrubiya.py
"""

import hashlib
import json
import math
import pathlib
import random
import re
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(JADHR / "scripts"))
import qiyas_intrubiya as qi  # noqa: E402

LAW = JADHR / "integrations" / "nabt" / "src" / "nabt" / "data" / "law.json"
NABT = "ابتثجحخدذرزسشصضطظعغفقكلمنهويء"
FAIL = []


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


def nb(h, s):
    return 4 * NABT.index(h) + s


def main():
    nass = (JADHR / "hawkama" / "tasjil_qiyas_intrubiya.md").read_text(encoding="utf-8")
    sijill = dict(re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", nass, flags=re.M))

    # ١
    B = sorted(random.Random(20261029).sample(range(6236), 3118))
    hb = hashlib.sha256("\n".join(map(str, B)).encode("ascii")).hexdigest()
    check("بصمة الشطر المحجوب هي المسجَّلة", sijill.get("qaimat_B") == hb)
    check("shatr في السكربت = الشطر هنا", qi.shatr(6236) == B and qi.qaimat_basma(B) == hb)

    # ٢
    sab = {"scripts/qiyas_intrubiya.py", "scripts/intrubiya.py", "Dal/Tahsil.lean", "Qari/Tahsil.lean",
           "integrations/nabt/src/nabt/data/law.json", "quran-simple-enhanced.txt", "qaimat_B"}
    check("الوثيقة تسمّي البصمات السبع", set(sijill) == sab)
    natija = JADHR / "hawkama" / "natija_qiyas_intrubiya.json"
    if natija.exists():
        n = json.loads(natija.read_text(encoding="utf-8"))
        check("النتيجة تحمل البصمات المسجَّلة نفسَها", n.get("basamat") == sijill)
        check("النتيجة تحمل بصمةَ وثيقة التسجيل",
              n.get("tasjil_sha256") == hashlib.sha256((JADHR / "hawkama" / "tasjil_qiyas_intrubiya.md").read_bytes()).hexdigest())
    else:
        print("—    لا نتيجةَ مودَعة بعد")

    # ٣ — الحيُّ لكلّ حالة من law.json مباشرةً
    d = json.loads(LAW.read_text(encoding="utf-8"))
    step = [[t[0] for t in row] for row in d["transitions"]]
    hayy = lambda q: sum(1 for a in range(116) if step[q][a] != 96)
    qanun = qi.it.Qanun()
    # كُتِبَ: حالاتُها الثلاث مختلفة (البداية، ثمّ بعد الضمّة، ثمّ بعد الكسرة)، فلكلٍّ حدثٌ واحد. (كَتَبَ تمرّ بحالة الفتحة مرّتين.)
    w = (nb("ك", 1), nb("ت", 2), nb("ب", 0))
    qs = [0, step[0][w[0]], step[step[0][w[0]]][w[1]]]
    check("حالاتُ كُتِبَ مختلفة", len(set(qs)) == 3)
    m = qi.maqadir(qanun, [w], [w])
    ce = sum(-math.log2(1.5 / (1 + 0.5 * hayy(q))) for q in qs) / 3
    check("CE_B بصيغة كريشيفسكي–تروفيموف على كلمةٍ واحدة", abs(m["CE_B"] - ce) < 1e-12)
    check("cap_B = متوسّط log₂|حيّ|", abs(m["cap_B"] - sum(math.log2(hayy(q)) for q in qs) / 3) < 1e-12)
    check("H_MM_A على حدثٍ واحدٍ لكلّ حالة = 0", m["H_MM_A"] == 0)
    w2 = (nb("ء", 0), nb("ق", 0))
    q2 = [0, step[0][w2[0]]]
    check("ءَقَ لا تشارك كُتِبَ إلّا حالةَ البداية", set(q2) & set(qs) == {0})
    m2 = qi.maqadir(qanun, [w2], [w])
    ce2 = (-math.log2(0.5 / (1 + 0.5 * hayy(0))) - math.log2(0.5 / (0.5 * hayy(qs[1]))) - math.log2(0.5 / (0.5 * hayy(qs[2])))) / 3
    check("حالاتٌ لم تُرَ في A: التوزيعُ المنتظم على الحيّ", abs(m2["CE_B"] - ce2) < 1e-12)
    lam_sukun = nb("ل", 3)
    m3 = qi.maqadir(qanun, [w, (lam_sukun, nb("ي", 0))], [w])
    check("نسبةُ الردّ: كلمةٌ من اثنتين يردّها القانون", m3["rej_A"] == 0.5 and m3["rej_B"] == 0.0)

    # ٤
    f = qi.hukm_furud({"CE_B": 3.0, "H_MM_A": 2.9001, "cap_B": 4.8001, "rej_A": 0.07, "rej_B": 0.0799})
    check("دون الحدود صدق", [f[k]["hukm"] for k in ("F1", "F2", "F3")] == ["صدق", "صدق", "صدق"])
    f = qi.hukm_furud({"CE_B": 3.0, "H_MM_A": 2.8999, "cap_B": 4.7999, "rej_A": 0.07, "rej_B": 0.0801})
    check("فوق الحدود كذب", [f[k]["hukm"] for k in ("F1", "F2", "F3")] == ["كذب", "كذب", "كذب"])

    print(f"القياسُ المسجَّل: {'فشل ' + str(len(FAIL)) if FAIL else 'مرّ'}")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
