# -*- coding: utf-8 -*-
"""الطبقة الأولى — الدالّ وحده: نصّ مشكول ← خلايا Mashru.

لا جدولَ ترميزٍ هنا: جدول الحوامل يُقرأ من Dal/Makharij.lean في شجرة Mashru وقت التشغيل
(def hawamil : List Char := [...]) ، والحالات الأربع من Dal/Khaliya.lean (فتحة 0 ضمّة 1 كسرة 2 سكون 3) ،
ورقم الخلية n = 4·حامل + حالة (Dal.n). كلُّ تحويلٍ على السطح (همزة ، شدّة ، تنوين ، أل) يُسمَّى في المخرجات.
"""
from __future__ import annotations
import re, unicodedata
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List, Optional

FATHA, DAMMA, KASRA, SUKUN = 0, 1, 2, 3
HARAKAT = {'َ': FATHA, 'ُ': DAMMA, 'ِ': KASRA, 'ْ': SUKUN}
TANWIN = {'ً': FATHA, 'ٌ': DAMMA, 'ٍ': KASRA}   # فتحتان ضمّتان كسرتان
SHADDA = 'ّ'
# صور الهمزة على الحوامل → حرف الهمزة في جدول المخارج (تحويل مُعلَن ، لا تطبيع صامت)
HAMZA_FORMS = {'أ': 'ء', 'إ': 'ء', 'ؤ': 'ء', 'ئ': 'ء'}
ALIF_MADDA = 'آ'   # آ = ءَ + اْ
# اللام الشمسيّة: الحروف التي تُدغَم فيها لام التعريف
SHAMSIYYA = set('تثدذرزسشصضطظلن')


@dataclass
class KalimaDal:
    surface: str
    khalaya: List[int]
    wasl: bool
    al: bool
    tanwin: bool
    transforms: List[str] = field(default_factory=list)   # تحويلات مُعلَنة بأسمائها
    residuals: List[str] = field(default_factory=list)    # ما لم يُرمَّز ولماذا
    cells_human: List[str] = field(default_factory=list)  # «ذَ=23/0→92»

    @property
    def ok(self) -> bool:
        return not self.residuals

    def to_dict(self):
        x = asdict(self); x['qari'] = getattr(self, 'qari', None); return x


def load_hawamil(mashru_root: Path) -> List[str]:
    """يقرأ قائمة الحوامل من Dal/Makharij.lean ؛ يرفض إن لم يجدها (لا جدول موازٍ)."""
    p = mashru_root / 'Dal' / 'Makharij.lean'
    src = p.read_text(encoding='utf-8')
    m = re.search(r"def\s+hawamil\s*:\s*List\s+Char\s*:=\s*\[(.*?)\]", src, re.S)
    if not m:
        raise RuntimeError('HAWAMIL_TABLE_NOT_FOUND_IN_MASHRU: ' + str(p))
    chars = re.findall(r"'(.)'", m.group(1))
    if len(chars) != 29:
        raise RuntimeError(f'HAWAMIL_LEN_{len(chars)}_NE_29')
    return chars


def _nfc(s: str) -> str:
    return unicodedata.normalize('NFC', s)


def tokenize(text: str) -> List[str]:
    """تقطيع على الفراغات فقط ؛ علامات الترقيم العربية تُفصَل وتُسقَط مُعلَنةً عند المستدعي."""
    return [w for w in re.split(r'\s+', text.strip()) if w]


