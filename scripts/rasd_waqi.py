"""رصدُ «الواقع المختوم»: تشغيلُ الحواسّ المسجَّلة وكتابةُ دفعة مشاهداتٍ مرشّحةٍ للختم (Aql/Waqi.lean).

القرار: قولُ المالك في الجلسة 2026-10-22 (01:57 بتوقيت عمّان) — جدولُ واقعٍ مختومٍ قابلٌ للنموّ، نواةٌ للتوسّع بالتعلّم.

القواعد (الدستور م12، م14–م16؛ وتعيينُ البنّاء في ترويسة Aql/Waqi.lean):
  * الحاسّةُ أداةٌ مسجَّلةٌ هنا بأمرها الحرفيّ؛ لا تُضاف حاسّةٌ إلّا في هذا الجدول (HAWASS)، فيظهر إيداعُها.
  * كلُّ صفٍّ مشاهدةٌ واحدة: الأمرُ كما شُغِّل، ومخرجُه الخامّ (stdout) محفوظًا باسم بصمته sha256 في
    <المجلّد>/waqi_shawahid/، ورمزُ الخروج، ووقتُ المشاهدة (UTC)، والقيمةُ بقاعدة استخراجٍ معلَنة من المخرج.
  * الوجه: «قياس» إذا كانت القيمةُ خاصّةً للبايتات أو للعمليّة المشهودة نفسها (بصمة، عدد، محتوى شجرة، مخرجُ تشغيلٍ على مدخلٍ
    معيَّن، رمزُ خروج)؛ «رواية» إذا كانت قولًا عن غير البايتات الحاضرة أو عن القائل نفسه (إصدار، تاريخ، رابط، وصف، تعريف، ما يرويه
    خادم). والمصدرُ الراوي الفعليّ (البرنامجُ أو الحزمةُ أو كاتبُ النصّ وناشرُه، لا مسارُ الملفّ): روايتان من مصدرٍ واحد ليستا مستقلّتين
    (lean وlake مصدرٌ واحد، وملفّاتُ المشروع كلُّها مصدرٌ واحد). وحدُّه المعلَن: المصدرُ الناشرُ لا الشخصُ الكاتب، فنصوصُ المشروع
    ونسخةُ دستور الوكيل مصدران وكاتبُهما واحد — قرارُ المالك.
    الوجهُ والمصدرُ تعيينُ البنّاء في هذا الجدول، فهما معلَنان ويُعرضان على المالك.
  * لا تنظيف ولا قياسَ من فشل: ما لا يُستخرج بقاعدته، أو قيمةٌ فيها جدولةٌ أو سطرٌ جديد، أو أمرٌ خرج بغير صفر (إلّا في قاعدة
    «khuruj» التي تسجّل رمزَ الخروج نفسَه)، تُرفض الدفعةُ باسم حاسّتها؛ ولا يُكتب شيءٌ — لا الجدولُ ولا المخرجاتُ الخامّة — قبل أن
    تنجح الحواسُّ كلُّها.
  * النموّ: دفعةٌ جديدة (--dafa n) تحمل بصمةَ الدفعة السابقة (--sabiq)، ولا تُقبل إلّا إن كانت تلك البصمةُ قيدًا «مختومًا» من نوع
    «واقع-مختوم» في mudaat/sijill.json؛ ولا يُعدَّل صفٌّ مكتوب.
  * المخرجُ مرشّحٌ لا مختوم: الختمُ بـ mudaat/idaa.py sajjil بإذن المالك وحده.

التشغيل (من جذر المستودع):
  python3 -I scripts/rasd_waqi.py <مجلّد المودَعات> --commit <إيداع> --dafa 1 [--sabiq <بصمة الدفعة السابقة>]
"""
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QIYAS, RIWAYA = "قياس", "رواية"
AMDA = ["raqm", "hassa", "amr", "masdar", "mawdu", "sifa", "qima", "wajh", "istikhraj", "basmat_mukhraj", "khuruj",
        "waqt", "dafa", "sabiq"]

