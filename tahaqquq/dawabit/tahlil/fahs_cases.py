# -*- coding: utf-8 -*-
# فاحصُ ملفّ الحالات قبل التجميد (على wasf.md).
# الاستعمال: python3 -I fahs_cases.py <cases.json> <qatr.txt>
# يخرج 0 إن مرّ كلُّ فحص، و1 مع قائمة الأخطاء إن لم يمرّ.
import hashlib, json, re, sys
from collections import Counter

BASMA_MASDAR = '2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d'
NITAQ = set()
for a, b in [(53, 67), (75, 78), (82, 85), (88, 90), (96, 100), (110, 114), (123, 126),
             (152, 158), (219, 224), (267, 268), (337, 343)]:
    NITAQ.update(range(a, b + 1))

FIAT = ['موجب', 'حد', 'خارج', 'عموم', 'غموض']
HUKM = ['مقبول', 'خطأ', 'لا_حكم']
ADWAR = ['رابط', 'جازم', 'ناصب', 'نافية', 'فعل', 'فاعل', 'مفعول_به', 'مبتدأ', 'خبر',
         'حرف_جر', 'مجرور', 'مضاف_إليه']
HADD_FIA = {'موجب': 15, 'حد': 12, 'خارج': 5, 'عموم': 6, 'غموض': 2}
KEYS = ['id', 'fia', 'nass', 'mithal_harfi', 'adwar', 'hukm', 'zawj', 'sanad', 'taliq']

FATHA, DAMMA, KASRA, SUKUN, SHADDA = 'َ', 'ُ', 'ِ', 'ْ', 'ّ'
TANWIN = 'ًٌٍ'
HARAKAT = FATHA + DAMMA + KASRA + SUKUN + TANWIN
MARKS = HARAKAT + SHADDA
LETTERS = set(chr(c) for c in range(0x0621, 0x063B)) | set(chr(c) for c in range(0x0641, 0x064B))
ALIF, ALIF_MAQSURA, WAW, YA = 'ا', 'ى', 'و', 'ي'
SHAMSI = set('تثدذرزسشصضطظلن')
DAMAIR = ['هُمَا', 'كُمَا', 'هُمْ', 'هِمْ', 'كُمْ', 'هَا', 'نَا', 'نِي', 'هُ', 'هِ', 'كَ', 'كِ', 'ي', 'يَ']
HURUF_JARR_KALIMA = ['مِنْ', 'إِلَى', 'عَنْ', 'عَلَى', 'فِي']
ASMA_ADWAR = {'فاعل', 'مفعول_به', 'مبتدأ', 'خبر', 'مجرور', 'مضاف_إليه'}

errs = []
def err(m):
    errs.append(m)

def bila(s):
    return ''.join(ch for ch in s if ch not in MARKS)

