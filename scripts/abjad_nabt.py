"""قارئُ NABT الصارم ورجيستري A116، منقولٌ إلى Mashru بنصّه (sonaiso/NABT@3dbe335: src/nabt/alphabet.py وsrc/nabt/errors.py؛ MIT، Saleh1967).

لا يستورد شيئًا من NABT: الملفّان مضمومان هنا بلا تغييرٍ في المنطق (إلّا الاستيرادَ النسبيّ). يقرأ كلمةً مشكولةً تامّة: حاملٌ ثمّ علامةٌ واحدة من
الأربع، بلا تخمينٍ ولا تطبيع؛ وما ينقصه الشكلُ أو يحتاج جسرَ رسمٍ «DEFER» باسمه، وما سواه «REJECT» باسمه.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any
import unicodedata

class NabtError(ValueError):
    """A named rejection or an explicitly incomplete computation."""

    def __init__(
        self, code: str, message: str, *, status: str = "REJECT", details: Any = None
    ) -> None:
        super().__init__(message)
        if status not in {"REJECT", "DEFER"}:
            raise ValueError("Unsupported NABT error status")
        self.code = code
        self.message = message
        self.status = status
        self.details = details

    def as_dict(self) -> dict[str, Any]:
        result = {"status": self.status, "code": self.code, "message": self.message}
        if self.details is not None:
            result["details"] = self.details
        return result


def natural(value: object, name: str, *, maximum: int | None = None) -> int:
    """Require an actual natural integer; Python booleans are not numbers here."""
    if type(value) is not int or value < 0:
        raise NabtError("INVALID_NATURAL", f"{name} must be a non-negative integer")
    if maximum is not None and value > maximum:
        raise NabtError("OUTSIDE_DOMAIN", f"{name} exceeds its declared domain")
    return value


def resource_limit(message: str, **details: Any) -> NabtError:
    return NabtError("RESOURCE_LIMIT", message, status="DEFER", details=details or None)


ALPHABET_ID = "nabt.a116.v1"
LAW_ID = "nabt-sound-shape-v1"
CARRIERS = tuple("ابتثجحخدذرزسشصضطظعغفقكلمنهويء")
HARAKAT = ("َ", "ُ", "ِ", "ْ")
STATE_NAMES = ("fatha", "damma", "kasra", "sukun")
ALPHABET_SIZE = 116
MAX_CELLS = 4096
MAX_SOURCE_BYTES = MAX_CELLS * 8

if len(CARRIERS) != 29 or len(set(CARRIERS)) != 29:
    raise RuntimeError("A116 carrier registry is malformed")


def validate_cell(value: object) -> int:
    return natural(value, "cell", maximum=ALPHABET_SIZE - 1)


def validate_cells(cells: Iterable[int]) -> tuple[int, ...]:
    if isinstance(cells, (str, bytes, bytearray)):
        raise NabtError("INVALID_CELLS", "A cell sequence must contain integer cell IDs")
    try:
        iterator = iter(cells)
    except TypeError as exc:
        raise NabtError("INVALID_CELLS", "A cell sequence must be iterable") from exc
    result = []
    for i, cell in enumerate(iterator):
        if i >= MAX_CELLS:
            raise resource_limit("Cell sequence exceeds the runtime budget", maximum=MAX_CELLS)
        result.append(validate_cell(cell))
    return tuple(result)


def cell_id(carrier: str, state: int) -> int:
    if type(carrier) is not str or carrier not in CARRIERS:
        raise NabtError("UNKNOWN_CARRIER", "Carrier is outside the declared A116 registry")
    natural(state, "state", maximum=3)
    return 4 * CARRIERS.index(carrier) + state


def cell_parts(cell: int) -> tuple[str, int]:
    c, s = divmod(validate_cell(cell), 4)
    return CARRIERS[c], s


def parse_word(text: str) -> tuple[int, ...]:
    """Read an exact fully marked word, without trimming or Unicode folding.

    Missing vocalization and unsupported representation features are DEFER.
    Conflicting marks, malformed UTF-8 scalars, and non-word boundaries reject.
    """
    if type(text) is not str:
        raise NabtError("INVALID_TEXT", "Source text must be a string")
    if len(text) > MAX_SOURCE_BYTES:
        raise resource_limit("Source text exceeds the runtime budget", maximum_bytes=MAX_SOURCE_BYTES)
    try:
        raw = text.encode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise NabtError("INVALID_UNICODE", "Source contains an invalid Unicode scalar") from exc
    if len(raw) > MAX_SOURCE_BYTES:
        raise resource_limit("Source text exceeds the runtime budget", maximum_bytes=MAX_SOURCE_BYTES)
    if not text:
        raise NabtError("EMPTY_WORD", "A word source cannot be empty")
    result: list[int] = []
    current: str | None = None
    mark: str | None = None
    for position, char in enumerate(text):
        if char in CARRIERS:
            if current is not None:
                if mark is None:
                    raise NabtError("MISSING_VOCALIZATION", "A carrier has no declared state", status="DEFER", details={"carrier": current, "before_position": position})
                result.append(cell_id(current, HARAKAT.index(mark)))
            current, mark = char, None
        elif char in HARAKAT:
            if current is None:
                raise NabtError("MARK_WITHOUT_CARRIER", "A mark has no preceding carrier", details={"position": position})
            if mark is not None:
                raise NabtError("CONFLICTING_MARKS", "A carrier has more than one mark", details={"position": position})
            mark = char
        elif char.isspace():
            raise NabtError("WORD_BOUNDARY_NOT_ALLOWED", "This entry point accepts one word with no boundary", details={"position": position})
        elif unicodedata.category(char).startswith("M") or char in "أإؤئآٱىة":
            raise NabtError("UNSUPPORTED_ORTHOGRAPHY", "This spelling requires an orthographic bridge not implemented in this release", status="DEFER", details={"position": position, "codepoint": f"U+{ord(char):04X}"})
        else:
            raise NabtError("UNKNOWN_CARRIER", "Source contains a symbol outside the word alphabet", status="DEFER", details={"position": position, "codepoint": f"U+{ord(char):04X}"})
    if current is None or mark is None:
        raise NabtError("MISSING_VOCALIZATION", "The final carrier has no declared state", status="DEFER")
    result.append(cell_id(current, HARAKAT.index(mark)))
    return validate_cells(result)


def render_word(cells: Iterable[int]) -> str:
    return "".join(CARRIERS[a // 4] + HARAKAT[a % 4] for a in validate_cells(cells))