# (الحاسّة، الأمر، المصدر، الشيء، الخاصّة، الوجه، قاعدة الاستخراج)
# في الأمر: {C} الإيداع، {MUDAA} مجلّد المودَعات، {DUSTUR} ملفّ دستور الوكيل في هذه البيئة.
HAWASS = [
    # — الرصدُ نفسُه —
    ("date", "date -u +%Y-%m-%dT%H:%M:%SZ", "ساعة النظام", "بيئة الرصد", "وقتُ بدء الرصد (UTC)", RIWAYA, "kamil"),
    # — Mashru: المستودع وإيداعه ومكوّناته —
    ("git", "git rev-parse {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru", "معرّف الإيداع المرصود", QIYAS, "kamil"),
    ("git", "git remote get-url origin", "git: إعداد النسخة المحلّيّة", "مستودع:Mashru", "الأصل البعيد", RIWAYA, "kamil"),
    ("git", "git ls-tree --name-only -d {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "المجلّدات العليا", QIYAS,
     "satran"),
    ("git", "git ls-tree -r --name-only {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "عدد الملفّات", QIYAS, "adad"),
    ("git", "git ls-tree -r --name-only {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "عدد ملفّات Lean", QIYAS,
     "adad_lahiqa:.lean"),
    ("git", "git ls-tree -r --name-only {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "عدد ملفّات بايثون", QIYAS,
     "adad_lahiqa:.py"),
    ("git", "git log --format=%H {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "عدد الإيداعات", QIYAS, "adad"),
    ("git", "git log --format=%b {C}", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "أسطرُ «Co-Authored-By: Claude» في رسائل الإيداعات",
     QIYAS, "adad_fih:Co-Authored-By: Claude"),
    ("git", "git show {C}:CLAUDE.md", "نصوص المشروع (مستودع Mashru)", "Mashru", "تعريفُه في سطره الأوّل", RIWAYA,
     "awwal"),
    ("sha256sum", "git show {C}:CLAUDE.md | sha256sum", "sha256sum", "ملفّ:CLAUDE.md@{C}", "بصمة sha256", QIYAS,
     "regex:^([0-9a-f]{64})"),
    ("python3-hashlib", "git show {C}:CLAUDE.md | python3 -I -c \"import hashlib,sys; print(hashlib.sha256(sys.stdin.buffer.read()).hexdigest())\"",
     "python3 hashlib", "ملفّ:CLAUDE.md@{C}", "بصمة sha256", QIYAS, "kamil"),
    ("git", "git show {C}:Audit.lean", "git: حسابٌ محلّيّ", "مستودع:Mashru@{C}", "أسطر «#print axioms» في Audit.lean", QIYAS,
     "adad_bidaya:#print axioms"),
    ("git", "git show {C}:tahaqquq/khatt_asas.json", "نصوص المشروع (مستودع Mashru)", "مستودع:Mashru@{C}",
     "عدد المبرهنات المدقَّقة", RIWAYA, "json:mubarhanat"),
    ("git", "git show {C}:lean-toolchain", "نصوص المشروع (مستودع Mashru)", "Lean", "الإصدار المطلوب في المستودع", RIWAYA,
     "regex:v([0-9.]+)"),
    # — GitHub: ما يرويه الخادم —
    ("gh", "gh api repos/Saleh1967/Mashru --jq .full_name", "GitHub", "مستودع:Mashru", "الاسم على GitHub", RIWAYA, "kamil"),
    ("gh", "gh api repos/Saleh1967/Mashru --jq .private", "GitHub", "مستودع:Mashru", "خاصّ", RIWAYA, "kamil"),
    ("gh", "gh api repos/Saleh1967/Mashru --jq .default_branch", "GitHub", "مستودع:Mashru", "الفرع الافتراضيّ", RIWAYA,
     "kamil"),
    ("gh", "gh api repos/Saleh1967/Mashru --jq .created_at", "GitHub", "مستودع:Mashru", "تاريخ الإنشاء", RIWAYA, "kamil"),
    ("git", "git ls-remote origin refs/heads/main", "GitHub", "مستودع:Mashru", "رأس main على الخادم", RIWAYA,
     "regex:^([0-9a-f]{40})"),
    ("gh", "gh api repos/Saleh1967/Mashru/pulls/70 --jq .state", "GitHub", "طلب دمج:Mashru#70", "الحال", RIWAYA, "kamil"),
    ("gh", "gh --help", "gh (الأداة نفسها)", "gh", "وصفُها نفسَها", RIWAYA, "awwal"),
    ("gh", "gh --version", "gh (الأداة نفسها)", "gh", "الإصدار", RIWAYA, "regex:gh version ([0-9.]+)"),
    ("git", "git --version", "git (الأداة نفسها)", "git", "الإصدار", RIWAYA, "regex:git version ([0-9.]+)"),
    # — الوكيل —
    ("claude", "claude --version", "claude (الأداة نفسها)", "Claude Code", "الإصدار", RIWAYA, "kamil"),
    ("git", "git show {C}:CLAUDE.md", "نصوص المشروع (مستودع Mashru)", "البنّاء", "تعريفُه", RIWAYA,
     "satr:البنّاء (الجلسة الرئيسة)"),
    ("git", "git show {C}:.claude/agents/murajii.md", "نصوص المشروع (مستودع Mashru)", "وكيل:murajii", "تعريفُه", RIWAYA,
     "regex:^description: (.*)$"),
    ("git", "git show {C}:.claude/agents/qayyis.md", "نصوص المشروع (مستودع Mashru)", "وكيل:qayyis", "تعريفُه", RIWAYA,
     "regex:^description: (.*)$"),
    # — الدستور —
    ("git", "git show {C}:CLAUDE.md", "نصوص المشروع (مستودع Mashru)", "الدستور", "مادّتُه الأولى", RIWAYA,
     "satr:- لا كلام قبل الطبعة"),
    ("cat", "cat {DUSTUR}", "دستور الوكيل (ملفّ مهارة المالك في هذه البيئة)", "دستور الوكيل", "عنوانُه", RIWAYA,
     "regex:^# (.*)$"),
    ("sha256sum", "sha256sum {DUSTUR}", "sha256sum", "ملفّ:دستور الوكيل", "بصمة sha256", QIYAS, "regex:^([0-9a-f]{64})"),
    ("git", "git show {C}:tahaqquq/bawwaba.py", "نصوص المشروع (مستودع Mashru)", "البوّابة", "وصفُها نفسَها", RIWAYA,
     "regex:^\"\"\"(.*)$"),
    ("git", "git show {C}:mudaat/idaa.py", "نصوص المشروع (مستودع Mashru)", "بوّابة الإيداع", "وصفُها نفسَها", RIWAYA,
     "regex:^\"\"\"(.*)$"),
    # — العمليّات، مشاهدةً بالتشغيل على الشجرة العاملة وقت الرصد (إيداعُها وما لم يُودَع منها صفّان أوّلَها) —
    ("git", "git rev-parse HEAD", "git: حسابٌ محلّيّ", "الشجرة العاملة وقت الرصد", "إيداعُها", QIYAS, "kamil"),
    ("git", "git status --porcelain", "git: حسابٌ محلّيّ", "الشجرة العاملة وقت الرصد", "ملفّاتٌ غيرُ مودَعة", QIYAS, "adad"),
    ("python3", "python3 -I mudaat/idaa.py fahs", "تشغيل", "سجلّ المودَعات (الشجرة العاملة)", "فحصُه", QIYAS, "kamil"),
    ("python3", "python3 -I mudaat/idaa.py tahaqqaq {MUDAA}", "تشغيل", "بصمات المودَعات الحاضرة (الشجرة العاملة)", "عددُ المطابق", QIYAS,
     "adad_bidaya:مطابق"),
    ("python3", "python3 -I mudaat/test_idaa.py", "تشغيل", "اختبار بوّابة الإيداع (الشجرة العاملة)", "النتيجة", QIYAS, "kamil"),
    ("faahis", ".lake/build/bin/faahis mudaat/sijill.tsv mawsua/makhzan.tsv", "تشغيل", "الفاحص على المخزن (الشجرة العاملة)",
     "سطرُ الخلاصة", QIYAS, "satr:القاعدة"),
    ("qari", ".lake/build/bin/qari mudaat/sijill.tsv mawsua/makhzan_kamil.tsv ذَهَبَ", "تشغيل", "القارئ على «ذَهَبَ» (الشجرة العاملة)",
     "المقاطع", QIYAS, "regex:المقاطع \\(\\d+\\): (.*?) —"),
    # — بايثون —
    ("python3", "python3 --version", "python3 (الأداة نفسها)", "Python", "الإصدار", RIWAYA, "regex:Python ([0-9.]+)"),
    ("python3", "python3 -I -c \"import sys; print('.'.join(map(str, sys.version_info[:3])))\"", "python3 (الأداة نفسها)",
     "Python", "الإصدار", RIWAYA, "kamil"),
    ("python3", "python3 -I -c \"import sys; print(sys.implementation.name)\"", "python3 (الأداة نفسها)", "Python",
     "التنفيذ", RIWAYA, "kamil"),
    ("python3", "python3 --help", "python3 (الأداة نفسها)", "Python", "وصفُ استدعائه", RIWAYA, "awwal"),
    ("python3", "python3 -I -c \"print(2+3)\"", "تشغيل", "Python", "يُخرج لـ print(2+3)", QIYAS, "kamil"),
    # — Lean —
    ("lean", "lean --version", "حزمة Lean (lean وlake بناءٌ واحد)", "Lean", "الإصدار", RIWAYA, "regex:version ([0-9.]+)"),
    ("lake", "lake --version", "حزمة Lean (lean وlake بناءٌ واحد)", "Lean", "الإصدار", RIWAYA, "regex:Lean version ([0-9.]+)"),
    ("lean", "printf '%s\\n' 'example : 2 + 3 = 5 := by decide' | lean --stdin", "تشغيل", "Lean",
     "رمزُ الخروج لـ «example : 2 + 3 = 5 := by decide»", QIYAS, "khuruj"),
    ("lean", "printf '%s\\n' 'example : 2 + 3 = 6 := by decide' | lean --stdin", "تشغيل", "Lean",
     "رمزُ الخروج لـ «example : 2 + 3 = 6 := by decide»", QIYAS, "khuruj"),
    # — البيئة —
    ("uname", "uname -sr", "uname (النواة)", "بيئة الرصد", "النظام", RIWAYA, "kamil"),
]


def istakhrij(qaida, out, code):
    """القيمة بقاعدتها من المخرج الخامّ؛ None إن لم تُستخرج."""
    text = out.decode("utf-8")
    lines = text.splitlines()
    nonempty = [l for l in lines if l.strip()]
    if qaida == "kamil":
        return nonempty[0].strip() if len(nonempty) == 1 else None
    if qaida == "awwal":
        return nonempty[0].strip() if nonempty else None
    if qaida == "satran":
        return "،".join(l.strip() for l in nonempty) if nonempty else None
    if qaida == "adad":
        return str(len(nonempty))
    if qaida == "khuruj":
        return str(code)
    kind, _, arg = qaida.partition(":")
    if kind == "adad_lahiqa":
        return str(sum(l.strip().endswith(arg) for l in nonempty))
    if kind == "adad_fih":
        return str(sum(arg in l for l in nonempty))
    if kind == "adad_bidaya":
        return str(sum(l.startswith(arg) for l in nonempty))
    if kind == "satr":
        for l in lines:
            if arg in l:
                return l.strip()
        return None
    if kind == "regex":
        for l in lines:
            m = re.search(arg, l)
            if m:
                return m.group(1).strip()
        return None
    if kind == "json":
        try:
            return str(json.loads(text)[arg])
        except (ValueError, KeyError):
            return None
    raise SystemExit(f"قاعدة استخراجٍ مجهولة: {qaida}")


def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        sys.exit(__doc__)
    mudaa = os.path.abspath(sys.argv[1])
    commit, dafa, sabiq = arg("--commit"), arg("--dafa", "1"), arg("--sabiq", "-")
    if not commit or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
        sys.exit("مرفوض: --commit إيداعٌ بمعرّفه")
    if dafa != "1":
        sijill = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
        if not any(m["sha256"] == sabiq and m["hala"] == "مختوم" and m["naw"] == "واقع-مختوم" for m in sijill):
            sys.exit("مرفوض: دفعةٌ بعد الأولى تحمل بصمةَ سابقتها، قيدًا مختومًا «واقع-مختوم» في mudaat/sijill.json (--sabiq)")
    dustur = sorted(glob.glob("/root/.claude/skills/synced/*/dustur-al-wakil/SKILL.md"))
    shdir = os.path.join(mudaa, "waqi_shawahid")
    rows, khamat = [], {}
    for i, (hassa, amr, masdar, mawdu, sifa, wajh, qaida) in enumerate(HAWASS, 1):
        if "{DUSTUR}" in amr and not dustur:
            sys.exit(f"مرفوض: الحاسّة {i} ({hassa}) تحتاج ملفّ دستور الوكيل، ولم يحضر")
        sub = lambda s: s.replace("{C}", commit).replace("{MUDAA}", mudaa).replace("{DUSTUR}", dustur[0] if dustur else "")
        amr, mawdu = sub(amr), sub(mawdu)
        waqt = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        p = subprocess.run(["bash", "-c", amr], cwd=ROOT, capture_output=True, timeout=600)
        out = p.stdout
        if p.returncode != 0 and qaida != "khuruj":
            sys.exit(f"مرفوض: الحاسّة {i} ({hassa}: {amr}) خرجت {p.returncode}؛ لا قياسَ من فشل")
        qima = istakhrij(qaida, out, p.returncode)
        if qima is None or not qima or "\t" in qima or "\n" in qima:
            sys.exit(f"مرفوض: الحاسّة {i} ({hassa}: {amr}) لم تُستخرج قيمتُها بقاعدة «{qaida}» (خروج {p.returncode})")
        b = hashlib.sha256(out).hexdigest()
        khamat[b] = out
        rows.append([str(i), hassa, amr, masdar, mawdu, sifa, qima, wajh, qaida, b, str(p.returncode), waqt, dafa, sabiq])
    for r in rows:
        for v in r:
            if "\t" in v or "\n" in v:
                sys.exit(f"مرفوض: الصفّ {r[0]} فيه جدولةٌ أو سطرٌ جديد")
    name = os.path.join(mudaa, f"waqi_{int(dafa):03d}.tsv")
    if os.path.exists(name):
        sys.exit(f"مرفوض: {name} موجود؛ الدفعةُ لا تُعاد كتابتُها")
    os.makedirs(shdir, exist_ok=True)
    for b, out in khamat.items():
        path = os.path.join(shdir, b)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(out)
    with open(name, "w", encoding="utf-8") as f:
        f.write("\t".join(AMDA) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    with open(name, "rb") as f:
        print(f"{name}: {len(rows)} مشاهدة، بصمتها {hashlib.sha256(f.read()).hexdigest()}")


if __name__ == "__main__":
    main()
