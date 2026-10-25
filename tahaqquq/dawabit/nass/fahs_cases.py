# -*- coding: utf-8 -*-
"""Checker for cases.json (spec: wasf.md). Run: python3 -I fahs_cases.py [cases.json]
Exit 0 = all checks pass; exit 1 = at least one failure (each printed)."""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "cases.json")
TAALIF = os.path.join(HERE, "taalif.md")

SOURCES = {
    "قطر": ("/home/claude/mudaa_dir/qatr.txt",
            "2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d",
            set(range(75, 81)) | {219, 220, 267, 268} | set(range(337, 346))),
    "ألفية": ("/home/claude/mudaa_dir/alfiyya.txt",
              "13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0",
              set(range(75, 80))),
}
PREFIXES = ("### | ", "~~", "# ")

FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
MIN_FIA = {"موجب": 12, "حد": 10, "خارج": 5, "عموم": 6}
HUKM = {"مقبول", "خطأ", "لا_حكم"}
ROLES = {"فعل", "فاعل", "مفعول_به", "حرف_جر", "مجرور", "مضاف_إليه"}
SHAPES = [
    ["فعل", "فاعل"],
    ["فعل", "فاعل", "مضاف_إليه"],
    ["فعل", "فاعل", "مفعول_به"],
    ["فعل", "فاعل", "مفعول_به", "مضاف_إليه"],
    ["حرف_جر", "مجرور"],
    ["حرف_جر", "مجرور", "مضاف_إليه"],
]
NOUN_ROLES = {"فاعل", "مفعول_به", "مجرور", "مضاف_إليه"}
NAMES = {
    "أب": {"أبو", "أبا", "أبي", "أب"},
    "أخ": {"أخو", "أخا", "أخي", "أخ"},
    "حم": {"حمو", "حما", "حمي", "حم"},
    "هن": {"هنو", "هنا", "هني", "هن"},
    "فم": {"فو", "فا", "في", "فم", "فمو", "فما", "فمي"},
    "ذو": {"ذو", "ذا", "ذي"},
}
KEYS = {"id", "fia", "nass", "mithal_harfi", "itar", "hukm", "zawj", "sanad", "taliq"}

FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SHADDA, SUKUN = "ّ", "ْ"
MARKS = {FATHA, DAMMA, KASRA, FATHATAN, DAMMATAN, KASRATAN, SHADDA, SUKUN}
VOWELS = {FATHA, DAMMA, KASRA}
TANWIN = {FATHATAN, DAMMATAN, KASRATAN}
LETTERS = {chr(c) for c in list(range(0x0621, 0x063B)) + list(range(0x0641, 0x064B))}
ALIF, ALIF_MAQSURA, WAW, YA, LAM, TA_MARBUTA = "ا", "ى", "و", "ي", "ل", "ة"
LONG = {ALIF, ALIF_MAQSURA, WAW, YA}

errors = []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def strip_marks(s):
    return "".join(ch for ch in s if ch not in MARKS)


def load_lines():
    out = {}
    for masdar, (path, sha, _scope) in SOURCES.items():
        data = open(path, "rb").read()
        got = hashlib.sha256(data).hexdigest()
        if got != sha:
            err("source", f"{masdar}: sha256 {got} != {sha}")
        out[masdar] = data.decode("utf-8").split("\n")
    return out


def stripped_line(lines, masdar, satr):
    raw = lines[masdar][satr - 1].rstrip("\r")
    for p in PREFIXES:
        if raw.startswith(p):
            return raw[len(p):]
    return None


def clusters(word):
    """Split a word into (letter, marks) pairs; returns None if a mark has no letter."""
    out = []
    for ch in word:
        if ch in LETTERS:
            out.append([ch, []])
        elif ch in MARKS:
            if not out:
                return None
            out[-1][1].append(ch)
        else:
            return None
    return out


