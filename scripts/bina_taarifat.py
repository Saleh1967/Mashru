"""بناءُ «جدول التعريفات» (نوعُه «وضع»): كلُّ لفظٍ بتعريفه منقولًا بأسطره من مصدرٍ مرصود، لا بلفظ البنّاء.

القرار: قولُ المالك في الجلسة 2026-10-22 (01:57 بتوقيت عمّان): «… ما هو الوكيل وما هو جيت هب وما هوmashru وما مكوناته وما
تعريفاته وما إطار عمله وكيف تتم عملياته وما هو بايثون وما هو الدستور …».

لماذا جدولٌ ثانٍ (الدستور م12: لا يُقاس نوعٌ بمقياس غيره): التعريفُ وضعٌ — خبرٌ عمّا اصطُلح عليه — لا واقعٌ مشهود. وإن دخل
«الواقع المختوم» فروايةٌ من مصدرٍ واحد لا ترتفع (`Waqi.masdar_wahid_la_yarfa`)؛ ونصُّه يُحفظ هنا وضعًا بدرجته. وما شوهد من مكوّنات
Mashru وعمليّاته صفوفٌ في waqi_001.tsv يحيل إليها عمودُ shawahid_waqi.

القواعد:
  * النصُّ يُستخرج آليًّا من مصدره بأسطره عند الإيداع المرصود (git show <إيداع>:<مسار>) أو من ملفّ دستور الوكيل في البيئة
    (غيرُ مودَع: نسخةُ مهارةٍ تُزامَن، وبصمتُها في الصفّ) أو من مخرجٍ خامّ في waqi_shawahid؛ والأسطرُ تُضمّ بـ « / » وتُحذف مسافةُ
    أوّل السطر وحدها (عُرفُ الاقتباس في المستودع).
  * لكلّ صفٍّ بصمةُ مصدره (sha256 لبايتاته)، وواضعُه كما يُعرف من مصدره، وبصمةُ دفعة الواقع التي تحيل إليها أرقامُ صفوفه، ودرجتُه (م12: آحاد/مشهور/متواتر بعدد المصادر المستقلّة —
    كلُّها هنا آحاد)، وصفوفُ الواقع التي تشهد له. ومن الصفوف ما ليس تعريفًا بالمعنى الدقيق (عنوانٌ مع مادّة، قاعدةُ عمل، سطرُ
    استدعاء)، فاسمُ اللفظ فيها يقول ما هو.
  * المخرجُ مرشّحٌ؛ الختمُ بإذن المالك وحده.

التشغيل (من جذر المستودع):
  python3 -I scripts/bina_taarifat.py <مجلّد المودَعات> --commit <الإيداع المرصود في waqi_001>
"""
import csv
import glob
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AMDA = ["raqm", "lafz", "taarif", "masdar", "basmat_masdar", "wadi", "daraja", "shawahid_waqi", "basmat_waqi"]
MASHRU, TALIMAT, WAKIL, SANI = "نصّ المشروع (CLAUDE.md)", "تعليمات المالك (تعليمات_المشروع.md)", "دستور الوكيل", "صانع الأداة"
MILAF = "ملفّ المشروع"  # يُلحق به مسارُه

# (اللفظ، المصدر، أوّل سطر، آخر سطر، الواضع، صفوف الواقع الشاهدة)
# المصدر: مسارٌ في المستودع، أو «DUSTUR» لملفّ دستور الوكيل، أو «waqi:<رقم>» لمخرجٍ خامّ مرصود.
TAARIFAT = [
    ("Mashru", "CLAUDE.md", 1, 1, MASHRU, "2,3,10,11,12,16"),
    ("هدفُ Mashru", "تعليمات_المشروع.md", 4, 5, TALIMAT, ""),
    ("مراحلُ Mashru", "تعليمات_المشروع.md", 6, 6, TALIMAT, ""),
    ("الدستور: عنوانُه ومادّتُه الأولى", "CLAUDE.md", 3, 4, MASHRU, "29"),
    ("الوسم", "CLAUDE.md", 5, 7, MASHRU, ""),
    ("مراتبُ المخرج", "CLAUDE.md", 14, 15, MASHRU, ""),
    ("الحكمُ المرخَّص", "CLAUDE.md", 18, 19, MASHRU, ""),
    ("المخزن والفاحص", "CLAUDE.md", 20, 22, MASHRU, "39"),
    ("المودَع والختم", "CLAUDE.md", 23, 25, MASHRU, "36,37"),
    ("السلطة", "CLAUDE.md", 26, 26, MASHRU, ""),
    ("سيرُ العمل على GitHub", "CLAUDE.md", 28, 30, MASHRU, "16,17,18,20,21"),
    ("البناء بـ Lean", "CLAUDE.md", 80, 83, MASHRU, "13,14,15,46,47"),
    ("القارئ", "CLAUDE.md", 391, 395, MASHRU, "40"),
    ("البنّاء (الوكيل)", "CLAUDE.md", 48, 48, MASHRU, "9,26"),
    ("murajii (الوكيل المراجع)", ".claude/agents/murajii.md", 3, 3, MILAF, "27"),
    ("qayyis (الوكيل القائس)", ".claude/agents/qayyis.md", 3, 3, MILAF, "28"),
    ("البوّابة", "tahaqquq/bawwaba.py", 1, 1, MILAF, "32"),
    ("بوّابة الإيداع", "mudaat/idaa.py", 1, 1, MILAF, "33,36"),
    ("أنواعُ المودَع", "mudaat/idaa.py", 6, 6, MILAF, ""),
    ("النواةُ في Lean", "تعليمات_المشروع.md", 5, 5, TALIMAT, "48,49"),
    ("موضعُ بايثون في طريقة العمل (القاعدة الرابعة)", "تعليمات_المشروع.md", 17, 17, TALIMAT, "7,45"),
    ("دستورُ الوكيل", "DUSTUR", 6, 6, WAKIL, "30,31"),
    ("أنواعُ المودَع (دستور الوكيل م12)", "DUSTUR", 26, 26, WAKIL, ""),
    ("أركانُ العقل (دستور الوكيل م14)", "DUSTUR", 28, 28, WAKIL, ""),
    ("مراتبُ المخرج (دستور الوكيل م15)", "DUSTUR", 32, 32, WAKIL, ""),
    ("الواقعُ المودَع (دستور الوكيل م16)", "DUSTUR", 33, 33, WAKIL, ""),
    ("gh: وصفُه نفسَه", "waqi:22", 1, 1, SANI, "22,23"),
    ("python3: سطرُ استدعائه", "waqi:44", 1, 1, SANI, "41,42,43,44,45"),
]


