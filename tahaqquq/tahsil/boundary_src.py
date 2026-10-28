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
# ---- amendment 3
DAL = "\u062f"   # د


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


# ---- amendment 3 (2026-10-29) sinf helpers
def WA(a, b):
    return L(a, b, "hamzaWaslAl", [0])


def MD(a, b):
    return L(a, b, "madda", [0, 11])


def TM(a, b, cells):
    return L(a, b, "taMarbuta", cells)


def AM(a, b):
    return L(a, b, "alifMaqsura", [11])


def AK(a, b):
    return L(a, b, "alifKhatt")


def TN(a, b, cells):
    return L(a, b, "tanwin", cells)


def TNA(a, b):
    return L(a, b, "tanwinAlif", [59])


def HT(a, b, cells):
    return L(a, b, "harakaMinTanwin", cells)


def SI(a, b, cell):
    return L(a, b, "shaddaIbtida", [cell])


def LM(a, b):
    return L(a, b, "lamMudgham")


def SM(a, b, cell):
    return L(a, b, "sukunMuqaddar", [cell])


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
    ("R8 madda alif alone [amended-3: bare madda]", MADDA, [MD(0, 1)]),
    ("R8 madda alif mid-word with fatha", BA + FA + MADDA + FA, [HH(0, 2, [104]), P(2, 4, I8)]),
    ("R9 ta marbuta alone", TAM, [P(0, 1, I9)]),
    ("R9 ta marbuta with dammatan (9 before 11) [amended-3: akhir, one tanwin]", BA + FA + TAM + DAN,
     [HH(0, 2, [104]), TM(2, 4, [73, 59])]),
    ("R10 alif maqsura alone", MAQ, [P(0, 1, I10)]),
    ("R10 alif maqsura after ba [amended-3: after fatha]", BA + FA + MAQ, [HH(0, 2, [104]), AM(2, 3)]),
    ("R11 dammatan [amended-3: tanwin, nothing after]", BA + DAN, [TN(0, 2, [105, 59])]),
    ("R11 shadda + fathatan", BA + SH + FAN, [P(0, 3, I11)]),
    ("R12 fathatan then alif [amended-3: tanwin + alifKhatt]", BA + FAN + ALIF, [TN(0, 2, [104, 59]), AK(2, 3)]),
    ("R12 shadda+fathatan then alif [amended-3: awwal+shadda stays P; alif alifKhatt]", BA + SH + FAN + ALIF,
     [P(0, 3, I11), AK(3, 4)]),
    ("R12 needs no akhir: fathatan, alif, bare final ba [amended-3]", BA + FAN + ALIF + BA,
     [P(0, 2, I11), AK(2, 3), SM(3, 4, 107)]),
    ("R12 contrast: dammatan then alif -> harfMadd [amended-3: tanwin]", BA + DAN + ALIF,
     [TN(0, 2, [105, 59]), HM(2, 3, 11)]),
    ("R13 bare waw then final alif [amended-3]", BA + DA + WAW + ALIF, [HH(0, 2, [105]), HM(2, 3, 115), AK(3, 4)]),
    ("R13 waw with sukun then final alif [amended-3]", BA + DA + WAW + SU + ALIF,
     [HH(0, 2, [105]), HH(2, 4, [115]), AK(4, 5)]),
    ("R13 final alif before a space [amended-3]", BA + DA + WAW + ALIF + SP + BA + FA,
     [HH(0, 2, [105]), HM(2, 3, 115), AK(3, 4), FS(4, 5), HH(5, 7, [104])]),
    ("R13 kataboo [amended-3]", KAF + FA + TA + FA + BA + DA + WAW + ALIF,
     [HH(0, 2, [32]), HH(2, 4, [72]), HH(4, 6, [105]), HM(6, 7, 115), AK(7, 8)]),
    ("R13 word-initial waw then alif [amended-3]", WAW + ALIF, [F(0, 1, MID), AK(1, 2)]),
    ("R13 contrast: waw with fatha -> alif harfMadd", BA + DA + WAW + FA + ALIF,
     [HH(0, 2, [105]), HH(2, 4, [112]), HM(4, 5, 11)]),
    ("R13 contrast: alif not akhir [amended-3: final ba sukunMuqaddar]", BA + DA + WAW + ALIF + BA,
     [HH(0, 2, [105]), HM(2, 3, 115), HM(3, 4, 11), SM(4, 5, 107)]),
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
    ("R15 al-shams [amended-3: hamzaWaslAl + lamMudgham]", ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [43, 40]), HH(5, 7, [111]), HH(7, 9, [81])]),
    ("R15 al-shams with alif wasla [amended-3]", WASLA + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [43, 40]), HH(5, 7, [111]), HH(7, 9, [81])]),
    ("R15 Allahu (lam then lam with shadda) [amended-3]", ALIF + LAM + LAM + SH + FA + HA + DA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [55, 52]), HH(5, 7, [5])]),
    ("R15 lam rule ignores the alif's own verdict [amended-3: lamMudgham]", ALIF + FA + LAM + SHIN + SH + FA,
     [F(0, 2, I6F), LM(2, 3), HH(3, 6, [43, 40])]),
    ("R15 lam rule: next has shadda only [amended-3]", ALIF + LAM + SHIN + SH,
     [WA(0, 1), LM(1, 2), P(2, 4, I14)]),
    ("R15 lam rule: next is F but has shadda [amended-3]", ALIF + LAM + SHIN + SH + FA + DA,
     [WA(0, 1), LM(1, 2), F(2, 6, I4)]),
    ("R15 al-qamar (lam with sukun is R16) [amended-3: hamzaWaslAl]",
     ALIF + LAM + SU + QAF + FA + MIM + FA + RA + DA,
     [WA(0, 1), HH(1, 3, [55]), HH(3, 5, [28]), HH(5, 7, [108]), HH(7, 9, [61])]),
    ("R15 bare lam, next without shadda [amended-3: lam sukunMuqaddar]", ALIF + LAM + KAF + FA,
     [P(0, 1, WASL), SM(1, 2, 55), HH(2, 4, [32])]),
    ("R15 'al' alone [amended-3: lam sukunMuqaddar]", ALIF + LAM, [P(0, 1, WASL), SM(1, 2, 55)]),
    ("R15 lam after non-alif first segment [amended-3: sukunMuqaddar]", BA + FA + LAM + SHIN + SH + FA,
     [HH(0, 2, [104]), SM(2, 3, 55), HH(3, 6, [43, 40])]),
    # AMENDED (amendment 1): alif is now R14b hamzaWasl, so the lam is R15 lam-al (widened prev)
    ("R15 lam after alif that is not the first segment (wa-al-shams) [amended: R14b + widened R15] [amended-3]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [HH(0, 2, [112]), HW(2, 3), LM(3, 4), HH(4, 7, [43, 40]), HH(7, 9, [111]), HH(9, 11, [81])]),
    ("R15 word-initial lam (no prev)", LAM + SHIN + SH + FA, [F(0, 1, MID), HH(1, 4, [43, 40])]),
    ("R15 alif and lam separated by space", ALIF + SP + LAM + SHIN + SH + FA,
     [P(0, 1, WASL), FS(1, 2), F(2, 3, MID), HH(3, 6, [43, 40])]),
    ("R15 bare final letter [amended-3: sukunMuqaddar]", BA + FA + BA, [HH(0, 2, [104]), SM(2, 3, 107)]),
    ("R15 bare middle letter [amended-3: sukunMuqaddar]", BA + FA + BA + BA + FA,
     [HH(0, 2, [104]), SM(2, 3, 107), HH(3, 5, [104])]),
    ("R15 bare hamza seat alone", A_HAMZA_ABOVE, [P(0, 1, AKH)]),
    ("R15 bare hamza seat word-initial", A_HAMZA_ABOVE + BA + FA, [F(0, 1, MID), HH(1, 3, [104])]),
    ("R15 bare hamza seat mid-word [amended-3: sukunMuqaddar]", BA + FA + A_HAMZA_ABOVE + BA + FA,
     [HH(0, 2, [104]), SM(2, 3, 3), HH(3, 5, [104])]),
    ("R15 bare final hamza [amended-3: sukunMuqaddar]", BA + FA + HAMZA, [HH(0, 2, [104]), SM(2, 3, 3)]),
    ("R16 hamza on alif with fatha", A_HAMZA_ABOVE + FA, [HH(0, 2, [0])]),
    ("R16 hamza below alif with kasra", A_HAMZA_BELOW + KA, [HH(0, 2, [2])]),
    ("R16 hamza on waw with damma", W_HAMZA + DA, [HH(0, 2, [1])]),
    ("R16 hamza on ya with sukun", Y_HAMZA + SU, [HH(0, 2, [3])]),
    ("R16 bare hamza with fatha", HAMZA + FA, [HH(0, 2, [0])]),
    ("R14a hamza seat awwal with shadda+fatha [amended, was R16] [amended-3: shaddaIbtida]",
     A_HAMZA_ABOVE + SH + FA, [SI(0, 3, 0)]),
    ("R14a fatha before shadda, awwal [amended, was R16] [amended-3]", BA + FA + SH, [SI(0, 3, 104)]),
    ("R14a shadda before fatha, awwal [amended, was R16] [amended-3]", BA + SH + FA, [SI(0, 3, 104)]),
    ("R14a shadda + sukun, awwal [amended, was R16]", BA + SH + SU, [P(0, 3, I14A)]),
    ("R14a ya awwal with shadda+kasra [amended, was R16] [amended-3]", YA + SH + KA, [SI(0, 3, 46)]),
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
    ("A7 R14b+R15 bi-allahi (lam, lam+shadda) [amended-3: lamMudgham]", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [HH(0, 2, [106]), HW(2, 3), LM(3, 4), HH(4, 7, [55, 52]), HH(7, 9, [6])]),
    ("A8 R14b+R15 lam branch, after-lam has shadda only (R14) [amended-3]", WAW + FA + ALIF + LAM + SHIN + SH,
     [HH(0, 2, [112]), HW(2, 3), LM(3, 4), P(4, 6, I14)]),
    ("A9 bare lam, after it no shadda: alif harfMadd, lam sukunMuqaddar [amended-3]",
     WAW + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),
    ("A10 bare lam at word end: alif harfMadd, lam sukunMuqaddar [amended-3]", WAW + FA + ALIF + LAM,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55)]),
    ("A11 shadda two segments after the lam does not count (immediate reading) [amended-3]",
     WAW + FA + ALIF + LAM + KAF + FA + TA + SH + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32]), HH(6, 9, [75, 72])]),
    # --- 14b must not fire
    ("A12 next has a vowel: harfMadd", BA + FA + ALIF + BA + FA,
     [HH(0, 2, [104]), HM(2, 3, 11), HH(3, 5, [104])]),
    ("A13 qala: next lam with fatha", QAF + FA + ALIF + LAM + FA,
     [HH(0, 2, [28]), HM(2, 3, 11), HH(3, 5, [52])]),
    ("A14 prev with sukun", BA + SU + ALIF + SIN + SU,
     [HH(0, 2, [107]), HM(2, 3, 11), HH(3, 5, [83])]),
    ("A15 prev with dammatan", BA + DAN + ALIF + SIN + SU,
     [P(0, 2, I11), HM(2, 3, 11), HH(3, 5, [83])]),
    ("A16 prev with fathatan: R12 first [amended-3: alifKhatt]", BA + FAN + ALIF + SIN + SU,
     [P(0, 2, I11), AK(2, 3), HH(3, 5, [83])]),
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
    # AMENDED (amendment 2): prev carries two marks, so it is not a one-mark chain segment -> no 14b
    ("A30 prev is R14a (shadda+kasra awwal): two marks break the chain [amended-2] [amended-3]",
     BA + SH + KA + ALIF + SIN + SU,
     [SI(0, 3, 106), HM(3, 4, 11), HH(4, 6, [83])]),
    ("A31 prev is F (fatha+damma): two marks break the chain [amended-2]", BA + FA + DA + ALIF + SIN + SU,
     [F(0, 3, I4), HM(3, 4, 11), HH(4, 6, [83])]),
    ("A32 R12 pre-empts 14b, so the lam is not R15 lam-al (NOTES A7) [amended-3]",
     BA + FAN + FA + ALIF + LAM + SHIN + SH + FA,
     [F(0, 3, I4), AK(3, 4), SM(4, 5, 55), HH(5, 8, [43, 40])]),
    # --- 14a: shadda on the word-initial carrier / hamza seat
    ("B1 R14a mim shadda+kasra awwal [amended-3]", MIM + SH + KA + NUN + FA,
     [SI(0, 3, 110), HH(3, 5, [56])]),
    ("B2 shadda only awwal: R14 before R14a", MIM + SH + MIM + KA + NUN + FA,
     [P(0, 2, I14), HH(2, 4, [110]), HH(4, 6, [56])]),
    ("B3 R14a hamza-on-waw seat shadda+damma awwal [amended-3]", W_HAMZA + SH + DA + BA + FA,
     [SI(0, 3, 1), HH(3, 5, [104])]),
    ("B4 R14a bare hamza shadda+fatha [amended-3]", HAMZA + SH + FA, [SI(0, 3, 0)]),
    ("B5 hamza seat shadda only awwal: R14", A_HAMZA_ABOVE + SH, [P(0, 2, I14)]),
    ("B6 R14a in second word [amended-3]", BA + FA + SP + MIM + SH + FA,
     [HH(0, 2, [104]), FS(2, 3), SI(3, 6, 108)]),
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
    ("B15 after a space carrying a mark: awwal [amended-3]", BA + FA + SP + FA + MIM + SH + FA,
     [HH(0, 2, [104]), F(2, 4, I1), SI(4, 7, 108)]),
    ("B16 waw awwal shadda+fatha [amended-3]", WAW + SH + FA, [SI(0, 3, 112)]),
    # ================= amendment 2 (2026-10-28): 14b needs every segment before the alif in its
    # word to be one of «و ف ب ك ل ت أ» with exactly one mark, fatha/damma/kasra.
    # Hand-derived.  Cells: و 112..115, ف 100..103, ب 104..107, ك 32..35, ل 52..55, ت 72..75,
    # أ/إ/ء 0..3, س 80..83, ق 28..31, ن 56..59, م 108..111, ش 40..43, ه 4..7.
    # A chain segment (one short haraka, no shadda) is always R16 with one cell.
    # --- each of the seven letters as the single segment before the alif
    ("C1 waw-fatha chain of one", WAW + FA + ALIF + SIN + SU,
     [HH(0, 2, [112]), HW(2, 3), HH(3, 5, [83])]),
    ("C2 fa-kasra chain of one", FEH + KA + ALIF + SIN + SU,
     [HH(0, 2, [102]), HW(2, 3), HH(3, 5, [83])]),
    ("C3 ba-damma chain of one", BA + DA + ALIF + SIN + SU,
     [HH(0, 2, [105]), HW(2, 3), HH(3, 5, [83])]),
    ("C4 kaf-fatha chain of one", KAF + FA + ALIF + SIN + SU,
     [HH(0, 2, [32]), HW(2, 3), HH(3, 5, [83])]),
    ("C5 lam-kasra chain of one", LAM + KA + ALIF + SIN + SU,
     [HH(0, 2, [54]), HW(2, 3), HH(3, 5, [83])]),
    ("C6 ta-fatha chain of one", TA + FA + ALIF + SIN + SU,
     [HH(0, 2, [72]), HW(2, 3), HH(3, 5, [83])]),
    ("C7 hamza-on-alif fatha chain of one", A_HAMZA_ABOVE + FA + ALIF + SIN + SU,
     [HH(0, 2, [0]), HW(2, 3), HH(3, 5, [83])]),
    # --- chains of two and three
    ("C8 chain of two a-fa", A_HAMZA_ABOVE + FA + FEH + FA + ALIF + SIN + SU + TA + FA,
     [HH(0, 2, [0]), HH(2, 4, [100]), HW(4, 5), HH(5, 7, [83]), HH(7, 9, [72])]),
    ("C9 chain of two wa-bi", WAW + FA + BA + KA + ALIF + SIN + SU,
     [HH(0, 2, [112]), HH(2, 4, [106]), HW(4, 5), HH(5, 7, [83])]),
    ("C10 chain of three a-fa-bi", A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + SIN + SU,
     [HH(0, 2, [0]), HH(2, 4, [100]), HH(4, 6, [106]), HW(6, 7), HH(7, 9, [83])]),
    ("C11 chain of three wa-li-tu (any order, any short haraka)",
     WAW + FA + LAM + KA + TA + DA + ALIF + SIN + SU,
     [HH(0, 2, [112]), HH(2, 4, [54]), HH(4, 6, [73]), HW(6, 7), HH(7, 9, [83])]),
    # --- chain broken by one segment
    ("C12 broken: letter outside the set (qaf) second", WAW + FA + QAF + FA + ALIF + SIN + SU,
     [HH(0, 2, [112]), HH(2, 4, [28]), HM(4, 5, 11), HH(5, 7, [83])]),
    ("C13 broken: letter outside the set (qaf) first", QAF + FA + WAW + FA + ALIF + SIN + SU,
     [HH(0, 2, [28]), HH(2, 4, [112]), HM(4, 5, 11), HH(5, 7, [83])]),
    ("C14 broken: shadda+fatha on ba", WAW + FA + BA + SH + FA + ALIF + SIN + SU,
     [HH(0, 2, [112]), HH(2, 5, [107, 104]), HM(5, 6, 11), HH(6, 8, [83])]),
    ("C15 broken: sukun on ba", WAW + FA + BA + SU + ALIF + SIN + SU,
     [HH(0, 2, [112]), HH(2, 4, [107]), HM(4, 5, 11), HH(5, 7, [83])]),
    ("C16 broken: dammatan on ba", WAW + FA + BA + DAN + ALIF + SIN + SU,
     [HH(0, 2, [112]), P(2, 4, I11), HM(4, 5, 11), HH(5, 7, [83])]),
    ("C17 broken: fathatan on ba (R12 first) [amended-3: alifKhatt]", WAW + FA + BA + FAN + ALIF + SIN + SU,
     [HH(0, 2, [112]), P(2, 4, I11), AK(4, 5), HH(5, 7, [83])]),
    ("C18 broken: two marks (fatha+damma) on ba", WAW + FA + BA + FA + DA + ALIF + SIN + SU,
     [HH(0, 2, [112]), F(2, 5, I4), HM(5, 6, 11), HH(6, 8, [83])]),
    ("C19 broken: bare ba [amended-3: sukunMuqaddar]", WAW + FA + BA + ALIF + SIN + SU,
     [HH(0, 2, [112]), SM(2, 3, 107), HM(3, 4, 11), HH(4, 6, [83])]),
    ("C20 broken: bare waw first", WAW + BA + FA + ALIF + SIN + SU,
     [F(0, 1, MID), HH(1, 3, [104]), HM(3, 4, 11), HH(4, 6, [83])]),
    ("C21 hamza below alif is not the set's alif-hamza", A_HAMZA_BELOW + KA + ALIF + SIN + SU,
     [HH(0, 2, [2]), HM(2, 3, 11), HH(3, 5, [83])]),
    ("C22 bare hamza is not the set's alif-hamza", HAMZA + FA + ALIF + SIN + SU,
     [HH(0, 2, [0]), HM(2, 3, 11), HH(3, 5, [83])]),
    ("C23 broken: text-initial mark-headed segment", FA + WAW + FA + ALIF + SIN + SU,
     [F(0, 1, I2), HH(1, 3, [112]), HM(3, 4, 11), HH(4, 6, [83])]),
    ("C24 broken: tab inside the word", WAW + FA + TAB + BA + KA + ALIF + SIN + SU,
     [HH(0, 2, [112]), F(2, 3, I3), HH(3, 5, [106]), HM(5, 6, 11), HH(6, 8, [83])]),
    ("C25 space resets the chain: only the alif's own word counts",
     QAF + FA + SP + WAW + FA + ALIF + SIN + SU,
     [HH(0, 2, [28]), FS(2, 3), HH(3, 5, [112]), HW(5, 6), HH(6, 8, [83])]),
    # --- mid-word madd alif before a sukun letter
    ("C26 qaltu: madd alif before sukun lam is harfMadd", QAF + FA + ALIF + LAM + SU + TA + DA,
     [HH(0, 2, [28]), HM(2, 3, 11), HH(3, 5, [55]), HH(5, 7, [73])]),
    ("C27 namtu: madd alif before sukun mim is harfMadd", NUN + FA + ALIF + MIM + SU + TA + DA,
     [HH(0, 2, [56]), HM(2, 3, 11), HH(3, 5, [111]), HH(5, 7, [73])]),
    ("C28 qatalaas: long word, non-set letters", QAF + FA + TA + FA + LAM + FA + ALIF + SIN + SU,
     [HH(0, 2, [28]), HH(2, 4, [72]), HH(4, 6, [52]), HM(6, 7, 11), HH(7, 9, [83])]),
    ("C29 baat: shape-only reading, set letter before madd alif -> hamzaWasl (NOTES B4)",
     BA + FA + ALIF + TA + SU,
     [HH(0, 2, [104]), HW(2, 3), HH(3, 5, [75])]),
    # --- lam branch after a chain, and the rule-15 lam bullet
    ("C30 a-fa-bi-allahi: chain of three + lam branch; lam lamMudgham [amended-3]",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [HH(0, 2, [0]), HH(2, 4, [100]), HH(4, 6, [106]), HW(6, 7), LM(7, 8), HH(8, 11, [55, 52]),
      HH(11, 13, [6])]),
    ("C31 wa-bi-al-shams: chain of two + lam branch; lam lamMudgham [amended-3]",
     WAW + FA + BA + KA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [HH(0, 2, [112]), HH(2, 4, [106]), HW(4, 5), LM(5, 6), HH(6, 9, [43, 40]), HH(9, 11, [111]),
      HH(11, 13, [82])]),
    ("C32 qa-al-sha: alif not 14b (qaf), so lam is not lam-al -> sukunMuqaddar [amended-3]",
     QAF + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [28]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 7, [43, 40])]),
    ("C33 wa-bba-al-sha: chain broken by shadda, lam not lam-al -> sukunMuqaddar [amended-3]",
     WAW + FA + BA + SH + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [112]), HH(2, 5, [107, 104]), HM(5, 6, 11), SM(6, 7, 55), HH(7, 10, [43, 40])]),
    ("C34 ta-al-lam: alif not 14b (lam not followed by shadda), lam sukunMuqaddar [amended-3]",
     TA + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [72]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),
    # ================= amendment 3 (2026-10-29), hand-derived from spec.md.
    # Cells: ب 104..107, م 108..111, ت 72..75 (ة uses ت: 72+s), ن 56..59 (nun of tanwin 59),
    # ل 52..55, ق 28..31, ر 60..63, د 68..71, ض 48..51, ف 100..103, ك 32..35, ء/seats 0..3, ا 8..11.
    # --- rule 6: hamzaWaslAl
    ("D1 R6 alif + lam-sukun -> hamzaWaslAl", ALIF + LAM + SU + BA + FA,
     [WA(0, 1), HH(1, 3, [55]), HH(3, 5, [104])]),
    ("D2 R6 alif wasla + lam-sukun -> hamzaWaslAl", WASLA + LAM + SU + QAF + FA,
     [WA(0, 1), HH(1, 3, [55]), HH(3, 5, [28])]),
    ("D3 R6 alif + bare lam + shadda (nun) -> hamzaWaslAl, lamMudgham", ALIF + LAM + NUN + SH + FA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [59, 56])]),
    ("D4 R6 fails: lam with fatha -> P", ALIF + LAM + FA + BA + FA,
     [P(0, 1, WASL), HH(1, 3, [52]), HH(3, 5, [104])]),
    ("D5 R6 fails: no next in the word (lam in next word)", ALIF + SP + LAM + SU,
     [P(0, 1, WASL), FS(1, 2), HH(2, 4, [55])]),
    ("D6 R6 fails: next is not lam", ALIF + BA + SU, [P(0, 1, WASL), HH(1, 3, [107])]),
    ("D7 R6 fails: lam with shadda+fatha (neither sukun alone nor bare)", ALIF + LAM + SH + FA,
     [P(0, 1, WASL), HH(1, 4, [55, 52])]),
    ("D8 R6 fails: bare lam, after it no shadda; lam and ba sukunMuqaddar", ALIF + LAM + BA,
     [P(0, 1, WASL), SM(1, 2, 55), SM(2, 3, 107)]),
    ("D9 R6 fails: alif carries shadda (not bare)", ALIF + SH + LAM + SU,
     [P(0, 2, WASL), HH(2, 4, [55])]),
    # --- rule 8: madda
    ("D10 R8 bare madda awwal -> [0, 11]", MADDA + BA + SU, [MD(0, 1), HH(1, 3, [107])]),
    ("D11 R8 madda with fatha -> P", MADDA + FA, [P(0, 2, I8)]),
    ("D12 R8 bare madda mid-word -> madda", BA + FA + MADDA, [HH(0, 2, [104]), MD(2, 3)]),
    ("D13 R8 madda with shadda only -> P", MADDA + SH, [P(0, 2, I8)]),
    # --- rule 9: ta marbuta
    ("D14 R9 final ta marbuta fatha", BA + FA + TAM + FA, [HH(0, 2, [104]), TM(2, 4, [72])]),
    ("D15 R9 final ta marbuta damma", BA + FA + TAM + DA, [HH(0, 2, [104]), TM(2, 4, [73])]),
    ("D16 R9 final ta marbuta kasra", BA + FA + TAM + KA, [HH(0, 2, [104]), TM(2, 4, [74])]),
    ("D17 R9 final ta marbuta fathatan", BA + FA + TAM + FAN, [HH(0, 2, [104]), TM(2, 4, [72, 59])]),
    ("D18 R9 final ta marbuta kasratan", BA + FA + TAM + KAN, [HH(0, 2, [104]), TM(2, 4, [74, 59])]),
    ("D19 R9 bare final ta marbuta -> P", BA + FA + TAM, [HH(0, 2, [104]), P(2, 3, I9)]),
    ("D20 R9 non-final ta marbuta with fatha -> P", BA + FA + TAM + FA + BA + FA,
     [HH(0, 2, [104]), P(2, 4, I9), HH(4, 6, [104])]),
    ("D21 R9 final ta marbuta shadda+fatha (two marks) -> P", BA + FA + TAM + SH + FA,
     [HH(0, 2, [104]), P(2, 5, I9)]),
    ("D22 R9 ta marbuta akhir before a space", BA + FA + TAM + DA + SP + BA + FA,
     [HH(0, 2, [104]), TM(2, 4, [73]), FS(4, 5), HH(5, 7, [104])]),
    # --- rule 10: alif maqsura
    ("D23 R10 after fathatan -> alifKhatt; prev tanwin (only bare ى after)", BA + FAN + MAQ,
     [TN(0, 2, [104, 59]), AK(2, 3)]),
    ("D24 R10 after kasra -> P", BA + KA + MAQ, [HH(0, 2, [106]), P(2, 3, I10)]),
    ("D25 R10 prev shadda+fatha contains fatha -> alifMaqsura", BA + FA + MIM + SH + FA + MAQ,
     [HH(0, 2, [104]), HH(2, 5, [111, 108]), AM(5, 6)]),
    ("D26 R10 non-final -> P", BA + FA + MAQ + BA + FA, [HH(0, 2, [104]), P(2, 3, I10), HH(3, 5, [104])]),
    ("D27 R10 no prev (word of one) -> P", MAQ + SP, [P(0, 1, I10), FS(1, 2)]),
    ("D27b R10 prev is a mark-headed segment (no marks) -> P", FA + MAQ, [F(0, 1, I2), P(1, 2, I10)]),
    ("D28 R10 maqsura with fatha (not bare) -> P", BA + FA + MAQ + FA, [HH(0, 2, [104]), P(2, 4, I10)]),
    ("D29 R10 after bare letter -> P; that letter sukunMuqaddar", BA + FA + BA + MAQ,
     [HH(0, 2, [104]), SM(2, 3, 107), P(3, 4, I10)]),
    # --- rule 11: tanwin on carriers
    ("D30 R11 seat with dammatan", BA + FA + W_HAMZA + DAN, [HH(0, 2, [104]), TN(2, 4, [1, 59])]),
    ("D31 R11 shadda+dammatan not awwal -> three cells", BA + FA + MIM + SH + DAN,
     [HH(0, 2, [104]), TN(2, 5, [111, 109, 59])]),
    ("D32 R11 followed by another segment -> P", BA + DAN + BA + FA, [P(0, 2, I11), HH(2, 4, [104])]),
    ("D34 R11 head waw -> P", BA + FA + WAW + DAN, [HH(0, 2, [104]), P(2, 4, I11)]),
    ("D35 R11 head ya -> P", BA + FA + YA + KAN, [HH(0, 2, [104]), P(2, 4, I11)]),
    ("D36 R11 head alif with dammatan -> P", BA + FA + ALIF + DAN, [HH(0, 2, [104]), P(2, 4, I11)]),
    ("D37 R11 bare hamza with kasratan", BA + FA + HAMZA + KAN, [HH(0, 2, [104]), TN(2, 4, [2, 59])]),
    ("D38 R11 followed by alif with a mark -> P; alif R16", BA + FAN + ALIF + FA,
     [P(0, 2, I11), HH(2, 4, [8])]),
    ("D39 R11 followed by two bare alifs -> tanwin; alifKhatt then harfMadd", BA + FAN + ALIF + ALIF,
     [TN(0, 2, [104, 59]), AK(2, 3), HM(3, 4, 11)]),
    # --- rule 11: tanwinAlif
    ("D40 R11 alif + fathatan akhir -> tanwinAlif", BA + FA + ALIF + FAN, [HH(0, 2, [104]), TNA(2, 4)]),
    ("D41 R11 alif + fathatan not akhir -> P", BA + FA + ALIF + FAN + BA + FA,
     [HH(0, 2, [104]), P(2, 4, I11), HH(4, 6, [104])]),
    ("D42 R6 alif + fathatan awwal (second word) -> F", BA + FA + SP + ALIF + FAN,
     [HH(0, 2, [104]), FS(2, 3), F(3, 5, I6F)]),
    ("D43 R11 alif + shadda + fathatan akhir -> P", BA + FA + ALIF + SH + FAN,
     [HH(0, 2, [104]), P(2, 5, I11)]),
    # --- rule 12 alifKhatt after a seat with fathatan
    ("D44 R12 seat fathatan then alif", BA + FA + A_HAMZA_ABOVE + FAN + ALIF,
     [HH(0, 2, [104]), TN(2, 4, [0, 59]), AK(4, 5)]),
    # --- rule 14: shadda without vowel before final «اً»
    ("D46 R14 mim shadda before final alif-fathatan", BA + FA + MIM + SH + ALIF + FAN,
     [HH(0, 2, [104]), HT(2, 4, [111, 108]), TNA(4, 6)]),
    ("D47 R14 awwal shadda before final alif-fathatan (14 before 14a)", MIM + SH + ALIF + FAN,
     [HT(0, 2, [111, 108]), TNA(2, 4)]),
    ("D48 R14 seat shadda before final alif-fathatan", BA + FA + A_HAMZA_ABOVE + SH + ALIF + FAN,
     [HH(0, 2, [104]), HT(2, 4, [3, 0]), TNA(4, 6)]),
    ("D49 R14 alif-fathatan not akhir -> P", BA + FA + MIM + SH + ALIF + FAN + BA + FA,
     [HH(0, 2, [104]), P(2, 4, I14), P(4, 6, I11), HH(6, 8, [104])]),
    ("D50 R14 next alif with dammatan -> P", BA + FA + MIM + SH + ALIF + DAN,
     [HH(0, 2, [104]), P(2, 4, I14), P(4, 6, I11)]),
    # --- rule 14a: shaddaIbtida
    ("D52 R14a shadda+damma awwal", BA + SH + DA, [SI(0, 3, 105)]),
    ("D53 R14a shadda+kasra awwal", BA + SH + KA, [SI(0, 3, 106)]),
    ("D54 R14a seat hamza-below shadda+kasra", A_HAMZA_BELOW + SH + KA, [SI(0, 3, 2)]),
    # --- rule 15: lamMudgham
    ("D55 R15 lam before ra-shadda -> lamMudgham", ALIF + LAM + RA + SH + FA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [63, 60])]),
    ("D56 R15 lam before qaf-shadda (not of the 14) -> P", ALIF + LAM + QAF + SH + FA,
     [WA(0, 1), P(1, 2, LAMT), HH(2, 5, [31, 28])]),
    ("D57 R15 lam before ba-shadda (not of the 14) -> P", ALIF + LAM + BA + SH + FA,
     [WA(0, 1), P(1, 2, LAMT), HH(2, 5, [107, 104])]),
    ("D58 R15 lam after a 14b chain of two, before dal-shadda -> lamMudgham",
     FEH + FA + BA + KA + ALIF + LAM + DAL + SH + FA,
     [HH(0, 2, [100]), HH(2, 4, [106]), HW(4, 5), LM(5, 6), HH(6, 9, [71, 68])]),
    ("D59 R15 lam after a 14b chain, before qaf-shadda -> P", WAW + FA + ALIF + LAM + QAF + SH + FA,
     [HH(0, 2, [112]), HW(2, 3), P(3, 4, LAMT), HH(4, 7, [31, 28])]),
    ("D60 R15 alif wasla, lam before dad-shadda", WASLA + LAM + DAD + SH + FA,
     [WA(0, 1), LM(1, 2), HH(2, 5, [51, 48])]),
    # --- rule 15: harakaMinTanwin
    ("D61 R15 bare ta before final alif-fathatan", BA + FA + TA + ALIF + FAN,
     [HH(0, 2, [104]), HT(2, 3, [72]), TNA(3, 5)]),
    ("D62 R15 bare seat before final alif-fathatan", BA + FA + A_HAMZA_ABOVE + ALIF + FAN,
     [HH(0, 2, [104]), HT(2, 3, [0]), TNA(3, 5)]),
    ("D63 R15 awwal bare ba before alif-fathatan -> F", BA + ALIF + FAN, [F(0, 1, MID), TNA(1, 3)]),
    ("D69 R15 bare alif before alif-fathatan: harfMadd first", BA + FA + ALIF + ALIF + FAN,
     [HH(0, 2, [104]), HM(2, 3, 11), TNA(3, 5)]),
    ("D70 R15 lam after first alif, next alif-fathatan (no shadda) -> harakaMinTanwin",
     ALIF + LAM + ALIF + FAN, [P(0, 1, WASL), HT(1, 2, [52]), TNA(2, 4)]),
    # --- rule 15: sukunMuqaddar and awwal bare carriers
    ("D64 R15 mid-word bare mim", BA + FA + MIM + TA + FA,
     [HH(0, 2, [104]), SM(2, 3, 111), HH(3, 5, [72])]),
    ("D65 R15 word-final bare mim before a space", BA + FA + MIM + SP + BA + FA,
     [HH(0, 2, [104]), SM(2, 3, 111), FS(3, 4), HH(4, 6, [104])]),
    ("D66 R15 word-final bare ya-seat", BA + FA + Y_HAMZA, [HH(0, 2, [104]), SM(2, 3, 3)]),
    ("D67 R15 awwal bare ba alone before space -> P akhir", BA + SP, [P(0, 1, AKH), FS(1, 2)]),
    ("D68 R15 awwal bare ba not akhir -> F", BA + BA + FA, [F(0, 1, MID), HH(1, 3, [104])]),
]

