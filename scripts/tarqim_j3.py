"""ترقيمُ ج3 الموحّد (قرار المالك 2026-10-18، 19:39؛ البروتوكول §٨).

الترقيمُ المعتمد: أسطرُ تحويل `scripts/tahwil_docx.py` لـ a2.docx المختوم (`360f7653…`)، فقرةً بسطر.
في المستودع ترقيمان قديمان لج3 (تحويلاتٌ مختلفةٌ لنفس الكتاب)؛ فلا يُترجَم رقمٌ قديمٌ برقمٍ — بل بنصّه:
لكلّ إحالةٍ «ج3 [س]N» يؤخذ أقربُ اقتباسٍ «…» في سطرها (أو السطرين التاليين)، ويُبحث بعد نزع التشكيل والتطويل
وتوحيد الهمزات في أسطر التحويل. المخرج تقريرٌ مقيس، لكلّ إحالة: الملفّ والسطر والرقم القديم والرقم الموحّد،
أو «بلا اقتباس» (لا يُترجم تخمينًا)، أو «لم يوجد»، أو «ملتبس» (الاقتباس في أكثر من سطر).
التشغيل: python3 -I scripts/tarqim_j3.py <a2.txt من tahwil_docx> [--tsv مخرج]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXT = (".lean", ".md", ".py", ".tsv")
SKIP = (".lake", ".git", "SLGE", "__pycache__")
REF = re.compile(r"ج3\s+(س)?(\d{2,4})")
QUOTE = re.compile(r"«([^«»]{6,})»")
TASHKIL = re.compile(r"[ً-ْٰـ]")


def norm(s):
    s = TASHKIL.sub("", s)
    s = re.sub("[أإآ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    s = re.sub(r"[^ء-ي ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    lines = [norm(l) for l in open(sys.argv[1], encoding="utf-8").read().split("\n")]
    if "--fahs" in sys.argv:
        # جدولُ المقابلة `hawkama/tarqim_j3.tsv`: كلُّ صفٍّ اقتباسُه في سطره الموحّد بعينه
        rows = [l.split("\t") for l in open(os.path.join(ROOT, "hawkama", "tarqim_j3.tsv"), encoding="utf-8").read().split("\n")[1:] if l]
        # والاقتباسُ فريدٌ في التحويل كلّه: وإلّا لم تُثبت المقابلةُ بالاقتباس (إزاحةُ الصفّ تمرّ)
        bad = [r for r in rows if [k + 1 for k, t in enumerate(lines) if norm(r[3]) in t] != [int(r[2])]]
        for r in bad:
            print("لا يطابق أو غير فريد:", "\t".join(r))
        print(f"المقابلة: {len(rows) - len(bad)}/{len(rows)} صفًّا اقتباسُه في سطره الموحّد وحده")
        sys.exit(1 if bad else 0)
    rows = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in sorted(fn):
            if not f.endswith(EXT) or f == "tarqim_j3.py":
                continue
            p = os.path.join(dp, f)
            src = open(p, encoding="utf-8").read().split("\n")
            for i, l in enumerate(src):
                for m in REF.finditer(l):
                    ctx = l[m.end():] + " " + " ".join(src[i + 1:i + 3])
                    q = QUOTE.search(ctx)
                    rel = os.path.relpath(p, ROOT)
                    old = (m.group(1) or "") + m.group(2)
                    if not q:
                        rows.append((rel, i + 1, old, "بلا اقتباس", ""))
                        continue
                    parts = [norm(x) for x in re.split(r"…|\.\.\.", q.group(1)) if len(norm(x)) >= 6]
                    key = max(parts, key=len) if parts else ""
                    hits = [k + 1 for k, t in enumerate(lines) if key and key in t]
                    if not hits:
                        rows.append((rel, i + 1, old, "لم يوجد", key[:40]))
                    elif len(hits) > 1:
                        rows.append((rel, i + 1, old, "ملتبس", ",".join(map(str, hits[:5]))))
                    else:
                        rows.append((rel, i + 1, old, "س" + str(hits[0]), key[:40]))
    from collections import Counter
    c = Counter("موحَّد" if r[3].startswith("س") else r[3] for r in rows)
    same = sum(1 for r in rows if r[3] == "س" + r[2].lstrip("س"))
    out = "\n".join("\t".join(map(str, r)) for r in rows)
    if "--tsv" in sys.argv:
        open(sys.argv[sys.argv.index("--tsv") + 1], "w", encoding="utf-8").write("milaf\tsatr\tqadim\tmuwahhad\tiqtibas\n" + out + "\n")
    else:
        print(out)
    print(f"الإحالات: {len(rows)} — " + "، ".join(f"{k} {v}" for k, v in c.items()) + f"؛ منها مطابقٌ رقمُه الموحّد بالفعل {same}")


if __name__ == "__main__":
    main()
