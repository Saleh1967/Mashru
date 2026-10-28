"""بوّابة الإيداع: سجلّ المودَعات، والختم بإذن، وتوليد سجلّ الفاحص.

القواعد (الدستور م9، م12؛ Aql/Idaa.lean):
  * المودَع يُختم ببصمة sha256 لبايتاته كما رُفعت: لا تنظيف ولا تطبيع ولا حذف تصحيف
    (`Idaa.la_tanzif_bila_daya`: الحذف الذي يجمع صورتين لا يُفكّ).
  * لكلّ مودَع نوعٌ من أربعة: واقع-مختوم، وضع، معلومات-سابقة، مرجع-محجوب.
  * لا ختم بلا إذن المالك: `sajjil` بلا `--idhn` يُرفض ولا يمسّ السجلّ.
  * الاسم الواحد لا يُختم ببصمتين، والبصمة الواحدة لا تُسجَّل باسمين.
  * حالة المودَع: «مختوم» يدخل سجلّ الفاحص (sijill.tsv)؛ «مرشح» لا يدخله حتّى يُختم.
  * جدولُ الربط (P2-أ؛ «جدول الربط — القطعة الأولى»، 2026-10-29): مودَعٌ «وضع» يحمل في السجلّ حقلَ `shawahid` — أسطرَه
    بعينها (المعنى، الشيء، الخاصّة، القيمة) — وبصمتُه بصمةُ هذه الأسطر مكتوبةً «حقولًا بـTAB، وسطرًا بـLF» فتُفحص من السجلّ
    نفسه بلا مودَع؛ ويولّد منها `wallid` أسطرَ `shahid` بعد أسطر `mudaa` كلّها. فلا يربط معنًى بواقعٍ إلّا مودَعٌ مختومٌ بإذن.
    الختم: `sajjil <ملفّ> --ism X --naw وضع --ribt --idhn …`.

التشغيل:
  python3 -I mudaat/idaa.py fahs [--sijill S]                 يتحقّق من السجلّ ويقارن sijill.tsv بالمولَّد
  python3 -I mudaat/idaa.py wallid [--sijill S]               يولّد sijill.tsv
  python3 -I mudaat/idaa.py sajjil <ملفّ> --ism X --naw Y --idhn "<إذن المالك>" [--sijill S]
  python3 -I mudaat/idaa.py tahaqqaq <مجلّد>                   يطابق بصمات ما حضر من المودَعات في مجلّد
"""
import datetime
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ANWA = {"واقع-مختوم", "وضع", "معلومات-سابقة", "مرجع-محجوب"}
AHWAL = {"مختوم", "مرشح"}


