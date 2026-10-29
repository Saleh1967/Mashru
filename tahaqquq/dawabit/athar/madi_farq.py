"""فروقُ صورة الماضي (`madiSura` في Nizam/Athar.lean) بين نسخها على صيغٍ مولَّدة. عدُّ أداةٍ لا اختبار، بلا وسم.

الصيغُ: لخمسةٍ وعشرين فعلًا من أصنافٍ (الصحيحُ بحركات العين الثلاث، والمضعَّف، والأجوف، والناقص، والمهموز، والمثال، وفَعَّلَ، وفَاعَلَ وفَاعَّ،
والرباعيّ وفَوْعَلَ، والمثلُ قبل الضمير، وثلاثةٌ من أفعال جدول العوامل: كَانَ وكَادَ وعَسَى) الغائبُ والغائبةُ بتاءٍ ساكنةٍ أو مكسورة، ومعهما ضميرٌ منصوبٌ
أو بدونه، وكلاهما بسابقة «فَ» أو «وَ»، والغائبُ موقوفًا بسكون آخره (إلّا المضعَّفَ والمنتهي بحرف مدّ)، والضمائرُ المرفوعةُ المتحرّكةُ الثمانية وواوُ الجماعة وألفُ الاثنين ومعها ضميرٌ منصوبٌ
أو بدونه، والمضارعُ المجزومُ للغائب بلام الأمر مكسورةً أو ساكنةً بعد «فَ» أو «وَ» (إلّا «عَسَى»: لا مضارعَ له)؛ وستَّ عشرةَ كلمةً قد لا تكون فعلًا
(ومنها ما يكون فعلًا في اللسان: «مَعَكَ» س191916، و«عَلَّكَ» س209944، و«عَلَّ» س209946، و«حَاشَ» س122916، و«لَاتَ» س31016). وهي مولَّدةٌ بنقش الحركات لا من معجم، وفي بعضها ما لا تقوله العرب (ومنه إدغامُ المثل قبل الضمير بطريقةٍ
واحدة). فالعدُّ على هذه الصيغ وحدها، لا على اللغة.

تُقرأ خلاياها بالقارئ (`qari --khalaya`)، ثمّ يحسب Lean `madiSura` الحاليّة عليها من البيئة المبنيّة (`lake env lean --stdin`)، وتحسب مرآتان بايثون
نسختيها في 86aca8d وcb5502f؛ ومرآةُ الحاليّة تُقارَن بحساب Lean فإن اختلفتا خرج 1. ويكتب الفروقَ بأصنافها في ملفّ المخرج.

التشغيل: python3 -I tahaqquq/dawabit/athar/madi_farq.py <ملفّ المخرج .md>
"""
import collections
import pathlib
import subprocess
import sys
import tempfile

JADHR = pathlib.Path(__file__).resolve().parent.parent.parent.parent
QARI = JADHR / ".lake" / "build" / "bin" / "qari"

