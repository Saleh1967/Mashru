"""اختبار جدول التجاور المكانيّ (مرشّح حتّى يُختم) ومطابقة `Aql/Makan.lean` له (الجهات الستّ بمحاورها وإشاراتها ونقائضها، ووحدات المسافة
وحدودها، وشواهد الكتاب بجهاتها ومقاديرها، و«وراء» من الأضداد).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه makan.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها (الجهات والنقائض والحدود وأسماء المبرهنات) وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 35 صفًّا — 6 جهات (ثلاثة أزواج على ثلاثة محاور، لكلّ جهة نقيضٌ على محورها بإشارة معكوسة)، 6 مرادفات، 1 مشترك (وراء
   بقرينته)، 3 وحدات، 12 شاهدًا، 7 قواعد؛ وكلُّ «…» في عمود الشاهد إمّا تعيين/قراءة البنّاء وإمّا على نمط «المصدر سN: «…»» موجودٌ في سطره في المودَع
   الحاضر بلفظه (الكتاب/لسان العرب).
٣. Lean من النصّ (لا عبر Lean): `Jiha.mihwar`/`Jiha.naqid`/`Jiha.ishara` تُقرأ من Makan.lean وتُطابَق بصفوف الجهات؛ `muradif` بصفوف المرادفات؛
   `hadd` بصفوف الوحدات؛ `jar` (الجيران الستّة: وحدةٌ واحدة على محور الجهة بإشارتها)؛ قائمةُ `shawahid` (اللفظ، الجهة الاختياريّة، المقدار)
   بصفوف الشواهد بترتيبها؛ و`hukmWara` (مكان خلف، ممرّ أمام، زمان لا حكم) و`maaniWara` = [خلف، أمام].
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Makan.lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر)، والمنقوطُ منشئٌ في
   فضاء نوعه أو دالّةٌ معرَّفة باسمها الكامل؛ و«(لم يُبنَ)» يُقبل إعلانًا.
٥. القاعدة من بنية الجدول: نقيضُ النقيض هو الجهة، والنقيضان على محورٍ واحد، وإشارتاهما متعاكستان؛ «وراء» إشارته «لا حكم»؛ الفرسخُ بعددين.
التشغيل: python3 -I tahaqquq/test_makan.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول التجاور المكانيّ"
J = {"فوق": "fawq", "تحت": "taht", "يمين": "yamin", "شمال": "shimal", "أمام": "amam", "خلف": "khalf"}
W = {"ذراع": "dhira", "ميل": "mil", "فرسخ": "farsakh"}

lean = open(os.path.join(ROOT, "Aql", "Makan.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def fahs_lean():
    """فحوصٌ على نصّ Lean لا تحتاج الجدول: الجهات ومحاورها ونقائضها وإشاراتها، والحدود، وأسماء المبرهنات."""
    mihwar = dict(re.findall(r"\| \.(\w+) => \.(\w+)", block("def Jiha.mihwar : Jiha → Mihwar", "/-- النقيض")))
    naqid = dict(re.findall(r"\| \.(\w+) => \.(\w+)", block("def Jiha.naqid : Jiha → Jiha", "/-- الإشارة")))
    ishara = {k: int(v) for k, v in re.findall(r"\| \.(\w+) => (-?\d+)", block("def Jiha.ishara : Jiha → Int", "/-- الجهةُ الموجبة"))}
    assert set(mihwar) == set(naqid) == set(ishara) == set(J.values()), (mihwar, naqid, ishara)
    for j in J.values():
        assert naqid[naqid[j]] == j and naqid[j] != j and mihwar[naqid[j]] == mihwar[j] and ishara[naqid[j]] == -ishara[j], j
    assert sorted(mihwar.values()) == ["amudi", "amudi", "tuli", "tuli", "ufuqi", "ufuqi"]
    hadd = {u: (int(a), int(b)) for u, a, b in re.findall(r"\| \.(\w+) => some \((\d+), (\d+)\)", block("def hadd : WahdaMakan → Option (Int × Int)", "\n\n"))}
    assert hadd == {"dhira": (1, 1), "mil": (4000, 4000), "farsakh": (12000, 24000)}, hadd
    ad = block("def ilaAdhru (n : Int) (u : WahdaMakan) : Option Int :=", "\n\n")
    assert "match hadd u with" in ad and "if a = b then some (a * n) else none" in ad, ad
    wara = re.findall(r"\.(\w+)", block("def maaniWara : List Jiha :=", "\n\n"))
    assert wara == ["khalf", "amam"], wara
    hw = dict(re.findall(r"\| \.(\w+) => (some \.\w+|none)", block("def hukmWara : Qarina → Option Jiha", "\n\n")))
    assert hw == {"makan": "some .khalf", "mamarr": "some .amam", "zaman": "none"}, hw
    jar = {j: tuple(int(x) for x in v.split(", ")) for j, v in re.findall(r"\| \.(\w+) => ⟨(-?\d+, -?\d+, -?\d+)⟩", block("def jar : Jiha → Izaha3", "\n\n"))}
    ax = {"amudi": 0, "ufuqi": 1, "tuli": 2}
    for j in J.values():   # الجارُ وحدةٌ واحدة على محور جهته بإشارتها، وصفرٌ على غيره — توقّعٌ مستقلّ
        v = jar[j]
        assert v[ax[mihwar[j]]] == ishara[j] and sum(abs(x) for x in v) == 1, (j, v)
    mur = re.findall(r'\("([^"]+)", \.(\w+)\)', block("def muradif : List (String × Jiha) :=", "theorem muradifat"))
    for name in ("naqid_naqid", "naqid_ghayr", "naqid_mihwar", "naqid_ishara", "jihat_sitt", "muradifat", "jiha_hasira", "aks_yunaqid",
                 "tanazur", "taaddi", "la_yajtami", "intiqal_marja", "jar_jiha", "jar_naqid", "mujawir_tabadul", "farsakh_la_hukm",
                 "shawahid_sibawayhi", "ghaya_tahfaz", "bila_marja_la_hukm", "jisr_wajhan", "wara_bil_qarina", "wara_wajhan"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name
    return mihwar, naqid, ishara, hadd, mur


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "makan.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه makan.tsv)؛ فحص نصّ Lean: الجهات الستّ بنقائضها وإشاراتها، والحدود 1/4000/12000–24000، والمبرهنات المسمّاة موجودة")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


def segs(cell):
    out, cur, depth, i = [], "", 0, 0
    while i < len(cell):
        c = cell[i]
        if c == "«":
            depth += 1
        elif c == "»":
            depth -= 1
        if depth == 0 and cell.startswith("؛ ", i):
            out.append(cur)
            cur = ""
            i += 2
            continue
        cur += c
        i += 1
    out.append(cur)
    return out


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح"), m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
hala = m["hala"]
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 35, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"jiha": 6, "muradif": 6, "mushtarak": 1, "wahda": 3, "shahid": 12, "qaida": 7}, {k: len(v) for k, v in by.items()}
assert [r["ramz"] for r in by["jiha"]] == ["فوق", "تحت", "يمين", "شمال", "أمام", "خلف"]
assert [r["ramz"] for r in by["wahda"]] == ["ذراع", "ميل", "فرسخ"]
src = {"الكتاب": "sibawayhi.txt", "لسان العرب": "lisan.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(الكتاب|لسان العرب) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kull = 0
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("تعيين البنّاء", "قراءة البنّاء", "قول المالك")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج النمط فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
assert kull == 95, kull   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا): 54 الكتاب، 41 لسان العرب
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull}" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣
mihwar, naqid, ishara, hadd, mur = fahs_lean()
for r in by["jiha"]:
    j = J[r["ramz"]]
    assert mihwar[j] == r["mihwar"] and ishara[j] == int(r["ishara"]) and naqid[j] == J[r["naqid"]], r["ramz"]
for r in by["wahda"]:
    u = W[r["ramz"]]
    a, bb = hadd[u]
    assert r["ishara"].startswith(str(a) if a == bb else f"{a}–{bb}"), (r["ramz"], r["ishara"], hadd[u])
sh = re.findall(r'\("([^"]+)", ⟨(none|some \.\w+), (none|some \((\d+), \.(\w+)\))⟩\)', block("def shawahid : List (String × Mawdi) :=", "theorem shawahid_sibawayhi"))
sh = [(s, j.replace("some .", "") if j != "none" else "—", (int(n), u) if n else None) for s, j, _, n, u in sh]
jadwal = [(r["ramz"], r["mihwar"], None if r["ishara"] == "—" else (int(r["ishara"].split()[0]), W[r["ishara"].split()[1]])) for r in by["shahid"]]
assert sh == jadwal, (sh, jadwal)
assert mur == [(r["ramz"], J[[k for k, v in J.items() if mihwar[v] == r["mihwar"] and ishara[v] == int(r["ishara"])][0]]) for r in by["muradif"]], mur
w0 = by["mushtarak"][0]
assert w0["ramz"] == "وراء" and w0["mihwar"] == "tuli" and "مكانًا خلف (-1)" in w0["ishara"] and "ممرًّا قدّام (1)" in w0["ishara"] and "زمانًا لا حكم" in w0["ishara"]
ok += 1

# ٤
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        if ident != "(لم يُبنَ)":
            asma.add(ident)
munshiat = {}
for typ, body in re.findall(r"^inductive (\w+) ((?:\| \w+ ?)+)", lean, re.M):
    munshiat[typ] = set(re.findall(r"\| (\w+)", body))
for ident in asma:
    if "." in ident:
        typ, c = ident.split(".", 1)
        found = c in munshiat.get(typ, set()) or re.search(rf"^def {re.escape(ident)}\b", lean, re.M)
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M)
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٥ — من بنية الجدول وحدها
tbl = {r["ramz"]: r for r in by["jiha"]}
for r in by["jiha"]:
    n = tbl[r["naqid"]]
    assert n["naqid"] == r["ramz"] and n["mihwar"] == r["mihwar"] and int(n["ishara"]) == -int(r["ishara"]), r["ramz"]
assert sorted(r["mihwar"] for r in by["jiha"]) == ["amudi", "amudi", "tuli", "tuli", "ufuqi", "ufuqi"]
assert "لا حكم" in by["wahda"][2]["ishara"] and "أو" in by["wahda"][2]["ishara"]
ok += 1
print(f"{ok}/5 — 35/35 صفًّا ({hala})، {iqt_bayan}، الجهات الستّ والمرادفات (6) والوحدات والجيران والشواهد (12) ووراء بقرينته في Lean مطابقة، "
      f"{len(asma)} اسمًا معرَّفًا، النقائض متعاكسة على محاورها")
