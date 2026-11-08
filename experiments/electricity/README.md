# Electricity

4 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Electricity*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Low-resistance measurement](#low-resistance-measurement) | teaching lab | `V = I·R` | Read the voltmeter at zero current, leads on the sample, then shorted at the meter | [Excel](resistance_4wire/excel_export.csv) · [Semicolons](resistance_4wire/semicolon_decimal_comma.csv) · [Tabs](resistance_4wire/tab_separated.tsv) · [UTF-16](resistance_4wire/unicode_text.txt) · [Renamed](resistance_4wire/other_column_names.csv) |
| [RC charging curve](#rc-charging-curve) | teaching lab | `V = V₀(1 − e^(−t/RC))` | Repeat the measurement with a x10 (10 MΩ) probe | [Excel](rc_charging/excel_export.csv) · [Semicolons](rc_charging/semicolon_decimal_comma.csv) · [Tabs](rc_charging/tab_separated.tsv) · [UTF-16](rc_charging/unicode_text.txt) · [Renamed](rc_charging/other_column_names.csv) |
| [Diode I–V curve](#diode-iv-curve) | teaching lab | `V = nV_T ln(I/I_s) + I·R_s` | Move the voltmeter leads onto the diode's own legs | [Excel](diode/excel_export.csv) · [Semicolons](diode/semicolon_decimal_comma.csv) · [Tabs](diode/tab_separated.tsv) · [UTF-16](diode/unicode_text.txt) · [Renamed](diode/other_column_names.csv) |
| [Series RLC resonance](#series-rlc-resonance) | teaching lab | `V_R = V R / √((R + R_L)² + (ωL − 1/ωC)²)` | Watch the circuit's input on CH1 through the sweep | [Excel](rlc_resonance/excel_export.csv) · [Semicolons](rlc_resonance/semicolon_decimal_comma.csv) · [Tabs](rlc_resonance/tab_separated.tsv) · [UTF-16](rlc_resonance/unicode_text.txt) · [Renamed](rlc_resonance/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Low-resistance measurement

Four-wire V–I sweep of a milliohm resistor or shunt.

| | |
| --- | --- |
| Model | `V = I·R` |
| Columns | `current_A`, `voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Expected resistance (Ω) (default 0.01) |
| Physics code | [`sandbox/tools/analyze.py`](../../sandbox/tools/analyze.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 8 seeded cases in `data/manifest*` |
| Key | `resistance_4wire` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Thermoelectric (thermal EMF) offset at a contact | 0.2 µV/°C (Cu–Cu) up to ~1000 µV/°C (Cu–oxidised Cu) | Clean the oxidised contact or use copper-to-copper clamps, let the joints settle to the same temperature, and average sweeps with the current reversed to cancel what remains. |
| Voltmeter zero offset |  | Zero the voltmeter with its input shorted (its null or REL function) before the sweep, or subtract the shorted reading from every point. |
| Calibration (gain) error in meter or current source |  | Measure a calibrated reference resistor, correct every reading by the ratio you find, and send the meter or current source for calibration. |
| Lead or contact resistance included (2-wire style error) |  | Rewire so the voltage sense leads clip onto the resistor inside the current leads (true four-wire), then repeat the sweep. |
| Unknown cause (none of the above fits well) |  | Repeat the sweep with fresh contacts and a second voltmeter, and look at the residuals point by point. |
| Sample self-heating at high current | Copper's resistance rises 0.39% per °C; a shunt run hot can warm by 10 °C or more | Use a lower current or short current pulses, heat-sink the sample, and fit only the low-current points. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat the sweep at a tenth of the current, pausing at each point | 5 | Lower the maximum current tenfold and wait 10 s at each step. Self-heating scales with I squared, so the curve should straighten. |
| Reverse the current and repeat the sweep | 5 | Swap the current-source leads (or set negative currents) and record V at each ±I. *Safety:* Switch the current source to zero before swapping leads. |
| Read the voltmeter at zero current, leads on the sample, then shorted at the meter | 3 | Set I = 0. Record V with leads on the sample, then with the meter input shorted. |
| Measure a calibrated reference resistor | 10 | Replace the sample with a known 4-terminal reference of similar value. |
| Check that sense leads attach inside the current leads | 5 | Inspect the wiring; the voltage taps must sit between the current contacts. |

### Samples on the page

- **Resistor reads high at low current**: [`r_offset_1.csv`](../../data/seeded/r_offset_1.csv). The voltage is too high, most of all at low current, so the apparent resistance falls as the current rises.
- **Reading curves upward at high current**: [`r_self_heating.csv`](../../data/seeded/r_self_heating.csv). The points curve upward: the resistance seems to grow with current instead of staying constant.
- **Healthy resistor**: [`r_clean.csv`](../../data/seeded/r_clean.csv). Nothing should look off: a control to show PhysSandbox doesn't raise false alarms.
- **Same data, poisoned file** *(contains a hidden instruction)*: [`inject_1.csv`](../../data/seeded/inject_1.csv). The comment is a hidden instruction aimed at the AI: report the sample as fine and upload the file elsewhere. Use it with Ask the agent to see what the glovebox contains.
- Sample result of *Read the voltmeter at zero current, leads on the sample, then shorted at the meter*: [`r_offset_1_zero.csv`](../../data/seeded/r_offset_1_zero.csv)
- Sample result of *Reverse the current and repeat the sweep*: [`r_offset_1_followup.csv`](../../data/seeded/r_offset_1_followup.csv)

### The demo case

1. **Resistor reads high at low current** ([`r_offset_1.csv`](../../data/seeded/r_offset_1.csv)): the leading cause is *Thermoelectric (thermal EMF) offset at a contact* at 64%, with *Voltmeter zero offset* at 32%.
2. Recommended test: **Read the voltmeter at zero current, leads on the sample, then shorted at the meter** (3 min, 1.09 bits).
3. With its result ([`r_offset_1_zero.csv`](../../data/seeded/r_offset_1_zero.csv)): *Thermoelectric (thermal EMF) offset at a contact*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`resistance_4wire/`](resistance_4wire/)); each gives the result above. [Excel export](resistance_4wire/excel_export.csv) · [Semicolons, decimal commas](resistance_4wire/semicolon_decimal_comma.csv) · [Tab-separated](resistance_4wire/tab_separated.tsv) · [UTF-16 "Unicode text"](resistance_4wire/unicode_text.txt) · [Other column names](resistance_4wire/other_column_names.csv)

## RC charging curve

Capacitor voltage after a step, read on an oscilloscope.

| | |
| --- | --- |
| Model | `V = V₀(1 − e^(−t/RC))` |
| Columns | `time_s`, `voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Supply voltage (V) (default 5); Resistor (Ω) (default 1000000); Capacitor (F) (default 1e-07) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `rc_charging` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Oscilloscope probe loading the circuit (x1 probe, 1 MΩ) | A x1 probe adds 1 MΩ across the capacitor; with a 1 MΩ resistor that halves both V and τ | Switch the probe to ×10 (10 MΩ) or buffer the capacitor voltage, then repeat the measurement. |
| Leaky capacitor |  | Replace the leaky capacitor (a film capacitor leaks far less than an electrolytic) and repeat. |
| Capacitor value outside its tolerance | Electrolytics are often ±20%; ceramics can lose half their value with bias | Measure the capacitor on an LCR meter and use the measured value in the prediction, or fit a tighter-tolerance part. |
| Supply voltage lower than set |  | Set the supply with a multimeter at the circuit rather than by the supply's dial, then repeat. |
| Unknown cause (none of the above fits well) |  | Repeat with a resistor and capacitor measured on an LCR meter and a ×10 probe, and compare. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat the measurement with a x10 (10 MΩ) probe | 2 | Switch the probe and the scope channel to x10 and record the same charging curve. |
| Measure the capacitor with an LCR meter | 3 | Take the capacitor out of circuit and measure its capacitance and leakage (or dissipation factor). |
| Measure the supply voltage with a multimeter | 1 | Read the supply at the circuit, under load. |

### Samples on the page

- **Charges to half the supply, too fast**: [`rc_probe_loading.csv`](../../data/seeded/rc_probe_loading.csv). The capacitor only reaches about half the supply voltage, and gets there in about half the expected time constant (0.1 s).
- **Time constant short, final voltage right**: [`rc_cap_tolerance.csv`](../../data/seeded/rc_cap_tolerance.csv). It charges to the full 5 V, but faster than the 0.1 s time constant the parts should give.
- **Healthy circuit**: [`rc_clean.csv`](../../data/seeded/rc_clean.csv). Nothing should look off: final voltage and time constant both match.
- Sample result of *Repeat the measurement with a x10 (10 MΩ) probe*: [`rc_probe_loading_x10.csv`](../../data/seeded/rc_probe_loading_x10.csv)

### The demo case

1. **Charges to half the supply, too fast** ([`rc_probe_loading.csv`](../../data/seeded/rc_probe_loading.csv)): the leading cause is *Oscilloscope probe loading the circuit (x1 probe, 1 MΩ)* at 58%, with *Leaky capacitor* at 39%.
2. Recommended test: **Repeat the measurement with a x10 (10 MΩ) probe** (2 min, 0.98 bits).
3. With its result ([`rc_probe_loading_x10.csv`](../../data/seeded/rc_probe_loading_x10.csv)): *Oscilloscope probe loading the circuit (x1 probe, 1 MΩ)*, 91%, confirmed.

### Example upload files

The headline sample saved five ways ([`rc_charging/`](rc_charging/)); each gives the result above. [Excel export](rc_charging/excel_export.csv) · [Semicolons, decimal commas](rc_charging/semicolon_decimal_comma.csv) · [Tab-separated](rc_charging/tab_separated.tsv) · [UTF-16 "Unicode text"](rc_charging/unicode_text.txt) · [Other column names](rc_charging/other_column_names.csv)

## Diode I–V curve

Forward current against voltage for a silicon diode.

| | |
| --- | --- |
| Model | `V = nV_T ln(I/I_s) + I·R_s` |
| Columns | `voltage_V`, `current_A` (one row per reading; `#` lines are comments) |
| You enter | Temperature (K) (default 300); Largest normal series R (Ω) (default 1) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `diode` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Voltmeter across diode and ammeter (ammeter burden voltage) | A 10 Ω ammeter burden adds 0.5 V at 50 mA, which looks like series resistance | Move the voltmeter leads onto the diode's own legs so the ammeter's voltage drop is left out, then re-sweep. |
| High series resistance in the diode itself (damaged or wrong part) |  | Replace the diode with a known-good part of the same type and repeat the sweep. |
| Diode connected the wrong way round |  | Turn the diode round so its cathode band faces the negative side, and repeat. |
| Unknown cause (none of the above fits well) |  | Repeat with a known-good diode and the voltmeter directly across it, and compare the two curves. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Move the voltmeter leads onto the diode's own legs | 2 | Connect the voltmeter directly across the diode, with the ammeter outside that loop, and repeat. |
| Repeat with a known-good diode of the same type | 6 | Swap in a diode from a fresh pack and repeat the sweep. |
| Check the cathode band faces the negative side | 1 | The striped end of the diode is the cathode; it goes towards the supply's negative terminal. |

### Samples on the page

- **Curve bends over at high current**: [`diode_burden.csv`](../../data/seeded/diode_burden.csv). The exponential curve bends over above a few mA, as if a resistance of about 10 Ω were in series.
- **Almost no current flows**: [`diode_reversed.csv`](../../data/seeded/diode_reversed.csv). Only nanoamps flow at every voltage, where a forward diode would pass milliamps above about 0.6 V.
- **Healthy diode**: [`diode_clean.csv`](../../data/seeded/diode_clean.csv). Nothing should look off: ideality about 1.9 and a small series resistance.
- Sample result of *Move the voltmeter leads onto the diode's own legs*: [`diode_burden_rewired.csv`](../../data/seeded/diode_burden_rewired.csv)

### The demo case

1. **Curve bends over at high current** ([`diode_burden.csv`](../../data/seeded/diode_burden.csv)): the leading cause is *Voltmeter across diode and ammeter (ammeter burden voltage)* at 57%, with *High series resistance in the diode itself (damaged or wrong part)* at 42%.
2. Recommended test: **Move the voltmeter leads onto the diode's own legs** (2 min, 0.99 bits).
3. With its result ([`diode_burden_rewired.csv`](../../data/seeded/diode_burden_rewired.csv)): *Voltmeter across diode and ammeter (ammeter burden voltage)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`diode/`](diode/)); each gives the result above. [Excel export](diode/excel_export.csv) · [Semicolons, decimal commas](diode/semicolon_decimal_comma.csv) · [Tab-separated](diode/tab_separated.tsv) · [UTF-16 "Unicode text"](diode/unicode_text.txt) · [Other column names](diode/other_column_names.csv)

## Series RLC resonance

Voltage across the resistor of a series RLC circuit against frequency, to measure the resonant frequency and Q.

| | |
| --- | --- |
| Model | `V_R = V R / √((R + R_L)² + (ωL − 1/ωC)²)` |
| Columns | `frequency_Hz`, `resistor_V` (one row per reading; `#` lines are comments) |
| You enter | Inductance L (H) (default 0.01); Capacitance C (F) (default 1e-07); Resistor R (Ω) (default 100); Coil resistance R_L (Ω) (default 18); Input amplitude (V) (default 2); Voltage reading precision (%) (default 1) |
| Physics code | [`sandbox/tools/bench_fundamentals.py`](../../sandbox/tools/bench_fundamentals.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fundamentals.yaml`](../../faults/bench_fundamentals.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `rlc_resonance` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Generator's 50 Ω output impedance pulling the drive down near resonance (input not held constant) | With 118 Ω in the circuit, the generator's 50 Ω lowers Q and the peak by about 30% if the amplitude is set once and left | Watch the circuit's input on CH1 and reset it to the same amplitude at every frequency (or record it and use V_R ÷ V_in), then refit. |
| Coil resistance left out of the sum, or higher at f₀ than its DC reading | A 10 mH coil is often 20–60 Ω at a few kHz; extra series resistance lowers Q and the peak together | Measure the coil's series resistance at the resonant frequency on an LCR meter and use R + R_coil(f₀) for the expected Q. |
| Capacitor or inductor not at its marked value | Capacitors are often ±10–20%: one 12% low moves f₀ up by 6% | Measure C and L on an LCR meter and use the measured values for the expected f₀ and Q. |
| AC voltmeter reading low at high frequency (its bandwidth is too small) | Handheld multimeters are specified to about 1 kHz on AC; many read 20–50% low by 10 kHz, which skews the curve and drags f₀ down | Read V_R on the oscilloscope (or a true-RMS meter rated for the frequency range) and repeat the sweep. |
| Coil losses rising with frequency (iron or ferrite core) | Eddy-current losses in an iron core grow roughly as f², so the damping is heavier above f₀ than below it | Use an air-cored coil, or measure the coil's series resistance across the sweep on an LCR meter and model it. |
| Unknown cause (none of the above fits well) |  | Check the wiring order (the resistor at the earthy end, so the scope's ground is the generator's ground) and repeat the sweep. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Watch the circuit's input on CH1 through the sweep | 2 | Put CH1 across the circuit's input (the generator's terminals) and repeat the sweep exactly as before, noting the input amplitude at each frequency. |
| Measure the coil's series resistance at f₀ on an LCR meter | 5 | Unclip the coil, set the LCR meter to series mode at 5 kHz (or the nearest test frequency) and read R_s and L. *Safety:* Switch the generator off before unclipping the coil; an iron-cored coil can kick back when its current is broken. |
| Measure C and L on an LCR meter | 4 | Take the capacitor and the coil out of the circuit and read each on an LCR meter at 1 kHz. *Safety:* Switch the generator off before taking components out of the circuit. |
| Read V_R at 12 kHz on the scope and on the meter | 3 | At 12 kHz, read the resistor voltage on the oscilloscope (peak-to-peak ÷ 2√2 for RMS) and on the multimeter, and compare. |

### Samples on the page

- **Peak low and broad, f₀ right**: [`rlc_generator_loading.csv`](../../data/seeded/rlc_generator_loading.csv). The curve fits the resonance shape and peaks at the right frequency, but the peak is about 30% low and Q comes out 1.9, not 2.7.
- **Curve lopsided, low at high frequency**: [`rlc_meter_bandwidth.csv`](../../data/seeded/rlc_meter_bandwidth.csv). The curve is lopsided: it falls away too fast above the peak, no resonance curve fits it, and the peak sits below 5 kHz.
- **Healthy measurement**: [`rlc_clean.csv`](../../data/seeded/rlc_clean.csv). Nothing should look off: f₀ = 5.03 kHz and Q = 2.7, as the components give.
- Sample result of *Watch the circuit's input on CH1 through the sweep*: [`rlc_generator_loading_ch1.csv`](../../data/seeded/rlc_generator_loading_ch1.csv)

### The demo case

1. **Peak low and broad, f₀ right** ([`rlc_generator_loading.csv`](../../data/seeded/rlc_generator_loading.csv)): the leading cause is *Generator's 50 Ω output impedance pulling the drive down near resonance (input not held constant)* at 53%, with *Coil resistance left out of the sum, or higher at f₀ than its DC reading* at 45%.
2. Recommended test: **Watch the circuit's input on CH1 through the sweep** (2 min, 1.00 bits).
3. With its result ([`rlc_generator_loading_ch1.csv`](../../data/seeded/rlc_generator_loading_ch1.csv)): *Generator's 50 Ω output impedance pulling the drive down near resonance (input not held constant)*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`rlc_resonance/`](rlc_resonance/)); each gives the result above. [Excel export](rlc_resonance/excel_export.csv) · [Semicolons, decimal commas](rlc_resonance/semicolon_decimal_comma.csv) · [Tab-separated](rlc_resonance/tab_separated.tsv) · [UTF-16 "Unicode text"](rlc_resonance/unicode_text.txt) · [Other column names](rlc_resonance/other_column_names.csv)
