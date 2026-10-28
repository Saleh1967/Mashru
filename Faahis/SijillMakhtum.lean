/-
  Faahis/SijillMakhtum.lean — مولَّدٌ بـ `python3 -I scripts/bina_sijill_makhtum.py` من `mudaat/sijill.tsv`؛ لا يُحرَّر يدويًّا.
  أسطرُ سجلّ المودَعات المختوم بنصّها: السلطةُ المعتمدة للفاحص والقارئ (الحزمة P1-ج).
-/

/-- أسطرُ `mudaat/sijill.tsv` بترتيبها. -/
def sijillMakhtum : List String := [
  "mudaa\t936c68e0c2c62ddbfb881c573487c7b37650ef69117bca364c219b6d1bf8e76c\tمعلومات-سابقة\tالمخصص",
  "mudaa\t34fa56710a5b701532a34cb70f8fe440b261e80ae3c40d9667d18b65be7ed86d\tمعلومات-سابقة\tلسان العرب",
  "mudaa\teb756c4c41479451040caedc9aa8fb7fef0f6acd3a4cb47a2a7e8a536a3d6cc7\tمعلومات-سابقة\tتاج العروس",
  "mudaa\t7f71af0dfe056cb84e7da24657fa13edc6e8061ca1980eed7f6c196bd18b5689\tمعلومات-سابقة\tمقاييس اللغة",
  "mudaa\ta160f940bb194e6fe7e6655d2c7f28e41f1fc648c4c5e340cc4e42306d5cb625\tمعلومات-سابقة\tكتاب سيبويه",
  "mudaa\t21be30ec01de89b8a4ba3d7b9023c813aa55034b89a92b0400b77d3f614a5f20\tمعلومات-سابقة\tجدول العوامل المئة (جدول المالك؛ «مئة حسب الجرجاني» بتسميته في الجلسة)",
  "mudaa\t2d9241beca1b138187ace8f6782d5eed68f3864f402ec1d5fc90fdeb306ceb9d\tوضع\tمتن قطر الندى",
  "mudaa\tf37ac2bb4b273f59169053dd0ac2abf50a52846a7e87ddf689ee5c0b87f77e7d\tوضع\tمغني اللبيب",
  "mudaa\t13b351a0a02d9060fdedbb5db568544718eb4e89bef323f5572b8a26c0921ca0\tوضع\tألفية ابن مالك",
  "mudaa\t756890608761e098054af5b7c912ae5078ff3e008820e638d47acf2a759ba64d\tوضع\tالجنى الداني في حروف المعاني",
  "mudaa\tf567d1ab2fe3c0aa90bc6d48abc95136a8d492af35129dee36b84c9659021731\tمعلومات-سابقة\tجدول الأجناس — القطعة الأولى",
  "mudaa\t2e5477cdb1fe501bf934cfbc250e3bd35ebc6e4ba8f6cc0dc3f0ed136b9b9de0\tمعلومات-سابقة\tجدول الأجناس — القطعة الثانية",
  "mudaa\teb761b85c7ce0a9a72b2cebbeb719d3e40fd3d77bae4677035ba3882e5c33b1f\tمعلومات-سابقة\tنظام الفيزياء",
  "mudaa\t478a3dea39cc593cc397ed0699cdf17a160c83b2fb5c667c3d853639cceb2f31\tمعلومات-سابقة\tنظام الرياضيات",
  "mudaa\t0269d2cee8b8032c225c674ac4e85acc22168791137cf71044e7bb3bacadc146\tمعلومات-سابقة\tجدول العلاقات",
  "mudaa\t5e327aa2563af094962833951972b7537a872119a58bbfce5f2a813d20c88e17\tمعلومات-سابقة\tالشخصية الإسلامية ج1",
  "mudaa\t360f7653df4e3396d18153d0ea31e607523d33e0cb552b419340400b2211d5bd\tمعلومات-سابقة\tالشخصية الإسلامية ج3 (أصول الفقه)",
  "mudaa\te917d9a03b1a546d783868d3bc018b24ced19eb85df671bd41e05f50c2de492c\tمعلومات-سابقة\tالتفكير",
  "mudaa\t483cf19f6153cfb31bb6d965e1b7da6927f330633b49c586360f3567798bc161\tمعلومات-سابقة\tسرعة البديهة",
  "mudaa\ta1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46\tمرجع-محجوب\tالمدوّنة القرآنية الصرفية QAC 0.4",
  "mudaa\td43d2a813afbe0490254bb26623d6041ed352a273d333e731ddbcda3bd0b6f3a\tمرجع-محجوب\tMASAQ 2 (مدوّنة القرآن المحلّلة صرفيًّا ونحويًّا)",
  "mudaa\t8841da440bac9bc27544b217e610b045c98ca5d33ebc566832b112b1369fb598\tمعلومات-سابقة\tمرجع المالك: القوانين الأربعة على البرج (A116.Marja)",
  "mudaa\t0e5941ae1d66a2fa907fe6d6373d7e3913f2923abf04a04940c841cb2e598dbf\tمعلومات-سابقة\tجدول القواعد",
  "mudaa\te29bf2a9ef074fb021ce4f0dbcfa42a4e480e7b8e604b39bb664011d2c65dbc4\tواقع-مختوم\tالواقع المختوم — الدفعة الأولى",
  "mudaa\t74cbcf139ae6a3ffd582d79210fd178a722c37057055fc18f8f6de3056f4465c\tوضع\tجدول التعريفات — القطعة الأولى",
  "mudaa\t37633090743d403886b334d12dd911d1994e49767faa9f2be0f01fd48b466c5a\tوضع\tنصّ المصحف (Tanzil، quran-simple-enhanced)"
]
