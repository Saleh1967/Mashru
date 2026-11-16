"""اختبارُ التواتر بشجرة النقل: `Madlul/NTP/Silsila.lean` و`Madlul/NTP/SilsilaMaajim.lean`.

١. دائمًا، بلا مودَع:
   - يقرأ الشجرةَ (`shajara`) والأسانيدَ (`asanid`) من نصّ Lean، ويطابق: لكلّ ضلعٍ سندٌ ولكلّ سندٍ ضلع، والملفّاتُ أربعةُ المعاجم المختومة في
     `mudaat/sijill.json`.
   - تنفيذٌ مستقلٌّ عن Lean للأسلاف والاستقلال والعدّ، بتوقّعاتٍ مكتوبةٍ باليد من الخُطَب: المقاييسُ والمخصّصُ يلتقيان في
     {العين 10، المصنف 11، غريب الحديث 12، الجمهرة 15} لا غير؛ والتاجُ غيرُ مستقلٍّ عن الثلاثة؛ واللسانُ مع المخصّص ومع المقاييس «لا حكم»؛
     والأربعةُ شاهدٌ واحد.
   - مبرهناتُ الملفّين بأسمائها في Audit.lean.
٢. بالمودَع (إن حضر MUDAA_DIR فيه الملفّاتُ الأربعة ببصماتها في السجلّ): كلُّ قطعةٍ في سطرها.
الطفرات: P1588–P1597 في tafrat.json.
التشغيل: python3 -I tahaqquq/test_tawatur.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


maajim = open(os.path.join(ROOT, "Madlul", "NTP", "SilsilaMaajim.lean"), encoding="utf-8").read()
silsila = open(os.path.join(ROOT, "Madlul", "NTP", "Silsila.lean"), encoding="utf-8").read()
audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]

ism = {k: int(v) for k, v in re.findall(r"^def (\w+) : Nat := (\d+)$", maajim, re.M)}
check(ism == {"mukhassas": 1, "lisan": 2, "maqayis": 3, "taj": 4, "waqud": 3}, f"أرقام الكتب {ism}")

shajara = {}
for name, lst in re.findall(r"if n = (\w+) then some \[([^\]]*)\]", maajim):
    shajara[ism[name]] = [int(x) for x in re.findall(r"\d+", lst)]
check(sorted(shajara) == [1, 2, 3, 4], f"عُقَد الشجرة المقروءة {sorted(shajara)}")

asanid = re.findall(r'⟨(\d+), (\d+), "([a-z]+\.txt)", (\d+), "([^"]+)"⟩', maajim)
check(len(asanid) == 52, f"الأسانيد {len(asanid)} لا 52")
adlaa = {(b, s) for b, l in shajara.items() for s in l}
sanad_adlaa = {(int(b), int(s)) for b, s, _, _, _ in asanid}
check(adlaa == sanad_adlaa, f"أضلاعٌ بلا سند {adlaa - sanad_adlaa}، وأسانيدُ بلا ضلع {sanad_adlaa - adlaa}")
milafat = {"mukhassas.txt": "المخصص", "lisan.txt": "لسان العرب", "maqayis.txt": "مقاييس اللغة", "taj.txt": "تاج العروس"}
mukhtum = {r["milaf"]: r for r in sijill if r.get("hala") == "مختوم"}
for f in {a[2] for a in asanid}:
    check(f in milafat and f in mukhtum and mukhtum[f]["ism"] == milafat[f], f"{f} ليس من المعاجم الأربعة المختومة")


def aslaf(n, k):
    if k == 0:
        return [n]
    out = [n]
    for s in shajara.get(n, []):
        out += aslaf(s, k - 1)
    return out


def maftuh(n, k):
    if k == 0 or n not in shajara:
        return True
    return any(maftuh(s, k - 1) for s in shajara[n])


def istiqlal(a, b, k=3):
    if set(aslaf(a, k)) & set(aslaf(b, k)):
        return "ghayr"
    if maftuh(a, k) or maftuh(b, k):
        return "laHukm"
    return "mustaqill"


def adad(ws, k=3):
    best = 0
    n = len(ws)
    for mask in range(1 << n):
        g = [ws[i] for i in range(n) if mask >> i & 1]
        if all(istiqlal(g[i], g[j], k) == "mustaqill" for i in range(len(g)) for j in range(i + 1, len(g))):
            best = max(best, len(g))
    return best


# توقّعاتٌ باليد من الخُطَب (لا من مخرج Lean)
check(set(aslaf(3, 3)) & set(aslaf(1, 3)) == {10, 11, 12, 15}, "ما التقى فيه المقاييس والمخصّص ليس {10، 11، 12، 15}")
tawaqqu = {(3, 1): "ghayr", (4, 2): "ghayr", (4, 1): "ghayr", (4, 3): "ghayr", (2, 1): "laHukm", (2, 3): "laHukm"}
for (a, b), v in tawaqqu.items():
    check(istiqlal(a, b) == v, f"الاستقلال ({a}، {b}) {istiqlal(a, b)} لا {v}")
check(adad([1, 2, 3, 4]) == 1 and adad([1, 2, 3]) == 1, "المعاجم ليست شاهدًا واحدًا")
check(istiqlal(1, 1) == "ghayr", "الكتاب مستقلٌّ عن نفسه")
check(istiqlal(2, 1, 0) == "laHukm", "الوقود صفر لا يعطي «لا حكم»")

# المبرهنات بأسمائها في Audit.lean
for f, ns in ((silsila, "NTP.Silsila"), (maajim, "NTP.SilsilaMaajim")):
    for n in re.findall(r"^theorem (\S+)", f, re.M):
        check(f"#print axioms {ns}.{n}\n" in audit, f"{ns}.{n} ليست في Audit.lean")

# بالمودَع
D = os.environ.get("MUDAA_DIR")
hadir = False
if D and all(os.path.isfile(os.path.join(D, f)) for f in milafat):
    hadir = True
    for f in milafat:
        b = open(os.path.join(D, f), "rb").read()
        if hashlib.sha256(b).hexdigest() != mukhtum[f]["sha256"]:
            fails.append(f"{f}: البصمة غير المختومة")
            continue
        L = b.decode("utf-8").split("\n")
        for _, _, milaf, satr, nass in asanid:
            if milaf == f:
                check(nass in L[int(satr) - 1], f"{f}:{satr} ليس فيه «{nass}»")

if fails:
    print("\n".join(fails))
    print(f"التواتر بشجرة النقل: {len(fails)} خلل")
    sys.exit(1)
print(f"التواتر بشجرة النقل: مرّ ({len(asanid)} سندًا، المعاجمُ الأربعة شاهدٌ واحد، المودَع {'حاضر' if hadir else 'غائب'})")
