"""Parsing robustness across every experiment.

Every seeded file in the evaluation (all experiments, first measurements and
follow-ups) is rewritten the ways real files arrive: Windows line endings and a
byte-order mark, a spreadsheet export (comment lines padded with commas, an
empty row of only commas, trailing empty columns), quoted column names, a
semicolon-separated European export with decimal commas, tab- and
space-separated tables, UTF-16, and stray blank lines. Each variant must give
exactly the same physics result (values and evidence) as the original.

Run:  python eval/check_parsing.py
"""
import json
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "sandbox" / "tools"))
import analyze  # noqa: E402

SEEDED = ROOT / "data" / "seeded"


def split(text):
    """(comment lines, table lines) of an original seeded file."""
    lines = [l for l in text.splitlines() if l.strip()]
    return [l for l in lines if l.startswith("#")], [l for l in lines if not l.startswith("#")]


def variants(text):
    comments, table = split(text)
    ncol = len(table[0].split(","))
    pad = "," * 2
    yield "CRLF + byte-order mark", ("﻿" + "\r\n".join(comments + table) + "\r\n").encode("utf-8")
    yield "spreadsheet export (padded comments, comma-only row, trailing empty columns)", (
        "\r\n".join([c + pad for c in comments] + ["," * (ncol + 1)] + [r + pad for r in table]) + "\r\n"
    ).encode("utf-8")
    quoted = ",".join(f'"{h}"' for h in table[0].split(","))
    yield "quoted column names", "\n".join(comments + [quoted] + table[1:]).encode("utf-8")
    semi = [table[0].replace(",", ";")] + [";".join(c.replace(".", ",") for c in r.split(",")) for r in table[1:]]
    yield "semicolon-separated, decimal commas", "\n".join(comments + semi).encode("utf-8")
    yield "tab-separated", "\n".join(comments + [r.replace(",", "\t") for r in table]).encode("utf-8")
    yield "space-separated", "\n".join(comments + [r.replace(",", "   ") for r in table]).encode("utf-8")
    yield "UTF-16 with byte-order mark", "\r\n".join(comments + table).encode("utf-16")
    yield "blank lines and trailing spaces", ("\n\n".join(comments + [r + "  " for r in table]) + "\n\n").encode("utf-8")


def result(path, experiment, expected):
    header, data, _ = analyze.load_csv(path)
    analyze.check_columns(experiment, header)
    out = analyze.ANALYSES[experiment](header, data, expected)
    return json.dumps({"values": out.get("values"), "evidence": out.get("evidence")}, sort_keys=True, default=float)


def main():
    manifest = yaml.safe_load((ROOT / "data" / "manifest.yaml").read_text())["datasets"]
    for p in sorted((ROOT / "data" / "manifest.d").glob("*.yaml")):
        manifest += yaml.safe_load(p.read_text())["datasets"]
    cases, seen, failures, checked = [], set(), [], 0
    for d in manifest:
        key = (d["file"], d["experiment"])
        if key not in seen:
            seen.add(key)
            cases.append((d["file"], d["experiment"], d.get("expected", {})))
    with tempfile.TemporaryDirectory() as tmp:
        for name, experiment, expected in cases:
            text = (SEEDED / name).read_text()
            reference = result(SEEDED / name, experiment, expected)
            for label, raw in variants(text):
                p = Path(tmp) / "input.csv"
                p.write_bytes(raw)
                checked += 1
                try:
                    got = result(p, experiment, expected)
                except Exception as e:  # noqa: BLE001
                    failures.append((name, label, f"{type(e).__name__}: {e}"))
                    continue
                if got != reference:
                    failures.append((name, label, "different result"))
    # The example upload files (examples/): each format must give the sample's result;
    # the renamed-columns one once its header is matched back to the expected names.
    index = json.loads((ROOT / "examples" / "index.json").read_text())
    for exp, v in index.items():
        expected = next((c[2] for c in cases if c[0] == v["source"] and c[1] == exp), {})
        reference = result(SEEDED / v["source"], exp, expected)
        original_header = [l for l in (SEEDED / v["source"]).read_text().splitlines()
                           if l.strip() and not l.startswith("#")][0]
        for rel, label in v["files"]:
            path = ROOT / "examples" / rel
            checked += 1
            try:
                if rel.endswith("other_column_names.csv"):
                    lines = path.read_text().splitlines()
                    i = next(k for k, l in enumerate(lines) if l.strip() and not l.startswith("#"))
                    lines[i] = original_header
                    with tempfile.TemporaryDirectory() as tmp2:
                        p = Path(tmp2) / "input.csv"
                        p.write_text("\n".join(lines) + "\n")
                        got = result(p, exp, expected)
                else:
                    got = result(path, exp, expected)
            except Exception as e:  # noqa: BLE001
                failures.append((rel, label, f"{type(e).__name__}: {e}"))
                continue
            if got != reference:
                failures.append((rel, label, "different result"))
    experiments = len({c[1] for c in cases})
    print(f"{len(cases)} seeded files across {experiments} experiments, plus examples/: {checked} rewritten files")
    for f in failures:
        print("FAIL", *f)
    print(f"{checked - len(failures)}/{checked} give exactly the original result")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
