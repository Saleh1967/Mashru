"""Independent oracle for the aligned tahsil (layer 1), written from spec.md alone.

Every special character is written as an explicit code point.  The rule names
("ism") are copied code point for code point from the spec's «...» quotes.
"""

# ---------------------------------------------------------------- constants

FATHA = "َ"
DAMMA = "ُ"
KASRA = "ِ"
SUKUN = "ْ"
FATHATAN = "ً"
DAMMATAN = "ٌ"
KASRATAN = "ٍ"
SHADDA = "ّ"

# the four harakat with their states
HARAKA_STATE = {FATHA: 0, DAMMA: 1, KASRA: 2, SUKUN: 3}
TANWIN = (FATHATAN, DAMMATAN, KASRATAN)
# "علامة حركة" = the four harakat or the three tanwins (seven)
VOWEL_MARKS = (FATHA, DAMMA, KASRA, SUKUN, FATHATAN, DAMMATAN, KASRATAN)
# the eight marks
MARKS = VOWEL_MARKS + (SHADDA,)

# carrier table, 29, in order, index from 0:
# ء ه ا ع ح غ خ ق ك ج ش ي ض ل ن ر ط د ت ز س ص ظ ذ ث ف ب م و
TABLE = [
    "ء",  # 0  ء
    "ه",  # 1  ه
    "ا",  # 2  ا
    "ع",  # 3  ع
    "ح",  # 4  ح
    "غ",  # 5  غ
    "خ",  # 6  خ
    "ق",  # 7  ق
    "ك",  # 8  ك
    "ج",  # 9  ج
    "ش",  # 10 ش
    "ي",  # 11 ي
    "ض",  # 12 ض
    "ل",  # 13 ل
    "ن",  # 14 ن
    "ر",  # 15 ر
    "ط",  # 16 ط
    "د",  # 17 د
    "ت",  # 18 ت
    "ز",  # 19 ز
    "س",  # 20 س
    "ص",  # 21 ص
    "ظ",  # 22 ظ
    "ذ",  # 23 ذ
    "ث",  # 24 ث
    "ف",  # 25 ف
    "ب",  # 26 ب
    "م",  # 27 م
    "و",  # 28 و
]
assert len(TABLE) == 29 and len(set(TABLE)) == 29
INDEX = {c: k for k, c in enumerate(TABLE)}

# hamza seats: أ إ ؤ ئ -- carrier 0
SEATS = ("أ", "إ", "ؤ", "ئ")

TA_MARBUTA = "ة"    # ة
ALIF_MAQSURA = "ى"  # ى
ALIF_MADDA = "آ"    # آ
ALIF_WASLA = "ٱ"    # ٱ
TATWEEL = "ـ"       # ـ
SPACE = " "
SPECIAL = (TA_MARBUTA, ALIF_MAQSURA, ALIF_MADDA, ALIF_WASLA, TATWEEL, SPACE)

ALIF = "ا"  # ا
WAW = "و"   # و
YA = "ي"    # ي
LAM = "ل"   # ل

# ---------------------------------------------------------------- names

ISM_1 = "علامة على فاصل"  # علامة على فاصل
ISM_2 = "علامة بلا حامل"  # علامة بلا حامل
ISM_3 = ("حرف ليس في جدول "
         "المخارج")  # حرف ليس في جدول المخارج
ISM_4 = "علامتان متعارضتان"  # علامتان متعارضتان
ISM_5 = ("قاعدة التطويل "
         "بعلامة")  # قاعدة التطويل بعلامة
ISM_6F = ("ألف محرّكة في "
          "أوّل الكلمة")  # ألف محرّكة في أوّل الكلمة
ISM_WASL = "قاعدة همزة الوصل"  # قاعدة همزة الوصل
ISM_8 = ("قاعدة الألف "
         "الممدودة")  # قاعدة الألف الممدودة
ISM_9 = ("قاعدة التاء "
         "المربوطة")  # قاعدة التاء المربوطة
ISM_10 = ("قاعدة الألف "
          "المقصورة")  # قاعدة الألف المقصورة
