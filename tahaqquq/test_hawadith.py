"""حوادثُ الدمج على تاريخ git الحقيقيّ: كيف وقع الفقد (بإعادة الدمج بـ git merge-tree)، وأنّ البند ٤أ يكشفه بدالّة البوّابة نفسِها
(`bawwaba.tafrat_naqisa`)؛ ثمّ دمجاتُ السجلّ (٣–١٠) يكشفها البند ٤ج (`bawwaba.dabt_naqis`).

١. 767e09b (دمجُ main في hawkama/brotokol): أضاف main ‏(b503857) سبعَ طفرات (P163–P169) على أساسٍ (916746e) خلا منها؛ وفي
   tafrat.json تعارضٌ نصّيّ وقعت السبعُ في كتلته، وحلُّ كلّ كتلةٍ بطرف الفرع (dfa7701) يعيد ملفَّ 767e09b حرفًا بحرف.
٢. feb12a8 (دمجُ origin/main في jisr/iqtiran-jins-sigha، طلب #35): الفرعُ (1356f61) خلا من 13 طفرةً في الأساس (916746e) بلا شاهد —
   خلوٌّ ورثه من دمجٍ سابق (9453f0b، في «ما ضُبطتُ عليه») — وأبقاها main (f5fbaae). في الملفّ كتلةُ تعارضٍ واحدة وقعت فيها تسعٌ
   (P154–P162) فعادت بحلّها، وأربعٌ (P150–P153 بأسمائها أدناه) خارجها في قطعةٍ لا تتداخل، فحمل git حذفَها بلا تعارض.
٣–١٠. ثماني دمجاتٍ لـ main في فروعٍ على GitHub (كلُّ ما في `git rev-list --merges --all` ممّا أسقط بندًا لم يكن في نقطة الالتقاء)
   حلّت تعارضَ آخر CLAUDE.md بطرف الفرع، فغاب من الفرع بندٌ في «ما ضُبطتُ عليه» كان في طرف main:
   - 4b4db8f (في aql/adawat-maani) و43d9179 (في jisr/tartib-mamul): بندُ «HALLUCINATED_REFERENCE وخرقٌ لمادّة السلطة (٩)» (2026-10-17)؛
     بلغ main بـ #28.
   - 5d278a1 (في jisr/tartib-mamul): بندُ «أدوات المعاني» (2026-10-17)؛ بلغ main بـ #29.
   - dfa7701 (في hawkama/brotokol): بندُ «خمسُ مخالفاتٍ … في سند الاقتباسات» (2026-10-18)؛ لم يبلغ main.
   - 9edde9c (في jisr/utur-sabab) وb66e004 (في jisr/majhul-sabab): بندُ «أداةُ الطفرات تعدّ قتلَ المعالج» (2026-10-20)؛ بلغ main بـ #59.
   - 79056cf (في jisr/utur-sabab): بندُ «المجهول» (2026-10-20)؛ واستُعيد في e44715c قبل دمج #58.
   - d3ca615 (في hawkama/khitta-jabr-v4): بندُ «تحديث فرع الطبقة الثالثة (#58)» (2026-10-21)؛ بلغ main بـ #64.
   وتُعيد البنودَ الأربعةَ التي بلغت main طلبُ #65.
التوقّعات أسماءٌ وأوائلُ بنودٍ مكتوبةٌ باليد من الحوادث، لا من مخرج الدوالّ. وأساسُ ٤أ في كلٍّ طرفُ main (قاعدةُ الطلب على CI)؛ والأساسُ من
طرف الفرع لا يكشف شيئًا (الضابط السلبيّ) — فالكشفُ يتوقّف على اختيار الأساس.
ما هنا مفحوصٌ للحادثتين ١ و٢: الآليّةُ (بإعادة الدمج) والكشف؛ وللدمجات ٣–١٠: الأبوان والكشفُ وحدَهما (لا الآليّة). والمنعُ (لقائمة الطفرات، ١–٢) مبرهنٌ في Nizam/Damj.lean: `la_faqd` و`la_faqd_janib`/`la_faqd_janib_b` لكلّ مدخل، و
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

# دمجاتُ السجلّ: أوّلُ البند الغائب، مكتوبًا باليد من طرف main
HAWADITH_DABT = {
    "43d9179200aca7bd7cfce8d5df44fea6e2935fd1": {
        "abawan": ("5affac0dee368f71d1eabbf9f59b76082654e877", "acbe8174dfb07c28330acfaf89751af99d4ed658"),
        "naqis": "- 2026-10-17 — HALLUCINATED_REFERENCE وخرقٌ لمادّة السلطة (٩) في ختم كتب النبهاني الأربعة"},
    "dfa77010f0fbd7c81aba3624e9d9c0600c06d7db": {
        "abawan": ("7a377edd3798485c0b2b1ba1ba36c20a77d31263", "916746ecea4a64837991a3150a3d55b7684775bc"),
        "naqis": "- 2026-10-18 — خمسُ مخالفاتٍ CLAIM_ABOVE_ITS_SUPPORT في سند"},
    "4b4db8f455c2d1447b1d3f12904736d33bda31fc": {
        "abawan": ("f1d2654c0f117063f0062e77e6600896ca9e3ffd", "acbe8174dfb07c28330acfaf89751af99d4ed658"),
        "naqis": "- 2026-10-17 — HALLUCINATED_REFERENCE وخرقٌ لمادّة السلطة (٩) في ختم كتب النبهاني الأربعة"},
    "5d278a15f55d6d180388302c0de6098f3094a202": {
        "abawan": ("795b8251611438a2acca42f65dc9808949f0a598", "339c460c4949c2574189761f02c42997b171e469"),
        "naqis": "- 2026-10-17 — CLAIM_ABOVE_ITS_SUPPORT في قطعة أدوات المعاني"},
    "9edde9c790ea0ae5709d7046c696bdb0136af0f6": {
        "abawan": ("f4ac9449d0c439cd6c1166a3dfbc6ad6631e0b0c", "0801e04e64f5fd64a1b59b8410e9d1298fa4b134"),
        "naqis": "- 2026-10-20 — أداةُ الطفرات تعدّ قتلَ المعالج قتلًا للطفرة"},
    "b66e00419528e39438303ead0353ff632f38b9aa": {
        "abawan": ("1f8d2dca154c454cf7c04578c3b197ac41c5a86e", "0801e04e64f5fd64a1b59b8410e9d1298fa4b134"),
        "naqis": "- 2026-10-20 — أداةُ الطفرات تعدّ قتلَ المعالج قتلًا للطفرة"},
    "79056cfce13fee11d91923deb3bde6f48862c0fe": {
        "abawan": ("9edde9c790ea0ae5709d7046c696bdb0136af0f6", "20587e65e8db196bc68083cc825f002dc5a70268"),
        "naqis": "- 2026-10-20 — المجهول (LC06، `Jisr/JisrDal.lean`)، ضبطه المراجع المستقلّ"},
    "d3ca615741e511f0dd867e083b0d5f6e1d332339": {
        "abawan": ("32bb7b46e656336c40bef01e846f77ed0fe155e2", "70ca1c22c65fcff2e77a7c627e5a430d3826aba0"),
        "naqis": "- 2026-10-21 — تحديثُ فرع الطبقة الثالثة (#58) من main بعد دمج #62"},
}


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=300)
    return p.returncode, p.stdout


def asmaa(sha):
    code, txt = git("show", f"{sha}:tahaqquq/tafrat.json")
    assert code == 0, f"تعذّرت قراءة tafrat.json عند {sha[:7]}"
    return bawwaba.asmaa_tafrat(txt)


def bunud(sha):
    code, txt = git("show", f"{sha}:CLAUDE.md")
    assert code == 0, f"تعذّرت قراءة CLAUDE.md عند {sha[:7]}"
    return bawwaba.bunud_dabt(txt)


def damj_nassi(p1, p2):
    """ملفُّ tafrat.json كما يخرجه git merge-tree بكتل تعارضه، أو None إن لم يتوفّر --write-tree."""
    code, out = git("merge-tree", "--write-tree", p1, p2)
    if code not in (0, 1) or not out.strip():
        return None
    code, txt = git("show", f"{out.split()[0]}:tahaqquq/tafrat.json")
    return txt if code == 0 else None


def main():
    if any(git("cat-file", "-e", f"{sha}^{{commit}}")[0] != 0 for sha in [*HAWADITH, *HAWADITH_DABT]):
        print("حوادث الدمج: لم يُشغَّل (التاريخ غير حاضر؛ استنسخ بلا --depth)")
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
    dabt = 0
    for sha, h in HAWADITH_DABT.items():
        code, out = git("rev-list", "--parents", "-n", "1", sha)
        assert code == 0 and tuple(out.split()[1:]) == h["abawan"], (sha[:7], out)
        far, ra = h["abawan"]
        hali = bunud(sha)
        # الكشف: ٤ج على طرف main يسمّي البندَ الغائب وحده؛ وعلى طرف الفرع لا يسمّي شيئًا
        naqis = bawwaba.dabt_naqis(bunud(ra), hali, [])
        assert len(naqis) == 1 and naqis[0].startswith(h["naqis"]), (sha[:7], naqis)
        assert bawwaba.dabt_naqis(bunud(far), hali, []) == [], sha[:7]
        dabt += 1
    print(f"حوادث الدمج: ٤أ {ok}/{len(HAWADITH)} (يسمّي ما أسقطه كلُّ دمج: 7 و4؛ والآليّة {aliyya}/{len(HAWADITH)})؛ "
          f"و٤ج {dabt}/{len(HAWADITH_DABT)} (يسمّي البندَ الذي أسقطه كلُّ دمجٍ من الثمانية)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
