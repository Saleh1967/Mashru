"""هيكلُ الإنتروبيا على الشيفرة، وجدولُ المعرفة المنظَّمة (Jisr/Intrubiya.lean، Jisr/IntrubiyaShahada.lean).

ثلاثُ طبقاتٍ على فضاء الخلايا نفسِه، والمعرفةُ هي الفرقُ بينها:
  ٠ الشيفرة:  log2 116 بتّ/خلية = log2 29 (الحامل) + 2 (الحالة)؛ والعنوان تقابليّ (مبرهن).
  ١ القانون:  عددُ كلمات كلّ طول بالضبط (= `lawCount` في Lean)، ومعدّلُ نموّه log2 ρ، وحدّاه المبرهنان من شهادة
              `IntrubiyaShahada`؛ والسعةُ لكلّ حالة log2 |الحيّ|.
  ٢ الاستعمال: انتقالاتُ كلماتٍ يرخّصها تحصيلُ Mashru (الأداة `tahsil`، Dal/Tahsil.lean) على حالات القانون نفسِه، بعد نقل خلاياها بالجسر
              المبرهن (جدولُ `nabtBridge`: Jisr/NabtExport.lean). والقارئُ الصارم في NABT (`parse_word`) يُعدّ معه قبلَه وبعدَه.

وجدولُ المعرفة: (حالة × خلية) = 96 × 116 خانة، بأربع خانات ومرتبةٍ لكلّ خانة (الدستور م15–16):
  ممتنع_بالقانون  ← من حيث هي (القانون المودَع وحده)
  مرخَّص_مشهود   ← معلومة (تردّدٌ في مودَع؛ التكرارُ لا يرفعها إلى مفهوم)
  مرخَّص_غير_مشهود ← لا حكم (الغيابُ ليس امتناعًا)
  تعارض           ← لا حكم، يُعرض بأمثلته (يردّه القانون ويشهد له المودَع)
ولا «مفهوم» من هذا الهيكل: لا شاهدَ واقعٍ مختوم مربوط.

المقدِّرات: plug-in، وMiller–Madow (H + (K−1)/(2N ln 2))، وفترةُ ثقةٍ بإعادة المعاينة على الكلمات (بذرةٌ ثابتة).
والعيّنةُ ما رخّصه التحصيلُ كلَّه من كلمات المودَع؛ والمعلَّقُ يُعدّ باسم قاعدته ولا يُخمَّن.

الاستعمال:
  python3 -I scripts/intrubiya.py --mudaa <نصّ> --basma <sha256> [--khuruj <مجلّد>]
  python3 -I scripts/intrubiya.py ... --check <مجلّد>   يعيد البناء ويطابق المخرج المحفوظ بالبايت
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

JADHR = Path(__file__).resolve().parent.parent
LAW = JADHR / "jadawil" / "law.json"   # مولَّدٌ من Nabt.Law في Mashru (`lake exe qanunJadwal`)
LAW_SHA256 = "14e32ae208ac5ed2f754e83506e72133d0962756ef0c944d12370746febddcdd"
TAHSIL = JADHR / ".lake" / "build" / "bin" / "tahsil"
NABT_BRIDGE = JADHR / ".lake" / "build" / "bin" / "nabtBridge"
DEAD = 96
N_ATOMS = 116
CARRIERS = "ابتثجحخدذرزسشصضطظعغفقكلمنهويء"       # ترتيب NABT (Nabt/Cell.lean)
HARAKAT = ("َ", "ُ", "ِ", "ْ")
MARKS = ("فتحة", "ضمّة", "كسرة", "سكون")
# fromSlgeCarrier من Nabt/Law.lean بنصّه: فهرسُ SLGE ← فهرسُ NABT
FROM_SLGE = [28, 25, 0, 17, 5, 18, 6, 20, 21, 4, 12, 27, 14, 22, 24, 9, 15, 7, 2, 10, 11,
             13, 16, 8, 3, 19, 1, 23, 26]
BADHRA = 20261028
B_IADA = 200


def basma(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def H(counter) -> float:
    n = sum(counter.values())
    return -sum(c / n * math.log2(c / n) for c in counter.values() if c) if n else 0.0


def H_mm(counter) -> float:
    """Miller–Madow: H + (K − 1)/(2 N ln 2)، وK عددُ ما شوهد."""
    n = sum(counter.values())
    k = sum(1 for c in counter.values() if c)
    return H(counter) + ((k - 1) / (2 * n * math.log(2)) if n else 0.0)


def rasm(atom: int) -> str:
    return CARRIERS[atom // 4] + HARAKAT[atom % 4]


# ───────────────────────── الطبقة ١ ─────────────────────────

class Qanun:
    def __init__(self, path: Path = LAW):
        if basma(path) != LAW_SHA256:
            raise SystemExit(f"LAW_SHA_MISMATCH {basma(path)}")
        d = json.loads(path.read_text(encoding="utf-8"))
        self.Q = d["state_count"]
        self.step = [[t[0] for t in row] for row in d["transitions"]]
        self.final = {False: d["final_waqf"], True: d["final_wasl"]}
        self.start = d["start_state"]
        assert self.Q == 97 and all(len(r) == N_ATOMS for r in self.step)

    def adad(self, wasl: bool, nmax: int) -> list[int]:
        v = [1 if self.final[wasl][q] else 0 for q in range(self.Q)]
        out = [v[self.start]]
        for _ in range(nmax):
            v = [sum(v[self.step[q][a]] for a in range(N_ATOMS)) for q in range(self.Q)]
            out.append(v[self.start])
        return out

    def hayy(self, q: int) -> list[int]:
        return [a for a in range(N_ATOMS) if self.step[q][a] != DEAD]

    def rho(self, iters: int = 400) -> float:
        live = [q for q in range(self.Q) if q != DEAD]
        x = {q: 1.0 for q in live}
        lam = 0.0
        for _ in range(iters):
            y = {q: sum(x[self.step[q][a]] for a in range(N_ATOMS) if self.step[q][a] != DEAD)
                 for q in live}
            lam = max(y.values())
            x = {q: y[q] / lam for q in live}
        return lam


def wasf_hala(q: int) -> str:
    """وصفُ الحالة بمواضعها في rawStep (Nabt/Law.lean) كما كُتبت؛ التسميةُ قراءةُ البنّاء، بلا دعوى صوتيّة."""
    c = lambda s: CARRIERS[FROM_SLGE[s]]
    if q == 0:
        return "البداية"
    if 1 <= q <= 3:
        return f"بعد حركةٍ قصيرة ({MARKS[q - 1]})"
    if q == 4:
        return "بعد مدّ (سكونُ حرف المدّ الموافق)"
    if 6 <= q <= 34:
        return f"بعد مدٍّ ثمّ ساكن «{c(q - 6)}»"
    if q == 35:
        return "بعد ساكنين (من المقطع المغلق)"
    if q == 36:
        return "بعد ساكنٍ ثانٍ بعد المدّ"
    if q == 37:
        return "بعد حدّ الكلمة 116"
    if 38 <= q <= 66:
        return f"بعد حدٍّ عقيبَ مدٍّ وساكن «{c(q - 38)}»"
    if 67 <= q <= 95:
        return f"مقطعٌ مغلق بساكن «{c(q - 67)}»"
    return "لا يبلغها rawStep باسم"


# ───────────────────────── الجسر والقارئان ─────────────────────────

def jadwal_naql() -> dict[int, int]:
    """رقمُ خلية Mashru (`Dal.n`) ← ذرّةُ NABT، من منفذ Lean `nabtBridge` نفسِه."""
    out = subprocess.run([str(NABT_BRIDGE)], capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    rows = d["cells"] if isinstance(d, dict) and "cells" in d else d
    t = {r["mashru_atom"]: r["nabt_atom"] for r in rows}
    if sorted(t) != list(range(N_ATOMS)) or sorted(t.values()) != list(range(N_ATOMS)):
        raise SystemExit("NAQL_NOT_BIJECTIVE")
    return t


def qari_tahsil(suwar: list[str]) -> tuple[dict[str, tuple[int, ...]], dict[str, list[str]]]:
    """كلُّ صورةٍ ← خلاياها (Mashru) إن رخّصها التحصيلُ كلَّها، وإلّا أسماءُ ما علّقها أو أفسدها."""
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8") as f:
        for i, s in enumerate(suwar):
            f.write(f"{i}\t{' '.join(str(ord(c)) for c in s)}\n")
        p = f.name
    out = subprocess.run([str(TAHSIL), p], capture_output=True, text=True, check=True).stdout
    Path(p).unlink()
    murakhkhas, asbab = {}, defaultdict(list)
    for line in out.splitlines():
        f = line.split("\t")
        k = int(f[0])
        if f[1] == "M" and f[5] in ("P", "F"):
            asbab[suwar[k]].append(f"{f[5]}:{f[7]}")
        elif f[1] == "K" and f[4] == "1":
            murakhkhas[suwar[k]] = tuple(int(x) for x in f[5].split(",")) if f[5] else ()
    return murakhkhas, asbab


def qari_nabt(suwar: list[str]):
    """قارئُ NABT الصارم (`parse_word`) منقولًا إلى Mashru (`scripts/abjad_nabt.py`، من sonaiso/NABT@3dbe335 بنصّه): لا يُستورد NABT ولا
    يُشغَّل من لقطةٍ مضمَّنة."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("abjad_nabt", JADHR / "scripts" / "abjad_nabt.py")
    abjad_nabt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(abjad_nabt)
    ok, asbab = {}, {}
    for s in suwar:
        try:
            ok[s] = tuple(abjad_nabt.parse_word(s))
        except abjad_nabt.NabtError as e:
            asbab[s] = e.status + ":" + e.code
    return ok, asbab


