#!/usr/bin/env python3
# فاحص ملف الحالات قبل التجميد (ضابط «صكّ الجملة»).
# الاستعمال: python3 -I fahs_cases.py [cases.json] [--src DIR] [--wasf wasf.md]
# يخرج 0 إن مرّ كلّ شيء، و1 مع قائمة الأخطاء إن لم يمرّ.
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- المعاملات
args = sys.argv[1:]
cases_path = os.path.join(HERE, "cases.json")
src_dir = "/home/claude/mudaa_dir"
wasf_path = os.path.join(HERE, "wasf.md")
i = 0
pos = []
while i < len(args):
    if args[i] == "--src":
        src_dir = args[i + 1]
        i += 2
    elif args[i] == "--wasf":
        wasf_path = args[i + 1]
        i += 2
    else:
        pos.append(args[i])
        i += 1
if pos:
    cases_path = pos[0]

errors = []


def err(msg):
    errors.append(msg)


# ---------------------------------------------------------------- المواصفة
with open(wasf_path, encoding="utf-8") as f:
    wasf_lines = f.read().split("\n")

# جدول البصمات
HASHES = {}
for ln in wasf_lines:
    m = re.match(r"\|\s*`([a-z0-9]+\.txt)`\s*\|[^|]*\|\s*`([0-9a-f]{64})`\s*\|", ln)
    if m:
        HASHES[m.group(1)] = m.group(2)

# النطاق لكلّ نوع، مقروءًا من المواصفة
SCOPE = {}
cur = None
for ln in wasf_lines:
    m = re.match(r"- \*\*نطاقُ `(\S+)`:\*\*\s*$", ln)
    if m:
        cur = m.group(1)
        SCOPE[cur] = {}
        continue
    if cur is not None:
        if ln.startswith("  - "):
            for fm in re.finditer(r"`([a-z0-9]+\.txt)`:\s*([0-9\s–\-،]+)", ln):
                fname, spec = fm.group(1), fm.group(2)
                rngs = SCOPE[cur].setdefault(fname, [])
                for part in spec.split("،"):
                    part = part.strip()
                    if not part:
                        continue
                    mm = re.fullmatch(r"(\d+)\s*[–\-]\s*(\d+)", part)
                    if mm:
                        rngs.append((int(mm.group(1)), int(mm.group(2))))
                    elif re.fullmatch(r"\d+", part):
                        rngs.append((int(part), int(part)))
                    else:
                        err(f"wasf: cannot parse range '{part}'")
        else:
            cur = None

# نسخة مكتوبة يدويًّا من النطاق للمقارنة بالمقروء (حمايةٌ من خطأ القراءة)
EXPECTED_SCOPE = {
    "قوة": {
        "sibawayhi.txt": [(1268, 1294), (1522, 1525), (9190, 9304), (9544, 9652), (9782, 9787), (10022, 10041)],
        "mughni.txt": [(2217, 2239), (5901, 5919), (6109, 6116), (6400, 6405), (6483, 6486), (9567, 9589), (9620, 9668)],
        "qatr.txt": [(108, 122), (194, 197)],
        "alfiyya.txt": [(250, 256), (296, 302), (905, 912)],
        "a2.txt": [(767, 767), (896, 896)],
    },
    "سبب": {
        "sibawayhi.txt": [(3659, 3692), (4196, 4202), (8791, 8913), (8914, 9049), (9592, 9594), (9824, 9865),
                          (10143, 10221), (11484, 11574), (18400, 18405)],
        "mughni.txt": [(643, 687), (709, 712), (2748, 2848), (3660, 3697), (4158, 4163), (4781, 4802),
                       (7555, 7608), (11032, 11040), (12964, 13006)],
        "qatr.txt": [(50, 51), (97, 97), (108, 109), (293, 298)],
        "alfiyya.txt": [(399, 401), (491, 491), (534, 534), (895, 895)],
        "a1.txt": [(269, 271)],
        "a2.txt": [(1040, 1040)],
    },
    "مرجع": {
        "qatr.txt": [(123, 133)],
        "alfiyya.txt": [(105, 105), (138, 140)],
        "sibawayhi.txt": [(4434, 4551), (5203, 5248)],
        "a2.txt": [(749, 749), (918, 918), (1419, 1419)],
    },
}
if SCOPE != EXPECTED_SCOPE:
    err(f"wasf: parsed scope differs from the hand copy: {SCOPE!r}")