# ---------- الكتابة ----------
def fahs_kitaba(cid, s):
    if not s or s != s.strip() or '  ' in s:
        err('%s: مسافاتٌ غيرُ مفردة أو في الطرفين' % cid)
    for ch in s:
        if ch != ' ' and ch not in LETTERS and ch not in MARKS:
            err('%s: حرفٌ غيرُ مسموح %r' % (cid, ch))
    words = s.split(' ')
    if len(words) > 6:
        err('%s: أكثرُ من ستّ كلمات' % cid)
    for w in words:
        if not w:
            continue
        if w[0] in MARKS:
            err('%s: كلمةٌ تبدأ بعلامة %r' % (cid, w)); continue
        # عناقيد: حرفٌ وما بعده من العلامات (والشدّةُ قبل حركتها أو بعدها)
        cl = []
        for ch in w:
            if ch in MARKS:
                cl[-1][1].append(ch)
            else:
                cl.append([ch, []])
        n = len(cl)
        for i, (ch, mk) in enumerate(cl):
            prev = cl[i - 1] if i else None
            nxt = cl[i + 1] if i + 1 < n else None
            if mk:
                if ch in (ALIF, ALIF_MAQSURA):
                    err('%s: علامةٌ على ألفٍ مجرّدة في %r' % (cid, w))
                har = [m for m in mk if m != SHADDA]
                sh = [m for m in mk if m == SHADDA]
                if len(har) != 1 or len(sh) > 1:
                    err('%s: علاماتٌ على غير الشرط في %r' % (cid, w))
                elif sh and har[0] == SUKUN:
                    err('%s: شدّةٌ مع سكون في %r' % (cid, w))
                if har and har[0] == 'ً':
                    if not (nxt is not None and nxt[0] == ALIF and not nxt[1] and i + 2 == n):
                        err('%s: تنوينُ النصب بلا ألفٍ بعده آخرَ الكلمة في %r' % (cid, w))
                elif har and har[0] in 'ٌٍ' and i + 1 != n:
                    err('%s: تنوينٌ في غير آخر الكلمة %r' % (cid, w))
                continue
            if ch in (ALIF, ALIF_MAQSURA):
                continue
            if ch == WAW and prev is not None and prev[1] == [DAMMA]:
                continue
            if ch == YA and prev is not None and prev[1] == [KASRA]:
                continue
            # لامُ التعريف بلا علامة قبل الحرف الشمسيّ المشدّد
            if (ch == 'ل' and prev is not None and prev[0] == ALIF and not prev[1]
                    and nxt is not None and nxt[0] in SHAMSI and SHADDA in nxt[1]):
                continue
            err('%s: حرفٌ بلا حركةٍ ولا سكون %r في %r' % (cid, ch, w))
        ch, mk = cl[-1]
        if mk or ch in (ALIF, ALIF_MAQSURA):
            pass
        elif ch == WAW and n > 1 and cl[-2][1] == [DAMMA]:
            pass
        elif ch == YA and n > 1 and cl[-2][1] == [KASRA]:
            pass
        else:
            err('%s: آخرُ الكلمة بلا علامةٍ ولا حرفِ مدّ %r' % (cid, w))
        # الألفُ بعد الفتحتين، وألفُ واو الجماعة: لا ألفَ مجرّدة آخرَ الفعل بعد واوٍ بلا ضمّةٍ قبلها
    return words

# ---------- الأشكال ----------
def pp(seq, i):
    if i + 1 < len(seq) and seq[i] == 'حرف_جر' and seq[i + 1] == 'مجرور':
        i += 2
        if i < len(seq) and seq[i] == 'مضاف_إليه':
            i += 1
        return i
    return None

def ism(seq, i, dawr):
    if i < len(seq) and seq[i] == dawr:
        i += 1
        if i < len(seq) and seq[i] == 'مضاف_إليه':
            i += 1
        return i
    return None

def fiiliyya(seq):
    i = 0
    if i < len(seq) and seq[i] in ('جازم', 'ناصب', 'نافية'):
        i += 1
    if i >= len(seq) or seq[i] != 'فعل':
        return False
    i += 1
    fa = mf = 0
    while i < len(seq):
        j = pp(seq, i)
        if j is not None:
            i = j; continue
        j = ism(seq, i, 'فاعل')
        if j is not None and fa == 0:
            fa = 1; i = j; continue
        j = ism(seq, i, 'مفعول_به')
        if j is not None and mf == 0:
            mf = 1; i = j; continue
        return False
    return True

def ismiyya(seq):
    i = ism(seq, 0, 'مبتدأ')
    if i is None:
        return None
    j = pp(seq, i)
    if j is not None and j == len(seq):
        return 'شبه'
    if j is not None:
        i = j
    k = ism(seq, i, 'خبر')
    if k is not None and k == len(seq):
        return 'اسمية'
    return None

def shakl(seq):
    if any(r not in ADWAR for r in seq):
        return None
    if 'رابط' in seq[1:]:
        return None
    s = seq[1:] if seq and seq[0] == 'رابط' else seq
    if fiiliyya(s):
        return 'فعلية'
    return ismiyya(s)

