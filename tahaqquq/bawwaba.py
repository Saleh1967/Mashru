"""بوّابة التحقّق: لا يُقال «تمّ» قبل أن تمرّ كلّها. تعيد 0 إن مرّت، و2 مع السبب إن لم تمرّ.

البنود، بترتيبها (الدستور م2–م4، م8):
  ١. lake build ينجح.
  ٢. لا sorry ولا axiom ولا native_decide في ملفّات Lean (خارج التعليقات).
  ٣. Audit.lean يُبنى، وكلّ مبرهنة فيه مسلّماتها من الثلاث: propext، Classical.choice، Quot.sound.
  ٤. عدد المبرهنات المدقّقة لا ينقص عن خطّ الأساس في khatt_asas.json (نقصه حذفٌ يحتاج إذنًا).
  ٥. اختبارات بايثون (shabaka/test_shabaka.py) تمرّ، إن وُجد المودَع (MUDAA_MUKHASSAS).
  ٥ب. اختبارات المخزن (mawsua/test_mawsua.py): الفاحص التنفيذيّ المبنيّ من Lean يقبل المخزن ويرفض الفاسد.
  ٥ج. بوّابة الإيداع (mudaat/test_idaa.py): لا ختم بلا إذن ولا نوع، ولا تنظيف؛ وإن عُيّن MUDAA_DIR
      طوبقت بصمات ما حضر من المودَعات فيه.
  ٥هـ. القارئ (tahaqquq/test_qari.py): من النصّ المشكول إلى الخلايا والقانون والمقاطع والمخزن.
  ٥و. العوامل (tahaqquq/test_awamil.py): Jisr/AwamilJadwal.lean مطابقٌ لمودَعه إن حضر (MUDAA_AWAMIL أو MUDAA_DIR).
  ٥ز. نقول الأقسام (tahaqquq/test_aqsam.py): اقتباسات Jisr/AqsamAwamil.lean في أسطرها من المودَعات إن حضرت (MUDAA_DIR).
  ٥ح. جدول الأجناس (tahaqquq/test_ajnas.py): المودَع ajnas.tsv ببصمته، ومطابقة جدول Madlul/Tayin.lean له، وشجرة المخصّص إن حضرت.
  ٥ط. القطعة الثانية والنظامان (tahaqquq/test_jamad.py): ajnas_jamad.tsv وnizam_fizya.tsv وnizam_riyadiyyat.tsv ببصماتها، ومطابقة
      Madlul/Wiratha.lean وMadlul/Jamad.lean لها (الشجرة والثوابت وأسماء القوانين) إن حضرت.
  ٥ي. جدول العلاقات (tahaqquq/test_shabaka.py): alaqat.tsv ببصمته، ومطابقة شبكة Madlul/Shabaka.lean له وقرار «السائل شراب» إن حضر.
  ٥ك. جدول الحواسّ الخمس (tahaqquq/test_hawass.py): hawass.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Madlul/Hawass.lean له إن حضر.
  ٥ل. جدول أوّليات العقل (tahaqquq/test_awwaliyyat.py): awwaliyyat.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Awwaliyyat.lean له إن حضر.
  ٥م. جدول الأزمنة (tahaqquq/test_azmina.py): azmina.tsv ببصمته (مرشّح أو مختوم)، ومطابقة Aql/Azmina.lean له إن حضر.
  ٦. كلّ طفرة في tafrat.json تُقتل: تُفشل البناء أو تُفشل اختبارات المخزن. طفرة تعيش = اختبارٌ مرآة.
التشغيل: python3 -I tahaqquq/bawwaba.py [--bila-tafrat]
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def run(cmd, cwd=ROOT, timeout=1800):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def strip_comments(src):
    src = re.sub(r"/-.*?-/", "", src, flags=re.S)
    return re.sub(r"--.*", "", src)


def main():
    fails, report = [], []
    code, out = run(["lake", "build"])
    report.append(f"١ البناء: {'نجح' if code == 0 else 'فشل'}")
    if code != 0:
        fails.append("lake build فشل:\n" + out[-1500:])

    bad = []
    for d in ("SLGE", "Dal", "Madlul", "Jisr", "Aql", "Faahis", "Qari"):
        for root, _, fs in os.walk(os.path.join(ROOT, d)):
            for f in fs:
                if f.endswith(".lean"):
                    src = strip_comments(open(os.path.join(root, f), encoding="utf-8").read())
                    for w in ("sorry", "native_decide"):
                        if re.search(rf"\b{w}\b", src):
                            bad.append(f"{f}: {w}")
                    if re.search(r"^\s*axiom\s", src, re.M):
                        bad.append(f"{f}: axiom")
    report.append(f"٢ المحظورات: {len(bad)}")
    if bad:
        fails.append("محظورات: " + "، ".join(bad))

    code, out = run(["lake", "env", "lean", "Audit.lean"])
    lines = [l for l in out.splitlines() if "depends on axioms" in l or "does not depend" in l]
    nonstd = []
    for l in lines:
        m = re.search(r"\[(.*)\]", l)
        if m and not set(x.strip() for x in m.group(1).split(",")) <= ALLOWED:
            nonstd.append(l)
    report.append(f"٣ التدقيق: {len(lines)} مبرهنة، خارج المسموح {len(nonstd)}")
    if code != 0 or nonstd:
        fails.append("التدقيق: " + ("\n".join(nonstd) or out[-800:]))

    base_p = os.path.join(ROOT, "tahaqquq", "khatt_asas.json")
    base = json.load(open(base_p)) if os.path.exists(base_p) else {"mubarhanat": 0}
    report.append(f"٤ خطّ الأساس: {base['mubarhanat']} ← الآن {len(lines)}")
    if len(lines) < base["mubarhanat"]:
        fails.append(f"نقص عدد المبرهنات المدقّقة من {base['mubarhanat']} إلى {len(lines)}")

    mudaa = os.environ.get("MUDAA_MUKHASSAS")
    if mudaa and os.path.exists(mudaa):
        code, out = run([sys.executable, "-I", "shabaka/test_shabaka.py", mudaa])
        report.append(f"٥ اختبارات الشبكة: {out.strip().splitlines()[-1] if out.strip() else '?'}")
        if code != 0:
            fails.append("اختبارات الشبكة فشلت:\n" + out[-800:])
    else:
        report.append("٥ اختبارات الشبكة: لم تُشغَّل (المودَع غير حاضر؛ عيّن MUDAA_MUKHASSAS)")

    code, out = run([sys.executable, "-I", "mawsua/test_mawsua.py"])
    report.append(f"٥ب اختبارات المخزن: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات المخزن فشلت:\n" + out[-800:])

    code, out = run([sys.executable, "-I", "mudaat/test_idaa.py"])
    report.append(f"٥ج بوّابة الإيداع: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات الإيداع فشلت:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_qari.py"])
    report.append(f"٥هـ القارئ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبارات القارئ فشلت:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_awamil.py"])
    report.append(f"٥و العوامل: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار العوامل فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_aqsam.py"])
    report.append(f"٥ز نقول الأقسام: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار نقول الأقسام فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_ajnas.py"])
    report.append(f"٥ح جدول الأجناس: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأجناس فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_jamad.py"])
    report.append(f"٥ط القطعة الثانية والنظامان: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار القطعة الثانية والنظامين فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_shabaka.py"])
    report.append(f"٥ي جدول العلاقات: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول العلاقات فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_hawass.py"])
    report.append(f"٥ك جدول الحواسّ: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الحواسّ فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_awwaliyyat.py"])
    report.append(f"٥ل جدول الأوّليات: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأوّليات فشل:\n" + out[-800:])
    code, out = run([sys.executable, "-I", "tahaqquq/test_azmina.py"])
    report.append(f"٥م جدول الأزمنة: {out.strip().splitlines()[-1] if out.strip() else '?'}")
    if code != 0:
        fails.append("اختبار جدول الأزمنة فشل:\n" + out[-800:])
    mdir = os.environ.get("MUDAA_DIR")
    if mdir and os.path.isdir(mdir):
        code, out = run([sys.executable, "-I", "mudaat/idaa.py", "tahaqqaq", mdir])
        report.append(f"٥د بصمات المودَعات الحاضرة: {out.count('مطابق')} مطابق، {out.count('تغيّر')} تغيّر")
        if code != 0:
            fails.append("مودَع تغيّرت بصمته:\n" + out)

    if "--bila-tafrat" not in sys.argv:
        tafrat = json.load(open(os.path.join(ROOT, "tahaqquq", "tafrat.json"), encoding="utf-8"))
        alive = []
        for t in tafrat:
            tmp = tempfile.mkdtemp()
            dst = os.path.join(tmp, "p")
            # تُنسخ مخرجات البناء (.lake) أيضًا ليكون بناء الطفرة تدريجيًّا لا من الصفر
            shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns("__pycache__", "mustakshif", "jalsa_haqiqiyya_out"))
            path = os.path.join(dst, t["milaf"])
            s = open(path, encoding="utf-8").read()
            if t["min"] not in s:
                alive.append(f"{t['ism']} (الاقتباس غاب: عدّل الطفرة مع الكود)")
                shutil.rmtree(tmp)
                continue
            open(path, "w", encoding="utf-8").write(s.replace(t["min"], t["ila"], 1))
            code, _ = run(["lake", "build"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "mawsua/test_mawsua.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "mudaat/test_idaa.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_qari.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_awamil.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_aqsam.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_ajnas.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_jamad.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_shabaka.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_hawass.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_awwaliyyat.py"], cwd=dst)
            if code == 0:
                code, _ = run([sys.executable, "-I", "tahaqquq/test_azmina.py"], cwd=dst)
            if code == 0:
                alive.append(t["ism"])
            shutil.rmtree(tmp)
        report.append(f"٦ الطفرات: قُتلت {len(tafrat) - len(alive)} من {len(tafrat)}")
        if alive:
            fails.append("طفرات عاشت: " + "، ".join(alive))
    else:
        report.append("٦ الطفرات: تُركت بطلب (--bila-tafrat)")

    print("\n".join(report), flush=True)   # التقرير أوّلًا ثمّ الأسباب، بترتيبٍ واحد حين يُجمع المخرجان (2>&1) في الخطّاف
    if fails:
        print("\n".join(fails), file=sys.stderr, flush=True)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
