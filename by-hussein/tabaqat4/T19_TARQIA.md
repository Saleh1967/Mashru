# ترقية T19 — مطابقة الأداة مع المستودع (2026-10-25 ، على Mashru@5e22be7)

```
+ tests/test_conformance.py   T19a: كلّ شواهد Kalima الحرفيّة في Jisr/Utur.lean (42 اليوم ، تُقرأ من المصدر) ↔ encode_word
                              T19b: tests/conf/Conf.lean على Mashru — ours = dhahabaAlWalad by decide (بلا مسلّمات) ؛ mumtani الْوَلَدَ ؛
                                    find? none/J16 ؛ halat.filter(hukm≠kalam) = [] ؛ المسلّمات ⊆ {propext, Classical.choice, Quot.sound}
~ t4/dal.py                    ى → ألف ساكنة (ALIF_MAQSURA_AS_ALIF) اتّباعًا لقرار المستودع: alFata (Utur.lean:1021) ، yakhshaAlif (:1120) ،
                              Qari/Main.lean L444–445 ؛ كانت تُسقَط DAL_CELL_UNMAPPED — وجده T19a (40/42 قبل ، 42/42 بعد)
TABAQAT4_CONFORMANCE_PASS = YES (2/2) ؛ TABAQAT4_SCOPE_TESTS_PASS = YES (12/12) — هنا ؛ T13–T18 عندك
```

التركيب (من جذر mashru): قبل نسخ dal.py تأكّد أنّ نسختك هي v3 — `shasum -a 256 by-hussein/tabaqat4/t4/dal.py` تبدأ بـ 52e44fb0 — وإلّا فطبّق التعديل يدًا (ثلاثة أسطر قبل `if letter not in idx:` في encode_word).
```bash
tar xzf t19patch.tar.gz -C by-hussein/      # يضيف tests/conf/ ، tests/test_conformance.py ، T19_TARQIA.md ويستبدل t4/dal.py
python3 -I by-hussein/tabaqat4/tests/test_conformance.py
python3 -I by-hussein/tabaqat4/tests/test_tabaqat4.py
```
