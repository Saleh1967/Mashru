# -*- coding: utf-8 -*-
"""يفحص cases.json على wasf.md: العدد، والتوزيع، وكون كلّ nass في سطره بالبايت، وkalima في مداه،
ونصفَ الجمل على الأقلّ لها masdar_jumla، وما يتبعها من الشروط الشكليّة. يخرج 1 عند أيّ خلل."""
import json, os, re, sys, collections

D = os.path.dirname(os.path.abspath(__file__))
L = {}
for f in ("qatr.txt", "alfiyya.txt"):
    with open(os.path.join(D, f), "rb") as h:
        L[f] = h.read().split(b"\n")
with open(os.path.join(D, "cases.json"), encoding="utf-8") as h:
    C = json.load(h)

err = []
def e(m): err.append(m)

QIYAM = {
    "hukm": {"مقبول", "خطأ"},
    "irab": {"رفع", "نصب", "جرّ", "جزم", "مبنيّ"},
    "quwwa": {"خبر مثبت", "خبر منفي", "تعليق", "إنشاء"},
}
TASHKIL = re.compile("[ً-ْٰ]")
def jarrad(s): return TASHKIL.sub("", s)
def satr_nass(f, n):
    s = L[f][n - 1].decode("utf-8")
    s = re.sub(r"ms\d+", "", s).replace("~~", "").lstrip("#").replace('"', "")
    return s

# العدد والمعرّفات
if len(C) != 100: e("العدد %d لا 100" % len(C))
ids = [x["id"] for x in C]
if ids != ["Q%03d" % i for i in range(1, 101)]: e("المعرّفات ليست Q001–Q100 بلا تكرار")
# التوزيع
nawc = collections.Counter(x["naw"] for x in C)
for n in ("hukm", "fail", "irab", "jidhr", "quwwa"):
    if nawc[n] != 20: e("النوع %s: %d لا 20" % (n, nawc[n]))
if set(nawc) - {"hukm", "fail", "irab", "jidhr", "quwwa"}: e("نوعٌ مجهول")
hk = collections.Counter(x["mutawaqqa"] for x in C if x["naw"] == "hukm")
if hk["مقبول"] != 10 or hk["خطأ"] != 10: e("hukm: %s" % dict(hk))

ghumud = 0; masdar = 0
jc = collections.Counter(x["jumla"] for x in C)
for x in C:
    i, j, n = x["id"], x["jumla"], x["naw"]
    w = j.split(" ")
    if "  " in j or j != j.strip() or any(not t for t in w): e(i + ": المسافات")
    if len(w) > 8: e(i + ": أكثر من ثماني كلمات")
    if re.search(r"[،؛؟.,;:!?\"'«»()]", j): e(i + ": علامة ترقيم")
    # kalima
    k = x["kalima"]
    if n in ("irab", "jidhr"):
        if not isinstance(k, int) or not (1 <= k <= len(w)): e(i + ": kalima خارج المدى")
    elif k is not None: e(i + ": kalima ليست null")
    # القيم
    m = x["mutawaqqa"]
    vals = m if isinstance(m, list) else [m]
    if isinstance(m, list):
        ghumud += 1
        if len(m) != 2 or m[0] == m[1]: e(i + ": الغموض بديلان")
    for v in vals:
        if n in QIYAM and v not in QIYAM[n]: e(i + ": قيمة %r" % v)
        if n == "fail" and v != "مستتر" and v not in w: e(i + ": الفاعل ليس كلمةً في الجملة")
        if n == "jidhr" and (len(v) not in (3, 4) or TASHKIL.search(v)): e(i + ": الجذر")
    # السند: كلّ nass قطعةٌ بالبايت من سطره
    if not x["sanad"]: e(i + ": بلا سند")
    for s in x["sanad"]:
        f, sn, t = s["milaf"], s["satr"], s["nass"]
        if f not in L or not (1 <= sn <= len(L[f])): e(i + ": سطر غير موجود"); continue
        if not t or t.encode("utf-8") not in L[f][sn - 1]: e(i + ": nass ليس في %s:%d" % (f, sn))
    # موضع المثال
    md = x["masdar_jumla"]
    if md is not None:
        masdar += 1
        f, sn = md["milaf"], md["satr"]
        nass = satr_nass(f, sn) + " " + (satr_nass(f, sn + 1) if sn < len(L[f]) else "")
        nass = re.sub(r"\s+", " ", nass)
        if jarrad(j) not in nass: e(i + ": الجملة ليست في %s:%d (بعد نزع الشكل)" % (f, sn))
    if not x["taliq"] or "\n" in x["taliq"]: e(i + ": taliq")

if masdar < 50: e("masdar_jumla %d أقلّ من 50" % masdar)
if ghumud > 10: e("الغموض %d فوق 10" % ghumud)
for j, c in jc.items():
    if c > 3: e("الجملة %r في %d حالات" % (j, c))

print("العدد:", len(C), "التوزيع:", dict(nawc), "hukm:", dict(hk))
print("من المصدرين:", masdar, "الغموض:", ghumud, "أكثر تكرار لجملة:", max(jc.values()))
if err:
    print("خلل %d:" % len(err)); [print(" ", m) for m in err]; sys.exit(1)
print("مرّ")
