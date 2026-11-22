"""اختبارُ محاكاة قواعد العمليّة العقليّة (Aql/Muhakat.lean ومرآتُه scripts/muhakat_dayn.py) — البوّابة ٥ت١٤.

١. جدولُ السقوف: يُطبع من Lean نفسِه (`#eval` على وحدة Aql.Muhakat المبنيّة) ويُقارن بتوقّعٍ مكتوبٍ هنا يدويًّا من النصّ (لا من الشفرة)،
   ثمّ بمرآة بايثون. والتوقّعُ: الفرضُ والتخيّلُ ليسا فكرًا (التفكير [79]، [87])؛ والمدحُ والذمّ ليس فكرًا قبل الشرع (ج3 [339])؛
   والوجودُ من الحسّ والأثر والمتواتر قطعيّ وإلّا ظنّيّ (التفكير [38]، [82]، [90])؛ والصفةُ والكنهُ من الأثر ليسا فكرًا (التفكير [83]–[84])،
   ومن المتواتر قطعيّان (التفكير [90])، وإلّا ظنّيّان (التفكير [38])؛ ووجودُ الصفة كالوجود إلّا من الحسّ فظنّيٌّ إلّا بسياسة إسماعيل
   والأثرِ فظنّيّ؛ والملاءمةُ ظنّيّة.
٢. آيةُ الدَّين على المودَعات (يُتخطّى بخروج 0 إن غاب مودَع): عددُ الجمل والكلمات بحسابٍ هنا على السطر نفسِه؛ وكلُّ جملةٍ وجودُها قطعيٌّ
   حقيقة وحكمُها خارجَ النطاق؛ ولا معنى قطعيّ؛ والمعنى الظنّيّ بعدد المرشَّح الواحد؛ والدوافعُ الأربعة مخرجٌ واحد (INV-01)؛ وكلُّ سطر
   شاهدٍ عنوانُ مادّةٍ بجذره في معجمه (يُقرأ السطرُ هنا)؛ والملخّصُ يطابق `tahaqquq/muhakat/natija_1.json` (إعادةُ تشغيل: وصفيّ، لا دقّة).
الطفراتُ في tafrat.json باسم P1650–P1657 (muhakat).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import muhakat_dayn as md  # noqa: E402

JIHAT = ["wujud", "wujudSifa", "sifa", "kunh", "mulaama", "madhDhamm"]
QANAWAT = ["hiss", "athar", "mutawatir", "ahad", "nass", "fard", "takhayyul"]


def tawaqqu(ismail, j, q):
    """التوقّعُ اليدويّ من النصّ (انظر رأس الملفّ)، مستقلٌّ عن saqf في Lean وفي المرآة."""
    if q in ("fard", "takhayyul"):
        return "laFikr"
    if j == "madhDhamm":
        return "laFikr"
    if j == "mulaama":
        return "zanni"
    if j == "wujud":
        return {"hiss": "qati", "athar": "qati", "mutawatir": "qati"}.get(q, "zanni")
    if j == "wujudSifa":
        if q == "mutawatir":
            return "qati"
        if q == "hiss":
            return "qati" if ismail else "zanni"
        return "zanni"
    # sifa, kunh
    if q == "athar":
        return "laFikr"
    if q == "mutawatir":
        return "qati"
    return "zanni"


fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def jadwal_lean():
    path = os.path.join(ROOT, "Aql", "_MuhakatJadwalTmp.lean")
    lines = ["import Aql.Muhakat", "open Aql.Muhakat"]
    for p in ("true", "false"):
        for j in JIHAT:
            for q in QANAWAT:
                lines.append(f'#eval (s!"{p}|{j}|{q}|" ++ (reprStr (saqf {p} .{j} .{q})))')
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        p = subprocess.run(["lake", "env", "lean", path], cwd=ROOT, capture_output=True, text=True, timeout=1200)
    finally:
        if os.path.exists(path):
            os.remove(path)
    if p.returncode != 0:
        fails.append("١: تعذّر تقييم الجدول في Lean:\n" + (p.stdout + p.stderr)[-600:])
        return {}
    out = {}
    for ln in p.stdout.splitlines():
        m = re.fullmatch(r'"(true|false)\|(\w+)\|(\w+)\|Aql\.Muhakat\.Rutba\.(\w+)"', ln.strip())
        if m:
            out[(m.group(1) == "true", m.group(2), m.group(3))] = m.group(4)
    return out


def bab1():
    L = jadwal_lean()
    if not L:
        return
    check(len(L) == 2 * len(JIHAT) * len(QANAWAT), f"١: عددُ خانات Lean {len(L)}")
    for (p, j, q), r in sorted(L.items()):
        check(r == tawaqqu(p, j, q), f"١: Lean saqf {p} {j} {q} = {r}، والمتوقَّع {tawaqqu(p, j, q)}")
        check(md.saqf(p, j, q) == r, f"١: المرآة saqf {p} {j} {q} = {md.saqf(p, j, q)}، وLean {r}")
    for j in JIHAT:
        for q in QANAWAT:
            h = md.hukm(False, j, q, [])
            check(h == ("kharijNitaq" if j == "madhDhamm" else tawaqqu(False, j, q)), f"١: المرآة hukm {j} {q} = {h}")
    check(md.hukm(False, "wujud", "hiss", ["zanni"]) == "zanni", "١: الالتقاءُ في المرآة لا ينزل إلى أضعف المقدّمات")
    check(md.hukm(False, "wujud", "hiss", ["laFikr", "qati"]) == "laFikr", "١: الالتقاءُ في المرآة لا ينزل إلى أضعف المقدّمات")


def bab2(dir_):
    for m in ("quran-simple-enhanced.txt", "lisan.txt", "maqayis.txt"):
        if not os.path.isfile(os.path.join(dir_, m)):
            print(f"٢ تُخطّي: {m} غائب في {dir_}")
            return
    with open(os.path.join(dir_, "quran-simple-enhanced.txt"), encoding="utf-8") as f:
        satr = f.read().split("\n")[288]
    jumal_huna = satr.count("<sel>") + 1
    kalimat_huna = len([w for w in satr.split() if w != "<sel>"])
    m, natayij = md.mulakhkhas(dir_)
    check(m["jumal"] == jumal_huna, f"٢: الجمل {m['jumal']}، وبالعدّ هنا {jumal_huna}")
    check(m["kalimat"] == kalimat_huna, f"٢: الكلمات {m['kalimat']}، وبالعدّ هنا {kalimat_huna}")
    check(m["wujud_qati_haqiqa"] == jumal_huna, "٢: جملةٌ ليس وجودُها قطعيًّا حقيقة")
    check(m["hukm_shari_kharij"] == jumal_huna, "٢: جملةٌ حُكم فيها بالمدح والذمّ قبل الشرع")
    check(m["mana"]["qati"] == 0, "٢: معنًى لفظيٌّ بلغ القطع من نقلٍ آحاد")
    check(m["mana"]["zanni"] == m["halat_jadhr"]["murashshah_wahid"], "٢: المعنى الظنّيّ لا يساوي عددَ المرشَّح الواحد")
    check(m["mana"]["laFikr"] == m["halat_jadhr"]["murashshahun"] + m["halat_jadhr"]["la_murashshah"],
          "٢: ما لا مرشَّحَ واحدًا له لم يُترك «لا حكم»")
    basamat = {d: hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
               for d, v in natayij.items()}
    check(len(natayij) == 4 and len(set(basamat.values())) == 1, "٢: INV-01: الدوافعُ الأربعة لم تُخرج مخرجًا واحدًا")
    with open(os.path.join(dir_, "lisan.txt"), encoding="utf-8") as f:
        lisan = f.read().split("\n")
    with open(os.path.join(dir_, "maqayis.txt"), encoding="utf-8") as f:
        maqayis = f.read().split("\n")
    for row in next(iter(natayij.values())):
        for k in row["kalimat"]:
            for mujam, n in k["shuhud"]:
                ln = (lisan if mujam == "lisan" else maqayis)[n - 1]
                pat = r"^### \$ ([^:\s]+):" if mujam == "lisan" else r"^### \| \(([^)\s]+)\)\s*$"
                mm = re.match(pat, ln)
                check(bool(mm) and md.jl.norm(mm.group(1)) == k["jadhr"],
                      f"٢: سطرُ الشاهد {mujam}:{n} ليس عنوانَ {k['jadhr']}")
    natija = os.path.join(ROOT, "tahaqquq", "muhakat", "natija_1.json")
    with open(natija, encoding="utf-8") as f:
        mahfuz = json.load(f)
    check(mahfuz == m, "٢: الملخّصُ لا يطابق natija_1.json")


def main():
    bab1()
    bab2(os.environ.get("MUDAA_DIR", os.path.expanduser("~/mudaa_dir")))
    if fails:
        print("\n".join(fails))
        print(f"محاكاة العقل: فشل {len(fails)}")
        sys.exit(1)
    print("محاكاة العقل: نجح (جدول السقوف 84 خانة، وآية الدَّين)")


if __name__ == "__main__":
    main()
