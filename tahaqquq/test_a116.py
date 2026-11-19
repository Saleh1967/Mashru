"""A116 المستوردُ من Saleh1967/Alghanem (formal/a116، الإيداع 9d8fa03؛ أمرُ المالك 2026-11-20: «اوافق استوردها واجعلها جزء من Mashru»).

**وسمُ التوقّعات.** «مطابَق» بمعنى الدستور م2: الجداولُ الأربعةُ والثلاثون في `jadawil/a116/` وملفّا البيانات `A116/TawafiqMasfufaData.lean`
و`A116/MizanData.lean` نُقلت بايتًا من Alghanem، حيث يولّدها `a116-table` نفسُه في CI ويقارنها بـ`git diff --exit-code`؛ وهنا يولّدها
`a116-jadwal` (`Qari/A116Jadwal.lean` = `formal/a116/Main.lean` بنصّه) من Lean المبنيّ في Mashru، فتُقارَن بايتًا.
١. كلُّ جدولٍ من الأربعة والثلاثين يطابق مُخرَجَ وضعه (`a116-jadwal <وضع>`) بايتًا.
٢. `masfufa-lean` و`mizan-lean` يطابقان ملفّي البيانات بايتًا.
٣. ملفّاتُ A116 كلُّها تحت `A116/`، والمكتبةُ في lakefile.toml، و`Qari/A116Jadwal.lean` بصمتُه بصمةُ `formal/a116/Main.lean` في الإيداع المسجَّل.
الطفرات: P1642 (صفُّ الإشباع في Model يتغيّر: يقتلها البناء)، P1643 (مُخرَجُ marja يحذف سطرًا: ١).
التشغيل: python3 -I tahaqquq/test_a116.py
"""
import hashlib
import pathlib
import subprocess
import sys

JADHR = pathlib.Path(__file__).resolve().parent.parent
BIN = JADHR / ".lake" / "build" / "bin" / "a116-jadwal"
J = JADHR / "jadawil" / "a116"
AWDA = {"table": [], "counts": ["counts"], "order": ["bridge-order"], "numbers": ["numbers"], "pairs": ["pairs"], "utf8": ["utf8"],
        "hamza": ["hamza"], "licensable": ["licensable"], "degrees": ["degrees"], "wazn": ["wazn"], "wazn-body": ["wazn-body"],
        "neutral": ["neutral"], "degrees-pause": ["degrees-pause"], "ledger": ["ledger"], "need": ["need"], "nizam": ["nizam"],
        "mantuq": ["mantuq"], "baqi": ["baqi"], "silsila": ["silsila"], "furu": ["furu"], "amr": ["amr"], "roles": ["roles"],
        "tasrif": ["tasrif"], "rubai": ["rubai"], "maqayis": ["maqayis"], "qufl": ["qufl"], "tawafiq": ["tawafiq"],
        "masfufa": ["masfufa"], "amil": ["amil"], "huruf": ["huruf"], "marja": ["marja"], "marja-huruf": ["marja-huruf"],
        "marja-azwaj": ["marja-azwaj"], "mizan": ["mizan"]}
MAIN_SHA = "d27f63a2be3fdfef833d34cbf5f9f8161594f05373b5ad1d0f7890f57a6249c9"
najah, fashal = 0, []


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def main():
    if not BIN.exists():
        print(f"FAIL الأداة غير مبنيّة: {BIN} (lake build a116-jadwal)")
        sys.exit(1)
    tahaqqaq(sorted(p.stem for p in J.glob("*.csv")) == sorted(AWDA), "١ قائمةُ الجداول في jadawil/a116 غيرُ الأربعة والثلاثين")
    for ism, args in AWDA.items():
        r = subprocess.run([str(BIN), *args], capture_output=True, timeout=1800)
        tahaqqaq(r.returncode == 0 and r.stdout == (J / f"{ism}.csv").read_bytes(), f"١ {ism}.csv لا يطابق a116-jadwal {' '.join(args)}")
    for wad, milaf in (("masfufa-lean", "TawafiqMasfufaData.lean"), ("mizan-lean", "MizanData.lean")):
        r = subprocess.run([str(BIN), wad], capture_output=True, timeout=1800)
        tahaqqaq(r.returncode == 0 and r.stdout == (JADHR / "A116" / milaf).read_bytes(), f"٢ {milaf} لا يطابق a116-jadwal {wad}")
    lake = (JADHR / "lakefile.toml").read_text(encoding="utf-8")
    tahaqqaq('name = "A116"' in lake and 'root = "Qari.A116Jadwal"' in lake, "٣ المكتبةُ أو الأداةُ ليست في lakefile.toml")
    tahaqqaq(hashlib.sha256((JADHR / "Qari" / "A116Jadwal.lean").read_bytes()).hexdigest() == MAIN_SHA,
             "٣ Qari/A116Jadwal.lean ليس formal/a116/Main.lean بنصّه")
    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        sys.exit(1)
    print(f"test_a116: {najah} فحصًا نجح (34 جدولًا وملفّا بيانات = مُخرَجُ Lean المبنيّ في Mashru)")


if __name__ == "__main__":
    main()
