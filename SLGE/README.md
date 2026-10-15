# SLGE — قانون الدالّ وحده (الابتداء/الوصل/الوقف، المقطع، الجذر)

هذه الملفّات السبعة **من مرفق المالك slge-closed.zip** (بصمته b773980b3c66ce05b44034626af90bf4aa4cd6e50fb088d8c9cd098e6667e1a6)،
منقولةٌ بنصّها بلا تعديل، وبُنيت هنا بـ Lean 4.34.1 وأُدرجت مبرهناتها الرئيسة في Audit.lean:
Core، Ladder، Count، Law، Hamza، Syllable، Root. ما لم يُنقل (Category، Mazid، Ilal، Tarkib، …) ينتظر مرحلته.

الربط بخلايانا في `Dal/Qanun.lean`: ترميزنا `Dal.n` هو `SLGE.cellEnc` بعينه، وجدول مخارجنا `Dal.ahjam` هو
`SLGE.makharijSizes` بعينه، وجدول المدّ واحد — كلّها مبرهنة، فتسري قوانين المالك على خلايانا.
