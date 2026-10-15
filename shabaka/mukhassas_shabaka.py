"""شبكة المخصّص لابن سيده: الأجناس، والألفاظ، والمصادر (النِّسَب إلى القائلين)، والشواهد.

نوع المودَع: «معلومات سابقة» (الدستور م12). المودَع مختوم ببصمته، ويُرفض باسمه إن تغيّر.
المصدر: OpenITI/0475ah، 0458IbnSidaMursi.Mukhassas.Shamela0003590-ara1، commit cc9beb0d.

ما يُستخرج، وكلّه بقواعد معلنة هنا لا بتأويل:
  ١. شجرة الأجناس: كتاب ← باب ← فصل/عنوان، من رؤوس OpenITI (### | و ### $).
  ٢. أزواج «لفظ - شرح»: ابن سيده يفصل اللفظ عن شرحه بـ « - ». اللفظ = آخر ثلاث كلمات على الأكثر
     قبل الشرطة لا تعبر حدًّا (نقطة، فاصلة، نقطتان، اسم قائل، أداة ربط معلنة).
  ٣. النسبة: كلّ زوج يُنسب إلى آخر قائل مذكور قبله في الفقرة نفسها («أبو عبيد:»...). ما لا قائل له
     يوسم «بلا نسبة صريحة». أسماء القائلين مأخوذة من تكرارها في المودَع نفسه (≥ 5 مرّات)، ولا تُدمج
     الأسماء المتعدّدة لشخص واحد (أبو علي/الفارسي) إلّا بجدول هويّة يُودَع لاحقًا.
  ٤. الشواهد الشعرية: فقرات ‎# (… ... …)‎. تُربط بالفصل، وبالزوج السابق لها ربطَ «مجاورة» فقط.
  ٥. روابط الأجناس: لفظٌ عنوانٌ في فصلٍ يرد في شرح زوجٍ في فصلٍ آخر ← رابط «يُشرح به» بين الفصلين.

كلّ عنصر يحمل موضعه: إزاحة المحرف في النصّ المختوم، وآخر علامة صفحة (PageV..P..) قبله.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

SLOT = {
    "kind": "معلومات سابقة", "author": "ابن سيده", "file": "mukhassas.txt",
    "uri": "0458IbnSidaMursi.Mukhassas.Shamela0003590-ara1",
    "repo": "OpenITI/0475ah", "commit": "cc9beb0d9645e8cdce892556423b9926a127054f",
    "sha256": "936c68e0c2c62ddbfb881c573487c7b37650ef69117bca364c219b6d1bf8e76c",
}

# القائلون: كما ظهروا في المودَع ≥ 5 مرّات (عُدّوا في الجلسة)، صيغةً سطحية بلا دمج.
QAILUN = [
    "صاحب العين", "ابن الأعرابي", "ابن السكيت", "أبو عبيدة", "أبو حنيفة", "أبو عبيد", "ابن دريد",
    "أبو زيد", "أبو علي", "أبو حاتم", "أبو عمرو", "أبو سعيد", "أبو صاعد", "ابن جني", "ابن قتيبة",
    "غير واحد", "الأصمعي", "سيبويه", "ثعلب", "الفارسي", "اللحياني", "السيرافي", "قطرب", "الشيباني",
    "الكلابيون", "المتعقب", "ثابت", "الفراء", "النضر", "الزجاجي", "الأحول", "غيره", "علي",
]
BILA = "بلا نسبة صريحة"

AR = r"ء-ي"
WORD = re.compile(rf"[{AR}]+")
# حدود لا يعبرها اللفظ المستخرج (أدوات ربط وأفعال قول)
STOP = {"و", "وقد", "قد", "وهو", "وهي", "هو", "هي", "والجمع", "وجمعها", "وجمعه", "جمعه", "جمعها",
        "قال", "وقال", "يقال", "ويقال", "ومنه", "منه", "وفي", "في", "وكذلك", "كذلك", "أي", "يعني",
        "إذا", "وإذا", "أن", "وأن", "إن", "وإن", "ما", "وما", "لا", "ولا", "به", "له", "وأنشد", "أنشد",
        "أيضا", "مثل", "مثله", "نحو", "كما", "على", "من", "عن", "إلى", "مع", "وهما", "هما"}

QAIL_RX = re.compile(
    r"(?:(?<=\s)|^)(?:و?قال\s+)?(" + "|".join(sorted(map(re.escape, QAILUN), key=len, reverse=True))
    + r")(?:\s*[:،,]|(?=\s))", re.M)
HEAD_RX = re.compile(r"^### (\|+|\$+) ?(.*)$")
PAGE_RX = re.compile(r"PageV\d+P\d+")
MS_RX = re.compile(r"\bms\d+\b")
POEM_RX = re.compile(r"^\(.*\.\.\..*\)\s*$")


def sealed_text(path: str) -> str:
    raw = open(path, "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    if h != SLOT["sha256"]:
        raise ValueError(f"المودَع مختوم بغير هذه البصمة: {h}")
    return raw.decode("utf-8")


def _clean_title(s: str) -> str:
    s = re.sub(r"[()\[\]]", "", s).strip(" ،,.-")
    return re.sub(r"\s+", " ", s)


def _level(mark: str, title: str) -> tuple[int, str]:
    if mark.startswith("$"):
        return 3, "فصل"
    if title.startswith("كتاب"):
        return 1, "كتاب"
    if title in ("المقدمة", "الجزء") or not title:
        return 0, "رأس"
    if title.startswith("باب"):
        return 2, "باب"
    return 2, "عنوان"


def parse(text: str):
    """يعيد (الأجناس، الفقرات). الفقرة: (معرّف الجنس، الإزاحة، الصفحة، النصّ، شعر؟)."""
    lines = text.split("\n")
    off = 0
    offs = []
    for ln in lines:
        offs.append(off)
        off += len(ln) + 1
    start = next(i for i, ln in enumerate(lines) if ln.startswith("#META#Header#End#"))

    nodes = []          # {id, naw, title, parent, off, page}
    stack = {0: None, 1: None, 2: None}
    pending_num = None  # رأس مقسوم: «3 - » ثم العنوان في السطر التالي
    page = None
    paras = []
    cur = None          # [jins_id, off, page, [parts]]

    def flush():
        nonlocal cur
        if cur:
            body = " ".join(cur[3])
            body = MS_RX.sub("", body)
            body = PAGE_RX.sub("", body)
            body = re.sub(r"\s+", " ", body).strip()
            if body:
                paras.append((cur[0], cur[1], cur[2], body, bool(POEM_RX.match(body))))
        cur = None

    for i in range(start + 1, len(lines)):
        ln = lines[i]
        pm = PAGE_RX.search(ln)
        if pm:
            page = pm.group(0)
        hm = HEAD_RX.match(ln)
        if hm:
            flush()
            mark, title = hm.group(1), _clean_title(hm.group(2))
            if re.fullmatch(r"\d+\s*-?", title):
                pending_num = (mark, offs[i])
                continue
            if pending_num:
                mark = pending_num[0]
                pending_num = None
            title = re.sub(r"^\d+\s*-\s*", "", title)
            lvl, naw = _level(mark, title)
            parent = None
            for k in range(lvl - 1, 0, -1):
                if stack.get(k) is not None:
                    parent = stack[k]
                    break
            nid = len(nodes)
            nodes.append({"id": nid, "naw": naw, "title": title, "parent": parent,
                          "off": offs[i], "page": page})
            if lvl > 0:  # رأس الجزء علامة مجلّد لا جنس: لا يقطع شجرة الكتاب
                stack[lvl] = nid
                for k in range(lvl + 1, 3):
                    stack[k] = None
            continue
        if ln.startswith("# ") or ln.startswith("#\t"):
            flush()
            if nodes:
                cur = [nodes[-1]["id"], offs[i], page, [ln[2:]]]
        elif ln.startswith("~~") and cur:
            cur[3].append(ln[2:])
    flush()
    return nodes, paras


def _tail_lafz(left: str) -> list[str] | None:
    """آخر ثلاث كلمات على الأكثر قبل الشرطة، لا تعبر حدًّا. يعيد قائمة الألفاظ (المعطوفة بالواو)."""
    seg = re.split(r"[.،,:؟!_;\"«»()]", left)[-1]
    for q in sorted(QAILUN, key=len, reverse=True):
        seg = re.sub(rf"(?:^|\s)(?:و?قال\s+)?{re.escape(q)}(?=\s|$)", " ", seg)
    toks = seg.split()
    take = []
    n_all = len(toks)
    for tkn in reversed(toks):
        if tkn in STOP or not WORD.fullmatch(tkn):
            break
        take.append(tkn)
        if len(take) == 3:
            break
    if not take:
        return None
    take.reverse()
    # «في العين المقلة - …» = في العين: المقلة؛ فإن سبق اللفظَ حرفُ جرّ أُسقطت كلمته الأولى
    prev = toks[n_all - len(take) - 1] if n_all > len(take) else None
    if prev in ("في", "وفي", "من", "ومن") and len(take) > 1:
        take = take[1:]
    if take[0].startswith("وال"):
        take[0] = take[0][1:]
    # المعطوف: «الهانة والهنانة» ← لفظان؛ والمضاف «مخ العين» ← لفظ واحد
    out, buf = [], []
    for tkn in take:
        if buf and tkn.startswith("و") and len(tkn) > 3 and tkn[1:2] == "ا" and tkn[1:3] == "ال":
            out.append(" ".join(buf))
            buf = [tkn[1:]]
        else:
            buf.append(tkn)
    out.append(" ".join(buf))
    return out


def extract(path: str):
    text = sealed_text(path)
    nodes, paras = parse(text)
    pairs, poems, rejected = [], [], Counter()
    for (jid, off, page, body, is_poem) in paras:
        if is_poem:
            poems.append({"jins": jid, "off": off, "page": page, "bayt": body,
                          "jar": pairs[-1]["id"] if pairs and pairs[-1]["jins"] == jid else None})
            continue
        # النسبة: مواضع القائلين في الفقرة
        marks = [(m.start(), m.group(1)) for m in QAIL_RX.finditer(body)]
        for dm in re.finditer(r" - ", body):
            left, after = body[:dm.start()], body[dm.end():]
            lafz = _tail_lafz(left)
            if not lafz:
                rejected["لا لفظ قبل الشرطة"] += 1
                continue
            gloss = re.split(r"\.\s|\s-\s", after, maxsplit=1)[0]
            # إن قُطع الشرح عند شرطة تالية، فآخر كلماته لفظ الزوج التالي: احذفه
            nxt = re.search(r"\s-\s", after)
            if nxt and (not re.search(r"\.\s", after) or nxt.start() < re.search(r"\.\s", after).start()):
                g_toks = gloss.split()
                tl = _tail_lafz(gloss) or []
                drop = sum(len(x.split()) for x in tl)
                gloss = " ".join(g_toks[:max(1, len(g_toks) - drop)])
            gloss = QAIL_RX.split(gloss)[0].strip(" ،,_")
            gt = gloss.split()
            while gt and gt[-1] in STOP:
                gt.pop()
            gloss = " ".join(gt)
            if len(gloss) < 2:
                rejected["شرح فارغ"] += 1
                continue
            qail = BILA
            for (p, q) in marks:
                if p < dm.start():
                    qail = q
            for lf in lafz:
                pairs.append({"id": len(pairs), "jins": jid, "lafz": lf, "sharh": gloss[:300],
                              "qail": qail, "off": off + dm.start(), "page": page})
    return text, nodes, pairs, poems, rejected


def norm(w: str) -> str:
    w = re.sub("[أإآ]", "ا", w)
    w = w.replace("ة", "ه").replace("ى", "ي")
    if w.startswith("ال") and len(w) > 4:
        w = w[2:]
    return w


def links(nodes, pairs, max_jins=3):
    """رابط «يُشرح به»: لفظ عنوان في فصل B (مفرد الكلمة، يرد في ≤ max_jins أجناس) يقع في شرح زوج في فصل A ≠ B."""
    home = defaultdict(set)
    for p in pairs:
        if " " not in p["lafz"]:
            home[norm(p["lafz"])].add(p["jins"])
    home = {k: v for k, v in home.items() if len(v) <= max_jins and len(k) >= 3}
    w = Counter()
    ev = defaultdict(list)
    for p in pairs:
        seen = set()
        for tok in WORD.findall(p["sharh"]):
            k = norm(tok)
            if k in home and k not in seen:
                seen.add(k)
                for b in home[k]:
                    if b != p["jins"]:
                        w[(p["jins"], b)] += 1
                        if len(ev[(p["jins"], b)]) < 3:
                            ev[(p["jins"], b)].append({"lafz": tok, "pair": p["id"]})
    return [{"min": a, "ila": b, "wazn": c, "shawahid": ev[(a, b)]} for (a, b), c in w.most_common()]


def main(path: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    text, nodes, pairs, poems, rejected = extract(path)
    lk = links(nodes, pairs)
    stats = {
        "slot": SLOT,
        "ajnas": len(nodes),
        "ajnas_bil_naw": dict(Counter(n["naw"] for n in nodes)),
        "azwaj": len(pairs),
        "alfaz_mutamayyiza": len({norm(p["lafz"]) for p in pairs}),
        "shawahid_shiriyya": len(poems),
        "mansub": sum(p["qail"] != BILA for p in pairs),
        "qailun": dict(Counter(p["qail"] for p in pairs).most_common()),
        "marfud": dict(rejected),
        "rawabit": len(lk),
    }
    json.dump({"slot": SLOT, "ajnas": nodes}, open(os.path.join(out_dir, "ajnas.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(pairs, open(os.path.join(out_dir, "azwaj.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(poems, open(os.path.join(out_dir, "shawahid.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(lk, open(os.path.join(out_dir, "rawabit.json"), "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(stats, open(os.path.join(out_dir, "ihsa.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in stats.items() if k not in ("slot", "qailun")}, ensure_ascii=False, indent=1))
    print("أكثر القائلين:", list(stats["qailun"].items())[:12])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
