"""اختبار جدول أوّليات العقل (مرشّح حتّى يُختم) ومطابقة `Aql/Awwaliyyat.lean` له (الأزمنة الخمسة بإثباتها ونفيها، وأسماء الأوّليات).

يُشغَّل حين يحضر الجدول (MUDAA_DIR وفيه awwaliyyat.tsv)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ الجدول الحاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه)، ونوعُه «معلومات-سابقة»، وحالتُه مختوم أو مرشّح (تُطبع).
٢. توقّعاتٌ مستقلّة: 17 صفًّا — 7 أوّليات (أ1–أ7) و10 صفوف زمن (ز0–ز9)؛ وكلُّ اقتباسٍ «…» بسطره (الكتاب/لسان العرب/المخصّص) موجودٌ في
   سطره في المودَع الحاضر بلفظه (ج1/ج3 مرشّحان لا يُفحصان هنا).
٣. Lean من النصّ (لا عبر Lean): الأزمنةُ الخمسة ز1–ز5 بصورتَي الإثبات والنفي في الجدول («فعل ↔ لم يفعل» …) تطابق `ithbat`/`nafy` في
   Awwaliyyat.lean زمنًا زمنًا بترتيب المنشئات؛ وصورتا الحال والمستقبل في الإثبات واحدة والنفيُ مختلف (التخليص بالنفي)؛ وصورتا جواب القسم
   في ز7 («لقد فعل ↔ ما فعل»، «ليفعلن ↔ لا يفعل») تطابق `ithbatQasam`/`nafyQasam` على الماضي المتّصل والمستقبل وحدَهما، ونفيُ القسم
   على الماضي المتّصل غيرُ نفيه بلا قسم (إسقاط الانتظار).
٤. كلُّ اسمٍ في عمود mirat_lean معرَّفٌ في Awwaliyyat.lean باسمه الكامل (def/theorem/structure/inductive في أوّل السطر)، والمنقوطُ منشئٌ
   في فضاء نوعه؛ و«(لم يُبنَ)» يُقبل إعلانًا لا اسمًا.
٥. النفيُ الخمسة (لم، لمّا، ما، لا، لن) مختلفٌ كلُّه في الجدول (لا يشترك زمنان في نفي) — توقّعٌ مستقلّ يطابق `nafy_yukhallis`.
التشغيل: python3 -I tahaqquq/test_awwaliyyat.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISM = "جدول أوّليات العقل"
ZAMAN = {"ز1": "madiMunqati", "ز2": "madiMuttasil", "ز3": "hal", "ز4": "mustaqbal", "ز5": "mustaqbalMunaffas"}

d = os.environ.get("MUDAA_DIR")
p = os.path.join(d, "awwaliyyat.tsv") if d else None
if not p or not os.path.exists(p):
    print("لم يُشغَّل (الجدول غير حاضر؛ عيّن MUDAA_DIR وفيه awwaliyyat.tsv)")
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
assert len(rows) == 17, len(rows)
aw = [r for r in rows if r["naw"] == "awwaliyya"]
zm = [r for r in rows if r["naw"] == "zaman"]
assert [r["ramz"] for r in aw] == ["أ1", "أ2", "أ3", "أ4", "أ5", "أ6", "أ7"]
assert [r["ramz"] for r in zm] == ["ز0", "ز1", "ز2", "ز3", "ز4", "ز5", "ز6", "ز7", "ز8", "ز9"]
src = {"الكتاب": "sibawayhi.txt", "لسان العرب": "lisan.txt", "المخصّص": "mukhassas.txt"}
nusus = {k: open(os.path.join(d, v), encoding="utf-8").read().split("\n") for k, v in src.items() if os.path.exists(os.path.join(d, v))}
pat = re.compile(r"(?:(الكتاب|لسان العرب|المخصّص|ج1|ج3) )?س(\d+)(?:–\d+)?: «([^»]+)»")
iqt = 0
for line in open(p, encoding="utf-8"):
    for cell in line.rstrip("\n").split("\t"):
        s0 = None
        for s, ln, q in pat.findall(cell):
            if s:
                s0 = s
            assert s0 is not None, (ln, q[:30], "اقتباس بلا مصدر")
            if s0 in nusus:
                assert q in nusus[s0][int(ln) - 1], (s0, ln, q[:40])
                iqt += 1
iqt_bayan = f"{iqt} اقتباسًا في سطره" if nusus else "لم تُفحص الاقتباسات (المودَعات النصّية غير حاضرة)"
ok += 1

# ٣ — الأزمنة الخمسة: «إثبات ↔ نفي» في عمود bayan
lean = open(os.path.join(ROOT, "Aql", "Awwaliyyat.lean"), encoding="utf-8").read()


def block(start, end):
    a = lean.index(start)
    return lean[a:lean.index(end, a)]


ithbat = dict(re.findall(r'\| \.(\w+) => "([^"]+)"', block("def ithbat : Zaman5 → String", "def nafy : Zaman5 → String")))
nafy = dict(re.findall(r'\| \.(\w+) => "([^"]+)"', block("def nafy : Zaman5 → String", "theorem ithbat_la_yukhallis")))
jadwal = {}
for r in zm:
    if r["ramz"] in ZAMAN:
        mm = re.search(r": ([^:↔]+?) ↔ ([^(؛]+?)(?: \(|؛|$)", r["bayan"])
        assert mm, r["bayan"]
        jadwal[ZAMAN[r["ramz"]]] = (mm.group(1).strip(), mm.group(2).strip())
assert set(jadwal) == set(ZAMAN.values()) == set(ithbat) == set(nafy), (set(jadwal), set(ithbat))
for z, (ith, nf) in jadwal.items():
    assert ithbat[z] == ith and nafy[z] == nf, (z, ith, nf, ithbat[z], nafy[z])
assert jadwal["hal"][0] == jadwal["mustaqbal"][0] and jadwal["hal"][1] != jadwal["mustaqbal"][1], "التخليص بالنفي"
# جوابُ القسم (ز7): الأزواج في الجدول تطابق `ithbatQasam`/`nafyQasam` (some) بترتيب المنشئات، ولا قسمَ على غيرهما (none)
qasam_rows = [r for r in zm if r["ramz"] == "ز7"]
assert len(qasam_rows) == 1
azwaj = re.findall(r"([^:؛]+?) ↔ ([^؛ —]+(?: [^؛ —]+)*)", qasam_rows[0]["bayan"].split(" — ")[0])
azwaj = [(a.strip(), b.strip()) for a, b in azwaj]
ith_q = re.findall(r'\| \.(\w+) => some "([^"]+)"', block("def ithbatQasam : Zaman5 → Option String", "def nafyQasam"))
nafy_q = re.findall(r'\| \.(\w+) => some "([^"]+)"', block("def nafyQasam : Zaman5 → Option String", "theorem qasam_ala_zamanayn"))
assert [z for z, _ in ith_q] == [z for z, _ in nafy_q] == ["madiMuttasil", "mustaqbal"], (ith_q, nafy_q)
assert azwaj == [(a, b) for (_, a), (_, b) in zip(ith_q, nafy_q)], (azwaj, ith_q, nafy_q)
assert "| _ => none" in block("def ithbatQasam", "def nafyQasam") and "| _ => none" in block("def nafyQasam", "theorem qasam_ala_zamanayn")
assert dict(nafy_q)["madiMuttasil"] != nafy["madiMuttasil"] and dict(nafy_q)["mustaqbal"] == nafy["mustaqbal"], "إسقاط الانتظار"
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

# ٥ — النفي الخمسة مختلفة
anfiya = [jadwal[z][1] for z in ZAMAN.values()]
assert len(set(anfiya)) == 5 and [a.split()[0] for a in anfiya] == ["لم", "لما", "ما", "لا", "لن"], anfiya
assert re.search(r"^theorem nafy_yukhallis\b", lean, re.M) and re.search(r"^theorem zaman5_hasira\b", lean, re.M)
for name in ("qasam_ala_zamanayn", "qasam_yusqit_intizar", "muhal_naqd", "mustaqim_hasan"):
    assert re.search(rf"^theorem {name}\b", lean, re.M), name
ok += 1
print(f"{ok}/5 — 17/17 صفًّا ({hala})، {iqt_bayan}، الأزمنة الخمسة بإثباتها ونفيها وصورتا القسم مطابقة لـ Lean، {len(asma)} اسمًا معرَّفًا، "
      f"النفي الخمسة مختلفة (لم/لمّا/ما/لا/لن)")
