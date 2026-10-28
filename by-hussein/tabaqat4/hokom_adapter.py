# -*- coding: utf-8 -*-
"""hokom_adapter.py — تقدير Hokom للأداة tabaqat4 (B1).
العقد: def taqdir(surfaces: list[str]) -> list[dict]
  كلّ dict: {pin, word_class, word_class_subclass, final_root, final_wazn, mood, directive, active_residuals}
  قراءةٌ فقط من /Users/husseinhiyassat/hokom بالـpin الحيّ (8a232980) ؛ PYTHONDONTWRITEBYTECODE=1 ؛ لا كاش في شجرته.
  لا رقم ثقة ؛ ما غاب → None مع سببه في active_residuals ؛ لا تخمين ؛ المخرج رتبته «تقدير» تعرضه الأداة ولا تستهلكه.
"""
from __future__ import annotations
import os, subprocess, json

HOKOM = os.environ.get("HOKOM_ROOT", "/Users/husseinhiyassat/hokom")
PIN_DECLARED = "8a232980"

def _hokom_pin() -> str:
    try:
        h = subprocess.run(["git", "-C", HOKOM, "rev-parse", "HEAD"], capture_output=True, text=True, timeout=30).stdout.strip()
        return h[:12] or PIN_DECLARED
    except Exception:
        return PIN_DECLARED

def taqdir(surfaces):
    py = os.path.join(HOKOM, ".venv-taaqol", "bin", "python")
    if not os.path.exists(py):
        raise RuntimeError(f"HOKOM_VENV_ABSENT: لا مفسّر في {py} ؛ Hokom غير متاح للقراءة")
    pin = _hokom_pin()
    keep = ["final_root", "word_class", "word_class_subclass", "final_wazn", "mood", "verdict", "lemma_surface", "active_residuals"]
    code = ("import sys,json;sys.path.insert(0,%r)\nfrom hokom_pipeline import hokom\n"
            "S=%r;out=[]\n"
            "for w in S:\n"
            " try:\n"
            "  r=hokom(w);out.append({k:(list(r[k]) if isinstance(r.get(k),tuple) else r.get(k)) for k in %r})\n"
            " except Exception as e:\n"
            "  out.append({'_error':repr(e)})\n"
            "print(json.dumps(out,ensure_ascii=False))" % (HOKOM, list(surfaces), keep))
    env = dict(os.environ, PYTHONPATH=HOKOM, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([py, "-I", "-c", code], capture_output=True, text=True, timeout=300, env=env)
    if p.returncode != 0:
        raise RuntimeError("HOKOM_RUN_FAILED: " + (p.stderr or p.stdout)[-300:])
    raw = json.loads(p.stdout)
    res = []
    for r in raw:
        if "_error" in r:
            res.append({"pin": pin, "word_class": None, "word_class_subclass": None, "final_root": None,
                        "final_wazn": None, "mood": None, "directive": "REFUSE", "lemma_surface": None,
                        "active_residuals": [r["_error"]]})
            continue
        resid = list(r.get("active_residuals") or [])
        root = r.get("final_root")
        wazn = r.get("final_wazn")
        for name, val in [("final_root", root), ("final_wazn", wazn), ("word_class", r.get("word_class"))]:
            if val is None: resid.append(f"{name}:null")
        res.append({"pin": pin,
                    "word_class": r.get("word_class"),
                    "word_class_subclass": r.get("word_class_subclass"),
                    "final_root": root, "final_wazn": wazn,
                    "mood": r.get("mood"),
                    "directive": r.get("verdict") or "DEFER",
                    "lemma_surface": r.get("lemma_surface"),      # لِيمة Hokom الماضية (للمضارع) ؛ None إن غابت
                    "active_residuals": resid})
    return res

if __name__ == "__main__":
    import sys
    print(json.dumps(taqdir(sys.argv[1:] or ["ذَهَبَ", "الْوَلَدُ"]), ensure_ascii=False, indent=1))
