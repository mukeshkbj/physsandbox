"""Example upload files: each experiment's headline measurement saved the ways
real files arrive, so anyone can try an upload that isn't a tidy CSV.

For every experiment, the first sample in its catalogue entry is rewritten as:

  excel_export.csv            Excel-style CSV: byte-order mark, Windows line endings,
                              comment lines padded with commas, an empty row of only
                              commas above the header, a trailing empty column
  semicolon_decimal_comma.csv European spreadsheet: semicolons between columns and
                              decimal commas
  tab_separated.tsv           tab-separated text, as copied out of a spreadsheet
  unicode_text.txt            Excel's "Unicode text": UTF-16, tab-separated
  other_column_names.csv      the column names a person would type, with units in
                              brackets ("Current (A)"); the page asks which is which

The numbers are byte-for-byte the sample's, so every format except the renamed one
gives exactly the sample's result; the renamed one does once its columns are
matched (eval/check_parsing.py checks both). Output: examples/<experiment>/ and
examples/index.json. Run: python data/make_examples.py (data/generate.py runs it).
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SEEDED = ROOT / "data" / "seeded"
OUT = ROOT / "examples"

VARIANTS = [
    ("excel_export.csv", "Excel export"),
    ("semicolon_decimal_comma.csv", "Semicolons, decimal commas"),
    ("tab_separated.tsv", "Tab-separated"),
    ("unicode_text.txt", "UTF-16 \"Unicode text\""),
    ("other_column_names.csv", "Other column names"),
]

UNITS = {
    "V": "V", "mV": "mV", "kV": "kV", "A": "A", "nA": "nA", "s": "s", "ms": "ms", "us": "µs",
    "Hz": "Hz", "kHz": "kHz", "MHz": "MHz", "keV": "keV", "eV": "eV", "m": "m", "cm": "cm", "mm": "mm",
    "um": "µm", "nm": "nm", "deg": "°", "T": "T", "mT": "mT", "uT": "µT", "uW": "µW", "Wb": "Wb",
    "kg": "kg", "kPa": "kPa", "ml": "ml", "C": "°C", "K": "K", "ohm": "Ω", "mOhm": "mΩ",
    "1e19C": "1e-19 C",
}


def human(name):
    """current_A -> 'Current (A)', H_A_per_m -> 'H (A/m)', fringes -> 'Fringes'."""
    if name.endswith("_A_per_m"):
        return name[: -len("_A_per_m")].replace("_", " ").capitalize() + " (A/m)"
    stem, _, unit = name.rpartition("_")
    if stem and unit in UNITS:
        words = stem.replace("_", " ")
        return (words[0].upper() + words[1:]) + f" ({UNITS[unit]})"
    words = name.replace("_", " ")
    return words[0].upper() + words[1:]


def catalog():
    cat = yaml.safe_load((ROOT / "app" / "catalog.yaml").read_text())["experiments"]
    for p in sorted((ROOT / "app" / "catalog.d").glob("*.yaml")):
        cat.update(yaml.safe_load(p.read_text()).get("experiments", {}))
    return cat


def split(text):
    lines = [l for l in text.splitlines() if l.strip()]
    return [l for l in lines if l.startswith("#")], [l for l in lines if not l.startswith("#")]


def rewrite(text, variant):
    comments, table = split(text)
    header, rows = table[0], table[1:]
    if variant == "excel_export.csv":
        ncol = len(header.split(","))
        lines = [c + ",," for c in comments] + ["," * ncol] + [r + "," for r in table]
        return ("﻿" + "\r\n".join(lines) + "\r\n").encode("utf-8")
    if variant == "semicolon_decimal_comma.csv":
        body = [header.replace(",", ";")] + [";".join(c.replace(".", ",") for c in r.split(",")) for r in rows]
        return ("\r\n".join(comments + body) + "\r\n").encode("utf-8")
    if variant == "tab_separated.tsv":
        return ("\n".join(comments + [r.replace(",", "\t") for r in table]) + "\n").encode("utf-8")
    if variant == "unicode_text.txt":
        return ("\r\n".join(comments + [r.replace(",", "\t") for r in table]) + "\r\n").encode("utf-16")
    if variant == "other_column_names.csv":
        names = [human(h) for h in header.split(",")]
        quoted = ",".join(f'"{n}"' if "," in n else n for n in names)
        return ("\n".join(comments + [quoted] + rows) + "\n").encode("utf-8")
    raise ValueError(variant)


def main():
    index = {}
    for exp, e in catalog().items():
        source = e["samples"][0][0]
        text = (SEEDED / source).read_text()
        d = OUT / exp
        d.mkdir(parents=True, exist_ok=True)
        for fname, _ in VARIANTS:
            (d / fname).write_bytes(rewrite(text, fname))
        index[exp] = {"source": source, "source_label": e["samples"][0][1],
                      "files": [[f"{exp}/{f}", label] for f, label in VARIANTS]}
    (OUT / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    rows = "\n".join(f"| {exp} | `{v['source']}` ({v['source_label']}) | "
                     + " · ".join(f"[{label}]({f})" for f, label in v["files"]) + " |"
                     for exp, v in sorted(index.items()))
    (OUT / "README.md").write_text(
        "# Example upload files\n\n"
        "Each experiment's headline measurement, saved the ways real files arrive. Upload any of them on the "
        "live demo (or pick them under the samples, as \"Same measurement, other file formats\"): every one "
        "except *Other column names* gives exactly the sample's result, and that one does once you match its "
        "columns on the page. Made by `data/make_examples.py` from `data/seeded/`; "
        "`eval/check_parsing.py` checks them.\n\n"
        "| Experiment | Made from | Files |\n| --- | --- | --- |\n" + rows + "\n")
    print(f"Wrote {len(index) * len(VARIANTS)} example files for {len(index)} experiments to {OUT}")


if __name__ == "__main__":
    sys.exit(main())