ISM_11 = "قاعدة التنوين"  # قاعدة التنوين
ISM_12 = "قاعدة ألف التنوين"  # قاعدة ألف التنوين
ISM_13 = "قاعدة ألف الجماعة"  # قاعدة ألف الجماعة
ISM_14 = ("قاعدة الشدّة "
          "بلا حركة")  # قاعدة الشدّة بلا حركة
# Amendment 1 (2026-10-28): rule 14أ name, written as explicit code points.
ISM_14A = ("قاعدة الشدّة "
           "في أوّل الكلمة")
SINF_WASL = "hamzaWasl"
# the three short harakat of rule 14ب (fatha, damma, kasra)
SHORT_HARAKAT = ("َ", "ُ", "ِ")
assert SHORT_HARAKAT == (FATHA, DAMMA, KASRA)
# Amendment 2 (2026-10-28): the seven letters of rule 14ب «و ف ب ك ل ت أ», code points copied
# from the spec: U+0648 U+0641 U+0628 U+0643 U+0644 U+062A U+0623.
CHAIN_LETTERS = ("و", "ف", "ب", "ك", "ل", "ت", "أ")
# Amendment 3 (2026-10-29): new sinf names, the tanwin states, the tanwin nun cell, and the
# fourteen letters of the assimilated lam «ن ر د ت ص ط ز س ظ ث ذ ض ش ل» (code points copied from
# the spec: U+0646 U+0631 U+062F U+062A U+0635 U+0637 U+0632 U+0633 U+0638 U+062B U+0630 U+0636
# U+0634 U+0644).
SINF_WASL_AL = "hamzaWaslAl"
SINF_MADDA = "madda"
SINF_TA_MARBUTA = "taMarbuta"
SINF_ALIF_MAQSURA = "alifMaqsura"
SINF_ALIF_KHATT = "alifKhatt"
SINF_TANWIN = "tanwin"
SINF_TANWIN_ALIF = "tanwinAlif"
SINF_HARAKA_MIN_TANWIN = "harakaMinTanwin"
SINF_SHADDA_IBTIDA = "shaddaIbtida"
SINF_LAM_MUDGHAM = "lamMudgham"
SINF_SUKUN_MUQADDAR = "sukunMuqaddar"
TANWIN_STATE = {"\u064b": 0, "\u064c": 1, "\u064d": 2}
assert set(TANWIN_STATE) == set(TANWIN)
NUN_TANWIN = 4 * 14 + 3  # 59
LAM_LETTERS = ("\u0646", "\u0631", "\u062f", "\u062a", "\u0635", "\u0637", "\u0632",
               "\u0633", "\u0638", "\u062b", "\u0630", "\u0636", "\u0634", "\u0644")
assert len(set(LAM_LETTERS)) == 14 and all(c in INDEX for c in LAM_LETTERS)
assert NUN_TANWIN == 4 * INDEX["\u0646"] + 3
TA_INDEX = 18  # ت
assert INDEX["\u062a"] == TA_INDEX
ISM_15_LAM = ("قاعدة لام التعريف "
              "المدغمة")  # قاعدة لام التعريف المدغمة
ISM_15_AKHIR = ("قاعدة الحرف "
                "الأخير بلا حركة")  # قاعدة الحرف الأخير بلا حركة
ISM_15_F = ("حرف بلا حركة في "
            "غير آخر الكلمة")  # حرف بلا حركة في غير آخر الكلمة

# ---------------------------------------------------------------- cutting


def _segments(text):
    """[(a, b)]: head T[a], then the longest run of marks T[a+1..b)."""
    segs = []
    n = len(text)
    i = 0
    while i < n:
        j = i + 1
        while j < n and text[j] in MARKS:
            j += 1
        segs.append((i, j))
        i = j
    return segs


def _words(text, segs):
    """Lists of segment indices: maximal runs of segments whose head is not SPACE."""
    words = []
    cur = []
    for k, (a, _b) in enumerate(segs):
        if text[a] == SPACE:
            if cur:
                words.append(cur)
                cur = []
        else:
            cur.append(k)
    if cur:
        words.append(cur)
    return words


