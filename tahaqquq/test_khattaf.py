"""اختبار خطّاف Stop ببروتوكول Claude Code نفسه، على نسخة مؤقّتة من المشروع (بلا طفرات، لتسريع البوّابة).

البروتوكول (مرجع الخطّافات، code.claude.com/docs/en/hooks): المدخل JSON على stdin فيه stop_hook_active؛
الخروج 2 = حجب التوقّف والسبب على stderr يعود إلى الوكيل؛ الخروج 0 = السماح.
التوقّعات مكتوبة من القواعد المعلنة في qabl_tamm.sh، لا من مخرجه:
  ١. مشروع سليم، stop_hook_active=false → خروج 0، السجلّ: gate=pass.
  ٢. sorry مزروع، stop_hook_active=false → خروج 2، أوّل سطر في stderr «لم تمرّ البوّابة؛ أصلح ثم أعد. المخرج:»،
     وفيه «Tajriba.lean: sorry»؛ السجلّ: block=1.
  ٣. stop_hook_active=true (الوكيل يُكمل بسبب الحجب) → خروج 2، block=2.
  ٤. stop_hook_active=true → الحجب الثالث: خروج 0 (الحارس)، أوّل سطر «البوّابة فشلت ثلاث مرّات. أبلغ المالك …»؛
     ويُمحى العدّاد.
  ٥. بعد إزالة sorry، stop_hook_active=true → خروج 0، gate=pass.
  ٦. مدخل ليس JSON → لا يُعطّل الخطّاف: يعمل كمحاولة جديدة (stop_hook_active=?)، وخروجه بحسب البوّابة.
  ٧. حجبٌ ثمّ محاولة جديدة (stop_hook_active=false) تُعيد العدّ إلى 1 لا 2.
يحتاج: lake على PATH، وMUDAA_MUKHASSAS إن أُريد تشغيل اختبارات الشبكة داخل البوّابة.
التشغيل: python3 -I tahaqquq/test_khattaf.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    tmp = tempfile.mkdtemp()
    proj = os.path.join(tmp, "project")
    shutil.copytree(ROOT, proj, ignore=shutil.ignore_patterns("__pycache__", "mustakshif"))
    open(os.path.join(proj, "tahaqquq", "tafrat.json"), "w").write("[]")
    hooks = os.path.join(proj, ".claude", "hooks")
    for f in (".marrat_alhajb", "sijill_khattaf.log"):
        p = os.path.join(hooks, f)
        if os.path.exists(p):
            os.remove(p)
    env = dict(os.environ, CLAUDE_PROJECT_DIR=proj)
    tajriba = os.path.join(proj, "Aql", "Tajriba.lean")

    def hook(stdin):
        p = subprocess.run([os.path.join(hooks, "qabl_tamm.sh")], input=stdin, capture_output=True, text=True,
                           env=env, cwd=proj, timeout=1800)
        return p.returncode, p.stderr.splitlines()

    def sijill():
        return open(os.path.join(hooks, "sijill_khattaf.log"), encoding="utf-8").read().splitlines()

    ok = 0
    try:
        code, err = hook(json.dumps({"session_id": "t1", "hook_event_name": "Stop", "stop_hook_active": False}))
        assert code == 0 and err == [] and "gate=pass" in sijill()[-1], (code, err)
        ok += 1

        open(tajriba, "w").write("theorem tajriba_khattaf : 1 = 1 := by sorry\n")
        code, err = hook(json.dumps({"session_id": "t2", "hook_event_name": "Stop", "stop_hook_active": False}))
        assert code == 2 and err[0] == "لم تمرّ البوّابة؛ أصلح ثم أعد. المخرج:" and any("Tajriba.lean: sorry" in l for l in err), (code, err)
        assert "block=1 exit=2" in sijill()[-1]
        ok += 1

        code, err = hook(json.dumps({"session_id": "t2", "hook_event_name": "Stop", "stop_hook_active": True}))
        assert code == 2 and "block=2 exit=2" in sijill()[-1], (code, sijill()[-1])
        ok += 1

        code, err = hook(json.dumps({"session_id": "t2", "hook_event_name": "Stop", "stop_hook_active": True}))
        assert code == 0 and err[0].startswith("البوّابة فشلت ثلاث مرّات. أبلغ المالك"), (code, err[:1])
        assert "block=3 exit=0(guard)" in sijill()[-1] and not os.path.exists(os.path.join(hooks, ".marrat_alhajb"))
        ok += 1

        os.remove(tajriba)
        code, err = hook(json.dumps({"session_id": "t2", "hook_event_name": "Stop", "stop_hook_active": True}))
        assert code == 0 and err == [] and "gate=pass" in sijill()[-1], (code, err)
        ok += 1

        code, err = hook("ليس json")
        assert code == 0 and "stop_hook_active=? " in sijill()[-1], (code, sijill()[-1])
        ok += 1

        open(tajriba, "w").write("theorem tajriba_khattaf : 1 = 1 := by sorry\n")
        code, _ = hook(json.dumps({"session_id": "t3", "hook_event_name": "Stop", "stop_hook_active": False}))
        assert code == 2 and "block=1" in sijill()[-1]
        code, _ = hook(json.dumps({"session_id": "t4", "hook_event_name": "Stop", "stop_hook_active": False}))
        assert code == 2 and "block=1" in sijill()[-1], sijill()[-1]
        ok += 1
    finally:
        shutil.rmtree(tmp)
    print(f"{ok}/7")


if __name__ == "__main__":
    main()
