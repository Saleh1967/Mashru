# ملحقُ ضابط الخبر ١: ما أُخذ من قراءة المؤلّف بعد التشغيل الأوّل، وما تغيّر بعده

هذا الملحقُ لا يعدّل الملفّاتِ المجمَّدة (`tajmid.json`). يسجّل ما فعله البنّاءُ بعد أن قرأ الحالات، وهو على مادّةٍ مكشوفة.

## ١. التشغيلُ الأوّل وقراءةُ المؤلّف

التشغيلُ الأوّل (`natija_1.json`، على الشفرة المجمَّدة في `4374052`، قبل قراءة الحالات): 85 صوابًا من 88 حقلًا مسؤولًا، وثلاثةُ إخفاقات. ثمّ قرأ
البنّاءُ الحالاتِ و`taalif.md`. وأخذت الشفرةُ قراءةَ المؤلّف في المواضع الثلاثة كلِّها:

| الحالة | نتيجةُ الشفرة المجمَّدة | قراءةُ المؤلّف (من `taliq` وسندِه، وقاعدتُه في `taalif.md`) | ما صار |
|---|---|---|---|
| K21 (الزمانُ عن المعنى، غيرَ مفيد) | «لا حكم»: القطرُ يقبله بإطلاق «وظرفا» (س159)، والألفيةُ تخطّئه بـ«المتم الفائدة» (س182)، فاختلفا | القطرُ لا يتعرّض للإفادة، فحكمُها حكمُ الألفية: خطأ (القرار ٤) | خطأ؛ والقطرُ ساكتٌ في الزمان عن المعنى غيرَ مفيد، وكان يقبله مفيدًا (وصار ساكتًا فيه أيضًا بعد المراجعة، §٤) |
| K35، K36 (الخبرُ الجامدُ الرافعُ ظاهرًا) | خطأ: «فارغ» (س185) | الألفيةُ تذكر ما يحمله المفرد من الضمير ولا تذكر ظاهرًا يرفعه، والقطرُ في نطاقه لا يذكر المفرد: «لا حكم» | «لا حكم»، كالمشتقّ الرافع ظاهرًا |

والتشغيلُ الثاني (`natija_2.json`) بعد التعديل: 88 من 88. وهو موافقةٌ بعد الاطّلاع، لا شاهدٌ مستقلّ.

## ٢. ما تغيّر على المجال كلّه

مقابلةُ جواب الشفرة المجمَّدة (`4374052`) بجواب `Jisr.Khabar.jawab` الحاليّ على كلّ مدخلٍ من 2,903,040 (حقولُ `Dakhil` بقيمها)، بالسكربت أدناه
(يُشغَّل بنسخه إلى جذر الشجرة و`lake env lean`). المتّسقُ منها 110، وما سواها «لا حكم» قبلُ وبعدُ (`muttasiq` لم يتغيّر). تغيّر جوابُ تسعة:

| المدخل | من ← إلى | الحالة |
|---|---|---|
| مبتدأٌ معنًى، وخبرُه ظرفُ زمانٍ غيرُ مفيد | «لا حكم» ← خطأ | K21 |
| مبتدأٌ ذات، وخبرُه مفردٌ جامدٌ رافعٌ ظاهرًا | خطأ ← «لا حكم» | K35 |
| مبتدأٌ معنًى، وخبرُه مفردٌ جامدٌ رافعٌ ظاهرًا | خطأ ← «لا حكم» | K36 |
| وصفٌ مثنًّى أو مجموعٌ يطابق مرفوعَه، والمسؤولُ عنه الفاعلُ الذي أغنى، بالاعتمادات الثلاثة (بعد المراجعة، §٤) | خطأ ← «لا حكم» | — (ستّةُ مدخلات) |

ولا مدخلَ تغيّرت درجتُه وحدها. والحالاتُ تمسّ الثلاثةَ الأولى وحدها، فالستّةُ لا تشهد لها.

