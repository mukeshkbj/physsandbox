# Waves & sound: example upload files

1 experiment. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Speed of sound (resonance tube)

`resonance_tube` · model `L + e = v/4f, e ≈ 0.3 D` · columns `frequency_Hz`, `resonance_length_m`

Made from the sample **Speed of sound 2.5% high** ([`data/seeded/sound_warm_air.csv`](../../data/seeded/sound_warm_air.csv)).

- *The bench:* The same tube and generator, with the air temperature entered as 20 °C.
- *What looks off:* The points lie on a good straight line, but its slope gives a speed of sound about 2.5% above the value for 20 °C.

**Expected result:** Air in the tube not at the temperature entered, 53% as the leading cause (with the page's defaults: Air temperature (°C) = 20; Tube inner diameter (m) = 0.035; Length reading precision (mm) = 1).

Files: [Excel export](resonance_tube/excel_export.csv) · [Semicolons, decimal commas](resonance_tube/semicolon_decimal_comma.csv) · [Tab-separated](resonance_tube/tab_separated.tsv) · [UTF-16 "Unicode text"](resonance_tube/unicode_text.txt) · [Other column names](resonance_tube/other_column_names.csv)
