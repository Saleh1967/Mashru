"""اختبار النقول في Jisr/AqsamAwamil.lean (`naql`): كلُّ اقتباسٍ موجودٌ بلفظه في سطره من مودَعه المختوم.

يُشغَّل حين يحضر مجلّد المودَعات (MUDAA_DIR وفيه mughni.txt وjanadani.txt وalfiyya.txt وsibawayhi.txt)؛ وإلّا طُبع «لم يُشغَّل» وخرج 0.
١. بصمةُ كلّ مودَعٍ حاضر هي بصمتُه في mudaat/sijill.json (وإلّا رُفض باسمه).
٢. يُقرأ جدول `naql` من ملفّ Lean بالنصّ (لا عبر Lean) — ⟨"العامل", الصنف, .القسم, .المودَع, السطر, "الاقتباس", استدلال?⟩ — ويُفحص
   أنّ الاقتباس جزءٌ من سطره في المودَع بعد حذف علامات OpenITI في أوّل السطر (`# `، `~~`، `### | `، `# | `) لا غير.
٣. توقّعاتٌ مستقلّة عن Lean: 56 نقلًا، ولا سطرَ خارج المودَع، ولا اقتباسَ أقصر من ثمانية أحرف.
التشغيل: python3 -I tahaqquq/test_aqsam.py
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MILAFFAT = {"mughni": ("مغني اللبيب", "mughni.txt"), "janadani": ("الجنى الداني في حروف المعاني", "janadani.txt"),
            "alfiyya": ("ألفية ابن مالك", "alfiyya.txt"), "sibawayhi": ("كتاب سيبويه", "sibawayhi.txt")}

d = os.environ.get("MUDAA_DIR")
if not d or not all(os.path.exists(os.path.join(d, f)) for _, f in MILAFFAT.values()):
    print("لم يُشغَّل (المودَعات غير حاضرة؛ عيّن MUDAA_DIR)")
    sys.exit(0)

sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
nusus = {}
for k, (ism, f) in MILAFFAT.items():
    m = next(x for x in sijill if x["ism"] == ism)
    assert m["hala"] == "مختوم", m
    b = hashlib.sha256(open(os.path.join(d, f), "rb").read()).hexdigest()
    assert b == m["sha256"], f"{ism}: تغيّرت بصمته {b[:16]} ≠ {m['sha256'][:16]}"
    nusus[k] = open(os.path.join(d, f), encoding="utf-8").read().split("\n")
ok = 1

lean = open(os.path.join(ROOT, "Jisr", "AqsamAwamil.lean"), encoding="utf-8").read()
tab = lean[lean.index("def naql : List Naql := ["):]
tab = tab[:tab.index("\n]")]
rows = re.findall(r'⟨"((?:[^"\\]|\\.)*)", (\d+), \.(\w+), \.(\w+), (\d+), "((?:[^"\\]|\\.)*)", (true|false)⟩', tab)
assert len(rows) == 56, len(rows)
ok += 1

def tanzif(line):
    return re.sub(r"^(# \| |# |~~|### \| )", "", line)

ghalat = []
for amil, sinf, qism, mudaa, satr, iqtibas, istidlal in rows:
    iq = iqtibas.replace('\\"', '"')
    assert len(iq) >= 8, (amil, iq)
    n = int(satr)
    assert 1 <= n <= len(nusus[mudaa]), (amil, mudaa, n)
    if iq not in tanzif(nusus[mudaa][n - 1]):
        ghalat.append((amil, mudaa, n, iq))
assert not ghalat, ghalat
ok += 1
print(f"{ok}/3 — {len(rows)}/56 اقتباسًا في مواضعها")
