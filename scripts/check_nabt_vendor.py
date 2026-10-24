#!/usr/bin/env python3
"""Check the exact pinned NABT source snapshot before running its Python code.

The lock digest is installed policy, not an argument or a field supplied by
the snapshot. Git blob identities bind the retained bytes to the manifest;
the pinned commit/tree record their provenance. This is a checkout integrity
check, not a proof of source authentication or process isolation. Generated
Lean outputs and Python caches are outside its source inventory and are not
certified by a successful result.
"""

from __future__ import annotations

import argparse
from hashlib import sha1, sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys


ROOT = Path(__file__).absolute().parents[1]
EXPECTED_LOCK_SHA256 = "3be972ea9ecc797c15aaa5489220d0716fa21aeaabaa03f646d0f07611d3c5ea"
EXPECTED_REPOSITORY = "sonaiso/NABT"
EXPECTED_COMMIT = "f0064f0a4baab3cc816087a322aabc0c8fbb2d19"
EXPECTED_TREE = "63453db8c545403b22c137307bda64c9ac5656d9"
SCHEMA = "mashru.nabt.snapshot.v1"
MAX_LOCK_BYTES = 16 * 1024 * 1024
MAX_FILES = 25000
FILE_FIELDS = {"path", "sha256", "size", "git_blob_sha", "mode"}


class SnapshotError(ValueError):
    def __init__(self, code: str, message: str, path: str | None = None):
        super().__init__(message)
        self.code = code
        self.path = path

    def report(self) -> dict:
        result = {"status": "DEFER", "code": self.code, "message": str(self)}
        if self.path is not None:
            result["path"] = self.path
        return result


def _fail(code: str, message: str, path: str | None = None):
    raise SnapshotError(code, message, path)


def _object_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            _fail("NABT_LOCK_DUPLICATE_KEY", "Duplicate JSON object key", key)
        result[key] = value
    return result


def _hex(value, length: int) -> bool:
    return type(value) is str and re.fullmatch(r"[0-9a-f]{" + str(length) + r"}", value) is not None


def _path(value) -> str:
    if type(value) is not str or not value or "\\" in value or any(ord(c) < 32 for c in value):
        _fail("NABT_LOCK_PATH", "Expected a nonempty canonical relative POSIX path")
    parsed = PurePosixPath(value)
    if (parsed.is_absolute() or value != parsed.as_posix() or
            any(part in {"", ".", ".."} for part in parsed.parts) or
            ":" in parsed.parts[0]):
        _fail("NABT_LOCK_PATH", "Unsafe or noncanonical snapshot path", value)
    return value


def _ignored_directory(parts: tuple[str, ...]) -> bool:
    return parts[-1] in {".lake", "__pycache__"} or parts == ("artifacts", "local")


def _ignored_file(parts: tuple[str, ...]) -> bool:
    return (any(part in {".lake", "__pycache__"} for part in parts[:-1]) or
            parts[:2] == ("artifacts", "local") or parts[-1].endswith(".pyc"))


def _lstat(path: Path, label: str):
    try:
        info = path.lstat()
    except FileNotFoundError:
        _fail("NABT_SNAPSHOT_MISSING", "Required snapshot path is missing", label)
    if stat.S_ISLNK(info.st_mode):
        _fail("NABT_SNAPSHOT_SYMLINK", "Symbolic links are not snapshot files or directories", label)
    return info


def _directory(path: Path, label: str):
    if not stat.S_ISDIR(_lstat(path, label).st_mode):
        _fail("NABT_SNAPSHOT_DIRECTORY", "Expected a real directory", label)


def _check_root(root: Path):
    # Do not resolve() first: that would conceal a linked ancestor.
    for directory in reversed((root, *root.parents)):
        _directory(directory, str(directory))
    _directory(root / "integrations", "integrations")


def _read_regular(path: Path, label: str, *, limit: int | None = None) -> bytes:
    info = _lstat(path, label)
    if not stat.S_ISREG(info.st_mode):
        _fail("NABT_SNAPSHOT_FILE_TYPE", "Expected a regular file", label)
    if limit is not None and info.st_size > limit:
        _fail("NABT_LOCK_RESOURCE_LIMIT", "The lock exceeds its byte limit", label)
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    with os.fdopen(os.open(path, flags), "rb") as stream:
        content = stream.read() if limit is None else stream.read(limit + 1)
    if limit is not None and len(content) > limit:
        _fail("NABT_LOCK_RESOURCE_LIMIT", "The lock exceeds its byte limit", label)
    return content


def _inventory(vendor: Path) -> set[str]:
    _directory(vendor, "integrations/nabt")
    result = set()

    def visit(directory: Path, parts: tuple[str, ...]):
        with os.scandir(directory) as iterator:
            entries = sorted(iterator, key=lambda item: item.name)
        for entry in entries:
            relative = (*parts, entry.name)
            label = "/".join(relative)
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISLNK(info.st_mode):
                _fail("NABT_SNAPSHOT_SYMLINK", "Linked snapshot entry is forbidden", label)
            if stat.S_ISDIR(info.st_mode):
                if not _ignored_directory(relative):
                    visit(Path(entry.path), relative)
            elif stat.S_ISREG(info.st_mode):
                if not _ignored_file(relative):
                    result.add(label)
            else:
                _fail("NABT_SNAPSHOT_FILE_TYPE", "Nonregular snapshot entry is forbidden", label)

    visit(vendor, ())
    return result