def check_word(where, word):
    cl = clusters(word)
    if cl is None or not cl:
        err(where, f"word {word!r}: bad characters or starts with a mark")
        return
    n = len(cl)
    is_al = n >= 3 and cl[0][0] == ALIF and not cl[0][1] and cl[1][0] == LAM
    for i, (ch, mk) in enumerate(cl):
        w = f"{where} word {word!r} letter {i}"
        if len(mk) != len(set(mk)):
            err(w, "repeated mark")
        vt = [m for m in mk if m in VOWELS | TANWIN]
        if len(vt) > 1:
            err(w, "more than one vowel/tanwin")
        if SHADDA in mk and not vt:
            err(w, "shadda without its vowel")
        if SHADDA in mk and SUKUN in mk:
            err(w, "shadda with sukun")
        if SUKUN in mk and vt:
            err(w, "sukun with vowel")
        if any(m in TANWIN for m in mk):
            last_ok = (i == n - 1) or (i == n - 2 and cl[-1][0] == ALIF and not cl[-1][1])
            if not last_ok:
                err(w, "tanwin not on the last letter")
            if FATHATAN in mk and ch != TA_MARBUTA:
                if not (i == n - 2 and cl[-1][0] == ALIF):
                    err(w, "fathatan not followed by alif")
        if ch == TA_MARBUTA and i != n - 1:
            err(w, "ta marbuta not final")
        if ch == ALIF:
            if mk:
                err(w, "alif carries a mark")
            continue
        if ch == ALIF_MAQSURA:
            if mk or i != n - 1:
                err(w, "alif maqsura with mark or not final")
            continue
        if not mk:
            if ch == WAW and i > 0 and DAMMA in cl[i - 1][1]:
                continue  # madd waw
            if ch == YA and i > 0 and KASRA in cl[i - 1][1]:
                continue  # madd ya
            if ch == LAM and is_al and i == 1 and n > 2 and SHADDA in cl[2][1]:
                continue  # lam before a shamsi (doubled) letter
            err(w, "letter without vowel/sukun")
        if is_al and i == 1 and ch == LAM and n > 2 and SHADDA not in cl[2][1] and SUKUN not in mk:
            err(w, "lam of al before a qamari letter lacks sukun")
        if is_al and i == 1 and ch == LAM and n > 2 and SHADDA in cl[2][1] and mk:
            err(w, "lam of al before a shamsi letter carries a mark")
    # last letter: a mark, or a long-vowel letter
    ch, mk = cl[-1]
    if not mk and ch not in LONG:
        err(where, f"word {word!r}: last letter has no mark and is not a long-vowel letter")


def check_nass(where, nass):
    if not isinstance(nass, str) or not nass:
        err(where, "nass empty or not a string")
        return []
    if nass != nass.strip() or "  " in nass:
        err(where, "leading/trailing or double spaces")
    for ch in nass:
        if ch != " " and ch not in LETTERS and ch not in MARKS:
            err(where, f"forbidden character U+{ord(ch):04X}")
    words = nass.split(" ")
    for w in words:
        check_word(where, w)
    return words


def base(word):
    s = word
    while s and s[-1] in MARKS:
        s = s[:-1]
    while s and s[-1] in LONG:
        s = s[:-1]
    while s and s[-1] in MARKS:
        s = s[:-1]
    return s


def names_in(words, itar):
    found = set()
    for w, r in zip(words, itar):
        if r not in NOUN_ROLES:
            continue
        s = strip_marks(w)
        if s.startswith("ال"):
            s = s[2:]
        for name, forms in NAMES.items():
            if s in forms:
                found.add(name)
    return found


