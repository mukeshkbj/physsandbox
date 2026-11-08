# Nuclear & particle

5 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Nuclear & particle*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Gamma-ray attenuation in lead](#gamma-ray-attenuation-in-lead) | teaching lab | `N = N₀ e^(−μx),  μ = (μ/ρ)·ρ` | Count with the source removed | [Excel](gamma_attenuation/excel_export.csv) · [Semicolons](gamma_attenuation/semicolon_decimal_comma.csv) · [Tabs](gamma_attenuation/tab_separated.tsv) · [UTF-16](gamma_attenuation/unicode_text.txt) · [Renamed](gamma_attenuation/other_column_names.csv) |
| [Muon lifetime](#muon-lifetime-graduate) | graduate | `N(t) = A e^(−t/τ) + B` | Read the singles rate with the detector open, then under a black cloth | [Excel](muon_lifetime/excel_export.csv) · [Semicolons](muon_lifetime/semicolon_decimal_comma.csv) · [Tabs](muon_lifetime/tab_separated.tsv) · [UTF-16](muon_lifetime/unicode_text.txt) · [Renamed](muon_lifetime/other_column_names.csv) |
| [Radioactive decay (Geiger–Müller)](#radioactive-decay-geigermüller) | teaching lab | `N = N₀ e^(−λt) + B, t½ = ln 2 / λ` | Remove the source and count the room background | [Excel](radioactive_decay/excel_export.csv) · [Semicolons](radioactive_decay/semicolon_decimal_comma.csv) · [Tabs](radioactive_decay/tab_separated.tsv) · [UTF-16](radioactive_decay/unicode_text.txt) · [Renamed](radioactive_decay/other_column_names.csv) |
| [Rutherford scattering (alphas on gold)](#rutherford-scattering-alphas-on-gold-graduate) | graduate | `N(θ) ∝ 1/sin⁴(θ/2)` | Count at equal angles on both sides of the beam | [Excel](rutherford/excel_export.csv) · [Semicolons](rutherford/semicolon_decimal_comma.csv) · [Tabs](rutherford/tab_separated.tsv) · [UTF-16](rutherford/unicode_text.txt) · [Renamed](rutherford/other_column_names.csv) |
| [Compton scattering](#compton-scattering-graduate) | graduate | `E′ = E / (1 + (E/m_e c²)(1 − cos θ))` | Read known calibration lines with the same MCA settings | [Excel](compton/excel_export.csv) · [Semicolons](compton/semicolon_decimal_comma.csv) · [Tabs](compton/tab_separated.tsv) · [UTF-16](compton/unicode_text.txt) · [Renamed](compton/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Gamma-ray attenuation in lead

Cs-137 count rate against the thickness of lead in the beam, to measure lead's attenuation coefficient at 662 keV.

| | |
| --- | --- |
| Model | `N = N₀ e^(−μx),  μ = (μ/ρ)·ρ` |
| Columns | `thickness_mm`, `counts` (one row per reading; `#` lines are comments) |
| You enter | Mass attenuation coefficient of lead at 662 keV (cm²/g) (default 0.11); Lead density (g/cm³) (default 11.34); Count time per reading (s) (default 300); Background you subtracted (counts/s) (default 0.5) |
| Physics code | [`sandbox/tools/bench_advanced.py`](../../sandbox/tools/bench_advanced.py), fitted inside the glovebox |
| Fault library | [`faults/bench_advanced.yaml`](../../faults/bench_advanced.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `gamma_attenuation` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Background during the run higher than the figure subtracted | A source brought out on the next bench can lift a GM tube's background from 0.5 to 2 counts/s or more | Count the background for at least 5 minutes with the source in its pot and the room as it is during the run (other benches' sources out), subtract that rate, and refit. |
| Gamma rays reaching the tube round the lead (no collimator or tube shield) | Without collimation, scatter off the bench, walls and source holder can add about 1% of the beam behind any thickness | Put the lead collimator on the source and a lead sleeve round the tube, so the only way to the detector is through the absorbers, then repeat the thick end. |
| Counting losses at high rate (detector dead time) behind the thinnest absorbers | A GM tube with a 100 µs dead time loses about a quarter of the counts at 3000 /s | Move the source back until the unattenuated rate is under about 100 /s, or correct each rate with n = m/(1 − mτ) using the dead time from the two-source method, then repeat the thin end. |
| Absorber thicknesses not as recorded (nominal sheet sizes used) | Sheets sold as 5 mm are often 4.5–5.5 mm, and μ shifts by the same fraction | Measure every sheet with a micrometer in several places (or weigh it and divide by area × density), then refit with the measured thicknesses. |
| Photons scattered inside the lead still counted (broad beam) | Without collimation, scattered photons building up in the lead make μ come out 10–20% low | Collimate the source and the detector (narrow-beam geometry) so photons scattered in the lead miss the tube, then repeat. |
| Unknown cause (none of the above fits well) |  | Check the tube's plateau voltage, repeat a few thicknesses in random order, and compare counts point by point. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Count with the source removed | 6 | Put the Cs-137 source back in its lead pot and take it out of the room, leave the absorbers and tube as they were, and take five 60 s counts. Compare the rate with the background you subtracted. *Safety:* Move the source with tongs, never your fingers, and keep it in its pot whenever it's not in use. Lead is toxic; wear gloves or wash your hands after handling the sheets, and don't eat or drink at the bench. Follow your radiation safety officer's local rules (dosimeter, sign-out log). |
| Fit the lead collimator and tube shield, then recount the thickest absorbers | 12 | Put the lead collimator on the source and a lead sleeve round the tube, and recount 40, 45 and 50 mm. Gamma rays that went round the lead are blocked; the background is not. *Safety:* Handle the source with tongs and use the time, distance and shielding rule (work quickly, from arm's length, behind the lead). Lead bricks are heavy and toxic; wear gloves, wash your hands after, and follow your radiation safety officer's rules. |
| Measure the tube's dead time with the two-source method | 15 | Count two split sources separately and together (n₁, n₂, n₁₂, each with background b). The dead time is τ ≈ (n₁ + n₂ − n₁₂ − b)/(2 n₁ n₂). *Safety:* Handle sources with tongs, keep them in their pots when not in use, and follow your radiation safety officer's rules. The GM tube runs at several hundred volts; don't touch its connector with the counter on. |
| Measure the absorber sheets with a micrometer | 8 | Measure each lead sheet in five places and compare the total with the thicknesses you recorded. *Safety:* Lead is toxic; wear gloves or wash your hands after handling the sheets, and don't eat or drink at the bench. |

### Samples on the page

- **Counts level off behind thick lead**: [`gamma_background.csv`](../../data/seeded/gamma_background.csv). The thin end follows the expected line, but from about 30 mm of lead on the counts level off well above it.
- **Too few counts with little lead in**: [`gamma_dead_time.csv`](../../data/seeded/gamma_dead_time.csv). Behind thick lead the points follow the expected slope, but with little or no lead in the count rate falls below the line through the rest, by nearly a quarter at 0 mm.
- **Healthy attenuation**: [`gamma_clean.csv`](../../data/seeded/gamma_clean.csv). Nothing should look off: a straight line on a log scale with μ/ρ = 0.110 cm²/g (half-value layer 5.6 mm).
- Sample result of *Count with the source removed*: [`gamma_background_source_out.csv`](../../data/seeded/gamma_background_source_out.csv)

### The demo case

1. **Counts level off behind thick lead** ([`gamma_background.csv`](../../data/seeded/gamma_background.csv)): the leading cause is *Background during the run higher than the figure subtracted* at 53%, with *Gamma rays reaching the tube round the lead (no collimator or tube shield)* at 45%.
2. Recommended test: **Count with the source removed** (6 min, 0.99 bits).
3. With its result ([`gamma_background_source_out.csv`](../../data/seeded/gamma_background_source_out.csv)): *Background during the run higher than the figure subtracted*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`gamma_attenuation/`](gamma_attenuation/)); each gives the result above. [Excel export](gamma_attenuation/excel_export.csv) · [Semicolons, decimal commas](gamma_attenuation/semicolon_decimal_comma.csv) · [Tab-separated](gamma_attenuation/tab_separated.tsv) · [UTF-16 "Unicode text"](gamma_attenuation/unicode_text.txt) · [Other column names](gamma_attenuation/other_column_names.csv)

## Muon lifetime *(graduate)*

Time from a cosmic muon stopping in a scintillator to its decay electron, histogrammed, to measure the muon's lifetime.

| | |
| --- | --- |
| Model | `N(t) = A e^(−t/τ) + B` |
| Columns | `time_us`, `counts` (one row per reading; `#` lines are comments) |
| You enter | Expected lifetime in plastic scintillator, μ⁺ and μ⁻ together (µs) (default 2.12); Start the fit at (µs) (default 1) |
| Physics code | [`sandbox/tools/bench_advanced.py`](../../sandbox/tools/bench_advanced.py), fitted inside the glovebox |
| Fault library | [`faults/bench_advanced.yaml`](../../faults/bench_advanced.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `muon_lifetime` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Light leak in the scintillator's wrapping (room light making random pulses) | A pinhole in the black tape can triple the singles rate, and random stops go as its square | Find the leak (the singles rate jumps when a torch passes over it), cover it with black tape, and repeat the run. |
| Discriminator threshold too low (photomultiplier noise counted) | A threshold set into the photomultiplier's noise can triple the singles rate | Raise the threshold to the start of the singles-rate plateau (or lower the photomultiplier voltage by 50–100 V) until the singles rate is back to normal, then repeat. |
| Timer's time scale off (clock frequency not the one the software assumes) | An oscillator 10% fast logs every decay time, and so τ, 10% long | Time a pulse pair of known spacing (checked on an oscilloscope), set the right clock frequency in the software or rescale the time axis by true ÷ logged, and refit. |
| Photomultiplier afterpulses counted as early decays | Ion afterpulses 0.1–1 µs after a muon's pulse pile up in the first bins | Keep the fit starting at 1 µs or later, and lower the photomultiplier voltage or add a short veto after each start so an afterpulse can't stop the timer. |
| Unknown cause (none of the above fits well) |  | Look at the raw pulses on an oscilloscope and check the start and stop discriminators fire once per pulse. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the singles rate with the detector open, then under a black cloth | 2 | Read the discriminator's count rate in ten 10 s counts with the room lights on, then cover the detector completely with a thick black cloth (or turn the lights off) and take ten more. *Safety:* The photomultiplier runs at 1–2 kV. Leave its housing closed and its high-voltage cable connected while it is on, and turn the voltage down before uncovering any part of the tube. |
| Step the discriminator threshold up and read the singles rate | 6 | Raise the threshold in five steps from its present setting and read the singles rate at each. Noise falls away steeply into a plateau of real muons; light-leak pulses are bright and stay. *Safety:* The photomultiplier runs at 1–2 kV. Adjust the threshold on the discriminator, not inside the photomultiplier base, and keep the housing closed. |
| Time a calibrated pulse pair on the timer | 5 | Feed the timer two pulses from a pulse generator with a delay set and checked on an oscilloscope (say 5.00 µs), and compare the logged interval with it. *Safety:* Unplug the photomultiplier's signal cable from the timer only, never the high-voltage cable, and turn the high voltage down first if your setup shares a connector panel. |
| Flash an LED into the photomultiplier and histogram what follows | 8 | Drive the detector's LED port with short flashes and histogram the time to the next pulse. Afterpulses show as a bump 0.1–1 µs after each flash. *Safety:* The photomultiplier runs at 1–2 kV. Use the housing's LED port; don't open the housing with the high voltage on. |

### Samples on the page

- **Flat background ten times the usual**: [`muon_light_leak.csv`](../../data/seeded/muon_light_leak.csv). The decay has the expected lifetime, but it sits on a flat background about ten times the usual, so τ is less precise.
- **Lifetime 10% long**: [`muon_tdc_clock.csv`](../../data/seeded/muon_tdc_clock.csv). A clean exponential on a normal background, but τ comes out near 2.33 µs, 10% above the expected 2.12 µs.
- **Healthy decay curve**: [`muon_clean.csv`](../../data/seeded/muon_clean.csv). Nothing should look off: an exponential decay with τ = 2.12 µs on a small flat background.
- Sample result of *Read the singles rate with the detector open, then under a black cloth*: [`muon_light_leak_covered.csv`](../../data/seeded/muon_light_leak_covered.csv)

### The demo case

1. **Flat background ten times the usual** ([`muon_light_leak.csv`](../../data/seeded/muon_light_leak.csv)): the leading cause is *Light leak in the scintillator's wrapping (room light making random pulses)* at 53%, with *Discriminator threshold too low (photomultiplier noise counted)* at 45%.
2. Recommended test: **Read the singles rate with the detector open, then under a black cloth** (2 min, 0.99 bits).
3. With its result ([`muon_light_leak_covered.csv`](../../data/seeded/muon_light_leak_covered.csv)): *Light leak in the scintillator's wrapping (room light making random pulses)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`muon_lifetime/`](muon_lifetime/)); each gives the result above. [Excel export](muon_lifetime/excel_export.csv) · [Semicolons, decimal commas](muon_lifetime/semicolon_decimal_comma.csv) · [Tab-separated](muon_lifetime/tab_separated.tsv) · [UTF-16 "Unicode text"](muon_lifetime/unicode_text.txt) · [Other column names](muon_lifetime/other_column_names.csv)

## Radioactive decay (Geiger–Müller)

Counts per interval from a Ba-137m sample on a GM counter, to measure the half-life.

| | |
| --- | --- |
| Model | `N = N₀ e^(−λt) + B, t½ = ln 2 / λ` |
| Columns | `time_s`, `counts` (one row per reading; `#` lines are comments) |
| You enter | Expected half-life (s) (default 153.1); Counter dead time (µs) (default 150) |
| Physics code | [`sandbox/tools/bench_core.py`](../../sandbox/tools/bench_core.py), fitted inside the glovebox |
| Fault library | [`faults/bench_core.yaml`](../../faults/bench_core.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `radioactive_decay` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Room background not subtracted | About 0.8 counts per second, which is most of the count by the end of a 25-minute run | Subtract the room background (counted with the source away) from every interval and refit. |
| Long-lived activity in the sample (Cs-137 breakthrough from the generator) | A little Cs-137 washed out with the barium keeps the count from ever reaching background | Report the long-lived component, fit it as a constant, and tell whoever looks after the generator; it may need replacing. |
| Counter dead time losing counts at high rates | At 2000 counts per second a 150 µs dead time loses about a quarter of the counts | Move the source back until the rate is below about 500 per second, or correct each interval for dead time, n = m / (1 − mτ), and refit. |
| Unknown cause (none of the above fits well) |  | Check the counter's operating voltage is on its plateau and the interval timer is right, then repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Remove the source and count the room background | 4 | Take the sample well away (back in its lead pot) and count for three minutes with the same interval, appended to the same log. *Safety:* Pick up the sample with tongs, not fingers, and put it straight back in its lead pot. Keep your time near it short and your distance large; the eluate is an open source, so wear gloves, work over a tray and dispose of it as your radiation safety officer directs. |
| Count the same sample again after 30 minutes | 35 | Leave the sample in place for 30 minutes (over 10 half-lives of Ba-137m) and count for five minutes. *Safety:* Keep the sample shielded and labelled while you wait, and follow your radiation safety officer's rules for open sources. |
| Measure the dead time with the two-source method | 10 | Count source A alone, A and B together, then B alone, without moving either; the shortfall in the combined count gives the dead time. *Safety:* Handle the sealed sources with tongs, keep them in their lead pots when not in use, and use time, distance and shielding; ask your radiation safety officer before using sources you haven't been signed off on. |

### Samples on the page

- **Counts level off instead of falling to zero**: [`decay_background.csv`](../../data/seeded/decay_background.csv). The decay starts at the right rate, but after about 15 minutes the counts level off near 8 per interval instead of falling towards zero.
- **Decays too slowly at the start**: [`decay_dead_time.csv`](../../data/seeded/decay_dead_time.csv). The decay looks too slow at the start and the half-life comes out about 15% long.
- **Healthy decay**: [`decay_clean.csv`](../../data/seeded/decay_clean.csv). Nothing should look off: a straight line on the log plot with the 2.55-minute half-life.
- Sample result of *Remove the source and count the room background*: [`decay_background_removed.csv`](../../data/seeded/decay_background_removed.csv)

### The demo case

1. **Counts level off instead of falling to zero** ([`decay_background.csv`](../../data/seeded/decay_background.csv)): the leading cause is *Room background not subtracted* at 54%, with *Long-lived activity in the sample (Cs-137 breakthrough from the generator)* at 45%.
2. Recommended test: **Remove the source and count the room background** (4 min, 1.06 bits).
3. With its result ([`decay_background_removed.csv`](../../data/seeded/decay_background_removed.csv)): *Room background not subtracted*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`radioactive_decay/`](radioactive_decay/)); each gives the result above. [Excel export](radioactive_decay/excel_export.csv) · [Semicolons, decimal commas](radioactive_decay/semicolon_decimal_comma.csv) · [Tab-separated](radioactive_decay/tab_separated.tsv) · [UTF-16 "Unicode text"](radioactive_decay/unicode_text.txt) · [Other column names](radioactive_decay/other_column_names.csv)

## Rutherford scattering (alphas on gold) *(graduate)*

Count rate of Am-241 alphas scattered by a thin gold foil in vacuum against angle, to test the 1/sin⁴(θ/2) law.

| | |
| --- | --- |
| Model | `N(θ) ∝ 1/sin⁴(θ/2)` |
| Columns | `angle_deg`, `counts`, `live_time_s` (one row per reading; `#` lines are comments) |
| You enter | Count rate at 20° on the lab sheet (/s) (default 1.2) |
| Physics code | [`sandbox/tools/bench_fields.py`](../../sandbox/tools/bench_fields.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fields.yaml`](../../faults/bench_fields.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `rutherford` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Detector angle zero misset (scale zero not on the beam axis) | A zero 1.5° off makes the 10° point count about 90% fast if the angles read high (or 40% slow if they read low) | Find the true zero as the midpoint of equal count rates either side of the beam, correct every angle by it, and refit. |
| Foil too thick (multiple scattering spreads the beam into the small angles) | A foil several µm thick spreads the alphas over a few degrees, so the 10–15° rates come out tens of per cent fast, the same on both sides | Fit the thinnest gold foil (about 2 µm, checked against its label) and repeat the small angles, or fit only angles beyond about 20°. |
| Background counts from alphas leaking round the collimator | Two or three counts a minute reaching the detector directly swamp the 50° rate (about two a minute) | Reseat the source in its collimator (slit against the foil, nothing round the edge), count with the foil out to check the leak has gone, then repeat the large angles. |
| Chamber not pumped down (gas in the alphas' path) | Left at a few hundred millibar, the alphas lose 2–3 MeV in the gas; many fall below the discriminator and the rate drops to a fraction of the lab sheet's at every angle | Check the seal and the vent valve, pump the chamber below a few mbar (read it on the gauge) and repeat. |
| Unknown cause (none of the above fits well) |  | Check the discriminator threshold against the pulse-height spectrum of the alpha peak and that the foil is centred on the beam, then repeat a few angles. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Count at equal angles on both sides of the beam | 10 | Count for one minute at −10°, −15°, +10° and +15° and for two at −20° and +20°, as read. With the zero right each pair agrees; a zero error makes one side fast and the other slow. *Safety:* The Am-241 source is sealed and stays inside the closed chamber; turn the detector from outside and don't open the chamber while counting. If the source ever has to come out, handle it only with tongs and put it straight into its shielded container. |
| Fit a thin foil and recount the small angles | 30 | Vent the chamber, swap in the thinnest gold foil (about 2 µm, checked against its label), pump down below a few mbar and count at 10°, 15° and 20° for the same live times. *Safety:* Handle the sealed Am-241 source only with tongs and keep it in its shielded container while the chamber is open; never touch its face or the foil, and wash your hands afterwards. Vent the chamber slowly so the foil doesn't tear. |
| Count with the foil removed | 30 | Vent the chamber, take the gold foil out of its holder, pump down and count at 30° for 20 minutes. With no foil nothing should scatter into the detector. *Safety:* Handle the sealed Am-241 source only with tongs and keep it in its shielded container while the chamber is open; never touch its face, and follow your radiation safety officer's rules. Vent the chamber slowly. |
| Read the chamber's vacuum gauge | 1 | Read the Pirani gauge on the chamber a few times with the pump running. The working pressure should be below a few mbar. *Safety:* Keep the chamber closed and the source inside it while you check the vacuum, and keep clear of the rotary pump's belt and exhaust. |

### Samples on the page

- **Small angles count too fast**: [`ruth_zero_offset.csv`](../../data/seeded/ruth_zero_offset.csv). The larger angles follow 1/sin⁴(θ/2), but at 10° and 15° the rate is well above that curve.
- **Large angles level off**: [`ruth_leakage.csv`](../../data/seeded/ruth_leakage.csv). The small angles follow 1/sin⁴(θ/2), but from about 35° on the rate falls more slowly and starts to level off.
- **Healthy measurement**: [`ruth_clean.csv`](../../data/seeded/ruth_clean.csv). Nothing should look off: the rate follows 1/sin⁴(θ/2), the exponent close to 4.
- Sample result of *Count at equal angles on both sides of the beam*: [`ruth_zero_offset_both_sides.csv`](../../data/seeded/ruth_zero_offset_both_sides.csv)

### The demo case

1. **Small angles count too fast** ([`ruth_zero_offset.csv`](../../data/seeded/ruth_zero_offset.csv)): the leading cause is *Detector angle zero misset (scale zero not on the beam axis)* at 53%, with *Foil too thick (multiple scattering spreads the beam into the small angles)* at 45%.
2. Recommended test: **Count at equal angles on both sides of the beam** (10 min, 1.00 bits).
3. With its result ([`ruth_zero_offset_both_sides.csv`](../../data/seeded/ruth_zero_offset_both_sides.csv)): *Detector angle zero misset (scale zero not on the beam axis)*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`rutherford/`](rutherford/)); each gives the result above. [Excel export](rutherford/excel_export.csv) · [Semicolons, decimal commas](rutherford/semicolon_decimal_comma.csv) · [Tab-separated](rutherford/tab_separated.tsv) · [UTF-16 "Unicode text"](rutherford/unicode_text.txt) · [Other column names](rutherford/other_column_names.csv)

## Compton scattering *(graduate)*

Energy of Cs-137 gamma rays scattered off electrons against angle, to measure the electron's rest energy.

| | |
| --- | --- |
| Model | `E′ = E / (1 + (E/m_e c²)(1 − cos θ))` |
| Columns | `angle_deg`, `energy_keV` (one row per reading; `#` lines are comments) |
| You enter | Source line energy (keV) (default 661.66); Accepted m_e c² (keV) (default 510.999); Photopeak reading precision (keV) (default 2) |
| Physics code | [`sandbox/tools/bench_graduate.py`](../../sandbox/tools/bench_graduate.py), fitted inside the glovebox |
| Fault library | [`faults/bench_graduate.yaml`](../../faults/bench_graduate.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `compton` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| MCA energy calibration gain off (PMT voltage or temperature drift) | A 5% gain drift scales every peak, so both 662 keV and m_e c² come out 5% low | Recalibrate the MCA with two or more known lines at the same PMT voltage, let the detector settle at room temperature, and refit. |
| MCA energy calibration zero offset | A 15 keV zero offset shifts every peak by the same amount | Recalibrate with a low-energy line (Am-241 at 59.5 keV) and a high one, fitting a gain and an offset, then refit. |
| Detector arm's zero angle misread | A 5° zero error bends the small-angle points away from the Compton curve | Find the true zero by measuring at equal angles either side of the beam and taking the midpoint, then correct every angle. |
| Backscatter peak taken for the scattered photopeak at one angle | Near 135° the 206 keV photopeak sits close to the 184 keV backscatter peak | At that angle, subtract a spectrum taken with the scatterer removed, pick the peak that moves with angle, and refit. |
| Unknown cause (none of the above fits well) |  | Check the scatterer is in the beam's centre and the collimators are aligned, then look at the raw spectra one by one. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read known calibration lines with the same MCA settings | 6 | Without touching the PMT voltage or gain, record Am-241 (59.5 keV), Na-22 (511 and 1274.5 keV) and the unscattered Cs-137 line (661.7 keV), and fit reading against true energy. *Safety:* Handle the sealed sources with tongs, keep them in their lead pots when not in use, wear your dosimeter, and follow the local rules of your radiation safety officer. |
| Measure at the same angle on both sides of the beam | 12 | Take the photopeak at +45° and −45°. With the zero right they agree; a zero error makes them differ. *Safety:* The direct Cs-137 beam is the highest dose point; never put your hands in front of the collimator, and follow your radiation safety officer's rules. |
| Take the largest-angle spectrum again with the scatterer removed | 8 | Remove the aluminium rod and record the spectrum at the same angle. Peaks that stay are background (backscatter from shielding); the Compton peak goes. *Safety:* Handle the source and scatterer with tongs, wear your dosimeter, and follow your radiation safety officer's rules. |

### Samples on the page

- **m_e c² and 662 keV both read low**: [`compton_gain.csv`](../../data/seeded/compton_gain.csv). The points follow a Compton-like curve, but the fit puts the unscattered line near 629 keV and m_e c² about 5% low.
- **Largest-angle point off the curve**: [`compton_backscatter.csv`](../../data/seeded/compton_backscatter.csv). Seven angles fit the Compton formula, but the 135° point sits about 20 keV below the curve.
- **Healthy measurement**: [`compton_clean.csv`](../../data/seeded/compton_clean.csv). Nothing should look off: the Compton formula fits with m_e c² = 511 keV.
- Sample result of *Read known calibration lines with the same MCA settings*: [`compton_gain_calibration.csv`](../../data/seeded/compton_gain_calibration.csv)

### The demo case

1. **m_e c² and 662 keV both read low** ([`compton_gain.csv`](../../data/seeded/compton_gain.csv)): the leading cause is *MCA energy calibration gain off (PMT voltage or temperature drift)* at 54%, with *MCA energy calibration zero offset* at 46%.
2. Recommended test: **Read known calibration lines with the same MCA settings** (6 min, 1.03 bits).
3. With its result ([`compton_gain_calibration.csv`](../../data/seeded/compton_gain_calibration.csv)): *MCA energy calibration gain off (PMT voltage or temperature drift)*, 95%, confirmed.

### Example upload files

The headline sample saved five ways ([`compton/`](compton/)); each gives the result above. [Excel export](compton/excel_export.csv) · [Semicolons, decimal commas](compton/semicolon_decimal_comma.csv) · [Tab-separated](compton/tab_separated.tsv) · [UTF-16 "Unicode text"](compton/unicode_text.txt) · [Other column names](compton/other_column_names.csv)
