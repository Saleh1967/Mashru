# Mashru
Mantoq to mafhoum

محرّك عربيّ مبرهن: **الدال وحده ← المدلول وحده ← الدال والمدلول معًا ← العقلية ← الجواب**.
كلّ ادّعاء في الجواب منسوبٌ إلى قاعدةٍ واحدة لها إصدار وشاهدٍ مودَعٍ مختوم، ويعيد فحصَه الفاحص نفسه.

- الدستور وطريقة العمل: `CLAUDE.md` (ملزم لكلّ جلسة)، والتعليمات: `تعليمات_المشروع.md`، والحالة: `خارطة_الطريق.md`.
- Lean 4.34.1 (`lean-toolchain`): `lake build` ثمّ `lake env lean Audit.lean` (كلّ مبرهنة بمسلّماتها).
- البوّابة قبل أيّ «تمّ»: `python3 -I tahaqquq/bawwaba.py` — يشغّلها خطّاف Stop تلقائيًّا (`.claude/settings.json`).
- الفاحص: `.lake/build/bin/faahis mudaat/sijill.tsv mawsua/makhzan.tsv`؛ القارئ: `.lake/build/bin/qari mudaat/sijill.tsv mawsua/makhzan_kamil.tsv "<نصّ مشكول>"`
  — كلمةً أو جملةً (مثل `"قَالُوا اكْتُبُوا"`): الكلمات ثمّ تركيب الجملة في الوصل على آلة المالك `Msent`، بسقوط همزة الوصل
  وإصلاحها الأدنى (Hamza.lean)، وتقطيعها كلماتٍ صوتيّةً ومقاطع (`Dal/Jumla.lean`).
- المودَعات (المخصّص، لسان العرب، تاج العروس، المقاييس، سيبويه، جدول العوامل المئة، قطر الندى، مغني اللبيب، الألفية، الجنى الداني) مسجَّلة ببصماتها في `mudaat/sijill.json` ولا تُرفع هنا؛ تُعيَّن بـ `MUDAA_MUKHASSAS` و`MUDAA_DIR` (و`MUDAA_AWAMIL`).
- الجملة الاسمية والفعلية والظرفية بأقسام الكلم: `Jisr/Tarkib.lean` على مغني اللبيب وقطر الندى، فوق ملفّات المالك (Category/Ladder2/Wad).
- بقيّة طبقة التركيب عند المالك (13 ملفًّا بنصّها: Bridge، Tarkib، Maqam، TarkibExt، Simat، Muwahhad، Kull، …؛ ملفّات شواهدها وأقفالها لم تُنقل)، والنِّسَب الثلاث عليها (`Jisr/Nisab.lean`)، وأساليب الإخبار جردًا مستنفَدًا على القطر وتغطيتها بالأطر (`Jisr/Ikhbar.lean`)، وأوّل معجم الأقسام (`Jisr/AqsamAwamil.lean`).
- العوامل المئة وفق قانون الاستنفاد: `Jisr/Awamil.lean` — الأصناف على جدول المالك المودَع، والمعادلات بتعيينه، والانغلاق والاستنفاد عليها.

عدد المبرهنات المدقَّقة (بلا sorry/axiom/native_decide) مرجعُه مخرج `lake env lean Audit.lean` وخطّ الأساس `tahaqquq/khatt_asas.json`؛ والطفرات في `tahaqquq/tafrat.json` كلّها مقتولة عند مرور البوّابة.

## سير العمل
فرعٌ لكلّ مهمّة ثمّ Pull Request؛ لا دفع إلى `main` مباشرة. كلّ PR يمرّ بالبوّابة محلّيًّا وفي CI (`bawwaba`).
الجلسات السحابية: الصق `.claude/cloud-setup.sh` في خانة Setup script لبيئتك على claude.ai/code (يثبّت Lean 4.34.1).