EXPECTED_FILES = {"qatr.txt", "alfiyya.txt", "mughni.txt", "sibawayhi.txt", "a1.txt", "a2.txt"}
if set(HASHES) != EXPECTED_FILES:
    err(f"wasf: hash table files {sorted(HASHES)} != {sorted(EXPECTED_FILES)}")

# ---------------------------------------------------------------- المصادر
LINES = {}
for fname in sorted(EXPECTED_FILES):
    p = os.path.join(src_dir, fname)
    try:
        with open(p, "rb") as f:
            data = f.read()
    except OSError as e:
        err(f"source {fname}: cannot read ({e})")
        continue
    h = hashlib.sha256(data).hexdigest()
    if h != HASHES.get(fname):
        err(f"source {fname}: sha256 {h} != spec {HASHES.get(fname)}")
    LINES[fname] = data.decode("utf-8").split("\n")


def stripped(fname, satr):
    """السطر رقم satr (من 1) بعد حذف بادئته وحدها."""
    ls = LINES.get(fname)
    if ls is None or not (1 <= satr <= len(ls)):
        return None
    line = ls[satr - 1]
    for pre in ("### | ", "# ", "~~"):
        if line.startswith(pre):
            return line[len(pre):]
    return line


def in_scope(naw, fname, satr):
    for a, b in SCOPE.get(naw, {}).get(fname, []):
        if a <= satr <= b:
            return True
    return False


# ---------------------------------------------------------------- القيم المسموحة
LH = "لا_حكم"
SCHEMA = {
    "قوة": {
        "dakhil": {
            "adat": ["لا_شيء", "لم", "إن"],
            "qawl": ["لا_قول", "قال", "تقول_مستفهما"],
            "ma_baad_alqawl": ["لا_قول", "إن_مكسورة", "أن_مفتوحة", "مرفوع", "منصوب", "جملة_فعلية", "غير_معلن"],
            "lugha": ["عامة", "بنو_سليم", "غير_معلن"],
        },
        "kharij": {
            "awwal": ["إثبات", "نفي", "تعليق", "إنشاء", LH],
            "thani": ["إثبات", "نفي", "تعليق", "حكاية", "ظن", "لا_ثاني", LH],
        },
    },
    "سبب": {
        "dakhil": {
            "dall": ["مصدر_منصوب", "لام_جارة", "لام_ناصبة", "كي", "حتى_منصوب", "حتى_مرفوع", "فاء_منصوب",
                     "فاء_مرفوع", "أن_بلا_لام", "لما", "بعد", "قبل", "غير_ذلك"],
            "shurut": ["مستوفاة", "فقد_الفاعل", "فقد_الوقت", "غير_معلن", "لا_ينطبق"],
            "adaa": ["الأول_سبب_الثاني", "الأول_ليس_سببا", "غير_معلن", "لا_ينطبق"],
        },
        "kharij": {"sabab": ["علة", "سببية", "غير_مذكور", LH]},
    },
    "مرجع": {
        "dakhil": {
            "lafz": ["أنا", "أنت", "هو", "هذا", "ذاك"],
            "siyaq": ["متكلم_معين", "مخاطب_معين", "مفسر_واحد", "مفسران", "مشار_اليه_واحد", "مشار_اليهما",
                      "لا_شيء"],
        },
        "kharij": {"marji": ["معين", "محتمل", LH]},
    },
}
FIAT = ["موجب", "حد", "خارج", "عموم", "غموض"]
MIN_FIA = {"موجب": 10, "حد": 6, "خارج": 4, "عموم": 3, "غموض": 3}
CASE_KEYS = {"id", "naw", "fia", "mithal", "mithal_harfi", "dakhil", "kharij", "sanad", "taliq"}
DIACRITICS = re.compile("[ً-ٰٟ]")

