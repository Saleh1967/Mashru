#!/usr/bin/env python3
# فاحصُ ملفّ الحالات قبل التجميد، على المواصفة wasf.md وحدها.
# الاستعمال: python3 -I fahs_cases.py [مسار cases.json]
# يخرج 0 إن مرّ كلُّ فحص، و1 مع سرد الأخطاء إن لم يمرّ.
import hashlib
import json
import os
import re
import sys

HUNA = os.path.dirname(os.path.abspath(__file__))
MUDAA = '/home/claude/mudaa_dir/'

BASAMAT = {
    'qatr.txt': '2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d',
    'alfiyya.txt': '13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0',
    'mughni.txt': 'f37ac2bb4b273f59169053dd0ac2abf50a52846a7e87ddf689ee5c0b87f77e7d',
    'sibawayhi.txt': 'a160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625',
    'a2.txt': '8252ca521c91c285b0344b74ab5fc956f088447c8c7811fd5c95c6c2717b8401',
}

NITAQ = {
    'قوة': {
        'sibawayhi.txt': [(1268, 1294), (1522, 1525), (9190, 9304), (9544, 9652), (9782, 9787), (10022, 10041)],
        'mughni.txt': [(129, 134), (2217, 2239), (5901, 5919), (6109, 6116), (6400, 6405), (6483, 6486),
                       (8094, 8116), (9567, 9589), (9620, 9668)],
        'qatr.txt': [(108, 122), (194, 197)],
        'alfiyya.txt': [(250, 256), (296, 302), (905, 912)],
        'a2.txt': [(767, 767), (896, 896)],
    },
    'قيد': {
        'a2.txt': [(1062, 1106)],
    },
}

FIAT = ['موجب', 'حد', 'خارج', 'عموم', 'غموض']
HADD_FIA = {'موجب': 12, 'حد': 8, 'خارج': 3, 'عموم': 6, 'غموض': 2}
QUWWA = ['إثبات', 'نفي', 'تعليق', 'إنشاء']
QAYD4 = ['صفة', 'شرط', 'غاية', 'عدد']
QAYD = QAYD4 + ['لا_قيد']
LA_HUKM = 'لا_حكم'

HAROF = set(chr(c) for c in range(0x0621, 0x063B)) | set(chr(c) for c in range(0x0641, 0x064B))
ALAMAT = set(chr(c) for c in range(0x064B, 0x0653))
SHADDA = 'ّ'
SUKUN = 'ْ'
HARAKAT = set('ًٌٍَُِ')  # التنوين والحركات القصيرة
DAMMA, KASRA = 'ُ', 'ِ'

akhta = []


def khata(m):
    akhta.append(m)


def bila_badia(s):
    for p in ('### | ', '# ', '~~'):
        if s.startswith(p):
            return s[len(p):]
    return s


def bila_tashkil(s):
    return ''.join(c for c in s if c not in ALAMAT and c != 'ٰ')


_asatir = {}


def asatir(milaf):
    if milaf not in _asatir:
        with open(MUDAA + milaf, 'rb') as f:
            b = f.read()
        _asatir[milaf] = b.decode('utf-8').split('\n')
    return _asatir[milaf]


def fi_nitaq(naw, milaf, satr):
    for a, b in NITAQ.get(naw, {}).get(milaf, []):
        if a <= satr <= b:
            return True
    return False


def anaqid(kalima):
    """يقسم الكلمةَ عناقيدَ: (حرف، علاماته)."""
    out = []
    for c in kalima:
        if c in HAROF:
            out.append([c, ''])
        elif c in ALAMAT:
            if not out:
                return None
            out[-1][1] += c
        else:
            return None
    return out