# ───────────────────────── البناء ─────────────────────────

def intiqalat(qanun: Qanun, kalimat: list[tuple[int, ...]]):
    trans = defaultdict(Counter)
    taarud = Counter()
    amthila = defaultdict(list)
    murakhkhas_waqf = 0
    for w in kalimat:
        q = qanun.start
        for a in w:
            if q == DEAD:
                break
            nxt = qanun.step[q][a]
            if nxt == DEAD:
                taarud[(q, a)] += 1
                r = "".join(rasm(x) for x in w)
                if r not in amthila[(q, a)] and len(amthila[(q, a)]) < 5:
                    amthila[(q, a)].append(r)
            else:
                trans[q][a] += 1
            q = nxt
        if q != DEAD and qanun.final[False][q]:
            murakhkhas_waqf += 1
    return trans, taarud, amthila, murakhkhas_waqf


def maqadir(qanun: Qanun, trans, sicaq_hayy) -> dict:
    n = sum(sum(c.values()) for c in trans.values())
    if not n:
        return {"H_tali_bihala": 0.0, "H_tali_bihala_MM": 0.0, "sia_alhalat": 0.0, "marifa": 0.0, "marifa_MM": 0.0}
    w = {q: sum(c.values()) / n for q, c in trans.items()}
    h = sum(w[q] * H(c) for q, c in trans.items())
    hmm = sum(w[q] * H_mm(c) for q, c in trans.items())
    cap = sum(w[q] * math.log2(sicaq_hayy[q]) for q in trans)
    return {"H_tali_bihala": h, "H_tali_bihala_MM": hmm, "sia_alhalat": cap,
            "marifa": cap - h, "marifa_MM": cap - hmm}