def masdarBytes(masdar, commit, mudaa, waqi):
    if masdar == "DUSTUR":
        f = sorted(glob.glob("/root/.claude/skills/synced/*/dustur-al-wakil/SKILL.md"))
        if not f:
            sys.exit("مرفوض: ملفّ دستور الوكيل غير حاضر")
        return open(f[0], "rb").read(), "دستور الوكيل (SKILL.md في هذه البيئة)"
    if masdar.startswith("waqi:"):
        r = waqi[int(masdar[5:])]
        return open(os.path.join(mudaa, "waqi_shawahid", r["basmat_mukhraj"]), "rb").read(), \
            f"waqi_001.tsv الصفّ {r['raqm']} (مخرج «{r['amr']}»)"
    p = subprocess.run(["git", "show", f"{commit}:{masdar}"], cwd=ROOT, capture_output=True)
    if p.returncode != 0:
        sys.exit(f"مرفوض: {masdar} غير موجود في {commit}")
    return p.stdout, f"{masdar}@{commit}"


def main():
    if len(sys.argv) < 4 or "--commit" not in sys.argv:
        sys.exit(__doc__)
    mudaa, commit = os.path.abspath(sys.argv[1]), sys.argv[sys.argv.index("--commit") + 1]
    wpath = os.path.join(mudaa, "waqi_001.tsv")
    waqi = {int(r["raqm"]): r for r in csv.DictReader(open(wpath, encoding="utf-8"), delimiter="\t")}
    if not waqi[2]["qima"].startswith(commit):
        sys.exit(f"مرفوض: الإيداع {commit} ليس المرصودَ في waqi_001.tsv (الصفّ 2)")
    bwaqi = hashlib.sha256(open(wpath, "rb").read()).hexdigest()
    out = []
    for i, (lafz, masdar, a, b, wadi, shawahid) in enumerate(TAARIFAT, 1):
        data, ism = masdarBytes(masdar, commit, mudaa, waqi)
        lines = data.decode("utf-8").split("\n")
        if b > len(lines) or a < 1 or a > b:
            sys.exit(f"مرفوض: الأسطر {a}–{b} خارج {ism}")
        text = " / ".join(l.lstrip() for l in lines[a - 1:b])
        if not text or "\t" in text:
            sys.exit(f"مرفوض: نصُّ «{lafz}» فارغ أو فيه جدولة")
        for s in filter(None, shawahid.split(",")):
            if int(s) not in waqi:
                sys.exit(f"مرفوض: «{lafz}» يحيل إلى صفّ واقعٍ غير موجود: {s}")
        loc = f"{ism}:L{a}" if a == b else f"{ism}:L{a}–{b}"
        if wadi == MILAF:
            wadi = f"{MILAF} ({masdar})"
        # الدرجة (م12): كلُّ تعريفٍ هنا من مصدرٍ واحد، فهو آحاد
        out.append([str(i), lafz, text, loc, hashlib.sha256(data).hexdigest(), wadi, "آحاد", shawahid or "-", bwaqi])
    name = os.path.join(mudaa, "taarifat.tsv")
    if os.path.exists(name):
        sys.exit(f"مرفوض: {name} موجود؛ لا يُعاد كتابتُه")
    with open(name, "w", encoding="utf-8") as f:
        f.write("\t".join(AMDA) + "\n")
        for r in out:
            f.write("\t".join(r) + "\n")
    print(f"{name}: {len(out)} تعريفًا، بصمته {hashlib.sha256(open(name, 'rb').read()).hexdigest()}")


if __name__ == "__main__":
    main()
