"""اختبارُ فرضيّة تدوير الثلاثيّ في الرباعيّ: النحتُ عند ابن فارس والزيادةُ عند سيبويه، على جذور اللسان.

السند:
  * المقاييس س5274–5283: «اعلم أن للرباعي والخماسي مذهبا في القياس … أن أكثر ما تراه منه منحوت. ومعنى النحت أن تؤخذ كلمتان
    وتنحت منهما كلمة تكون آخذة منهما جميعا بحظ … إن ذلك على ضربين: أحدهما المنحوت … والضرب الآخر [الموضوع] وضعا لا مجال له
    في طرق القياس». وأمثلتُه: بحتر من بتر وحتر (س5289–5292)، بحثر من بحث وبثر (س5294–5297)، بعثق من بعق وبثق (س5298–5302)؛
    وبلعوم «مأخوذ من بلع، إلا أنه زيد عليه ما زيد» (س5285–5288).
  * الكتاب س18540–18564: حروفُ الزوائد العشرة ومواضعُها (`jadwal_luzum.MAWDI`).

المعيار (تعيين البنّاء من أمثلة ابن فارس، N1–N3):
  N1 منحوت: من الإسقاطات الأربعة للرباعيّ abcd (إسقاطُ حرفٍ واحد) ثلاثيّان مختلفان مشهودان جذرين في اللسان — فهما يغطّيان الأربعة.
  N2 مزيد: ثلاثيٌّ واحدٌ مشهود، والحرفُ المسقَط من العشرة في موضعٍ يجيزه سيبويه.
  N3 موضوع: ما سواهما.
  N1-م المنحوتُ معنًى («آخذة منهما جميعا بحظ»): منحوتٌ بـ N1، ولكلٍّ من ثلاثيَّين فيه جارٌ مشترك مع الرباعيّ في شبكة اللزوم
     (جذرٌ في تفسيره أو أصله — luzum_mujam.tsv). خطُّ أساسه: الثلاثيّان مستبدلان بثلاثيَّين عشوائيَّين مشهودين مطابقَي الدرجة.
خطُّ الأساس: الحروفُ نفسُها مبعثرةً داخل كلّ جذرٍ رباعيّ (تبديلٌ عشوائيّ يحفظ حروف الجذر وأعدادها)، 20 تبديلًا بذرة 20261018.
الاسترجاع: الكلمات التي صرّح ابن فارس بنحتها في أبواب «ما جاء على أكثر من ثلاثة أحرف» (عنوانٌ بين قوسين يليه «منحوت»)، يُطلب
لها رباعيٌّ مشهودٌ في اللسان تحمله الكلمة بزوائد مجازة، ثمّ يُسأل: هل هو منحوت بـ N1؟
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/naht.py
"""
import collections
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jadwal_luzum as J  # noqa: E402


def isqatat(q):
    return [(i, q[:i] + q[i + 1:]) for i in range(len(q))]


def sannif(q, T3):
    """N1–N3: (الصنف، الثلاثيّات المشهودة)."""
    mash = [(i, t) for i, t in isqatat(q) if t in T3]
    mukhtalif = sorted({t for _, t in mash})
    if len(mukhtalif) >= 2:
        return "manhut", mukhtalif
    if len(mukhtalif) == 1:
        t = mukhtalif[0]
        if any(J.zawaid_faqat(t, q) for i, tt in mash if tt == t):
            return "mazid", mukhtalif
    return "mawdu", mukhtalif


def tasrih_ibn_faris(M):
    """عناوينُ «(X)» في أبواب «أكثر من ثلاثة أحرف» من المقاييس، تليها في نصّها كلمةُ «منحوت/نحت»: (سطر، الكلمة)."""
    out, fi_bab = [], False
    for i, ln in enumerate(M, 1):
        if ln.startswith("### | [") or ln.startswith("### | باب"):
            fi_bab = "أكثر من ثلاثة" in ln
        if not fi_bab:
            continue
        for m in re.finditer(r"\(([ء-يً-ْ]{4,9})\)", ln):
            ctx = " ".join(M[i - 1:i + 3])
            if re.search(r"منحوت|نحت", ctx):
                out.append((i, J.norm(m.group(1))))
    return out


def jiran(D):
    import csv
    N = collections.defaultdict(set)
    with open(os.path.join(D, "luzum_mujam.tsv"), encoding="utf-8") as f:
        for r in list(csv.reader(f, delimiter="\t"))[1:]:
            if r[3] in ("juz", "taraduf", "asl", "luzum") and r[1] != r[4]:
                N[r[1]].add(r[4])
    return N


