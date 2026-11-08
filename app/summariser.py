"""Turn an uploaded CSV into a schema summary for the language model.

The model never sees raw rows or free text from the file. Comment lines and
any non-numeric text are dropped and only counted, which removes the
prompt-injection channel through uploaded data.
"""
import csv
import io
import re

MAX_BYTES = 5_000_000
_SAFE_COL = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,40}$")


def _decode(raw: bytes) -> str:
    """UTF-8 (with or without a byte-order mark) or UTF-16, as the sandbox reads it."""
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16", errors="replace")
    if raw[:400].count(b"\x00") > 40:
        return raw.decode("utf-16-le", errors="replace")
    return raw.decode("utf-8", errors="replace").lstrip("\ufeff")


def _delimiter(header_line):
    for d in (",", ";", "\t"):
        if d in header_line:
            return d
    return None


def _cells(line, delim):
    parts = line.split(delim) if delim else line.split()
    out = [c.strip().strip('"').strip("'").strip() for c in parts]
    while out and out[-1] == "":
        out.pop()
    return out


def summarise(raw: bytes) -> dict:
    if len(raw) > MAX_BYTES:
        raise ValueError("File too large (limit 5 MB)")
    text = _decode(raw)
    comment_lines, rows, header, delim = 0, [], None, ","
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            comment_lines += 1
            continue
        if header is None:
            if not line.strip():
                continue
            delim = _delimiter(line)
            header = _cells(line, delim) or None
            continue
        if _cells(line, delim):          # skip blank lines and rows of only separators
            rows.append(_cells(line, delim))

    columns = []
    for i, name in enumerate(header or []):
        name = name.strip()
        vals = []
        for parts in rows:
            try:
                c = parts[i]
                decimal_comma = delim == ";" or (delim is None and c.count(",") == 1 and "." not in c)
                vals.append(float(c.replace(",", ".") if decimal_comma else c))
            except (ValueError, IndexError):
                pass
        columns.append({
            # Column names are the only text that reaches the model, so they
            # must look like identifiers; anything else is replaced.
            "name": name if _SAFE_COL.match(name) else f"column_{i}",
            "count": len(vals),
            "min": min(vals) if vals else None,
            "max": max(vals) if vals else None,
        })

    return {
        "rows": len(rows),
        "columns": columns,
        "comment_lines_dropped": comment_lines,
        "note": "Free text in the file is never shown to the model.",
    }