KALIMAT_CASES = [
    ("empty", "", []),
    ("spaces only: no words", SP + SP, []),
    ("two words", BA + FA + SP + BA + DA,
     [(0, 2, True, [104]), (3, 5, True, [105])]),
    ("tatweel alone: all L but no cell", TAT, [(0, 1, False, [])]),
    ("al-shams [amended-3: all L now, licensed; hamzaWaslAl cell 0]",
     ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA, [(0, 9, True, [0, 43, 40, 111, 81])]),
    ("tatweel inside a licensed word", BA + FA + TAT + BA + FA, [(0, 5, True, [104, 104])]),
    ("tab does not split", BA + FA + TAB + BA + FA, [(0, 5, False, [104, 104])]),
    ("kataba", KAF + FA + TA + FA + BA + FA, [(0, 6, True, [32, 72, 104])]),
    ("leading/trailing spaces", SP + BA + FA + SP, [(1, 3, True, [104])]),
    # ================= amendment 1 (hand-derived)
    ("K1 wa-al-ardi fully licensed, no cell for the alif",
     WAW + FA + ALIF + LAM + SU + A_HAMZA_ABOVE + FA + RA + SU + DAD + KA,
     [(0, 11, True, [112, 55, 0, 63, 50])]),
    ("K2 wa-ista licensed", WAW + FA + ALIF + SIN + SU + TA + FA, [(0, 7, True, [112, 83, 72])]),
    ("K3 wa-al-shams [amended-3: lam lamMudgham, licensed]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [(0, 11, True, [112, 43, 40, 111, 82])]),
    ("K4 minna with word-initial shadda [amended-3: shaddaIbtida, licensed]", MIM + SH + KA + NUN + FA,
     [(0, 5, True, [110, 56])]),
    ("K5 second word with initial shadda [amended-3]", BA + FA + SP + MIM + SH + KA + NUN + FA,
     [(0, 2, True, [104]), (3, 8, True, [110, 56])]),
    ("K6 bi-ismi licensed", BA + KA + ALIF + SIN + SU + MIM + KA, [(0, 7, True, [106, 83, 110])]),
    ("K7 qala: harfMadd alif keeps its cell", QAF + FA + ALIF + LAM + FA, [(0, 5, True, [28, 11, 52])]),
    ("K8 bi-allahi [amended-3: licensed]", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 9, True, [106, 55, 52, 6])]),
    ("K9 wa-istaghfir licensed", WAW + FA + ALIF + SIN + SU + TA + FA + GHAIN + SU + FEH + KA + RA + SU,
     [(0, 13, True, [112, 83, 72, 23, 102, 63])]),
    ("K10 non-initial shadda licensed", BA + FA + MIM + SH + FA, [(0, 5, True, [104, 111, 108])]),
    # ================= amendment 2 (hand-derived)
    ("K11 qaltu licensed, madd alif keeps its cell", QAF + FA + ALIF + LAM + SU + TA + DA,
     [(0, 7, True, [28, 11, 55, 73])]),
    ("K12 a-fa-sta licensed, chain of two, no cell for the alif",
     A_HAMZA_ABOVE + FA + FEH + FA + ALIF + SIN + SU + TA + FA,
     [(0, 9, True, [0, 100, 83, 72])]),
    ("K13 wa-bba-as licensed: chain broken by shadda, alif harfMadd",
     WAW + FA + BA + SH + FA + ALIF + SIN + SU,
     [(0, 8, True, [112, 107, 104, 11, 83])]),
    ("K14 a-fa-bi-allahi [amended-3: licensed]",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 13, True, [0, 100, 106, 55, 52, 6])]),
    ("K15 wa-b-dammatan-as not licensed (tanwin P)", WAW + FA + BA + DAN + ALIF + SIN + SU,
     [(0, 7, False, [112, 11, 83])]),
    # ================= amendment 3 (hand-derived)
    ("K16 al-qamar licensed", ALIF + LAM + SU + QAF + FA + MIM + FA + RA + DA,
     [(0, 9, True, [0, 55, 28, 108, 61])]),
    ("K17 ba + final ta marbuta dammatan licensed", BA + FA + TAM + DAN, [(0, 4, True, [104, 73, 59])]),
    ("K18 bare ta before alif-fathatan licensed", BA + FA + TA + ALIF + FAN,
     [(0, 5, True, [104, 72, 59])]),
    ("K19 madda word licensed", MADDA + MIM + FA + NUN + FA, [(0, 5, True, [0, 11, 108, 56])]),
    ("K20 lam before qaf-shadda: not licensed", ALIF + LAM + QAF + SH + FA, [(0, 5, False, [0, 31, 28])]),
    ("K21 tanwin + alifKhatt licensed", BA + FAN + ALIF, [(0, 3, True, [104, 59])]),
    ("K22 dal-fathatan + alif maqsura (alifKhatt) licensed", BA + DA + DAL + FAN + MAQ,
     [(0, 5, True, [105, 68, 59])]),
    ("K23 final bare mim licensed", BA + FA + MIM, [(0, 3, True, [104, 111])]),
    ("K24 'al' alone not licensed (alif P)", ALIF + LAM, [(0, 2, False, [55])]),
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