def _verify_snapshot(root: Path, expected_lock_sha256: str) -> dict:
    """Internal engine; the CLI fixes both arguments. Tests use isolated fixtures."""
    if not _hex(expected_lock_sha256, 64):
        _fail("NABT_LOCK_PIN_UNSET", "The installed snapshot digest has not been finalized")
    root = root.absolute()
    _check_root(root)
    lock = _read_regular(root / "integrations/nabt.lock.json", "integrations/nabt.lock.json",
                         limit=MAX_LOCK_BYTES)
    if sha256(lock).hexdigest() != expected_lock_sha256:
        _fail("NABT_LOCK_DIGEST_MISMATCH", "The lock does not match the installed digest",
              "integrations/nabt.lock.json")
    try:
        document = json.loads(lock.decode("utf-8"), object_pairs_hook=_object_pairs,
                              parse_constant=lambda value: _fail("NABT_LOCK_JSON", "Non-JSON constant", value))
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        _fail("NABT_LOCK_JSON", "Invalid bounded UTF-8 JSON: " + str(error))
    if type(document) is not dict or set(document) != {"schema", "upstream", "selection", "files"}:
        _fail("NABT_LOCK_SCHEMA", "Unexpected snapshot manifest fields")
    if document["schema"] != SCHEMA or type(document["selection"]) is not dict:
        _fail("NABT_LOCK_SCHEMA", "Unknown schema or malformed selection metadata")
    upstream = document["upstream"]
    if type(upstream) is not dict or set(upstream) != {"repository", "commit", "tree"}:
        _fail("NABT_LOCK_UPSTREAM", "Unexpected upstream provenance fields")
    if upstream != {"repository": EXPECTED_REPOSITORY, "commit": EXPECTED_COMMIT, "tree": EXPECTED_TREE}:
        _fail("NABT_LOCK_UPSTREAM", "The upstream repository, commit or tree is not the installed source")
    files = document["files"]
    if type(files) is not list or not 1 <= len(files) <= MAX_FILES:
        _fail("NABT_LOCK_FILES", "Expected a bounded nonempty file inventory")
    declared = {}
    for row in files:
        if type(row) is not dict or set(row) != FILE_FIELDS:
            _fail("NABT_LOCK_FILE_SCHEMA", "Unexpected file inventory fields")
        name = _path(row["path"])
        if name in declared:
            _fail("NABT_LOCK_DUPLICATE_PATH", "Snapshot path is declared more than once", name)
        if _ignored_file(PurePosixPath(name).parts):
            _fail("NABT_LOCK_GENERATED_PATH", "Generated artifacts cannot be pinned source files", name)
        if (type(row["size"]) is not int or row["size"] < 0 or
                not _hex(row["sha256"], 64) or not _hex(row["git_blob_sha"], 40) or
                type(row["mode"]) is not str or row["mode"] not in {"100644", "100755"}):
            _fail("NABT_LOCK_FILE_SCHEMA", "Malformed size, hash or Git mode", name)
        declared[name] = row
    vendor = root / "integrations/nabt"
    actual = _inventory(vendor)
    missing = set(declared) - actual
    extra = actual - set(declared)
    if missing:
        _fail("NABT_SNAPSHOT_MISSING", "Declared file is missing", sorted(missing)[0])
    if extra:
        _fail("NABT_SNAPSHOT_EXTRA", "Undeclared file is present", sorted(extra)[0])
    total = 0
    for name, row in declared.items():
        path = vendor / name
        for parent in reversed(path.parents):
            if parent == vendor or vendor in parent.parents:
                _directory(parent, parent.relative_to(root).as_posix())
        info = _lstat(path, name)
        if not stat.S_ISREG(info.st_mode):
            _fail("NABT_SNAPSHOT_FILE_TYPE", "Expected a regular source file", name)
        mode = "100755" if info.st_mode & 0o111 else "100644"
        if mode != row["mode"]:
            _fail("NABT_SNAPSHOT_MODE", "Executable mode differs from the snapshot", name)
        if info.st_size != row["size"]:
            _fail("NABT_SNAPSHOT_SIZE", "File size differs from the snapshot", name)
        content = _read_regular(path, name)
        if len(content) != row["size"]:
            _fail("NABT_SNAPSHOT_SIZE", "File size changed during inspection", name)
        if sha256(content).hexdigest() != row["sha256"]:
            _fail("NABT_SNAPSHOT_DIGEST", "File bytes differ from the snapshot", name)
        blob = sha1(b"blob " + str(len(content)).encode("ascii") + b"\0" + content).hexdigest()
        if blob != row["git_blob_sha"]:
            _fail("NABT_SNAPSHOT_GIT_BLOB", "Git blob identity differs from the snapshot", name)
        total += len(content)
    return {"status": "VERIFIED", "schema": SCHEMA, "upstream_commit": EXPECTED_COMMIT,
            "files": len(declared), "bytes": total, "lock_sha256": expected_lock_sha256}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="Suppress successful verification output")
    args = parser.parse_args(argv)
    try:
        report = _verify_snapshot(ROOT, EXPECTED_LOCK_SHA256)
    except SnapshotError as error:
        print(json.dumps(error.report(), ensure_ascii=False), file=sys.stderr)
        return 3
    except OSError as error:
        print(json.dumps({"status": "DEFER", "code": "NABT_SNAPSHOT_IO", "message": str(error)},
                         ensure_ascii=False), file=sys.stderr)
        return 3
    if not args.quiet:
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
