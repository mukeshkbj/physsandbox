# Waves & sound

1 experiment on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Waves & sound*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Speed of sound (resonance tube)](#speed-of-sound-resonance-tube) | teaching lab | `L + e = v/4f, e ≈ 0.3 D` | Read the air temperature inside the tube | [Excel](resonance_tube/excel_export.csv) · [Semicolons](resonance_tube/semicolon_decimal_comma.csv) · [Tabs](resonance_tube/tab_separated.tsv) · [UTF-16](resonance_tube/unicode_text.txt) · [Renamed](resonance_tube/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Speed of sound (resonance tube)

First resonance length of a closed tube against 1/f, to measure the speed of sound.

| | |
| --- | --- |
| Model | `L + e = v/4f, e ≈ 0.3 D` |
| Columns | `frequency_Hz`, `resonance_length_m` (one row per reading; `#` lines are comments) |
| You enter | Air temperature (°C) (default 20); Tube inner diameter (m) (default 0.035); Length reading precision (mm) (default 1) |
| Physics code | [`sandbox/tools/bench_classical.py`](../../sandbox/tools/bench_classical.py), fitted inside the glovebox |
| Fault library | [`faults/bench_classical.yaml`](../../faults/bench_classical.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `resonance_tube` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Air in the tube not at the temperature entered | Air 14 °C warmer than entered makes v about 2.4% high (v = 331.3√(1 + T/273.15) m/s) | Enter the temperature measured inside the tube (or let the water and air settle to room temperature) and compare with v at that temperature. |
| Signal generator frequency dial reading off | Analogue generator dials are often 2–5% off, which scales v by the same amount | Read the frequency on a counter or oscilloscope instead of the dial, or correct every frequency by the measured ratio, then refit. |
| Lengths read from the wrong zero (not the tube's open end) | The intercept should be −0.3 × diameter (about −1 cm); a ruler zero 2.5 cm off moves it to +1.5 cm | Measure every length from the open end of the tube to the water surface, or subtract the ruler's offset, and refit. |
| Unknown cause (none of the above fits well) |  | Check that each length is the first (shortest) resonance and repeat the sweep listening for the loudest point. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the air temperature inside the tube | 3 | Lower a thermometer down the tube at several depths, without touching the water, and compare with the temperature you entered. *Safety:* If the reservoir was filled from the hot tap, the water can scald; don't put your hand in it. |
| Read the generator's frequency on a counter or oscilloscope | 6 | Connect a frequency counter (or a scope) to the generator output and compare with the dial at three settings. *Safety:* Keep the speaker volume low; tones at resonance are loud, so don't hold your ear over the tube. |
| Check where the ruler's zero sits against the tube's open end | 1 | Hold a set square across the top of the tube and read the ruler there. |

### Samples on the page

- **Speed of sound 2.5% high**: [`sound_warm_air.csv`](../../data/seeded/sound_warm_air.csv). The points lie on a good straight line, but its slope gives a speed of sound about 2.5% above the value for 20 °C.
- **Lengths all a few cm long**: [`sound_ruler_zero.csv`](../../data/seeded/sound_ruler_zero.csv). The speed of sound is right, but every length is a few centimetres longer than expected, and the end correction comes out negative.
- **Healthy measurement**: [`sound_clean.csv`](../../data/seeded/sound_clean.csv). Nothing should look off: the slope gives v at 20 °C and the intercept is the end correction, about 0.3 × diameter.
- Sample result of *Read the air temperature inside the tube*: [`sound_warm_air_thermometer.csv`](../../data/seeded/sound_warm_air_thermometer.csv)

### The demo case

1. **Speed of sound 2.5% high** ([`sound_warm_air.csv`](../../data/seeded/sound_warm_air.csv)): the leading cause is *Air in the tube not at the temperature entered* at 53%, with *Signal generator frequency dial reading off* at 45%.
2. Recommended test: **Read the air temperature inside the tube** (3 min, 0.99 bits).
3. With its result ([`sound_warm_air_thermometer.csv`](../../data/seeded/sound_warm_air_thermometer.csv)): *Air in the tube not at the temperature entered*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`resonance_tube/`](resonance_tube/)); each gives the result above. [Excel export](resonance_tube/excel_export.csv) · [Semicolons, decimal commas](resonance_tube/semicolon_decimal_comma.csv) · [Tab-separated](resonance_tube/tab_separated.tsv) · [UTF-16 "Unicode text"](resonance_tube/unicode_text.txt) · [Other column names](resonance_tube/other_column_names.csv)
