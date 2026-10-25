"""يَسِم حالاتِ ضابط بقيّة أبواب الجزاء ببنود «ما هو تعيينُ البنّاء» في رأس Jisr/BaqiJaza.lean، بشرط كلّ بندٍ على حقول الحالة.

الشروطُ نقلٌ يدويٌّ لنصّ البنود (لا تقرأ الشفرة)، والإخفاقاتُ من حقل akhta في آخر سجلّ (natija_N.json). ويطبع جدولَ الملحق
(tahaqquq/dawabit/jaza2/mulhaq_1.md §٣): لكلّ بندٍ الحالاتُ التي تمسّه، وما أخفق منها بنوعه.
وحدُّه: الوسمُ بالحقول وحدها؛ والبندُ الذي لا حقلَ له لا يُوسم («الترتيبُ ليس في الحقول»، و«الشعرُ لا حكم ما لم يُذكر»: ذكرُ النطاق
الشعرَ ليس حقلًا). والوسمُ لا يقول إنّ الإخفاق من البند: الحالةُ تمسّ بنودًا، وسببُ إخفاقها في الملحق §٢.

التشغيل: python3 -I tahaqquq/dawabit/jaza2/wasm_taayin.py
"""
import json
import pathlib
import re

D = pathlib.Path(__file__).resolve().parent
HALAT = json.loads((D / "cases.json").read_text(encoding="utf-8"))
natayij = sorted(D.glob("natija_*.json"), key=lambda p: int(re.search(r"(\d+)\.json$", p.name).group(1)))
AKHIR = json.loads(natayij[-1].read_text(encoding="utf-8"))
NAW = {"naqsTaghtiya": "نقصُ تغطية", "tajawuz": "تجاوز", "qabulKhati": "قبولٌ خاطئ", "raddKhati": "ردٌّ خاطئ",
       "ikhtilafDaraja": "اختلافُ درجة", "ikhtiyar": "اختيار", "tawaqquf": "توقّف", "khata": "خطأ"}
AKHTA = {i: NAW[n] for i, _, n in AKHIR["akhta"]}

MAWSUL = {"من", "ما", "أي"}
HURUF = {"مهما", "متى", "حيثما", "أين", "أنى", "إن"}
GHAYR = {"كلما", "الذي", "كل", "أن", "أما"}
TALAB = {"طلب_أمر", "طلب_نهي", "طلب_استفهام", "طلب_تمن", "طلب_عرض", "معنى_أمر", "خبر_واجب"}
ARBAA = {"ناسخ", "حرف_ابتداء", "إذا_فجائية", "قسم"}
JAZMI = {"مجزوم", "منفي_بلا_مجزوم"}
JAZA = {"جزاء", "غير_معلن"}


def shir_masul(h):
    return h["kharij"]["shir"] != "غير_مسؤول"


def kalam(h):
    k = h["kharij"]["kalam"]
    return k if isinstance(k, list) else [k]


