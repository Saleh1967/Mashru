"""مديرُ الوكلاء (Nizam/Mudir.lean، والأداة `mudir` من Qari/Mudir.lean).

**وسمُ التوقّعات.** حارسُ تراجعٍ على مخرجٍ رآه البنّاء، لا «مفحوص» ولا «مطابَق»: كتبها البنّاءُ لا مؤلّفٌ مستقلّ. والمدير بنيةٌ لا
قطعةٌ تحكم على تركيبٍ أو لفظٍ من مصدر (CLAUDE.md، طريقة العمل ٢أ: «لا على قطع البنية»)، فلا ضابطَ مجمَّد له. يفحص، بلا مودَع:
١. القسمة والقرار: أمرُ المالك ينفَّذ، والقناةُ المجهولة لا تأمر («لا مقام»)، والنظيرُ لا يقترح إيداعًا، والمحظورُ مرفوضٌ من المالك نفسِه،
   والأمرُ بلا نصٍّ مرفوض، وقالبُ «ما معنى» سؤالٌ يقرأ من أيّ قناة، ولفظٌ ليس في السجلّ قراءةٌ لا أمر.
٢. الخطّة: لكلّ أمرٍ وكلاؤه بترتيبهم، والمرفوضُ لا وكيلَ له (لا سطرَ خطوة).
٣. النتيجة: القارئُ على نصٍّ غير مشكولٍ رفضٌ باسمه (خروج 2)، والسؤالُ بالدلالات يكفيه حكمٌ واحد، والوكيلُ الغائبُ خطأُ تنفيذ لا يُخفى (خروج 3).
٤. المتعلّم: الاقتراحُ يُكتب في مجلّد الاقتراحات وحده، ولا تتغيّر بصمةُ `mudaat/sijill.json` ولا `mawsua/makhzan.tsv`.
٥. الإيصال: `--tahaqquq` يطابق إعادةَ التشغيل، ويرفض إيصالًا غُيّرت فيه بصمةُ خطوة.
٧. لا جوابَ معلَّق: لكلّ خطوةٍ غيرِ «حكمٌ صدر» سطرُ سببٍ وعلاج، ولكلّ رفضٍ علاجُه، و`rabt` بلا مودَعٍ «لا حكم» بعلاجه (`mudaat/jalb.py`).
٨. وإن حضرت المودَعاتُ المختومة في MUDAA_DIR: «أعرب» كاملٌ بـ`rabt` (فحصٌ بالمودَع بلا طفرة).
٦. التصديق: الخبرُ «لا حكم على الواقع» بلا شاهد، ومعالجُ NTP يصنّف الزيتونَ نباتًا والولدَ إنسانًا.

الطفرات وقاتلُها: على Lean يقتلها البناء — P1620 (المجهولُ يأمر: `bila_maqam_la_qisma`)، P1621 (الالتماسُ يقترح: `taallam_malik`)،
P1622 (المحظورُ أمرٌ مرخَّص: `shawahid_qarar`)، P1623 (الخطأُ لا يغلب: `khata_yaghlib`)، P1624 (المرفوضُ له خطّة: `rafd_la_khitta`)،
P1625 (الإنشاءُ يُصدَّق: `insha_ghayr_qabil`)، P1626 (الخروجُ بغير صفرٍ نجاح: `khuruj_khata`)؛ وفي الأداة يقتلها هذا الاختبار —
P1627 (القارئُ لا يُرفض: ٣)، P1628 (الإيصالُ لا يقارن الخطوات: ٥)، P1629 (المتعلّمُ يكتب في mawsua: ٤)، P1638 (لا يُطبع سطرُ السبب: ٧)، P1639 (rabt يُشغَّل بلا مودَع: ٧)، P1630 (القناةُ الافتراضيّة المالك: ١).
التشغيل: python3 -I tahaqquq/test_mudir.py
"""
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent
MUDIR = JADHR / ".lake" / "build" / "bin" / "mudir"

najah = 0
fashal = []


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


FARIGH = tempfile.mkdtemp()  # MUDAA_DIR فارغ: الحالاتُ لا تتبع حضورَ المودَعات في البيئة


def shaghghil(*args, bia=None):
    bia = bia or dict(os.environ, MUDAA_DIR=FARIGH)
    p = subprocess.run([str(MUDIR), *args], cwd=JADHR, capture_output=True, text=True, timeout=300, env=bia)
    return p.returncode, p.stdout


def satr(out, bad):
    for l in out.splitlines():
        if l.startswith(bad):
            return l
    return ""


def basma(p):
    return hashlib.sha256((JADHR / p).read_bytes()).hexdigest()