def naht_mana(q, comps, N):
    """N1-م: عددُ الثلاثيّات (من comps) التي تشارك الرباعيَّ جارًا؛ منحوتٌ معنًى إن بلغ اثنين."""
    return sum(1 for t in comps if N[q] & N[t])


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    S = J.sijill()
    for f in ("lisan.txt", "maqayis.txt"):
        if J.basma(os.path.join(D, f)) != S[f]["sha256"]:
            sys.exit(f"رُفض {f}: بصمته لا تطابق السجلّ")
    L = open(os.path.join(D, "lisan.txt"), encoding="utf-8").read().split("\n")
    M = open(os.path.join(D, "maqayis.txt"), encoding="utf-8").read().split("\n")
    roots = {r for r, _, _ in J.mawadd_lisan(L)}
    T3 = {r for r in roots if len(r) == 3}
    Q4 = sorted(r for r in roots if len(r) == 4)
    if "--lean" in sys.argv:
        # أمثلةُ ابن فارس بأسطرها (المقاييس س5285–5302)، والثلاثيّاتُ: كلُّ ما في اللسان من إسقاطاتها (لا اختيارَ يدويّ)
        AMTHILA = [("بحتر", 5289, "بتر", "حتر"), ("بحثر", 5294, "بحث", "بثر"), ("بعثق", 5299, "بعق", "بثق"), ("بلعم", 5285, "بلع", "")]
        T3w = sorted({t for q, *_ in AMTHILA for _, t in isqatat(q) if t in T3})
        q_ = lambda x: '"' + x + '"'
        lines = ["/- مولَّدٌ بـ `python3 -I shabaka/naht.py --lean` من اللسان والمقاييس المختومين. لا يُحرَّر يدويًّا. -/", "namespace Naht", "",
                 "/-- ثلاثيّاتُ اللسان المشهودة جذورًا من بين إسقاطات أمثلة ابن فارس الأربعة كلِّها. -/",
                 "def thulathiyyat : List String := [" + ", ".join(q_(t) for t in T3w) + "]", "",
                 "/-- أمثلةُ ابن فارس: (الرباعيّ، سطر المقاييس، الكلمة الأولى، الثانية — فارغةٌ للمزيد). -/",
                 "def amthila : List (String × Nat × String × String) := [" + ", ".join(f"({q_(a)}, {b}, {q_(c)}, {q_(d)})" for a, b, c, d in AMTHILA) + "]",
                 "", "end Naht", ""]
        out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Madlul", "NahtData.lean")
        open(out, "w", encoding="utf-8").write("\n".join(lines))
        print(out, T3w, [r for r in Q4 if r == "بلعم"])
        return
    obs = collections.Counter(sannif(q, T3)[0] for q in Q4)
    print("رباعيّ اللسان:", len(Q4), "| ثلاثيّه:", len(T3), "| المشاهد:", dict(obs),
          "| نسبة المنحوت:", round(obs["manhut"] / len(Q4), 4))
    random.seed(20261018)
    nisab = []
    for _ in range(20):
        c = collections.Counter()
        for q in Q4:
            l = list(q)
            random.shuffle(l)
            c[sannif("".join(l), T3)[0]] += 1
        nisab.append(c["manhut"] / len(Q4))
    print("خطّ الأساس (تبعثُر الحروف داخل الجذر، 20 تبديلًا): نسبة المنحوت من", round(min(nisab), 4), "إلى", round(max(nisab), 4),
          "| المتوسّط", round(sum(nisab) / len(nisab), 4))
    N = jiran(D)
    lahu = [q for q in Q4 if N[q]]
    mana = [q for q in lahu if sannif(q, T3)[0] == "manhut" and naht_mana(q, sannif(q, T3)[1], N) >= 2]
    print("N1-م: رباعيٌّ له جيرانٌ في الشبكة:", len(lahu), "| منحوتٌ معنًى:", len(mana), "| النسبة:", round(len(mana) / len(lahu), 4))
    T3l = sorted(T3, key=lambda t: (len(N[t]), t))
    pos = {t: i for i, t in enumerate(T3l)}
    random.seed(20261018)
    asas = []
    for _ in range(20):
        k = 0
        for q in lahu:
            cls, comps = sannif(q, T3)
            if cls != "manhut":
                continue
            rnd = [T3l[random.randint(max(0, pos[t] - 50), min(len(T3l) - 1, pos[t] + 50))] for t in comps]
            k += naht_mana(q, rnd, N) >= 2
        asas.append(k / len(lahu))
    print("خطّ أساس N1-م (ثلاثيّات عشوائيّة مطابَقة الدرجة، 20 سحبة): من", round(min(asas), 4), "إلى", round(max(asas), 4),
          "| المتوسّط", round(sum(asas) / len(asas), 4))
    tas = tasrih_ibn_faris(M)
    hit, miss, la = [], [], []
    for satr, w in tas:
        qs = [q for q in Q4 if J.zawaid_faqat(q, w)]
        if not qs:
            la.append((satr, w))
            continue
        cls = [(q,) + sannif(q, T3) for q in qs]
        (hit if any(c[1] == "manhut" for c in cls) else miss).append((satr, w, cls))
    hit_m = [x for x in hit if any(c[1] == "manhut" and naht_mana(c[0], c[2], N) >= 2 for c in x[2])]
    print("استرجاع N1-م على تصريح ابن فارس:", f"{len(hit_m)}/{len(hit) + len(miss)}")
    for x in hit_m[:5]:
        print("  منحوتٌ معنًى:", x[:2], [(c[0], [t for t in c[2] if N[c[0]] & N[t]]) for c in x[2]])
    print("تصريحُ ابن فارس بالنحت:", len(tas), "| لها رباعيٌّ في اللسان:", len(hit) + len(miss), "| بلا رباعيّ:", len(la),
          "| الاسترجاع:", f"{len(hit)}/{len(hit) + len(miss)}")
    for x in hit[:6]:
        print("  منحوت:", x)
    for x in miss[:12]:
        print("  فاته:", x)


if __name__ == "__main__":
    main()