BUNUD = [
    ("الترتيبُ ليس في الحقول", "لا يُوسم (لا حقلَ له)"),
    ("الجوابُ المرفوعُ مع «من» و«ما» و«أي» مرادًا به الجزاء",
     lambda d, h: d["adat"] in MAWSUL and d["fil"] == "الجواب" and d["rabit"] == "بلا" and d["sura"] == "مرفوع"
     and d["shart"] == "مضارع" and d["mana"] in JAZA),
    ("الأصناف: ما لا يُجازى به جزمًا، وصدورُ الطلب", lambda d, h: d["adat"] in GHAYR | TALAB),
    ("أربعةٌ تذهب بالجزاء", lambda d, h: d["qabl"] in ARBAA and d["adat"] in MAWSUL | HURUF),
    ("ما قبل الأداة غيرُ الأربعة و«لكن» لا يغيّر الكلام",
     lambda d, h: d["qabl"] not in ARBAA | {"لا_شيء", "لكن"} and d["adat"] in MAWSUL | HURUF),
    ("«لكن»: الجزمُ بعدها بديلان", lambda d, h: d["qabl"] == "لكن"),
    ("الماضي بعد حرف الابتداء مقبولٌ شرطًا",
     lambda d, h: d["qabl"] == "حرف_ابتداء" and d["fil"] == "فعل_الشرط" and d["sura"] == "ماض"),
    ("الماضي شرطًا والجوابُ مرفوعًا (على القلب)",
     lambda d, h: d["shart"] == "ماض" and d["fil"] == "الجواب" and d["sura"] == "مرفوع" and d["rabit"] == "بلا"
     and d["mana"] in JAZA and d["qabl"] != "قسم" and d["adat"] in MAWSUL | HURUF),
    ("الجوابُ بحرف الجرّ بديلان", lambda d, h: d["qabl"] == "حرف_جر" and d["fil"] == "الجواب" and d["sura"] in JAZMI),
    ("الحالُ بعد الأمر مرفوعًا بديلان",
     lambda d, h: d["adat"] == "طلب_أمر" and d["fil"] == "جواب_الطلب" and d["sura"] == "مرفوع" and d["mana"] in {"حال", "غير_معلن"}),
    ("القسمُ ثمّ الماضي شرطًا والجوابُ مرفوعًا بديلان",
     lambda d, h: d["qabl"] == "قسم" and d["shart"] == "ماض" and d["fil"] == "الجواب" and d["sura"] == "مرفوع"),
    ("النهيُ مجزومًا جوابُه", lambda d, h: d["adat"] == "طلب_نهي" and d["fil"] == "جواب_الطلب" and d["rabit"] == "بلا"
     and d["sura"] in JAZMI),
    ("الخبرُ الواجبُ مجزومًا جوابُه خطأ", lambda d, h: d["adat"] == "خبر_واجب" and d["fil"] == "جواب_الطلب" and d["sura"] in JAZMI),
    ("«إذا» بلا إضمار في الشعر", lambda d, h: d["qabl"] == "إذا_فجائية" and d["sura"] in JAZMI and shir_masul(h)),
    ("«كلما» مجزومًا خطأ", lambda d, h: d["adat"] == "كلما" and d["sura"] in JAZMI),
    ("«أو» بعد الجواب مجزومًا، وبين المجزومين منصوبًا",
     lambda d, h: d["rabit"] == "أو" and ((d["fil"] == "بعد_الجواب" and d["sura"] in JAZMI)
                                         or (d["fil"] == "بين_المجزومين" and d["sura"] == "منصوب"))),
    ("الجوابُ المرفوعُ بعد «إن» في الشعر",
     lambda d, h: d["adat"] == "إن" and d["fil"] == "الجواب" and d["sura"] == "مرفوع" and d["shart"] == "مضارع" and shir_masul(h)),
    ("الواوُ مرفوعًا بين المجزومين حالًا أو بلا معنًى معلن",
     lambda d, h: d["fil"] == "بين_المجزومين" and d["rabit"] == "واو" and d["sura"] == "مرفوع" and d["mana"] in {"حال", "غير_معلن"}),
    ("الاستفهامُ مرفوعًا جوابُه", lambda d, h: d["adat"] == "طلب_استفهام" and d["fil"] == "جواب_الطلب" and d["sura"] == "مرفوع"),
    ("«لا ينبغي» محمولةً على خطأ",
     lambda d, h: d["qabl"] == "ناسخ" and d["adat"] in MAWSUL and d["fil"] in {"فعل_الشرط", "الجواب"} and d["sura"] in JAZMI
     and d["mana"] in JAZA),
    ("الشعرُ «لا حكم» ما لم يُذكر وهو غيرُ مقبولٍ في الكلام",
     "لا يُوسم (ذكرُ النطاق الشعرَ ليس حقلًا)؛ والمسؤولُ عنه في الشعر " +
     str(sum(1 for h in HALAT if shir_masul(h))) + " حالات، متوقَّعُها كلُّها: " +
     "، ".join(sorted({str(h["kharij"]["shir"]) for h in HALAT if shir_masul(h)}))),
]

print("| البند | الحالات |")
print("|---|---|")
for ism, shart in BUNUD:
    if isinstance(shart, str):
        print(f"| {ism} | {shart} |")
        continue
    ids = [h["id"] for h in HALAT if shart(h["dakhil"], h)]
    cells = [f"{i} (أخفقت: {AKHTA[i]})" if i in AKHTA else i for i in ids]
    print(f"| {ism} | {'، '.join(cells) if cells else '—'} |")
print(f"\nآخرُ سجلّ: {natayij[-1].name}؛ الإخفاقات: {', '.join(sorted(AKHTA))}")