# ---------- التقطيع (لعدّ الخصائص) ----------
def taqti(words, seq):
    """يحاذي الكلماتِ بالأدوار: يُرجع قائمةً لكلّ كلمة من (نوع الوحدة، الدور، النصّ) أو None."""
    def khiyarat(wi, w):
        res = []
        pre_opts = [[]]
        if wi == 0:
            for r in ('وَ', 'فَ'):
                if w.startswith(r) and len(w) > 2:
                    pre_opts.append([('rabit', r)])
        out = []
        for pre in pre_opts:
            rest = w[sum(len(p[1]) for p in pre):]
            # لامُ الأمر
            lam_opts = [[]]
            if pre and rest.startswith('لْ') and len(rest) > 2:
                lam_opts.append([('lam', 'لْ')])
            if not pre and wi == 0 and rest.startswith('لِ') and len(rest) > 2 and rest[2] in 'يتنأ':
                lam_opts.append([('lam', 'لِ')])
            for lam in lam_opts:
                rest2 = rest[sum(len(p[1]) for p in lam):]
                jar_opts = [[]]
                for j in ('بِ', 'لِ', 'كَ'):
                    if rest2.startswith(j) and not lam and len(rest2) > 2:
                        jar_opts.append([('jar', j)])
                for jar in jar_opts:
                    core = rest2[sum(len(p[1]) for p in jar):]
                    # بلا ضمير
                    if core:
                        out.append(pre + lam + jar + [('core', core)])
                    for d in DAMAIR:
                        if core.endswith(d):
                            c2 = core[:-len(d)]
                            if c2 or jar:
                                out.append(pre + lam + jar + ([('core', c2)] if c2 else []) + [('damir', d)])
        return out

    def awfaq(units, roles):
        for (k, t), r in zip(units, roles):
            if k == 'rabit' and r != 'رابط': return False
            if k == 'lam' and r != 'جازم': return False
            if k == 'jar' and r != 'حرف_جر': return False
            if k == 'damir' and r not in ('مفعول_به', 'مضاف_إليه', 'مجرور'): return False
            if k == 'core' and r in ('رابط',): return False
            if k == 'core' and r == 'حرف_جر' and t not in HURUF_JARR_KALIMA: return False
        return True

    sols = []
    def dp(wi, ri, acc):
        if wi == len(words):
            if ri == len(seq):
                sols.append(list(acc))
            return
        for units in khiyarat(wi, words[wi]):
            m = len(units)
            if ri + m <= len(seq) and awfaq(units, seq[ri:ri + m]):
                acc.append([(u[0], seq[ri + x], u[1]) for x, u in enumerate(units)])
                dp(wi + 1, ri + m, acc)
                acc.pop()
    dp(0, 0, [])
    if not sols:
        return None
    # الأقلُّ تقطيعًا للنواة (يمنع تقطيع كلمةٍ كاملةٍ حرفَ جرٍّ وبقيّة)
    sols.sort(key=lambda s: sum(1 for w in s for u in w if u[0] != 'core'))
    return sols[0]

RAF_DAMAIR = ['ْتُ', 'ْتَ', 'ْتِ', 'ْتُمْ', 'ْتُمَا', 'ْنَا', 'ُوا', 'ْنَ', 'َا', 'ِي', 'َانِ', 'ُونَ', 'ِينَ']
KHAMSA = ['َانِ', 'ُونَ', 'ِينَ', 'ُوا', 'َا', 'ِي']

def khasais(tq):
    k = set()
    for wi, w in enumerate(tq):
        for x, (kind, dawr, txt) in enumerate(w):
            nxt = w[x + 1] if x + 1 < len(w) else (tq[wi + 1][0] if wi + 1 < len(tq) else None)
            if kind == 'core' and x > 0 and w[x - 1][0] == 'jar' and txt in DAMAIR:
                kind = 'damir'
            if kind == 'rabit': k.add('rabit')
            if kind == 'lam': k.add('lam')
            if kind == 'jar': k.add('jar_muttasil')
            if kind == 'damir':
                k.add({'مفعول_به': 'damir_maf', 'مضاف_إليه': 'damir_mudaf', 'مجرور': 'damir_majrur'}[dawr])
            if kind == 'core' and dawr == 'فعل':
                if any(txt.endswith(e) for e in RAF_DAMAIR):
                    k.add('raf_muttasil')
                if txt[0] in 'يت' and any(txt.endswith(e) for e in KHAMSA):
                    k.add('khamsa')
            if kind == 'core' and dawr in ASMA_ADWAR:
                mudaf = nxt is not None and nxt[1] == 'مضاف_إليه'
                if txt.endswith('َانِ') or txt.endswith('َيْنِ') or (mudaf and (txt.endswith('َا') or txt.endswith('َيْ'))):
                    k.add('muthanna')
                if txt.endswith('ُونَ') or txt.endswith('ِينَ') or (mudaf and (txt.endswith('ُو') or txt.endswith('ِي'))):
                    k.add('jam')
    return k

