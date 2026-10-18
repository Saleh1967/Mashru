"""تحويلُ مودَعٍ مختومٍ بصيغة docx إلى نصٍّ بأسطر، تحويلًا حتميًّا لا يُنظِّف شيئًا.

القاعدة: كلُّ فقرةٍ <w:p> في word/document.xml سطرٌ (الفارغةُ سطرٌ فارغ)، ونصُّها وصلُ عناصر <w:t> بترتيبها مع فكّ الكيانات الخمسة؛
والأسطرُ تُوصَل بـ «\\n» بلا سطرٍ أخير. فرقمُ السطر = رقمُ الفقرة في الملفّ. يُرفض الملفّ إن لم تطابق بصمتُه السجلّ.
التشغيل: python3 -I scripts/tahwil_docx.py <ملفّ.docx> <مخرج.txt>
"""
import hashlib
import json
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fakra(p):
    x = zipfile.ZipFile(p).read("word/document.xml").decode("utf-8")
    out = []
    for para in re.findall(r"<w:p[ >].*?</w:p>|<w:p/>", x, flags=re.S):
        t = "".join(re.findall(r"<w:t(?: [^>]*)?>(.*?)</w:t>", para, flags=re.S))
        for a, b in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'"), ("&amp;", "&")):
            t = t.replace(a, b)
        out.append(t)
    return "\n".join(out)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    b = hashlib.sha256(open(src, "rb").read()).hexdigest()
    d = json.load(open(os.path.join(ROOT, "mudaat", "sijill.json"), encoding="utf-8"))["sijill"]
    rec = [v for v in (d.values() if isinstance(d, dict) else d) if v["milaf"] == os.path.basename(src)]
    if not rec or rec[0]["sha256"] != b:
        sys.exit(f"رُفض {src}: بصمته لا تطابق السجلّ")
    t = fakra(src)
    open(dst, "w", encoding="utf-8").write(t)
    print(dst, len(t.split("\n")), "سطرًا", hashlib.sha256(t.encode()).hexdigest())


if __name__ == "__main__":
    main()
