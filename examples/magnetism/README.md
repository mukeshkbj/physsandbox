# Magnetism: example upload files

7 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Helmholtz coil calibration

`helmholtz` · model `B = (4/5)^(3/2) μ₀NI/R` · columns `current_A`, `measured_B_uT`

Made from the sample **Field doesn't start at zero** ([`data/seeded/helmholtz_ambient.csv`](../../data/seeded/helmholtz_ambient.csv)).

- *The bench:* Hall-probe field at the centre of a Helmholtz pair (R = 15 cm, 100 turns each) for currents 0.1–1 A.
- *What looks off:* The slope matches theory, but the line doesn't pass through zero: there is about 45 µT of field at zero current.

**Expected result:** Earth's field or nearby steel adding to the coil field, 64% as the leading cause (with the page's defaults: Coil radius (m) = 0.15; Turns per coil = 100).

Files: [Excel export](helmholtz/excel_export.csv) · [Semicolons, decimal commas](helmholtz/semicolon_decimal_comma.csv) · [Tab-separated](helmholtz/tab_separated.tsv) · [UTF-16 "Unicode text"](helmholtz/unicode_text.txt) · [Other column names](helmholtz/other_column_names.csv)

## Faraday's law of induction

`faraday` · model `ε = −N dΦ/dt` · columns `time_s`, `magnetic_flux_Wb`, `induced_voltage_V`

Made from the sample **EMF sits on a DC offset** ([`data/seeded/faraday_offset.csv`](../../data/seeded/faraday_offset.csv)).

- *The bench:* Coil of 200 turns in a 10 Hz sinusoidal flux (0.1 mWb peak); induced voltage recorded through an amplifier.
- *What looks off:* The induced voltage has the right size and shape, but the whole trace is shifted up by about 0.15 V.

