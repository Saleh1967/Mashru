# hand-written replacements of existing expectations under amendment 3 (one per changed case)
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
R = [
# helpers
('''def P(a, b, ism):''', '''# ---- amendment 3 (2026-10-29) sinf helpers
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


def P(a, b, ism):'''),
('''    ("R8 madda alif alone", MADDA, [P(0, 1, I8)]),''',
 '''    ("R8 madda alif alone [amended-3: bare madda]", MADDA, [MD(0, 1)]),'''),
('''    ("R9 ta marbuta with dammatan (9 before 11)", BA + FA + TAM + DAN, [HH(0, 2, [104]), P(2, 4, I9)]),''',
 '''    ("R9 ta marbuta with dammatan (9 before 11) [amended-3: akhir, one tanwin]", BA + FA + TAM + DAN,
     [HH(0, 2, [104]), TM(2, 4, [73, 59])]),'''),
('''    ("R10 alif maqsura after ba", BA + FA + MAQ, [HH(0, 2, [104]), P(2, 3, I10)]),''',
 '''    ("R10 alif maqsura after ba [amended-3: after fatha]", BA + FA + MAQ, [HH(0, 2, [104]), AM(2, 3)]),'''),
('''    ("R11 dammatan", BA + DAN, [P(0, 2, I11)]),''',
 '''    ("R11 dammatan [amended-3: tanwin, nothing after]", BA + DAN, [TN(0, 2, [105, 59])]),'''),
('''    ("R12 fathatan then alif", BA + FAN + ALIF, [P(0, 2, I11), P(2, 3, I12)]),
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
    ("R13 word-initial waw then alif", WAW + ALIF, [F(0, 1, MID), P(1, 2, I13)]),''',
 '''    ("R12 fathatan then alif [amended-3: tanwin + alifKhatt]", BA + FAN + ALIF, [TN(0, 2, [104, 59]), AK(2, 3)]),
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
    ("R13 word-initial waw then alif [amended-3]", WAW + ALIF, [F(0, 1, MID), AK(1, 2)]),'''),
('''    ("R13 contrast: alif not akhir", BA + DA + WAW + ALIF + BA,
     [HH(0, 2, [105]), HM(2, 3, 115), HM(3, 4, 11), P(4, 5, AKH)]),''',
 '''    ("R13 contrast: alif not akhir [amended-3: final ba sukunMuqaddar]", BA + DA + WAW + ALIF + BA,
     [HH(0, 2, [105]), HM(2, 3, 115), HM(3, 4, 11), SM(4, 5, 107)]),'''),
('''    ("R15 al-shams", ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
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
     [HH(0, 2, [104]), F(2, 3, MID), HH(3, 6, [43, 40])]),''',
 '''    ("R15 al-shams [amended-3: hamzaWaslAl + lamMudgham]", ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
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
     [HH(0, 2, [104]), SM(2, 3, 55), HH(3, 6, [43, 40])]),'''),
('''    ("R15 lam after alif that is not the first segment (wa-al-shams) [amended: R14b + widened R15]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [HH(0, 2, [112]), HW(2, 3), P(3, 4, LAMT),''',
 '''    ("R15 lam after alif that is not the first segment (wa-al-shams) [amended: R14b + widened R15] [amended-3]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA,
     [HH(0, 2, [112]), HW(2, 3), LM(3, 4),'''),
('''    ("R15 bare final letter", BA + FA + BA, [HH(0, 2, [104]), P(2, 3, AKH)]),
    ("R15 bare middle letter", BA + FA + BA + BA + FA, [HH(0, 2, [104]), F(2, 3, MID), HH(3, 5, [104])]),''',
 '''    ("R15 bare final letter [amended-3: sukunMuqaddar]", BA + FA + BA, [HH(0, 2, [104]), SM(2, 3, 107)]),
    ("R15 bare middle letter [amended-3: sukunMuqaddar]", BA + FA + BA + BA + FA,
     [HH(0, 2, [104]), SM(2, 3, 107), HH(3, 5, [104])]),'''),
('''    ("R15 bare hamza seat mid-word", BA + FA + A_HAMZA_ABOVE + BA + FA,
     [HH(0, 2, [104]), F(2, 3, MID), HH(3, 5, [104])]),
    ("R15 bare final hamza", BA + FA + HAMZA, [HH(0, 2, [104]), P(2, 3, AKH)]),''',
 '''    ("R15 bare hamza seat mid-word [amended-3: sukunMuqaddar]", BA + FA + A_HAMZA_ABOVE + BA + FA,
     [HH(0, 2, [104]), SM(2, 3, 3), HH(3, 5, [104])]),
    ("R15 bare final hamza [amended-3: sukunMuqaddar]", BA + FA + HAMZA, [HH(0, 2, [104]), SM(2, 3, 3)]),'''),
('''    ("R14a hamza seat awwal with shadda+fatha [amended, was R16]", A_HAMZA_ABOVE + SH + FA, [P(0, 3, I14A)]),
    ("R14a fatha before shadda, awwal [amended, was R16]", BA + FA + SH, [P(0, 3, I14A)]),
    ("R14a shadda before fatha, awwal [amended, was R16]", BA + SH + FA, [P(0, 3, I14A)]),''',
 '''    ("R14a hamza seat awwal with shadda+fatha [amended, was R16] [amended-3: shaddaIbtida]",
     A_HAMZA_ABOVE + SH + FA, [SI(0, 3, 0)]),
    ("R14a fatha before shadda, awwal [amended, was R16] [amended-3]", BA + FA + SH, [SI(0, 3, 104)]),
    ("R14a shadda before fatha, awwal [amended, was R16] [amended-3]", BA + SH + FA, [SI(0, 3, 104)]),'''),
('''    ("R14a ya awwal with shadda+kasra [amended, was R16]", YA + SH + KA, [P(0, 3, I14A)]),''',
 '''    ("R14a ya awwal with shadda+kasra [amended, was R16] [amended-3]", YA + SH + KA, [SI(0, 3, 46)]),'''),
('''     [HH(0, 2, [106]), HW(2, 3), P(3, 4, LAMT), HH(4, 7, [55, 52]), HH(7, 9, [6])]),
    ("A8 R14b+R15 lam branch, after-lam has shadda only (R14)", WAW + FA + ALIF + LAM + SHIN + SH,
     [HH(0, 2, [112]), HW(2, 3), P(3, 4, LAMT), P(4, 6, I14)]),
    ("A9 bare lam, after it no shadda: alif harfMadd, lam F", WAW + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), F(3, 4, MID), HH(4, 6, [32])]),
    ("A10 bare lam at word end: alif harfMadd, lam akhir", WAW + FA + ALIF + LAM,
     [HH(0, 2, [112]), HM(2, 3, 11), P(3, 4, AKH)]),
    ("A11 shadda two segments after the lam does not count (immediate reading)",
     WAW + FA + ALIF + LAM + KAF + FA + TA + SH + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), F(3, 4, MID), HH(4, 6, [32]), HH(6, 9, [75, 72])]),''',
 '''     [HH(0, 2, [106]), HW(2, 3), LM(3, 4), HH(4, 7, [55, 52]), HH(7, 9, [6])]),
    ("A8 R14b+R15 lam branch, after-lam has shadda only (R14) [amended-3]", WAW + FA + ALIF + LAM + SHIN + SH,
     [HH(0, 2, [112]), HW(2, 3), LM(3, 4), P(4, 6, I14)]),
    ("A9 bare lam, after it no shadda: alif harfMadd, lam sukunMuqaddar [amended-3]",
     WAW + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),
    ("A10 bare lam at word end: alif harfMadd, lam sukunMuqaddar [amended-3]", WAW + FA + ALIF + LAM,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55)]),
    ("A11 shadda two segments after the lam does not count (immediate reading) [amended-3]",
     WAW + FA + ALIF + LAM + KAF + FA + TA + SH + FA,
     [HH(0, 2, [112]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32]), HH(6, 9, [75, 72])]),'''),
('''    ("A7 R14b+R15 bi-allahi (lam, lam+shadda)",''', '''    ("A7 R14b+R15 bi-allahi (lam, lam+shadda) [amended-3: lamMudgham]",'''),
('''    ("A16 prev with fathatan: R12 first", BA + FAN + ALIF + SIN + SU,
     [P(0, 2, I11), P(2, 3, I12), HH(3, 5, [83])]),''',
 '''    ("A16 prev with fathatan: R12 first [amended-3: alifKhatt]", BA + FAN + ALIF + SIN + SU,
     [P(0, 2, I11), AK(2, 3), HH(3, 5, [83])]),'''),
('''    ("A30 prev is R14a (shadda+kasra awwal): two marks break the chain [amended-2]",
     BA + SH + KA + ALIF + SIN + SU,
     [P(0, 3, I14A),''',
 '''    ("A30 prev is R14a (shadda+kasra awwal): two marks break the chain [amended-2] [amended-3]",
     BA + SH + KA + ALIF + SIN + SU,
     [SI(0, 3, 106),'''),
('''    ("A32 R12 pre-empts 14b, so the lam is not R15 lam-al (NOTES A7)",
     BA + FAN + FA + ALIF + LAM + SHIN + SH + FA,
     [F(0, 3, I4), P(3, 4, I12), F(4, 5, MID), HH(5, 8, [43, 40])]),''',
 '''    ("A32 R12 pre-empts 14b, so the lam is not R15 lam-al (NOTES A7) [amended-3]",
     BA + FAN + FA + ALIF + LAM + SHIN + SH + FA,
     [F(0, 3, I4), AK(3, 4), SM(4, 5, 55), HH(5, 8, [43, 40])]),'''),
('''    ("B1 R14a mim shadda+kasra awwal", MIM + SH + KA + NUN + FA,
     [P(0, 3, I14A), HH(3, 5, [56])]),''',
 '''    ("B1 R14a mim shadda+kasra awwal [amended-3]", MIM + SH + KA + NUN + FA,
     [SI(0, 3, 110), HH(3, 5, [56])]),'''),
('''    ("B3 R14a hamza-on-waw seat shadda+damma awwal", W_HAMZA + SH + DA + BA + FA,
     [P(0, 3, I14A), HH(3, 5, [104])]),
    ("B4 R14a bare hamza shadda+fatha", HAMZA + SH + FA, [P(0, 3, I14A)]),''',
 '''    ("B3 R14a hamza-on-waw seat shadda+damma awwal [amended-3]", W_HAMZA + SH + DA + BA + FA,
     [SI(0, 3, 1), HH(3, 5, [104])]),
    ("B4 R14a bare hamza shadda+fatha [amended-3]", HAMZA + SH + FA, [SI(0, 3, 0)]),'''),
('''    ("B6 R14a in second word", BA + FA + SP + MIM + SH + FA,
     [HH(0, 2, [104]), FS(2, 3), P(3, 6, I14A)]),''',
 '''    ("B6 R14a in second word [amended-3]", BA + FA + SP + MIM + SH + FA,
     [HH(0, 2, [104]), FS(2, 3), SI(3, 6, 108)]),'''),
('''    ("B15 after a space carrying a mark: awwal", BA + FA + SP + FA + MIM + SH + FA,
     [HH(0, 2, [104]), F(2, 4, I1), P(4, 7, I14A)]),
    ("B16 waw awwal shadda+fatha", WAW + SH + FA, [P(0, 3, I14A)]),''',
 '''    ("B15 after a space carrying a mark: awwal [amended-3]", BA + FA + SP + FA + MIM + SH + FA,
     [HH(0, 2, [104]), F(2, 4, I1), SI(4, 7, 108)]),
    ("B16 waw awwal shadda+fatha [amended-3]", WAW + SH + FA, [SI(0, 3, 112)]),'''),
('''    ("C17 broken: fathatan on ba (R12 first)", WAW + FA + BA + FAN + ALIF + SIN + SU,
     [HH(0, 2, [112]), P(2, 4, I11), P(4, 5, I12), HH(5, 7, [83])]),''',
 '''    ("C17 broken: fathatan on ba (R12 first) [amended-3: alifKhatt]", WAW + FA + BA + FAN + ALIF + SIN + SU,
     [HH(0, 2, [112]), P(2, 4, I11), AK(4, 5), HH(5, 7, [83])]),'''),
('''    ("C19 broken: bare ba", WAW + FA + BA + ALIF + SIN + SU,
     [HH(0, 2, [112]), F(2, 3, MID), HM(3, 4, 11), HH(4, 6, [83])]),''',
 '''    ("C19 broken: bare ba [amended-3: sukunMuqaddar]", WAW + FA + BA + ALIF + SIN + SU,
     [HH(0, 2, [112]), SM(2, 3, 107), HM(3, 4, 11), HH(4, 6, [83])]),'''),
('''    ("C30 a-fa-bi-allahi: chain of three + lam branch; lam R15 lam-al",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [HH(0, 2, [0]), HH(2, 4, [100]), HH(4, 6, [106]), HW(6, 7), P(7, 8, LAMT),''',
 '''    ("C30 a-fa-bi-allahi: chain of three + lam branch; lam lamMudgham [amended-3]",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [HH(0, 2, [0]), HH(2, 4, [100]), HH(4, 6, [106]), HW(6, 7), LM(7, 8),'''),
('''    ("C31 wa-bi-al-shams: chain of two + lam branch; lam R15 lam-al",
     WAW + FA + BA + KA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [HH(0, 2, [112]), HH(2, 4, [106]), HW(4, 5), P(5, 6, LAMT),''',
 '''    ("C31 wa-bi-al-shams: chain of two + lam branch; lam lamMudgham [amended-3]",
     WAW + FA + BA + KA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [HH(0, 2, [112]), HH(2, 4, [106]), HW(4, 5), LM(5, 6),'''),
('''    ("C32 qa-al-sha: alif not 14b (qaf), so lam is not lam-al -> F",
     QAF + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [28]), HM(2, 3, 11), F(3, 4, MID), HH(4, 7, [43, 40])]),
    ("C33 wa-bba-al-sha: chain broken by shadda, lam not lam-al -> F",
     WAW + FA + BA + SH + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [112]), HH(2, 5, [107, 104]), HM(5, 6, 11), F(6, 7, MID), HH(7, 10, [43, 40])]),
    ("C34 ta-al-lam: alif not 14b (lam not followed by shadda), lam F",
     TA + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [72]), HM(2, 3, 11), F(3, 4, MID), HH(4, 6, [32])]),''',
 '''    ("C32 qa-al-sha: alif not 14b (qaf), so lam is not lam-al -> sukunMuqaddar [amended-3]",
     QAF + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [28]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 7, [43, 40])]),
    ("C33 wa-bba-al-sha: chain broken by shadda, lam not lam-al -> sukunMuqaddar [amended-3]",
     WAW + FA + BA + SH + FA + ALIF + LAM + SHIN + SH + FA,
     [HH(0, 2, [112]), HH(2, 5, [107, 104]), HM(5, 6, 11), SM(6, 7, 55), HH(7, 10, [43, 40])]),
    ("C34 ta-al-lam: alif not 14b (lam not followed by shadda), lam sukunMuqaddar [amended-3]",
     TA + FA + ALIF + LAM + KAF + FA,
     [HH(0, 2, [72]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),'''),
# kalimat
('''    ("al-shams: P segments -> not licensed; cells still concatenated",
     ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA, [(0, 9, False, [43, 40, 111, 81])]),''',
 '''    ("al-shams [amended-3: all L now, licensed; hamzaWaslAl cell 0]",
     ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + DA, [(0, 9, True, [0, 43, 40, 111, 81])]),'''),
('''    ("K3 wa-al-shams not licensed (lam P)", WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [(0, 11, False, [112, 43, 40, 111, 82])]),
    ("K4 minna with word-initial shadda not licensed", MIM + SH + KA + NUN + FA, [(0, 5, False, [56])]),
    ("K5 second word with initial shadda", BA + FA + SP + MIM + SH + KA + NUN + FA,
     [(0, 2, True, [104]), (3, 8, False, [56])]),''',
 '''    ("K3 wa-al-shams [amended-3: lam lamMudgham, licensed]",
     WAW + FA + ALIF + LAM + SHIN + SH + FA + MIM + SU + SIN + KA,
     [(0, 11, True, [112, 43, 40, 111, 82])]),
    ("K4 minna with word-initial shadda [amended-3: shaddaIbtida, licensed]", MIM + SH + KA + NUN + FA,
     [(0, 5, True, [110, 56])]),
    ("K5 second word with initial shadda [amended-3]", BA + FA + SP + MIM + SH + KA + NUN + FA,
     [(0, 2, True, [104]), (3, 8, True, [110, 56])]),'''),
('''    ("K8 bi-allahi not licensed", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 9, False, [106, 55, 52, 6])]),''',
 '''    ("K8 bi-allahi [amended-3: licensed]", BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 9, True, [106, 55, 52, 6])]),'''),
('''    ("K14 a-fa-bi-allahi not licensed (lam P)",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 13, False, [0, 100, 106, 55, 52, 6])]),''',
 '''    ("K14 a-fa-bi-allahi [amended-3: licensed]",
     A_HAMZA_ABOVE + FA + FEH + FA + BA + KA + ALIF + LAM + LAM + SH + FA + HA + KA,
     [(0, 13, True, [0, 100, 106, 55, 52, 6])]),'''),
]
for old, new in R:
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
print(len(R), "replacements")
