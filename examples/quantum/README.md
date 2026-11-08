# Quantum: example upload files

10 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Electron diffraction (de Broglie)

`electron_diffraction` · model `λ = h/√(2meV),  2d sin θ = λ,  D = 2L tan 2θ` · columns `voltage_kV`, `ring`, `diameter_mm`

Made from the sample **Both spacings 8% large** ([`data/seeded/ediff_camera_length.csv`](../../data/seeded/ediff_camera_length.csv)).

- *The bench:* The same tube, rings and voltages.
- *What looks off:* Both rings shrink with voltage as they should, but both lattice spacings come out about 8% large, by the same factor.

**Expected result:** Foil-to-screen distance L wrong (another tube's figure, or measured from the wrong point), 53% as the leading cause (with the page's defaults: Foil-to-screen distance L (mm) = 135; Inner ring spacing d₁₀ (nm) = 0.213; Outer ring spacing d₁₁ (nm) = 0.123; Diameter reading precision (mm) = 0.5).

Files: [Excel export](electron_diffraction/excel_export.csv) · [Semicolons, decimal commas](electron_diffraction/semicolon_decimal_comma.csv) · [Tab-separated](electron_diffraction/tab_separated.tsv) · [UTF-16 "Unicode text"](electron_diffraction/unicode_text.txt) · [Other column names](electron_diffraction/other_column_names.csv)

## Zeeman effect (cadmium red line)

`zeeman` · graduate · model `Δν̃ = 2μ_B B/hc = (1/2nt)·δ/Δ` · columns `field_mT`, `r1_inner_mm`, `r1_outer_mm`, `r2_inner_mm`, `r2_outer_mm`

Made from the sample **Bohr magneton 11% low** ([`data/seeded/zeeman_field_scale.csv`](../../data/seeded/zeeman_field_scale.csv)).

- *The bench:* The same lamp, étalon and fields.
- *What looks off:* The splitting is proportional to B, but its slope gives a Bohr magneton about 11% low.

