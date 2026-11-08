# Electricity: example upload files

4 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Low-resistance measurement

`resistance_4wire` · model `V = I·R` · columns `current_A`, `voltage_V`

Made from the sample **Resistor reads high at low current** ([`data/seeded/r_offset_1.csv`](../../data/seeded/r_offset_1.csv)).

- *The bench:* Four-wire V–I sweep of a 10 mΩ resistor: 10 currents from 10 to 100 mA, read on a nanovoltmeter.
- *What looks off:* The voltage is too high, most of all at low current, so the apparent resistance falls as the current rises.

**Expected result:** Thermoelectric (thermal EMF) offset at a contact, 64% as the leading cause (with the page's defaults: Expected resistance (Ω) = 0.01).

Files: [Excel export](resistance_4wire/excel_export.csv) · [Semicolons, decimal commas](resistance_4wire/semicolon_decimal_comma.csv) · [Tab-separated](resistance_4wire/tab_separated.tsv) · [UTF-16 "Unicode text"](resistance_4wire/unicode_text.txt) · [Other column names](resistance_4wire/other_column_names.csv)

## RC charging curve

`rc_charging` · model `V = V₀(1 − e^(−t/RC))` · columns `time_s`, `voltage_V`

Made from the sample **Charges to half the supply, too fast** ([`data/seeded/rc_probe_loading.csv`](../../data/seeded/rc_probe_loading.csv)).

- *The bench:* 1 MΩ resistor charging a 100 nF capacitor from 5 V, captured on an oscilloscope over 0.6 s.
- *What looks off:* The capacitor only reaches about half the supply voltage, and gets there in about half the expected time constant (0.1 s).

**Expected result:** Oscilloscope probe loading the circuit (x1 probe, 1 MΩ), 58% as the leading cause (with the page's defaults: Supply voltage (V) = 5; Resistor (Ω) = 1000000; Capacitor (F) = 1e-07).

Files: [Excel export](rc_charging/excel_export.csv) · [Semicolons, decimal commas](rc_charging/semicolon_decimal_comma.csv) · [Tab-separated](rc_charging/tab_separated.tsv) · [UTF-16 "Unicode text"](rc_charging/unicode_text.txt) · [Other column names](rc_charging/other_column_names.csv)

## Diode I–V curve

`diode` · model `V = nV_T ln(I/I_s) + I·R_s` · columns `voltage_V`, `current_A`

Made from the sample **Curve bends over at high current** ([`data/seeded/diode_burden.csv`](../../data/seeded/diode_burden.csv)).

- *The bench:* Forward I–V sweep of a silicon signal diode, 1 µA to 50 mA, with a multimeter as voltmeter and a second as ammeter.
- *What looks off:* The exponential curve bends over above a few mA, as if a resistance of about 10 Ω were in series.

**Expected result:** Voltmeter across diode and ammeter (ammeter burden voltage), 57% as the leading cause (with the page's defaults: Temperature (K) = 300; Largest normal series R (Ω) = 1).

Files: [Excel export](diode/excel_export.csv) · [Semicolons, decimal commas](diode/semicolon_decimal_comma.csv) · [Tab-separated](diode/tab_separated.tsv) · [UTF-16 "Unicode text"](diode/unicode_text.txt) · [Other column names](diode/other_column_names.csv)

## Series RLC resonance

`rlc_resonance` · model `V_R = V R / √((R + R_L)² + (ωL − 1/ωC)²)` · columns `frequency_Hz`, `resistor_V`

Made from the sample **Peak low and broad, f₀ right** ([`data/seeded/rlc_generator_loading.csv`](../../data/seeded/rlc_generator_loading.csv)).

- *The bench:* The same circuit, generator set to 2.00 V, resistor voltage on the scope from 1.5 to 15 kHz.
- *What looks off:* The curve fits the resonance shape and peaks at the right frequency, but the peak is about 30% low and Q comes out 1.9, not 2.7.

**Expected result:** Generator's 50 Ω output impedance pulling the drive down near resonance (input not held constant), 53% as the leading cause (with the page's defaults: Inductance L (H) = 0.01; Capacitance C (F) = 1e-07; Resistor R (Ω) = 100; Coil resistance R_L (Ω) = 18; Input amplitude (V) = 2; Voltage reading precision (%) = 1).

Files: [Excel export](rlc_resonance/excel_export.csv) · [Semicolons, decimal commas](rlc_resonance/semicolon_decimal_comma.csv) · [Tab-separated](rlc_resonance/tab_separated.tsv) · [UTF-16 "Unicode text"](rlc_resonance/unicode_text.txt) · [Other column names](rlc_resonance/other_column_names.csv)
