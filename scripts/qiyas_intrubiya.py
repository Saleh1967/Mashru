"""القياسُ المسجَّل لهيكل الإنتروبيا على شطرٍ محجوب (hawkama/tasjil_qiyas_intrubiya.md؛ النصُّ حاكمٌ على هذا السكربت).

الحراسات قبل أيّ قراءة: بصمةُ وثيقة التسجيل، وبصماتُ الملفّات المسمّاة فيها (هذا السكربت، وscripts/intrubiya.py، وDal/Tahsil.lean،
وQari/Tahsil.lean، وlaw.json)، وبصمةُ المودَع، وبصمةُ قائمة الشطر المحجوب؛ وأيُّ اختلافٍ يوقف التشغيل باسمه قبل حساب شيء.

الطريقة (بنصّ التسجيل §٣): الآياتُ أسطرُ المودَع؛ الشطرُ المحجوب B عيّنةٌ من 3118 سطرًا بـ random.Random(20261029)، والباقي A.
لكلّ شطر: الصورُ يرخّصها التحصيلُ كلّها (`tahsil`)، منقولةً بالجسر (`nabtBridge`)، وانتقالاتُها على حالات القانون (`intrubiya.intiqalat`).
جدولُ A لكلّ حالة: تكراراتُ الخلايا الحيّة؛ والتوقّعُ على B بتنعيم كريشيفسكي–تروفيموف على الخلايا الحيّة وحدها.

التشغيل: python3 -I scripts/qiyas_intrubiya.py --mudaa <quran-simple-enhanced.txt> --khuruj <ملفّ JSON خارج المستودع>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

JADHR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(JADHR / "scripts"))
import intrubiya as it  # noqa: E402

TASJIL = JADHR / "hawkama" / "tasjil_qiyas_intrubiya.md"
BADHRA = 20261029
HAJM_B = 3118
ALPHA = 0.5


def basma_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def hirasat(mudaa: Path) -> dict:
    """البصماتُ المسجَّلة في وثيقة التسجيل (§٢) تُقرأ منها، ثمّ تُطابق؛ ولا يُحسب شيءٌ قبلها."""
    nass = TASJIL.read_text(encoding="utf-8")
    sijill = dict(re.findall(r"^- `([^`]+)`: `([0-9a-f]{64})`$", nass, flags=re.M))
    matlub = {"scripts/qiyas_intrubiya.py", "scripts/intrubiya.py", "Dal/Tahsil.lean", "Qari/Tahsil.lean",
              "integrations/nabt/src/nabt/data/law.json", "quran-simple-enhanced.txt", "qaimat_B"}
    if set(sijill) != matlub:
        raise SystemExit(f"TASJIL_FIELDS {sorted(set(sijill) ^ matlub)}")
    for rel in matlub - {"quran-simple-enhanced.txt", "qaimat_B"}:
        got = basma_bytes((JADHR / rel).read_bytes())
        if got != sijill[rel]:
            raise SystemExit(f"TASJIL_MISMATCH {rel} {got}")
    if basma_bytes(mudaa.read_bytes()) != sijill["quran-simple-enhanced.txt"]:
        raise SystemExit("MUDAA_SHA_MISMATCH")
    return sijill


def shatr(n_ayat: int) -> list[int]:
    return sorted(random.Random(BADHRA).sample(range(n_ayat), HAJM_B))


def qaimat_basma(b: list[int]) -> str:
    return basma_bytes("\n".join(map(str, b)).encode("ascii"))


def kalimat_shatr(ayat: list[str], tm: dict, naql: dict) -> tuple[list[tuple[int, ...]], int]:
    out, kull = [], 0
    for aya in ayat:
        for s in aya.split():
            kull += 1
            if s in tm:
                out.append(tuple(naql[x] for x in tm[s]))
    return out, kull


def jadwal(qanun, kalimat):
    trans, taarud, _, rw = it.intiqalat(qanun, kalimat)
    return trans, sum(taarud.values()), rw


def maqadir(qanun, kA, kB) -> dict:
    """المقاديرُ بنصّ التسجيل §٣ على كلمات الشطرين (خلايا NABT)."""
    tA, taA, rwA = jadwal(qanun, kA)
    tB, taB, rwB = jadwal(qanun, kB)
    nevA = sum(sum(c.values()) for c in tA.values())
    nevB = sum(sum(c.values()) for c in tB.values())
    H_MM_A = sum(sum(c.values()) / nevA * it.H_mm(c) for c in tA.values())
    ce, cap = 0.0, 0.0
    for q, c in tB.items():
        hayy = set(qanun.hayy(q))
        cA = tA.get(q, Counter())
        NA = sum(cA[x] for x in hayy)
        for x, k in c.items():
            ce += k * -math.log2((cA[x] + ALPHA) / (NA + ALPHA * len(hayy)))
        cap += sum(c.values()) * math.log2(len(hayy))
    return {"kalimat_murakhkhasa": {"A": len(kA), "B": len(kB)}, "ahdath": {"A": nevA, "B": nevB},
            "taarud_ahdath": {"A": taA, "B": taB}, "H_MM_A": H_MM_A, "CE_B": ce / nevB, "cap_B": cap / nevB,
            "rej_A": (len(kA) - rwA) / len(kA), "rej_B": (len(kB) - rwB) / len(kB)}


def hukm_furud(m: dict) -> dict:
    f1 = m["CE_B"] - m["H_MM_A"]
    f2 = m["cap_B"] - m["CE_B"]
    f3 = abs(m["rej_B"] - m["rej_A"])
    return {"F1": {"nass": "CE_B − H_MM_A ≤ 0.10", "qima": f1, "hukm": "صدق" if f1 <= 0.10 else "كذب"},
            "F2": {"nass": "marifa_B = cap_B − CE_B ≥ 1.80", "qima": f2, "hukm": "صدق" if f2 >= 1.80 else "كذب"},
            "F3": {"nass": "|rej_B − rej_A| ≤ 0.01", "qima": f3, "hukm": "صدق" if f3 <= 0.01 else "كذب"}}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--mudaa", required=True, type=Path)
    p.add_argument("--khuruj", required=True, type=Path)
    a = p.parse_args(argv)
    if JADHR in a.khuruj.resolve().parents:
        raise SystemExit("KHURUJ_INSIDE_REPO")
    sijill = hirasat(a.mudaa)
    ayat = a.mudaa.read_text(encoding="utf-8").split("\n")
    if ayat and ayat[-1] == "":
        ayat = ayat[:-1]
    B = shatr(len(ayat))
    if qaimat_basma(B) != sijill["qaimat_B"]:
        raise SystemExit("QAIMAT_B_MISMATCH")
    Bset = set(B)
    ayat_A = [x for i, x in enumerate(ayat) if i not in Bset]
    ayat_B = [ayat[i] for i in B]

    qanun = it.Qanun()
    naql = it.jadwal_naql()
    suwar = sorted({s for x in ayat for s in x.split()})
    tm, _ = it.qari_tahsil(suwar)
    kA, nA = kalimat_shatr(ayat_A, tm, naql)
    kB, nB = kalimat_shatr(ayat_B, tm, naql)
    m = maqadir(qanun, kA, kB)
    furud = hukm_furud(m)
    natija = {"tasjil_sha256": basma_bytes(TASJIL.read_bytes()), "basamat": sijill,
              "ayat": {"A": len(ayat_A), "B": len(ayat_B)}, "rumuz": {"A": nA, "B": nB}, **m, "furud": furud}
    a.khuruj.write_text(json.dumps(natija, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(furud, ensure_ascii=False))


if __name__ == "__main__":
    main()
