# Mechanics: example upload files

7 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Simple pendulum

`pendulum` · model `T = 2π√(L/g)` · columns `length_m`, `period_s`

Made from the sample **g comes out 3% low** ([`data/seeded/pendulum_large_amp.csv`](../../data/seeded/pendulum_large_amp.csv)).

- *The bench:* Period of a simple pendulum at 11 lengths from 0.2 to 1.2 m, each timed over 10 swings.
- *What looks off:* T² against L is a straight line through the origin, but its slope gives g about 3% below 9.81 m/s².

**Expected result:** Too large a release angle, 54% as the leading cause (with the page's defaults: Expected g (m/s²) = 9.81).

Files: [Excel export](pendulum/excel_export.csv) · [Semicolons, decimal commas](pendulum/semicolon_decimal_comma.csv) · [Tab-separated](pendulum/tab_separated.tsv) · [UTF-16 "Unicode text"](pendulum/unicode_text.txt) · [Other column names](pendulum/other_column_names.csv)

## Hooke's law spring

`hooke` · model `F = mg = k·x` · columns `mass_kg`, `extension_m`

Made from the sample **Force line misses the origin** ([`data/seeded/hooke_hanger.csv`](../../data/seeded/hooke_hanger.csv)).

- *The bench:* Extension of a spring under 10 loads from 50 g to 500 g, read against a ruler.
- *What looks off:* The slope gives the expected spring constant, but the force line misses the origin by about half a newton.

**Expected result:** Hanger's mass left out of the loads, 52% as the leading cause (with the page's defaults: Expected spring constant (N/m) = 25).

Files: [Excel export](hooke/excel_export.csv) · [Semicolons, decimal commas](hooke/semicolon_decimal_comma.csv) · [Tab-separated](hooke/tab_separated.tsv) · [UTF-16 "Unicode text"](hooke/unicode_text.txt) · [Other column names](hooke/other_column_names.csv)

## Viscosity by Stokes' law (falling ball)

`stokes_viscosity` · model `v = 2r²g(ρ_s − ρ_l) / 9η, corrected for the tube wall` · columns `ball_diameter_mm`, `fall_time_s`

Made from the sample **Viscosity 16% low, every ball alike** ([`data/seeded/stokes_warm_liquid.csv`](../../data/seeded/stokes_warm_liquid.csv)).

- *The bench:* The same balls, tube and marks, with the glycerol's temperature entered as 20 °C.
- *What looks off:* Every ball gives the same viscosity, but it is about 16% below the table value for glycerol at 20 °C.

