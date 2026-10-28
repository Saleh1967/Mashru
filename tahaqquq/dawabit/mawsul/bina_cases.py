"""يبني cases.json من bayanat_1.txt وbayanat_2.txt (سطرٌ لكلّ حالة).
الاستعمال: python3 -I bina_cases.py <مجلد العمل> <مجلد المصدرين>
"""
import json, os, sys

KEYS = ["mawsul", "marji", "mawdi", "tashdid", "lugha", "qabl", "mulgha", "sila", "aid", "aid_sima"]
LUGHA = {"غ": "غير_مذكورة", "ط": "طيئ"}
QABL = {"-": "غيرهما", "ما": "ما_الاستفهامية", "من": "من_الاستفهامية"}
BOOL = {"T": True, "F": False}
MASDAR = {"Q": ("قطر", "qatr.txt"), "A": ("ألفية", "alfiyya.txt")}


def strip_prefix(line):
    for p in ("### | ", "~~", "# "):
        if line.startswith(p):
            return line[len(p):]
    return line


def build():
    wd, src = sys.argv[1], sys.argv[2]
    lines = {}
    for k, (_, fn) in MASDAR.items():
        with open(os.path.join(src, fn), encoding="utf-8") as f:
            lines[k] = f.read().split("\n")
    rows = []
    for fn in ("bayanat_1.txt", "bayanat_2.txt"):
        with open(os.path.join(wd, fn), encoding="utf-8") as f:
            for ln in f:
                ln = ln.rstrip("\n")
                if ln.strip():
                    parts = ln.split("|")
                    if len(parts) != 9:
                        raise SystemExit("حقول غير تسعة: " + ln[:40])
                    rows.append(parts)
    ids = {r[0]: "M%02d" % (i + 1) for i, r in enumerate(rows)}
    out = []
    for pid, fia, mithal, dak, hukm, daraja, zawj, sanad, taliq in rows:
        vals = dak.split(",")
        if len(vals) != 10:
            raise SystemExit("dakhil: " + pid)
        d = dict(zip(KEYS, vals))
        d["tashdid"] = BOOL[d["tashdid"]]
        d["mulgha"] = BOOL[d["mulgha"]]
        d["lugha"] = LUGHA[d["lugha"]]
        d["qabl"] = QABL[d["qabl"]]
        h = hukm.split("+") if "+" in hukm else hukm
        dr = daraja.split("+") if "+" in daraja else daraja
        sn = []
        full = []
        if sanad:
            for piece in sanad.split(";"):
                code, nass = piece.split(":", 1)
                m, satr = code[0], int(code[1:])
                sn.append({"masdar": MASDAR[m][0], "satr": satr, "nass": nass})
                full.append(strip_prefix(lines[m][satr - 1]))
        harfi = any(mithal in t for t in full)
        out.append({
            "id": ids[pid], "fia": fia, "mithal": mithal, "mithal_harfi": harfi,
            "dakhil": d, "hukm": h, "daraja": dr,
            "zawj": None if zawj == "-" else ids[zawj],
            "sanad": sn, "taliq": taliq,
        })
    with open(os.path.join(wd, "cases.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(len(out))


if __name__ == "__main__":
    build()
