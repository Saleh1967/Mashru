"""اختبار جدول الأزمنة (مرشّح حتّى يُختم) ومطابقة `Aql/Azmina.lean` له (الوحدات ونسبها، أسماءُ الإزاحات بأعدادها ووحداتها وأزمنتها،
واستقامةُ الكلام عند سيبويه).

يُشغَّل حين يحضر الجدول (MUDAA_DIR وفيه azmina.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 25 صفًّا — 5 وحدات برتبها 0–4 (ساعة، يوم، أسبوع، شهر، سنة)، 16 اسمًا، 4 شواهد استقامة؛ وزمنُ كلّ اسم من إشارة
   عدده (سالب ماضٍ، صفر حال، موجب مستقبل)؛ وكلُّ «…» في عمود الشاهد إمّا قولُ المالك/قراءة البنّاء وإمّا على نمط «المصدر سN: «…»» موجودٌ
   في سطره في المودَع الحاضر بلفظه (لسان العرب/الكتاب/المخصّص؛ ج3 مرشّح لا يُفحص).
٣. Lean من النصّ (لا عبر Lean): قائمةُ `asma` تُقرأ من Azmina.lean وتُقوَّم بمقوِّمٍ مستقلّ صغير (⟨n, .u⟩، alAn .u، ams/ghad/alYawm/amAwwal/amQabil
   من تعاريفها، awwalMin = −1، bad = +1) فتطابق صفوفَ الأسماء اسمًا وعددًا ووحدةً بترتيبها؛ ونِسَبُ التحويل في `ilaAyyam`/`ilaAshhur`/`ilaSaat`
   (الأسبوع 7، السنة 12، اليوم 24، الأسبوع 168 ساعة) تطابق عمودَ adad في صفوف الوحدات؛ والشهرُ بالأيام غيرُ معرَّف في `ilaAyyam` (لا حكم).
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Azmina.lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر)، والمنقوطُ منشئٌ في
   فضاء نوعه أو حقلٌ/دالّةٌ معرَّفة باسمها الكامل.
٥. شواهدُ الاستقامة: الزمنُ المحكوم في عمود zaman («مستقيم»/«محال») يطابق توافقَ إشارة العدد مع زمن الفعل المذكور قبل «↔» — توقّعٌ
   مستقلّ عن `yastaqim`.
التشغيل: python3 -I tahaqquq/test_azmina.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول الأزمنة"
WAHDAT = ["saa", "yawm", "usbu", "shahr", "sana"]

d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "azmina.tsv") if d else None
if not p or not os.path.exists(p):
    print("لم يُشغَّل (الجدول غير حاضر؛ عيّن MUDAA_DIR وفيه azmina.tsv)")
    sys.exit(0)


def tsv(path):
    lines = [l for l in open(path, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, l.split("\t"))) for l in lines[1:]]


sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
m = next(x for x in sijill if x["ism"] == ISM)
assert m["naw"] == "معلومات-سابقة" and m["hala"] in ("مختوم", "مرشح"), m
b = hashlib.sha256(open(p, "rb").read()).hexdigest()
assert b == m["sha256"], f"{ISM}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
hala = m["hala"]
ok = 1

# ٢
rows = tsv(p)
assert len(rows) == 25, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"wahda": 5, "ism": 16, "istiqama": 4}, {k: len(v) for k, v in by.items()}
assert [(r["ramz"], r["wahda"], r["zaman"]) for r in by["wahda"]] == \
    [("ساعة", "saa", "0"), ("يوم", "yawm", "1"), ("أسبوع", "usbu", "2"), ("شهر", "shahr", "3"), ("سنة", "sana", "4")]
for r in by["ism"]:
    n = int(r["adad"])
    assert r["wahda"] in WAHDAT and r["zaman"] == ("ماضٍ" if n < 0 else "حال" if n == 0 else "مستقبل"), (r["ramz"], n, r["zaman"])
src = {"لسان العرب": "lisan.txt", "الكتاب": "sibawayhi.txt", "المخصّص": "mukhassas.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(لسان العرب|الكتاب|المخصّص|ج3) )?س(\d+)(?:–\d+)?: «([^»]+)»")


def segs(cell):
    """تقطيع خليّة الشاهد على «؛ » خارج الأقواس «…» فقط (فقد يقع الفاصل داخل الاقتباس)."""
    out, cur, depth = [], "", 0
    i = 0
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


iqt = kull = 0
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("قول المالك", "قراءة البنّاء", "وقراءة البنّاء")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج نمط «المصدر سN: «…»» فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
assert kull == 31, kull   # توقّع مستقلّ (عدٌّ يدويّ): 22 لسان العرب، 7 الكتاب، 1 المخصّص، 1 ج3؛ وقول المالك وقراءة البنّاء بلا سطر
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull} (ج3 لا يُفحص)" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣ — Lean من النصّ
lean = open(os.path.join(ROOT, "Aql", "Azmina.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def lit(expr):
    """مقوِّم مستقلّ لإزاحةٍ مكتوبة في Lean → (عدد، وحدة)."""
    expr = expr.strip()
    mm = re.fullmatch(r"⟨(-?\d+), \.(\w+)⟩", expr)
    if mm:
        return int(mm.group(1)), mm.group(2)
    mm = re.fullmatch(r"alAn \.(\w+)", expr)
    if mm:
        return 0, mm.group(1)
    mm = re.fullmatch(r"awwalMin \((.+)\)|awwalMin (\w+)", expr)
    if mm:
        n, u = lit(mm.group(1) or mm.group(2))
        return n - 1, u
    mm = re.fullmatch(r"bad \((.+)\)|bad (\w+)", expr)
    if mm:
        n, u = lit(mm.group(1) or mm.group(2))
        return n + 1, u
    dm = re.search(rf"^def {re.escape(expr)} : Izaha := ⟨(-?\d+), \.(\w+)⟩", lean, re.M)
    assert dm, f"تعبير لا يقوَّم: {expr}"
    return int(dm.group(1)), dm.group(2)


asma_src = block("def asma : List (String × Izaha) :=", "theorem asma_azmina")
asma = [(name, lit(e)) for name, e in re.findall(r'\("([^"]+)", ([^()\n]+?(?:\([^()]*\))?[^()\n]*?)\)(?=,|\])', asma_src)]
jadwal = [(r["ramz"], (int(r["adad"]), r["wahda"])) for r in by["ism"]]
assert asma == jadwal, (asma, jadwal)
nisab = {}
for fn in ("ilaAyyam", "ilaAshhur", "ilaSaat"):
    body = block(f"def {fn} : Izaha → Option Int", "\n\n")
    for u, k in re.findall(r"\| ⟨n, \.(\w+)⟩ => some \((\d+) \* n\)", body):
        nisab[(fn, u)] = int(k)
    for u in re.findall(r"\| ⟨n, \.(\w+)⟩ => some n\n", body):
        nisab[(fn, u)] = 1
    assert "| _ => none" in body, fn
assert nisab == {("ilaAyyam", "yawm"): 1, ("ilaAyyam", "usbu"): 7, ("ilaAshhur", "shahr"): 1, ("ilaAshhur", "sana"): 12,
                 ("ilaSaat", "saa"): 1, ("ilaSaat", "yawm"): 24, ("ilaSaat", "usbu"): 168}, nisab
w = {r["ramz"]: r["adad"] for r in by["wahda"]}
assert w["أسبوع"].startswith("7 ") and w["سنة"].startswith("12 ") and w["يوم"].startswith("24 ") and w["شهر"].startswith("لا حكم"), w
assert ("ilaAyyam", "shahr") not in nisab and ("ilaAyyam", "sana") not in nisab
ok += 1

# ٤
asma_lean = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        asma_lean.add(ident)
munshiat = {}
for typ, body in re.findall(r"^inductive (\w+) ((?:\| \w+ ?)+)", lean, re.M):
    munshiat[typ] = set(re.findall(r"\| (\w+)", body))
for ident in asma_lean:
    if "." in ident:
        typ, c = ident.split(".", 1)
        found = c in munshiat.get(typ, set()) or re.search(rf"^def {re.escape(ident)}\b", lean, re.M)
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M)
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٥ — الاستقامة من بنية الجدول: زمن الفعل قبل «↔» وإشارة العدد
Z = {"ماضٍ منقطع": -1, "ماضٍ متّصل": -1, "حال": 0, "مستقبل": 1, "مستقبل منفَّس": 1}
for r in by["istiqama"]:
    fil, hukm = r["zaman"].split(" ↔ ")
    n = int(r["adad"])
    sign = -1 if n < 0 else 0 if n == 0 else 1
    expected = "مستقيم" if Z[fil] == sign else "محال"
    assert hukm.endswith(expected), (r["ramz"], r["zaman"], expected)
assert [r["zaman"].split(": ")[-1] for r in by["istiqama"]] == ["مستقيم", "مستقيم", "محال", "محال"]
for name in ("mustaqim_hasan_ams_ghad", "muhal_ghad_ams", "la_yastaqim_maan", "zaman_hasir", "aks_yaqlib", "kull_ams_mada_lan_yaud"):
    assert re.search(rf"^theorem {name}\b", lean, re.M), name
ok += 1
print(f"{ok}/5 — 25/25 صفًّا ({hala})، {iqt_bayan}، أسماء الإزاحات (16) ونسب الوحدات في Lean مطابقة، {len(asma_lean)} اسمًا معرَّفًا، "
      f"الاستقامة 2 والمحال 2")
