# Heat: example upload files

4 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Newton's law of cooling

`cooling` · model `T = T_room + ΔT e^(−t/τ)` · columns `time_s`, `temperature_C`

Made from the sample **Settles 2.5 °C above the room** ([`data/seeded/cooling_cjc_offset.csv`](../../data/seeded/cooling_cjc_offset.csv)).

- *The bench:* A sample at 80 °C cooling in a 21 °C room, logged every minute for 30 minutes with a K-type thermocouple.
- *What looks off:* It cools at the expected rate, but settles about 2.5 °C above the room temperature.

**Expected result:** Thermocouple cold-junction compensation error, 55% as the leading cause (with the page's defaults: Room temperature (°C) = 21; Expected time constant (s) = 420).

Files: [Excel export](cooling/excel_export.csv) · [Semicolons, decimal commas](cooling/semicolon_decimal_comma.csv) · [Tab-separated](cooling/tab_separated.tsv) · [UTF-16 "Unicode text"](cooling/unicode_text.txt) · [Other column names](cooling/other_column_names.csv)

## Stefan–Boltzmann law (lamp filament)

`stefan_lamp` · model `P = εσA T⁴,  R/R₀ = (T/T₀)^1.209` · columns `voltage_V`, `current_A`

Made from the sample **Exponent below 4, worst when cold** ([`data/seeded/stefan_ammeter_zero.csv`](../../data/seeded/stefan_ammeter_zero.csv)).

- *The bench:* The same lamp and meters, from 1.5 to 12 V.
- *What looks off:* The exponent comes out about 3.8, not 4: power ÷ T⁴ climbs at the cold end, by about a fifth at the coldest point.

**Expected result:** Ammeter zero not set (reads current with none flowing), 53% as the leading cause (with the page's defaults: Cold filament resistance R₀ (Ω) = 1.6; Room temperature T₀ (K) = 293; Meter precision (%) = 0.5).

Files: [Excel export](stefan_lamp/excel_export.csv) · [Semicolons, decimal commas](stefan_lamp/semicolon_decimal_comma.csv) · [Tab-separated](stefan_lamp/tab_separated.tsv) · [UTF-16 "Unicode text"](stefan_lamp/unicode_text.txt) · [Other column names](stefan_lamp/other_column_names.csv)

## Thermal conductivity (Lee's disc)

`lees_disc` · model `k = m c (dT/dt)|T₂ · x / (A (T₁ − T₂))` · columns `stage`, `time_s`, `steam_C`, `disc_C`

Made from the sample **Conductivity 10% low** ([`data/seeded/leesdisc_thermometer_offset.csv`](../../data/seeded/leesdisc_thermometer_offset.csv)).

- *The bench:* The same apparatus and sample, the same two stages.
- *What looks off:* The cooling curve looks normal, but k comes out about 10% below 0.19 W/m·K.

**Expected result:** The two thermometers disagree (calibration offset between them), 53% as the leading cause (with the page's defaults: Expected conductivity k (W/m·K) = 0.19; Sample thickness x (mm) = 3; Disc diameter (mm) = 110; Brass disc heat capacity m·c (J/K) = 335; Thermometer precision (K) = 0.1).

Files: [Excel export](lees_disc/excel_export.csv) · [Semicolons, decimal commas](lees_disc/semicolon_decimal_comma.csv) · [Tab-separated](lees_disc/tab_separated.tsv) · [UTF-16 "Unicode text"](lees_disc/unicode_text.txt) · [Other column names](lees_disc/other_column_names.csv)

## Thermocouple calibration (type K)

`thermocouple` · model `emf = S(T − T_ref) + q(T − T_ref)²,  S ≈ 41 µV/K` · columns `hot_junction_C`, `emf_mV`

Made from the sample **Every emf 0.3 mV low** ([`data/seeded/thermocouple_ice_melted.csv`](../../data/seeded/thermocouple_ice_melted.csv)).

- *The bench:* The same thermocouple, bath, meter and reference flask.
- *What looks off:* The slope matches type K, but every emf sits about 0.3 mV below the table.

**Expected result:** Reference junction not at 0 °C (ice melted, or the junction out of the ice), 56% as the leading cause (with the page's defaults: Reference junction temperature (°C) = 0; Emf reading precision (mV) = 0.01; Bath thermometer precision (°C) = 0.2).

Files: [Excel export](thermocouple/excel_export.csv) · [Semicolons, decimal commas](thermocouple/semicolon_decimal_comma.csv) · [Tab-separated](thermocouple/tab_separated.tsv) · [UTF-16 "Unicode text"](thermocouple/unicode_text.txt) · [Other column names](thermocouple/other_column_names.csv)