def main():
    lines = load_lines()
    try:
        cases = json.load(open(CASES, encoding="utf-8"))
    except Exception as e:  # noqa
        print(f"FAIL: invalid JSON: {e}")
        return 1
    if not isinstance(cases, list):
        print("FAIL: top level is not a list")
        return 1
    ids, texts = {}, set()
    fia_count = {f: 0 for f in FIAT}
    name_count = {n: 0 for n in NAMES}
    shape_count = {i: 0 for i in range(len(SHAPES))}
    verbatim = 0
    for k, c in enumerate(cases):
        where = f"case[{k}]"
        if not isinstance(c, dict):
            err(where, "not an object")
            continue
        if set(c.keys()) != KEYS:
            err(where, f"keys {sorted(c.keys())} != {sorted(KEYS)}")
            continue
        cid = c["id"]
        where = f"{cid}"
        if not (isinstance(cid, str) and len(cid) == 3 and cid[0] == "N" and cid[1:].isdigit()):
            err(where, "id not N + two digits")
        if cid in ids:
            err(where, "duplicate id")
        ids[cid] = c
        fia = c["fia"]
        if fia not in FIAT:
            err(where, f"fia {fia!r} not allowed")
        else:
            fia_count[fia] += 1
        words = check_nass(where, c["nass"])
        if c["nass"] in texts:
            err(where, "duplicate sentence")
        texts.add(c["nass"])
        # itar
        itar = c["itar"]
        frames = []
        if isinstance(itar, list) and itar and all(isinstance(x, list) for x in itar):
            if fia != "غموض" or len(itar) != 2:
                err(where, "list of frames allowed only in غموض with exactly two frames")
            frames = itar
        elif isinstance(itar, list):
            frames = [itar]
        else:
            err(where, "itar not a list")
        for fr in frames:
            if any(r not in ROLES for r in fr):
                err(where, f"itar has a role outside the allowed values: {fr}")
            if fr not in SHAPES:
                err(where, f"itar {fr} is not one of the six shapes")
            elif len(fr) != len(words):
                err(where, f"itar length {len(fr)} != word count {len(words)}")
        if frames and frames[0] in SHAPES:
            shape_count[SHAPES.index(frames[0])] += 1
            for nm in names_in(words, frames[0]):
                name_count[nm] += 1
        # hukm
        hukm = c["hukm"]
        if isinstance(hukm, list):
            if fia != "غموض" or len(hukm) != 2 or len(set(hukm)) != 2 or any(h not in HUKM for h in hukm):
                err(where, f"hukm list {hukm} not allowed")
        elif hukm not in HUKM:
            err(where, f"hukm {hukm!r} not allowed")
        if fia == "موجب" and hukm != "مقبول":
            err(where, "موجب must be مقبول")
        if fia == "حد" and hukm != "خطأ":
            err(where, "حد must be خطأ")
        if fia == "خارج" and hukm != "لا_حكم":
            err(where, "خارج must be لا_حكم")
        if fia == "عموم" and hukm not in ("مقبول", "خطأ"):
            err(where, "عموم must be مقبول or خطأ")
        if fia == "غموض" and not (isinstance(hukm, list) or len(frames) == 2):
            err(where, "غموض needs two judgments or two frames")
        if fia != "غموض" and (isinstance(hukm, list) or len(frames) != 1):
            err(where, "list forms only in غموض")
        # sanad
        sanad = c["sanad"]
        if not isinstance(sanad, list):
            err(where, "sanad not a list")
            sanad = []
        if hukm == "لا_حكم" and sanad:
            err(where, "لا_حكم must have empty sanad")
        if hukm != "لا_حكم" and not sanad:
            err(where, "judgment without sanad")
        full_lines = []
        for j, s in enumerate(sanad):
            w = f"{where} sanad[{j}]"
            if not isinstance(s, dict) or set(s.keys()) != {"masdar", "satr", "nass"}:
                err(w, "bad sanad item keys")
                continue
            m, n, t = s["masdar"], s["satr"], s["nass"]
            if m not in SOURCES:
                err(w, f"masdar {m!r} not allowed")
                continue
            if not isinstance(n, int) or isinstance(n, bool) or n not in SOURCES[m][2]:
                err(w, f"satr {n!r} outside the scope of {m}")
                continue
            sl = stripped_line(lines, m, n)
            if sl is None:
                err(w, "line has no recognised prefix")
                continue
            if not isinstance(t, str) or not t or "\n" in t or "\r" in t:
                err(w, "nass empty or spans lines")
                continue
            if t.encode("utf-8") not in sl.encode("utf-8"):
                err(w, f"nass {t!r} is not a byte substring of {m} line {n}")
            full_lines.append(sl)
        # mithal_harfi
        mh = c["mithal_harfi"]
        if not isinstance(mh, bool):
            err(where, "mithal_harfi not a boolean")
        else:
            plain = strip_marks(c["nass"])
            inside = any(plain in fl for fl in full_lines)
            if mh and not inside:
                err(where, "mithal_harfi=true but sentence not in its sanad lines")
            if not mh and inside:
                err(where, "mithal_harfi=false but sentence appears in a sanad line")
            if mh:
                verbatim += 1
        # taliq
        tq = c["taliq"]
        if not isinstance(tq, str) or not tq.strip() or "\n" in tq:
            err(where, "taliq empty or more than one line")
    # pairs
    pairs = set()
    for cid, c in ids.items():
        z = c.get("zawj")
        if z is None:
            continue
        where = f"{cid} zawj"
        if z == cid or z not in ids:
            err(where, f"zawj {z!r} missing or self")
            continue
        o = ids[z]
        if o.get("zawj") != cid:
            err(where, "zawj not mutual")
            continue
        a, b = c["nass"].split(" "), o["nass"].split(" ")
        if len(a) != len(b):
            err(where, "different word counts")
            continue
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        if len(diff) != 1:
            err(where, f"differs in {len(diff)} words, not one")
            continue
        i = diff[0]
        if base(a[i]) != base(b[i]):
            err(where, f"words {a[i]!r}/{b[i]!r} differ beyond the case ending")
        if c["hukm"] == o["hukm"]:
            err(where, "same hukm")
        pairs.add(tuple(sorted((cid, z))))
    # counts
    total = len(cases)
    if not 40 <= total <= 50:
        err("count", f"total {total} not in 40..50")
    for f, mn in MIN_FIA.items():
        if fia_count[f] < mn:
            err("count", f"{f} {fia_count[f]} < {mn}")
    if fia_count["غموض"] < 2:
        ok = os.path.exists(TAALIF) and "غموض" in open(TAALIF, encoding="utf-8").read()
        if fia_count["غموض"] == 1 or not ok:
            err("count", "غموض < 2 and taalif.md does not record the search")
    for nm, cnt in name_count.items():
        if cnt < 3:
            err("count", f"name {nm} in {cnt} cases < 3")
    for i, cnt in shape_count.items():
        if cnt < 3:
            err("count", f"shape {i + 1} in {cnt} cases < 3")
    if len(pairs) < 6:
        err("count", f"pairs {len(pairs)} < 6")
    print(f"total={total} fia={fia_count} verbatim={verbatim} pairs={len(pairs)}")
    print(f"names={name_count}")
    print(f"shapes={ {i + 1: v for i, v in shape_count.items()} }")
    if errors:
        for e in errors:
            print("FAIL:", e)
        print(f"{len(errors)} failure(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
