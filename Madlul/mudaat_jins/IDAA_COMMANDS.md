# أوامر الختم — للمالك وحده (qabiliyya-min-jins ج٢) ؛ الوكيل لا يشغّل sajjil

## ختم جدول الجنس (س٢)
```
python3 -I mudaat/idaa.py sajjil Madlul/mudaat_jins/jins.tsv \
  --ism "جدول جنس الكلمات (qabiliyya-min-jins)" --naw معلومات-سابقة --idhn "<إذنك>"
```
بعد تثبيت موضع كلّ صفٍّ في المخصّص المختوم (936c68e0).

## ختم جدول «الحدث مثال القابليّة» (س١+س٣)
```
python3 -I mudaat/idaa.py sajjil Madlul/mudaat_jins/mithal_qab.tsv \
  --ism "جدول الحدث مثال قابلية الحركة" --naw معلومات-سابقة --idhn "<إذنك>"
```
**متوقّف:** صفُّ «ذهب→سير» ينتظر نصّ «ذهب=سار/مضى» بموضعه — لسان العرب (34fa5671) غير محمَّل في MUDAA_DIR ، والمخصّص بلا مادّة جذرٍ واضحة. انظر OWNER_QUESTIONS س٣.
