"""تمامُ التدقيق: كلُّ مبرهنةٍ عامّةٍ في وحدات المشروع تُطبع مسلّماتُها في Audit.lean.

سببُه: البند ٣ في البوّابة يعدّ ما في Audit.lean ويفحص مسلّماته، والبند ٤ يمنع نقصَ عدده؛ ولا شيء يمنع مبرهنةً جديدةً من أن تُبنى ولا
تُدقَّق. وكذلك بقيت 250 مبرهنةً عامّةً مبنيّةً خارج Audit.lean على da1ffa6، منها ثلاثٌ وسمتُها «مبرهن» وهي في `Madlul/Dalala.lean`
(قولُ المالك 2026-10-25، 23:07: «… وبعدها اكمل الربط وفق افضل الممارسات ليكون كل المشروع مترابط ومتناسق ومتكامل وفق افضل الممارسات»).

الطريقة: يقرأ ملفّات `.ilean` التي يكتبها `lake build` في `.lake/build/lib/lean` (أسماءُ التصريحات كاملةً بمواضعها)، ويعدّ التصريحَ مبرهنةً
إذا سبقت اسمَه في سطره الكلمةُ `theorem` أو `lemma`، وخاصًّا إذا كان في ما قبلها `private`. ويُشغَّل بعد `lake build` (البوّابة ١).
والوحداتُ: ما تحت SLGE وDal وMadlul وJisr وAql وNizam وFaahis وQari ممّا له ملفُّ مصدر.

ويرفض: مبرهنةً عامّةً ليس لها `#print axioms <اسمها>` في Audit.lean؛ وغيابَ البناء (لا `.ilean`)؛ ووحدةً مصدرُها موجود ولا `.ilean` لها.
التشغيل (بعد lake build): python3 -I tahaqquq/test_tadqiq_tamm.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari")
BUILD = os.path.join(ROOT, ".lake", "build", "lib", "lean")
KIND = re.compile(r"(?:^|\s)(theorem|lemma)\s+$")


def wahdat():
    out = []
    for d in DIRS:
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        for dirpath, _, files in os.walk(p):
            for f in sorted(files):
                if f.endswith(".lean"):
                    rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                    out.append(rel[:-5].replace(os.sep, "."))
    return sorted(out)


def mubarhanat(mod):
    """المبرهناتُ العامّة في الوحدة من .ilean، أو None إن غاب."""
    p = os.path.join(BUILD, *mod.split(".")) + ".ilean"
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding="utf-8"))
    src = open(os.path.join(ROOT, *mod.split(".")) + ".lean", encoding="utf-8").read().split("\n")
    out = []
    for name, pos in d["decls"].items():
        line, col = pos[4], pos[5]
        pre = src[line][:col] if line < len(src) else ""
        if not KIND.search(pre):
            continue
        if "private" in pre.split() or name.startswith("_private"):
            continue
        out.append(name)
    return sorted(out)


def main():
    fails = []
    audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
    mudaqqaq = set(re.findall(r"^#print axioms\s+(\S+)\s*$", audit, flags=re.M))
    if not os.path.isdir(BUILD):
        print("تمامُ التدقيق: لا بناء (.lake/build/lib/lean غائب)؛ شغّل lake build أوّلًا")
        sys.exit(1)
    kull, ghaib, bila_ilean = 0, [], []
    for mod in wahdat():
        ms = mubarhanat(mod)
        if ms is None:
            bila_ilean.append(mod)
            continue
        kull += len(ms)
        ghaib += [n for n in ms if n not in mudaqqaq]
    for mod in bila_ilean:
        fails.append(f"وحدةٌ بلا .ilean (لم تُبنَ؟): {mod}")
    for n in ghaib:
        fails.append(f"مبرهنةٌ عامّةٌ لا تُدقَّق في Audit.lean: {n}")
    if fails:
        print("\n".join(fails[:60]))
        if len(fails) > 60:
            print(f"… و{len(fails) - 60} غيرُها")
        print(f"تمامُ التدقيق: {len(ghaib)} مبرهنةً خارج Audit.lean من {kull}، و{len(bila_ilean)} وحدةً بلا بناء")
        sys.exit(1)
    print(f"تمامُ التدقيق: مرّ ({kull} مبرهنةً عامّةً في الوحدات، كلُّها في Audit.lean)")


if __name__ == "__main__":
    main()
