"""Example upload files: each experiment's headline measurement saved the ways
real files arrive, so anyone can try an upload that isn't a tidy CSV.

Layout, one folder per area of physics (the tabs on the page):

  examples/README.md                      the formats and the list of areas
  examples/<area>/README.md               that area's experiments: what each file is
                                          made from and the result it should give
  examples/<area>/<experiment>/<file>     the five formats below
  examples/index.json                     what the page offers under the samples

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
matched (eval/check_parsing.py checks both). The expected result in each area's
README is computed here, with the physics code and the fault library, using the
page's default expected values. Run: python data/make_examples.py
(data/generate.py runs it).
"""
import importlib.util
import json
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SEEDED = ROOT / "data" / "seeded"
OUT = ROOT / "examples"
sys.path.insert(0, str(ROOT / "sandbox" / "tools"))
import analyze  # noqa: E402

_spec = importlib.util.spec_from_file_location("ranking", ROOT / "app" / "ranking.py")
ranking = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ranking)

VARIANTS = [
    ("excel_export.csv", "Excel export",
     "Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column"),
    ("semicolon_decimal_comma.csv", "Semicolons, decimal commas",
     "A European spreadsheet export: `;` between columns and `0,25` for 0.25"),
    ("tab_separated.tsv", "Tab-separated",
     "Tabs between columns, as copied out of a spreadsheet"),
    ("unicode_text.txt", "UTF-16 \"Unicode text\"",
     "Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated"),
    ("other_column_names.csv", "Other column names",
     "The names a person would type, units in brackets (`Current (A)`): the page asks you to match them"),
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
    """catalog.yaml merged with catalog.d/*.yaml, as app/pipeline.py does."""
    cat = yaml.safe_load((ROOT / "app" / "catalog.yaml").read_text())
    for p in sorted((ROOT / "app" / "catalog.d").glob("*.yaml")):
        c = yaml.safe_load(p.read_text())
        known = {d["id"] for d in cat["domains"]}
        cat["domains"] += [d for d in c.get("domains", []) if d["id"] not in known]
        cat["experiments"].update(c.get("experiments", {}))
        cat["sample_info"].update(c.get("sample_info", {}))
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


def expected_result(exp, e, source):
    """The top cause the page shows for the sample, with the page's default expected values."""
    expected = {k: v for k, _, v in e["expected"]}
    header, data, _ = analyze.load_csv(SEEDED / source)
    analyze.check_columns(exp, header)
    out = analyze.ANALYSES[exp](header, data, expected)
    top = ranking.rank_causes(exp, out.get("evidence", {}))[0]
    return top["name"], top["probability"], [(l, v) for _, l, v in e["expected"]]


def fmt_value(v):
    return f"{v:g}" if isinstance(v, float) else str(v)


def area_readme(dom, exps, cat):
    n = len(exps)
    lines = [
        f"# {dom['label']}: example upload files",
        "",
        f"{n} experiment{'s' if n > 1 else ''}. Each folder holds that experiment's headline sample saved five ways "
        "real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on "
        "the page under the samples (*Same measurement, other file formats*). Every file gives the result listed "
        "for its experiment; *Other column names* does once you match its columns on the page.",
        "",
        "| File | Format |",
        "| --- | --- |",
        *[f"| `{f}` | **{label}**: {desc} |" for f, label, desc in VARIANTS],
        "",
        "[All areas](../README.md)",
        "",
    ]
    for exp in exps:
        e = cat["experiments"][exp]
        source, slabel = e["samples"][0][0], e["samples"][0][1]
        name, p, defaults = expected_result(exp, e, source)
        grad = " · graduate" if e.get("level") == "graduate" else ""
        lines += [
            f"## {e['label']}",
            "",
            f"`{exp}`{grad} · model `{e.get('model', '')}` · columns "
            + ", ".join(f"`{c}`" for c in e["columns"]),
            "",
            f"Made from the sample **{slabel}** ([`data/seeded/{source}`](../../data/seeded/{source})).",
        ]
        info = cat["sample_info"].get(source)
        if info:
            lines += ["", f"- *The bench:* {info[0]}", f"- *What looks off:* {info[1]}"]
        lines += [
            "",
            f"**Expected result:** {name}, {round(p * 100)}% as the leading cause"
            + (" (with the page's defaults: " + "; ".join(f"{l} = {fmt_value(v)}" for l, v in defaults) + ")."
               if defaults else "."),
            "",
            "Files: " + " · ".join(f"[{label}]({exp}/{f})" for f, label, _ in VARIANTS),
            "",
        ]
    return "\n".join(lines)


def main():
    cat = catalog()
    if OUT.exists():
        shutil.rmtree(OUT)
    index, areas = {}, []
    for dom in cat["domains"]:
        exps = [k for k, e in cat["experiments"].items() if e.get("domain") == dom["id"]]
        if not exps:
            continue
        for exp in exps:
            e = cat["experiments"][exp]
            source = e["samples"][0][0]
            text = (SEEDED / source).read_text()
            d = OUT / dom["id"] / exp
            d.mkdir(parents=True, exist_ok=True)
            for fname, _, _ in VARIANTS:
                (d / fname).write_bytes(rewrite(text, fname))
            index[exp] = {"area": dom["id"], "source": source, "source_label": e["samples"][0][1],
                          "files": [[f"{dom['id']}/{exp}/{f}", label] for f, label, _ in VARIANTS]}
        (OUT / dom["id"] / "README.md").write_text(area_readme(dom, exps, cat))
        areas.append((dom, exps))
    (OUT / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    total = sum(len(x) for _, x in areas)
    (OUT / "README.md").write_text("\n".join([
        "# Example upload files",
        "",
        f"Every experiment's headline measurement ({total} experiments in {len(areas)} areas of physics), saved the "
        "ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick "
        "them on the page under the samples (*Same measurement, other file formats*). Every file except *Other "
        "column names* gives exactly the sample's result, and that one does once you match its columns on the page.",
        "",
        "Made by [`data/make_examples.py`](../data/make_examples.py) from `data/seeded/`; "
        "[`eval/check_parsing.py`](../eval/check_parsing.py) checks that every file gives the sample's result.",
        "",
        "## The five formats",
        "",
        "| File | Format |",
        "| --- | --- |",
        *[f"| `{f}` | **{label}**: {desc} |" for f, label, desc in VARIANTS],
        "",
        "## By area",
        "",
        "| Area | Experiments |",
        "| --- | --- |",
        *[f"| [{dom['label']}]({dom['id']}/README.md) | "
          + ", ".join(cat["experiments"][x]["label"] for x in exps) + " |" for dom, exps in areas],
        "",
    ]))
    print(f"Wrote {total * len(VARIANTS)} example files for {total} experiments in {len(areas)} areas to {OUT}")


if __name__ == "__main__":
    sys.exit(main())
