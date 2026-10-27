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


def L(a, b, sinf, cells=()):
    return ("L", a, b, sinf, "", list(cells))


def HH(a, b, cells):
    return L(a, b, "harfHaraka", cells)


def HM(a, b, cell):
    return L(a, b, "harfMadd", [cell])


def FS(a, b):
    return L(a, b, "fasil")


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
    ("R15 lam after alif that is not the first segment (wa-al-shams)",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [HH(0, 2, [112]), HM(2, 3, 11), F(3, 4, MID), HH(4, 7, [43, 40]), HH(7, 9, [111]), HH(9, 11, [81])]),
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
    ("R16 hamza seat with shadda+fatha", A_HAMZA_ABOVE + SH + FA, [HH(0, 3, [3, 0])]),
    ("R16 fatha before shadda", BA + FA + SH, [HH(0, 3, [107, 104])]),
    ("R16 shadda before fatha", BA + SH + FA, [HH(0, 3, [107, 104])]),
    ("R16 shadda + sukun", BA + SH + SU, [HH(0, 3, [107, 107])]),
    ("R16 ya awwal with shadda+kasra", YA + SH + KA, [HH(0, 3, [47, 46])]),
    ("R16 alif with fatha mid-word", BA + FA + ALIF + FA, [HH(0, 2, [104]), HH(2, 4, [8])]),
    ("R16 alif with sukun mid-word", BA + FA + ALIF + SU, [HH(0, 2, [104]), HH(2, 4, [11])]),
    ("multiple spaces between words", BA + FA + SP + SP + BA + FA,
     [HH(0, 2, [104]), FS(2, 3), FS(3, 4), HH(4, 6, [104])]),
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
