"""اختبار جدول المرساة (مرشّح حتّى يُختم) ومطابقة `Aql/Mirsat.lean` له (الآن وهنا، والمبهم هذا/ذاك، والحكم بالإزاحة وحدها).

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه mirsat.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها (منشئا المبهم، تعريفُ المسافة، أسماءُ المبرهنات) وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 12 صفًّا — 2 مرساة (الآن، هنا)، 4 قواعد، 2 شاهدان، 2 مبهم (هذا، ذاك)، 2 فحص لجدول المالك؛ وكلُّ «…» في عمود الشاهد إمّا
   قولُ المالك/قراءة البنّاء/تعيينه وإمّا على نمط «المصدر سN: «…»» موجودٌ في سطره في المودَع الحاضر بلفظه (الكتاب/لسان العرب).
٣. Lean من النصّ (لا عبر Lean): `Mubham` منشئاه hadha وdhaka بترتيب صفَّي المبهم؛ `masafa` مجموعُ القيم المطلقة للمحاور الثلاثة؛ `mubhamOf`
   بالقاعدة «≤ الحدّ → هذا وإلّا ذاك»؛ `hukmMubham none … = none`؛ `Mirsat` حقلاه `an : Int` و`huna : Izaha3`.
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Mirsat.lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر)، والمنقوطُ منشئٌ في فضاء
   نوعه؛ و«(لم يُبنَ)» يُقبل إعلانًا.
٥. من بنية الجدول: صفّا الفحص يذكران البابَ الصحيح س3000 والعددين 0؛ وصفّ «هنا» يسند «ظرف مكان» إلى اللسان لا إلى الكتاب.
التشغيل: python3 -I tahaqquq/test_mirsat.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول المرساة"

lean = open(os.path.join(ROOT, "Aql", "Mirsat.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def fahs_lean():
    m = re.search(r"^inductive Mubham \| (\w+) \| (\w+)", lean, re.M)
    assert m and m.groups() == ("hadha", "dhaka"), m
    assert "def masafa (v : Izaha3) : Nat := v.amudi.natAbs + v.ufuqi.natAbs + v.tuli.natAbs" in lean
    assert "if masafa (nisba r.huna x) ≤ hadd then .hadha else .dhaka" in lean
    assert "| none => none" in block("def hukmMubham", "\n\n")
    st = block("structure Mirsat where", "deriving")
    assert "an : Int" in st and "huna : Izaha3" in st, st
    for name in ("an_hal", "huna_la_jiha", "thabat_naql_zaman", "thabat_naql_jiha", "thabat_naql_istiqama", "naql_mirsat_zaman",
                 "naql_mirsat_jiha", "alyawm_bimanzilat_alan", "min_alan_ila_ghad", "huna_hadha", "taqrib_tabid", "bila_mirsat_la_hukm",
                 "thabat_naql_mubham", "la_qabl_wa_bad", "mustaqim_min_kull_mirsat"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name
    return m.groups()


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "mirsat.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه mirsat.tsv)؛ فحص نصّ Lean: المبهم ومسافته وقاعدته والمرساة والمبرهنات المسمّاة موجودة")
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
assert len(rows) == 12, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"mirsat": 2, "qaida": 4, "shahid": 2, "mubham": 2, "fahs": 2}, {k: len(v) for k, v in by.items()}
assert [r["ramz"] for r in by["mirsat"]] == ["الآن", "هنا"] and [r["ramz"] for r in by["mubham"]] == ["هذا", "ذاك"]
src = {"الكتاب": "sibawayhi.txt", "لسان العرب": "lisan.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(الكتاب|لسان العرب) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kull = 0
bimasdar = {}
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("قول المالك", "قراءة البنّاء", "تعيين البنّاء")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج النمط فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            kull += 1
            bimasdar[s0] = bimasdar.get(s0, 0) + 1
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
assert kull == 23 and bimasdar == {"الكتاب": 19, "لسان العرب": 4}, (kull, bimasdar)   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا)
iqt_bayan = f"{iqt} اقتباسًا في سطره من {kull}" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣
munsh = fahs_lean()
assert [r["ramz"] for r in by["mubham"]] == ["هذا", "ذاك"] and munsh == ("hadha", "dhaka")
assert "Mubham.hadha" in by["mubham"][0]["mirat_lean"] and "Mubham.dhaka" in by["mubham"][1]["mirat_lean"]
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
        found = c in munshiat.get(typ, set())
    else:
        found = re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M)
    assert found, f"اسم في الجدول لا تعريف له في Lean بهذا الاسم الكامل: {ident}"
ok += 1

# ٥
f3 = by["fahs"][0]
assert "س3000" in f3["shahid"] and "0 في الكتاب" in f3["shahid"] and "«أسماء الإشارة» 0" in f3["shahid"], f3["shahid"][-80:]
assert "لسان العرب س303598: «هنا: ظرف مكان" in by["mirsat"][1]["shahid"]
ok += 1
print(f"{ok}/5 — 12/12 صفًّا ({hala})، {iqt_bayan}، المبهم ومسافته وقاعدته والمرساة في Lean مطابقة، {len(asma)} اسمًا معرَّفًا، "
      f"صفّا فحص جدول المالك بموضعيهما")