AFAL = {
    # (الغائب، الغائبةُ قبل التاء، قبل الضمير المتحرّك، قبل الواو، قبل ألف الاثنين)
    "sahih_a": ("ضَرَبَ", "ضَرَبَ", "ضَرَبْ", "ضَرَبُ", "ضَرَبَ"),
    "sahih_i": ("عَلِمَ", "عَلِمَ", "عَلِمْ", "عَلِمُ", "عَلِمَ"),
    "sahih_u": ("كَرُمَ", "كَرُمَ", "كَرُمْ", "كَرُمُ", "كَرُمَ"),
    "mudaaf": ("مَدَّ", "مَدَّ", "مَدَدْ", "مَدُّ", "مَدَّ"),
    "mudaaf_t": ("بَتَّ", "بَتَّ", "بَتَتْ", "بَتُّ", "بَتَّ"),
    "ajwaf_q": ("قَالَ", "قَالَ", "قُلْ", "قَالُ", "قَالَ"),
    "ajwaf_b": ("بَاعَ", "بَاعَ", "بِعْ", "بَاعُ", "بَاعَ"),
    "ajwaf_m": ("مَاتَ", "مَاتَ", "مُتْ", "مَاتُ", "مَاتَ"),
    "naqis_r": ("رَمَى", "رَمَ", "رَمَيْ", "رَمَ", "رَمَيَ"),
    "naqis_d": ("دَعَا", "دَعَ", "دَعَوْ", "دَعَ", "دَعَوَ"),
    "naqis_b": ("بَقِيَ", "بَقِيَ", "بَقِي", "بَقُ", "بَقِيَ"),
    "mahmuz_l": ("رَأَى", "رَأَ", "رَأَيْ", "رَأَ", "رَأَيَ"),
    "fa33al": ("كَلَّمَ", "كَلَّمَ", "كَلَّمْ", "كَلَّمُ", "كَلَّمَ"),
    "fa33a": ("رَبَّى", "رَبَّ", "رَبَّيْ", "رَبَّ", "رَبَّيَ"),
    "faa3al": ("قَاتَلَ", "قَاتَلَ", "قَاتَلْ", "قَاتَلُ", "قَاتَلَ"),
    "faa33": ("حَاجَّ", "حَاجَّ", "حَاجَجْ", "حَاجُّ", "حَاجَّ"),
    "ruba3i": ("دَحْرَجَ", "دَحْرَجَ", "دَحْرَجْ", "دَحْرَجُ", "دَحْرَجَ"),
    "fawal": ("حَوْقَلَ", "حَوْقَلَ", "حَوْقَلْ", "حَوْقَلُ", "حَوْقَلَ"),
    "mahmuz_a": ("سَأَلَ", "سَأَلَ", "سَأَلْ", "سَأَلُ", "سَأَلَ"),
    "mithal": ("وَجَدَ", "وَجَدَ", "وَجَدْ", "وَجَدُ", "وَجَدَ"),
    "sakata": ("سَكَتَ", "سَكَتَ", "سَكَتْ", "سَكَتُ", "سَكَتَ"),
    "sakana": ("سَكَنَ", "سَكَنَ", "سَكَنْ", "سَكَنُ", "سَكَنَ"),
    "jadwal_kana": ("كَانَ", "كَانَ", "كُنْ", "كَانُ", "كَانَ"),
    "jadwal_kada": ("كَادَ", "كَادَ", "كِدْ", "كَادُ", "كَادَ"),
    "jadwal_asa": ("عَسَى", "عَسَ", "عَسَيْ", "عَسَ", "عَسَيَ"),
}
# المضارعُ المجزومُ للغائب، لصيغ لام الأمر
MAJZUM = {
    "sahih_a": "يَضْرِبْ", "sahih_i": "يَعْلَمْ", "sahih_u": "يَكْرُمْ", "mudaaf": "يَمُدَّ", "mudaaf_t": "يَبُتَّ", "ajwaf_q": "يَقُلْ",
    "ajwaf_b": "يَبِعْ", "ajwaf_m": "يَمُتْ", "naqis_r": "يَرْمِ", "naqis_d": "يَدْعُ", "naqis_b": "يَبْقَ", "mahmuz_l": "يَرَ",
    "fa33al": "يُكَلِّمْ", "fa33a": "يُرَبِّ", "faa3al": "يُقَاتِلْ", "faa33": "يُحَاجَّ", "ruba3i": "يُدَحْرِجْ", "fawal": "يُحَوْقِلْ",
    "mahmuz_a": "يَسْأَلْ", "mithal": "يَجِدْ", "sakata": "يَسْكُتْ", "sakana": "يَسْكُنْ", "jadwal_kana": "يَكُنْ", "jadwal_kada": "يَكَدْ",
}
MUTAHARRIK = ["تُ", "تَ", "تِ", "تُمَا", "تُمْ", "تُنَّ", "نَا", "نَ"]
MANSUB = ["", "كَ", "كِ", "هُ", "هَا", "نِي", "نَا", "كُمْ", "هُمْ"]
LAYSA_FILAN = ["جَعْفَرَ", "ذَلِكَ", "هَذَا", "لَيْتَكَ", "عَلَّكَ", "لَاتَ", "كَأَنَّكَ", "بَيْتَ", "ضَرْبَ", "عُمَرَ", "لَكَ", "فَمَا",
               "مَعَكَ", "عَلَّ", "حَاشَ", "وَلَكَ"]