**Expected result:** Glycerol not at the temperature entered, 53% as the leading cause (with the page's defaults: Glycerol temperature (°C) = 20; Distance between the marks (mm) = 300; Tube inner diameter (mm) = 50; Ball density (kg/m³) = 7800; Timing precision (s) = 0.2; Micrometer reading precision (mm) = 0.003).

Files: [Excel export](stokes_viscosity/excel_export.csv) · [Semicolons, decimal commas](stokes_viscosity/semicolon_decimal_comma.csv) · [Tab-separated](stokes_viscosity/tab_separated.tsv) · [UTF-16 "Unicode text"](stokes_viscosity/unicode_text.txt) · [Other column names](stokes_viscosity/other_column_names.csv)

## Kater's reversible pendulum

`kater_pendulum` · model `T₁ = T₂ = T at the crossing,  g = 4π² L / T²` · columns `knife_edge_mass_position_cm`, `period_1_s`, `period_2_s`

Made from the sample **g 0.8% low, smooth curves** ([`data/seeded/kater_amplitude.csv`](../../data/seeded/kater_amplitude.csv)).

- *The bench:* The same pendulum and stopwatch, nine slider positions, with the release amplitude entered as 2°.
- *What looks off:* Both curves are smooth and cross cleanly, but the crossing period gives g about 0.8% below the local value.

**Expected result:** Swung from a larger angle than the amplitude entered, 53% as the leading cause (with the page's defaults: Knife-edge separation L (mm) = 995; Local g, from a gravity survey (m/s²) = 9.812; Release amplitude the periods are corrected for (°) = 2; Swings timed for each period = 50; Period precision (ms) = 1; Separation reading precision (mm) = 0.3).

Files: [Excel export](kater_pendulum/excel_export.csv) · [Semicolons, decimal commas](kater_pendulum/semicolon_decimal_comma.csv) · [Tab-separated](kater_pendulum/tab_separated.tsv) · [UTF-16 "Unicode text"](kater_pendulum/unicode_text.txt) · [Other column names](kater_pendulum/other_column_names.csv)

## Cavendish torsion balance

`cavendish` · graduate · model `G = 2π² L r² θ / (M T²) ÷ (1 − β),  θ = ΔS / 4D` · columns `time_s`, `beam_position_mm`

Made from the sample **G 8% low, clean swing** ([`data/seeded/cavendish_scale_distance.csv`](../../data/seeded/cavendish_scale_distance.csv)).

- *The bench:* The same balance and scale, with D entered as 4.20 m from the lab sheet.
- *What looks off:* The swing is clean and damps normally, but the shift and period give G about 8% below 6.674 × 10⁻¹¹.

**Expected result:** Mirror-to-scale distance D not what was entered, 53% as the leading cause (with the page's defaults: Mass of each large sphere M (kg) = 1.5; Fibre axis to small sphere centre d (mm); L = 2d = 50; Large to small sphere, centre to centre r (mm) = 46.5; Mirror-to-scale distance D (m) = 4.2; Spot reading precision (mm) = 1; Precision of r and d (mm) = 0.2).

Files: [Excel export](cavendish/excel_export.csv) · [Semicolons, decimal commas](cavendish/semicolon_decimal_comma.csv) · [Tab-separated](cavendish/tab_separated.tsv) · [UTF-16 "Unicode text"](cavendish/unicode_text.txt) · [Other column names](cavendish/other_column_names.csv)

## Driven damped oscillator (resonance)

`driven_oscillator` · model `A = a ω₀² / √((ω₀² − ω²)² + (γω)²)` · columns `drive_frequency_Hz`, `amplitude_mm`

Made from the sample **Resonance 4% low, shape right** ([`data/seeded/oscillator_dial.csv`](../../data/seeded/oscillator_dial.csv)).

- *The bench:* The same oscillator and brake, frequencies read from the motor's speed dial.
- *What looks off:* The curve has the right shape and width, but it peaks about 4% below the 0.800 Hz the free oscillations gave.

**Expected result:** Drive frequency read from the motor's dial, which is off, 56% as the leading cause (with the page's defaults: Natural frequency f₀ from free oscillations (Hz) = 0.8; Damping γ from the free decay at the set current (1/s) = 0.6; Brake magnet current set (A) = 0.4; Amplitude reading precision (mm) = 0.4).

Files: [Excel export](driven_oscillator/excel_export.csv) · [Semicolons, decimal commas](driven_oscillator/semicolon_decimal_comma.csv) · [Tab-separated](driven_oscillator/tab_separated.tsv) · [UTF-16 "Unicode text"](driven_oscillator/unicode_text.txt) · [Other column names](driven_oscillator/other_column_names.csv)

## Boyle's law (syringe and pressure sensor)

`boyle_gas` · model `p (V + V₀) = nRT` · columns `volume_ml`, `pressure_kPa`

Made from the sample **pV falls as the gas is squeezed** ([`data/seeded/boyle_dead_volume.csv`](../../data/seeded/boyle_dead_volume.csv)).

- *The bench:* The same syringe and sensor, now joined by a length of tubing, with the dead volume entered as 0.5 ml.
- *What looks off:* The points are smooth, but p(V + V₀) falls steadily as the gas is squeezed, by about 8% at 20 ml.

**Expected result:** Tubing volume left out of the dead volume, 53% as the leading cause (with the page's defaults: Dead volume outside the syringe scale V₀ (ml) = 0.5; Room pressure from the lab barometer (kPa) = 101.3; Volume reading precision (ml) = 0.3; Pressure reading precision (kPa) = 0.2).

Files: [Excel export](boyle_gas/excel_export.csv) · [Semicolons, decimal commas](boyle_gas/semicolon_decimal_comma.csv) · [Tab-separated](boyle_gas/tab_separated.tsv) · [UTF-16 "Unicode text"](boyle_gas/unicode_text.txt) · [Other column names](boyle_gas/other_column_names.csv)
