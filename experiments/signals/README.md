# Signals

1 experiment on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Signals*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Oscilloscope trace](#oscilloscope-trace) | teaching lab | `spectrum of V(t)` | Connect all instruments to one ground point and re-record | [Excel](waveform/excel_export.csv) · [Semicolons](waveform/semicolon_decimal_comma.csv) · [Tabs](waveform/tab_separated.tsv) · [UTF-16](waveform/unicode_text.txt) · [Renamed](waveform/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Oscilloscope trace

Time-domain capture, checked for mains pickup.

| | |
| --- | --- |
| Model | `spectrum of V(t)` |
| Columns | `time_s`, `voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Signal frequency (Hz) (default 1000); Mains frequency (Hz) (default 50) |
| Physics code | [`sandbox/tools/analyze.py`](../../sandbox/tools/analyze.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `waveform` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Ground loop picking up mains hum | mV to hundreds of mV at the mains frequency and its odd harmonics | Connect every instrument to one ground point (never lift a safety earth), or use a differential probe if the hum stays. |
| Magnetic (inductive) pickup from a nearby transformer or cable loop |  | Twist the signal leads together, shrink the loop they enclose, and move them away from transformers and mains cables. |
| Aliasing (sample rate too low for the signal) |  | Raise the sample rate to at least ten times the highest signal frequency, or add a low-pass anti-aliasing filter before the input. |
| Unknown cause (none of the above fits well) |  | Re-record with short shielded leads and a second scope channel on the same signal, and compare the two spectra. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Connect all instruments to one ground point and re-record | 5 | Plug the scope and the source into the same outlet strip; remove any extra ground connections between them. *Safety:* Never lift or remove a safety (protective) earth. Change signal grounding only. |
| Twist the signal leads and move them away from transformers | 5 | Shorten and twist the cable pair; move it at least 30 cm from mains equipment. |
| Re-record at a higher sample rate | 2 | Increase the sample rate at least 10x and compare the dominant frequency. |

### Samples on the page

- **Trace with a hum on it**: [`scope_hum_1.csv`](../../data/seeded/scope_hum_1.csv). There is an extra slow wobble riding on the signal, a few hundred millivolts.
- **Clean trace**: [`scope_clean.csv`](../../data/seeded/scope_clean.csv). Nothing should look off: only the 1 kHz signal and a little noise.
- Sample result of *Connect all instruments to one ground point and re-record*: [`scope_hum_1_followup.csv`](../../data/seeded/scope_hum_1_followup.csv)

### The demo case

1. **Trace with a hum on it** ([`scope_hum_1.csv`](../../data/seeded/scope_hum_1.csv)): the leading cause is *Ground loop picking up mains hum* at 75%, with *Magnetic (inductive) pickup from a nearby transformer or cable loop* at 22%.
2. Recommended test: **Connect all instruments to one ground point and re-record** (5 min, 0.93 bits).
3. With its result ([`scope_hum_1_followup.csv`](../../data/seeded/scope_hum_1_followup.csv)): *Ground loop picking up mains hum*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`waveform/`](waveform/)); each gives the result above. [Excel export](waveform/excel_export.csv) · [Semicolons, decimal commas](waveform/semicolon_decimal_comma.csv) · [Tab-separated](waveform/tab_separated.tsv) · [UTF-16 "Unicode text"](waveform/unicode_text.txt) · [Other column names](waveform/other_column_names.csv)
