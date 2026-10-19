"""حادثتا الدمج على تاريخ git الحقيقيّ: كيف وقع الفقد (بإعادة الدمج بـ git merge-tree)، وأنّ البند ٤أ يكشفه بدالّة البوّابة نفسِها
(`bawwaba.tafrat_naqisa`).

١. 767e09b (دمجُ main في hawkama/brotokol): أضاف main ‏(b503857) سبعَ طفرات (P163–P169) على أساسٍ (916746e) خلا منها؛ وفي
   tafrat.json تعارضٌ نصّيّ وقعت السبعُ في كتلته، وحلُّ كلّ كتلةٍ بطرف الفرع (dfa7701) يعيد ملفَّ 767e09b حرفًا بحرف.
٢. feb12a8 (دمجُ origin/main في jisr/iqtiran-jins-sigha، طلب #35): الفرعُ (1356f61) خلا من 13 طفرةً في الأساس (916746e) بلا شاهد —
   خلوٌّ ورثه من دمجٍ سابق (9453f0b، في «ما ضُبطتُ عليه») — وأبقاها main (f5fbaae). في الملفّ كتلةُ تعارضٍ واحدة وقعت فيها تسعٌ
   (P154–P162) فعادت بحلّها، وأربعٌ (P150–P153 بأسمائها أدناه) خارجها في قطعةٍ لا تتداخل، فحمل git حذفَها بلا تعارض.
التوقّعات أسماءٌ مكتوبةٌ باليد من الحادثتين، لا من مخرج الدوالّ. وأساسُ ٤أ في كلٍّ طرفُ main (قاعدةُ الطلب على CI)؛ والأساسُ من
طرف الفرع لا يكشف شيئًا (الضابط السلبيّ) — فالكشفُ يتوقّف على اختيار الأساس.
ما هنا مفحوصٌ: الآليّةُ والكشف. والمنعُ مبرهنٌ في Nizam/Damj.lean: `la_faqd` و`la_faqd_janib`/`la_faqd_janib_b` لكلّ مدخل، و
`shahid_hadith_767e09b`/`shahid_hadith_35` على نموذجهما.
بلا تاريخٍ حاضر (استنساخٌ ضحل) لا يُشغَّل ويقول ذلك؛ وبلا `git merge-tree --write-tree` (git < 2.38) تُترك فحوصُ الآليّة ويقول ذلك.
التشغيل: python3 -I tahaqquq/test_hawadith.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tahaqquq"))
import bawwaba  # noqa: E402

KUTLA = re.compile(r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n", re.S)
SAB = ["P163_khatt_asas_fail_open", "P164_elan_bootstrap_false_success", "P165_lean_checksum_bypass",
       "P166_lean_download_unbounded", "P167_naql_binadaraja_hadd", "P168_naql_yasluhu_and_to_or",
       "P169_naql_yasluhu_yatruk_qail"]
ARBA = ["P150_tadammun_ala_ghayr_juz", "P151_luzum_min_taraduf", "P152_formula_fi_tafsir", "P153_taalil_bila_tasmiya"]
TIS = ["P154_matufat_ajza", "P155_naht_bithulathi_wahid", "P156_ishtirak_huwiyya", "P157_uqad_mukhtalita",
       "P158_hiss_bila_ittihad", "P159_naht_bithulathi_wahid_py", "P160_idmar_dun_majaz", "P161_bila_qarina_la_hukm",
       "P162_mirat_tarjih_py"]
HAWADITH = {
    "767e09b77d5ec8dec4878ebb971a1f45e767437b": {
        "abawan": ("dfa77010f0fbd7c81aba3624e9d9c0600c06d7db", "b503857f07f9baf430892b7db1e661f0be74e825"),
        "asas": "916746ecea4a64837991a3150a3d55b7684775bc", "naqisa": SAB},
    "feb12a8c1ac5f83aa3646fe194ec5cf31c6e5ad6": {
        "abawan": ("1356f6139619f15d0f587ad8291a99a4b58d6827", "f5fbaae724f7948a70181586554b935538227843"),
        "asas": "916746ecea4a64837991a3150a3d55b7684775bc", "naqisa": ARBA},
}


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=300)
    return p.returncode, p.stdout


def asmaa(sha):
    code, txt = git("show", f"{sha}:tahaqquq/tafrat.json")
    assert code == 0, f"تعذّرت قراءة tafrat.json عند {sha[:7]}"
    return bawwaba.asmaa_tafrat(txt)


def damj_nassi(p1, p2):
    """ملفُّ tafrat.json كما يخرجه git merge-tree بكتل تعارضه، أو None إن لم يتوفّر --write-tree."""
    code, out = git("merge-tree", "--write-tree", p1, p2)
    if code not in (0, 1) or not out.strip():
        return None
    code, txt = git("show", f"{out.split()[0]}:tahaqquq/tafrat.json")
    return txt if code == 0 else None


def main():
    if any(git("cat-file", "-e", f"{sha}^{{commit}}")[0] != 0 for sha in HAWADITH):
        print("حادثتا الدمج: لم يُشغَّل (التاريخ غير حاضر؛ استنسخ بلا --depth)")
        return 0
    ok, aliyya = 0, 0
    for sha, h in HAWADITH.items():
        code, out = git("rev-list", "--parents", "-n", "1", sha)
        assert code == 0 and tuple(out.split()[1:]) == h["abawan"], (sha[:7], out)
        code, out = git("merge-base", *h["abawan"])
        assert out.strip() == h["asas"], (sha[:7], out)
        far, ra = h["abawan"]
        hali = asmaa(sha)
        # الكشف: ٤أ على أساسٍ هو طرفُ main يسمّي المفقود؛ وعلى طرف الفرع لا يسمّي شيئًا
        assert bawwaba.tafrat_naqisa(asmaa(ra), hali, []) == h["naqisa"], sha[:7]
        assert bawwaba.tafrat_naqisa(asmaa(far), hali, []) == [], sha[:7]
        # الآليّة: إعادةُ الدمج النصّيّ
        nass = damj_nassi(far, ra)
        if nass is not None:
            kutal = KUTLA.findall(nass)
            kharij = KUTLA.sub("", nass)
            if sha.startswith("767e09b"):
                assert kutal and all(n not in kharij and any(n in k[1] for k in kutal) for n in SAB), sha[:7]
                code, asli = git("show", f"{sha}:tahaqquq/tafrat.json")
                assert KUTLA.sub(lambda m: m.group(1), nass) == asli, "حلُّ الكتل بطرف الفرع لا يعيد 767e09b"
            else:
                asas = asmaa(h["asas"])
                assert all(n in asas and n not in asmaa(far) for n in ARBA + TIS), sha[:7]
                assert len(kutal) == 1 and all(n not in nass for n in ARBA), sha[:7]
                assert all(n in kutal[0][1] and n not in kharij for n in TIS) and all(n in hali for n in TIS), sha[:7]
            aliyya += 1
        ok += 1
    print(f"حادثتا الدمج: {ok}/{len(HAWADITH)} (٤أ يسمّي ما أسقطه كلُّ دمج: 7 و4؛ والآليّة {aliyya}/{len(HAWADITH)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