def siyagh():
    out = []
    for k, (g, gf, s1, s2, s3) in AFAL.items():
        for o in MANSUB:
            out.append((k, "الغائب" + ("+منصوب" if o else ""), (g[:-1] + "ا" if o and g.endswith("ى") else g) + o))
            out.append((k, "الغائبة بتاءٍ ساكنة" + ("+منصوب" if o else ""), gf + "تْ" + o))
            if not o:
                out.append((k, "الغائبة بتاءٍ مكسورة", gf + "تِ"))
                if not g.endswith(("ى", "ا")) and "ّ" not in g[-2:]:  # المضعَّفُ لا يُوقف عليه هنا
                    out.append((k, "الغائب موقوفًا", g[:-1] + "ْ"))
                for s in ("فَ", "وَ"):
                    out.append((k, "سابقة على الغائب", s + g))
                    out.append((k, "سابقة على الغائبة", s + gf + "تْ"))
        for m in MUTAHARRIK:
            for o in MANSUB:
                if s1.endswith("تْ") and m.startswith("ت") or s1.endswith("نْ") and m.startswith("ن"):
                    w = s1[:-1] + "ّ" + m[1:]  # إدغامُ المثل
                else:
                    w = s1 + m
                if m == "تُمْ" and o:
                    w = w[:-1] + "ُو"
                out.append((k, "ضميرٌ مرفوعٌ متحرّك" + ("+منصوب" if o else ""), w + o))
        for o in MANSUB:
            waw = (s2 + "وْ" if s2.endswith("َ") else s2 + "و") + ("ا" if not o else "") + o
            out.append((k, "واو الجماعة" + ("+منصوب" if o else ""), waw))
            out.append((k, "ألف الاثنين" + ("+منصوب" if o else ""), s3 + "ا" + o))
        if k in MAJZUM:
            for s in ("لِ", "فَلْ", "وَلْ"):
                out.append((k, "لام الأمر" + ("" if s == "لِ" else " بعد سابقة"), s + MAJZUM[k]))
    out += [("laysa_fil", "قد لا يكون فعلًا", w) for w in LAYSA_FILAN]
    return out


def ras(k):
    return k[0] % 4 == 0 and k[0] // 4 not in (0, 14, 11, 18)


