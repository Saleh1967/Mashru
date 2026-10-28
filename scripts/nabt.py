#!/usr/bin/env python3
"""Run Mashru's pinned local NABT implementation without installing a package.

Examples, from the Mashru checkout:

  python3 -I scripts/nabt.py runtime analyse 'كَتَبَ'
  python3 -I scripts/nabt.py recursive read integrations/nabt/examples/recursive_morphology.txt
  python3 -I scripts/nabt.py classical assess integrations/nabt/examples/classical_language/qatr_inna.json
  python3 -I scripts/nabt.py runtime inquire integrations/nabt/examples/rational_inquiry/plan.json \
      --sources integrations/nabt/examples/rational_inquiry/sources.json
  python3 -I scripts/nabt.py inquiry-conformance --lake /path/to/lake

Relative input and output paths retain the caller's working directory. The
snapshot checker runs before any NABT code. The child interpreter ignores
PYTHONPATH and user site packages, and imports the checked local source only.
Each launch redirects bytecode lookup into a fresh temporary directory; -B
alone would still allow an unchecked, valid __pycache__ entry to be executed.
An import guard replaces the path finder in the child: every module comes from
the checked snapshot or from the standard library (site-packages excluded);
sourceless bytecode and vendored extension modules are refused by name
(NABT_MODULE_ORIGIN, NABT_SOURCELESS_MODULE, NABT_VENDOR_EXTENSION). NABT
declares no third-party dependency (pyproject.toml: dependencies = []).
Results keep the upstream evidence scope; this entry point grants no new
grammar, acquisition, sealed-deposit or external-world authority.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "integrations" / "nabt"
CHECKER = ROOT / "scripts" / "check_nabt_vendor.py"
COMMANDS = {
    "runtime": ("src/nabt/__main__.py", "All NABT runtime commands; includes inquire and verify-inquiry"),
    "recursive": ("tools/recursive_bridge.py", "Exact source transport, replay and bounded Lean assessment"),
    "classical": ("tools/classical_language_evidence.py", "Audit, assess and replay the pinned classical-source catalog"),
    "inquiry-conformance": ("tools/check_rational_inquiry.py", "Fresh bounded Lean/Python inquiry comparison; accepts --lake"),
    "classical-conformance": ("tools/check_classical_language_evidence.py", "Fresh bounded Lean/Python classical-law comparison; accepts --lake"),
}

# Paths and arguments are separate argv entries, never interpolated Python or
# shell source. -I keeps the caller's directory and Python environment off the
# import search path. run_path does not itself add these two source roots.
GUARD = """import importlib.machinery as _m, os as _os, sys as _sys, sysconfig as _sc
def _real(p):
    return _os.path.realpath(p)
def _under(p, roots):
    return any(p == r or p.startswith(r + _os.sep) for r in roots)
_paths = _sc.get_paths()
_site = [_real(_paths[k]) for k in ("purelib", "platlib") if _paths.get(k)]
_std = [_real(_paths[k]) for k in ("stdlib", "platstdlib") if _paths.get(k)]
class _PinnedOrigin:
    def __init__(self, roots):
        self.roots = [_real(r) for r in roots]
    def find_spec(self, name, path=None, target=None):
        spec = _m.PathFinder.find_spec(name, path, target)
        if spec is None:
            return None
        if spec.origin in (None, "namespace"):
            places = list(spec.submodule_search_locations or [])
        else:
            places = [spec.origin]
        for place in places:
            real = _real(place)
            if not (_under(real, self.roots) or (_under(real, _std) and not _under(real, _site))):
                raise ImportError("NABT_MODULE_ORIGIN: " + name + " resolves outside the checked snapshot and the standard library: " + real)
        if isinstance(spec.loader, _m.SourcelessFileLoader):
            raise ImportError("NABT_SOURCELESS_MODULE: " + name + " has bytecode without checked source")
        if isinstance(spec.loader, _m.ExtensionFileLoader) and _under(_real(spec.origin), self.roots):
            raise ImportError("NABT_VENDOR_EXTENSION: " + name + " is a native module inside the snapshot")
        return spec
    def invalidate_caches(self):
        _m.PathFinder.invalidate_caches()
