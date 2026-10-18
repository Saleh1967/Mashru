"""عيّنةُ تقدير الدقّة لردّ كلمات التفسير إلى جذورها (القاعدة R2 في `shabaka/jadwal_luzum.py`)، بذرةٌ مختومة.

السحب: مادّةٌ عشوائيّة من مواد اللسان المقبولة، ثمّ جملةٌ عشوائيّة منها، ثمّ تفسيرٌ «W: G» عشوائيّ فيها، ثمّ كلمةٌ عشوائيّة من
كلماته الأولى الثماني لها جذرٌ متعيّن غيرُ جذر المادّة؛ حتّى 80 كلمة. الحكمُ عليها لقائسٍ مستقلٍّ يقرأ النصّ الخامّ وحده.
  البذرة 20261018: عيّنةُ ما قبل إصلاح الواو العاطفة وحروف المعاني (حكمُ القائس: 73/80).
  البذرة 20261019: عيّنةُ ما بعده.
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/ayyina_jadhr.py <البذرة> <ملفّ المخرج>
"""
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as J  # noqa: E402

TAFSIR = re.compile(r"(?:^|[،,\s])((?:[ء-يً-ْ]+ ?){1,2}): ([^:]+?)(?=$|[.؛]| [ء-يً-ْ]+:)")


def main():
    bidhra, makhraj = int(sys.argv[1]), sys.argv[2]
    D = os.environ["MUDAA_DIR"]
    L = open(os.path.join(D, "lisan.txt"), encoding="utf-8").read().split("\n")
    ml = J.mawadd_lisan(L)
    Jd = J.Jadhr(ml)
    random.seed(bidhra)
    out = []
    while len(out) < 80:
        A, _, body = random.choice(ml)
        js = J.jumal(body)
        if not js:
            continue
        _, s, satr_at = random.choice(js)
        mm = list(TAFSIR.finditer(s))
        if not mm:
            continue
        m = random.choice(mm)
        toks = [t for t in J.kalimat(m.group(2))[:8] if len(Jd.mursh(t) - {A}) == 1]
        if not toks:
            continue
        t = random.choice(toks)
        out.append({"n": len(out) + 1, "satr": satr_at(m.start(2)), "madda": A, "kalima": t,
                    "jadhr": next(iter(Jd.mursh(t) - {A})), "bidhra": bidhra})
    json.dump(out, open(makhraj, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(makhraj, len(out))


if __name__ == "__main__":
    main()
