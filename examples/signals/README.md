# Signals: example upload files

1 experiment. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Oscilloscope trace

`waveform` · model `spectrum of V(t)` · columns `time_s`, `voltage_V`

Made from the sample **Trace with a hum on it** ([`data/seeded/scope_hum_1.csv`](../../data/seeded/scope_hum_1.csv)).

- *The bench:* Oscilloscope capture of a 1 kHz, 1 V test signal: 2,000 samples at 10 kHz.
- *What looks off:* There is an extra slow wobble riding on the signal, a few hundred millivolts.

**Expected result:** Ground loop picking up mains hum, 75% as the leading cause (with the page's defaults: Signal frequency (Hz) = 1000; Mains frequency (Hz) = 50).

Files: [Excel export](waveform/excel_export.csv) · [Semicolons, decimal commas](waveform/semicolon_decimal_comma.csv) · [Tab-separated](waveform/tab_separated.tsv) · [UTF-16 "Unicode text"](waveform/unicode_text.txt) · [Other column names](waveform/other_column_names.csv)