def bina(qanun: Qanun, rumuz: list[str], tahsil_m: dict, tahsil_asbab: dict,
         nabt_m: dict, nabt_asbab: dict, naql: dict[int, int], nmax: int = 12) -> dict:
    L0 = {"bitat_lil_khaliya": math.log2(N_ATOMS), "bitat_alhamil": math.log2(29), "bitat_alhala": 2.0}

    waqf, wasl = qanun.adad(False, nmax), qanun.adad(True, nmax)
    rho = qanun.rho()
    sia = {q: len(qanun.hayy(q)) for q in range(qanun.Q) if q != DEAD}
    L1 = {"adad_waqf": [str(x) for x in waqf], "adad_wasl": [str(x) for x in wasl],
          "log2_nisbat_alnumuw": [math.log2(waqf[n + 1] / waqf[n]) for n in range(1, nmax)],
          "rho": rho, "intrubiya_tubulujiyya": math.log2(rho),
          "ma_yahdhifuhu_alqanun": math.log2(N_ATOMS) - math.log2(rho)}

    # الكلماتُ بتردّدها، والخلايا منقولةً إلى NABT بالجسر
    tik = Counter(rumuz)
    kalimat_t = []                         # (خلايا NABT) لكلّ رمزٍ رخّصه التحصيل
    for s, c in tik.items():
        if s in tahsil_m:
            kalimat_t.extend([tuple(naql[x] for x in tahsil_m[s])] * c)
    kalimat_n = []
    for s, c in tik.items():
        if s in nabt_m:
            kalimat_n.extend([tuple(nabt_m[s])] * c)

    asbab_t = Counter()
    for s, c in tik.items():
        if s not in tahsil_m:
            for r in dict.fromkeys(tahsil_asbab.get(s, ["?:بلا سبب مطبوع"])):
                asbab_t[r] += c
    asbab_n = Counter()
    for s, c in tik.items():
        if s in nabt_asbab:
            asbab_n[nabt_asbab[s]] += c

    def tabaqa2(kalimat):
        trans, taarud, amthila, rw = intiqalat(qanun, kalimat)
        cell, car, mark, joint = Counter(), Counter(), Counter(), Counter()
        for w in kalimat:
            for a in w:
                cell[a] += 1; car[a // 4] += 1; mark[a % 4] += 1; joint[(a // 4, a % 4)] += 1
        m = maqadir(qanun, trans, sia)
        m.update({"kalimat": len(kalimat), "murakhkhasa_waqfan": rw, "yarudduha_alqanun": len(kalimat) - rw,
                  "H_khaliya": H(cell), "H_hamil": H(car), "H_hala": H(mark),
                  "H_hala_bihamil": H(joint) - H(car), "I_hamil_hala": H(car) + H(mark) - H(joint),
                  "ahdath": sum(sum(c.values()) for c in trans.values()),
                  "halat_muzara": sorted(trans)})
        return m, trans, taarud, amthila

    L2_t, trans, taarud, amthila = tabaqa2(kalimat_t)
    L2_n, _, _, _ = tabaqa2(kalimat_n)

    # فترةُ الثقة بإعادة المعاينة على الكلمات
    rnd = random.Random(BADHRA)
    sams = []
    for _ in range(B_IADA):
        samp = [kalimat_t[rnd.randrange(len(kalimat_t))] for _ in range(len(kalimat_t))] if kalimat_t else []
        tr, _, _, _ = intiqalat(qanun, samp)
        sams.append(maqadir(qanun, tr, sia)["marifa_MM"])
    sams.sort()
    L2_t["marifa_MM_95"] = [sams[int(0.025 * B_IADA)], sams[int(0.975 * B_IADA) - 1]] if sams else None

    suwar = set(rumuz)
    L2_mudaa = {"rumuz": len(rumuz), "suwar": len(suwar),
                "suwar_bila_sel_wa_bihi_harf": len({w for w in suwar if w != "<sel>" and any("ء" <= c <= "ي" for c in w)}),
                "tahsil": {"rumuz_murakhkhasa": len(kalimat_t),
                           "rumuz_ghayr_murakhkhasa": sum(c for s, c in tik.items() if s not in tahsil_m),
                           "suwar_murakhkhasa": sum(1 for s in suwar if s in tahsil_m),
                           "muallaq_wa_fasid": dict(asbab_t.most_common())},
                "nabt_sarim": {"rumuz_maqbula": len(kalimat_n), "suwar_maqbula": sum(1 for s in suwar if s in nabt_m),
                               "muajjal": dict(asbab_n.most_common())}}

    # جدولُ المعرفة
    halat, taarudat = [], []
    for q in range(qanun.Q):
        if q == DEAD:
            continue
        hayy = set(qanun.hayy(q))
        seen = trans.get(q, Counter())
        cats = Counter()
        for a in range(N_ATOMS):
            if a in hayy:
                cat = "مرخَّص_مشهود" if seen[a] else "مرخَّص_غير_مشهود"
            else:
                cat = "تعارض" if taarud[(q, a)] else "ممتنع_بالقانون"
            cats[cat] += 1
            if cat == "تعارض":
                taarudat.append({"hala": q, "khaliya": a, "rasm": rasm(a), "adad": taarud[(q, a)],
                                 "amthila": amthila[(q, a)]})
        n = sum(seen.values())
        aala = [{"khaliya": a, "rasm": rasm(a), "adad": c, "pmi": math.log2((c / n) * len(hayy))}
                for a, c in seen.most_common(5)] if n else []
        halat.append({"hala": q, "wasf": wasf_hala(q), "hayy": len(hayy),
                      "sia": math.log2(len(hayy)) if hayy else None, "ahdath": n,
                      "H": H(seen) if n else None, "H_MM": H_mm(seen) if n else None,
                      "marifa_MM": (math.log2(len(hayy)) - H_mm(seen)) if n and hayy else None,
                      "khanat": dict(sorted(cats.items())), "aala": aala})
    maratib = {"ممتنع_بالقانون": "من حيث هي", "مرخَّص_مشهود": "معلومة",
               "مرخَّص_غير_مشهود": "لا حكم", "تعارض": "لا حكم"}
    return {"tabaqa0": L0, "tabaqa1": L1, "mudaa": L2_mudaa,
            "tabaqa2_tahsil": L2_t, "tabaqa2_nabt_sarim": L2_n,
            "maratib": maratib, "halat": halat, "taarudat": taarudat, "mafhum": 0}


def taqrir(r: dict, meta: dict) -> str:
    L0, L1, M, T, N = r["tabaqa0"], r["tabaqa1"], r["mudaa"], r["tabaqa2_tahsil"], r["tabaqa2_nabt_sarim"]
    tot = Counter()
    for s in r["halat"]:
        tot.update(s["khanat"])
    L = ["# تقرير هيكل الإنتروبيا (scripts/intrubiya.py)", "",
         f"- القانون `law.json` sha256 `{LAW_SHA256}`",
         f"- المودَع `{meta['mudaa']}` sha256 `{meta['basma']}`", "",
         "## الطبقة ٠ — الشيفرة",
         f"- {L0['bitat_lil_khaliya']:.4f} بتّ/خلية = {L0['bitat_alhamil']:.4f} (الحامل) + 2 (الحالة).", "",
         "## الطبقة ١ — القانون (العددُ مبرهنٌ حتى 4 ومطابَقٌ لـ`lawCount` حتى 12)",
         "| n | وقف | وصل |", "|---|---|---|"]
    for n, (a, b) in enumerate(zip(L1["adad_waqf"], L1["adad_wasl"])):
        L.append(f"| {n} | {a} | {b} |")
    L += ["", f"- ρ ≈ {L1['rho']:.4f}؛ log2 ρ = {L1['intrubiya_tubulujiyya']:.4f} بتّ/خلية (والحدّان المبرهنان في "
          "`Jisr/IntrubiyaShahada.lean`)؛ ما يحذفه القانون من الشيفرة "
          f"{L1['ma_yahdhifuhu_alqanun']:.4f} بتّ/خلية.", "",
          "## المودَع والقارئان (قبلُ وبعدُ على المودَع نفسِه)",
          f"- الرموز {M['rumuz']}، والصور {M['suwar']} ({M['suwar_bila_sel_wa_bihi_harf']} بلا «<sel>» وفيها حرف).",
          f"- قارئ NABT الصارم: يقبل {M['nabt_sarim']['rumuz_maqbula']} رمزًا ({M['nabt_sarim']['suwar_maqbula']} صورة)؛ "
          f"المؤجَّل {M['nabt_sarim']['muajjal']}",
          f"- تحصيل Mashru: يرخّص {M['tahsil']['rumuz_murakhkhasa']} رمزًا ({M['tahsil']['suwar_murakhkhasa']} صورة)؛ "
          "وأسبابُ ما لم يُرخَّص (رمزٌ يُعدّ في كلّ سببٍ فيه):", "",
          "| السبب | الرموز |", "|---|---|"]
    for k, v in list(M["tahsil"]["muallaq_wa_fasid"].items())[:20]:
        L.append(f"| {k} | {v} |")
    L += ["", "## الطبقة ٢ — الاستعمال (تقدير على عيّنة)",
          "| المقدار | التحصيل | NABT الصارم |", "|---|---|---|"]
    for k in ("kalimat", "murakhkhasa_waqfan", "yarudduha_alqanun", "ahdath", "H_khaliya", "H_hamil", "H_hala",
              "H_hala_bihamil", "I_hamil_hala", "H_tali_bihala", "H_tali_bihala_MM", "sia_alhalat", "marifa", "marifa_MM"):
        a, b = T[k], N[k]
        f = (lambda x: f"{x:.4f}") if isinstance(a, float) else str
        L.append(f"| {k} | {f(a)} | {f(b)} |")
    L += [f"| الحالاتُ المزورة | {len(T['halat_muzara'])} | {len(N['halat_muzara'])} |",
          f"| فترة 95% لـmarifa_MM (إعادة معاينة، البذرة {BADHRA}، {B_IADA}) | "
          f"{T['marifa_MM_95'][0]:.4f}–{T['marifa_MM_95'][1]:.4f} | — |", "",
          "## جدول المعرفة (حالة × خلية = 96 × 116)", "| الخانة | العدد | المرتبة |", "|---|---|---|"]
    for k, g in r["maratib"].items():
        L.append(f"| {k} | {tot[k]} | {g} |")
    L += ["", f"- «مفهوم»: {r['mafhum']}.", "",
          "### الحالاتُ الأغنى معرفةً (≥ 100 حدث؛ سعةُ القانون − H_MM)",
          "| الحالة | الوصف | حيّ | أحداث | معرفة | الأكثر |", "|---|---|---|---|---|---|"]
    rk = sorted((s for s in r["halat"] if s["marifa_MM"] is not None and s["ahdath"] >= 100), key=lambda s: -s["marifa_MM"])
    for s in rk[:15]:
        L.append(f"| {s['hala']} | {s['wasf']} | {s['hayy']} | {s['ahdath']} | {s['marifa_MM']:.3f} | "
                 + " ".join(f"{t['rasm']}({t['adad']})" for t in s["aala"][:3]) + " |")
    if r["taarudat"]:
        L += ["", "### التعارضات (يردّها القانون ويشهد لها المودَع)", "| الحالة | الخلية | العدد | أمثلة |", "|---|---|---|---|"]
        for t in sorted(r["taarudat"], key=lambda t: (-t["adad"], t["hala"], t["khaliya"]))[:25]:
            L.append(f"| {t['hala']} ({wasf_hala(t['hala'])}) | {t['rasm']} | {t['adad']} | {'، '.join(t['amthila'][:3])} |")
    return "\n".join(L) + "\n"


def tashghil(mudaa: Path, basma_mutawaqqaa: str) -> tuple[dict, str]:
    if basma(mudaa) != basma_mutawaqqaa:
        raise SystemExit(f"MUDAA_SHA_MISMATCH {basma(mudaa)}")
    rumuz = mudaa.read_text(encoding="utf-8").split()
    suwar = sorted(set(rumuz))
    qanun = Qanun()
    naql = jadwal_naql()
    tm, ta = qari_tahsil(suwar)
    nm, na = qari_nabt(suwar)
    r = bina(qanun, rumuz, tm, ta, nm, na, naql)
    meta = {"mudaa": mudaa.name, "basma": basma_mutawaqqaa}
    r["meta"] = meta
    return r, taqrir(r, meta)


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--mudaa", required=True, type=Path)
    p.add_argument("--basma", required=True)
    p.add_argument("--khuruj", type=Path)
    p.add_argument("--check", type=Path)
    a = p.parse_args(argv)
    r, md = tashghil(a.mudaa, a.basma)
    js = json.dumps(r, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if a.check:
        old_js = (a.check / "intrubiya.json").read_text(encoding="utf-8")
        old_md = (a.check / "intrubiya.md").read_text(encoding="utf-8")
        ok = old_js == js and old_md == md
        print("CHECK_OK" if ok else "CHECK_DIFF")
        sys.exit(0 if ok else 1)
    out = a.khuruj or Path(".")
    out.mkdir(parents=True, exist_ok=True)
    (out / "intrubiya.json").write_text(js, encoding="utf-8")
    (out / "intrubiya.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
