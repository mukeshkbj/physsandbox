# Condensed matter: example upload files

3 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## X-ray Bragg diffraction (NaCl)

`bragg_xray` · graduate · model `nλ = 2d sin θ` · columns `order_n`, `angle_deg`

Made from the sample **The orders disagree on d** ([`data/seeded/bragg_zero_offset.csv`](../../data/seeded/bragg_zero_offset.csv)).

- *The bench:* The same tube, crystal and scan.
- *What looks off:* d comes out small from the first order and closer to 282 pm from the fourth: the orders disagree.

**Expected result:** Goniometer zero misset (every angle read from a wrong zero), 53% as the leading cause (with the page's defaults: X-ray wavelength, Mo Kα (pm) = 71.07; NaCl (200) spacing d (pm) = 282; Peak angle precision (°) = 0.05; Mo Kβ wavelength (pm) = 63.26).

Files: [Excel export](bragg_xray/excel_export.csv) · [Semicolons, decimal commas](bragg_xray/semicolon_decimal_comma.csv) · [Tab-separated](bragg_xray/tab_separated.tsv) · [UTF-16 "Unicode text"](bragg_xray/unicode_text.txt) · [Other column names](bragg_xray/other_column_names.csv)

## Superconducting transition

`sc_transition` · graduate · model `R(T) = R_n(T) / (1 + e^(−(T−Tc)/w))` · columns `temperature_K`, `resistance_mOhm`

Made from the sample **Transition low and broad** ([`data/seeded/sc_lag.csv`](../../data/seeded/sc_lag.csv)).

- *The bench:* The same pellet, current and cooling sweep.
- *What looks off:* The resistance drops to zero, but about 1.5 K low and spread over more than 2 K.

**Expected result:** Thermometer not at the sample's temperature (lag or gradient), 54% as the leading cause (with the page's defaults: Expected Tc (K) = 92; Expected 10–90% width (K) = 1; Reading precision (mΩ) = 0.01).

Files: [Excel export](sc_transition/excel_export.csv) · [Semicolons, decimal commas](sc_transition/semicolon_decimal_comma.csv) · [Tab-separated](sc_transition/tab_separated.tsv) · [UTF-16 "Unicode text"](sc_transition/unicode_text.txt) · [Other column names](sc_transition/other_column_names.csv)

## Band gap of germanium

`band_gap` · graduate · model `R ∝ T^(−3/2) e^(Eg/2kT)` · columns `temperature_K`, `resistance_ohm`

Made from the sample **Band gap 9% high** ([`data/seeded/bandgap_lag.csv`](../../data/seeded/bandgap_lag.csv)).

- *The bench:* The same bar, current and oven, 340 to 450 K while heating.
- *What looks off:* The plot is a straight line, but its slope gives a band gap about 9% above 0.67 eV.

**Expected result:** Sample lagging the oven's thermometer while it heats, 56% as the leading cause (with the page's defaults: Expected band gap (eV): Ge 0.67, Si 1.12 = 0.67; Resistance reading precision (%) = 0.5; Temperature reading precision (K) = 0.5).

Files: [Excel export](band_gap/excel_export.csv) · [Semicolons, decimal commas](band_gap/semicolon_decimal_comma.csv) · [Tab-separated](band_gap/tab_separated.tsv) · [UTF-16 "Unicode text"](band_gap/unicode_text.txt) · [Other column names](band_gap/other_column_names.csv)