```lean
import Jisr.Khabar
/-! مقابلةُ جواب الشفرة المجمَّدة (`4374052`) بجواب `Jisr.Khabar.jawab` على المجال كلّه. `qatr0` و`alfiyya0` منسوختان بنصّهما من
    `git show 4374052:Jisr/Khabar.lean` على الأنواع نفسِها؛ و`muttasiq` و`jamaa` و`tabaq` لم تتغيّر (يُرى بـ`git diff 4374052 -- Jisr/Khabar.lean`). -/
namespace Mj
open Jisr.Khabar

def qatr0 (d : Dakhil) : Qawl :=
  match d.binya with
  | .mubtadaKhabar =>
    match d.khabar with
    | .jumlaIsmiyya | .jumlaFiliyya => some (if d.rabit = .laRabit then khataJ else maqbulJ [.bila])
    | .zarfMakan | .jarMajrur => some (maqbulJ [.bila])
    | .zarfZaman =>
      match d.jins, d.ifada with
      | .dhat, .mufid => some (maqbulJ [.bitawil])
      | .dhat, _ => some khataJ
      | _, _ => some (maqbulJ [.bila])
    | _ => none
  | .wasfMarfu =>
    match d.tahlil with
    | .failAghna =>
      if d.wasfAdad = .mufrad then some (if d.itimad = .laItimad then khataJ else maqbulJ [.bila]) else none
    | _ => none

def alfiyya0 (d : Dakhil) : Qawl :=
  match d.binya with
  | .mubtadaKhabar =>
    match d.khabar with
    | .jumlaIsmiyya | .jumlaFiliyya => some (if d.rabit ≠ .laRabit then maqbulJ [.bila] else khataJ)
    | .mufradJamid => some (if d.marfu = .laShay then maqbulJ [.bila] else khataJ)
    | .mufradMushtaq =>
      match d.jaryan, d.marfu with
      | .lisahibihi, .mustakin => some (maqbulJ [.bila])
      | .lighayrihi, .bariz => some (maqbulJ [.bila])
      | _, .zahir => none
      | _, _ => some khataJ
    | .jarMajrur | .zarfMakan => some (maqbulJ [.bila])
    | .zarfZaman => some (if d.ifada = .mufid then maqbulJ [.bila] else khataJ)
    | .la => none
  | .wasfMarfu =>
    match d.tahlil with
    | .failAghna =>
      some (if tabaq d then khataJ else if d.itimad = .laItimad then maqbulJ [.qalil] else maqbulJ [.bila])
    | .khabarMuqaddam => some (if tabaq d then maqbulJ [.bila] else khataJ)
    | .la => none


def jawab0 (d : Dakhil) : Jawab := if !muttasiq d then laHukmJ else jamaa (qatr0 d) (alfiyya0 d)

def majal : List Dakhil :=
  [Binya.mubtadaKhabar, .wasfMarfu].flatMap fun b => [Jins.dhat, .maana, .la].flatMap fun j =>
  [NawKhabar.mufradJamid, .mufradMushtaq, .jumlaIsmiyya, .jumlaFiliyya, .zarfMakan, .zarfZaman, .jarMajrur, .la].flatMap fun k =>
  [Rabit.damir, .ishara, .iada, .umum, .hiya, .laRabit, .la].flatMap fun r =>
  [Marfu.mustakin, .bariz, .zahir, .laShay, .la].flatMap fun m =>
  [Jaryan.lisahibihi, .lighayrihi, .la].flatMap fun y =>
  [Ifada.mufid, .ghayrMufid, .la].flatMap fun i =>
  [Itimad.istifham, .nafy, .laItimad, .la].flatMap fun t =>
  [Adad.mufrad, .muthanna, .jam, .la].flatMap fun w =>
  [Adad.mufrad, .muthanna, .jam, .la].flatMap fun f =>
  [Tahlil.failAghna, .khabarMuqaddam, .la].map fun l => ⟨b, j, k, r, m, y, i, t, w, f, l⟩

def taghayyar : List (Dakhil × Jawab × Jawab) :=
  majal.filterMap fun d => if jawab0 d != jawab d then some (d, jawab0 d, jawab d) else none

#eval majal.length
#eval (majal.filter muttasiq).length
#eval taghayyar.length
#eval taghayyar
end Mj
```

## ٣. ما لا تشهد له الحالات من التعيين

بنودُ «ما هو تعيينُ البنّاء» في رأس `Jisr/Khabar.lean`، وما يمسّها من الحالات (بمقابلة حقول `dakhil`، عدُّ أداةٍ في الجلسة):
- الروابطُ الأربعةُ والجملةُ التي هي المبتدأ، في الجملتين وفي الذات والمعنى: تمسّها K01–K13 (كلُّ رابطٍ في حالةٍ على الأقلّ، وكلٌّ من الجملتين، ومن الذات
  والمعنى)؛ ولا تمسّ كلَّ جمعٍ منها (عشرون جمعًا مقبولًا، في الحالات عشرة).
- «فارغ» و«ذو ضمير مستكن»، والبارزُ لصاحبه خطأ: تمسّها K22–K34 (والبارزُ لصاحبه K29 وحدها). والرافعُ ظاهرًا «لا حكم»: K35–K39.
- الإفادةُ في الزمان عن المعنى: K20، K21.
- **«وصف» في القطر مفرد، وحكمُ المثنّى والمجموع من الألفية وحدها: لا حالةَ تمسّه.** الوصفُ المثنّى والمجموع في الحالات (K50–K54) كلُّه خبرٌ مقدَّم،
  والقطرُ لا يحكم فيه بأيّ عدد؛ ولا حالةَ بوصفٍ غيرِ مفردٍ والمسؤولُ عنه الفاعلُ الذي أغنى، وهو الموضعُ الذي يفرّق فيه هذا التعيين.
