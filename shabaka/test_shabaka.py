"""اختبارات شبكة المخصّص. التوقّعات مكتوبة من قراءة النصّ المختوم نفسه (الأسطر 2175–2196 من
mukhassas.txt، فصل «العين وما فيها»)، لا من مخرج الكود. وعدد الكتب يُعدّ بتعبير مستقلّ عن parse().

التشغيل: python3 -I test_shabaka.py <مسار mukhassas.txt>
"""
import os
import re
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mukhassas_shabaka as S  # noqa: E402

PATH = sys.argv[1]
text, nodes, pairs, poems, rejected = S.extract(PATH)
by_id = {n["id"]: n for n in nodes}


def path_of(i):
    out = []
    while i is not None:
        out.append(by_id[i]["title"])
        i = by_id[i]["parent"]
    return list(reversed(out))


def find_pair(jid, lafz, qail):
    return [p for p in pairs if p["jins"] == jid and p["lafz"] == lafz and p["qail"] == qail]


ayn = [n for n in nodes if n["title"] == "العين وما فيها"]
CASES = []


def case(name):
    def deco(f):
        CASES.append((name, f))
        return f
    return deco


@case("الفصل موجود مرّة واحدة وتحت كتاب خلق الإنسان مباشرة")
def _():
    assert len(ayn) == 1
    assert path_of(ayn[0]["id"]) == ["كتاب خلق الإنسان", "العين وما فيها"]


@case("ابن دريد: الهانة والهنانة - شحمة في باطن العين")
def _():
    for lf in ("الهانة", "الهنانة"):
        ps = find_pair(ayn[0]["id"], lf, "ابن دريد")
        assert ps and ps[0]["sharh"].startswith("شحمة في باطن العين"), lf


@case("أبو زيد: مخ العين - شحمها (قائل بلا نقطتين)")
def _():
    ps = find_pair(ayn[0]["id"], "مخ العين", "أبو زيد")
    assert ps and ps[0]["sharh"] == "شحمها"


@case("ثابت: في العين المقلة - … ← اللفظ «المقلة» لا «العين المقلة»")
def _():
    assert find_pair(ayn[0]["id"], "المقلة", "ثابت")
    assert not find_pair(ayn[0]["id"], "العين المقلة", "ثابت")


@case("أبو عبيد: ذباب العين - إنسانها")
def _():
    ps = find_pair(ayn[0]["id"], "ذباب العين", "أبو عبيد")
    assert ps and ps[0]["sharh"] == "إنسانها"


@case("بيت ذي الرمّة شاهد في الفصل")
def _():
    assert any(p["jins"] == ayn[0]["id"] and "وإنسان عيني يحسر الماء" in p["bayt"] for p in poems)


@case("عدد الكتب يساوي عدّها المستقلّ في النصّ الخام")
def _():
    raw = len(re.findall(r"^### \| \(?كتاب", text, re.M))
    assert raw == sum(n["naw"] == "كتاب" for n in nodes), raw


@case("كلّ جنس غير الكتب ورؤوس المجلّدات له أب، والأب يسبقه")
def _():
    for n in nodes:
        if n["naw"] in ("كتاب", "رأس"):
            assert n["parent"] is None
        else:
            assert n["parent"] is not None and n["parent"] < n["id"], n


@case("الختم: تغيير محرف واحد في المودَع يُرفض باسمه")
def _():
    raw = open(PATH, "rb").read()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(raw[:-1] + (b"X" if raw[-1:] != b"X" else b"Y"))
    try:
        S.sealed_text(f.name)
        raise AssertionError("قُبل مودَع مغيَّر")
    except ValueError:
        pass
    finally:
        os.unlink(f.name)


fails = 0
for name, f in CASES:
    try:
        f()
        print("✓", name)
    except AssertionError as e:
        fails += 1
        print("✗", name, e)
print(f"{len(CASES) - fails}/{len(CASES)}")
sys.exit(1 if fails else 0)