# ---------------------------------------------------------------- classification


def _L(sinf, cells):
    return ("L", sinf, "", list(cells))


def _P(name):
    return ("P", "-", name, [])


def _F(name):
    return ("F", "-", name, [])


def _ctx(word, pos):
    return {
        "word": word,
        "awwal": pos == 0,
        "akhir": pos == len(word) - 1,
        "prev": word[pos - 1] if pos > 0 else None,
        "next": word[pos + 1] if pos + 1 < len(word) else None,
    }


def _is_14b(text, segs, k, ctx):
    """The conditions of rule 14ب alone (the caller has already ruled out rules 1-14أ)."""
    if ctx is None:
        return False
    a, b = segs[k]
    if text[a] != ALIF or b != a + 1 or ctx["awwal"]:
        return False
    prev, nxt = ctx["prev"], ctx["next"]
    if prev is None or nxt is None:
        return False
    # Amendment 2: every segment before the alif in its word has a head from
    # «و ف ب ك ل ت أ» and its marks are exactly one mark, a fatha, damma or kasra
    # (see NOTES B1-B5).
    word = ctx["word"]
    for idx in word[:word.index(k)]:
        ca, cb = segs[idx]
        if text[ca] not in CHAIN_LETTERS or text[ca + 1:cb] not in SHORT_HARAKAT:
            return False
    na, nb = segs[nxt]
    nhead, nmarks = text[na], text[na + 1:nb]
    if not (nhead in INDEX or nhead in SEATS):
        return False
    if nmarks == SUKUN:
        return True
    if nhead == LAM and nmarks == "":
        word = ctx["word"]
        pos = word.index(nxt)
        if pos + 1 < len(word):  # the segment right after the lam (see NOTES, amendment)
            fa, fb = segs[word[pos + 1]]
            if SHADDA in text[fa + 1:fb]:
                return True
    return False


def _lam_tarif_after(text, segs, k, ctx):
    """Amendment 3, «لامُ التعريف بعد المقطع k»: `next` exists and its head is ل, and its marks
    are either exactly one sukun, or nothing with the segment right after the lam in the word
    carrying a shadda (NOTES C1)."""
    nxt = ctx["next"]
    if nxt is None:
        return False
    na, nb = segs[nxt]
    if text[na] != LAM:
        return False
    nmarks = text[na + 1:nb]
    if nmarks == SUKUN:
        return True
    if nmarks == "":
        word = ctx["word"]
        pos = word.index(nxt)
        if pos + 1 < len(word):
            fa, fb = segs[word[pos + 1]]
            return SHADDA in text[fa + 1:fb]
    if SHADDA in nmarks:
        # amendment 4: the lam itself carries a shadda (أل assimilated into a lam-initial stem, الَّذِي),
        # provided a segment follows it in the word. Bare «الَّ» alone (no following segment) stays P (D7).
        word = ctx["word"]
        pos = word.index(nxt)
        return pos + 1 < len(word)
    return False


def _is_14b_at(text, segs, k, word):
    """True iff segment k's verdict (first matching rule) is rule 14ب."""
    res = _classify(text, segs, k, _ctx(word, word.index(k)))
    return res[0] == "L" and res[1] == SINF_WASL


