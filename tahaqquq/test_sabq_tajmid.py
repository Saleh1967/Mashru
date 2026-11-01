"""اختبارُ سبق التجميد (tahaqquq/sabq_tajmid.py) على مستودعاتِ git مصنوعة، وتوقّعاتُها من شروط رأسه لا من مخرجه، ثمّ على المستودع نفسِه.

١. سليم: cases ثمّ الشفرة ثمّ natija_1 بصمتُه صحيحة ← لا خطأ.
٢. الحالاتُ والشفرةُ في إيداعٍ واحد ← «ليس سلفًا صارمًا» (P1340).
٣. cases.json غُيّر بعد النتيجة ← خطأُ البصمة (P1341).
٤. النتيجةُ أُودعت قبل الشفرة التي تسمّيها ← «ليست سلفًا للنتيجة» (P1342).
٥. نسخةٌ ضحلة ← خروج 3 باسم TARIKH_DAHL، لا نجاح (P1343).
٦. المستودعُ نفسُه: كلُّ ضابطٍ في tahaqquq/dawabit يمرّ (إن لم تكن النسخةُ ضحلة).
والملفُّ الموروث (الشرط ١ في رأس sabq_tajmid.py؛ ملفٌّ في البصمة أُودع قبل التجميد ولم يتغيّر إليه، وبصمتُه المسجَّلة بايتاتُه):
٧. موروثٌ وشفرةٌ بعد التجميد ← لا خطأ.
٨. الملفّاتُ كلُّها موروثة ← «لا شفرةَ بعد التجميد» (P1549).
٩. موروثٌ غُيّر بين إيداعه والتجميد ← «ليس سلفًا صارمًا» (P1548).
١٠. موروثٌ بصمتُه المسجَّلة غيرُ بايتاته في إيداعه ← «ليس سلفًا صارمًا» (P1547).
١١. «موروثٌ» أُودع مع الحالات في إيداع التجميد ← «ليس سلفًا صارمًا» (P1550).
التشغيل: python3 -I tahaqquq/test_sabq_tajmid.py
"""

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

JADHR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("sabq_tajmid", os.path.join(JADHR, "tahaqquq", "sabq_tajmid.py"))
st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(st)
FAIL = []
ENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")


def check(name, cond):
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


def g(r, *a):
    return subprocess.run(["git", "-C", r, *a], capture_output=True, text=True, env=ENV, check=True).stdout.strip()


