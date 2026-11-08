"""The experiment bench, one folder per area of physics, written from the catalogue,
the fault libraries and the physics code, so the documentation can't drift from what runs.

  experiments/README.md                    the areas, with every experiment in each
  experiments/<area>/README.md             that area's experiments in full: model, columns,
                                           what you enter, the faults it tells apart with
                                           their fixes, the bench tests it can recommend,
                                           the samples, the demo case end to end, and the
                                           example upload files
  experiments/<area>/<experiment>/<file>   the example upload files (five formats below)
  experiments/index.json                   what the page offers under the samples

The example files are the experiment's headline sample (the first in its catalogue entry)
saved the ways real files arrive:

  excel_export.csv            Excel-style CSV: byte-order mark, Windows line endings,
                              comment lines padded with commas, an empty row of only
                              commas above the header, a trailing empty column
  semicolon_decimal_comma.csv European spreadsheet: semicolons between columns and
                              decimal commas
  tab_separated.tsv           tab-separated text, as copied out of a spreadsheet
  unicode_text.txt            Excel's "Unicode text": UTF-16, tab-separated
  other_column_names.csv      the column names a person would type, with units in
                              brackets ("Current (A)"); the page asks which is which

The numbers are byte-for-byte the sample's, so every format except the renamed one gives
exactly the sample's result; the renamed one does once its columns are matched
(eval/check_parsing.py checks both). The demo case in each README is computed here the
way the server does it (app/pipeline.py), with the page's default expected values:
rank the causes, pick the test with the most information per minute, fold in only the
outcome of that test's sample result, rank again.
Run: python data/make_experiments.py (data/generate.py runs it).
"""
import importlib.util
import json
import shutil
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SEEDED = ROOT / "data" / "seeded"
OUT = ROOT / "experiments"
DEMO = "https://192-248-159-149.sslip.io/"
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

SHORT = ["Excel", "Semicolons", "Tabs", "UTF-16", "Renamed"]  # link text in the summary tables

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


def fault_files():
    """Which fault library file describes each experiment."""
    out = {exp: "faults/faults.yaml" for exp in yaml.safe_load((ROOT / "faults" / "faults.yaml").read_text())["experiments"]}
    for p in sorted((ROOT / "faults").glob("bench_*.yaml")):
        out.update({exp: f"faults/{p.name}" for exp in yaml.safe_load(p.read_text())["experiments"]})
    return out


def eval_cases():
    manifest = yaml.safe_load((ROOT / "data" / "manifest.yaml").read_text())["datasets"]
    for p in sorted((ROOT / "data" / "manifest.d").glob("*.yaml")):
        manifest += yaml.safe_load(p.read_text())["datasets"]
    return Counter(d["experiment"] for d in manifest)


def split(text):
    lines = [l for l in text.splitlines() if l.strip()]
    return [l for l in lines if l.startswith("#")], [l for l in lines if not l.startswith("#")]


def rewrite(text, variant):
    comments, table = split(text)
    header, rows = table[0], table[1:]
    if variant == "excel_export.csv":
        ncol = len(header.split(","))
        lines = [c + ",," for c in comments] + ["," * ncol] + [r + "," for r in table]
        return ("\ufeff" + "\r\n".join(lines) + "\r\n").encode("utf-8")
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


def physics(exp, path, expected):
    header, data, _ = analyze.load_csv(path)
    analyze.check_columns(exp, header)
    return analyze.ANALYSES[exp](header, data, expected)


def demo_case(exp, e):
    """The headline sample run as the server runs it: causes, the recommended test, and
    (when the catalogue has that test's sample result) the causes after the test."""
    expected = {k: v for k, _, v in e["expected"]}
    out = physics(exp, SEEDED / e["samples"][0][0], expected)
    causes = ranking.rank_causes(exp, out["evidence"])
    case = {"causes": causes, "values": out.get("values", {}), "test": None, "after": None}
    tests = ranking.next_tests(exp, causes) if causes[0]["probability"] < ranking.CONFIRM_AT else []
    if not tests:
        return case
    case["test"] = tests[0]
    follow = (e.get("followups") or {}).get(tests[0]["id"])
    if follow:
        new = physics(exp, SEEDED / follow, expected)
        evidence = dict(out["evidence"])
        evidence.update({k: v for k, v in ranking.test_outcome(tests[0]["id"], new["evidence"], evidence).items()
                         if v is not None})
        case["after"] = (follow, ranking.rank_causes(exp, evidence))
    return case


def pct(p):
    return f"{round(p * 100)}%"