def encode_word(word: str, hawamil: List[str]) -> KalimaDal:
    """كلمة مشكولة ← KalimaDal. يعمل على نقاط الرمز كما وصلت (NFC) ؛ كلُّ تحويلٍ يُسجَّل باسمه."""
    w = _nfc(word)
    idx = {c: i for i, c in enumerate(hawamil)}
    k = KalimaDal(surface=word, khalaya=[], wasl=False, al=False, tanwin=False)

    # 1) تفكيك إلى (حرف ، حركة|None ، شدّة؟ ، تنوين?)
    units = []   # [letter, haraka(int|None), shadda(bool), tanwin(int|None)]
    for ch in w:
        if ch in HARAKAT:
            if not units: k.residuals.append('DAL_HARAKA_WITHOUT_CARRIER'); continue
            units[-1][1] = HARAKAT[ch]
        elif ch in TANWIN:
            if not units: k.residuals.append('DAL_TANWIN_WITHOUT_CARRIER'); continue
            units[-1][3] = TANWIN[ch]
        elif ch == SHADDA:
            if not units: k.residuals.append('DAL_SHADDA_WITHOUT_CARRIER'); continue
            units[-1][2] = True
        elif ch == 'ٰ':   # ألف خنجرية
            k.residuals.append('DAL_CELL_UNMAPPED:ألف_خنجرية')
        else:
            units.append([ch, None, False, None])

    # 2) أل التعريف: «ا» ثمّ «ل» في أوّل الكلمة ، لا حركة على الألف
    if len(units) >= 2 and units[0][0] == 'ا' and units[0][1] is None and units[1][0] == 'ل':
        k.al = True; k.wasl = True
        k.transforms.append('AL_FLAG:همزة_الوصل_لا_تُرمَّز(Dal.Kalima.al=true,wasl=true)')
        units = units[1:]           # تبقى اللام
        lam = units[0]
        if len(units) >= 2 and units[1][0] in SHAMSIYYA and units[1][2]:
            # لام شمسيّة مدغمة: تسقط اللام ، والحرف التالي مشدَّد = ساكن + متحرّك
            units = units[1:]
            k.transforms.append('AL_SHAMSIYYA:اللام_مدغمة_في_' + units[0][0])
        else:
            if lam[1] is None: lam[1] = SUKUN
            k.transforms.append('AL_QAMARIYYA:لام_ساكنة')

    # 3) الحروف إلى خلايا
    out: List[int] = []
    human: List[str] = []
    for i, (ch, h, sh, tn) in enumerate(units):
        letter = ch
        if ch in HAMZA_FORMS:
            letter = 'ء'; k.transforms.append(f'HAMZA_FORM:{ch}→ء')
        if ch == ALIF_MADDA:
            k.transforms.append('ALIF_MADDA:آ→ءَ+اْ')
            out += [4 * idx['ء'] + FATHA, 4 * idx['ا'] + SUKUN]
            human += ['ءَ', 'اْ']; continue
        if letter not in idx:
            k.residuals.append(f'DAL_CELL_UNMAPPED:{ch}')   # ة ى … ليست في جدول المخارج (Dal.kh? يرفضها)
            continue
        c = idx[letter]
        if letter == 'ا' and h is None and i == len(units) - 1 and i > 0 and units[i - 1][3] == FATHA:
            k.transforms.append('TANWIN_FATH_ALIF_DROPPED:ألف_تنوين_الفتح_لا_تُرمَّز(شاهد_ذَاهِبًا)')
            continue
        if letter in ('ا', 'و', 'ي') and h is None and tn is None:
            h = SUKUN; k.transforms.append(f'MADD_UNMARKED_AS_SUKUN:{letter}_بلا_حركة=ساكنة(حرف_مدّ)')
        if h is None and tn is None:
            if i == len(units) - 1:
                h = SUKUN; k.transforms.append('FINAL_UNMARKED_AS_SUKUN:' + ch)
            else:
                k.residuals.append(f'DAL_HARAKA_MISSING:{ch}@{i}'); continue
        if sh:
            out.append(4 * c + SUKUN); human.append(ch + 'ْ')
            k.transforms.append(f'SHADDA:{ch}→ساكن+متحرّك')
        if tn is not None:
            out.append(4 * c + tn); human.append(ch + '◌' + 'َُِ'[tn])
            out.append(4 * idx['ن'] + SUKUN); human.append('نْ(تنوين)')
            k.tanwin = True
            k.transforms.append('TANWIN:نون_ساكنة(59)_بعد_الحركة')
        else:
            out.append(4 * c + h); human.append(ch + 'َُِْ'[h])
    k.khalaya = out
    k.cells_human = [f'{hm}={n}' for hm, n in zip(human, out)]
    if any(n >= 116 for n in out):
        k.residuals.append('DAL_CELL_GE_116')
    return k
