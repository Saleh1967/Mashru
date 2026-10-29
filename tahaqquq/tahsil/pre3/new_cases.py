import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
seg_anchor = '''     [HH(0, 2, [72]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),
]
'''
kal_anchor = '''     [(0, 7, False, [112, 11, 83])]),
]
'''
assert s.count(seg_anchor) == 1 and s.count(kal_anchor) == 1
new_seg = '''     [HH(0, 2, [72]), HM(2, 3, 11), SM(3, 4, 55), HH(4, 6, [32])]),
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
'''
new_kal = '''     [(0, 7, False, [112, 11, 83])]),
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
'''
s = s.replace(seg_anchor, new_seg).replace(kal_anchor, new_kal)
s = s.replace('''FEH, DAD, GHAIN = "ف", "ض", "غ"   # ف ض غ
''', '''FEH, DAD, GHAIN = "ف", "ض", "غ"   # ف ض غ
# ---- amendment 3
DAL = "\\u062f"   # د
''')
assert 'DAL = ' in s
open(p, "w", encoding="utf-8").write(s)
