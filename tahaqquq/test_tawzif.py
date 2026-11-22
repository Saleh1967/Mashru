"""خريطةُ التوظيف وسقّاطتُها (البوّابة ٥خ٤؛ scripts/bina_tawzif.py؛ أمرُ المالك 2026-11-21، 13:57: «لا اريد ان تبقي اي مختوم او مودع او جدول
او lean خارج التوظيف مطلقا»).

يفحص:
١. على مستودعٍ مصنوعٍ صغير، بتوقّعاتٍ مكتوبةٍ باليد لا محسوبةٍ بالمولِّد: lakefile فيه مكتبةٌ «M» وتنفيذيٌّ جذرُه M.A؛ وM.A يستورد M.B، وM.B
   يستورد M.D، وM.C لا يستورده أحد ← غيرُ الموظَّف [M.C] وحده (فالبلوغُ متعدٍّ لا جذرٌ وحده). ومودَعان: x.tsv مذكورٌ في M.B وy.tsv مذكورٌ في
   mudaat/jalb.py وحده (في UKHRA) ← y غيرُ مستعمَل (ذكرُ الجالب ليس استعمالًا) ويُجلب، وx مستعمَلٌ ولا يُجلب.
٢. tahaqquq/tawzif.json مخرجُ المولِّد على المستودع بايتًا (`--check`).
٣. السقّاطة: كلُّ وحدةٍ غيرِ موظَّفةٍ الآن في قائمة خطّ الأساس tahaqquq/tawzif_asas.json، وكلُّ مودَعٍ غيرِ مستعمَلٍ أو لا يُجلب كذلك. فوحدةٌ جديدةٌ
   لا يبلغها تنفيذيٌّ تُفشل البوّابة باسمها، ولا تُستبدل بوحدةٍ خرجت من القائمة (المقارنةُ بالأسماء لا بالعدد). وما وُظِّف من القائمة يُطبع
   عددُه ليُحذف منها (تضييقُها لا يحتاج إذنًا، وتوسيعُها يحتاج).
الطفرات: P1652_tawzif_bila_taaddi (البلوغُ الجذرُ وحده) وP1653_jalb_istimal (ذكرُ الجالب استعمال) لـ ١، وP1654_saqqata_bil_adad (السقّاطة بالعدد) لـ ٣.
التشغيل: python3 -I tahaqquq/test_tawzif.py
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import bina_tawzif  # noqa: E402

fashal, najah = [], 0


def tahaqqaq(shart, wasf):
    global najah
    if shart:
        najah += 1
    else:
        fashal.append(wasf)


def ikhtibar_masnu():
    with tempfile.TemporaryDirectory() as d:
        def ktb(p, t):
            os.makedirs(os.path.dirname(os.path.join(d, p)) or d, exist_ok=True)
            open(os.path.join(d, p), "w", encoding="utf-8").write(t)
        ktb("lakefile.toml", 'name = "t"\n[[lean_lib]]\nname = "M"\nglobs = ["M.+"]\n[[lean_exe]]\nname = "e"\nroot = "M.A"\n')
        ktb("M/A.lean", "import M.B\ndef a := 1\n")
        ktb("M/B.lean", "import M.D\n-- يقرأ x.tsv\ndef b := 2\n")
        ktb("M/C.lean", "def c := 3\n")
        ktb("M/D.lean", "def d := 4\n")
        ktb("mudaat/sijill.json", json.dumps({"sijill": [
            {"ism": "س", "naw": "وضع", "sha256": "0" * 64, "milaf": "x.tsv", "hala": "مختوم", "idhn": "ا"},
            {"ism": "ص", "naw": "وضع", "sha256": "1" * 64, "milaf": "y.tsv", "hala": "مختوم", "idhn": "ا"}]}, ensure_ascii=False))
        ktb("mudaat/jalb.py", 'UKHRA = {\n    "y.tsv": "https://example.invalid/y.tsv",\n}\n')
        w = bina_tawzif.wallid(d)
    tahaqqaq(w["ghayr_muwazzafa"] == ["M.C"], f"١ غيرُ الموظَّف {w['ghayr_muwazzafa']} لا [M.C]")
    tahaqqaq(w["lean"]["M.D"] == ["e"], f"١ M.D يبلغه e بالتعدّي: {w['lean']['M.D']}")
    tahaqqaq(w["mudaat_ghayr_mustamala"] == ["y.tsv"], f"١ غيرُ المستعمَل {w['mudaat_ghayr_mustamala']} لا [y.tsv]")
    tahaqqaq(w["mudaat"]["x.tsv"]["mustamil"] == ["M/B.lean"], f"١ مستعمِلُ x {w['mudaat']['x.tsv']['mustamil']}")
    tahaqqaq(w["mudaat_la_tujlab"] == ["x.tsv"] and w["mudaat"]["y.tsv"]["yujlab"], f"١ الجلب {w['mudaat_la_tujlab']}")
    tahaqqaq(w["khulasa"]["wahdat"] == 4 and w["khulasa"]["muwazzafa"] == 3, f"١ الخلاصة {w['khulasa']}")


def saqqata(hali, asas):
    """ما في hali وليس في asas، بالاسم."""
    return sorted(set(hali) - set(asas))


def ikhtibar_saqqata_masnu():
    tahaqqaq(saqqata(["M.C", "M.E"], ["M.C", "M.F"]) == ["M.E"], "٣ السقّاطةُ بالاسم: M.E جديدةٌ وإن ثبت العدد")
    tahaqqaq(saqqata(["M.C"], ["M.C", "M.F"]) == [], "٣ التضييقُ لا يُفشل")


def main():
    ikhtibar_masnu()
    ikhtibar_saqqata_masnu()
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "bina_tawzif.py"), "--check"],
                       capture_output=True, text=True)
    tahaqqaq(p.returncode == 0, "٢ tawzif.json لا يطابق المولَّد: " + p.stdout.strip())
    hali = json.load(open(os.path.join(ROOT, "tahaqquq", "tawzif.json"), encoding="utf-8"))
    asas = json.load(open(os.path.join(ROOT, "tahaqquq", "tawzif_asas.json"), encoding="utf-8"))
    judud = {}
    for k in ("ghayr_muwazzafa", "mudaat_ghayr_mustamala", "mudaat_la_tujlab"):
        j = saqqata(hali[k], asas[k])
        tahaqqaq(not j, f"٣ {k}: جديدٌ خارج التوظيف لا في خطّ الأساس: {'، '.join(j[:12])}")
        judud[k] = len(set(asas[k]) - set(hali[k]))
    if fashal:
        print("\n".join("FAIL " + x for x in fashal))
        sys.exit(1)
    k = hali["khulasa"]
    print(f"التوظيف: {najah} فحصًا نجح — الوحدات {k['wahdat']} موظَّفٌ منها {k['muwazzafa']} وغيرُ موظَّف {k['ghayr_muwazzafa']}؛ "
          f"المودَعات {k['mudaat']} غيرُ مستعمَل {k['mudaat_ghayr_mustamala']} ولا يُجلب {k['mudaat_la_tujlab']}؛ "
          f"وُظِّف من خطّ الأساس {judud['ghayr_muwazzafa']} وحدةً و{judud['mudaat_ghayr_mustamala']} مودَعًا")


if __name__ == "__main__":
    main()
