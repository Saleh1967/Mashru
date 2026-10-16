"""شجرةُ الأجناس الأعلى من عناوين المخصّص المختوم — جدولٌ مولَّد بأسطره (مطابَق لا نقل؛ قرار المالك 2026-10-16).

القاعدة المعلَنة (لا تصنيف بكلمات العناوين — م14):
  * «كتاب»: كلُّ عنوانٍ في وسم OpenITI `### |` يبدأ لفظُه بـ«كتاب» بعد إسقاط القوس الافتتاحيّ «(».
  * «باب»: كلُّ عنوانٍ في `### |` يبدأ لفظُه بـ«باب» كذلك.
  * «كتاب-بلا-وسم»: كتبٌ يذكرها النصُّ ختامًا أو تلوًا بلا عنوانٍ موسوم: «تم كتاب X» و«ويتلوه كتاب Y».
المخرج TSV: sinf <tab> satr <tab> unwan — يُكتب إلى stdout.
التشغيل: python3 -I scripts/bina_ajnas_mukhassas.py <mukhassas.txt> > mawsua/ajnas_mukhassas.tsv
"""
import re
import sys


def nazzif(t):
    return re.sub(r"^[\s(]+|[\s).]+$", "", t)


def bina(path):
    out = ["sinf\tsatr\tunwan"]
    for i, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if line.startswith("### |"):
            t = nazzif(line[len("### |"):])
            if t.startswith("كتاب"):
                out.append(f"كتاب\t{i}\t{t}")
            elif t.startswith("باب"):
                out.append(f"باب\t{i}\t{t}")
        for k in re.findall(r"تم كتاب ([^\s،.)]+)", line):
            out.append(f"كتاب-ختام\t{i}\tكتاب {k}")
        for k in re.findall(r"ويتلوه كتاب ([^\s،.)]+)", line):
            out.append(f"كتاب-تالٍ\t{i}\tكتاب {k}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    sys.stdout.write(bina(sys.argv[1]))