def basma(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def qira(p):
    return json.load(open(p, encoding="utf-8"))["sijill"]


def kitaba(p, s):
    json.dump({"sijill": s}, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def akhta(s):
    e = []
    asma, basamat = {}, {}
    for i, m in enumerate(s):
        if m.get("naw") not in ANWA:
            e.append(f"{i}: نوع مجهول (م12): {m.get('naw')}")
        if not re.fullmatch(r"[0-9a-f]{64}", m.get("sha256", "")):
            e.append(f"{i}: بصمة ليست sha256")
        if m.get("hala") not in AHWAL:
            e.append(f"{i}: حالة مجهولة")
        if m.get("hala") == "مختوم" and not m.get("idhn"):
            e.append(f"{i}: مختوم بلا إذن (م9)")
        if m["ism"] in asma and asma[m["ism"]] != m["sha256"]:
            e.append(f"{i}: الاسم {m['ism']} ببصمتين")
        if m["sha256"] in basamat and basamat[m["sha256"]] != m["ism"]:
            e.append(f"{i}: البصمة باسمين")
        if "shawahid" in m:
            r = m["shawahid"]
            if m.get("naw") != "وضع":
                e.append(f"{i}: جدولُ ربطٍ نوعُه غيرُ «وضع»")
            if not isinstance(r, list) or not r or any(not isinstance(x, list) or len(x) != 4 or
                                                       not all(isinstance(y, str) and y and "\t" not in y and "\n" not in y for y in x) for x in r):
                e.append(f"{i}: أسطرُ الربط لا تُقرأ (أربعةُ حقولٍ غيرُ فارغةٍ لكلّ سطر)")
            elif hashlib.sha256(baytRibt(r)).hexdigest() != m.get("sha256"):
                e.append(f"{i}: أسطرُ الربط لا تطابق بصمةَ المودَع")
        asma[m["ism"]] = m["sha256"]
        basamat[m["sha256"]] = m["ism"]
    return e


def baytRibt(rows):
    return "".join("\t".join(r) + "\n" for r in rows).encode("utf-8")


def qiraRibt(path):
    b = open(path, "rb").read()
    rows = [l.split("\t") for l in b.decode("utf-8").split("\n")[:-1]] if b.endswith(b"\n") else None
    if not rows or any(len(r) != 4 or not all(r) for r in rows) or baytRibt(rows) != b:
        return None
    return rows


def tsv(s):
    mk = [m for m in s if m["hala"] == "مختوم"]
    return "".join(f"mudaa\t{m['sha256']}\t{m['naw']}\t{m['ism']}\n" for m in mk) + \
        "".join("shahid\t" + "\t".join(r) + "\n" for m in mk for r in m.get("shawahid", []))


def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a and a.index(name) + 1 < len(a) else default


def main():
    sp = arg("--sijill", os.path.join(HERE, "sijill.json"))
    tp = os.path.join(os.path.dirname(sp), "sijill.tsv")
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    s = qira(sp)
    if cmd == "fahs":
        e = akhta(s)
        if not os.path.exists(tp) or open(tp, encoding="utf-8").read() != tsv(s):
            e.append("sijill.tsv لا يطابق المولَّد من sijill.json")
        print(f"مودَعات {len(s)}: مختوم {sum(m['hala'] == 'مختوم' for m in s)}، مرشح {sum(m['hala'] == 'مرشح' for m in s)}، أخطاء {len(e)}")
        for x in e:
            print("خطأ", x)
        sys.exit(1 if e else 0)
    if cmd == "wallid":
        e = akhta(s)
        if e:
            sys.exit("\n".join(e))
        open(tp, "w", encoding="utf-8").write(tsv(s))
        return
    if cmd == "sajjil":
        f, ism, naw, idhn = sys.argv[2], arg("--ism"), arg("--naw"), arg("--idhn")
        if not idhn:
            print("مرفوض: لا ختم بلا إذن المالك (الدستور م9)")
            sys.exit(3)
        if naw not in ANWA:
            print(f"مرفوض: نوع مجهول (الدستور م12): {naw}")
            sys.exit(3)
        b = basma(f)
        for m in s:
            if m["ism"] == ism and m["sha256"] != b:
                print(f"مرفوض: «{ism}» مختوم ببصمة أخرى؛ تغيّر المودَع")
                sys.exit(3)
            if m["sha256"] == b and m["ism"] != ism:
                print(f"مرفوض: البصمة مسجّلة باسم «{m['ism']}»")
                sys.exit(3)
            if m["sha256"] == b and m["ism"] == ism and m["hala"] == "مختوم":
                print("موجود مختومًا؛ لا تغيير")
                return
        s = [m for m in s if not (m["ism"] == ism and m["sha256"] == b)]
        qayd = {"ism": ism, "naw": naw, "sha256": b, "milaf": os.path.basename(f),
                "masdar": arg("--masdar", ""), "hala": "مختوم", "idhn": idhn,
                "tarikh": datetime.date.today().isoformat()}
        if "--ribt" in sys.argv:
            rows = qiraRibt(f)
            if naw != "وضع" or rows is None:
                print("مرفوض: جدولُ الربط «وضع»، وأسطرُه أربعةُ حقولٍ غيرُ فارغةٍ بـTAB وكلُّ سطرٍ ينتهي بـLF")
                sys.exit(3)
            qayd["shawahid"] = rows
        s.append(qayd)
        kitaba(sp, s)
        open(tp, "w", encoding="utf-8").write(tsv(s))
        print(f"خُتم «{ism}» {b}")
        return
    if cmd == "tahaqqaq":
        d = sys.argv[2]
        bad = 0
        for m in s:
            p = os.path.join(d, m["milaf"])
            if os.path.exists(p):
                ok = basma(p) == m["sha256"]
                bad += not ok
                print(("مطابق" if ok else "تغيّر") + f"\t{m['ism']}")
        sys.exit(1 if bad else 0)
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
