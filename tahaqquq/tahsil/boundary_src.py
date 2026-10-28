"""Hand-derived boundary cases, written out as compact tuples and serialised to
boundary.json / boundary_kalimat.json.  This file does NOT import oracle.py: every
expectation below was derived by reading spec.md by hand (derivation notes inline).
Run:  python3 -I boundary_src.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# characters (explicit code points)
FA, DA, KA, SU = "َ", "ُ", "ِ", "ْ"   # fatha damma kasra sukun
FAN, DAN, KAN = "ً", "ٌ", "ٍ"             # tanwins
SH = "ّ"                                            # shadda
SP = " "
TAB, NL, NBSP = "\u0009", "\u000a", " "
COMMA_AR = "،"
SUP_ALEF = "ٰ"                                      # not one of the eight marks
HAMZA, HA, ALIF, AIN = "ء", "ه", "ا", "ع"
QAF, KAF, SHIN, YA = "ق", "ك", "ش", "ي"
LAM, NUN, RA, TA = "ل", "ن", "ر", "ت"
SIN, BA, MIM, WAW = "س", "ب", "م", "و"
A_HAMZA_ABOVE, A_HAMZA_BELOW = "أ", "إ"       # أ إ
W_HAMZA, Y_HAMZA = "ؤ", "ئ"                    # ؤ ئ
TAM, MAQ, MADDA, WASLA, TAT = "ة", "ى", "آ", "ٱ", "ـ"

# names, code point for code point from the spec's «...»
I1 = "علامة على فاصل"
I2 = "علامة بلا حامل"
I3 = "حرف ليس في جدول المخارج"
I4 = "علامتان متعارضتان"
I5 = "قاعدة التطويل بعلامة"
I6F = "ألف محرّكة في أوّل الكلمة"
WASL = "قاعدة همزة الوصل"
I8 = "قاعدة الألف الممدودة"
I9 = "قاعدة التاء المربوطة"
I10 = "قاعدة الألف المقصورة"
I11 = "قاعدة التنوين"
I12 = "قاعدة ألف التنوين"
I13 = "قاعدة ألف الجماعة"
I14 = "قاعدة الشدّة بلا حركة"
LAMT = "قاعدة لام التعريف المدغمة"
AKH = "قاعدة الحرف الأخير بلا حركة"
MID = "حرف بلا حركة في غير آخر الكلمة"

# ---- amendment 1 (2026-10-28): explicit code points
I14A = ("قاعدة الشدّة "
        "في أوّل الكلمة")
FEH, DAD, GHAIN = "ف", "ض", "غ"   # ف ض غ


def L(a, b, sinf, cells=()):
    return ("L", a, b, sinf, "", list(cells))


def HH(a, b, cells):
    return L(a, b, "harfHaraka", cells)


def HM(a, b, cell):
    return L(a, b, "harfMadd", [cell])


def FS(a, b):
    return L(a, b, "fasil")


def HW(a, b):
    return L(a, b, "hamzaWasl")


def P(a, b, ism):
    return ("P", a, b, "-", ism, [])


def F(a, b, ism):
    return ("F", a, b, "-", ism, [])


# Cell values used below (4h+s, h from the table, by hand):
#   ب h=26 -> 104..107   ك h=8 -> 32..35   ت h=18 -> 72..75   ل h=13 -> 52..55
#   م h=27 -> 108..111   ش h=10 -> 40..43  س h=20 -> 80..83   ق h=7 -> 28..31
#   ر h=15 -> 60..63     ه h=1 -> 4..7     ا h=2 -> 8..11     ي h=11 -> 44..47
#   و h=28 -> 112..115   ء/seats h=0 -> 0..3
CASES = [
    # (label, nass, expectation)
    ("empty", "", []),
    ("R1 one space", SP, [FS(0, 1)]),
    ("R1 two spaces", SP + SP, [FS(0, 1), FS(1, 2)]),
    ("R1F space carrying fatha", SP + FA, [F(0, 2, I1)]),
    ("R1F space carrying two marks (rule 1 before rule 4)", SP + FA + DA, [F(0, 3, I1)]),
    ("R2 lone fatha", FA, [F(0, 1, I2)]),
    ("R2 text starts with two marks then ba", FA + DA + BA + FA, [F(0, 2, I2), HH(2, 4, [104])]),
    ("R2 starts with mark, then space, then bare ba (awwal+akhir)", FA + SP + BA,
     [F(0, 1, I2), FS(1, 2), P(2, 3, AKH)]),
    # mark-headed segment is part of the word, so the alif is not awwal; its prev has no marks
    ("R2 fathatan head then alif (alif not awwal; prev marks empty)", FAN + ALIF,
     [F(0, 1, I2), HM(1, 2, 11)]),
    ("R2 leading shadda then ba", SH + BA + FA, [F(0, 1, I2), HH(1, 3, [104])]),
    ("R3 latin letter", "a", [F(0, 1, I3)]),
    ("R3 latin letter carrying fatha (rule 3 before 4)", "a" + FA, [F(0, 2, I3)]),
    ("R3 digit", "1", [F(0, 1, I3)]),
    ("R3 arabic comma after ba", BA + FA + COMMA_AR, [HH(0, 2, [104]), F(2, 3, I3)]),
    # tab is not U+0020, so it does not split the word: the alif is not awwal
    ("R3 tab inside a word; alif after it not awwal", BA + FA + TAB + ALIF,
     [HH(0, 2, [104]), F(2, 3, I3), HM(3, 4, 11)]),
    ("R3 newline inside a word", BA + FA + NL + ALIF, [HH(0, 2, [104]), F(2, 3, I3), HM(3, 4, 11)]),
    ("R3 nbsp inside a word", BA + FA + NBSP + ALIF, [HH(0, 2, [104]), F(2, 3, I3), HM(3, 4, 11)]),
    # U+0670 is not one of the eight marks: own segment; ba is then bare, awwal, not akhir
    ("R3 superscript alef after ba", BA + SUP_ALEF, [F(0, 1, MID), F(1, 2, I3)]),
    ("R6 contrast: real space before alif -> awwal", BA + FA + SP + ALIF,
     [HH(0, 2, [104]), FS(2, 3), P(3, 4, WASL)]),
    ("R4 two shaddas", BA + FA + SH + SH, [F(0, 4, I4)]),
    ("R4 fatha + damma", BA + FA + DA, [F(0, 3, I4)]),
    ("R4 same vowel twice", BA + FA + FA, [F(0, 3, I4)]),
    ("R4 tanwin + haraka", BA + FAN + FA, [F(0, 3, I4)]),
    ("R4 two tanwins", BA + FAN + DAN, [F(0, 3, I4)]),
    ("R4 tatweel with two vowels (4 before 5)", TAT + FA + DA, [F(0, 3, I4)]),
    ("R4 madda alif with two vowels (4 before 8)", MADDA + FA + DA, [F(0, 3, I4)]),
    ("R4 ta marbuta with two vowels (4 before 9)", TAM + FA + DA, [F(0, 3, I4)]),
    ("R5 bare tatweel", TAT, [L(0, 1, "tatwil")]),
    ("R5 tatweel inside word", BA + FA + TAT + BA + FA, [HH(0, 2, [104]), L(2, 3, "tatwil"), HH(3, 5, [104])]),
    ("R5P tatweel with fatha", TAT + FA, [P(0, 2, I5)]),
    ("R5P tatweel with shadda only", TAT + SH, [P(0, 2, I5)]),
    ("R5 tatweel then bare alif (alif not awwal -> harfMadd)", TAT + ALIF, [L(0, 1, "tatwil"), HM(1, 2, 11)]),
    ("R6F alif awwal with fatha", ALIF + FA, [F(0, 2, I6F)]),
    ("R6F alif awwal with sukun (sukun is a vowel mark)", ALIF + SU, [F(0, 2, I6F)]),
    ("R6F alif awwal with fathatan (6 before 11)", ALIF + FAN, [F(0, 2, I6F)]),
    ("R6F alif wasla awwal with kasra", WASLA + KA, [F(0, 2, I6F)]),
    ("R6P bare alif alone", ALIF, [P(0, 1, WASL)]),
    ("R6P alif wasla alone", WASLA, [P(0, 1, WASL)]),
    ("R6P alif awwal with shadda only", ALIF + SH, [P(0, 2, WASL)]),
    ("R6P alif between spaces", SP + ALIF + SP, [FS(0, 1), P(1, 2, WASL), FS(2, 3)]),
    ("R1F/R6 space with mark still splits words", BA + FA + SP + FA + ALIF,
     [HH(0, 2, [104]), F(2, 4, I1), P(4, 5, WASL)]),
    ("R7 alif wasla mid-word with fatha", BA + FA + WASLA + FA, [HH(0, 2, [104]), P(2, 4, WASL)]),
    ("R8 madda alif alone", MADDA, [P(0, 1, I8)]),
    ("R8 madda alif mid-word with fatha", BA + FA + MADDA + FA, [HH(0, 2, [104]), P(2, 4, I8)]),
    ("R9 ta marbuta alone", TAM, [P(0, 1, I9)]),
    ("R9 ta marbuta with dammatan (9 before 11)", BA + FA + TAM + DAN, [HH(0, 2, [104]), P(2, 4, I9)]),
    ("R10 alif maqsura alone", MAQ, [P(0, 1, I10)]),
    ("R10 alif maqsura after ba", BA + FA + MAQ, [HH(0, 2, [104]), P(2, 3, I10)]),
    ("R11 dammatan", BA + DAN, [P(0, 2, I11)]),
    ("R11 shadda + fathatan", BA + SH + FAN, [P(0, 3, I11)]),
    ("R12 fathatan then alif", BA + FAN + ALIF, [P(0, 2, I11), P(2, 3, I12)]),
    ("R12 shadda+fathatan then alif", BA + SH + FAN + ALIF, [P(0, 3, I11), P(3, 4, I12)]),
    ("R12 needs no akhir: fathatan, alif, bare final ba", BA + FAN + ALIF + BA,
     [P(0, 2, I11), P(2, 3, I12), P(3, 4, AKH)]),
    ("R12 contrast: dammatan then alif -> harfMadd", BA + DAN + ALIF, [P(0, 2, I11), HM(2, 3, 11)]),
    ("R13 bare waw then final alif", BA + DA + WAW + ALIF, [HH(0, 2, [105]), HM(2, 3, 115), P(3, 4, I13)]),
    ("R13 waw with sukun then final alif", BA + DA + WAW + SU + ALIF,
     [HH(0, 2, [105]), HH(2, 4, [115]), P(4, 5, I13)]),
    ("R13 final alif before a space", BA + DA + WAW + ALIF + SP + BA + FA,
     [HH(0, 2, [105]), HM(2, 3, 115), P(3, 4, I13), FS(4, 5), HH(5, 7, [104])]),
    ("R13 kataboo", KAF + FA + TA + FA + BA + DA + WAW + ALIF,
     [HH(0, 2, [32]), HH(2, 4, [72]), HH(4, 6, [105]), HM(6, 7, 115), P(7, 8, I13)]),
    ("R13 word-initial waw then alif", WAW + ALIF, [F(0, 1, MID), P(1, 2, I13)]),
    ("R13 contrast: waw with fatha -> alif harfMadd", BA + DA + WAW + FA + ALIF,
     [HH(0, 2, [105]), HH(2, 4, [112]), HM(4, 5, 11)]),
    ("R13 contrast: alif not akhir", BA + DA + WAW + ALIF + BA,
     [HH(0, 2, [105]), HM(2, 3, 115), HM(3, 4, 11), P(4, 5, AKH)]),
    ("R13 contrast: waw with shadda only (R14) then alif", BA + DA + WAW + SH + ALIF,
     [HH(0, 2, [105]), P(2, 4, I14), HM(4, 5, 11)]),
    ("R13 contrast: waw with shadda+sukun then alif", BA + DA + WAW + SH + SU + ALIF,
     [HH(0, 2, [105]), HH(2, 5, [115, 115]), HM(5, 6, 11)]),
    ("R14 shadda alone on ba", BA + SH, [P(0, 2, I14)]),
    ("R14 shadda alone word-initial, then ba", BA + SH + BA + FA, [P(0, 2, I14), HH(2, 4, [104])]),
    ("R14 shadda alone on mid alif", BA + FA + ALIF + SH, [HH(0, 2, [104]), P(2, 4, I14)]),
    ("R15 harfMadd ya", BA + FA + YA, [HH(0, 2, [104]), HM(2, 3, 47)]),
    ("R15 harfMadd waw mid-word", BA + FA + WAW + BA + FA, [HH(0, 2, [104]), HM(2, 3, 115), HH(3, 5, [104])]),
    ("R15 harfMadd alif", BA + FA + ALIF, [HH(0, 2, [104]), HM(2, 3, 11)]),
    ("R15 ya alone (awwal, akhir)", YA, [P(0, 1, AKH)]),
    ("R15 waw alone", WAW, [P(0, 1, AKH)]),
    ("R15 ya awwal not akhir", YA + BA + FA, [F(0, 1, MID), HH(1, 3, [104])]),
    ("R15 al-shams", ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [P(0, 1, WASL), P(1, 2, LAMT), HH(2, 5, [43, 40]), HH(5, 7, [111]), HH(7, 9, [81])]),
    ("R15 al-shams with alif wasla", WASLA + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [P(0, 1, WASL), P(1, 2, LAMT), HH(2, 5, [43, 40]), HH(5, 7, [111]), HH(7, 9, [81])]),
    ("R15 Allahu (lam then lam with shadda)", ALIF + LAM + LAM + SH + FA + HA + DA,
     [P(0, 1, WASL), P(1, 2, LAMT), HH(2, 5, [55, 52]), HH(5, 7, [5])]),
    ("R15 lam rule ignores the alif's own verdict", ALIF + FA + LAM + SHIN + SH + FA,
     [F(0, 2, I6F), P(2, 3, LAMT), HH(3, 6, [43, 40])]),
    ("R15 lam rule: next has shadda only", ALIF + LAM + SHIN + SH,
     [P(0, 1, WASL), P(1, 2, LAMT), P(2, 4, I14)]),
    ("R15 lam rule: next is F but has shadda", ALIF + LAM + SHIN + SH + FA + DA,
     [P(0, 1, WASL), P(1, 2, LAMT), F(2, 6, I4)]),
    ("R15 al-qamar (lam with sukun is R16)", ALIF + LAM + SU + QAF + FA + MIM + FA + RA + DA,
     [P(0, 1, WASL), HH(1, 3, [55]), HH(3, 5, [28]), HH(5, 7, [108]), HH(7, 9, [61])]),
    ("R15 bare lam, next without shadda", ALIF + LAM + KAF + FA, [P(0, 1, WASL), F(1, 2, MID), HH(2, 4, [32])]),
    ("R15 'al' alone: lam akhir", ALIF + LAM, [P(0, 1, WASL), P(1, 2, AKH)]),
    ("R15 lam after non-alif first segment", BA + FA + LAM + SHIN + SH + FA,
     [HH(0, 2, [104]), F(2, 3, MID), HH(3, 6, [43, 40])]),
    # AMENDED (amendment 1): alif is now R14b hamzaWasl, so the lam is R15 lam-al (widened prev)
    ("R15 lam after alif that is not the first segment (wa-al-shams) [amended: R14b + widened R15]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [HH(0, 2, [112]), HW(2, 3), P(3, 4, LAMT), HH(4, 7, [43, 40]), HH(7, 9, [111]), HH(9, 11, [81])]),
    ("R15 word-initial lam (no prev)", LAM + SHIN + SH + FA, [F(0, 1, MID), HH(1, 4, [43, 40])]),
    ("R15 alif and lam separated by space", ALIF + SP + LAM + SHIN + SH + FA,
     [P(0, 1, WASL), FS(1, 2), F(2, 3, MID), HH(3, 6, [43, 40])]),
    ("R15 bare final letter", BA + FA + BA, [HH(0, 2, [104]), P(2, 3, AKH)]),
    ("R15 bare middle letter", BA + FA + BA + BA + FA, [HH(0, 2, [104]), F(2, 3, MID), HH(3, 5, [104])]),
    ("R15 bare hamza seat alone", A_HAMZA_ABOVE, [P(0, 1, AKH)]),
    ("R15 bare hamza seat word-initial", A_HAMZA_ABOVE + BA + FA, [F(0, 1, MID), HH(1, 3, [104])]),
    ("R15 bare hamza seat mid-word", BA + FA + A_HAMZA_ABOVE + BA + FA,
     [HH(0, 2, [104]), F(2, 3, MID), HH(3, 5, [104])]),
    ("R15 bare final hamza", BA + FA + HAMZA, [HH(0, 2, [104]), P(2, 3, AKH)]),
    ("R16 hamza on alif with fatha", A_HAMZA_ABOVE + FA, [HH(0, 2, [0])]),
    ("R16 hamza below alif with kasra", A_HAMZA_BELOW + KA, [HH(0, 2, [2])]),
    ("R16 hamza on waw with damma", W_HAMZA + DA, [HH(0, 2, [1])]),
    ("R16 hamza on ya with sukun", Y_HAMZA + SU, [HH(0, 2, [3])]),
    ("R16 bare hamza with fatha", HAMZA + FA, [HH(0, 2, [0])]),
    ("R14a hamza seat awwal with shadda+fatha [amended, was R16]", A_HAMZA_ABOVE + SH + FA, [P(0, 3, I14A)]),
    ("R14a fatha before shadda, awwal [amended, was R16]", BA + FA + SH, [P(0, 3, I14A)]),
    ("R14a shadda before fatha, awwal [amended, was R16]", BA + SH + FA, [P(0, 3, I14A)]),
    ("R14a shadda + sukun, awwal [amended, was R16]", BA + SH + SU, [P(0, 3, I14A)]),
    ("R14a ya awwal with shadda+kasra [amended, was R16]", YA + SH + KA, [P(0, 3, I14A)]),
    ("R16 alif with fatha mid-word", BA + FA + ALIF + FA, [HH(0, 2, [104]), HH(2, 4, [8])]),
    ("R16 alif with sukun mid-word", BA + FA + ALIF + SU, [HH(0, 2, [104]), HH(2, 4, [11])]),
    ("multiple spaces between words", BA + FA + SP + SP + BA + FA,
     [HH(0, 2, [104]), FS(2, 3), FS(3, 4), HH(4, 6, [104])]),
    # ================= amendment 1 (2026-10-28): rules 14a, 14b, widened 15 lam, hamzaWasl
    # All expectations below derived by hand from spec.md (cells: 4h+s, see table above;
    # also: f h=25 -> 100..103, d h=12 -> 48..51, gh h=5 -> 20..23, n h=14 -> 56..59).
    # --- 14b: wasl alif after a prefix with a short haraka, before a sukun-only carrier
    ("A1 R14b wa-istaghfir", WAW + FA + ALIF + SIN + SU + TA + FA + GHAIN + SU + FEH + KA + RA + SU,
     [HH(0, 2, [112]), HW(2, 3), HH(3, 5, [83]), HH(5, 7, [72]), HH(7, 9, [23]), HH(9, 11, [102]),
      HH(11, 13, [63])]),
    ("A2 R14b fa-ista", FEH + FA + ALIF + SIN + SU + TA + FA,
     [HH(0, 2, [100]), HW(2, 3), HH(3, 5, [83]), HH(5, 7, [72])]),
    ("A3 R14b bi-al-qa (lam with sukun)", BA + KA + ALIF + LAM + SU + QAF + FA,
     [HH(0, 2, [106]), HW(2, 3), HH(3, 5, [55]), HH(5, 7, [28])]),
    ("A4 R14b ka-al-ba", KAF + FA + ALIF + LAM + SU + BA + FA,
     [HH(0, 2, [32]), HW(2, 3), HH(3, 5, [55]), HH(5, 7, [104])]),
    ("A5 R14b li-ismi", LAM + KA + ALIF + SIN + SU + MIM + KA,
     [HH(0, 2, [54]), HW(2, 3), HH(3, 5, [83]), HH(5, 7, [110])]),
    ("A6 R14b prev with damma", BA + DA + ALIF + SIN + SU,
     [HH(0, 2, [105]), HW(2, 3), HH(3, 5, [83])]),
    # --- 14b lam branch + widened 15 lam bullet
    ("A7 R14b+R15 bi-allahi (lam, lam+shadda)", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [HH(0, 2, [106]), HW(2, 3), P(3, 4, LAMT), HH(4, 7, [55, 52]), HH(7, 9, [6])]),
    ("A8 R14b+R15 lam branch, after-lam has shadda only (R14)", WAW + FA + ALIF + LAM + SHIN + SH,
     [HH(0, 2, [112]), HW(2, 3), P(3, 4, LAMT), P(4, 6, I14)]),
    ("A9 bare lam, after it no shadda: alif harfMadd, lam F", WAW + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), F(3, 4, MID), HH(4, 6, [32])]),
    ("A10 bare lam at word end: alif harfMadd, lam akhir", WAW + FA + ALIF + LAM,
     [HH(0, 2, [112]), HM(2, 3, 11), P(3, 4, AKH)]),
    ("A11 shadda two segments after the lam does not count (immediate reading)",
     WAW + FA + ALIF + LAM + KAF + FA + TA + SH + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), F(3, 4, MID), HH(4, 6, [32]), HH(6, 9, [75, 72])]),
    # --- 14b must not fire
    ("A12 next has a vowel: harfMadd", BA + FA + ALIF + BA + FA,
     [HH(0, 2, [104]), HM(2, 3, 11), HH(3, 5, [104])]),
    ("A13 qala: next lam with fatha", QAF + FA + ALIF + LAM + FA,
     [HH(0, 2, [28]), HM(2, 3, 11), HH(3, 5, [52])]),
    ("A14 prev with sukun", BA + SU + ALIF + SIN + SU,
     [HH(0, 2, [107]), HM(2, 3, 11), HH(3, 5, [83])]),
    ("A15 prev with dammatan", BA + DAN + ALIF + SIN + SU,
     [P(0, 2, I11), HM(2, 3, 11), HH(3, 5, [83])]),
    ("A16 prev with fathatan: R12 first", BA + FAN + ALIF + SIN + SU,
     [P(0, 2, I11), P(2, 3, I12), HH(3, 5, [83])]),
    ("A17 bare prev", BA + ALIF + SIN + SU,
     [F(0, 1, MID), HM(1, 2, 11), HH(2, 4, [83])]),
    ("A18 alif awwal before sukun: R6", ALIF + SIN + SU + TA + FA,
     [P(0, 1, WASL), HH(1, 3, [83]), HH(3, 5, [72])]),
    ("A19 alif at word end, sukun letter in next word", BA + FA + ALIF + SP + SIN + SU,
     [HH(0, 2, [104]), HM(2, 3, 11), FS(3, 4), HH(4, 6, [83])]),
    ("A20 prefix and alif separated by space: R6", WAW + FA + SP + ALIF + SIN + SU,
     [HH(0, 2, [112]), FS(2, 3), P(3, 4, WASL), HH(4, 6, [83])]),
    ("A21 next sukun+shadda is not sukun alone", BA + FA + ALIF + SIN + SH + SU,
     [HH(0, 2, [104]), HM(2, 3, 11), HH(3, 6, [83, 83])]),
    ("A22 next ta marbuta with sukun (not a carrier)", BA + FA + ALIF + TAM + SU,
     [HH(0, 2, [104]), HM(2, 3, 11), P(3, 5, I9)]),
    ("A23 next alif maqsura with sukun (not a carrier)", BA + FA + ALIF + MAQ + SU,
     [HH(0, 2, [104]), HM(2, 3, 11), P(3, 5, I10)]),
    ("A24 next tatweel (not a carrier)", BA + FA + ALIF + TAT,
     [HH(0, 2, [104]), HM(2, 3, 11), L(3, 4, "tatwil")]),
    ("A25 next alif wasla with sukun (not in table)", BA + FA + ALIF + WASLA + SU,
     [HH(0, 2, [104]), HM(2, 3, 11), P(3, 5, WASL)]),
    ("A26 prev is mark-headed segment (no marks)", FA + ALIF + SIN + SU,
     [F(0, 1, I2), HM(1, 2, 11), HH(2, 4, [83])]),
    # --- 14b fires (edge)
    ("A27 next hamza seat with sukun", FEH + FA + ALIF + A_HAMZA_ABOVE + SU + TA + DA,
     [HH(0, 2, [100]), HW(2, 3), HH(3, 5, [3]), HH(5, 7, [73])]),
    ("A28 next bare hamza with sukun", BA + FA + ALIF + HAMZA + SU,
     [HH(0, 2, [104]), HW(2, 3), HH(3, 5, [3])]),
    ("A29 next alif with sukun (alif is a table carrier)", BA + FA + ALIF + ALIF + SU,
     [HH(0, 2, [104]), HW(2, 3), HH(3, 5, [11])]),
    ("A30 prev is R14a (shadda+kasra awwal): prev verdict ignored", BA + SH + KA + ALIF + SIN + SU,
     [P(0, 3, I14A), HW(3, 4), HH(4, 6, [83])]),
    ("A31 prev is F (fatha+damma) but has fatha", BA + FA + DA + ALIF + SIN + SU,
     [F(0, 3, I4), HW(3, 4), HH(4, 6, [83])]),
    ("A32 R12 pre-empts 14b, so the lam is not R15 lam-al (NOTES A7)",
     BA + FAN + FA + ALIF + LAM + SHIN + SH + FA,
     [F(0, 3, I4), P(3, 4, I12), F(4, 5, MID), HH(5, 8, [43, 40])]),
    # --- 14a: shadda on the word-initial carrier / hamza seat
    ("B1 R14a mim shadda+kasra awwal", MIM + SH + KA + NUN + FA,
     [P(0, 3, I14A), HH(3, 5, [56])]),
    ("B2 shadda only awwal: R14 before R14a", MIM + SH + MIM + KA + NUN + FA,
     [P(0, 2, I14), HH(2, 4, [110]), HH(4, 6, [56])]),
    ("B3 R14a hamza-on-waw seat shadda+damma awwal", W_HAMZA + SH + DA + BA + FA,
     [P(0, 3, I14A), HH(3, 5, [104])]),
    ("B4 R14a bare hamza shadda+fatha", HAMZA + SH + FA, [P(0, 3, I14A)]),
    ("B5 hamza seat shadda only awwal: R14", A_HAMZA_ABOVE + SH, [P(0, 2, I14)]),
    ("B6 R14a in second word", BA + FA + SP + MIM + SH + FA,
     [HH(0, 2, [104]), FS(2, 3), P(3, 6, I14A)]),
    ("B7 same letter not awwal: R16 two cells", BA + FA + MIM + SH + FA,
     [HH(0, 2, [104]), HH(2, 5, [111, 108])]),
    ("B8 shadda+sukun not awwal: R16", BA + FA + BA + SH + SU,
     [HH(0, 2, [104]), HH(2, 5, [107, 107])]),
    ("B9 shadda+dammatan awwal: R11 first", BA + SH + DAN, [P(0, 3, I11)]),
    ("B10 alif awwal shadda+fatha: R6 first", ALIF + SH + FA, [F(0, 3, I6F)]),
    ("B11 after mark-headed segment: not awwal", FA + BA + SH + FA,
     [F(0, 1, I2), HH(1, 4, [107, 104])]),
    ("B12 after a tab: not awwal", BA + FA + TAB + BA + SH + FA,
     [HH(0, 2, [104]), F(2, 3, I3), HH(3, 6, [107, 104])]),
    ("B13 ta marbuta awwal shadda+fatha: R9", TAM + SH + FA, [P(0, 3, I9)]),
    ("B14 tatweel awwal shadda+fatha: R5", TAT + SH + FA, [P(0, 3, I5)]),
    ("B15 after a space carrying a mark: awwal", BA + FA + SP + FA + MIM + SH + FA,
     [HH(0, 2, [104]), F(2, 4, I1), P(4, 7, I14A)]),
    ("B16 waw awwal shadda+fatha", WAW + SH + FA, [P(0, 3, I14A)]),
]

KALIMAT_CASES = [
    ("empty", "", []),
    ("spaces only: no words", SP + SP, []),
    ("two words", BA + FA + SP + BA + DA,
     [(0, 2, True, [104]), (3, 5, True, [105])]),
    ("tatweel alone: all L but no cell", TAT, [(0, 1, False, [])]),
    ("al-shams: P segments -> not licensed; cells still concatenated",
     ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA, [(0, 9, False, [43, 40, 111, 81])]),
    ("tatweel inside a licensed word", BA + FA + TAT + BA + FA, [(0, 5, True, [104, 104])]),
    ("tab does not split", BA + FA + TAB + BA + FA, [(0, 5, False, [104, 104])]),
    ("kataba", KAF + FA + TA + FA + BA + FA, [(0, 6, True, [32, 72, 104])]),
    ("leading/trailing spaces", SP + BA + FA + SP, [(1, 3, True, [104])]),
    # ================= amendment 1 (hand-derived)
    ("K1 wa-al-ardi fully licensed, no cell for the alif",
     WAW + FA + ALIF + LAM + SU + A_HAMZA_ABOVE + FA + RA + SU + DAD + KA,
     [(0, 11, True, [112, 55, 0, 63, 50])]),
    ("K2 wa-ista licensed", WAW + FA + ALIF + SIN + SU + TA + FA, [(0, 7, True, [112, 83, 72])]),
    ("K3 wa-al-shams not licensed (lam P)", WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [(0, 11, False, [112, 43, 40, 111, 82])]),
    ("K4 minna with word-initial shadda not licensed", MIM + SH + KA + NUN + FA, [(0, 5, False, [56])]),
    ("K5 second word with initial shadda", BA + FA + SP + MIM + SH + KA + NUN + FA,
     [(0, 2, True, [104]), (3, 8, False, [56])]),
    ("K6 bi-ismi licensed", BA + KA + ALIF + SIN + SU + MIM + KA, [(0, 7, True, [106, 83, 110])]),
    ("K7 qala: harfMadd alif keeps its cell", QAF + FA + ALIF + LAM + FA, [(0, 5, True, [28, 11, 52])]),
    ("K8 bi-allahi not licensed", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 9, False, [106, 55, 52, 6])]),
    ("K9 wa-istaghfir licensed", WAW + FA + ALIF + SIN + SU + TA + FA + GHAIN + SU + FEH + KA + RA + SU,
     [(0, 13, True, [112, 83, 72, 23, 102, 63])]),
    ("K10 non-initial shadda licensed", BA + FA + MIM + SH + FA, [(0, 5, True, [104, 111, 108])]),
]


def expand(exp):
    return [{"i": k, "a": a, "b": b, "hukm": h, "sinf": sinf, "ism": ism, "khalaya": cells}
            for k, (h, a, b, sinf, ism, cells) in enumerate(exp)]


def main():
    out = [{"label": lab, "nass": nass, "tawaqqu": expand(exp)} for lab, nass, exp in CASES]
    with open(os.path.join(HERE, "boundary.json"), "w", encoding="ascii") as f:
        json.dump(out, f, ensure_ascii=True, indent=1)
        f.write("\n")
    kout = [{"label": lab, "nass": nass,
             "tawaqqu": [{"a": a, "b": b, "murakhkhasa": m, "khalaya": c} for a, b, m, c in exp]}
            for lab, nass, exp in KALIMAT_CASES]
    with open(os.path.join(HERE, "boundary_kalimat.json"), "w", encoding="ascii") as f:
        json.dump(kout, f, ensure_ascii=True, indent=1)
        f.write("\n")
    print(len(out), "tahsil cases;", len(kout), "kalimat cases")


if __name__ == "__main__":
    main()