**Expected result:** Amplifier input offset voltage, 54% as the leading cause (with the page's defaults: Turns on the coil = 200).

Files: [Excel export](faraday/excel_export.csv) · [Semicolons, decimal commas](faraday/semicolon_decimal_comma.csv) · [Tab-separated](faraday/tab_separated.tsv) · [UTF-16 "Unicode text"](faraday/unicode_text.txt) · [Other column names](faraday/other_column_names.csv)

## Hall effect

`hall` · model `V_H = IB / (n e t)` · columns `current_A`, `hall_voltage_V`

Made from the sample **Carrier density 25% high** ([`data/seeded/hall_misaligned.csv`](../../data/seeded/hall_misaligned.csv)).

- *The bench:* Hall voltage of a 1 mm thick sample in 0.3 T, for sample currents 1–10 mA.
- *What looks off:* The line goes through zero, but its slope gives a carrier density about 25% above the expected 1×10²¹ /m³.

**Expected result:** Hall contacts not exactly opposite each other, 55% as the leading cause (with the page's defaults: Field (T) = 0.3; Sample thickness (m) = 0.001; Expected carrier density (/m³) = 1e+21).

Files: [Excel export](hall/excel_export.csv) · [Semicolons, decimal commas](hall/semicolon_decimal_comma.csv) · [Tab-separated](hall/tab_separated.tsv) · [UTF-16 "Unicode text"](hall/unicode_text.txt) · [Other column names](hall/other_column_names.csv)

## Magnetic hysteresis (B–H loop)

`hysteresis` · model `H = N₁I/ℓ,  B = Φ/(N₂A)` · columns `H_A_per_m`, `B_T`

Made from the sample **Loop 12% too short** ([`data/seeded/hysteresis_turns.csv`](../../data/seeded/hysteresis_turns.csv)).

- *The bench:* The same core, windings and fluxmeter.
- *What looks off:* The loop closes and has the expected coercivity, but it is about 12% too short: 1.25 T at the tips and 0.72 T remanence.

**Expected result:** Search coil's turns not as stated, 53% as the leading cause (with the page's defaults: Expected coercivity (A/m) = 45; Expected remanence (T) = 0.83; Expected B at the loop tip (T) = 1.42; Search-coil turns N₂ used to work out B = 100; B reading precision (T) = 0.005; H reading precision (A/m) = 2).

Files: [Excel export](hysteresis/excel_export.csv) · [Semicolons, decimal commas](hysteresis/semicolon_decimal_comma.csv) · [Tab-separated](hysteresis/tab_separated.tsv) · [UTF-16 "Unicode text"](hysteresis/unicode_text.txt) · [Other column names](hysteresis/other_column_names.csv)

## e/m of the electron (fine-beam tube)

`e_over_m` · model `e/m = 2V/(B r)²,  B = (4/5)^(3/2) μ₀NI/R` · columns `accelerating_voltage_V`, `coil_current_A`, `beam_radius_cm`

Made from the sample **e/m 11% high at every voltage** ([`data/seeded/em_parallax.csv`](../../data/seeded/em_parallax.csv)).

- *The bench:* The same tube and coils, another group's run at the same voltages.
- *What looks off:* e/m comes out about 11% high, by the same amount at every voltage and current.

**Expected result:** Beam diameter read with parallax (scale not in the plane of the beam), 53% as the leading cause (with the page's defaults: Coil radius R (m) = 0.15; Turns per coil N = 130; Beam radius reading precision (cm) = 0.05; Accepted e/m (C/kg) = 1.75882e+11; Hall probe precision (mT) = 0.01).

Files: [Excel export](e_over_m/excel_export.csv) · [Semicolons, decimal commas](e_over_m/semicolon_decimal_comma.csv) · [Tab-separated](e_over_m/tab_separated.tsv) · [UTF-16 "Unicode text"](e_over_m/unicode_text.txt) · [Other column names](e_over_m/other_column_names.csv)

## Electron spin resonance (DPPH)

`esr` · graduate · model `h f = g μ_B B` · columns `rf_frequency_MHz`, `resonance_field_mT`

Made from the sample **Line misses the origin** ([`data/seeded/esr_probe_offset.csv`](../../data/seeded/esr_probe_offset.csv)).

- *The bench:* The same sample, coils and gaussmeter.
- *What looks off:* The slope gives the right g, but the line doesn't pass through the origin: every resonance sits about 0.1 mT high.

**Expected result:** Field zero offset (Hall probe not zeroed, or a residual field along the coils), 53% as the leading cause (with the page's defaults: g-factor of DPPH = 2.0036; Resonance field reading precision (mT) = 0.01).

Files: [Excel export](esr/excel_export.csv) · [Semicolons, decimal commas](esr/semicolon_decimal_comma.csv) · [Tab-separated](esr/tab_separated.tsv) · [UTF-16 "Unicode text"](esr/unicode_text.txt) · [Other column names](esr/other_column_names.csv)

## Pulsed NMR spin echo

`nmr_echo` · graduate · model `A(2τ) = A₀ e^(−2τ/T₂)` · columns `echo_time_ms`, `echo_amplitude_mV`

Made from the sample **Echo only half its usual size** ([`data/seeded/nmr_pulse_misset.csv`](../../data/seeded/nmr_pulse_misset.csv)).

- *The bench:* The same doped-water sample and the same echo sequence.
- *What looks off:* The decay has the right T₂, but the echo starts at about 290 mV instead of 500 mV.

**Expected result:** RF pulses not 90° and 180° (pulse length mis-set), 53% as the leading cause (with the page's defaults: Expected T₂ (ms) = 20; Echo amplitude on the reference sample (mV) = 500; 90° pulse length set (µs) = 10; Reading precision (mV) = 3).

Files: [Excel export](nmr_echo/excel_export.csv) · [Semicolons, decimal commas](nmr_echo/semicolon_decimal_comma.csv) · [Tab-separated](nmr_echo/tab_separated.tsv) · [UTF-16 "Unicode text"](nmr_echo/unicode_text.txt) · [Other column names](nmr_echo/other_column_names.csv)