HADD_KHASAIS = ['rabit', 'lam', 'jar_muttasil', 'damir_maf', 'damir_mudaf', 'damir_majrur',
                'raf_muttasil', 'khamsa', 'muthanna', 'jam']

def haykal(w):
    return ''.join(ch for ch in bila(w) if ch not in (ALIF, WAW, YA, ALIF_MAQSURA, 'ن'))

def main():
    if len(sys.argv) != 3:
        print('الاستعمال: fahs_cases.py <cases.json> <qatr.txt>'); return 2
    raw = open(sys.argv[2], 'rb').read()
    if hashlib.sha256(raw).hexdigest() != BASMA_MASDAR:
        err('بصمةُ المصدر غيرُ بصمة المواصفة')
    LINES = raw.split(b'\n')
    def satr(n):
        s = LINES[n - 1].decode('utf-8')
        for p in ('### | ', '# ', '~~'):
            if s.startswith(p):
                return s[len(p):]
        return s
    try:
        data = json.loads(open(sys.argv[1], 'rb').read().decode('utf-8'))
    except Exception as e:
        print('JSON غيرُ صالح:', e); return 1
    if not isinstance(data, list):
        print('الملفّ ليس قائمة'); return 1

    ids = Counter(); nusus = Counter()
    fia_c = Counter(); dawr_c = Counter(); shakl_c = Counter(); kh_c = Counter()
    bymap = {}
    for c in data:
        cid = c.get('id', '?')
        if not isinstance(c, dict) or sorted(c.keys()) != sorted(KEYS):
            err('%s: حقولٌ غيرُ حقول المواصفة' % cid); continue
        bymap[cid] = c
        ids[cid] += 1
        if not re.fullmatch(r'T\d\d', cid):
            err('%s: رقمٌ على غير الصيغة' % cid)
        f, h, a = c['fia'], c['hukm'], c['adwar']
        if f not in FIAT:
            err('%s: فئةٌ غيرُ مسموحة' % cid); continue
        fia_c[f] += 1
        if not isinstance(c['mithal_harfi'], bool):
            err('%s: mithal_harfi ليس منطقيًّا' % cid)
        if not isinstance(c['taliq'], str) or not c['taliq'].strip() or '\n' in c['taliq']:
            err('%s: taliq ليس سطرًا واحدًا' % cid)
        # الحكم
        if isinstance(h, list):
            if f != 'غموض' or len(h) != 2 or len(set(h)) != 2 or any(x not in HUKM for x in h):
                err('%s: حكمٌ قائمةً على غير شرط الغموض' % cid)
        elif h not in HUKM:
            err('%s: حكمٌ غيرُ مسموح' % cid)
        else:
            want = {'موجب': 'مقبول', 'حد': 'خطأ', 'خارج': 'لا_حكم'}.get(f)
            if want and h != want:
                err('%s: الحكمُ لا يوافق الفئة' % cid)
        # الأدوار
        if isinstance(a, list) and a and all(isinstance(x, list) for x in a):
            qiraat = a
            if f != 'غموض' or len(qiraat) != 2 or qiraat[0] == qiraat[1]:
                err('%s: قراءتان على غير شرط الغموض' % cid)
        elif isinstance(a, list) and all(isinstance(x, str) for x in a):
            qiraat = [a]
        else:
            err('%s: adwar على غير الصيغة' % cid); continue
        if f == 'غموض' and not (isinstance(h, list) or len(qiraat) == 2):
            err('%s: غموضٌ بلا بديلين' % cid)
        # النصّ
        nass = c['nass']
        if not isinstance(nass, str):
            err('%s: nass ليس نصًّا' % cid); continue
        nusus[nass] += 1
        words = fahs_kitaba(cid, nass)
        roles_here = set(); ashkal = set(); kh = set()
        for q in qiraat:
            sh = shakl(q)
            if sh is None:
                err('%s: الأدوار لا توافق شكلًا %r' % (cid, q))
                continue
            ashkal.add(sh)
            roles_here.update(q)
            tq = taqti(words, q)
            if tq is None:
                err('%s: لا تقطيعَ يوافق الأدوار %r' % (cid, q))
                continue
            kh |= khasais(tq)
        for r in roles_here:
            dawr_c[r] += 1
        for s_ in ashkal:
            shakl_c[s_] += 1
        for x in kh:
            kh_c[x] += 1
        # السند
        sanad = c['sanad']
        if not isinstance(sanad, list):
            err('%s: sanad ليس قائمة' % cid); continue
        lahukm = (h == 'لا_حكم')
        if lahukm and sanad:
            err('%s: لا_حكم له سند' % cid)
        if not lahukm and not sanad:
            err('%s: حكمٌ بلا سند' % cid)
        lines_here = []
        for e in sanad:
            if not isinstance(e, dict) or sorted(e.keys()) != ['masdar', 'nass', 'satr']:
                err('%s: عنصرُ سندٍ على غير الصيغة' % cid); continue
            if e['masdar'] != 'قطر':
                err('%s: مصدرٌ غيرُ قطر' % cid)
            k = e['satr']
            if not isinstance(k, int) or k not in NITAQ:
                err('%s: سطرٌ خارج النطاق %r' % (cid, k)); continue
            q = e['nass']
            if not isinstance(q, str) or not q or '\n' in q:
                err('%s: قطعةٌ فارغة أو تعبر سطرًا' % cid); continue
            line = satr(k)
            if q.encode('utf-8') not in line.encode('utf-8'):
                err('%s: القطعةُ ليست في سطرها س%d: %r' % (cid, k, q))
            lines_here.append(line)
        harfi = any(bila(nass) in ln for ln in lines_here)
        if c['mithal_harfi'] != harfi:
            err('%s: mithal_harfi=%r والجملةُ %sفي أسطر السند' % (cid, c['mithal_harfi'], '' if harfi else 'ليست '))

    for i_, n_ in ids.items():
        if n_ > 1: err('رقمٌ مكرّر %s' % i_)
    for s_, n_ in nusus.items():
        if n_ > 1: err('جملةٌ مكرّرة %s' % s_)

    # الأزواج
    azwaj = 0
    for cid, c in bymap.items():
        z = c['zawj']
        if z is None:
            continue
        o = bymap.get(z)
        if o is None:
            err('%s: زوجٌ غيرُ موجود %s' % (cid, z)); continue
        if o['zawj'] != cid:
            err('%s: الزوجُ غيرُ متبادل' % cid)
        if o['hukm'] == c['hukm']:
            err('%s: الزوجان بحكمٍ واحد' % cid)
        a_, b_ = c['nass'].split(' '), o['nass'].split(' ')
        diff = [i for i in range(min(len(a_), len(b_))) if a_[i] != b_[i]]
        if len(a_) != len(b_) or len(diff) != 1:
            err('%s: الزوجان لا يختلفان في كلمةٍ واحدة' % cid)
        elif haykal(a_[diff[0]]) != haykal(b_[diff[0]]):
            err('%s: الكلمةُ المختلفة ليست هي بعلامتها الأخيرة' % cid)
        azwaj += 1
    azwaj //= 2

    # الأعداد
    n = len(data)
    if not 45 <= n <= 55:
        err('عددُ الحالات %d خارج 45–55' % n)
    for f, m in HADD_FIA.items():
        if fia_c[f] < m:
            err('الفئة %s: %d أقلّ من %d' % (f, fia_c[f], m))
    for r in ADWAR:
        if dawr_c[r] < 3:
            err('الدور %s: %d أقلّ من 3' % (r, dawr_c[r]))
    for s_ in ('فعلية', 'اسمية', 'شبه'):
        if shakl_c[s_] < 4:
            err('الشكل %s: %d أقلّ من 4' % (s_, shakl_c[s_]))
    for x in HADD_KHASAIS:
        if kh_c[x] < 2:
            err('الخاصّة %s: %d أقلّ من 2' % (x, kh_c[x]))
    if azwaj < 8:
        err('الأزواج %d أقلّ من 8' % azwaj)

    print('الحالات', n, '| الفئات', dict(fia_c), '| الأزواج', azwaj)
    print('الأدوار', dict(dawr_c))
    print('الأشكال', dict(shakl_c))
    print('الخصائص', dict(kh_c))
    if errs:
        print('أخطاء (%d):' % len(errs))
        for e in errs:
            print(' -', e)
        return 1
    print('مرّ كلُّ فحص')
    return 0

if __name__ == '__main__':
    sys.exit(main())
