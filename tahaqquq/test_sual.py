"""تجربةُ الجواب (tahaqquq/dawabit/sual/): حارسُ التجميد والعدّ، بلا مودَع.

**وسمُ التوقّعات.** كلُّ توقّعٍ هنا من نصّ `wasf.md` (المواصفة المجمَّدة ببصمتها في `tajmid.json`) أو من البصمات المسجَّلة، لا من مخرج
المحوِّل؛ وكتبه البنّاءُ بعد التشغيل الأوّل، فهو حارسٌ لا «مفحوص» بمؤلّفٍ مستقلّ. والنتيجةُ نفسُها (32 صوابًا من 100) «موافقةُ قراءتين على
حالاتٍ مؤلَّفة» كما في المواصفة، لا «مقيس».
١. البصمات: `cases.json` و`tashghil.py` و`wasf.md` و`fahs_cases.py` و`bina_cases.py` و`taalif.md` بايتاتُها بصماتُها في `tajmid.json`، و`cases_sha256`
   و`tashghil_sha256` في `natija_1.json` هما هما (لم يتغيّر شيءٌ بعد التجميد ولا بعد التشغيل).
٢. شروطُ الحالات الشكليّة من المواصفة (§الحالة، §ما لا يُسأل عنه)، بتنفيذٍ مستقلٍّ عن `fahs_cases.py` (وذاك يحتاج المصدرين غيرَ المودَعين).
٣. العدّ: نتائجُ `natija_1.json` هي الحالاتُ بأعيانها وترتيبها ونوعها، وأعدادُ `kull` و`ala_naw` و`sawab_min_100` و`sawab_mimma_ajab` تُعاد من النتائج.
٤. الأصناف: كلُّ `sinf` يُعاد من (`mutawaqqa`، `jawab`) بقواعد §العدّ في المواصفة.
٥. المحوِّل على مخرجٍ مكتوبٍ باليد بصيغة جدول §العدّ: الحكمُ من الحقل الثالث، والمسندُ إليه، والإعراب، والجذر، والقوّة، ولا جوابَ لغير المرخَّص.
الطفرات: P1634 (المحوِّل يبدّل «اختيار بلا مرجّح» و«خطأ»): يقتلها أوّلًا ٦ في test_sabq_tajmid.py (بصمةُ المحوِّل الآن، ت٢) ثمّ ١ هنا.
التشغيل: python3 -I tahaqquq/test_sual.py
"""
import collections
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
D = JADHR / "tahaqquq" / "dawabit" / "sual"