def main():
    if not MUDIR.exists():
        print(f"FAIL الأداة غير مبنيّة: {MUDIR} (lake build mudir)")
        sys.exit(1)

    # ١ و٢: القرار والخطّة (البرومبت، القناة) ← (بادئة القرار، الخطّة، الخروج)
    HALAT = [
        (["--qanat", "malik", "اقْرَأْ كَتَبَ الطَّالِبُ الدَّرْسَ"], "القرار: تنفيذ «اقرأ» على «كَتَبَ الطَّالِبُ الدَّرْسَ»", "qari", 0),
        (["اقْرَأْ كَتَبَ الطَّالِبُ الدَّرْسَ"], "القرار: رفض: «اقرأ» أمرٌ بلا مقام", "", 2),
        (["--qanat", "majhul", "اقْرَأْ كَتَبَ"], "القرار: رفض: «اقرأ» أمرٌ بلا مقام", "", 2),
        (["--qanat", "wakil", "تَعَلَّمْ الْمَاءُ سَائِلٌ"], "القرار: رفض: «تعلّم» لا يرخّصه قسمُ «التماس»", "", 2),
        (["--qanat", "wakil", "أَعْرِبْ كَتَبَ الطَّالِبُ الدَّرْسَ"], "القرار: تنفيذ «أعرب»", "tarkib ← athar ← rabt", 1),
        (["--qanat", "malik", "ادْمُجْ الفرع"], "القرار: رفض: «ادمج» سلطةُ المالك في الجلسة", "", 2),
        (["--qanat", "malik", "احْذِفْ mudaat"], "القرار: رفض: «احذف» سلطةُ المالك في الجلسة", "", 2),
        (["--qanat", "malik", "اقْرَأْ:"], "القرار: رفض: «اقرأ» يحتاج نصًّا بعده", "", 2),
        (["ما معنى البلجة؟"], "القرار: تنفيذ «اسأل» على «البلجة»", "faahis --sual ← faahis --sual ← faahis --sual", 0),
        (["--qanat", "malik", "طِرْ إِلَى الْقَمَرِ"], "القرار: قراءة «طِرْ إِلَى الْقَمَرِ»", "athar", 1),
        (["--qanat", "wakil", "تتبّع كَتَبَ الطَّالِبُ"], "القرار: تنفيذ «تتبّع»", "silsila", 0),
        # «صنّف» خطوتان منذ 2026-11-21 (أمرُ المالك 13:57): الشبكةُ المبنيّة، ثمّ شبكةُ المخصّص المختوم (NTP.Mukhassas)، بديلتان
        # (Nizam.Mudir.natijaJamia ← jamBadil). وبلا مودَعٍ (MUDAA_DIR فارغ) الثانيةُ «لا حكم»، فالزيتونُ يبقى 0 بالأولى والقمرُ 1.
        (["--qanat", "malik", "صَنِّفْ الزَّيْتُونَ"], "القرار: تنفيذ «صنّف» على «الزَّيْتُونَ»", "NTP.Wasl ← NTP.Mukhassas", 0),
        (["--qanat", "malik", "صنف القمر"], "القرار: تنفيذ «صنّف» على «القمر»", "NTP.Wasl ← NTP.Mukhassas", 1),
        (["--qanat", "malik", "اعرض"], "القرار: تنفيذ «اعرض»", "", 0),
        (["--qanat", "wakil", "شَكِّلْ كتب"], "القرار: تنفيذ «شكّل» على «كتب»", "A116.Tashkil", 1),
    ]
    for args, qarar, khitta, khuruj in HALAT:
        code, out = shaghghil(*args)
        tahaqqaq(satr(out, "القرار:").startswith(qarar), f"١ {args}: {satr(out, 'القرار:')!r}")
        k = satr(out, "الخطّة")
        tahaqqaq(k.split(": ", 1)[-1] == khitta, f"٢ {args}: {k!r}")
        tahaqqaq(code == khuruj, f"١ {args}: خروج {code} لا {khuruj}")
        if qarar.startswith("القرار: رفض"):
            tahaqqaq("لم يُشغَّل وكيل" in out and " · خروج " not in out, f"٢ {args}: المرفوضُ شغّل وكيلًا")

    # ١: قالبُ «ما معنى» من القناة المجهولة، وأمرُ «اعرض» يطبع السجلّ بمحظوراته
    code, out = shaghghil("--qanat", "malik", "اعرض")
    tahaqqaq("ادمج\t← محظور" in out and "تعلم\t← تعلّم (اقتراح، للمالك وحده)" in out, "١ اعرض: السجلّ")

    # ٣: النتيجة
    code, out = shaghghil("--qanat", "malik", "اقرأ كتب الطالب")
    tahaqqaq(code == 2 and "· رفضٌ باسمه" in out and "مرفوضة باسمها" in out, f"٣ غيرُ المشكول: خروج {code}")
    code, out = shaghghil("ما معنى البلجة؟")
    tahaqqaq(satr(out, "النتيجة الجامعة:") == "النتيجة الجامعة: حكمٌ صدر" and out.count("· لا حكم") == 2,
             "٣ الدلالات: حكمُ المطابقة يكفي وتبقى الأخريان لا حكم")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, ".lake", "build", "bin"))
        for f in ("mudaat", "mawsua"):
            os.symlink(JADHR / f, os.path.join(d, f))
        bia = dict(os.environ, MASHRU_JADHR=d, MUDAA_DIR=FARIGH)
        code, out = shaghghil("--qanat", "malik", "أَعْرِبْ كَتَبَ", bia=bia)
        tahaqqaq(code == 3 and "· خطأ تنفيذ" in out and "النتيجة الجامعة: خطأ تنفيذ" in out,
                 f"٣ الوكيلُ الغائب: خروج {code}")

    # ٤: المتعلّم
    qabl = (basma("mudaat/sijill.json"), basma("mawsua/makhzan.tsv"))
    with tempfile.TemporaryDirectory() as d:
        iq = os.path.join(d, "iq")
        code, out = shaghghil("--qanat", "malik", "--iqtirahat", iq, "--isal", os.path.join(d, "isal.json"),
                              "تَعَلَّمْ الْمَاءُ سَائِلٌ")
        ms = sorted(os.listdir(iq)) if os.path.isdir(iq) else []
        tahaqqaq(code == 0 and len(ms) == 1 and ms[0].endswith(".tsv"), f"٤ الاقتراح: خروج {code}، ملفّات {ms}")
        if ms:
            nass = open(os.path.join(iq, ms[0]), encoding="utf-8").read()
            tahaqqaq(nass.startswith("nass\tالْمَاءُ سَائِلٌ\n") and "لا يدخل المخزن ولا يُختم إلّا بإذن المالك" in nass,
                     "٤ نصُّ الاقتراح")
        tahaqqaq((basma("mudaat/sijill.json"), basma("mawsua/makhzan.tsv")) == qabl, "٤ تغيّر mudaat أو mawsua")

        # ٥: الإيصال
        p = os.path.join(d, "isal.json")
        j = json.load(open(p, encoding="utf-8"))
        tahaqqaq(j.get("schema") == "mashru.mudir.isal.v1" and [k["wakil"] for k in j["khitta"]] == ["athar", "mutaallim"],
                 "٥ الإيصال: المخطّط والخطّة")
        code, out = shaghghil("--tahaqquq", p)
        tahaqqaq(code == 0 and out.startswith("الإيصال يطابق"), f"٥ التحقّق: خروج {code} {out!r}")
        j["khitta"][0]["basma"] = "0" * 64
        q = os.path.join(d, "fasid.json")
        json.dump(j, open(q, "w", encoding="utf-8"), ensure_ascii=False)
        code, out = shaghghil("--tahaqquq", q)
        tahaqqaq(code == 4 and "الخطوة 1" in out, f"٥ الإيصالُ المغيَّر: خروج {code} {out!r}")
        tahaqqaq(len(os.listdir(iq)) == 1, "٥ التحقّقُ كتب اقتراحًا في مجلّد الاقتراحات الأصليّ")

    # ٦: التصديق ومعالج NTP
    code, out = shaghghil("كَتَبَ الطَّالِبُ الدَّرْسَ")
    tahaqqaq(code == 0 and "«خبرٌ مثبت» ← خبر: لا شاهدَ واقعٍ مودَع" in out, f"٦ الخبر: خروج {code}")
    code, out = shaghghil("--qanat", "malik", "صَنِّفْ الزَّيْتُونَ")
    tahaqqaq("القسم بالوراثة: نبات\tحملُ «يسير» إسناديًّا: لا حكم" in out, "٦ الزيتون")
    code, out = shaghghil("--qanat", "malik", "صنف الولد")
    tahaqqaq("القسم بالوراثة: إنسان\tحملُ «يسير» إسناديًّا: مرخَّص" in out, "٦ الولد")

    # ٧: لا جوابَ معلَّق — لكلّ خطوةٍ نتيجتُها غيرُ «حكمٌ صدر» سطرُ سببٍ وعلاجٍ في «ما بقي باسمه»، ولكلّ رفضٍ في القرار علاجُه
    for args, _, _, _ in HALAT + [(["--qanat", "malik", "اقرأ كتب الطالب"], 0, 0, 0), (["ما معنى البلجة؟"], 0, 0, 0)]:
        code, out = shaghghil(*args)
        khatawat = [l for l in out.splitlines() if l.startswith("- ") and " · خروج " in l]
        ghayr = [l.split(" «")[0][5:] for l in khatawat if not l.endswith("· حكمٌ صدر")]
        baqi = out.split("## ما بقي باسمه", 1)[-1]
        asbab = [l for l in baqi.splitlines() if " — السبب: " in l and " · العلاج: " in l and not l.endswith("العلاج: ")]
        tahaqqaq(len(asbab) == len(ghayr), f"٧ {args}: {len(ghayr)} خطوةً بلا حكم و{len(asbab)} سطرَ سببٍ وعلاج")
        if satr(out, "القرار:").startswith("القرار: رفض"):
            tahaqqaq(". العلاج: " in baqi, f"٧ {args}: رفضٌ بلا علاج")
        tahaqqaq("لا جوابَ معلَّق" in baqi, f"٧ {args}: لا سطرَ «لا جوابَ معلَّق»")
    code, out = shaghghil("--qanat", "malik", "أَعْرِبْ كَتَبَ الطَّالِبُ الدَّرْسَ")
    tahaqqaq("- rabt: لا حكم — السبب: المودَعاتُ المختومة" in out and "python3 -I mudaat/jalb.py" in out and " · خروج 0 " in out,
             "٧ rabt بلا مودَع: لا سببَ ولا علاج، أو شُغّل")
    # ٩: وكيلُ التشكيل (A116.Tashkil، 2026-11-20). بلا معجم: «مودَعٌ غائب» وسببٌ وعلاج. وبمعجمٍ صغيرٍ مكتوبٍ باليد هنا (لا من
    # المودَع ولا من الشيفرة): «كتب» محتمَلٌ بصورتيه كلتيهما بترتيبهما، و«قال» مرشَّحٌ واحد، و«غول» لا حكم؛ ولا يُكتب في النصّ شيء.
    code, out = shaghghil("--qanat", "malik", "شَكِّلْ كتب")
    tahaqqaq(code == 1 and "مودَعٌ غائب" in out and "- A116.Tashkil: لا حكم — السبب: معجمُ التشكيل المختوم" in out
             and "python3 -I mudaat/jalb.py" in out, f"٩ التشكيل بلا معجم: خروج {code}")
    with tempfile.TemporaryDirectory() as d:
        pathlib.Path(d, "tashkil_mujam.tsv").write_text("قال\tقَالَ\nكتب\tكَتَبَ كُتُبٌ\n", encoding="utf-8")
        bia = dict(os.environ, MUDAA_DIR=d)
        code, out = shaghghil("--qanat", "malik", "شَكِّلْ قال كتب", bia=bia)
        tahaqqaq(code == 0 and "قال\tقال\tمرشَّحٌ_واحد\tقَالَ\n" in out and "كتب\tكتب\tمحتمَل\tكَتَبَ كُتُبٌ\n" in out
                 and "النتيجة الجامعة: حكمٌ صدر" in out, f"٩ التشكيل بمعجم: خروج {code}")
        code, out = shaghghil("--qanat", "malik", "شَكِّلْ قَالَ غول", bia=bia)
        tahaqqaq(code == 1 and "قَالَ\tقال\tمرشَّحٌ_واحد\tقَالَ\n" in out and "غول\tغول\tلا_حكم" in out.splitlines()
                 and "النتيجة الجامعة: لا حكم" in out, f"٩ التشكيل بهيكلٍ لا صورةَ له: خروج {code}")
    # ٨: بالمودَعات المختومة إن حضرت في MUDAA_DIR البيئة (فحصٌ بالمودَع بلا طفرة): الإعرابُ كاملٌ بـrabt
    M = os.environ.get("MUDAA_DIR")
    if M and all(os.path.exists(os.path.join(M, n)) for n in ("luzum_mujam.tsv", "jins.tsv", "mithal.tsv")):
        code, out = shaghghil("--qanat", "malik", "أَعْرِبْ كَتَبَ الطَّالِبُ الدَّرْسَ", bia=dict(os.environ))
        tahaqqaq(code == 0 and "j\tكَتَبَ الطَّالِبُ الدَّرْسَ\tمقبول" in out and "الطَّالِبُ\tفاعل\tرفع" in out
                 and "النتيجة الجامعة: حكمٌ صدر" in out, f"٨ rabt بالمودَع: خروج {code}")

    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        print(f"{najah} نجح، {len(fashal)} فشل")
        sys.exit(1)
    print(f"test_mudir: {najah} فحصًا نجح ({len(HALAT)} برومبتًا في القرار والخطّة)")


if __name__ == "__main__":
    main()
