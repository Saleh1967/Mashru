# أوامر الختم — للمالك وحده (v7 B4)

الوكيل لا يشغّل `idaa.py sajjil` ولا يكتب في `mudaat/sijill.json` (م9). هذه الأوامر مُعدّةٌ لتشغيلها أنتَ بإذنك.

## ١) ختم مصدر D6: MANIFEST (HFN release_v18)
البصمة الحاليّة: `975b7da58be2aa8211435bb310d4c36ac9a1b477f5e489fa99ac080628984fd3`
```
python3 -I mudaat/idaa.py sajjil \
  /Users/husseinhiyassat/arabic-net/HusseinFrameNet/release/release_v18/MANIFEST.json \
  --ism "HFN release_v18 MANIFEST" --naw معلومات-سابقة --idhn "<إذنك>"
```

## ٢) سند المقاييس — مختومٌ أصلًا ، لا أمرَ جديد
«مقاييس اللغة» مختومٌ في `mudaat/sijill.json` ببصمة `7f71af0dfe056cb84e7da24657fa13edc6e8061c…`.
**لكنّ نصّه (maqayis.txt) غيرُ حاضرٍ في هذه البيئة** (MUDAA_DIR نائب) ، فتعيينُ «الموضع في النصّ المختوم» (B4: `7f71af0d@موضع`)
يتعذّر هنا ⇒ كلُّ مودَع D6 يبقى `D6_NO_SANAD_SEALED_ABSENT` حتى يحضُر النصّ المختوم على جهازك. لا إحالةَ إلى `maqayis.db`.

## ٣) ختم المودَعات المصدَّرة (حين تُرسَّم D6 على جهازك)
بعد أن يحضُر النصّ المختوم وتُرسَّم مودَعات D6 في `madlulat_export.tsv` ، تختمه في MUDAA_DIR:
```
python3 -I mudaat/idaa.py sajjil \
  <MUDAA_DIR>/madlulat_export.tsv \
  --ism "madlulat tabaqat4 (D5+D6)" --naw معلومات-سابقة --idhn "<إذنك>"
```
ثمّ بصمتُه في `mudaat/sijill.json` ترفع `MUDAAT_UNSEALED` عن الأداة ، فيُولَّد `Mudaat.lean` من نسخةٍ مختومة.

## ما لم يُفعَل (بيئة)
- لم يُشغَّل أيُّ `sajjil` (م9).
- النصّ المختوم للمقاييس/المخصّص غيرُ حاضر ⇒ لا مودَع D6 رُسِّم في هذه البيئة (الأهليّة في `D6_COVERAGE.md` وضع `db_preview`).