def cell(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def fmt_value(v):
    return f"{v:g}" if isinstance(v, float) else str(v)


def anchor(label):
    keep = "".join(ch for ch in label.lower() if ch.isalnum() or ch in " -")
    return keep.replace(" ", "-")


def section_anchor(e):
    return anchor(e["label"] + (" graduate" if e.get("level") == "graduate" else ""))


def experiment_section(exp, e, cat, lib, ffile, n_cases):
    module = analyze.ANALYSES[exp].__module__
    code = "sandbox/tools/analyze.py" if module in ("analyze", "__main__") else f"sandbox/tools/{module}.py"
    grad = " *(graduate)*" if e.get("level") == "graduate" else ""
    case = demo_case(exp, e)
    L = [f"## {e['label']}{grad}", "", f"{e['blurb']}.", ""]
    L += ["| | |", "| --- | --- |",
          f"| Model | `{cell(e.get('model', ''))}` |",
          "| Columns | " + ", ".join(f"`{c}`" for c in e["columns"]) + " (one row per reading; `#` lines are comments) |"]
    if e["expected"]:
        L.append("| You enter | " + "; ".join(f"{cell(l)} (default {fmt_value(v)})" for _, l, v in e["expected"]) + " |")
    L += [f"| Physics code | [`{code}`](../../{code}), fitted inside the glovebox |",
          f"| Fault library | [`{ffile}`](../../{ffile}) |",
          f"| Evaluation | {n_cases} seeded cases in `data/manifest*` |",
          f"| Key | `{exp}` |", ""]

    faults = lib["faults"]
    L += ["### What goes wrong on this bench", "", "| Cause | Typical size | Fix |", "| --- | --- | --- |"]
    for k, f in faults.items():
        if k == "no_fault":
            continue
        L.append(f"| {cell(f['name'])} | {cell(f.get('typical_size', ''))} | {cell(f.get('fix', ''))} |")
    L += ["", "### Bench tests it can recommend", "",
          "Chosen by expected information per minute of bench time, among the causes still in the running.", "",
          "| Test | Minutes | What you do |", "| --- | --- | --- |"]
    for k, t in lib.get("tests", {}).items():
        safety = f" *Safety:* {cell(t['safety'])}" if t.get("safety") else ""
        L.append(f"| {cell(t['name'])} | {t['minutes']} | {cell(t['how'])}{safety} |")
    L += ["", "### Samples on the page", ""]
    for s in e["samples"]:
        tag = f" *({s[2]})*" if len(s) > 2 else ""
        info = cat["sample_info"].get(s[0])
        L.append(f"- **{s[1]}**{tag}: [`{s[0]}`](../../data/seeded/{s[0]})" + (f". {info[1]}" if info else ""))
    for t, f in (e.get("followups") or {}).items():
        tname = lib.get("tests", {}).get(t, {}).get("name", t)
        L.append(f"- Sample result of *{tname}*: [`{f}`](../../data/seeded/{f})")

    src, slabel = e["samples"][0][0], e["samples"][0][1]
    top = case["causes"][0]
    second = case["causes"][1] if len(case["causes"]) > 1 else None
    L += ["", "### The demo case", "",
          f"1. **{slabel}** ([`{src}`](../../data/seeded/{src})): the leading cause is *{top['name']}* at {pct(top['probability'])}"
          + (f", with *{second['name']}* at {pct(second['probability'])}." if second else ".")]
    if case["test"]:
        t = case["test"]
        L.append(f"2. Recommended test: **{t['name']}** ({t['minutes']} min, {t['info_gain_bits']:.2f} bits).")
        if case["after"]:
            follow, after = case["after"]
            a = after[0]
            state = "confirmed" if a["probability"] >= ranking.CONFIRM_AT else "leading"
            L.append(f"3. With its result ([`{follow}`](../../data/seeded/{follow})): *{a['name']}*, "
                     f"{pct(a['probability'])}, {state}.")
    L += ["", "### Example upload files", "",
          f"The headline sample saved five ways ([`{exp}/`]({exp}/)); each gives the result above. "
          + " · ".join(f"[{label}]({exp}/{f})" for f, label, _ in VARIANTS), ""]
    return L


def area_readme(dom, exps, cat, libs, ffiles, cases):
    n = len(exps)
    L = [f"# {dom['label']}", "",
         f"{n} experiment{'s' if n > 1 else ''} on the PhysSandbox bench. Try any of them on the [live demo]({DEMO}) "
         f"under *{dom['label']}*. [All areas](../README.md) · [Project README](../../README.md)", "",
         "| Experiment | Level | Model | Test that settles the demo case | Example files |", "| --- | --- | --- | --- | --- |"]
    for exp in exps:
        e = cat["experiments"][exp]
        case = demo_case(exp, e)
        test = case["test"]["name"] if case["test"] else "none needed"
        L.append(f"| [{cell(e['label'])}](#{section_anchor(e)}) | "
                 f"{'graduate' if e.get('level') == 'graduate' else 'teaching lab'} | `{cell(e.get('model', ''))}` | {cell(test)} | "
                 + " · ".join(f"[{short}]({exp}/{f})" for (f, _, _), short in zip(VARIANTS, SHORT)) + " |")
    L += ["", "Each experiment's folder holds its headline sample in five file formats:", "",
          "| File | Format |", "| --- | --- |",
          *[f"| `{f}` | **{label}**: {desc} |" for f, label, desc in VARIANTS], ""]
    for exp in exps:
        L += experiment_section(exp, cat["experiments"][exp], cat, libs[exp], ffiles[exp], cases[exp])
    return "\n".join(L)


def main():
    cat = catalog()
    libs, ffiles, cases = ranking.LIB["experiments"], fault_files(), eval_cases()
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
        (OUT / dom["id"] / "README.md").write_text(area_readme(dom, exps, cat, libs, ffiles, cases))
        areas.append((dom, exps))
    (OUT / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    total = sum(len(x) for _, x in areas)
    n_grad = sum(1 for _, x in areas for k in x if cat["experiments"][k].get("level") == "graduate")
    (OUT / "README.md").write_text("\n".join([
        "# The experiment bench",
        "",
        f"{total} experiments in {len(areas)} areas of physics, {total - n_grad} from teaching labs and {n_grad} from "
        "graduate advanced labs. Each area has its own folder and README with, for every experiment: the model and "
        "columns, what you enter, the faults it tells apart with a fix for each, the bench tests it can recommend, "
        "the samples, the demo case run end to end, and example upload files in five formats.",
        "",
        "| Area | Experiments |",
        "| --- | --- |",
        *[f"| [{dom['label']}]({dom['id']}/README.md) | "
          + ", ".join(f"[{cat['experiments'][x]['label']}]({dom['id']}/README.md#{section_anchor(cat['experiments'][x])})"
                      + (" *(graduate)*" if cat["experiments"][x].get("level") == "graduate" else "")
                      + f" ([files]({dom['id']}/{x}/))" for x in exps) + " |" for dom, exps in areas],
        "",
        "## Example upload files",
        "",
        f"Every experiment's folder holds its headline sample saved the ways real files arrive. Upload any of them on "
        f"the [live demo]({DEMO}), or pick them on the page under the samples (*Same measurement, other file formats*). "
        "Every file except *Other column names* gives exactly the sample's result, and that one does once you match "
        "its columns on the page.",
        "",
        "| File | Format |",
        "| --- | --- |",
        *[f"| `{f}` | **{label}**: {desc} |" for f, label, desc in VARIANTS],
        "",
        "Everything here is written by [`data/make_experiments.py`](../data/make_experiments.py) from the catalogue "
        "(`app/catalog.yaml`, `app/catalog.d/`), the fault libraries (`faults/`) and the physics code, so it matches "
        "what runs. [`eval/check_parsing.py`](../eval/check_parsing.py) checks that every example file gives the "
        "sample's result.",
        "",
    ]))
    write_main_readme_block(areas, cat)
    print(f"Wrote {len(areas)} area READMEs and {total * len(VARIANTS)} example files for {total} experiments to {OUT}")


def write_main_readme_block(areas, cat):
    """The bench section of the project README, between its bench:start/end markers:
    one heading per area, each experiment linked to its section and its example files."""
    readme = ROOT / "README.md"
    text = readme.read_text()
    a, b = "<!-- bench:start -->", "<!-- bench:end -->"
    if a not in text or b not in text:
        return
    L = [a, "", "Each area has its own folder and README in [`experiments/`](experiments/README.md) with every experiment "
         "in full: the model and columns, the faults it tells apart with a fix for each, the bench tests it can "
         "recommend, the samples, and the demo case run end to end. The example files are that experiment's "
         "headline sample in five real-world formats (Excel export, semicolons with decimal commas, tab-separated, "
         "UTF-16 \"Unicode text\", renamed columns); each gives the same result.", ""]
    for dom, exps in areas:
        L += [f"### [{dom['label']}](experiments/{dom['id']}/README.md)", "",
              "| Experiment | Model | Test that settles the demo case | Example files |", "| --- | --- | --- | --- |"]
        for exp in exps:
            e = cat["experiments"][exp]
            case = demo_case(exp, e)
            test = case["test"]["name"] if case["test"] else "none needed"
            grad = " *(graduate)*" if e.get("level") == "graduate" else ""
            base = f"experiments/{dom['id']}"
            L.append(f"| [{cell(e['label'])}]({base}/README.md#{section_anchor(e)}){grad} | `{cell(e.get('model', ''))}` | "
                     f"{cell(test)} | [folder]({base}/{exp}/): "
                     + " · ".join(f"[{short}]({base}/{exp}/{f})" for (f, _, _), short in zip(VARIANTS, SHORT)) + " |")
        L.append("")
    L.append(b)
    readme.write_text(text[: text.index(a)] + "\n".join(L) + text[text.index(b) + len(b):])


if __name__ == "__main__":
    sys.exit(main())