def m_86aca8d(k):
    z = k[-1]
    p = k[-2] if len(k) >= 2 else None
    return (ras(k) and (z % 4 == 0 or (z in (75, 74) and p is not None and p % 4 == 0))
            and not (z // 4 in (18, 14) and p is not None and p % 4 == 3 and p // 4 != 2))


def wazn_cb5502f(k):
    if len(k) == 3:
        return k[2] % 4 == 0 and (k[1] % 4 != 3 or k[1] == 11 or k[1] // 4 == k[2] // 4)
    if len(k) == 4:
        return k[2] % 4 == 0 and k[3] % 4 == 0 and k[1] % 4 == 3
    return False


def m_cb5502f(k):
    return ras(k) and (wazn_cb5502f(k) or (k[-1] in (75, 74) and wazn_cb5502f(k[:-1])))


def wazn_hali(k):
    if len(k) == 3:
        return k[2] % 4 == 0 and (k[1] % 4 != 3 or k[1] == 11 or k[1] // 4 == k[2] // 4)
    if len(k) == 4:
        _, b, c, d = k
        return d % 4 == 0 and ((c % 4 == 0 and b % 4 == 3) or (b == 11 and c % 4 == 3 and c // 4 == d // 4))
    return False


def m_hali(k):
    if not ras(k):
        return False
    if wazn_hali(k):
        return True
    s = k[:-1]
    return k[-1] in (75, 74) and (wazn_hali(s) or (len(s) == 2 and s[1] % 4 == 0))


LEAN = """import Nizam.Athar
open Nizam.Athar
#eval show IO Unit from do
  let s ← IO.FS.readFile "{p}"
  for line in s.splitOn "\\n" do
    if line.isEmpty then continue
    IO.println (if madiSura ((line.splitOn ",").map String.toNat!) then "1" else "0")
"""


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    sg = siyagh()
    with tempfile.TemporaryDirectory() as d:
        tsv = pathlib.Path(d) / "s.tsv"
        tsv.write_text("".join(f"w{i}\t{w}\n" for i, (_, _, w) in enumerate(sg)), encoding="utf-8")
        r = subprocess.run([str(QARI), "--khalaya", str(tsv)], capture_output=True, text=True, check=True)
        khalaya = []
        for line in r.stdout.splitlines():
            p = line.split("\t")
            khalaya.append([int(x) for x in p[2].split(";")[0].split(",")] if len(p) > 2 and p[1] == "QABUL" else None)
        if len(khalaya) != len(sg) or any(k is None for k in khalaya):
            print("القارئ لم يقرأ كلَّ الصيغ")
            return 1
        ks = pathlib.Path(d) / "ks.txt"
        ks.write_text("".join(",".join(map(str, k)) + "\n" for k in khalaya))
        r = subprocess.run(["lake", "env", "lean", "--stdin"], input=LEAN.format(p=ks), cwd=JADHR, capture_output=True, text=True)
        lean = [x.strip() == "1" for x in r.stdout.splitlines() if x.strip() in ("0", "1")]
    if r.returncode != 0 or len(lean) != len(sg):
        print("تعذّر حسابُ madiSura بـLean: " + (r.stdout + r.stderr)[-300:])
        return 1
    ikhtilaf = [w for (_, _, w), k, b in zip(sg, khalaya, lean) if b != m_hali(k)]
    if ikhtilaf:
        print(f"مرآةُ الحاليّة تخالف Lean في {len(ikhtilaf)}: {ikhtilaf[:5]}")
        return 1
    sutur = [f"# فروقُ صورة الماضي على {len(sg)} صيغة", "",
             "مخرجُ `tahaqquq/dawabit/athar/madi_farq.py` (عدُّ أداةٍ بلا وسم؛ الحاليّةُ بحساب Lean، ومرآتُها تطابقه في كلّ الصيغ).", ""]
    for ism, (a, b) in (("86aca8d ← cb5502f", (m_86aca8d, m_cb5502f)), ("cb5502f ← الحاليّة", (m_cb5502f, m_hali)),
                        ("86aca8d ← الحاليّة", (m_86aca8d, m_hali))):
        c = collections.defaultdict(list)
        for (sinf, naw, w), k in zip(sg, khalaya):
            x, y = a(k), b(k)
            if x != y:
                c[(naw, "تُقبل" if y else "تُردّ")].append(w)
        sutur += [f"## {ism}: {sum(len(v) for v in c.values())}", ""]
        for (naw, ittijah), ws in sorted(c.items(), key=lambda kv: -len(kv[1])):
            sutur.append(f"- {naw}، صارت {ittijah}: {len(ws)} — " + "، ".join(ws[:8]))
        sutur.append("")
    c = collections.defaultdict(list)
    for (sinf, naw, w), b in zip(sg, lean):
        if b:
            c[naw].append(w)
    sutur += [f"## ما تقبله الحاليّة: {sum(len(v) for v in c.values())}", ""]
    for naw, ws in sorted(c.items(), key=lambda kv: -len(kv[1])):
        sutur.append(f"- {naw}: {len(ws)} — " + "، ".join(ws))
    pathlib.Path(sys.argv[1]).write_text("\n".join(sutur) + "\n", encoding="utf-8")
    print(f"كُتب {sys.argv[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