najah = 0
fashal = []


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def basma(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    tajmid = json.loads((D / "tajmid.json").read_text(encoding="utf-8"))
    natija = json.loads((D / "natija_1.json").read_text(encoding="utf-8"))
    cases = json.loads((D / "cases.json").read_text(encoding="utf-8"))

    # ١
    for f, k in (("cases.json", "cases_sha256"), ("tashghil.py", "tashghil_sha256"), ("wasf.md", "wasf_sha256"),
                 ("fahs_cases.py", "fahs_cases_sha256"), ("bina_cases.py", "bina_cases_sha256"), ("taalif.md", "taalif_sha256")):
        tahaqqaq(basma(D / f) == tajmid.get(k), f"١ {f}: بصمتُه غيرُ {k} في tajmid.json")
    tahaqqaq(natija.get("cases_sha256") == tajmid.get("cases_sha256"), "١ cases_sha256 في natija_1.json غيرُه في tajmid.json")
    tahaqqaq(natija.get("tashghil_sha256") == tajmid.get("tashghil_sha256"), "١ tashghil_sha256 في natija_1.json غيرُه في tajmid.json")

    # ٢
    QIYAM = {"hukm": {"مقبول", "خطأ"}, "irab": {"رفع", "نصب", "جرّ", "جزم", "مبنيّ"},
             "quwwa": {"خبر مثبت", "خبر منفي", "تعليق", "إنشاء"}}
    tahaqqaq(len(cases) == 100, f"٢ عددُ الحالات {len(cases)}")
    tahaqqaq([c["id"] for c in cases] == [f"Q{i:03d}" for i in range(1, 101)], "٢ المعرّفات Q001–Q100 بترتيبها")
    tahaqqaq(collections.Counter(c["naw"] for c in cases) == {n: 20 for n in ("hukm", "fail", "irab", "jidhr", "quwwa")},
             "٢ عشرون لكلّ نوع")
    hk = collections.Counter(c["mutawaqqa"] for c in cases if c["naw"] == "hukm" and isinstance(c["mutawaqqa"], str))
    tahaqqaq(hk == {"مقبول": 10, "خطأ": 10}, f"٢ الحكم عشرٌ وعشر: {dict(hk)}")
    gh = sum(isinstance(c["mutawaqqa"], list) for c in cases)
    tahaqqaq(gh <= 10, f"٢ الغموض {gh} > 10")
    tahaqqaq(sum(c.get("masdar_jumla") is not None for c in cases) >= 50, "٢ نصفُ الجمل على الأقلّ من المصدرين")
    jumal = collections.Counter(c["jumla"] for c in cases)
    tahaqqaq(max(jumal.values()) <= 3, "٢ جملةٌ مكرَّرةٌ في أكثر من ثلاث حالات")
    for c in cases:
        k, n, m = c.get("kalima"), c["naw"], c["mutawaqqa"]
        kalimat = c["jumla"].split(" ")
        tahaqqaq(len(kalimat) <= 8 and "  " not in c["jumla"], f"٢ {c['id']}: أكثرُ من ثماني كلمات أو مسافةٌ مزدوجة")
        if n in ("irab", "jidhr"):
            tahaqqaq(isinstance(k, int) and 1 <= k <= len(kalimat), f"٢ {c['id']}: kalima خارج مداها")
        else:
            tahaqqaq(k is None, f"٢ {c['id']}: kalima في غير irab وjidhr")
        qiyam = m if isinstance(m, list) else [m]
        tahaqqaq(not isinstance(m, list) or len(m) == 2, f"٢ {c['id']}: الغموضُ بديلان")
        if n in QIYAM:
            tahaqqaq(all(q in QIYAM[n] for q in qiyam), f"٢ {c['id']}: قيمةٌ خارج قيم {n}: {m}")
        if n == "jidhr":
            tahaqqaq(all(re.fullmatch("[ء-ي]{3,4}", q) for q in qiyam), f"٢ {c['id']}: الجذرُ ثلاثةُ أحرفٍ أو أربعة بلا شكل: {m}")
        if n == "fail":
            tahaqqaq(all(q == "مستتر" or q in kalimat for q in qiyam), f"٢ {c['id']}: المسندُ إليه ليس كلمةً من الجملة: {m}")
        tahaqqaq(bool(c.get("sanad")) and all({"milaf", "satr", "nass"} <= set(s) for s in c["sanad"]), f"٢ {c['id']}: سندٌ ناقص")

    # ٣
    nataij = natija["nataij"]
    tahaqqaq([(x["id"], x["naw"]) for x in nataij] == [(c["id"], c["naw"]) for c in cases], "٣ النتائجُ غيرُ الحالات بترتيبها ونوعها")
    kull = collections.Counter(x["sinf"] for x in nataij)
    tahaqqaq(dict(kull) == natija["kull"], f"٣ kull: {dict(kull)} لا {natija['kull']}")
    ala = {}
    for x in nataij:
        ala.setdefault(x["naw"], collections.Counter())[x["sinf"]] += 1
    tahaqqaq({k: dict(v) for k, v in ala.items()} == natija["ala_naw"], "٣ ala_naw لا يُعاد من النتائج")
    tahaqqaq(natija["sawab_min_100"] == kull["صواب"], "٣ sawab_min_100")
    tahaqqaq(natija["sawab_mimma_ajab"] == [kull["صواب"], len(nataij) - kull["نقص تغطية"]], "٣ sawab_mimma_ajab")

    # ٤: قواعدُ §العدّ — صواب: الجوابُ المتوقَّعُ بعينه (أو البديلان بعينهما)؛ نقص تغطية: لا جواب؛
    #    اختيار بلا مرجّح: مجموعةٌ فيها المتوقَّع وغيرُه؛ خطأ: جوابٌ ليس فيه المتوقَّع.
    def sinf(m, j):
        mt, j = (set(m) if isinstance(m, list) else {m}), set(j)
        if not j:
            return "نقص تغطية"
        if j == mt:
            return "صواب"
        if mt < j:
            return "اختيار بلا مرجّح"
        return "خطأ" if not (mt & j) or len(mt) > 1 else "اختيار بلا مرجّح"
    for c, x in zip(cases, nataij):
        tahaqqaq(sinf(c["mutawaqqa"], x["jawab"]) == x["sinf"], f"٤ {c['id']}: {x['sinf']} لا {sinf(c['mutawaqqa'], x['jawab'])}")

    # ٥: المحوِّل على مخرجٍ بصيغة جدول §العدّ (مكتوبٍ باليد)
    spec = importlib.util.spec_from_file_location("tashghil_sual", D / "tashghil.py")
    t = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(t)
    makhraj = ("j\tكَتَبَ زَيْدٌ\tمقبول\n"
               "  كَتَبَ\tالفعل\tمبنيّ\n"
               "  زَيْدٌ\tالفاعل\tرفع\n"
               "  الإسناد: الفعل «كَتَبَ» والمسند إليه «زَيْدٌ»\n"
               "  الدلالة: «كَتَبَ» مرشَّحُ جذره كتب من اللسان\n"
               "  القوّة: خبرٌ مثبت — من الصدر\n")
    hukm, jism = t.qira(makhraj, "كَتَبَ زَيْدٌ")
    tahaqqaq(hukm == "مقبول", f"٥ الحكم: {hukm!r}")
    for naw, k, tawaqqu in (("hukm", None, {"مقبول"}), ("fail", None, {"زَيْدٌ"}), ("irab", 2, {"رفع"}), ("irab", 1, {"مبنيّ"}),
                            ("jidhr", 1, {"كتب"}), ("quwwa", None, {"خبر مثبت"})):
        j = t.jawab(naw, k, "كَتَبَ زَيْدٌ", hukm, jism)
        tahaqqaq(j == tawaqqu, f"٥ {naw} {k}: {j}")
    j = t.jawab("fail", None, "قَامَ", "مقبول", ["  الإسناد: الفعل «قَامَ» والمسند إليه ضميرٌ مستتر"])
    tahaqqaq(j == {"مستتر"}, f"٥ المستتر: {j}")
    for h in ("لا_حكم", "خطأ"):
        tahaqqaq(t.jawab("irab", 2, "كَتَبَ زَيْدٌ", h, jism) == set(), f"٥ {h}: لا جوابَ في غير hukm")
    tahaqqaq(t.jawab("hukm", None, "x", "لا_حكم", []) == set(), "٥ «لا_حكم» في hukm لا جواب")

    if fashal:
        print("\n".join("FAIL " + x for x in fashal[:40]))
        print(f"{najah} نجح، {len(fashal)} فشل")
        sys.exit(1)
    print(f"test_sual: {najah} فحصًا نجح (100 حالة؛ النتيجة الأولى {natija['sawab_min_100']} صوابًا من 100، موافقةُ قراءتين)")


if __name__ == "__main__":
    main()
