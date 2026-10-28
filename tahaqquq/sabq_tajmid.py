"""سبقُ التجميد مقيسًا من التاريخ (مأخوذٌ فكرتُه من `tools/seal_chain.py` في Saleh1967/Algebra، ومبنيٌّ هنا على ضوابط Mashru).

المنهج (`CLAUDE.md` طريقة العمل ٢أ): تُجمَّد حالاتُ الضابط في إيداعٍ قبل الشفرة، والنتيجةُ الأولى على الشفرة المجمَّدة. وكان ذلك يُكتب في
`tajmid.json` و`natija_1.json` قولًا ولا شيءَ يسأل `git` عنه. وههنا يُسأل، لكلّ ضابطٍ في `tahaqquq/dawabit/<اسم>/`:
  مرساةُ التجميد F: أقدمُ إيداعٍ أضاف `cases.json`؛ ومراسي الشفرة C: الإيداعاتُ في حقل `shifra` من `natija_1.json` (`iydaa`)؛
  ومرساةُ النتيجة N: أقدمُ إيداعٍ أضاف `natija_1.json`.
الشروط:
  ١. F سلفٌ صارمٌ لكلّ C (التجميدُ أُودع قبل الشفرة، لا معها).
  ٢. كلُّ C سلفٌ لـN أو هو هو (النتيجةُ الأولى على شفرةٍ أُودعت).
  ٣. بايتاتُ `cases.json` في F بصمتُها `cases_sha256` في `natija_1.json`، وهي بايتاتُه الآن (لم تُغيَّر الحالاتُ بعد التجميد).
حدُّه المعلَن: يُثبت ترتيبَ الإيداعات في التاريخ، لا ترتيبَ الدفع إلى GitHub ولا أنّ البنّاء لم يقرأ الحالات؛ ونسخةٌ ضحلةٌ تُردّ باسمها
(`TARIKH_DAHL`) لا تُعدّ نجاحًا. وضابطُ التحصيل (`tahaqquq/tahsil/`) بصيغةٍ أخرى لا يدخل هنا.
التشغيل: python3 -I tahaqquq/sabq_tajmid.py [جذر المستودع]
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys


def git(jadhr, *args):
    r = subprocess.run(["git", "-C", jadhr, *args], capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


def awwal_idafa(jadhr, rel):
    """أقدمُ إيداعٍ أضاف الملفّ (عبر إعادة التسمية لا)، أو None."""
    code, out = git(jadhr, "log", "--diff-filter=A", "--format=%H", "--reverse", "--", rel)
    lines = out.split("\n") if code == 0 and out else []
    return lines[0] if lines else None


def salaf(jadhr, a, b):
    return subprocess.run(["git", "-C", jadhr, "merge-base", "--is-ancestor", a, b], capture_output=True).returncode == 0


def marasi_shifra(natija):
    sh = natija.get("shifra")
    if isinstance(sh, dict) and "iydaa" in sh:
        return [sh["iydaa"]]
    if isinstance(sh, dict):
        return sorted({v["iydaa"] for v in sh.values() if isinstance(v, dict) and v.get("iydaa")})
    return []


def fahs_dabit(jadhr, ism):
    """أخطاءُ ضابطٍ واحد (قائمةٌ فارغة إن سلم)."""
    d = f"tahaqquq/dawabit/{ism}"
    akhta = []
    try:
        natija = json.load(open(os.path.join(jadhr, d, "natija_1.json"), encoding="utf-8"))
    except (OSError, ValueError) as e:
        return [f"{ism}: natija_1.json لا يُقرأ ({e})"]
    F = awwal_idafa(jadhr, f"{d}/cases.json")
    N = awwal_idafa(jadhr, f"{d}/natija_1.json")
    C = marasi_shifra(natija)
    if not F or not N:
        return [f"{ism}: لا مرساةَ في التاريخ لـ{'cases.json' if not F else 'natija_1.json'}"]
    if not C:
        return [f"{ism}: natija_1.json بلا إيداع شفرة (shifra.iydaa)"]
    for c in C:
        if git(jadhr, "cat-file", "-e", c + "^{commit}")[0] != 0:
            akhta.append(f"{ism}: إيداعُ الشفرة {c[:7]} ليس في التاريخ")
            continue
        if c == F or not salaf(jadhr, F, c):
            akhta.append(f"{ism}: التجميد {F[:7]} ليس سلفًا صارمًا للشفرة {c[:7]}")
        if not salaf(jadhr, c, N):
            akhta.append(f"{ism}: الشفرة {c[:7]} ليست سلفًا للنتيجة الأولى {N[:7]}")
    code, _ = git(jadhr, "cat-file", "-e", f"{F}:{d}/cases.json")
    if code == 0:
        bytes_f = subprocess.run(["git", "-C", jadhr, "show", f"{F}:{d}/cases.json"], capture_output=True).stdout
        b_f = hashlib.sha256(bytes_f).hexdigest()
        b_now = hashlib.sha256(open(os.path.join(jadhr, d, "cases.json"), "rb").read()).hexdigest()
        if b_f != natija.get("cases_sha256") or b_f != b_now:
            akhta.append(f"{ism}: بصمةُ cases.json عند التجميد غيرُ بصمته في natija_1.json أو الآن")
    return akhta


def main(jadhr):
    if os.path.exists(os.path.join(jadhr, ".git", "shallow")) or git(jadhr, "rev-parse", "--is-shallow-repository")[1] == "true":
        print("TARIKH_DAHL: نسخةٌ ضحلة، لا تُقرأ المراسي")
        return 3
    asma = sorted(x for x in os.listdir(os.path.join(jadhr, "tahaqquq", "dawabit"))
                  if os.path.exists(os.path.join(jadhr, "tahaqquq", "dawabit", x, "natija_1.json")))
    kull = []
    for ism in asma:
        a = fahs_dabit(jadhr, ism)
        kull += a
        print(("ok   " if not a else "FAIL ") + ism)
    for a in kull:
        print("  " + a)
    print(f"سبقُ التجميد: {len(asma) - len({a.split(':')[0] for a in kull})} من {len(asma)} ضابطًا")
    return 1 if kull else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