def fahs_kitaba(cid, nass):
    if not isinstance(nass, str) or not nass:
        khata(f'{cid}: النصّ فارغ أو ليس نصًّا')
        return
    for c in nass:
        if not (c in HAROF or c in ALAMAT or c == ' '):
            khata(f'{cid}: محرفٌ غيرُ مسموح {hex(ord(c))}')
            return
    if nass != nass.strip(' ') or '  ' in nass:
        khata(f'{cid}: مسافاتٌ زائدة')
        return
    kalimat = nass.split(' ')
    if not (2 <= len(kalimat) <= 7):
        khata(f'{cid}: عدد الكلمات {len(kalimat)} خارج 2–7')
    for kalima in kalimat:
        an = anaqid(kalima)
        if not an:
            khata(f'{cid}: كلمةٌ تبدأ بعلامة أو فارغة «{kalima}»')
            continue
        for i, (h, al) in enumerate(an):
            # العلامات في العنقود: شدّةٌ اختياريّة، وعلامةٌ واحدةٌ من الحركات أو السكون
            ghayr_shadda = [c for c in al if c != SHADDA]
            if al.count(SHADDA) > 1 or len(ghayr_shadda) > 1:
                khata(f'{cid}: علاماتٌ متعارضة على «{h}» في «{kalima}»')
            if SHADDA in al and not (set(ghayr_shadda) & HARAKAT):
                khata(f'{cid}: شدّةٌ بلا حركة في «{kalima}»')
            if al:
                continue
            sabiq = an[i - 1] if i > 0 else None
            lahiq = an[i + 1] if i + 1 < len(an) else None
            if h in ('ا', 'آ', 'ى'):
                continue
            if h == 'و' and sabiq and DAMMA in sabiq[1]:
                continue
            if h == 'ي' and sabiq and KASRA in sabiq[1]:
                continue
            if h == 'ل' and lahiq and SHADDA in lahiq[1] and sabiq and (sabiq[0] == 'ا' or sabiq[0] == 'ل'):
                continue  # لامُ التعريف قبل الحرف الشمسيّ المشدَّد
            khata(f'{cid}: حرفٌ بلا علامة «{h}» في «{kalima}»')
        h, al = an[-1]
        if not al and h not in ('ا', 'ى', 'و', 'ي', 'آ'):
            khata(f'{cid}: آخرُ «{kalima}» بلا علامة')


def qima_kharij(c):
    naw = c.get('naw')
    k = c.get('kharij')
    if not isinstance(k, dict) or len(k) != 1:
        return None, 'kharij ليس قاموسًا بحقلٍ واحد'
    maftah = 'quwwa' if naw == 'قوة' else 'qayd'
    if maftah not in k:
        return None, f'kharij بلا الحقل {maftah}'
    return k[maftah], None


def tabaayun(a, b):
    """كم كلمةً يختلف فيها النصّان: استبدالٌ واحد أو زيادةُ كلمةٍ واحدة."""
    x, y = a.split(' '), b.split(' ')
    if len(x) == len(y):
        return sum(1 for p, q in zip(x, y) if p != q)
    if abs(len(x) - len(y)) == 1:
        tawil, qasir = (x, y) if len(x) > len(y) else (y, x)
        for i in range(len(tawil)):
            if tawil[:i] + tawil[i + 1:] == qasir:
                return 1
        return 99
    return 99


