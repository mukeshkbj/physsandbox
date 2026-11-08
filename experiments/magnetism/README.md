# Magnetism

7 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Magnetism*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Helmholtz coil calibration](#helmholtz-coil-calibration) | teaching lab | `B = (4/5)^(3/2) μ₀NI/R` | Read the probe at zero current, in the open and inside a zero-gauss chamber | [Excel](helmholtz/excel_export.csv) · [Semicolons](helmholtz/semicolon_decimal_comma.csv) · [Tabs](helmholtz/tab_separated.tsv) · [UTF-16](helmholtz/unicode_text.txt) · [Renamed](helmholtz/other_column_names.csv) |
| [Faraday's law of induction](#faradays-law-of-induction) | teaching lab | `ε = −N dΦ/dt` | Hold the magnet still, then short the amplifier input | [Excel](faraday/excel_export.csv) · [Semicolons](faraday/semicolon_decimal_comma.csv) · [Tabs](faraday/tab_separated.tsv) · [UTF-16](faraday/unicode_text.txt) · [Renamed](faraday/other_column_names.csv) |
| [Hall effect](#hall-effect) | teaching lab | `V_H = IB / (n e t)` | Repeat with the magnetic field reversed | [Excel](hall/excel_export.csv) · [Semicolons](hall/semicolon_decimal_comma.csv) · [Tabs](hall/tab_separated.tsv) · [UTF-16](hall/unicode_text.txt) · [Renamed](hall/other_column_names.csv) |
| [Magnetic hysteresis (B–H loop)](#magnetic-hysteresis-bh-loop) | teaching lab | `H = N₁I/ℓ,  B = Φ/(N₂A)` | Compare the search coil with a freshly wound 10-turn coil | [Excel](hysteresis/excel_export.csv) · [Semicolons](hysteresis/semicolon_decimal_comma.csv) · [Tabs](hysteresis/tab_separated.tsv) · [UTF-16](hysteresis/unicode_text.txt) · [Renamed](hysteresis/other_column_names.csv) |
| [e/m of the electron (fine-beam tube)](#em-of-the-electron-fine-beam-tube) | teaching lab | `e/m = 2V/(B r)²,  B = (4/5)^(3/2) μ₀NI/R` | Re-read the diameters on a mirror scale | [Excel](e_over_m/excel_export.csv) · [Semicolons](e_over_m/semicolon_decimal_comma.csv) · [Tabs](e_over_m/tab_separated.tsv) · [UTF-16](e_over_m/unicode_text.txt) · [Renamed](e_over_m/other_column_names.csv) |
| [Electron spin resonance (DPPH)](#electron-spin-resonance-dpph-graduate) | graduate | `h f = g μ_B B` | Reverse the field and read the resonances again | [Excel](esr/excel_export.csv) · [Semicolons](esr/semicolon_decimal_comma.csv) · [Tabs](esr/tab_separated.tsv) · [UTF-16](esr/unicode_text.txt) · [Renamed](esr/other_column_names.csv) |
| [Pulsed NMR spin echo](#pulsed-nmr-spin-echo-graduate) | graduate | `A(2τ) = A₀ e^(−2τ/T₂)` | Run a nutation sweep (FID amplitude against pulse length) | [Excel](nmr_echo/excel_export.csv) · [Semicolons](nmr_echo/semicolon_decimal_comma.csv) · [Tabs](nmr_echo/tab_separated.tsv) · [UTF-16](nmr_echo/unicode_text.txt) · [Renamed](nmr_echo/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Helmholtz coil calibration

Hall-probe field at the centre against coil current.

| | |
| --- | --- |
| Model | `B = (4/5)^(3/2) μ₀NI/R` |
| Columns | `current_A`, `measured_B_uT` (one row per reading; `#` lines are comments) |
| You enter | Coil radius (m) (default 0.15); Turns per coil (default 100) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `helmholtz` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Earth's field or nearby steel adding to the coil field | Earth's field is 25–65 µT; a steel bench or laptop can add tens of µT | Subtract the zero-current reading taken at the same probe position from every point, and move steel and laptops away from the coils. |
| Hall probe zero offset (probe not zeroed) | Uncompensated Hall sensors drift by several µT to tens of µT | Zero the Hall probe inside a zero-gauss chamber before the run, or subtract its zero-current reading from every point. |
| Hall probe gain (sensitivity) calibration error |  | Calibrate the probe against a reference magnetometer and scale every reading by the ratio, or swap in a calibrated probe. |
| Coil spacing or radius not at the Helmholtz condition | Spacing off by 10% of R changes the centre field by a few per cent | Set the coil spacing equal to the coil radius, measured between the centres of the windings, and repeat the sweep. |
| Unknown cause (none of the above fits well) |  | Repeat the sweep with a second Hall probe, checking its zero before and after, and compare point by point. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the probe at zero current, in the open and inside a zero-gauss chamber | 3 | Switch the coil current off. Record the field with the probe at the coil centre, then with the probe inside a mu-metal zero-gauss chamber. |
| Compare the probe with a calibrated reference magnetometer | 10 | Put a calibrated fluxgate or reference probe at the coil centre and read both at the same currents. |
| Measure the coil spacing and radius | 5 | The coils should be one radius apart (R = 0.15 m means 0.15 m between coil planes). *Safety:* Switch the coil current off before handling the coils; they can be hot at high current. |

### Samples on the page

- **Field doesn't start at zero**: [`helmholtz_ambient.csv`](../../data/seeded/helmholtz_ambient.csv). The slope matches theory, but the line doesn't pass through zero: there is about 45 µT of field at zero current.
- **Field 18% below theory**: [`helmholtz_gain.csv`](../../data/seeded/helmholtz_gain.csv). The line goes through zero, but its slope is about 18% below the theoretical 600 µT/A.
- **Healthy calibration**: [`helmholtz_clean.csv`](../../data/seeded/helmholtz_clean.csv). Nothing should look off: slope matches theory, no offset.
- Sample result of *Read the probe at zero current, in the open and inside a zero-gauss chamber*: [`helmholtz_ambient_shield.csv`](../../data/seeded/helmholtz_ambient_shield.csv)

### The demo case

1. **Field doesn't start at zero** ([`helmholtz_ambient.csv`](../../data/seeded/helmholtz_ambient.csv)): the leading cause is *Earth's field or nearby steel adding to the coil field* at 64%, with *Hall probe zero offset (probe not zeroed)* at 35%.
2. Recommended test: **Read the probe at zero current, in the open and inside a zero-gauss chamber** (3 min, 1.02 bits).
3. With its result ([`helmholtz_ambient_shield.csv`](../../data/seeded/helmholtz_ambient_shield.csv)): *Earth's field or nearby steel adding to the coil field*, 95%, confirmed.

### Example upload files

The headline sample saved five ways ([`helmholtz/`](helmholtz/)); each gives the result above. [Excel export](helmholtz/excel_export.csv) · [Semicolons, decimal commas](helmholtz/semicolon_decimal_comma.csv) · [Tab-separated](helmholtz/tab_separated.tsv) · [UTF-16 "Unicode text"](helmholtz/unicode_text.txt) · [Other column names](helmholtz/other_column_names.csv)

## Faraday's law of induction

Induced EMF in a search coil against the changing flux.

| | |
| --- | --- |
| Model | `ε = −N dΦ/dt` |
| Columns | `time_s`, `magnetic_flux_Wb`, `induced_voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Turns on the coil (default 200) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 7 seeded cases in `data/manifest*` |
| Key | `faraday` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| One reading far off the rest (a loose contact or an amplifier spike) | One point many times the scatter away from the line; the rest agree with the prediction | Re-seat the coil leads and the amplifier input and repeat the run. If the spike comes back at the same moment, look for something switching on then (a relay, a motor, a lamp) and screen or move it. |
| Amplifier input offset voltage | General-purpose op-amps: 1–10 mV, multiplied by the amplifier gain | Null the amplifier offset with its trim while the input is shorted, or subtract the shorted-input reading from the trace. |
| Ground potential difference between coil circuit and recorder |  | Connect the coil circuit and the recorder to one common ground point, then re-record. |
| Coil has fewer turns than specified, or a shorted winding |  | Find the real number of turns (count them or infer it from the inductance) and use it in the prediction, or replace a coil with a shorted winding. |
| Flux sensor calibration error |  | Recalibrate the flux sensor against a known field and recompute the predicted EMF. |
| Coil leads connected the wrong way round |  | Swap the coil leads at the amplifier input and re-record. |
| Unknown cause (none of the above fits well) |  | Re-record with the magnet moving at a steady speed and check the coil, amplifier and recorder one at a time. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Hold the magnet still, then short the amplifier input | 3 | With no changing flux, record the output with the coil connected, then with the amplifier input shorted to its own ground. |
| Measure the coil inductance with an LCR meter | 5 | Inductance scales with N squared; half the turns gives a quarter of the expected inductance. |
| Swap the coil leads and repeat | 2 | Reverse the two coil connections at the amplifier input and record one cycle. |

### Samples on the page

- **EMF sits on a DC offset**: [`faraday_offset.csv`](../../data/seeded/faraday_offset.csv). The induced voltage has the right size and shape, but the whole trace is shifted up by about 0.15 V.
- **EMF half the predicted size**: [`faraday_half_turns.csv`](../../data/seeded/faraday_half_turns.csv). The induced voltage is only about half what N·dΦ/dt predicts, with the right shape and no offset.
- **Healthy coil**: [`faraday_clean.csv`](../../data/seeded/faraday_clean.csv). Nothing should look off: measured EMF matches the prediction.
- Sample result of *Hold the magnet still, then short the amplifier input*: [`faraday_offset_shorted.csv`](../../data/seeded/faraday_offset_shorted.csv)

### The demo case

1. **EMF sits on a DC offset** ([`faraday_offset.csv`](../../data/seeded/faraday_offset.csv)): the leading cause is *Amplifier input offset voltage* at 54%, with *Ground potential difference between coil circuit and recorder* at 42%.
2. Recommended test: **Hold the magnet still, then short the amplifier input** (3 min, 1.16 bits).
3. With its result ([`faraday_offset_shorted.csv`](../../data/seeded/faraday_offset_shorted.csv)): *Amplifier input offset voltage*, 90%, confirmed.

### Example upload files

The headline sample saved five ways ([`faraday/`](faraday/)); each gives the result above. [Excel export](faraday/excel_export.csv) · [Semicolons, decimal commas](faraday/semicolon_decimal_comma.csv) · [Tab-separated](faraday/tab_separated.tsv) · [UTF-16 "Unicode text"](faraday/unicode_text.txt) · [Other column names](faraday/other_column_names.csv)

## Hall effect

Hall voltage against sample current in a fixed field.

| | |
| --- | --- |
| Model | `V_H = IB / (n e t)` |
| Columns | `current_A`, `hall_voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Field (T) (default 0.3); Sample thickness (m) (default 0.001); Expected carrier density (/m³) (default 1e+21) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `hall` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Hall contacts not exactly opposite each other | A small offset between contacts adds an IR drop proportional to current, which looks like extra Hall voltage | Average the readings taken with the field forward and reversed, which cancels the misalignment voltage, or remake the contacts exactly opposite each other. |
| Magnetic field lower than the value you set |  | Measure the field in the gap with a gaussmeter and use the measured value in the analysis. |
| Thermoelectric voltage at the contacts |  | Let the contacts reach a steady temperature, then reverse the sample current and average the two readings. |
| Unknown cause (none of the above fits well) |  | Repeat with the current and the field each reversed, and measure the field with a gaussmeter. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat with the magnetic field reversed | 3 | Reverse the magnet current (or turn the sample over) and repeat the current sweep. The Hall voltage flips; a misalignment voltage does not. |
| Measure the field in the gap with a gaussmeter | 4 | Put the gaussmeter probe where the sample sits, at the same magnet current. |
| Read the Hall voltage with zero sample current, then reverse the current | 2 | A voltage that stays at zero current, and does not flip with current, is thermoelectric. |

### Samples on the page

- **Carrier density 25% high**: [`hall_misaligned.csv`](../../data/seeded/hall_misaligned.csv). The line goes through zero, but its slope gives a carrier density about 25% above the expected 1×10²¹ /m³.
- **Voltage at zero current**: [`hall_thermal.csv`](../../data/seeded/hall_thermal.csv). The slope is right, but the voltage doesn't start at zero: there is about 0.5 mV with no current.
- **Healthy sample**: [`hall_clean.csv`](../../data/seeded/hall_clean.csv). Nothing should look off: carrier density matches, no offset.
- Sample result of *Repeat with the magnetic field reversed*: [`hall_misaligned_reversed.csv`](../../data/seeded/hall_misaligned_reversed.csv)

### The demo case

1. **Carrier density 25% high** ([`hall_misaligned.csv`](../../data/seeded/hall_misaligned.csv)): the leading cause is *Hall contacts not exactly opposite each other* at 55%, with *Magnetic field lower than the value you set* at 44%.
2. Recommended test: **Repeat with the magnetic field reversed** (3 min, 1.00 bits).
3. With its result ([`hall_misaligned_reversed.csv`](../../data/seeded/hall_misaligned_reversed.csv)): *Hall contacts not exactly opposite each other*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`hall/`](hall/)); each gives the result above. [Excel export](hall/excel_export.csv) · [Semicolons, decimal commas](hall/semicolon_decimal_comma.csv) · [Tab-separated](hall/tab_separated.tsv) · [UTF-16 "Unicode text"](hall/unicode_text.txt) · [Other column names](hall/other_column_names.csv)

## Magnetic hysteresis (B–H loop)

Flux density in a transformer core against the magnetising field around a full loop, for its coercivity, remanence and saturation.

| | |
| --- | --- |
| Model | `H = N₁I/ℓ,  B = Φ/(N₂A)` |
| Columns | `H_A_per_m`, `B_T` (one row per reading; `#` lines are comments) |
| You enter | Expected coercivity (A/m) (default 45); Expected remanence (T) (default 0.83); Expected B at the loop tip (T) (default 1.42); Search-coil turns N₂ used to work out B (default 100); B reading precision (T) (default 0.005); H reading precision (A/m) (default 2) |
| Physics code | [`sandbox/tools/bench_advanced.py`](../../sandbox/tools/bench_advanced.py), fitted inside the glovebox |
| Fault library | [`faults/bench_advanced.yaml`](../../faults/bench_advanced.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `hysteresis` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Search coil's turns not as stated | A rewound search coil with 88 turns instead of 100 makes every B 12% low | Use the turns found from the 10-turn comparison (N₂ = 10 × the ratio), recompute B = Φ/(N₂A), and refit. |
| Core cross-section wrong (outside size used, tape and lamination gaps included) | A taped toroid's outside dimensions can overstate the iron's area by 10–20% | Use the iron's own cross-section (the lamination stack's width × height × a stacking factor of about 0.95, or the datasheet's effective area), recompute B, and refit. |
| Fluxmeter (integrator) drifting during the loop | An integrator offset of a few µV creeps by a few hundredths of a tesla over a slow loop | Null the fluxmeter's drift with the search coil connected (until the reading holds still for a minute), then trace the loop again, more quickly. |
| Fluxmeter zeroed with the core still magnetised (not demagnetised first) | Zeroing on a magnetised core shifts the whole loop up or down by as much as the remanence | Demagnetise the core (reduce an alternating current slowly to zero), zero the fluxmeter, take the initial curve up to the top field, then trace the loop. |
| Unknown cause (none of the above fits well) |  | Check the H calibration (magnetising turns, mean path length, current reading) and the core for an air gap or damage. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Compare the search coil with a freshly wound 10-turn coil | 4 | Wind 10 turns of insulated wire round the core beside the search coil. Reverse the magnetising current from +I to −I five times reading the fluxmeter on the search coil, then five times on the 10-turn coil. The ratio of the readings is N₂ ÷ 10. *Safety:* Turn the magnetising current to zero before winding or reconnecting anything; the winding is inductive and breaking its current can give a shock or an arc. The winding can be hot after a long run. |
| Measure the core's iron cross-section | 5 | Measure the lamination stack's width and height with callipers where it is bare (or read the datasheet's effective area), allow for the stacking factor, and compare with the area you used. *Safety:* Turn the magnetising current to zero first; the winding is inductive and can be hot after a long run. |
| Hold the current at zero for a minute and watch the fluxmeter | 2 | Set the magnetising current to zero and leave everything still. The reading should stay put; drift shows as a steady creep. |
| Demagnetise, re-zero and trace the loop again | 10 | Reduce an alternating current through the magnetising winding slowly to zero, zero the fluxmeter, take the initial curve to the top field, then trace the loop. *Safety:* Turn the current down slowly rather than switching it off; the winding is inductive and can arc. |

### Samples on the page

- **Loop 12% too short**: [`hysteresis_turns.csv`](../../data/seeded/hysteresis_turns.csv). The loop closes and has the expected coercivity, but it is about 12% too short: 1.25 T at the tips and 0.72 T remanence.
- **Loop doesn't close**: [`hysteresis_drift.csv`](../../data/seeded/hysteresis_drift.csv). The loop's coercivity and height look right, but it doesn't close: it ends about 0.07 T above where it started.
- **Healthy loop**: [`hysteresis_clean.csv`](../../data/seeded/hysteresis_clean.csv). Nothing should look off: a closed loop with coercivity 45 A/m, remanence 0.83 T and 1.42 T at the tips.
- Sample result of *Compare the search coil with a freshly wound 10-turn coil*: [`hysteresis_turns_reference.csv`](../../data/seeded/hysteresis_turns_reference.csv)

### The demo case

1. **Loop 12% too short** ([`hysteresis_turns.csv`](../../data/seeded/hysteresis_turns.csv)): the leading cause is *Search coil's turns not as stated* at 53%, with *Core cross-section wrong (outside size used, tape and lamination gaps included)* at 45%.
2. Recommended test: **Compare the search coil with a freshly wound 10-turn coil** (4 min, 0.99 bits).
3. With its result ([`hysteresis_turns_reference.csv`](../../data/seeded/hysteresis_turns_reference.csv)): *Search coil's turns not as stated*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`hysteresis/`](hysteresis/)); each gives the result above. [Excel export](hysteresis/excel_export.csv) · [Semicolons, decimal commas](hysteresis/semicolon_decimal_comma.csv) · [Tab-separated](hysteresis/tab_separated.tsv) · [UTF-16 "Unicode text"](hysteresis/unicode_text.txt) · [Other column names](hysteresis/other_column_names.csv)

## e/m of the electron (fine-beam tube)

Radius of an electron beam's circle in a Helmholtz field against accelerating voltage and coil current, to measure e/m.

| | |
| --- | --- |
| Model | `e/m = 2V/(B r)²,  B = (4/5)^(3/2) μ₀NI/R` |
| Columns | `accelerating_voltage_V`, `coil_current_A`, `beam_radius_cm` (one row per reading; `#` lines are comments) |
| You enter | Coil radius R (m) (default 0.15); Turns per coil N (default 130); Beam radius reading precision (cm) (default 0.05); Accepted e/m (C/kg) (default 1.75882e+11); Hall probe precision (mT) (default 0.01) |
| Physics code | [`sandbox/tools/bench_fields.py`](../../sandbox/tools/bench_fields.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fields.yaml`](../../faults/bench_fields.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `e_over_m` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Beam diameter read with parallax (scale not in the plane of the beam) | A scale a few cm in front of the beam, read without lining up the eye, makes every diameter about 5% small and e/m about 10% high | Read every diameter on the mirror scale with each edge of the beam lined up with its own reflection (or use the tube's internal marks), then refit. |
| Coil constant wrong (turns, radius or spacing of the Helmholtz pair) | Using another pair's data (130 turns and 150 mm for coils of 124 turns and 147.5 mm) puts B 3% high in the analysis and e/m 6% low | Take N and R from the label on these coils and set their spacing equal to R (or use the constant measured with the Hall probe), then refit. |
| Earth's field along the coil axis not cancelled | The UK's horizontal field is about 19 µT; along the coil axis it changes B by 1–3% at these currents and e/m by 2–6% | Turn the apparatus so the coil axis points east–west (or average every current taken facing both ways), then repeat. |
| Voltmeter reads the supply, not the anode–cathode voltage (Wehnelt bias counted in) | With a 25 V bias counted in, e/m comes out about 33% high at 100 V but only 9% high at 300 V | Connect the voltmeter straight across the tube's anode and cathode sockets (or subtract the Wehnelt voltage from every reading), then refit. |
| Unknown cause (none of the above fits well) |  | Check the beam closes on itself in a flat circle (a spiral means the tube is turned in its holder, so the beam isn't at right angles to the field) and that both coils carry the current in the same direction, then repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Re-read the diameters on a mirror scale | 5 | Put the mirror scale behind the tube, line each edge of the beam up with its own reflection before reading it, and repeat the same voltages and currents. *Safety:* The anode runs at up to 300 V. Leave the connections alone while the supply is on and switch off before moving anything near the tube's sockets. The tube is evacuated glass; don't knock it or lean on it. |
| Measure the coil constant with a calibrated Hall probe | 10 | With the anode supply off, zero a calibrated Hall probe in its zero-gauss chamber, put it at the centre of the coils and read the field at five currents from 0.5 to 2.5 A. *Safety:* Switch the 300 V anode supply off before reaching into the coils. The coils get warm at 2–3 A; keep within their rated current and turn it down between readings. |
| Turn the apparatus round and reset the beam to the same diameter | 6 | At 100 V, set the current that puts the beam on the 10 cm diameter five times; then turn the whole base round to face the other way and do the same. The Earth's field along the axis changes sign, so the current needed changes if that field matters. *Safety:* Switch the supplies off before turning the base, so no lead pulls out of a 300 V socket, and carry the tube on its base, never by the glass. |
| Read the voltage across the tube's own anode and cathode sockets | 3 | At one setting, read the voltmeter as it was wired for the run five times; switch off, move its leads to the tube's anode and cathode sockets, switch on and read it five times again. *Safety:* Move the leads only with the supply switched off; the anode is at up to 300 V. Use shrouded 4 mm leads rated for the voltage. |

### Samples on the page

- **e/m 11% high at every voltage**: [`em_parallax.csv`](../../data/seeded/em_parallax.csv). e/m comes out about 11% high, by the same amount at every voltage and current.
- **e/m high, worst at low voltage**: [`em_wehnelt.csv`](../../data/seeded/em_wehnelt.csv). e/m comes out high, by about a third at 100 V but much less at 300 V.
- **Healthy measurement**: [`em_clean.csv`](../../data/seeded/em_clean.csv). Nothing should look off: every reading gives e/m = 1.76 × 10¹¹ C/kg.
- Sample result of *Re-read the diameters on a mirror scale*: [`em_parallax_mirror.csv`](../../data/seeded/em_parallax_mirror.csv)

### The demo case

1. **e/m 11% high at every voltage** ([`em_parallax.csv`](../../data/seeded/em_parallax.csv)): the leading cause is *Beam diameter read with parallax (scale not in the plane of the beam)* at 53%, with *Coil constant wrong (turns, radius or spacing of the Helmholtz pair)* at 45%.
2. Recommended test: **Re-read the diameters on a mirror scale** (5 min, 0.99 bits).
3. With its result ([`em_parallax_mirror.csv`](../../data/seeded/em_parallax_mirror.csv)): *Beam diameter read with parallax (scale not in the plane of the beam)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`e_over_m/`](e_over_m/)); each gives the result above. [Excel export](e_over_m/excel_export.csv) · [Semicolons, decimal commas](e_over_m/semicolon_decimal_comma.csv) · [Tab-separated](e_over_m/tab_separated.tsv) · [UTF-16 "Unicode text"](e_over_m/unicode_text.txt) · [Other column names](e_over_m/other_column_names.csv)

## Electron spin resonance (DPPH) *(graduate)*

Resonance field of a DPPH sample against radio frequency in Helmholtz coils, to measure the electron's g-factor.

| | |
| --- | --- |
| Model | `h f = g μ_B B` |
| Columns | `rf_frequency_MHz`, `resonance_field_mT` (one row per reading; `#` lines are comments) |
| You enter | g-factor of DPPH (default 2.0036); Resonance field reading precision (mT) (default 0.01) |
| Physics code | [`sandbox/tools/bench_fields.py`](../../sandbox/tools/bench_fields.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fields.yaml`](../../faults/bench_fields.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `esr` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Field zero offset (Hall probe not zeroed, or a residual field along the coils) | A gaussmeter left 0.1 mT off zero shifts every resonance by 0.1 mT; the slope, and so g, is unchanged | Zero the Hall probe in its zero-gauss chamber (or take each resonance as the mean of the forward and reversed field magnitudes), then refit. |
| Resonance read off the edge of the line (modulation phase not set) | With the phase off, the up- and down-sweep signals don't coincide and the peak read sits about half a line width (0.1 mT) to one side | Turn the phase shifter until the up- and down-sweep signals lie on top of each other (or null the quadrature on the lock-in), read the centre of the line, and repeat. |
| Field calibration off (coil constant or gaussmeter range) | A coil constant 4% too high puts every field 4% high and g about 4% low (1.93 instead of 2.004) | Calibrate the field at the sample against a calibrated Hall probe (or recompute the coil constant from N, R and the spacing), then refit. |
| RF frequency misread at one point (counter digits or range) | Two digits swapped (68.4 for 64.8 MHz) put one point 0.13 mT off the line | Set the RF to that point again, read the counter carefully (gate time and range), and refit with the corrected frequency. |
| Unknown cause (none of the above fits well) |  | Check that the sample sits at the centre of the coils, that the line is not saturated (lower the RF level), and read the resonance at a few frequencies again. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Reverse the field and read the resonances again | 4 | Swap the leads of the Helmholtz coils so the field points the other way, and read the resonance field at the same frequencies, noting the magnitudes. A field zero offset adds on one side and subtracts on the other; a reading bias does not. *Safety:* Turn the coil current to zero before swapping the leads; the coils are inductive and can spark at the plug. Keep the RF level low and don't touch the RF coil or its leads while the oscillator is on. |
| Set the modulation phase and re-read the resonances | 6 | At one frequency, turn the phase shifter until the signals of the up- and down-sweep lie on top of each other (or null the quadrature on the lock-in), then read the resonance at five frequencies as before and again with the phase set. *Safety:* Keep the RF level low and your hands off the RF coil while the oscillator is on; switch it off before touching the sample holder. |
| Compare the field with a calibrated Hall probe at the sample | 10 | Take the sample out, zero a calibrated Hall probe in its zero-gauss chamber and put it where the sample sat; at six coil currents compare its reading with the field used in the run. *Safety:* Switch the RF oscillator off before reaching into the coils, and keep the coil current within its rating; the coils get warm. |
| Read the frequency counter again at every point | 5 | Set the RF to each frequency in turn, read the counter with its gate at 1 s and its range noted, and read the resonance field again. *Safety:* Change between RF plug-in coils only with the oscillator switched off, and don't touch the coil while it's on. |

### Samples on the page

- **Line misses the origin**: [`esr_probe_offset.csv`](../../data/seeded/esr_probe_offset.csv). The slope gives the right g, but the line doesn't pass through the origin: every resonance sits about 0.1 mT high.
- **g comes out 4% low**: [`esr_field_scale.csv`](../../data/seeded/esr_field_scale.csv). The line goes through the origin, but its slope gives g about 4% low.
- **One point off the line**: [`esr_counter_misread.csv`](../../data/seeded/esr_counter_misread.csv). Eleven points lie on the line with the right g, but the one at 68.4 MHz sits well below it.
- **Healthy measurement**: [`esr_clean.csv`](../../data/seeded/esr_clean.csv). Nothing should look off: a straight line through the origin with g = 2.0036.
- Sample result of *Reverse the field and read the resonances again*: [`esr_probe_offset_reversed.csv`](../../data/seeded/esr_probe_offset_reversed.csv)

### The demo case

1. **Line misses the origin** ([`esr_probe_offset.csv`](../../data/seeded/esr_probe_offset.csv)): the leading cause is *Field zero offset (Hall probe not zeroed, or a residual field along the coils)* at 53%, with *Resonance read off the edge of the line (modulation phase not set)* at 45%.
2. Recommended test: **Reverse the field and read the resonances again** (4 min, 0.99 bits).
3. With its result ([`esr_probe_offset_reversed.csv`](../../data/seeded/esr_probe_offset_reversed.csv)): *Field zero offset (Hall probe not zeroed, or a residual field along the coils)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`esr/`](esr/)); each gives the result above. [Excel export](esr/excel_export.csv) · [Semicolons, decimal commas](esr/semicolon_decimal_comma.csv) · [Tab-separated](esr/tab_separated.tsv) · [UTF-16 "Unicode text"](esr/unicode_text.txt) · [Other column names](esr/other_column_names.csv)

## Pulsed NMR spin echo *(graduate)*

Hahn echo amplitude against echo time, to measure the spin-spin relaxation time T₂.

| | |
| --- | --- |
| Model | `A(2τ) = A₀ e^(−2τ/T₂)` |
| Columns | `echo_time_ms`, `echo_amplitude_mV` (one row per reading; `#` lines are comments) |
| You enter | Expected T₂ (ms) (default 20); Echo amplitude on the reference sample (mV) (default 500); 90° pulse length set (µs) (default 10); Reading precision (mV) (default 3) |
| Physics code | [`sandbox/tools/bench_graduate.py`](../../sandbox/tools/bench_graduate.py), fitted inside the glovebox |
| Fault library | [`faults/bench_graduate.yaml`](../../faults/bench_graduate.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `nmr_echo` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| RF pulses not 90° and 180° (pulse length mis-set) | Pulses at 60% of the true 90° length leave the echo at about half its full size | Set the 90° pulse to the first maximum of the nutation sweep (and the 180° to twice it), then repeat the echo decay. |
| Sample sitting partly outside the RF coil (wrong depth) | A tube set a centimetre high can lose 30–50% of the signal | Set the sample depth with the depth gauge so the liquid fills the coil, then repeat. |
| Molecules diffusing through a field gradient (magnet poorly shimmed) | A few gauss per cm in water adds an e^(−(2τ)³) decay that shortens the apparent T₂ | Shim the magnet (or move the sample to the field's sweet spot) and measure T₂ with a CPMG train, which suppresses diffusion loss. |
| Sample really relaxes faster (paramagnetic impurity or wrong dopant) |  | Make up a fresh sample with the stated dopant concentration (and degas it if oxygen matters), then repeat. |
| Unknown cause (none of the above fits well) |  | Check the spectrometer on a reference sample with a known T₂, then compare the two decays point by point. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Run a nutation sweep (FID amplitude against pulse length) | 4 | Apply one pulse, read the FID amplitude, and step the pulse length from 2 to 34 µs. The first maximum is the true 90° pulse. *Safety:* Keep ferromagnetic tools, keys and phones away from the magnet, and no one with a pacemaker or implant near it. Don't touch the probe connector while the RF is on. |
| Measure the decay with a CPMG echo train | 6 | Record a Carr-Purcell-Meiboom-Gill train with a short echo spacing (1 ms). Short spacing suppresses diffusion loss. The Meiboom–Gill phase shift largely compensates mis-set 180° pulses, so a CPMG train decays smoothly even when the pulses are off; a plain Carr–Purcell train would not. *Safety:* Keep ferromagnetic tools, keys and phones away from the magnet, and no one with a pacemaker or implant near it. |
| Re-seat the sample with the depth gauge and repeat one echo | 5 | Lift the tube out, set its depth with the gauge so the liquid fills the coil, and repeat the echo at the shortest 2τ. *Safety:* Keep ferromagnetic tools, keys and phones away from the magnet, and no one with a pacemaker or implant near it. |

### Samples on the page

- **Echo only half its usual size**: [`nmr_pulse_misset.csv`](../../data/seeded/nmr_pulse_misset.csv). The decay has the right T₂, but the echo starts at about 290 mV instead of 500 mV.
- **Decay curves down too fast**: [`nmr_diffusion.csv`](../../data/seeded/nmr_diffusion.csv). The echo starts at the right size, but the decay bends downward and drops much faster than T₂ = 20 ms at long echo times.
- **Healthy echo decay**: [`nmr_clean.csv`](../../data/seeded/nmr_clean.csv). Nothing should look off: a single exponential with T₂ = 20 ms and a 500 mV echo.
- Sample result of *Run a nutation sweep (FID amplitude against pulse length)*: [`nmr_pulse_misset_nutation.csv`](../../data/seeded/nmr_pulse_misset_nutation.csv)

### The demo case

1. **Echo only half its usual size** ([`nmr_pulse_misset.csv`](../../data/seeded/nmr_pulse_misset.csv)): the leading cause is *RF pulses not 90° and 180° (pulse length mis-set)* at 53%, with *Sample sitting partly outside the RF coil (wrong depth)* at 45%.
2. Recommended test: **Run a nutation sweep (FID amplitude against pulse length)** (4 min, 1.00 bits).
3. With its result ([`nmr_pulse_misset_nutation.csv`](../../data/seeded/nmr_pulse_misset_nutation.csv)): *RF pulses not 90° and 180° (pulse length mis-set)*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`nmr_echo/`](nmr_echo/)); each gives the result above. [Excel export](nmr_echo/excel_export.csv) · [Semicolons, decimal commas](nmr_echo/semicolon_decimal_comma.csv) · [Tab-separated](nmr_echo/tab_separated.tsv) · [UTF-16 "Unicode text"](nmr_echo/unicode_text.txt) · [Other column names](nmr_echo/other_column_names.csv)