def _classify(text, segs, k, ctx):
    """ctx: None for a segment outside any word, else dict with awwal, akhir, prev, next
    (prev/next are segment indices inside the same word, or None)."""
    a, b = segs[k]
    head = text[a]
    marks = text[a + 1:b]

    def marks_of(idx):
        pa, pb = segs[idx]
        return text[pa + 1:pb]

    n_shadda = sum(1 for m in marks if m == SHADDA)
    vowels = [m for m in marks if m in VOWEL_MARKS]
    has_tanwin = any(m in TANWIN for m in marks)

    # 1
    if head == SPACE:
        if not marks:
            return _L("fasil", [])
        return _F(ISM_1)
    # 2
    if head in MARKS:
        return _F(ISM_2)
    # 3
    if head not in INDEX and head not in SEATS and head not in SPECIAL:
        return _F(ISM_3)

    awwal = ctx["awwal"]
    akhir = ctx["akhir"]
    prev = ctx["prev"]
    nxt = ctx["next"]

    # 4
    if n_shadda > 1 or len(vowels) > 1:
        return _F(ISM_4)
    # 5
    if head == TATWEEL:
        if not marks:
            return _L("tatwil", [])
        return _P(ISM_5)
    word = ctx["word"]
    is_carrier = head in INDEX or head in SEATS
    h = 0 if head in SEATS else INDEX.get(head)

    def next_is_tanwin_alif():
        """Amendment 3, rules 14 and 15: `next` has head ا, its marks are exactly one fathatan,
        and it is `akhir` (NOTES C10)."""
        if nxt is None:
            return False
        na, nb = segs[nxt]
        return text[na] == ALIF and text[na + 1:nb] == FATHATAN and word[-1] == nxt

    # 6
    if head in (ALIF, ALIF_WASLA) and awwal:
        if vowels:
            return _F(ISM_6F)
        # amendment 3: bare, followed by «لامُ التعريف» -> hamzaWaslAl [0]
        if not marks and _lam_tarif_after(text, segs, k, ctx):
            return _L(SINF_WASL_AL, [0])
        return _P(ISM_WASL)
    # 7
    if head == ALIF_WASLA:
        return _P(ISM_WASL)
    # 8 (amendment 3: bare -> madda [0, 11])
    if head == ALIF_MADDA:
        if not marks:
            return _L(SINF_MADDA, [0, 4 * INDEX[ALIF] + 3])
        return _P(ISM_8)
    # 9 (amendment 3: akhir, exactly one mark: short haraka or tanwin)
    if head == TA_MARBUTA:
        if akhir and len(marks) == 1:
            if marks in SHORT_HARAKAT:
                return _L(SINF_TA_MARBUTA, [4 * TA_INDEX + HARAKA_STATE[marks]])
            if marks in TANWIN:
                return _L(SINF_TA_MARBUTA, [4 * TA_INDEX + TANWIN_STATE[marks], NUN_TANWIN])
        return _P(ISM_9)
    # 10 (amendment 3: bare, akhir, has prev; prev's marks contain fatha / fathatan)
    if head == ALIF_MAQSURA:
        if not marks and akhir and prev is not None:
            pm = marks_of(prev)
            if FATHA in pm:
                return _L(SINF_ALIF_MAQSURA, [4 * INDEX[ALIF] + 3])
            if FATHATAN in pm:
                return _L(SINF_ALIF_KHATT, [])
        return _P(ISM_10)
    # 11 (amendment 3)
    if has_tanwin:
        tan = [m for m in marks if m in TANWIN][0]
        s_t = TANWIN_STATE[tan]
        if ((head in INDEX and head not in (ALIF, WAW, YA)) or head in SEATS) \
                and not (awwal and n_shadda >= 1):
            after = word[word.index(k) + 1:]
            ok = True
            for idx in after:
                xa, xb = segs[idx]
                if text[xa] not in (ALIF, ALIF_MAQSURA) or xb != xa + 1:
                    ok = False
                    break
            if ok:
                if n_shadda == 1:
                    return _L(SINF_TANWIN, [4 * h + 3, 4 * h + s_t, NUN_TANWIN])
                return _L(SINF_TANWIN, [4 * h + s_t, NUN_TANWIN])
        if head == ALIF and marks == FATHATAN and akhir and prev is not None:
            return _L(SINF_TANWIN_ALIF, [NUN_TANWIN])
        return _P(ISM_11)
    # 12 (amendment 3: alifKhatt)
    if head == ALIF and not marks and prev is not None and FATHATAN in marks_of(prev):
        return _L(SINF_ALIF_KHATT, [])
    # 13 (amendment 3: alifKhatt)
    if head == ALIF and not marks and akhir and prev is not None:
        pa, _pb = segs[prev]
        pm = marks_of(prev)
        if text[pa] == WAW and (pm == "" or pm == SUKUN):
            return _L(SINF_ALIF_KHATT, [])
    # 14 (amendment 3: before a final «اً» -> harakaMinTanwin [4h+3, 4h+0])
    if n_shadda == 1 and not vowels:
        if is_carrier and next_is_tanwin_alif():
            return _L(SINF_HARAKA_MIN_TANWIN, [4 * h + 3, 4 * h + 0])
        return _P(ISM_14)
    # 14أ (amendment 1): table carrier or hamza seat, awwal, shadda in marks
    # amendment 3: with a short haraka s -> shaddaIbtida [4h+s]
    if is_carrier and awwal and n_shadda >= 1:
        shorts = [m for m in marks if m in SHORT_HARAKAT]
        if shorts:
            return _L(SINF_SHADDA_IBTIDA, [4 * h + HARAKA_STATE[shorts[0]]])
        return _P(ISM_14A)
    # 14ب (amendments 1, 2): wasl alif after a chain of one-letter prefixes, each with one
    # short haraka, before a "sakin"
    if _is_14b(text, segs, k, ctx):
        return _L(SINF_WASL, [])
    # 15
    if not marks:
        if head in (ALIF, WAW, YA) and not awwal:
            return _L("harfMadd", [4 * INDEX[head] + 3])
        if head == LAM and prev is not None and nxt is not None:
            pa, _pb = segs[prev]
            prev_is_first = ctx["word"][0] == prev
            prev_first_alif = prev_is_first and text[pa] in (ALIF, ALIF_WASLA)
            # amendment 1: or prev's verdict is by rule 14ب
            if (prev_first_alif or _is_14b_at(text, segs, prev, ctx["word"])) \
                    and SHADDA in marks_of(nxt):
                # amendment 3: next's head among the fourteen letters -> lamMudgham
                if text[segs[nxt][0]] in LAM_LETTERS:
                    return _L(SINF_LAM_MUDGHAM, [])
                return _P(ISM_15_LAM)
        # amendment 3: bare carrier/seat, not awwal
        if is_carrier and not awwal:
            if next_is_tanwin_alif():
                return _L(SINF_HARAKA_MIN_TANWIN, [4 * h + 0])
            return _L(SINF_SUKUN_MUQADDAR, [4 * h + 3])
        if akhir:
            return _P(ISM_15_AKHIR)
        return _F(ISM_15_F)
    # 16: exactly one of the four harakat (state s), at most one shadda
    assert len(vowels) == 1 and vowels[0] in HARAKA_STATE, (text, k)
    s = HARAKA_STATE[vowels[0]]
    h = 0 if head in SEATS else INDEX[head]
    if n_shadda == 1:
        return _L("harfHaraka", [4 * h + 3, 4 * h + s])
    return _L("harfHaraka", [4 * h + s])


def _analyse(text):
    segs = _segments(text)
    words = _words(text, segs)
    ctxs = [None] * len(segs)
    for w in words:
        for pos, k in enumerate(w):
            ctxs[k] = _ctx(w, pos)
    out = []
    for k, (a, b) in enumerate(segs):
        hukm, sinf, ism, cells = _classify(text, segs, k, ctxs[k])
        out.append({"i": k, "a": a, "b": b, "hukm": hukm, "sinf": sinf,
                    "ism": ism, "khalaya": cells})
    return out, words


def tahsil(text: str) -> list:
    return _analyse(text)[0]


def kalimat(text: str) -> list:
    """Per word: a = start of its first segment, b = end (exclusive, = j) of its last
    segment -- the same convention as a segment's (a, b); see NOTES.md."""
    segs_out, words = _analyse(text)
    res = []
    for w in words:
        cells = []
        for k in w:
            cells.extend(segs_out[k]["khalaya"])
        all_L = all(segs_out[k]["hukm"] == "L" for k in w)
        res.append({"a": segs_out[w[0]]["a"], "b": segs_out[w[-1]]["b"],
                    "murakhkhasa": bool(all_L and len(cells) >= 1),
                    "khalaya": cells})
    return res
