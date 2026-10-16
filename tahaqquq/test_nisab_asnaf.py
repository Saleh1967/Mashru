"""اختبار جدول النِّسَب الثلاث على أصناف العوامل المئة (مرشّح حتّى يُختم) ومطابقة `Jisr/NisabAsnaf.lean` له.

يُشغَّل على الجدول حين يحضر (MUDAA_DIR وفيه nisab_asnaf.tsv)؛ وإلّا أُجريت فحوصُ نصّ Lean وحدها وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 16 صفًّا — 13 صنفًا، 3 قواعد؛ 28 اقتباسًا (21 من قطر الندى و2 من الكتاب و1 من الألفية بأسطرها تُفحص في سطرها من المودَعات
   المختومة الحاضرة، و4 من ج3 مرشّحٍ لا تُفحص)؛ وكلُّ «…» في عمود الشاهد إمّا قراءةُ البنّاء/تعيينُه/تعيينُ المالك وإمّا على نمط «المصدر سN: «…»».
٣. Lean من النصّ (لا عبر Lean): `semDawr` بحالاته الأربع (11/12 ← 2، 13 ← 4، 9/10 ← 0، وسائرُها semOf)، والمبرهناتُ السبع بأسمائها.
٤. عدٌّ مستقلّ من جدول المالك المولَّد `Jisr/AwamilJadwal.lean` (نصًّا) على تعيينٍ مكتوبٍ هنا يدويًّا مطابقٍ لتعيين Lean (الصنف ← نِسَبُه؛ الاستقلالُ
   في العدّ لا في التعيين): 57 إسنادية، 18 إضافية، 4 تقييدية (يا، أيا، هيا، آ)، 22 بلا نسبة — يطابق صفَّ الإحصاء في الجدول ونصَّ `ihsa_awamil`.
٥. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في NisabAsnaf.lean باسمه.
التشغيل: python3 -I tahaqquq/test_nisab_asnaf.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول النِّسَب الثلاث على الأصناف"

lean = open(os.path.join(ROOT, "Jisr", "NisabAsnaf.lean"), encoding="utf-8").read()
jadwal = open(os.path.join(ROOT, "Jisr", "AwamilJadwal.lean"), encoding="utf-8").read()

# ٤: التعيين اليدويّ المطابق لتعيين Lean (مستقلٌّ في العدّ لا في التعيين): الصنف ← نِسَبُ معمولاته
TAYIN = {1: {"إسنادية"}, 2: {"إسنادية"}, 3: {"إسنادية"}, 4: {"إسنادية"}, 5: {"إسنادية"}, 6: {"إسنادية"}, 7: {"إضافية"},
         8: set(), 9: {"إسنادية", "إضافية"}, 10: {"إسنادية"}, 11: set(), 12: set(), 13: {"تقييدية"}}


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


def ihsa_mustaqill():
    rows = re.findall(r'\("([^"]+)", (\d+), (true|false)\)', jadwal)
    assert len(rows) == 100, len(rows)
    n = {"إسنادية": 0, "إضافية": 0, "تقييدية": 0, "بلا": 0}
    nida = []
    for ism, c, _ in rows:
        s = TAYIN[int(c)]
        if not s:
            n["بلا"] += 1
        for x in s:
            n[x] += 1
        if int(c) == 13:
            nida.append(ism)
    return n, nida


def fahs_lean():
    sd = block("def semDawr ", "\n\n")
    for s in ("| 11 | 12 => 2", "| 13 => 4", "| 9 | 10 => 0", "| _ => semOf r"):
        assert s in sd, s
    for name in ("muwafiq_semOf", "jadwal_nisab", "kull_mamul_nisba", "idafiyya_jarr", "taqyidiyya_nida", "isnadiyya_asnaf", "ihsa_awamil"):
        assert re.search(rf"^theorem {name}\b", lean, re.M), name
    n, nida = ihsa_mustaqill()
    assert n == {"إسنادية": 57, "إضافية": 18, "تقييدية": 4, "بلا": 22}, n
    assert nida == ["يا", "أيا", "هيا", "آ"], nida
    ih = block("theorem ihsa_awamil", "by decide")
    assert "(awamilBi .isnadiyya).length = 57" in ih and "(awamilBi .idafiyya).length = 18" in ih
    assert "(awamilBi .taqyidiyya).length = 4" in ih and "nisabSinf g.2.1 = []).length = 22" in ih
    assert 'awamilBi .taqyidiyya = ["يا", "أيا", "هيا", "آ"]' in ih
    return n


d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "nisab_asnaf.tsv") if d else None
if not p or not os.path.exists(p):
    fahs_lean()
    print("لم يُشغَّل على الجدول (غير حاضر؛ عيّن MUDAA_DIR وفيه nisab_asnaf.tsv)؛ فحص نصّ Lean: semDawr بحالاته والمبرهنات السبع، والإحصاء المستقلّ "
          "من جدول المالك 57/18/4/22 يطابق نصّ ihsa_awamil")
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
assert len(rows) == 16, len(rows)
by = {}
for r in rows:
    by.setdefault(r["naw"], []).append(r)
assert {k: len(v) for k, v in by.items()} == {"sinf": 13, "qaida": 3}, {k: len(v) for k, v in by.items()}
nusus = {}
for ism, milaf in (("قطر الندى", "qatr.txt"), ("الكتاب", "sibawayhi.txt"), ("الألفية", "alfiyya.txt")):
    fp = os.path.join(d, milaf)
    if os.path.exists(fp):
        nusus[ism] = open(fp, encoding="utf-8").read().split("\n")
pat = re.compile(r"(?:(قطر الندى|ج3|الكتاب|الألفية) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = kj = 0
kq = {"قطر الندى": 0, "الكتاب": 0, "الألفية": 0}
for r in rows:
    s0 = None
    for seg in segs(r["shahid"]):
        if "«" not in seg:
            continue
        if seg.startswith(("قول المالك", "قراءة البنّاء", "تعيين البنّاء", "تعيين المالك")):
            continue
        found = pat.findall(seg)
        assert len(found) == seg.count("«"), ("اقتباس خارج النمط فلا يُفحص", r["ramz"], seg[:60])
        for s, ln, q in found:
            if s:
                s0 = s
            assert s0 in kq or s0 == "ج3", (ln, q[:30], "اقتباس بلا مصدر")
            if s0 == "ج3":
                kj += 1
                continue
            kq[s0] += 1
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
assert (kq, kj) == ({"قطر الندى": 21, "الكتاب": 2, "الألفية": 1}, 4), (kq, kj)   # توقّع مستقلّ (عدٌّ يدويّ صفًّا صفًّا)
iqt_bayan = f"{iqt} اقتباسًا في سطره من 24 (ج3 {kj} لا تُفحص)" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣، ٤
n = fahs_lean()
asnaf = [r["ramz"] for r in by["sinf"]]
assert [int(a.split()[0]) for a in asnaf] == list(range(1, 14)), asnaf
ih = by["qaida"][2]
assert ih["ramz"] == "الإحصاء" and all(x in ih["qima"] for x in ("57 إسنادية", "18 إضافية", "4 تقييدية (يا، أيا، هيا، آ)", "22 بلا معمول")), ih["qima"]
ok += 2   # ٣ و٤ كلاهما في fahs_lean

# ٥
asma = set()
for r in rows:
    for ident in [x.strip() for x in r["mirat_lean"].split(";") if x.strip()]:
        asma.add(ident)
for ident in asma:
    assert re.search(rf"^(def|theorem|structure|inductive) {re.escape(ident)}\b", lean, re.M), f"اسم في الجدول لا تعريف له في Lean: {ident}"
ok += 1
print(f"{ok}/5 — 16/16 صفًّا ({hala})، {iqt_bayan}، semDawr بحالاته والمبرهنات السبع، الإحصاء المستقلّ من جدول المالك "
      f"{n['إسنادية']}/{n['إضافية']}/{n['تقييدية']}/{n['بلا']} يطابق الجدول وLean، {len(asma)} اسمًا معرَّفًا")