def ktb(r, rel, nass):
    p = os.path.join(r, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(nass)


def awda(r, msg):
    g(r, "add", "-A")
    g(r, "commit", "-q", "-m", msg)
    return g(r, "rev-parse", "HEAD")


def mustawda(tartib):
    """مستودعٌ بضابطٍ واحد «x»؛ tartib: «salim» أو «maan» أو «taghyir» أو «qabl»."""
    r = tempfile.mkdtemp()
    g(r, "init", "-q")
    cases = '[{"id": 1}]\n'
    sha = hashlib.sha256(cases.encode()).hexdigest()
    D = "tahaqquq/dawabit/x"
    ktb(r, f"{D}/cases.json", cases)
    if tartib == "maan":
        ktb(r, "Jisr/X.lean", "def x := 1\n")
    F = awda(r, "tajmid")
    C = F if tartib == "maan" else None
    if tartib == "qabl":
        ktb(r, "a.txt", "a\n")
        awda(r, "ghayr")
        ktb(r, f"{D}/natija_1.json", "{}\n")
        N = awda(r, "natija")
        ktb(r, "Jisr/X.lean", "def x := 1\n")
        C = awda(r, "shifra")
        ktb(r, f"{D}/natija_1.json", json.dumps({"cases_sha256": sha, "shifra": {"Jisr/X.lean": {"iydaa": C}}}))
        awda(r, "tahdith")
        return r
    if C is None:
        ktb(r, "Jisr/X.lean", "def x := 1\n")
        C = awda(r, "shifra")
    ktb(r, f"{D}/natija_1.json", json.dumps({"cases_sha256": sha, "shifra": {"Jisr/X.lean": {"iydaa": C}}}))
    awda(r, "natija")
    if tartib == "taghyir":
        ktb(r, f"{D}/cases.json", '[{"id": 2}]\n')
        awda(r, "taghyir")
    return r


def mustawda_mawruth(naw):
    """مستودعٌ بضابطٍ «x» وملفٍّ موروث Y.lean؛ naw: «salim» أو «kulluha» أو «taghayyar» أو «basma» أو «maa_F»."""
    r = tempfile.mkdtemp()
    g(r, "init", "-q")
    y = "def y := 1\n"
    D = "tahaqquq/dawabit/x"
    cases = '[{"id": 1}]\n'
    if naw != "maa_F":
        ktb(r, "Jisr/Y.lean", y)
        C0 = awda(r, "asl")
        if naw == "taghayyar":
            ktb(r, "Jisr/Y.lean", "def y := 2\n")
            awda(r, "taghyir")
    else:
        ktb(r, "Jisr/Y.lean", y)
    ktb(r, f"{D}/cases.json", cases)
    F = awda(r, "tajmid")
    if naw == "maa_F":
        C0 = F
    sh = {"Jisr/Y.lean": {"iydaa": C0, "sha256": hashlib.sha256(("def y := 9\n" if naw == "basma" else y).encode()).hexdigest()}}
    if naw != "kulluha":
        ktb(r, "Jisr/X.lean", "def x := 1\n")
        C = awda(r, "shifra")
        sh["Jisr/X.lean"] = {"iydaa": C, "sha256": hashlib.sha256(b"def x := 1\n").hexdigest()}
    ktb(r, f"{D}/natija_1.json", json.dumps({"cases_sha256": hashlib.sha256(cases.encode()).hexdigest(), "shifra": sh}))
    awda(r, "natija")
    return r


check("١ السليمُ بلا خطأ", st.fahs_dabit(mustawda("salim"), "x") == [])
a = st.fahs_dabit(mustawda("maan"), "x")
check("٢ الحالاتُ والشفرةُ معًا: ليس سلفًا صارمًا", any("ليس سلفًا صارمًا" in x for x in a))
a = st.fahs_dabit(mustawda("taghyir"), "x")
check("٣ الحالاتُ غُيّرت بعد التجميد: خطأُ البصمة", any("بصمةُ cases.json" in x for x in a))
a = st.fahs_dabit(mustawda("qabl"), "x")
check("٤ النتيجةُ قبل الشفرة: ليست سلفًا للنتيجة", any("ليست سلفًا للنتيجة" in x for x in a))
asl = mustawda("salim")
g(asl, "commit", "-q", "--allow-empty", "-m", "z")
dahl = tempfile.mkdtemp()
subprocess.run(["git", "clone", "-q", "--depth", "1", "file://" + asl, dahl], capture_output=True, check=True)
check("٥ النسخةُ الضحلة: خروج 3 لا نجاح", st.main(dahl) == 3)
check("٧ موروثٌ وشفرةٌ بعد التجميد: لا خطأ", st.fahs_dabit(mustawda_mawruth("salim"), "x") == [])
a = st.fahs_dabit(mustawda_mawruth("kulluha"), "x")
check("٨ كلُّها موروثة: لا شفرةَ بعد التجميد", any("لا شفرةَ بعد التجميد" in x for x in a))
for n, naw in [("٩ موروثٌ غُيّر قبل التجميد", "taghayyar"), ("١٠ موروثٌ ببصمةٍ غيرِ بايتاته", "basma"), ("١١ «موروثٌ» مع الحالات", "maa_F")]:
    a = st.fahs_dabit(mustawda_mawruth(naw), "x")
    check(n + ": ليس سلفًا صارمًا", any("ليس سلفًا صارمًا" in x for x in a))
r6 = subprocess.run(["git", "-C", JADHR, "rev-parse", "--is-shallow-repository"], capture_output=True, text=True)
if r6.returncode != 0 or r6.stdout.strip() != "false":
    print("—    المستودعُ ضحلٌ أو بلا تاريخ: تُرك ٦")
else:
    check("٦ المستودعُ نفسُه: كلُّ ضابطٍ يمرّ", st.main(JADHR) == 0)
print(f"سبقُ التجميد: {'فشل ' + str(len(FAIL)) if FAIL else 'مرّ'}")
sys.exit(1 if FAIL else 0)
