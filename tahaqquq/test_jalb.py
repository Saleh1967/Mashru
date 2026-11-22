"""جلبُ المودَعات المختومة (mudaat/jalb.py) وإعادةُ بناء جدولَي الجنس والمثال (scripts/bina_jadawil_rabt.py)، بلا شبكة.

**وسمُ التوقّعات.** من القاعدة في رأس jalb.py لا من مخرجه: لا يدخل المجلّدَ ملفٌّ إلّا وبصمتُه بصمتُه المختومة في mudaat/sijill.json.
١. مصدرٌ محلّيّ (`--mahalli`) بايتاتُه غيرُ المختومة (lisan.txt «x») ← «مرفوض» باسمه، ولا يُكتب الملفّ، والخروجُ 1.
٢. مصدرٌ غائب ← «غائب» باسمه، ولا يُكتب.
٣. ما أصولُه غائبة (luzum_mujam.tsv بلا lisan وmaqayis) ← «غائب» بأصوله، ولا يُكتب.
٤. jins.tsv وmithal.tsv يُبنيان، وبصمتاهما بصمتاهما المختومتان في السجلّ (تُقرأ هنا من السجلّ لا من الشفرة).
٥. ملفٌّ حاضرٌ بغير بصمته المختومة لا يُعدّ حاضرًا ويُستبدل بالمبنيّ.
٦. الرسالةُ الأخيرة تعدّ المرشَّحةَ الثمانية بأسمائها، ولا يُغيَّر السجلّ.
الطفرات: P1640 (الجلبُ يكتب بلا مطابقة البصمة: ١)، P1641 (المبنيُّ يُكتب بغير بصمته المختومة: ٤).
التشغيل: python3 -I tahaqquq/test_jalb.py
"""
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
najah, fashal = 0, []


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def main():
    sj = json.loads((JADHR / "mudaat/sijill.json").read_text(encoding="utf-8"))["sijill"]
    mk = {m["milaf"]: m["sha256"] for m in sj if m["hala"] == "مختوم"}
    murashshah = [m["milaf"] for m in sj if m["hala"] == "مرشح"]
    qabl = hashlib.sha256((JADHR / "mudaat/sijill.json").read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as src:
        open(os.path.join(src, "lisan.txt"), "w").write("x")
        open(os.path.join(d, "jins.tsv"), "w").write("fasid\n")
        p = subprocess.run([sys.executable, "-I", str(JADHR / "mudaat/jalb.py"), d, "--mahalli", src],
                           capture_output=True, text=True, timeout=600)
        out = p.stdout
        tahaqqaq(p.returncode == 1, f"خروج {p.returncode} لا 1")
        tahaqqaq(any(l.startswith("مرفوض: lisan.txt") for l in out.splitlines()) and not os.path.exists(os.path.join(d, "lisan.txt")),
                 "١ lisan.txt بغير بصمته كُتب أو لم يُرفض")
        tahaqqaq(any(l.startswith("غائب: maqayis.txt") for l in out.splitlines()) and not os.path.exists(os.path.join(d, "maqayis.txt")),
                 "٢ maqayis.txt الغائب")
        tahaqqaq("غائب: luzum_mujam.tsv (أصولُه غائبة" in out and not os.path.exists(os.path.join(d, "luzum_mujam.tsv")),
                 "٣ luzum_mujam.tsv بلا أصوله")
        for f in ("jins.tsv", "mithal.tsv"):
            q = os.path.join(d, f)
            tahaqqaq(os.path.exists(q) and hashlib.sha256(open(q, "rb").read()).hexdigest() == mk[f], f"٤/٥ {f} غيرُ المختوم")
        # كانت ثمانيةً مرشَّحة، وخُتمت كلُّها بإذن المالك 2026-11-21 (13:57)؛ فلا مرشَّحَ يُذكر، والثمانيةُ في «غائبٌ بلا جلب» بأسمائها.
        tahaqqaq(murashshah == [] and "مرشَّحةٌ لا تُجلب" not in out, "٦ مرشَّحٌ باقٍ بعد الختم")
        tahaqqaq(all(f"غائبٌ بلا جلب: {f}" in out for f in ("hawass.tsv", "awwaliyyat.tsv", "azmina.tsv", "makan.tsv", "mirsat.tsv",
                                                         "isnad.tsv", "jisr_dal.tsv", "nisab_asnaf.tsv")),
                 "٦ب الثمانيةُ المختومة غائبةٌ بلا جلب")
        tahaqqaq(not [x for x in os.listdir(d) if x.startswith(".jalb_")], "مؤقّتٌ باقٍ في المجلّد")
    tahaqqaq(hashlib.sha256((JADHR / "mudaat/sijill.json").read_bytes()).hexdigest() == qabl, "٦ تغيّر السجلّ")
    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        sys.exit(1)
    print(f"test_jalb: {najah} فحصًا نجح")


if __name__ == "__main__":
    main()
