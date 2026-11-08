# Nuclear & particle: example upload files

5 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Gamma-ray attenuation in lead

`gamma_attenuation` · model `N = N₀ e^(−μx),  μ = (μ/ρ)·ρ` · columns `thickness_mm`, `counts`

Made from the sample **Counts level off behind thick lead** ([`data/seeded/gamma_background.csv`](../../data/seeded/gamma_background.csv)).

- *The bench:* The same source, lead sheets and GM tube, with the same 0.5 /s background subtracted.
- *What looks off:* The thin end follows the expected line, but from about 30 mm of lead on the counts level off well above it.

**Expected result:** Background during the run higher than the figure subtracted, 53% as the leading cause (with the page's defaults: Mass attenuation coefficient of lead at 662 keV (cm²/g) = 0.11; Lead density (g/cm³) = 11.34; Count time per reading (s) = 300; Background you subtracted (counts/s) = 0.5).

Files: [Excel export](gamma_attenuation/excel_export.csv) · [Semicolons, decimal commas](gamma_attenuation/semicolon_decimal_comma.csv) · [Tab-separated](gamma_attenuation/tab_separated.tsv) · [UTF-16 "Unicode text"](gamma_attenuation/unicode_text.txt) · [Other column names](gamma_attenuation/other_column_names.csv)

## Muon lifetime

`muon_lifetime` · graduate · model `N(t) = A e^(−t/τ) + B` · columns `time_us`, `counts`

Made from the sample **Flat background ten times the usual** ([`data/seeded/muon_light_leak.csv`](../../data/seeded/muon_light_leak.csv)).

- *The bench:* The same detector, timer and counting time.
- *What looks off:* The decay has the expected lifetime, but it sits on a flat background about ten times the usual, so τ is less precise.

**Expected result:** Light leak in the scintillator's wrapping (room light making random pulses), 53% as the leading cause (with the page's defaults: Expected lifetime in plastic scintillator, μ⁺ and μ⁻ together (µs) = 2.12; Start the fit at (µs) = 1).

Files: [Excel export](muon_lifetime/excel_export.csv) · [Semicolons, decimal commas](muon_lifetime/semicolon_decimal_comma.csv) · [Tab-separated](muon_lifetime/tab_separated.tsv) · [UTF-16 "Unicode text"](muon_lifetime/unicode_text.txt) · [Other column names](muon_lifetime/other_column_names.csv)

## Radioactive decay (Geiger–Müller)

`radioactive_decay` · model `N = N₀ e^(−λt) + B, t½ = ln 2 / λ` · columns `time_s`, `counts`

Made from the sample **Counts level off instead of falling to zero** ([`data/seeded/decay_background.csv`](../../data/seeded/decay_background.csv)).

- *The bench:* The same generator, counter and intervals, starting at about 120 counts per second.
- *What looks off:* The decay starts at the right rate, but after about 15 minutes the counts level off near 8 per interval instead of falling towards zero.

**Expected result:** Room background not subtracted, 54% as the leading cause (with the page's defaults: Expected half-life (s) = 153.1; Counter dead time (µs) = 150).

Files: [Excel export](radioactive_decay/excel_export.csv) · [Semicolons, decimal commas](radioactive_decay/semicolon_decimal_comma.csv) · [Tab-separated](radioactive_decay/tab_separated.tsv) · [UTF-16 "Unicode text"](radioactive_decay/unicode_text.txt) · [Other column names](radioactive_decay/other_column_names.csv)

## Rutherford scattering (alphas on gold)

`rutherford` · graduate · model `N(θ) ∝ 1/sin⁴(θ/2)` · columns `angle_deg`, `counts`, `live_time_s`

Made from the sample **Small angles count too fast** ([`data/seeded/ruth_zero_offset.csv`](../../data/seeded/ruth_zero_offset.csv)).

- *The bench:* The same source, foil, detector and live times.
- *What looks off:* The larger angles follow 1/sin⁴(θ/2), but at 10° and 15° the rate is well above that curve.

**Expected result:** Detector angle zero misset (scale zero not on the beam axis), 53% as the leading cause (with the page's defaults: Count rate at 20° on the lab sheet (/s) = 1.2).

Files: [Excel export](rutherford/excel_export.csv) · [Semicolons, decimal commas](rutherford/semicolon_decimal_comma.csv) · [Tab-separated](rutherford/tab_separated.tsv) · [UTF-16 "Unicode text"](rutherford/unicode_text.txt) · [Other column names](rutherford/other_column_names.csv)

## Compton scattering

`compton` · graduate · model `E′ = E / (1 + (E/m_e c²)(1 − cos θ))` · columns `angle_deg`, `energy_keV`

Made from the sample **m_e c² and 662 keV both read low** ([`data/seeded/compton_gain.csv`](../../data/seeded/compton_gain.csv)).

- *The bench:* The same source, scatterer and detector.
- *What looks off:* The points follow a Compton-like curve, but the fit puts the unscattered line near 629 keV and m_e c² about 5% low.

**Expected result:** MCA energy calibration gain off (PMT voltage or temperature drift), 54% as the leading cause (with the page's defaults: Source line energy (keV) = 661.66; Accepted m_e c² (keV) = 510.999; Photopeak reading precision (keV) = 2).

Files: [Excel export](compton/excel_export.csv) · [Semicolons, decimal commas](compton/semicolon_decimal_comma.csv) · [Tab-separated](compton/tab_separated.tsv) · [UTF-16 "Unicode text"](compton/unicode_text.txt) · [Other column names](compton/other_column_names.csv)