# ---------------------------------------------------------------- الحالات
try:
    with open(cases_path, "rb") as f:
        raw = f.read()
    cases = json.loads(raw.decode("utf-8"))
except Exception as e:  # noqa: BLE001
    print(f"FAIL: cases file is not valid UTF-8 JSON: {e}")
    sys.exit(1)

if not isinstance(cases, list):
    print("FAIL: cases.json must be a JSON list")
    sys.exit(1)

seen_ids = set()
seen_dakhil = {}
count_naw = {n: 0 for n in SCHEMA}
count_fia = {c: 0 for c in FIAT}
harfi = 0

for idx, c in enumerate(cases):
    tag = f"case#{idx + 1}"
    if not isinstance(c, dict):
        err(f"{tag}: not an object")
        continue
    cid = c.get("id")
    tag = f"{cid or tag}"
    if set(c.keys()) != CASE_KEYS:
        err(f"{tag}: keys {sorted(c.keys())} != {sorted(CASE_KEYS)}")
    # id
    if not isinstance(cid, str) or not re.fullmatch(r"S\d\d", cid):
        err(f"{tag}: bad id {cid!r}")
    elif cid in seen_ids:
        err(f"{tag}: duplicate id")
    else:
        seen_ids.add(cid)
    if isinstance(cid, str) and cid != f"S{idx + 1:02d}":
        err(f"{tag}: ids must run S01, S02, … in order (expected S{idx + 1:02d})")
    # naw / fia
    naw = c.get("naw")
    if naw not in SCHEMA:
        err(f"{tag}: bad naw {naw!r}")
        continue
    count_naw[naw] += 1
    fia = c.get("fia")
    if fia not in FIAT:
        err(f"{tag}: bad fia {fia!r}")
    else:
        count_fia[fia] += 1
    sch = SCHEMA[naw]
    # mithal
    mithal = c.get("mithal")
    if not isinstance(mithal, str) or not mithal.strip() or "\n" in mithal:
        err(f"{tag}: mithal must be a non-empty one-line string")
        mithal = ""
    elif DIACRITICS.search(mithal):
        err(f"{tag}: mithal carries diacritics")
    mh = c.get("mithal_harfi")
    if not isinstance(mh, bool):
        err(f"{tag}: mithal_harfi must be boolean")
    # taliq
    taliq = c.get("taliq")
    if not isinstance(taliq, str) or not taliq.strip() or "\n" in taliq or "\r" in taliq:
        err(f"{tag}: taliq must be a single non-empty line")
    # dakhil
    d = c.get("dakhil")
    if not isinstance(d, dict) or set(d.keys()) != set(sch["dakhil"]):
        err(f"{tag}: dakhil keys must be {sorted(sch['dakhil'])}")
        d = {}
    for k, allowed in sch["dakhil"].items():
        if k in d and d[k] not in allowed:
            err(f"{tag}: dakhil.{k}={d[k]!r} not allowed")
    if naw == "قوة" and d:
        if (d.get("qawl") == "لا_قول") != (d.get("ma_baad_alqawl") == "لا_قول"):
            err(f"{tag}: qawl=لا_قول iff ma_baad_alqawl=لا_قول")
    if naw == "سبب" and d:
        dall = d.get("dall")
        if (dall == "مصدر_منصوب") != (d.get("shurut") != "لا_ينطبق"):
            err(f"{tag}: shurut must be لا_ينطبق exactly when dall is not مصدر_منصوب")
        hf = dall in ("حتى_منصوب", "حتى_مرفوع", "فاء_منصوب", "فاء_مرفوع")
        if hf != (d.get("adaa") != "لا_ينطبق"):
            err(f"{tag}: adaa must be لا_ينطبق exactly when dall is not حتى/الفاء")
    dkey = json.dumps(d, ensure_ascii=False, sort_keys=True)
    if d:
        if (naw, dkey) in seen_dakhil:
            err(f"{tag}: same dakhil as {seen_dakhil[(naw, dkey)]} within type {naw}")
        else:
            seen_dakhil[(naw, dkey)] = tag
    # kharij
    k = c.get("kharij")
    if not isinstance(k, dict) or set(k.keys()) != set(sch["kharij"]):
        err(f"{tag}: kharij keys must be {sorted(sch['kharij'])}")
        k = {}
    lists = 0
    all_lh = bool(k)
    for fk, allowed in sch["kharij"].items():
        if fk not in k:
            continue
        v = k[fk]
        if isinstance(v, list):
            lists += 1
            all_lh = False
            if fia != "غموض":
                err(f"{tag}: kharij.{fk} is a list but fia is not غموض")
            if len(v) != 2 or len(set(v)) != 2 or any((x not in allowed) or x == LH for x in v):
                err(f"{tag}: kharij.{fk} list must be two distinct allowed values other than لا_حكم")
        else:
            if v not in allowed:
                err(f"{tag}: kharij.{fk}={v!r} not allowed")
            if v != LH:
                all_lh = False
    if fia == "غموض" and lists != 1:
        err(f"{tag}: غموض needs exactly one list-valued kharij field (has {lists})")
    if fia == "خارج" and not all_lh:
        err(f"{tag}: خارج must expect لا_حكم in every field")
    # sanad
    s = c.get("sanad")
    if not isinstance(s, list):
        err(f"{tag}: sanad must be a list")
        s = []
    if all_lh and s:
        err(f"{tag}: kharij is entirely لا_حكم so sanad must be empty")
    if not all_lh and not s:
        err(f"{tag}: kharij gives a verdict so sanad must not be empty")
    line_texts = []
    for j, piece in enumerate(s):
        ptag = f"{tag}.sanad[{j}]"
        if not isinstance(piece, dict) or set(piece.keys()) != {"milaf", "satr", "nass"}:
            err(f"{ptag}: keys must be milaf, satr, nass")
            continue
        fname, satr, nass = piece["milaf"], piece["satr"], piece["nass"]
        if fname not in EXPECTED_FILES:
            err(f"{ptag}: milaf {fname!r} not in the spec table")
            continue
        if not isinstance(satr, int) or isinstance(satr, bool) or satr < 1:
            err(f"{ptag}: satr must be a positive integer")
            continue
        if not isinstance(nass, str) or not nass or "\n" in nass:
            err(f"{ptag}: nass must be a non-empty one-line string")
            continue
        if not in_scope(naw, fname, satr):
            err(f"{ptag}: {fname}:{satr} is outside the scope of {naw}")
        text = stripped(fname, satr)
        if text is None:
            err(f"{ptag}: {fname} has no line {satr}")
            continue
        line_texts.append(text)
        if nass.encode("utf-8") not in text.encode("utf-8"):
            err(f"{ptag}: nass is not a byte substring of {fname}:{satr}")
    if mh is True:
        harfi += 1
        if mithal and not any(mithal in t for t in line_texts):
            err(f"{tag}: mithal_harfi is true but the mithal is not in any sanad line")

# ---------------------------------------------------------------- الأعداد
n = len(cases)
if not (36 <= n <= 48):
    err(f"total {n} not in 36..48")
for naw, cnt in count_naw.items():
    if cnt < 10:
        err(f"type {naw}: {cnt} cases < 10")
for fia, mn in MIN_FIA.items():
    if count_fia[fia] < mn:
        err(f"fia {fia}: {count_fia[fia]} < {mn}")

summary = (f"total={n} naw={count_naw} fia={count_fia} mithal_harfi_true={harfi}")
if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    print(summary)
    sys.exit(1)
print("OK")
print(summary)
sys.exit(0)
