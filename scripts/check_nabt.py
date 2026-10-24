#!/usr/bin/env python3
"""Rebuild and replay Mashru's pinned NABT capabilities, retaining every result.

Full mode runs the unmodified upstream ``make check`` after both Lean builds.
Runtime-only mode still builds its probe prerequisites, but does not claim
export conformance or full parity. Upstream UNMEASURED and documented coverage
limits remain in the generated reports. No skipped unittest suite passes.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "integrations/nabt"
NATIVE_TESTS = ("vendor", "cli", "bridge", "runner")
SAFE_MAKE_PATH = re.compile(r"[A-Za-z0-9_./:+@=-]+\Z")


class CheckFailed(RuntimeError):
    pass


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_make_path(value: str | Path) -> str:
    text = str(value)
    if not SAFE_MAKE_PATH.fullmatch(text):
        raise CheckFailed("NABT_UNSAFE_MAKE_PATH: upstream recipes require paths without shell metacharacters or whitespace")
    return text


def output_directory(path: Path) -> Path:
    destination = path.expanduser().resolve()
    if destination == VENDOR or VENDOR in destination.parents:
        raise CheckFailed("NABT_OUTPUT_INSIDE_SNAPSHOT: choose an output directory outside integrations/nabt")
    # A fresh directory prevents old reports from masquerading as this run.
    destination.mkdir(parents=True, exist_ok=False)
    return destination


def real_directory(path: Path):
    if not stat.S_ISDIR(path.lstat().st_mode) or path.resolve(strict=True) != path:
        raise CheckFailed("NABT_EVIDENCE_PATH_UNSAFE: expected an unlinked directory: " + str(path))


def evidence_parent(*, create: bool = False) -> Path:
    """Only the ignored artifacts/local subtree may contain generated work."""
    current = VENDOR
    real_directory(current)
    for component in ("artifacts", "local"):
        current = current / component
        if create:
            try:
                current.mkdir()
            except FileExistsError:
                pass
        real_directory(current)
    return current


def check_work_directory(work: Path):
    if work.parent != evidence_parent() or not work.name.startswith("mashru-check-"):
        raise CheckFailed("NABT_EVIDENCE_PATH_UNSAFE: work directory escaped artifacts/local")
    real_directory(work)


def fresh_work_directory() -> Path:
    work = Path(tempfile.mkdtemp(prefix="mashru-check-", dir=evidence_parent(create=True)))
    check_work_directory(work)
    (work / "evidence").mkdir()
    return work


def evidence_inventory(root: Path) -> dict:
    """Inventory every regular output, including archives and raw journals."""
    real_directory(root)
    directories, files = [], []

    def walk_error(error):
        raise error

    for folder, children, names in os.walk(root, followlinks=False, onerror=walk_error):
        directory = Path(folder)
        real_directory(directory)
        directories.append(directory.relative_to(root).as_posix())
        for child in children:
            real_directory(directory / child)
        for name in names:
            path = directory / name
            if not stat.S_ISREG(path.lstat().st_mode):
                raise CheckFailed("NABT_EVIDENCE_FILE_UNSAFE: expected a regular output: " + str(path))
            digest, size = sha256(), 0
            with os.fdopen(os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)), "rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            files.append({"path": path.relative_to(root).as_posix(), "bytes": size,
                          "sha256": digest.hexdigest()})
    return {"directories": sorted(directories), "files": sorted(files, key=lambda row: row["path"])}


def retain_evidence(work: Path, output: Path, report: dict):
    relocation = report["evidence_relocation"]
    try:
        check_work_directory(work)
        source, destination = work / "evidence", output / "evidence"
        before = evidence_inventory(source)
        # The destination must also be fresh. Preserve links as links during
        # copying so a changed source cannot make copytree follow an escape;
        # both complete inventories reject links before claiming retention.
        shutil.copytree(source, destination, symlinks=True)
        if evidence_inventory(destination) != before or evidence_inventory(source) != before:
            raise CheckFailed("NABT_EVIDENCE_COPY_MISMATCH: retained output differs from generated evidence")
        relocation.update(status="RETAINED", inventory=before, reports_rewritten=False)
        write_report(output, report)
        check_work_directory(work)
        shutil.rmtree(work)
        relocation["internal_removed"] = True
    except BaseException as error:
        if relocation["status"] != "RETAINED":
            relocation["status"] = "FAILED"
        relocation["error"] = str(error)
        raise
    finally:
        write_report(output, report)


def run_upstream_check(report: dict, output: Path, make: list[str], qac: Path, env: dict):
    work = fresh_work_directory()
    evidence = work / "evidence"
    report["evidence_relocation"] = {
        "schema": "mashru.nabt.evidence-relocation.v1", "status": "PENDING",
        "source_root": str(evidence), "source_relative_to_vendor": evidence.relative_to(VENDOR).as_posix(),
        "retained_root": str(output / "evidence"), "retained_relative_to_output": "evidence",
        "reports_rewritten": False, "internal_removed": False,
        "path_mapping": "Generated absolute or vendor-relative source prefixes map to retained_root; raw report bytes are unchanged",
    }
    write_report(output, report)
    try:
        variables = ["EVIDENCE_DIR=" + safe_make_path(evidence), "QAC_SOURCE=" + safe_make_path(qac),
                     "ARABIC_EVALUATION_DIR=" + str(evidence / "arabic-regression"),
                     "GOVERNOR_EVALUATION_DIR=" + str(evidence / "governor-regression")]
        run_step(report, output, "upstream-check", [*make, *variables, "check"], VENDOR, env, tests=True)
    finally:
        # Failed commands may have produced the only explanation of a failure.
        # Retain those bytes too; failed retention leaves the internal tree.
        retain_evidence(work, output, report)


def test_counts(text: str) -> dict:
    runs = [int(value) for value in re.findall(r"^Ran (\d+) tests? in ", text, re.MULTILINE)]
    skipped = [int(value) for value in re.findall(r"^OK \(skipped=(\d+)\)", text, re.MULTILINE)]
    skip_lines = len(re.findall(r"^.+ \.\.\. skipped [^\n]+$", text, re.MULTILINE))
    return {"unittest_runs": runs, "skipped": max(sum(skipped), skip_lines)}


def write_report(output: Path, report: dict):
    temporary = output / "manifest.json.tmp"
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(output / "manifest.json")


def run_step(report: dict, output: Path, name: str, argv: list[str], cwd: Path,
             env: dict, *, tests: bool = False):
    log = output / (str(len(report["steps"]) + 1).zfill(2) + "-" + name + ".log")
    step = {"name": name, "argv": argv, "cwd": str(cwd), "log": str(log), "started": stamp(), "status": "RUNNING"}
    report["steps"].append(step)
    write_report(output, report)
    print(name + ": " + str(log), flush=True)
    started = time.monotonic()
    try:
        with log.open("xb") as stream:
            result = subprocess.run(argv, cwd=cwd, env=env, stdout=stream, stderr=subprocess.STDOUT, check=False)
        step["returncode"] = result.returncode
        text = log.read_text(encoding="utf-8", errors="replace")
        step.update(test_counts(text))
        step["log_sha256"] = sha256(log.read_bytes()).hexdigest()
        if result.returncode:
            raise CheckFailed("NABT_COMMAND_FAILED: " + name + " exited " + str(result.returncode))
        if step["skipped"]:
            raise CheckFailed("NABT_TESTS_SKIPPED: " + name)
        if tests and not step["unittest_runs"]:
            raise CheckFailed("NABT_TEST_SUMMARY_MISSING: " + name)
        if tests and any(count == 0 for count in step["unittest_runs"]):
            raise CheckFailed("NABT_ZERO_TEST_RUN: " + name)
        step["status"] = "PASSED"
    except BaseException as error:
        step.update(status="FAILED", error=str(error))
        raise
    finally:
        step.update(finished=stamp(), seconds=round(time.monotonic() - started, 3))
        write_report(output, report)


def generated_reports(output: Path) -> list[dict]:
    summaries = []
    retained = {"status", "scope", "gate_pass", "strict_pass", "summary", "counts", "checked",
                "measured", "unmeasured", "passed", "failed", "theorems", "comparisons"}
    for path in sorted((output / "evidence").rglob("*.json")):
        raw = path.read_bytes()
        item = {"path": str(path.relative_to(output)), "bytes": len(raw), "sha256": sha256(raw).hexdigest()}
        try:
            value = json.loads(raw)
            if type(value) is dict:
                item["reported_summary"] = {key: value[key] for key in sorted(retained & value.keys())}
        except (ValueError, UnicodeError):
            item["reported_summary"] = {"status": "UNREADABLE_JSON"}
        summaries.append(item)
    return summaries


def execute(args, output: Path, report: dict):
    resolved_lake = shutil.which(args.lake)
    if not resolved_lake:
        raise CheckFailed("NABT_LAKE_UNAVAILABLE: install the pinned Lean toolchain or supply --lake")
    lake = safe_make_path(Path(resolved_lake).absolute())
    safe_make_path(ROOT)
    safe_make_path(output)
    safe_make_path(sys.executable)
    qac = (args.qac.expanduser().resolve() if args.qac else output / "external/qac-original.txt.gz")
    if qac == VENDOR or VENDOR in qac.parents:
        raise CheckFailed("NABT_QAC_INSIDE_SNAPSHOT: external acquisition must stay outside the pinned source")
    safe_make_path(qac)
    report["qac_source"] = str(qac)
    with tempfile.TemporaryDirectory(prefix="mashru-nabt-check-pyc-") as cache:
        safe_make_path(cache)
        env = dict(os.environ)
        for key in ("MAKEFLAGS", "MFLAGS", "GNUMAKEFLAGS", "MAKEFILES", "PYTHONHOME",
                    "PYTHONOPTIMIZE", "PYTHONINSPECT", "PYTHONSTARTUP", "PYTHONBREAKPOINT",
                    "GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE"):
            env.pop(key, None)
        env.update(PYTHONPATH=str(VENDOR / "src"), PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1",
                   PYTHONPYCACHEPREFIX=cache, LEAN_NUM_THREADS="2")
        for key, executable in (("UNIT_DISCOVERY", "unitDiscoveryProbe"),
                                ("PROGRESSIVE_UNIT", "progressiveUnitProbe"),
                                ("RECURSIVE_BRIDGE", "recursiveBridgeProbe")):
            env["NABT_" + key + "_PROBE"] = str(VENDOR / "formal/.lake/build/bin" / executable)
        python = [sys.executable, "-I", "-B", "-X", "pycache_prefix=" + cache]
        run_step(report, output, "snapshot-before", [*python, str(ROOT / "scripts/check_nabt_vendor.py")], ROOT, env)
        report["snapshot"] = json.loads(Path(report["steps"][-1]["log"]).read_text())
        run_step(report, output, "lean-version", [lake, "env", "lean", "--version"], ROOT, env)
        version = Path(report["steps"][-1]["log"]).read_text()
        if not re.search(r"version 4\.34\.1(?:[, )]|$)", version):
            raise CheckFailed("NABT_TOOLCHAIN_MISMATCH: expected Lean 4.34.1")
        report["lean_version"] = version.strip()
        run_step(report, output, "native-build", [lake, "build", "nabtBridge"], ROOT, env)
        make = ["make", "-j1", "PYTHON=" + sys.executable + " -B -X pycache_prefix=" + cache, "LAKE=" + lake]
        run_step(report, output, "upstream-build", [*make, "formal"], VENDOR, env)
        if args.runtime_only:
            run_step(report, output, "upstream-runtime", [*make, "test"], VENDOR, env, tests=True)
            run_step(report, output, "upstream-integrity", [*python, str(VENDOR / "tools/check_integrity.py")], VENDOR, env)
        else:
            run_step(report, output, "enclosing-revision", ["git", "rev-parse", "--verify", "HEAD"], ROOT, env)
            head = Path(report["steps"][-1]["log"]).read_text().strip()
            if not re.fullmatch(r"[0-9a-f]{40}", head):
                raise CheckFailed("NABT_CHECKOUT_IDENTITY_INVALID: expected the enclosing Mashru Git commit")
            report["provenance"] = {
                "upstream_commit": report["snapshot"]["upstream_commit"],
                "upstream_lock_sha256": report["snapshot"]["lock_sha256"],
                "runtime_git_head": head, "runtime_git_head_scope": "ENCLOSING_MASHRU_CHECKOUT",
                "runtime_git_head_is_upstream_identity": False,
            }
            run_upstream_check(report, output, make, qac, env)
        for name in NATIVE_TESTS:
            run_step(report, output, "native-" + name,
                     [*python, str(ROOT / ("tahaqquq/test_nabt_" + name + ".py"))], ROOT, env, tests=True)
        run_step(report, output, "snapshot-after", [*python, str(ROOT / "scripts/check_nabt_vendor.py")], ROOT, env)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default="lake", help="Executable from the pinned Lean 4.34.1 toolchain")
    parser.add_argument("--output", type=Path, help="Fresh output directory; must be outside the pinned snapshot")
    parser.add_argument("--qac", type=Path, help="External QAC cache; upstream fetcher validates its exact decoded digest")
    parser.add_argument("--runtime-only", action="store_true", help="Build prerequisites and test runtime only; no full parity claim")
    args = parser.parse_args(argv)
    report = {"schema": "mashru.nabt.validation.v1", "status": "RUNNING", "started": stamp(), "steps": [],
              "mode": "runtime-only" if args.runtime_only else "full", "full_parity": False,
              "formal_conformance": "NOT_RUN", "python": sys.version, "platform": platform.platform(),
              "scope": "Pinned implementation replay; upstream unmeasured cases and linguistic limits remain explicit"}
    output = None
    try:
        default = ROOT / "artifacts/local/nabt" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        output = output_directory(args.output or default)
        write_report(output, report)
        execute(args, output, report)
        report.update(status="PASSED_RUNTIME_ONLY" if args.runtime_only else "PASSED",
                      full_parity=not args.runtime_only,
                      formal_conformance="NOT_RUN" if args.runtime_only else "PASSED")
        code = 0
    except (OSError, ValueError, CheckFailed, KeyboardInterrupt) as error:
        report.update(status="FAILED", error=str(error))
        code = 1
    finally:
        report["finished"] = stamp()
        if output is not None:
            report["generated_reports"] = generated_reports(output)
            write_report(output, report)
    print(json.dumps({"status": report["status"], "full_parity": report["full_parity"],
                      "manifest": str(output / "manifest.json") if output else None,
                      "error": report.get("error")}, ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
