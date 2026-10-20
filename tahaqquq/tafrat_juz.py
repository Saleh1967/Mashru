"""تشغيل طفراتٍ مسمّاة وحدها بإجراء البند ٦ في tahaqquq/bawwaba.py نفسِه: يُحكم على نصّ الطفرة (٤ب) في المستودع ثمّ في
النسخة، وتُنسخ الشجرة مع .lake، ويُستبدل أوّلُ ظهور، ثمّ lake build ثمّ اختباراتُ `bawwaba.IKHTIBARAT_TAFRAT` بترتيبها (القائمةُ
نفسُها، لا نسخةٌ منها)، بمهلة البوّابة. للفحص المحلّيّ لما تغيّر من الطفرات؛ والمسح الكامل على CI.
يخرج 1 إن عاشت طفرة، و3 إن بقيت طفرةٌ غيرَ محسومة (حالٌ ثالثة: لا قتلٌ ولا حياة — تجاوزُ المهلة، أو خروجُ lake build بلا خطأٍ في ملفٍّ
مسمّى كقتل المعالج لنفاد الذاكرة، أو اختبارٌ قُتل بإشارة؛ القاعدةُ من `bawwaba.ghayr_mahsum_bina`/`ghayr_mahsum_ikhtibar`)، و2 لاستعمالٍ خاطئ (بلا أسماء، أو اسمٌ لا قيدَ
له، أو اسمٌ مكرَّر في القائمة). المهلة من TAFRAT_JUZ_MUHLA إن عُيّن (للاختبار)، وإلّا 1800 ث كالبوّابة.
التشغيل: python3 -I tahaqquq/tafrat_juz.py <جذر المستودع> <اسم طفرة>...
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

MUHLA = int(os.environ.get("TAFRAT_JUZ_MUHLA", "1800"))   # ثوانٍ، كمهلة run في البوّابة


class GhayrMahsum(Exception):
    """حالٌ ثالثة: لا قتلٌ ولا حياة."""


class TajawuzMuhla(GhayrMahsum):
    """أمرٌ تجاوز المهلة: لا يُعدّ قتلًا (البوّابة تنهار عنده ولا تعدّه قتلًا كذلك)."""


def sabab(out, namat):
    """موضعُ القتل من المخرج: ملفُّ أوّل خطأ بناءٍ في Lean، أو أوّلُ اختبار unittest فشل — ليُرى أنّ الطفرة قُتلت لسببها."""
    m = sorted(set(re.findall(namat, out, re.M)))
    return f" ({'، '.join(m[:4])})" if m else ""


def shaghghil(cmd, cwd):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=MUHLA)
        return p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        raise TajawuzMuhla(f"{' '.join(cmd[-2:])} تجاوز {MUHLA} ث")


def main(argv):
    if len(argv) < 3:
        print("الاستعمال: python3 -I tahaqquq/tafrat_juz.py <جذر المستودع> <اسم طفرة>...", file=sys.stderr)
        return 2
    root, names = os.path.abspath(argv[1]), argv[2:]
    sys.path.insert(0, os.path.join(root, "tahaqquq"))
    import bawwaba  # عيوبُ النصّ (٤ب) وقائمةُ الاختبارات من البوّابة نفسِها
    with open(os.path.join(root, "tahaqquq", "tafrat.json"), encoding="utf-8") as f:
        qaima = json.load(f)
    tafrat, mukarrar = {}, []
    for t in qaima:
        if isinstance(t, dict) and isinstance(t.get("ism"), str):
            if t["ism"] in tafrat:
                mukarrar.append(t["ism"])
            tafrat[t["ism"]] = t
    majhul = [n for n in names if n not in tafrat]
    if majhul:
        print("أسماءٌ لا قيدَ لها في tafrat.json:", "، ".join(majhul), file=sys.stderr)
        return 2
    mukarrar = [n for n in names if n in mukarrar]
    if mukarrar:
        print("أسماءٌ مكرَّرة في tafrat.json (البوّابة تشغّل كلَّ قيد):", "، ".join(mukarrar), file=sys.stderr)
        return 2
    tests = list(bawwaba.IKHTIBARAT_TAFRAT)
    print("الاختبارات:", len(tests), flush=True)
    alive, muhla = [], []
    for n in names:
        t = tafrat[n]
        ayb = bawwaba.ayb_tafra(t, root)
        if ayb:
            print(n, "— معيبة (٤ب):", ayb, flush=True)
            alive.append(n)
            continue
        tmp = tempfile.mkdtemp()
        try:
            dst = os.path.join(tmp, "p")
            shutil.copytree(root, dst, ignore=shutil.ignore_patterns("__pycache__", "mustakshif", "jalsa_haqiqiyya_out"))
            ayb = bawwaba.ayb_tafra(t, dst)
            if ayb:
                print(n, "— معيبة في النسخة (٤ب):", ayb, flush=True)
                alive.append(n)
                continue
            path = bawwaba.masar_tafra(t, dst)
            with open(path, encoding="utf-8") as f:
                s = f.read()
            with open(path, "w", encoding="utf-8") as f:
                f.write(s.replace(t["min"], t["ila"], 1))
            try:
                code, out = shaghghil(["lake", "build"], dst)
                ghayr = bawwaba.ghayr_mahsum_bina(code, out)
                if ghayr:
                    raise GhayrMahsum(ghayr)
                why = "lake build" + sabab(out, bawwaba.KHATA_BINA) if code != 0 else None
                if why is None:
                    for x in tests:
                        code, out = shaghghil([sys.executable, "-I", x], dst)
                        ghayr = bawwaba.ghayr_mahsum_ikhtibar(x, code)
                        if ghayr:
                            raise GhayrMahsum(ghayr)
                        if code != 0:
                            why = x + sabab(out, r"^(?:FAIL|ERROR): (\S+)")
                            break
            except TajawuzMuhla as e:
                print(n, "— تجاوز المهلة:", e, flush=True)
                muhla.append(n)
                continue
            except GhayrMahsum as e:
                print(n, "— غيرُ محسومة (لا قتلٌ ولا حياة):", e, flush=True)
                muhla.append(n)
                continue
            print(n, "— قُتلت بـ" + why if why else "— عاشت", flush=True)
            if not why:
                alive.append(n)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    print(f"قُتلت {len(names) - len(alive) - len(muhla)} من {len(names)}" + (f"؛ عاشت: {alive}" if alive else "")
          + (f"؛ غيرُ محسومة (تجاوزُ المهلة أو خروجٌ بلا سببٍ مسمّى): {muhla}" if muhla else ""))
    return 1 if alive else 3 if muhla else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
