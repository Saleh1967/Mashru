"""حادثتا الدمج على تاريخ git الحقيقيّ: البند ٤أ يكشف ما أسقطه كلٌّ منهما، بدالّة البوّابة نفسِها (`bawwaba.tafrat_naqisa`).

الحادثتان مسجّلتان في CLAUDE.md («ما ضُبطتُ عليه» 2026-10-19، والبند ٤أ):
١. 767e09b (دمجُ main في hawkama/brotokol): أضاف main ‏(b503857) سبع طفراتٍ على أساسٍ (916746e) خلا منها، وحُلّت كتلةُ التعارض
   في tafrat.json بأخذ طرف الفرع (dfa7701) كلِّه، فغابت السبع.
٢. feb12a8 (دمجُ origin/main في jisr/iqtiran-jins-sigha، طلب #35): في الأساس (916746e) أربعُ طفراتٍ خلا منها الفرعُ (1356f61) بلا
   شاهد، وأبقاها main (f5fbaae)؛ فحمل git الحذفَ بلا تعارضٍ في موضعه (خارج كتلة التعارض الوحيدة في الملفّ، وهي في موضعٍ آخر).
التوقّعات أسماءٌ مكتوبةٌ باليد من الحادثتين، لا من مخرج الدالّة. الأساسُ في كلٍّ طرفُ main (قاعدةُ الطلب على CI)، والحاليّ ناتجُ الدمج.
والمنعُ نفسُه (الدمجُ بالمفتاح يحفظ الطفرات) مبرهنٌ على نموذجهما في Nizam/Damj.lean (`shahid_hadith_767e09b`، `shahid_hadith_35`).
بلا تاريخٍ حاضر (استنساخٌ ضحل) لا يُشغَّل، ويقول ذلك.
التشغيل: python3 -I tahaqquq/test_hawadith.py
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tahaqquq"))
import bawwaba  # noqa: E402

HAWADITH = {
    "767e09b77d5ec8dec4878ebb971a1f45e767437b": {
        "abawan": ("dfa77010f0fbd7c81aba3624e9d9c0600c06d7db", "b503857f07f9baf430892b7db1e661f0be74e825"),
        "naqisa": ["P163_khatt_asas_fail_open", "P164_elan_bootstrap_false_success", "P165_lean_checksum_bypass",
                   "P166_lean_download_unbounded", "P167_naql_binadaraja_hadd", "P168_naql_yasluhu_and_to_or",
                   "P169_naql_yasluhu_yatruk_qail"],
    },
    "feb12a8c1ac5f83aa3646fe194ec5cf31c6e5ad6": {
        "abawan": ("1356f6139619f15d0f587ad8291a99a4b58d6827", "f5fbaae724f7948a70181586554b935538227843"),
        "naqisa": ["P150_tadammun_ala_ghayr_juz", "P151_luzum_min_taraduf", "P152_formula_fi_tafsir",
                   "P153_taalil_bila_tasmiya"],
    },
}


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout


def asmaa(sha):
    code, txt = git("show", f"{sha}:tahaqquq/tafrat.json")
    assert code == 0, f"تعذّرت قراءة tafrat.json عند {sha[:7]}"
    return bawwaba.asmaa_tafrat(txt)


def main():
    if any(git("cat-file", "-e", f"{sha}^{{commit}}")[0] != 0 for sha in HAWADITH):
        print("حادثتا الدمج: لم يُشغَّل (التاريخ غير حاضر؛ استنسخ بلا --depth)")
        return 0
    ok = 0
    for sha, h in HAWADITH.items():
        code, out = git("rev-list", "--parents", "-n", "1", sha)
        assert code == 0 and tuple(out.split()[1:]) == h["abawan"], (sha[:7], out)
        asas, hali = asmaa(h["abawan"][1]), asmaa(sha)
        naqisa = bawwaba.tafrat_naqisa(asas, hali, [])
        assert naqisa == h["naqisa"], (sha[:7], naqisa)
        # ولا يكشف البندُ شيئًا حيث لا فقد: ناتجُ الدمج مقارنًا بنفسه
        assert bawwaba.tafrat_naqisa(hali, hali, []) == []
        ok += 1
    print(f"حادثتا الدمج: {ok}/{len(HAWADITH)} (٤أ يسمّي ما أسقطه كلُّ دمج: 7 و4)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
