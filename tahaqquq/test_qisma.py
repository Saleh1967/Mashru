"""اختبارُ «جدول القسمة — القطعة الأولى»: `scripts/bina_qisma.py` و`Madlul/QismaJadwal.lean` و`Madlul/Qisma.lean`.

١. دائمًا، بلا مودَع:
   - `Madlul/QismaJadwal.lean` هو مخرجُ `bina_qisma.py --lean` بايتًا.
   - بصمةُ الجدول المولَّد هي بصمةُ «qisma.tsv» المختومة في `mudaat/sijill.json`.
   - توقّعاتٌ مكتوبةٌ باليد لا من الشيفرة: الجذورُ الأربعة، والنجومُ تحت الكواكب وحدها، و«ما وراء الكون» وحده غيرُ محسوس، وكلُّ صفٍّ سندُه قولُ
     المالك وسمُه يقول «قول المالك»، وكلُّ صفٍّ سندُه من a1.txt أو lisan.txt بادئتُه بصمتُهما المختومة.
   - مبرهناتُ `Madlul/Qisma.lean` بأسمائها في Audit.lean.
٢. بالمودَع (إن حضر في MUDAA_DIR): qisma.tsv بايتًا = المولَّد، وكلُّ نصٍّ في سطره من a1.txt وlisan.txt.
الطفرات: P1670–P1674 في tafrat.json.
التشغيل: python3 -I tahaqquq/test_qisma.py
"""
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


gen = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_qisma.py"), "--lean"],
                     capture_output=True, text=True)
lean = open(os.path.join(ROOT, "Madlul", "QismaJadwal.lean"), encoding="utf-8").read()
check(gen.returncode == 0 and gen.stdout == lean, "Madlul/QismaJadwal.lean ليس مخرجَ المولِّد")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bina_qisma as B  # noqa: E402

b = B.nass()
h = hashlib.sha256(b).hexdigest()
sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
mk = {m["milaf"]: m for m in sijill}
check(mk.get("qisma.tsv", {}).get("sha256") == h and mk["qisma.tsv"].get("hala") == "مختوم",
      f"بصمةُ الجدول {h[:12]} ليست بصمتَه المختومة")
check(mk.get("qisma.tsv", {}).get("naw") == "معلومات-سابقة", "نوعُ المودَع")

rows = [l.split("\t") for l in b.decode("utf-8").rstrip("\n").split("\n")[1:]]
asma = [r[1] for r in rows]
check([r[1] for r in rows if r[2] == ""] == ["الكون", "الإنسان", "الحياة", "ما وراء الكون"], "الجذور")
check([r[1] for r in rows if r[2] == "الكواكب"] == ["النجوم"], "ما تحت الكواكب")
check([r[1] for r in rows if r[3] == "لا"] == ["ما وراء الكون"], "غيرُ المحسوس")
check(all(r[2] == "" or r[2] in asma for r in rows), "أبٌ ليس في الجدول")
check(len(set(asma)) == len(asma) == 15, "الأسماء")
for r in rows:
    if "المالك" in r[4]:
        check("قول المالك" in r[6], f"صفّ {r[1]}: سندُه المالك ووسمُه لا يقوله")
    for part in r[4].split("؛ "):
        if part.startswith("a1.txt"):
            check(part.startswith("a1.txt " + mk["a1.txt"]["sha256"][:12] + "@"), f"صفّ {r[1]}: بادئة a1")
        if part.startswith("lisan.txt"):
            check(part.startswith("lisan.txt " + mk["lisan.txt"]["sha256"][:12] + "@"), f"صفّ {r[1]}: بادئة lisan")

audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
for t in ["hayy_iff", "la_tayin_la_mawdi", "shajara_sahiha", "asma_mutamayiza", "judhur", "ghayb_la_abna",
          "ghayb_la_tayin", "ahya", "ashya", "la_hukm"]:
    check(f"#print axioms Madlul.Qisma.{t}\n" in audit, f"Audit بلا {t}")

d = os.environ.get("MUDAA_DIR") or os.path.expanduser("~/mudaa_dir")
bil_mudaa = False
p = os.path.join(d, "qisma.tsv")
if os.path.exists(p):
    bil_mudaa = True
    check(open(p, "rb").read() == b, "qisma.tsv في المودَعات ليس المولَّد")
for milaf, n, q in B.NUSUS:
    f = os.path.join(d, milaf)
    if os.path.exists(f) and hashlib.sha256(open(f, "rb").read()).hexdigest() == mk[milaf]["sha256"]:
        check(q in open(f, encoding="utf-8").read().split("\n")[n - 1], f"«{q}» ليس في {milaf} س{n}")

if fails:
    print("\n".join(fails))
    print(f"جدول القسمة: فشل {len(fails)}")
    sys.exit(1)
print("جدول القسمة: نجح" + (" (بالمودَع)" if bil_mudaa else " (بلا مودَع)"))
