"""يولّد `Madlul/JadwalLuzumData.lean` من luzum_mujam.tsv (مخرج shabaka/jadwal_luzum.py على المودَعين المختومين).

لا يُحرَّر الملفّ المولَّد يدويًّا. الصفوف المختارة (اختيارٌ معلن لا استقراء):
  ١. كلُّ قضيّةٍ بين جذرين من شبكة المالك: كتب درس قلم علم فهم طلب عقل (A وB منها، A ≠ B).
  ٢. كلُّ قضايا مادّة «فهم» (المثالُ العامل للدلالات الثلاث).
  ٣. أصولُ ابن فارس لجذور الشبكة السبعة.
التشغيل: MUDAA_DIR=<مجلّد> python3 -I shabaka/bina_luzum_lean.py
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHABAKA = ["كتب", "درس", "قلم", "علم", "فهم", "طلب", "عقل"]
NAW = {"juz": ".juz", "taraduf": ".taraduf", "luzum": ".luzum", "kharij": ".kharij", "asl": ".asl"}
MUJAM = {"lisan": ".lisan", "maqayis": ".maqayis"}


def ikhtiyar(rows):
    out, seen = [], set()
    for r in rows:
        mujam, a, w, naw, b, satr = r[:6]
        ok = (a in SHABAKA and b in SHABAKA and a != b) or a == "فهم" or (mujam == "maqayis" and naw == "asl" and a in SHABAKA)
        key = (mujam, a, w, naw, b, satr)
        if ok and key not in seen:
            seen.add(key)
            out.append(key)
    return out


def lean_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    D = os.environ.get("MUDAA_DIR")
    if not D:
        sys.exit("MUDAA_DIR غير معيَّن")
    with open(os.path.join(D, "luzum_mujam.tsv"), encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter="\t"))[1:]
    sel = ikhtiyar(rows)
    lines = [
        "/- مولَّدٌ بـ `shabaka/bina_luzum_lean.py` من `luzum_mujam.tsv` (مخرج `shabaka/jadwal_luzum.py` على مقاييس اللغة ولسان العرب",
        "    المختومين). لا يُحرَّر يدويًّا؛ يطابقه `tahaqquq/test_luzum.py`. -/",
        "import Madlul.JadwalLuzumNaw",
        "",
        "namespace JadwalLuzum",
        "",
        f"/-- {len(sel)} صفًّا: (المعجم، جذر المادّة، اللفظ، القضيّة، الجذر الآخر، السطر). -/",
        "def jadwal : List Saff := [",
    ]
    body = [f"  ⟨{MUJAM[m]}, {lean_str(a)}, {lean_str(w)}, {NAW[n]}, {lean_str(b)}, {int(s)}⟩" for m, a, w, n, b, s in sel]
    lines.append(",\n".join(body))
    lines += ["]", "", "end JadwalLuzum", ""]
    p = os.path.join(ROOT, "Madlul", "JadwalLuzumData.lean")
    open(p, "w", encoding="utf-8").write("\n".join(lines))
    print(p, len(sel), "صفًّا")


if __name__ == "__main__":
    main()