def _pin(*roots):
    guard = _PinnedOrigin(roots)
    _sys.meta_path[:] = [guard if finder is _m.PathFinder else finder for finder in _sys.meta_path]
"""

BOOTSTRAP = GUARD + """import runpy, sys
source, root, entry, *arguments = sys.argv[1:]
sys.path[:0] = [source, root]
_pin(source, root)
sys.argv = [entry, *arguments]
if entry == 'nabt':
    runpy.run_module('nabt', run_name='__main__', alter_sys=True)
else:
    runpy.run_path(entry, run_name='__main__')
"""


def unavailable(code: str, message: str) -> int:
    print(json.dumps({"status": "DEFER", "code": code, "message": message},
                     ensure_ascii=False), file=sys.stderr)
    return 3


def exit_status(returncode: int) -> int:
    """Retain ordinary child codes; represent a signal using shell convention."""
    return returncode if returncode >= 0 else 128 - returncode


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Run the pinned NABT capabilities included in this Mashru checkout.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=("Arguments after COMMAND are passed unchanged. Use COMMAND --help for its\n"
                "upstream interface. Relative file paths use your current directory.\n"
                "Conformance commands forward --lake to the pinned tool; they do not\n"
                "install or download Lean. These results retain their declared scope."),
    )
    result.add_argument("command", choices=tuple(COMMANDS), metavar="COMMAND",
                        help="\n".join(name + ": " + value[1]
                                       for name, value in COMMANDS.items()))
    result.add_argument("arguments", nargs=argparse.REMAINDER)
    return result


def run_pinned(code: str, arguments: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess:
    """Run Python `code` against the checked snapshot, as the CLI runs an entry.

    The snapshot checker runs first; a failure raises RuntimeError with its
    report. The child receives (source, root, *arguments) in sys.argv[1:], the
    same fresh bytecode prefix, and the same import guard (`_pin`).
    """
    if not CHECKER.is_file() or CHECKER.is_symlink():
        raise RuntimeError("NABT_CHECKER_UNAVAILABLE")
    with tempfile.TemporaryDirectory(prefix="mashru-nabt-pyc-") as cache:
        python = [sys.executable, "-I", "-B", "-X", f"pycache_prefix={cache}"]
        checked = subprocess.run([*python, str(CHECKER), "--quiet"], capture_output=True, text=True, check=False)
        if checked.returncode:
            raise RuntimeError("NABT_SNAPSHOT_REJECTED: " + checked.stderr.strip())
        prelude = GUARD + "import sys\nsys.path[:0] = sys.argv[1:3]\n_pin(*sys.argv[1:3])\n"
        return subprocess.run([*python, "-c", prelude + code, str(VENDOR / "src"), str(VENDOR), *arguments],
                              input=input_text, capture_output=True, text=True, encoding="utf-8", check=False)


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    entry_path = VENDOR / COMMANDS[args.command][0]
    if not CHECKER.is_file() or CHECKER.is_symlink():
        return unavailable("NABT_CHECKER_UNAVAILABLE", "The local snapshot checker is missing or linked.")
    if not entry_path.is_file() or entry_path.is_symlink():
        return unavailable("NABT_ENTRY_UNAVAILABLE", "The selected local NABT entry point is missing or linked.")
    try:
        with tempfile.TemporaryDirectory(prefix="mashru-nabt-pyc-") as cache:
            python = [sys.executable, "-I", "-B", "-X", "pycache_prefix=" + cache]
            checked = subprocess.run([*python, str(CHECKER), "--quiet"], check=False)
            if checked.returncode:
                return exit_status(checked.returncode)
            entry = "nabt" if args.command == "runtime" else str(entry_path)
            child = subprocess.run(
                [*python, "-c", BOOTSTRAP, str(VENDOR / "src"),
                 str(VENDOR), entry, *args.arguments],
                check=False,
            )
            return exit_status(child.returncode)
    except OSError as error:
        return unavailable("NABT_LAUNCH_UNAVAILABLE", str(error))


if __name__ == "__main__":
    raise SystemExit(main())
