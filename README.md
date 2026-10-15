# Mashru
Mantoq to mafhoum

محرّك عربيّ مبرهن: **الدال وحده ← المدلول وحده ← الدال والمدلول معًا ← العقلية ← الجواب**.
كلّ ادّعاء في الجواب منسوبٌ إلى قاعدةٍ واحدة لها إصدار وشاهدٍ مودَعٍ مختوم، ويعيد فحصَه الفاحص نفسه.

- الدستور وطريقة العمل: `CLAUDE.md` (ملزم لكلّ جلسة)، والتعليمات: `تعليمات_المشروع.md`، والحالة: `خارطة_الطريق.md`.
- Lean 4.34.1 (`lean-toolchain`): `lake build` ثمّ `lake env lean Audit.lean` (كلّ مبرهنة بمسلّماتها).
- البوّابة قبل أيّ «تمّ»: `python3 -I tahaqquq/bawwaba.py` — يشغّلها خطّاف Stop تلقائيًّا (`.claude/settings.json`).
- الفاحص: `.lake/build/bin/faahis mudaat/sijill.tsv mawsua/makhzan.tsv`؛ القارئ: `.lake/build/bin/qari mudaat/sijill.tsv mawsua/makhzan_kamil.tsv "<نصّ مشكول>"`.
- المودَعات (المخصّص، لسان العرب، تاج العروس، المقاييس، سيبويه) مسجَّلة ببصماتها في `mudaat/sijill.json` ولا تُرفع هنا؛ تُعيَّن بـ `MUDAA_MUKHASSAS` و`MUDAA_DIR`.

الإصدار 11 (2026-10-15): 199 مبرهنة مدقَّقة بلا sorry/axiom/native_decide، 54 طفرة مقتولة، القارئ 8/8.
