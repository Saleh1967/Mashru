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
BOOTSTRAP = """import runpy, sys
source, root, entry, *arguments = sys.argv[1:]
sys.path[:0] = [source, root]
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
