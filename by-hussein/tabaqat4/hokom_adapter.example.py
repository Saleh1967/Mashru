# -*- coding: utf-8 -*-
"""مثال واجهة hokom_adapter.py — انسخه إلى by-hussein/tabaqat4/hokom_adapter.py وأكمله.
العقد: def taqdir(surfaces: list[str]) -> list[dict]
  كلّ dict: {"pin": "<sha12 لـ Hokom المقروء>", "word_class": ..., "root": [...], "wazn": ..., "directive": "ACCEPT|DEFER|REFUSE", "residuals": [...]}
  - قراءةٌ فقط من /Users/husseinhiyassat/hokom بالـpin المعلَن ؛ لا كتابة ولا كاش في شجرته (PYTHONDONTWRITEBYTECODE=1).
  - لا رقم ثقة ؛ لا تحويل إلى مدلول ؛ الأداة تعرض المخرج برتبة «تقدير» ولا تستهلكه.
  - إن غاب شيء أعِد None في حقله مع سبب في residuals ؛ لا تخمين."""
def taqdir(surfaces):
    raise NotImplementedError('HOKOM_ADAPTER_NOT_IMPLEMENTED: اربطه بسجلّ HokomSentenceRecord:v1 أو بموصل by-hussein القائم')