- **عمومُ س178–179 على عدد الوصف** (الوصفُ غيرُ المفرد بلا مطابقةٍ فاعلُه مقبولٌ معتمدًا وقليلًا بلا اعتماد): لا حالةَ تمسّه، للسبب نفسِه.
- المطابقةُ في غير الإفراد شرطٌ للخبر المقدَّم: تمسّه حالاتُ الخبر المقدَّم K41، K45، K50–K56. **والفاعلُ الذي أغنى مع المطابقة «لا حكم»: لا حالةَ تمسّه**
  (المطابقةُ في الحالات في K50 وK52 وK54 وحدها، وكلُّها خبرٌ مقدَّم؛ والمؤلّفُ تجنّب هذا الموضع، `taalif.md` القرار ٥). والاعتمادُ لا أثرَ له في الخبر
  المقدَّم: تفرّقه K54 وحدها (K55 خطأٌ على أيّ قراءة).
- الشرطُ حكمٌ في الصورة بلا شرطها: يمسّها كلُّ «خطأ» بشرط صورة (منها K02 بلا رابط، وK18 الزمانُ عن الذات غيرَ مفيد، وK41 الخبرُ المقدَّمُ بلا مطابقة).
- **درجةُ «قليل»** (س179): حالاتُها كلُّها (K47، K48، K57) غموضٌ بحكمين، والدرجةُ فيه لا تُقارَن (`Jisr/KhabarDabit.lean`، زيادةُ البنّاء)؛ فـ88/88 لا تشهد لها،
  وحارسُها شطرٌ من `shawahid` بمدخلٍ ليس من أمثلة النطاق.

## ٤. بعد مراجعة `murajii` الأولى

- **الحكم:** الفاعلُ الذي أغنى مع المطابقة في غير الإفراد «لا حكم» (كان خطأً بنسبته إلى س180، ومفتاحُ المواصفة لا يجعله خطأً وعمومُ س178 يقبله)؛ والقطرُ
  ساكتٌ في الزمان عن المعنى مفيدًا أيضًا (كانت قاعدةُ السكوت عن الإفادة مطبَّقةً على غير المفيد وحده؛ ولا يتغيّر به جواب).
- **المقارنة** (`Jisr/KhabarDabit.lean`): «لا حكم» في الغموض بدرجتين صوابٌ بنصّ المواصفة (كانت نقصَ تغطية)؛ ولا أثرَ له في أعداد التشغيلين.
- **التوثيق:** الصلةُ بقطع Lean القائمة مقابلاتٌ على الشاهد لا ربط؛ و`ibtida_wad` مطابقةُ اسمٍ ورقم، ومعه خلافُ الألفية س181 يُعرض على المالك؛ والخلافُ المعلَن
  مع `Aql.Isnad.yastaghni` صار حدَّ تمثيلٍ هناك (`hadd_isnad_rabit`، بدل `khilaf_isnad_rabit` الذي لم يُظهر مدخلًا مشتركًا)؛ وأقربُ الموجود في الوصف
  ومرفوعه (`Jisr/Mulhaqat.lean`، `Jisr/Tarkib.lean`) مذكور، وقُيّد «لم يُبنَ» في `Jisr/KhulasaIkhbar.lean` وجرد القطر؛ و«الروابط الخمسة» صارت «الأربعة والجملة
  التي هي المبتدأ»؛ و«أقائم زيد» بلا علامتي اقتباس (ليست في النطاق)؛ ووصفُ `isnad_kubra` بلا «كان».
- **الإفصاح:** وقتُ كتابة الشفرة في `tawjih_muallif.md` من أوقات الملفّات (آخرُ تعديلٍ لا بدءُ الكتابة)، و`sijill_muallif.json` يذكر مسارًا من متغيّرٍ في
  أوامر المؤلّف لا وجود له، و`CLAUDE.md` المحقونُ في سياقه فيه وصفُ `Aql.Isnad` بالقطر س157–160 (أفصح به المؤلّف في `taalif.md`).
- **الطفرات:** P1147 (الفاعلُ مع المطابقة) وP1148 (الغموضُ بدرجتين في المقارنة) جديدتان يقتلهما البناء؛ وP1090 على النصّ الجديد.
- والتشغيلُ الثالث (`natija_3.json`) بعد ذلك، بالأعداد نفسِها.

## ٥. ما رآه البنّاءُ قبل دفع الشفرة

في `tawjih_muallif.md`. ولم يقرأ البنّاءُ الحالاتِ ولا `taalif.md` قبل `b39dc59` (التشغيلُ الأوّل).