def main():
    masar = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HUNA, 'cases.json')

    # بصمات المصادر
    for milaf, b in BASAMAT.items():
        try:
            with open(MUDAA + milaf, 'rb') as f:
                h = hashlib.sha256(f.read()).hexdigest()
        except OSError as e:
            khata(f'المصدر {milaf} لا يُقرأ: {e}')
            continue
        if h != b:
            khata(f'بصمة {milaf} {h} لا تطابق المواصفة')
    wasf = os.path.join(HUNA, 'wasf.md')
    if os.path.exists(wasf):
        with open(wasf, encoding='utf-8') as f:
            nw = f.read()
        for milaf, b in BASAMAT.items():
            if not re.search(r'`' + re.escape(milaf) + r'`[^\n]*`' + b + '`', nw):
                khata(f'جدولُ البصمات في الفاحص لا يطابق wasf.md في {milaf}')
    if akhta:
        return

    try:
        with open(masar, encoding='utf-8') as f:
            cases = json.load(f)
    except Exception as e:
        khata(f'JSON غير صالح: {e}')
        return
    if not isinstance(cases, list):
        khata('الملفّ ليس قائمة')
        return

    ids = {}
    huqul = {'id', 'naw', 'fia', 'nass', 'mithal_harfi', 'kharij', 'zawj', 'sanad', 'taliq'}
    for i, c in enumerate(cases):
        if not isinstance(c, dict):
            khata(f'العنصر {i} ليس قاموسًا')
            continue
        cid = c.get('id')
        if not isinstance(cid, str) or not re.fullmatch(r'A\d\d', cid):
            khata(f'العنصر {i}: id غير صالح {cid!r}')
        elif cid in ids:
            khata(f'id مكرَّر {cid}')
        else:
            ids[cid] = c
        if set(c.keys()) != huqul:
            khata(f'{cid}: الحقول {sorted(c.keys())} غير الحقول المطلوبة')
    if akhta:
        return

    adad_naw = {'قوة': 0, 'قيد': 0}
    adad_fia = {f: 0 for f in FIAT}
    adad_q = {v: 0 for v in QUWWA}
    adad_k = {v: 0 for v in QAYD}
    nusus = {'قوة': set(), 'قيد': set()}

    for cid, c in ids.items():
        naw, fia = c['naw'], c['fia']
        if naw not in adad_naw:
            khata(f'{cid}: naw غير مسموح {naw!r}')
            continue
        adad_naw[naw] += 1
        if fia not in adad_fia:
            khata(f'{cid}: fia غير مسموحة {fia!r}')
            continue
        adad_fia[fia] += 1

        if not isinstance(c['mithal_harfi'], bool):
            khata(f'{cid}: mithal_harfi ليس منطقيًّا')
        if not isinstance(c['taliq'], str) or not c['taliq'].strip() or '\n' in c['taliq'] or '\r' in c['taliq']:
            khata(f'{cid}: taliq ليس سطرًا واحدًا غيرَ فارغ')

        fahs_kitaba(cid, c['nass'])
        if isinstance(c['nass'], str):
            if c['nass'] in nusus[naw]:
                khata(f'{cid}: الجملة مكرَّرة في النوع {naw}')
            nusus[naw].add(c['nass'])

        v, e = qima_kharij(c)
        if e:
            khata(f'{cid}: {e}')
            continue
        masmuh = QUWWA if naw == 'قوة' else QAYD
        if isinstance(v, list):
            if len(v) < 2 or len(set(v)) != len(v) or any(not isinstance(x, str) for x in v):
                khata(f'{cid}: قائمةٌ غير صالحة {v!r}')
            elif naw == 'قوة':
                if fia != 'غموض' or len(v) != 2 or any(x not in QUWWA for x in v):
                    khata(f'{cid}: القائمة في قوة لا تكون إلّا بديلين في غموض {v!r}')
            else:
                if fia == 'غموض':
                    if len(v) != 2 or any(x not in QAYD for x in v):
                        khata(f'{cid}: بديلا الغموض في قيد غير صالحين {v!r}')
                elif any(x not in QAYD4 for x in v):
                    khata(f'{cid}: قائمةُ الأصناف لا تحوي إلّا الأربعة {v!r}')
            la_hukm = False
        elif isinstance(v, str):
            if v != LA_HUKM and v not in masmuh:
                khata(f'{cid}: قيمةٌ غير مسموحة {v!r}')
            if fia == 'غموض':
                khata(f'{cid}: الغموض متوقَّعه قائمةٌ بالبديلين')
            la_hukm = (v == LA_HUKM)
            if naw == 'قوة' and v in adad_q:
                adad_q[v] += 1
            if naw == 'قيد' and v in adad_k:
                adad_k[v] += 1
        else:
            khata(f'{cid}: القيمة ليست نصًّا ولا قائمة')
            continue
        if (fia == 'خارج') != la_hukm:
            khata(f'{cid}: الخارج متوقَّعه لا_حكم، ولا_حكم لا يكون إلّا في الخارج')

        # السند
        sanad = c['sanad']
        if not isinstance(sanad, list):
            khata(f'{cid}: sanad ليس قائمة')
            continue
        if la_hukm and sanad:
            khata(f'{cid}: حالة لا_حكم لها سند')
        if not la_hukm and not sanad:
            khata(f'{cid}: حكمٌ بلا سند')
        asatir_sanad = []
        for q in sanad:
            if not isinstance(q, dict) or set(q.keys()) != {'milaf', 'satr', 'nass'}:
                khata(f'{cid}: قطعة سند بحقولٍ غير المطلوبة {q!r}')
                continue
            m, s, n = q['milaf'], q['satr'], q['nass']
            if m not in BASAMAT:
                khata(f'{cid}: ملفٌّ ليس في الجدول {m!r}')
                continue
            if not isinstance(s, int) or isinstance(s, bool) or s < 1 or s > len(asatir(m)):
                khata(f'{cid}: رقم سطر غير صالح {s!r} في {m}')
                continue
            if not isinstance(n, str) or not n or '\n' in n:
                khata(f'{cid}: نصّ القطعة فارغ أو يعبر سطرين')
                continue
            if not fi_nitaq(naw, m, s):
                khata(f'{cid}: السطر {m}:{s} خارج نطاق {naw}')
            satr = bila_badia(asatir(m)[s - 1])
            if n.encode('utf-8') not in satr.encode('utf-8'):
                khata(f'{cid}: القطعة ليست في {m}:{s} بالبايت «{n}»')
            asatir_sanad.append(satr)
        if c['mithal_harfi'] is True and isinstance(c['nass'], str):
            jumla = bila_tashkil(c['nass'])
            if not any(jumla in bila_tashkil(st) for st in asatir_sanad):
                khata(f'{cid}: mithal_harfi=true والجملة ليست بحروفها في سطرٍ من سندها')

    # الأزواج
    azwaj = set()
    for cid, c in ids.items():
        z = c['zawj']
        if z is None:
            continue
        if not isinstance(z, str) or z not in ids or z == cid:
            khata(f'{cid}: zawj غير صالح {z!r}')
            continue
        d = ids[z]
        if d['zawj'] != cid:
            khata(f'{cid}: الزوج {z} غير متبادل')
            continue
        if d['naw'] != c['naw']:
            khata(f'{cid}: الزوج {z} من نوعٍ آخر')
            continue
        v1, _ = qima_kharij(c)
        v2, _ = qima_kharij(d)
        s1 = frozenset(v1) if isinstance(v1, list) else frozenset([v1])
        s2 = frozenset(v2) if isinstance(v2, list) else frozenset([v2])
        if s1 == s2:
            khata(f'{cid}: متوقَّعا الزوج {z} متساويان')
        if isinstance(c['nass'], str) and isinstance(d['nass'], str) and tabaayun(c['nass'], d['nass']) != 1:
            khata(f'{cid}: الزوج {z} لا يخالفها في كلمةٍ واحدة')
        azwaj.add(frozenset((cid, z)))

    # الأعداد
    n = len(ids)
    if not (40 <= n <= 50):
        khata(f'عدد الحالات {n} خارج 40–50')
    for naw, a in adad_naw.items():
        if a < 18:
            khata(f'النوع {naw}: {a} حالة، والحدّ 18')
    for f, h in HADD_FIA.items():
        if adad_fia[f] < h:
            khata(f'الفئة {f}: {adad_fia[f]}، والحدّ {h}')
    for v, a in adad_q.items():
        if a < 3:
            khata(f'قوة={v}: {a}، والحدّ 3')
    for v, a in adad_k.items():
        if a < 2:
            khata(f'قيد={v}: {a}، والحدّ 2')
    if len(azwaj) < 4:
        khata(f'الأزواج {len(azwaj)}، والحدّ 4')

    print(f'الحالات {n}؛ الأنواع {adad_naw}؛ الفئات {adad_fia}')
    print(f'قوة {adad_q}؛ قيد {adad_k}؛ الأزواج {len(azwaj)}؛ '
          f'الحرفيّة {sum(1 for c in ids.values() if c["mithal_harfi"] is True)}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:  # أيُّ عطبٍ غير متوقَّع فشل
        khata(f'عطبٌ في الفحص: {type(e).__name__}: {e}')
    if akhta:
        for a in akhta:
            print('خطأ:', a)
        print(f'فشل: {len(akhta)} خطأ')
        sys.exit(1)
    print('مرّ: كلُّ الفحوص')
    sys.exit(0)