**Expected result:** Field reading off (gaussmeter on the wrong scale or not zeroed), 53% as the leading cause (with the page's defaults: Étalon thickness t (mm) = 3; Étalon refractive index n = 1.457; Accepted Bohr magneton (J/T) = 9.27401e-24; Ring radius precision (mm) = 0.01; Gaussmeter precision (mT) = 2).

Files: [Excel export](zeeman/excel_export.csv) · [Semicolons, decimal commas](zeeman/semicolon_decimal_comma.csv) · [Tab-separated](zeeman/tab_separated.tsv) · [UTF-16 "Unicode text"](zeeman/unicode_text.txt) · [Other column names](zeeman/other_column_names.csv)

## Millikan oil drop

`millikan` · model `q = n·e` · columns `drop`, `charge_1e19C`

Made from the sample **e comes out 13% high** ([`data/seeded/millikan_spacing.csv`](../../data/seeded/millikan_spacing.csv)).

- *The bench:* Twenty drops from the same chamber, timed the same way.
- *What looks off:* The charges fall in clean whole steps, but the step comes out about 13% above e.

**Expected result:** Plate spacing wrong in the field E = V/d, 53% as the leading cause (with the page's defaults: Accepted e (C) = 1.60218e-19; Charge precision per drop (%) = 2; Plate spacing used for the charges (mm) = 7.6).

Files: [Excel export](millikan/excel_export.csv) · [Semicolons, decimal commas](millikan/semicolon_decimal_comma.csv) · [Tab-separated](millikan/tab_separated.tsv) · [UTF-16 "Unicode text"](millikan/unicode_text.txt) · [Other column names](millikan/other_column_names.csv)

## Photoelectric effect (h/e)

`photoelectric` · model `eV_s = hf − φ` · columns `wavelength_nm`, `stopping_voltage_V`

Made from the sample **h/e comes out 12% low** ([`data/seeded/photo_anode.csv`](../../data/seeded/photo_anode.csv)).

- *The bench:* The same lamp, filters and phototube.
- *What looks off:* The five points lie on a good straight line, but its slope gives h/e about 12% below the accepted value.

**Expected result:** Light reaching the anode (reverse photocurrent), 53% as the leading cause (with the page's defaults: Accepted h/e (V·s) = 4.13567e-15; Reading precision (V) = 0.01).

Files: [Excel export](photoelectric/excel_export.csv) · [Semicolons, decimal commas](photoelectric/semicolon_decimal_comma.csv) · [Tab-separated](photoelectric/tab_separated.tsv) · [UTF-16 "Unicode text"](photoelectric/unicode_text.txt) · [Other column names](photoelectric/other_column_names.csv)

## Franck–Hertz experiment (mercury)

`franck_hertz` · model `peaks at V = V_c + n·E₁/e` · columns `accelerating_voltage_V`, `anode_current_nA`

Made from the sample **Dips between the peaks are shallow** ([`data/seeded/fh_cool_oven.csv`](../../data/seeded/fh_cool_oven.csv)).

- *The bench:* The same tube and settings.
- *What looks off:* The peaks are still 4.9 V apart, but the dips are shallow, the current is higher and the first peak barely shows above the rise.

**Expected result:** Oven too cool (mercury vapour too thin), 53% as the leading cause (with the page's defaults: First excitation energy (eV) = 4.9; Peak reading precision (V) = 0.15; Oven set point (°C) = 180).

Files: [Excel export](franck_hertz/excel_export.csv) · [Semicolons, decimal commas](franck_hertz/semicolon_decimal_comma.csv) · [Tab-separated](franck_hertz/tab_separated.tsv) · [UTF-16 "Unicode text"](franck_hertz/unicode_text.txt) · [Other column names](franck_hertz/other_column_names.csv)

## Optical pumping of rubidium

`optical_pumping` · graduate · model `hf = g_F μ_B |k·I + B₀|` · columns `coil_current_A`, `frequency_kHz`, `isotope`

Made from the sample **Both g_F values 7% low** ([`data/seeded/rb_current_scale.csv`](../../data/seeded/rb_current_scale.csv)).

- *The bench:* The same cell and coils.
- *What looks off:* Both isotopes give straight lines through zero with the right 3:2 ratio, but both g_F values come out about 7% low.

**Expected result:** Coil current read high or low (ammeter or sense resistor), 53% as the leading cause (with the page's defaults: Sweep coil constant k (µT/A) = 60; Resonance reading precision (kHz) = 1).

Files: [Excel export](optical_pumping/excel_export.csv) · [Semicolons, decimal commas](optical_pumping/semicolon_decimal_comma.csv) · [Tab-separated](optical_pumping/tab_separated.tsv) · [UTF-16 "Unicode text"](optical_pumping/unicode_text.txt) · [Other column names](optical_pumping/other_column_names.csv)

## Planck's constant from LEDs

`planck_led` · model `eV = hf − φ` · columns `wavelength_nm`, `turn_on_voltage_V`

Made from the sample **h comes out 10% low** ([`data/seeded/planck_gain.csv`](../../data/seeded/planck_gain.csv)).

- *The bench:* The same seven LEDs and the same turn-on method.
- *What looks off:* The points lie on a good straight line, but its slope gives h about 10% below the accepted value.

**Expected result:** Voltmeter reading low or high (gain error), 52% as the leading cause (with the page's defaults: Accepted h (J·s) = 6.62607e-34; Reading precision (V) = 0.015).

Files: [Excel export](planck_led/excel_export.csv) · [Semicolons, decimal commas](planck_led/semicolon_decimal_comma.csv) · [Tab-separated](planck_led/tab_separated.tsv) · [UTF-16 "Unicode text"](planck_led/unicode_text.txt) · [Other column names](planck_led/other_column_names.csv)

## Quantum tunnelling simulation

`tunnelling` · model `T ≈ e^(−2κa), κ = √(2m(V₀−E))/ħ` · columns `barrier_width_nm`, `transmission`

Made from the sample **Decays far too slowly** ([`data/seeded/tunnel_mass.csv`](../../data/seeded/tunnel_mass.csv)).

- *The bench:* The same barrier simulation.
- *What looks off:* Transmission falls exponentially, but far more slowly than an electron at this energy should.

**Expected result:** Particle mass wrong in the simulation (units or effective mass), 55% as the leading cause (with the page's defaults: Barrier height V₀ (eV) = 1; Particle energy E (eV) = 0.5; Mass (electron masses) = 1).

Files: [Excel export](tunnelling/excel_export.csv) · [Semicolons, decimal commas](tunnelling/semicolon_decimal_comma.csv) · [Tab-separated](tunnelling/tab_separated.tsv) · [UTF-16 "Unicode text"](tunnelling/unicode_text.txt) · [Other column names](tunnelling/other_column_names.csv)

## Blackbody radiation

`blackbody` · model `B(λ,T) ∝ λ⁻⁵ / (e^(hc/λkT) − 1)` · columns `wavelength_nm`, `spectral_radiance`

Made from the sample **Lamp looks 3% cooler than rated** ([`data/seeded/blackbody_shift.csv`](../../data/seeded/blackbody_shift.csv)).

- *The bench:* The same lamp and spectrometer.
- *What looks off:* Planck's law fits, but only at about 2715 K, 3% below the lamp's rating.

**Expected result:** Spectrometer wavelength scale shifted, 52% as the leading cause (with the page's defaults: Expected lamp temperature (K) = 2800).

Files: [Excel export](blackbody/excel_export.csv) · [Semicolons, decimal commas](blackbody/semicolon_decimal_comma.csv) · [Tab-separated](blackbody/tab_separated.tsv) · [UTF-16 "Unicode text"](blackbody/unicode_text.txt) · [Other column names](blackbody/other_column_names.csv)

## Atomic spectral lines (hydrogen)

`spectral_lines` · model `1/λ = R(1/2² − 1/n²)` · columns `n_upper`, `wavelength_nm`

Made from the sample **One line is off the series** ([`data/seeded/balmer_impurity.csv`](../../data/seeded/balmer_impurity.csv)).

- *The bench:* The same five Balmer lines.
- *What looks off:* Four lines fit the Rydberg formula, but the one taken as n = 5 is almost 2 nm out.

**Expected result:** A line from another element mistaken for a hydrogen line, 53% as the leading cause (with the page's defaults: Accepted Rydberg constant (/m) = 1.0967758e7; Reading precision (nm) = 0.1).

Files: [Excel export](spectral_lines/excel_export.csv) · [Semicolons, decimal commas](spectral_lines/semicolon_decimal_comma.csv) · [Tab-separated](spectral_lines/tab_separated.tsv) · [UTF-16 "Unicode text"](spectral_lines/unicode_text.txt) · [Other column names](spectral_lines/other_column_names.csv)
