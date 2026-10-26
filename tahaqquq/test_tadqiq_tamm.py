"""تمامُ التدقيق: كلُّ مبرهنةٍ عامّةٍ في وحدات المشروع (تصريحٌ تسبق اسمَه في سطره `theorem` أو `lemma`) تُطبع مسلّماتُها في Audit.lean.

مقترحُ البنّاء بأمر المالك العامّ، يسري بعد دمج طلبه. قولُ المالك (2026-10-25، 23:07):
«موافق على إضافة المبرهنات الثلاث وفقlean واربط مع النقل وبعدها اكمل الربط وفق افضل الممارسات ليكون كل المشروع مترابط ومتناسق ومتكامل وفق افضل الممارسات»
وصدرُ رسالته سؤالُ البنّاء ملصقًا («Then you should I carry on with the items on your list»)، فمعنى «الربط» قائمةٌ في الجلسة؛ وعدُّ هذا الفحص منها
قراءةُ البنّاء.

سببُه: البند ٣ في البوّابة يعدّ ما في Audit.lean ويفحص مسلّماته، والبند ٤ يمنع نقصَ عدده؛ ولا شيء يمنع مبرهنةً جديدةً من أن تُبنى ولا
تُدقَّق. وكذلك بقيت 250 مبرهنةً عامّةً مبنيّةً خارج Audit.lean على da1ffa6. ومنها ما تسِمه `خارطة_الطريق.md` «مبرهن» بأسمائه أو بعدده:
مبرهناتُ `Madlul/Dalala.lean` (س85، وكان منها في Audit.lean اثنتان)، و`fakk_n` و`n_fakk` (س71)، و`hadhayan_ghayr_mawdu` (س86).

الطريقة: يقرأ ملفّات `.ilean` التي يكتبها `lake build` في `.lake/build/lib/lean` (أسماءُ التصريحات كاملةً بمواضعها)، ويعدّ التصريحَ مبرهنةً
إذا سبقت اسمَه في سطره الكلمةُ `theorem` أو `lemma`، وخاصًّا إذا كان في ما قبلها `private`. ويُشغَّل بعد `lake build` (البوّابة ١).
والوحداتُ: ما تحت SLGE وDal وMadlul وJisr وAql وNizam وFaahis وQari ممّا له ملفُّ مصدر.

ويرفض: مبرهنةً عامّةً ليس لها `#print axioms <اسمها>` في Audit.lean خارج التعليقات (`bawwaba.strip_comments`)؛ وتصريحًا لا يقع اسمُه
في موضعه من سطره (فيُكشف خطأُ وحدة العمود بدل أن تفوت مبرهنةٌ بصمت؛ ويُستثنى `instance` بلا اسم، وموضعُه أوّلُ الكلمة)؛ وغيابَ البناء (لا `.ilean`)؛ ووحدةً مصدرُها
موجود ولا `.ilean` لها. الطفرات: P838 (مبرهنةٌ بلا سطر)، وP839 (سطرٌ في تعليق)، وP840 (خاصّةٌ صارت عامّة). وفرعا غياب البناء والوحدة بلا
`.ilean` بلا طفرة: الطفراتُ تبدّل نصًّا في ملفٍّ قائم، ولا تحذف بناءً ولا تُنشئ وحدة.
التشغيل (بعد lake build): python3 -I tahaqquq/test_tadqiq_tamm.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tahaqquq"))
import bawwaba  # noqa: E402
DIRS = ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Nizam", "Faahis", "Qari")
BUILD = os.path.join(ROOT, ".lake", "build", "lib", "lean")
KIND = re.compile(r"(?:^|\s)(theorem|lemma)\s+$")
TOKEN = re.compile(r"[^\s:(\[{]+")


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


def mubarhanat(mod, fails):
    """المبرهناتُ العامّة في الوحدة من .ilean، أو None إن غاب. ويُضاف إلى fails كلُّ تصريحٍ لا يقع اسمُه في موضعه."""
    p = os.path.join(BUILD, *mod.split(".")) + ".ilean"
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding="utf-8"))
    src = open(os.path.join(ROOT, *mod.split(".")) + ".lean", encoding="utf-8").read().split("\n")
    out = []
    for name, pos in d["decls"].items():
        line, col = pos[4], pos[5]
        pre = src[line][:col] if line < len(src) else ""
        tok = TOKEN.match(src[line][col:]) if line < len(src) else None
        if not (tok and name.endswith(tok.group(0))) and not src[line][col:].startswith("instance"):
            fails.append(f"موضعُ التصريح {name} في {mod} لا يقع عليه اسمُه (س{line + 1}، ع{col})")
            continue
        if not KIND.search(pre):
            continue
        if "private" in pre.split() or name.startswith("_private"):
            continue
        out.append(name)
    return sorted(out)


def main():
    fails = []
    audit = open(os.path.join(ROOT, "Audit.lean"), encoding="utf-8").read()
    mudaqqaq = set(re.findall(r"^#print axioms\s+(\S+)\s*$", bawwaba.strip_comments(audit), flags=re.M))
    if not os.path.isdir(BUILD):
        print("تمامُ التدقيق: لا بناء (.lake/build/lib/lean غائب)؛ شغّل lake build أوّلًا")
        sys.exit(1)
    kull, ghaib, bila_ilean = 0, [], []
    for mod in wahdat():
        ms = mubarhanat(mod, fails)
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
