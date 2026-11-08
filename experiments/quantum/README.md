# Quantum

10 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Quantum*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Electron diffraction (de Broglie)](#electron-diffraction-de-broglie) | teaching lab | `λ = h/√(2meV),  2d sin θ = λ,  D = 2L tan 2θ` | Measure the foil-to-screen distance with a rule | [Excel](electron_diffraction/excel_export.csv) · [Semicolons](electron_diffraction/semicolon_decimal_comma.csv) · [Tabs](electron_diffraction/tab_separated.tsv) · [UTF-16](electron_diffraction/unicode_text.txt) · [Renamed](electron_diffraction/other_column_names.csv) |
| [Zeeman effect (cadmium red line)](#zeeman-effect-cadmium-red-line-graduate) | graduate | `Δν̃ = 2μ_B B/hc = (1/2nt)·δ/Δ` | Measure the field in the gap with a calibrated gaussmeter | [Excel](zeeman/excel_export.csv) · [Semicolons](zeeman/semicolon_decimal_comma.csv) · [Tabs](zeeman/tab_separated.tsv) · [UTF-16](zeeman/unicode_text.txt) · [Renamed](zeeman/other_column_names.csv) |
| [Millikan oil drop](#millikan-oil-drop) | teaching lab | `q = n·e` | Measure the plate spacing with callipers | [Excel](millikan/excel_export.csv) · [Semicolons](millikan/semicolon_decimal_comma.csv) · [Tabs](millikan/tab_separated.tsv) · [UTF-16](millikan/unicode_text.txt) · [Renamed](millikan/other_column_names.csv) |
| [Photoelectric effect (h/e)](#photoelectric-effect-he) | teaching lab | `eV_s = hf − φ` | Mask the anode so only the cathode is lit, and reread every line | [Excel](photoelectric/excel_export.csv) · [Semicolons](photoelectric/semicolon_decimal_comma.csv) · [Tabs](photoelectric/tab_separated.tsv) · [UTF-16](photoelectric/unicode_text.txt) · [Renamed](photoelectric/other_column_names.csv) |
| [Franck–Hertz experiment (mercury)](#franckhertz-experiment-mercury) | teaching lab | `peaks at V = V_c + n·E₁/e` | Read the oven thermometer for a few minutes | [Excel](franck_hertz/excel_export.csv) · [Semicolons](franck_hertz/semicolon_decimal_comma.csv) · [Tabs](franck_hertz/tab_separated.tsv) · [UTF-16](franck_hertz/unicode_text.txt) · [Renamed](franck_hertz/other_column_names.csv) |
| [Optical pumping of rubidium](#optical-pumping-of-rubidium-graduate) | graduate | `hf = g_F μ_B \|k·I + B₀\|` | Read the coil current on a calibrated ammeter in series | [Excel](optical_pumping/excel_export.csv) · [Semicolons](optical_pumping/semicolon_decimal_comma.csv) · [Tabs](optical_pumping/tab_separated.tsv) · [UTF-16](optical_pumping/unicode_text.txt) · [Renamed](optical_pumping/other_column_names.csv) |
| [Planck's constant from LEDs](#plancks-constant-from-leds) | teaching lab | `eV = hf − φ` | Read one LED's turn-on voltage on a calibrated reference meter too | [Excel](planck_led/excel_export.csv) · [Semicolons](planck_led/semicolon_decimal_comma.csv) · [Tabs](planck_led/tab_separated.tsv) · [UTF-16](planck_led/unicode_text.txt) · [Renamed](planck_led/other_column_names.csv) |
| [Quantum tunnelling simulation](#quantum-tunnelling-simulation) | teaching lab | `T ≈ e^(−2κa), κ = √(2m(V₀−E))/ħ` | Rerun the simulation at a second energy (0.25 eV) | [Excel](tunnelling/excel_export.csv) · [Semicolons](tunnelling/semicolon_decimal_comma.csv) · [Tabs](tunnelling/tab_separated.tsv) · [UTF-16](tunnelling/unicode_text.txt) · [Renamed](tunnelling/other_column_names.csv) |
| [Blackbody radiation](#blackbody-radiation) | teaching lab | `B(λ,T) ∝ λ⁻⁵ / (e^(hc/λkT) − 1)` | Record a mercury calibration lamp on the same spectrometer | [Excel](blackbody/excel_export.csv) · [Semicolons](blackbody/semicolon_decimal_comma.csv) · [Tabs](blackbody/tab_separated.tsv) · [UTF-16](blackbody/unicode_text.txt) · [Renamed](blackbody/other_column_names.csv) |
| [Atomic spectral lines (hydrogen)](#atomic-spectral-lines-hydrogen) | teaching lab | `1/λ = R(1/2² − 1/n²)` | Remeasure the odd line with a fresh hydrogen tube | [Excel](spectral_lines/excel_export.csv) · [Semicolons](spectral_lines/semicolon_decimal_comma.csv) · [Tabs](spectral_lines/tab_separated.tsv) · [UTF-16](spectral_lines/unicode_text.txt) · [Renamed](spectral_lines/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Electron diffraction (de Broglie)

Graphite diffraction rings against accelerating voltage, to check λ = h/p and the lattice spacings.

| | |
| --- | --- |
| Model | `λ = h/√(2meV),  2d sin θ = λ,  D = 2L tan 2θ` |
| Columns | `voltage_kV`, `ring`, `diameter_mm` (one row per reading; `#` lines are comments) |
| You enter | Foil-to-screen distance L (mm) (default 135); Inner ring spacing d₁₀ (nm) (default 0.213); Outer ring spacing d₁₁ (nm) (default 0.123); Diameter reading precision (mm) (default 0.5) |
| Physics code | [`sandbox/tools/bench_atomic.py`](../../sandbox/tools/bench_atomic.py), fitted inside the glovebox |
| Fault library | [`faults/bench_atomic.yaml`](../../faults/bench_atomic.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `electron_diffraction` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Foil-to-screen distance L wrong (another tube's figure, or measured from the wrong point) | Entering 135 mm for a tube whose foil sits 125 mm from the screen makes both spacings 8% large | Use the measured foil-to-screen distance (graphite foil to the screen along the axis) and refit. |
| Accelerating voltage reads off (supply meter gain error) | A supply meter reading 15% high makes λ, and both spacings, about 7% small | Read the anode voltage on a calibrated high-voltage divider, correct the readings by the ratio, and refit. |
| Faint third ring (d = 0.107 nm) measured as the outer ring | The outer spacing comes out 13% small while the inner ring is right | Remeasure the second ring out from the centre (the bright 0.123 nm ring), not the faint one beyond it. |
| Unknown cause (none of the above fits well) |  | Check the rings are centred on the undiffracted spot and measure each diameter on two axes. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the foil-to-screen distance with a rule | 3 | With the supply off, measure from the graphite foil (just behind the anode aperture) to the screen along the tube axis, several times. *Safety:* Switch off and unplug the high-voltage supply before reaching near the tube. It is evacuated glass; don't knock it or lean on the screen. |
| Count the rings out from the centre at one voltage | 2 | At 4 kV in a darkened room, count the rings from the central spot outwards and note which one was measured as the outer ring (the bright 0.123 nm ring is the second; a faint one lies beyond it). *Safety:* Keep to the tube's rated voltage and don't touch the tube or its leads while the supply is on. |
| Read the accelerating voltage on a calibrated high-voltage divider | 8 | With the supply off, connect a calibrated divider across the anode supply, then step through 2.5–5 kV and compare with the supply meter. *Safety:* The anode runs at up to 5 kV. Make every connection with the supply off and discharged, use HV-rated leads, and never exceed the tube's rated voltage. |

### Samples on the page

- **Both spacings 8% large**: [`ediff_camera_length.csv`](../../data/seeded/ediff_camera_length.csv). Both rings shrink with voltage as they should, but both lattice spacings come out about 8% large, by the same factor.
- **Outer ring spacing off**: [`ediff_third_ring.csv`](../../data/seeded/ediff_third_ring.csv). The inner ring gives 0.213 nm, but the outer ring's spacing comes out well below 0.123 nm.
- **Healthy measurement**: [`ediff_clean.csv`](../../data/seeded/ediff_clean.csv). Nothing should look off: both rings give the graphite spacings 0.213 and 0.123 nm.
- Sample result of *Measure the foil-to-screen distance with a rule*: [`ediff_camera_length_ruler.csv`](../../data/seeded/ediff_camera_length_ruler.csv)

### The demo case

1. **Both spacings 8% large** ([`ediff_camera_length.csv`](../../data/seeded/ediff_camera_length.csv)): the leading cause is *Foil-to-screen distance L wrong (another tube's figure, or measured from the wrong point)* at 53%, with *Accelerating voltage reads off (supply meter gain error)* at 45%.
2. Recommended test: **Measure the foil-to-screen distance with a rule** (3 min, 0.99 bits).
3. With its result ([`ediff_camera_length_ruler.csv`](../../data/seeded/ediff_camera_length_ruler.csv)): *Foil-to-screen distance L wrong (another tube's figure, or measured from the wrong point)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`electron_diffraction/`](electron_diffraction/)); each gives the result above. [Excel export](electron_diffraction/excel_export.csv) · [Semicolons, decimal commas](electron_diffraction/semicolon_decimal_comma.csv) · [Tab-separated](electron_diffraction/tab_separated.tsv) · [UTF-16 "Unicode text"](electron_diffraction/unicode_text.txt) · [Other column names](electron_diffraction/other_column_names.csv)

## Zeeman effect (cadmium red line) *(graduate)*

Splitting of the Cd 643.8 nm line in a magnetic field, read on a Fabry–Pérot étalon, to measure the Bohr magneton.

| | |
| --- | --- |
| Model | `Δν̃ = 2μ_B B/hc = (1/2nt)·δ/Δ` |
| Columns | `field_mT`, `r1_inner_mm`, `r1_outer_mm`, `r2_inner_mm`, `r2_outer_mm` (one row per reading; `#` lines are comments) |
| You enter | Étalon thickness t (mm) (default 3); Étalon refractive index n (default 1.457); Accepted Bohr magneton (J/T) (default 9.27401e-24); Ring radius precision (mm) (default 0.01); Gaussmeter precision (mT) (default 2) |
| Physics code | [`sandbox/tools/bench_atomic.py`](../../sandbox/tools/bench_atomic.py), fitted inside the glovebox |
| Fault library | [`faults/bench_atomic.yaml`](../../faults/bench_atomic.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `zeeman` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Field reading off (gaussmeter on the wrong scale or not zeroed) | A gaussmeter reading 12% high makes the Bohr magneton come out about 11% low | Zero the gaussmeter in its zero-gauss chamber, check its range, or calibrate it against a reference probe at the lamp position; correct the fields and refit. |
| Étalon thickness or refractive index wrong in the analysis | Leaving out the index (n = 1.457) makes every splitting 46% large | Take the étalon's thickness and index from its certificate (or measure its free spectral range) and refit. |
| Rings of neighbouring orders paired wrongly at one field | Near half a free spectral range, σ⁺ of one order sits as close to σ⁻ of the next as to its own partner | Reread that field's rings, following each order out from the centre as the field is raised, and refit. |
| One field reading wrong (gaussmeter range switched or value misread at that point) |  | Set that magnet current again, read the field with the probe where the lamp sits, and refit. |
| Unknown cause (none of the above fits well) |  | Check the polariser (σ components only), the field uniformity over the lamp, and the camera focus on the rings. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the field in the gap with a calibrated gaussmeter | 5 | Remove the lamp, put a calibrated Hall probe where the lamp sat, step the magnet current and read both gaussmeters at each step. *Safety:* Strong electromagnet. Keep steel tools, watches and cards away from the gap, no pacemakers nearby, and ramp the current down slowly (the coils kick back when switched off). |
| Reread the ring orders at the odd field | 4 | Raise the field slowly from zero while watching the camera image, and follow each σ pair out from the centre so every ring keeps its order. *Safety:* Strong electromagnet. Keep steel tools, watches and cards away from the gap, and ramp the current down slowly. |
| Measure the étalon's free spectral range with the sodium D doublet | 12 | Swap in a sodium lamp, read the rings of the D lines (0.597 nm apart) and compare their spacing with the one the étalon constants predict. *Safety:* Discharge lamps run from a high-voltage supply and get hot; switch off and let the cadmium lamp cool before swapping. |

### Samples on the page

- **Bohr magneton 11% low**: [`zeeman_field_scale.csv`](../../data/seeded/zeeman_field_scale.csv). The splitting is proportional to B, but its slope gives a Bohr magneton about 11% low.
- **Highest field off the line**: [`zeeman_ring_order.csv`](../../data/seeded/zeeman_ring_order.csv). Every field lies on the expected line except the highest, whose splitting sits well above it.
- **Healthy measurement**: [`zeeman_clean.csv`](../../data/seeded/zeeman_clean.csv). Nothing should look off: the splitting rises in proportion to B and gives the Bohr magneton.
- Sample result of *Measure the field in the gap with a calibrated gaussmeter*: [`zeeman_field_scale_gaussmeter.csv`](../../data/seeded/zeeman_field_scale_gaussmeter.csv)

### The demo case

1. **Bohr magneton 11% low** ([`zeeman_field_scale.csv`](../../data/seeded/zeeman_field_scale.csv)): the leading cause is *Field reading off (gaussmeter on the wrong scale or not zeroed)* at 53%, with *Étalon thickness or refractive index wrong in the analysis* at 45%.
2. Recommended test: **Measure the field in the gap with a calibrated gaussmeter** (5 min, 0.99 bits).
3. With its result ([`zeeman_field_scale_gaussmeter.csv`](../../data/seeded/zeeman_field_scale_gaussmeter.csv)): *Field reading off (gaussmeter on the wrong scale or not zeroed)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`zeeman/`](zeeman/)); each gives the result above. [Excel export](zeeman/excel_export.csv) · [Semicolons, decimal commas](zeeman/semicolon_decimal_comma.csv) · [Tab-separated](zeeman/tab_separated.tsv) · [UTF-16 "Unicode text"](zeeman/unicode_text.txt) · [Other column names](zeeman/other_column_names.csv)

## Millikan oil drop

Charges of single oil drops, to show they come in whole steps and measure e.

| | |
| --- | --- |
| Model | `q = n·e` |
| Columns | `drop`, `charge_1e19C` (one row per reading; `#` lines are comments) |
| You enter | Accepted e (C) (default 1.60218e-19); Charge precision per drop (%) (default 2); Plate spacing used for the charges (mm) (default 7.6) |
| Physics code | [`sandbox/tools/bench_atomic.py`](../../sandbox/tools/bench_atomic.py), fitted inside the glovebox |
| Fault library | [`faults/bench_atomic.yaml`](../../faults/bench_atomic.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `millikan` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Plate spacing wrong in the field E = V/d | Using 7.60 mm for a 6.70 mm spacer makes every charge 13% high, still in whole steps | Use the measured spacer thickness, scale every charge by measured ÷ used spacing, and refit. |
| Plate voltage reads off (supply meter gain error) | A meter reading 10% high makes every charge about 9% low | Read the plate voltage on a calibrated meter, scale every charge by supply ÷ true voltage, and refit. |
| Drops evaporating while being timed | Each drop shrinks by a different amount, so its charge comes out several % low and the whole steps blur | Use low-vapour-pressure oil (silicone or Millikan oil), keep the lamp's heat filter in, and time each drop soon after it is sprayed. |
| Unknown cause (none of the above fits well) |  | Check the viscosity of air at the chamber's temperature and the oil density, and time a few drops again. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the plate spacing with callipers | 4 | Switch off, open the chamber, lift the top plate and measure the spacer ring at several places around it. *Safety:* The plates run at several hundred volts. Switch the supply off and let the interlock discharge the plates before opening the chamber. |
| Read the plate voltage on a calibrated meter | 7 | With the supply off, connect a calibrated meter across the plate terminals, then step through the working voltages and compare with the supply meter. *Safety:* Several hundred volts across the plates. Connect the meter with the supply off, use rated leads, and keep the chamber interlock closed. |
| Time the same drop rising and falling repeatedly | 5 | Hold one drop in view and time it over the same graticule distance, down and up, ten times; an evaporating drop falls more slowly each time. *Safety:* The plate voltage is switched on and off repeatedly; keep the chamber closed and your hands off the terminals. |

### Samples on the page

- **e comes out 13% high**: [`millikan_spacing.csv`](../../data/seeded/millikan_spacing.csv). The charges fall in clean whole steps, but the step comes out about 13% above e.
- **Charges don't fall in whole steps**: [`millikan_evaporation.csv`](../../data/seeded/millikan_evaporation.csv). The charges scatter between whole steps, mostly on the low side.
- **Healthy measurement**: [`millikan_clean.csv`](../../data/seeded/millikan_clean.csv). Nothing should look off: every charge is a whole multiple of 1.60 × 10⁻¹⁹ C.
- Sample result of *Measure the plate spacing with callipers*: [`millikan_spacing_callipers.csv`](../../data/seeded/millikan_spacing_callipers.csv)

### The demo case

1. **e comes out 13% high** ([`millikan_spacing.csv`](../../data/seeded/millikan_spacing.csv)): the leading cause is *Plate spacing wrong in the field E = V/d* at 53%, with *Plate voltage reads off (supply meter gain error)* at 45%.
2. Recommended test: **Measure the plate spacing with callipers** (4 min, 0.99 bits).
3. With its result ([`millikan_spacing_callipers.csv`](../../data/seeded/millikan_spacing_callipers.csv)): *Plate spacing wrong in the field E = V/d*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`millikan/`](millikan/)); each gives the result above. [Excel export](millikan/excel_export.csv) · [Semicolons, decimal commas](millikan/semicolon_decimal_comma.csv) · [Tab-separated](millikan/tab_separated.tsv) · [UTF-16 "Unicode text"](millikan/unicode_text.txt) · [Other column names](millikan/other_column_names.csv)

## Photoelectric effect (h/e)

Stopping voltage for mercury lines through filters, to measure h/e and the work function.

| | |
| --- | --- |
| Model | `eV_s = hf − φ` |
| Columns | `wavelength_nm`, `stopping_voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Accepted h/e (V·s) (default 4.13567e-15); Reading precision (V) (default 0.01) |
| Physics code | [`sandbox/tools/bench_core.py`](../../sandbox/tools/bench_core.py), fitted inside the glovebox |
| Fault library | [`faults/bench_core.yaml`](../../faults/bench_core.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `photoelectric` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Light reaching the anode (reverse photocurrent) | A coated anode lit by stray light can pull the slope 10–15% low | Fit the mask or aperture so the light falls only on the cathode, realign the lamp, then remeasure every line. |
| Stopping-voltage meter reading low or high (gain error) | A panel meter reading 10% low makes h/e come out 10% low | Read the stopping voltage on a calibrated meter (or correct every reading by its ratio to one), then refit. |
| A filter leaking a neighbouring, higher-frequency line | Green leaking through the yellow filter raises that point by about 0.12 V | Replace the leaking filter (or add a second one), check it on a spectrometer, and remeasure that line. |
| Unknown cause (none of the above fits well) |  | Record the full current–voltage curve for each line and look at how it approaches zero. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Mask the anode so only the cathode is lit, and reread every line | 4 | Fit the aperture mask (or turn the tube) so no light reaches the anode ring, then read the stopping voltage for each filter again. *Safety:* Mercury lamps emit ultraviolet that can burn eyes and skin. Keep the lamp housing closed, don't look into the aperture, and let the lamp cool before touching it. |
| Check the stopping voltage on a calibrated meter | 7 | Fetch a calibrated meter, put it across the anode and cathode terminals and compare it with the panel reading at three settings. |
| Look at the light through each filter with a spectrometer | 3 | Put each filter between the lamp and a fibre spectrometer and check that only its own mercury line comes through. *Safety:* Mercury lamps emit ultraviolet; keep the housing closed and never look straight at the lamp. |

### Samples on the page

- **h/e comes out 12% low**: [`photo_anode.csv`](../../data/seeded/photo_anode.csv). The five points lie on a good straight line, but its slope gives h/e about 12% below the accepted value.
- **Yellow point sits above the line**: [`photo_filter_leak.csv`](../../data/seeded/photo_filter_leak.csv). Four lines fall on a straight line, but the yellow 577 nm point sits about 0.12 V above it.
- **Healthy measurement**: [`photo_clean.csv`](../../data/seeded/photo_clean.csv). Nothing should look off: the slope of stopping voltage against frequency gives h/e.
- Sample result of *Mask the anode so only the cathode is lit, and reread every line*: [`photo_anode_masked.csv`](../../data/seeded/photo_anode_masked.csv)

### The demo case

1. **h/e comes out 12% low** ([`photo_anode.csv`](../../data/seeded/photo_anode.csv)): the leading cause is *Light reaching the anode (reverse photocurrent)* at 53%, with *Stopping-voltage meter reading low or high (gain error)* at 45%.
2. Recommended test: **Mask the anode so only the cathode is lit, and reread every line** (4 min, 0.99 bits).
3. With its result ([`photo_anode_masked.csv`](../../data/seeded/photo_anode_masked.csv)): *Light reaching the anode (reverse photocurrent)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`photoelectric/`](photoelectric/)); each gives the result above. [Excel export](photoelectric/excel_export.csv) · [Semicolons, decimal commas](photoelectric/semicolon_decimal_comma.csv) · [Tab-separated](photoelectric/tab_separated.tsv) · [UTF-16 "Unicode text"](photoelectric/unicode_text.txt) · [Other column names](photoelectric/other_column_names.csv)

## Franck–Hertz experiment (mercury)

Anode current against accelerating voltage in a heated mercury tube; the peak spacing gives the first excitation energy.

| | |
| --- | --- |
| Model | `peaks at V = V_c + n·E₁/e` |
| Columns | `accelerating_voltage_V`, `anode_current_nA` (one row per reading; `#` lines are comments) |
| You enter | First excitation energy (eV) (default 4.9); Peak reading precision (V) (default 0.15); Oven set point (°C) (default 180) |
| Physics code | [`sandbox/tools/bench_core.py`](../../sandbox/tools/bench_core.py), fitted inside the glovebox |
| Fault library | [`faults/bench_core.yaml`](../../faults/bench_core.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `franck_hertz` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Oven too cool (mercury vapour too thin) | At 145 °C instead of 180 °C the dips fill in and the first peak barely shows | Let the oven reach its set point (about 180 °C for mercury) and settle for ten minutes, then repeat the sweep. |
| Retarding (counter) voltage set too low | At 0.2 V instead of 1.5 V, slowed electrons still reach the anode and the dips fill in | Set the retarding voltage to the tube's recommended value (about 1.5 V), checked with a meter at the terminals, and repeat. |
| Current amplifier saturating (filament or gain too high) | The upper peaks are cut flat at the amplifier's limit | Turn the filament heating down or the amplifier gain down one range until the top peak sits below the limit, then repeat. |
| Accelerating-voltage reading off scale (meter or divider) | A display reading 5% high spreads the peaks 0.25 V too far apart | Check the accelerating-voltage reading (or the ÷10 output used for the scope) against a calibrated meter and rescale. |
| Unknown cause (none of the above fits well) |  | Check the filament current, the tube's wiring against its diagram, and repeat the sweep slowly. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the oven thermometer for a few minutes | 1 | Read the oven's thermometer (or thermocouple) once a minute and compare with the set point. *Safety:* The oven runs at about 180 °C; read it without touching the housing. The tube contains mercury, so don't move it while hot. |
| Measure the retarding voltage at the tube terminals | 3 | Put a meter across the anode and grid-2 terminals and compare with the setting (about 1.5 V). *Safety:* The oven and its terminals get hot (about 180 °C); use insulated probes and don't touch the housing. If the tube ever breaks, leave the room and follow the mercury-spill procedure. |
| Check the accelerating voltage on a calibrated meter | 5 | Put a calibrated meter across the accelerating-voltage terminals and compare it with the display at 10, 20 and 30 V. *Safety:* The oven terminals are hot; use insulated probes. |

### Samples on the page

- **Dips between the peaks are shallow**: [`fh_cool_oven.csv`](../../data/seeded/fh_cool_oven.csv). The peaks are still 4.9 V apart, but the dips are shallow, the current is higher and the first peak barely shows above the rise.
- **Top peaks cut flat**: [`fh_saturated.csv`](../../data/seeded/fh_saturated.csv). The lower peaks look right, but the top two are cut flat at the same current.
- **Healthy sweep**: [`fh_clean.csv`](../../data/seeded/fh_clean.csv). Nothing should look off: peaks about 4.9 V apart with deep dips between them.
- Sample result of *Read the oven thermometer for a few minutes*: [`fh_oven_thermometer.csv`](../../data/seeded/fh_oven_thermometer.csv)

### The demo case

1. **Dips between the peaks are shallow** ([`fh_cool_oven.csv`](../../data/seeded/fh_cool_oven.csv)): the leading cause is *Oven too cool (mercury vapour too thin)* at 53%, with *Retarding (counter) voltage set too low* at 45%.
2. Recommended test: **Read the oven thermometer for a few minutes** (1 min, 1.00 bits).
3. With its result ([`fh_oven_thermometer.csv`](../../data/seeded/fh_oven_thermometer.csv)): *Oven too cool (mercury vapour too thin)*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`franck_hertz/`](franck_hertz/)); each gives the result above. [Excel export](franck_hertz/excel_export.csv) · [Semicolons, decimal commas](franck_hertz/semicolon_decimal_comma.csv) · [Tab-separated](franck_hertz/tab_separated.tsv) · [UTF-16 "Unicode text"](franck_hertz/unicode_text.txt) · [Other column names](franck_hertz/other_column_names.csv)

## Optical pumping of rubidium *(graduate)*

Zeeman resonance frequency of ⁸⁵Rb and ⁸⁷Rb against coil current, to measure the Landé g_F factors.

| | |
| --- | --- |
| Model | `hf = g_F μ_B \|k·I + B₀\|` |
| Columns | `coil_current_A`, `frequency_kHz`, `isotope` (one row per reading; `#` lines are comments) |
| You enter | Sweep coil constant k (µT/A) (default 60); Resonance reading precision (kHz) (default 1) |
| Physics code | [`sandbox/tools/bench_graduate.py`](../../sandbox/tools/bench_graduate.py), fitted inside the glovebox |
| Fault library | [`faults/bench_graduate.yaml`](../../faults/bench_graduate.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `optical_pumping` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Coil current read high or low (ammeter or sense resistor) | A sense resistor 8% off makes both g_F values about 8% off, with the ratio still 3/2 | Correct the current readings by the ratio to the calibrated ammeter (or replace the sense resistor) and refit. |
| Coil constant wrong (turns, radius or spacing) | Coils set 10% off Helmholtz spacing, or a miscounted turn number, scale every g_F alike | Measure the coils' radius and spacing, count or look up the turns, recompute k = (4/5)^(3/2) μ₀N/R, and refit. |
| Lab field along the coil axis not nulled | Earth's horizontal field is about 18 µT in the UK; any part along the axis shifts every resonance | Turn the apparatus to align its axis with the field and null the rest with the horizontal coil (adjust until the zero-field resonance is at its narrowest), then repeat. |
| Coil current reading has a zero offset |  | Zero the meter (or subtract its reading at zero current) and refit. |
| ⁸⁵Rb and ⁸⁷Rb resonances swapped |  | The stronger, lower-frequency resonance is ⁸⁵Rb (72% abundance, g_F = 1/3); relabel and refit. |
| Unknown cause (none of the above fits well) |  | Check the RF frequency on a counter and look for a transverse field (a resonance that bends at low current). |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the coil current on a calibrated ammeter in series | 3 | Put a calibrated ammeter in series with the sweep coil, set 0.5 A on the lab reading, and take ten readings on each. *Safety:* Switch the coil supply off before breaking the circuit; the coils are inductive and can arc. |
| Read the current meter with the coil supply off | 1 | Switch the sweep supply off and read the current meter. It should read zero. |
| Measure the coils' radius and spacing | 10 | Measure each coil's mean radius and the distance between them (it should equal the radius), and check the turn count against the manual. *Safety:* Switch off the RF and let the rubidium lamp and cell oven cool before reaching inside the coils. If your setup pumps with a 795 nm diode laser, wear the laser eyewear; the beam is nearly invisible. |

### Samples on the page

- **Both g_F values 7% low**: [`rb_current_scale.csv`](../../data/seeded/rb_current_scale.csv). Both isotopes give straight lines through zero with the right 3:2 ratio, but both g_F values come out about 7% low.
- **Resonance not at zero frequency at zero current**: [`rb_residual_field.csv`](../../data/seeded/rb_residual_field.csv). The slopes give the right g_F values, but neither line passes through zero frequency at zero current.
- **Healthy measurement**: [`rb_clean.csv`](../../data/seeded/rb_clean.csv). Nothing should look off: g_F = 1/2 and 1/3, lines through zero.
- Sample result of *Read the coil current on a calibrated ammeter in series*: [`rb_current_scale_refmeter.csv`](../../data/seeded/rb_current_scale_refmeter.csv)

### The demo case

1. **Both g_F values 7% low** ([`rb_current_scale.csv`](../../data/seeded/rb_current_scale.csv)): the leading cause is *Coil current read high or low (ammeter or sense resistor)* at 53%, with *Coil constant wrong (turns, radius or spacing)* at 45%.
2. Recommended test: **Read the coil current on a calibrated ammeter in series** (3 min, 0.99 bits).
3. With its result ([`rb_current_scale_refmeter.csv`](../../data/seeded/rb_current_scale_refmeter.csv)): *Coil current read high or low (ammeter or sense resistor)*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`optical_pumping/`](optical_pumping/)); each gives the result above. [Excel export](optical_pumping/excel_export.csv) · [Semicolons, decimal commas](optical_pumping/semicolon_decimal_comma.csv) · [Tab-separated](optical_pumping/tab_separated.tsv) · [UTF-16 "Unicode text"](optical_pumping/unicode_text.txt) · [Other column names](optical_pumping/other_column_names.csv)

## Planck's constant from LEDs

Turn-on voltage of LEDs of different colours, to measure h.

| | |
| --- | --- |
| Model | `eV = hf − φ` |
| Columns | `wavelength_nm`, `turn_on_voltage_V` (one row per reading; `#` lines are comments) |
| You enter | Accepted h (J·s) (default 6.62607e-34); Reading precision (V) (default 0.015) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/bench_quantum.yaml`](../../faults/bench_quantum.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `planck_led` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Voltmeter reading low or high (gain error) | A meter reading 8% low makes h come out about 8% low | Recalibrate or replace the voltmeter, or correct every reading by the ratio to the reference meter, then refit. |
| LED wavelengths taken from the datasheet, not measured | LEDs emit 10–30 nm away from their nominal wavelength, which tilts the line | Measure each LED's peak wavelength with a spectrometer or grating and refit with the measured values. |
| One LED isn't the colour on its label |  | Measure the odd LED's wavelength, correct its label in the data, or drop it and say so. |
| Unknown cause (none of the above fits well) |  | Repeat the run with fresh LEDs and a second meter, and look at the residuals point by point. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read one LED's turn-on voltage on a calibrated reference meter too | 3 | Hold the LED at its turn-on current and read the voltage on the lab meter, then on a calibrated meter, ten times each. |
| Measure each LED's peak wavelength with a spectrometer | 8 | Point a fibre spectrometer at each LED at its turn-on current and record the peak. *Safety:* Don't look straight into bright LEDs; ultraviolet ones can damage your eyes. |

### Samples on the page

- **h comes out 10% low**: [`planck_gain.csv`](../../data/seeded/planck_gain.csv). The points lie on a good straight line, but its slope gives h about 10% below the accepted value.
- **One LED sits off the line**: [`planck_mislabelled.csv`](../../data/seeded/planck_mislabelled.csv). Six LEDs line up and give the right h, but the one labelled 590 nm sits well below the line.
- **Healthy measurement**: [`planck_clean.csv`](../../data/seeded/planck_clean.csv). Nothing should look off: the slope of V against frequency gives h.
- Sample result of *Read one LED's turn-on voltage on a calibrated reference meter too*: [`planck_gain_refmeter.csv`](../../data/seeded/planck_gain_refmeter.csv)

### The demo case

1. **h comes out 10% low** ([`planck_gain.csv`](../../data/seeded/planck_gain.csv)): the leading cause is *Voltmeter reading low or high (gain error)* at 52%, with *LED wavelengths taken from the datasheet, not measured* at 47%.
2. Recommended test: **Read one LED's turn-on voltage on a calibrated reference meter too** (3 min, 1.00 bits).
3. With its result ([`planck_gain_refmeter.csv`](../../data/seeded/planck_gain_refmeter.csv)): *Voltmeter reading low or high (gain error)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`planck_led/`](planck_led/)); each gives the result above. [Excel export](planck_led/excel_export.csv) · [Semicolons, decimal commas](planck_led/semicolon_decimal_comma.csv) · [Tab-separated](planck_led/tab_separated.tsv) · [UTF-16 "Unicode text"](planck_led/unicode_text.txt) · [Other column names](planck_led/other_column_names.csv)

## Quantum tunnelling simulation

Transmission through a rectangular barrier against its width, from a solver.

| | |
| --- | --- |
| Model | `T ≈ e^(−2κa), κ = √(2m(V₀−E))/ħ` |
| Columns | `barrier_width_nm`, `transmission` (one row per reading; `#` lines are comments) |
| You enter | Barrier height V₀ (eV) (default 1); Particle energy E (eV) (default 0.5); Mass (electron masses) (default 1) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/bench_quantum.yaml`](../../faults/bench_quantum.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `tunnelling` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Particle mass wrong in the simulation (units or effective mass) | Half the electron mass makes the decay constant 29% too small | Check the mass used in the code (SI units, and the effective mass if it's a semiconductor), then rerun. |
| Barrier height or energy measured from the wrong zero |  | Print V₀ − E inside the solver and make sure both share the same zero and the same units (J, not eV). |
| Solver grid too coarse to resolve small transmissions | The transmission levels off instead of falling exponentially for thick barriers | Refine the spatial grid (at least 20 points per decay length) or use the transfer-matrix method, then rerun. |
| Unknown cause (none of the above fits well) |  | Compare the solver against the analytic rectangular-barrier formula one width at a time. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Rerun the simulation at a second energy (0.25 eV) | 2 | Keep everything else the same and run at E = 0.25 eV. A mass error scales both energies alike; a wrong energy zero does not. |
| Compare one thick barrier with the analytic formula | 5 | Run a 1.2 nm barrier and compare with T = [1 + V₀² sinh²(κa) / 4E(V₀ − E)]⁻¹. |

### Samples on the page

- **Decays far too slowly**: [`tunnel_mass.csv`](../../data/seeded/tunnel_mass.csv). Transmission falls exponentially, but far more slowly than an electron at this energy should.
- **Levels off for thick barriers**: [`tunnel_floor.csv`](../../data/seeded/tunnel_floor.csv). Right at first, but for thick barriers the transmission stops falling and levels off near 2×10⁻⁴.
- **Healthy simulation**: [`tunnel_clean.csv`](../../data/seeded/tunnel_clean.csv). Nothing should look off: matches the analytic barrier formula.
- Sample result of *Rerun the simulation at a second energy (0.25 eV)*: [`tunnel_mass_two_energies.csv`](../../data/seeded/tunnel_mass_two_energies.csv)

### The demo case

1. **Decays far too slowly** ([`tunnel_mass.csv`](../../data/seeded/tunnel_mass.csv)): the leading cause is *Particle mass wrong in the simulation (units or effective mass)* at 55%, with *Barrier height or energy measured from the wrong zero* at 44%.
2. Recommended test: **Rerun the simulation at a second energy (0.25 eV)** (2 min, 0.99 bits).
3. With its result ([`tunnel_mass_two_energies.csv`](../../data/seeded/tunnel_mass_two_energies.csv)): *Particle mass wrong in the simulation (units or effective mass)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`tunnelling/`](tunnelling/)); each gives the result above. [Excel export](tunnelling/excel_export.csv) · [Semicolons, decimal commas](tunnelling/semicolon_decimal_comma.csv) · [Tab-separated](tunnelling/tab_separated.tsv) · [UTF-16 "Unicode text"](tunnelling/unicode_text.txt) · [Other column names](tunnelling/other_column_names.csv)

## Blackbody radiation

Spectrum of a tungsten lamp, fitted with Planck's law.

| | |
| --- | --- |
| Model | `B(λ,T) ∝ λ⁻⁵ / (e^(hc/λkT) − 1)` |
| Columns | `wavelength_nm`, `spectral_radiance` (one row per reading; `#` lines are comments) |
| You enter | Expected lamp temperature (K) (default 2800) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/bench_quantum.yaml`](../../faults/bench_quantum.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `blackbody` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Spectrometer wavelength scale shifted | A 30 nm shift moves the peak and makes a 2800 K lamp look about 3% cooler | Recalibrate the wavelength axis with the mercury lines, or subtract the measured shift, then refit. |
| Lamp running below its rated temperature (supply low) |  | Set the lamp to its rated voltage, measured at the lamp, let it settle for five minutes and repeat. |
| Stray light or dark current adding a background |  | Take a dark spectrum with the lamp shuttered and subtract it, and close the spectrometer to room light. |
| Unknown cause (none of the above fits well) |  | Check the detector's response curve and whether it was applied to the spectrum. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Record a mercury calibration lamp on the same spectrometer | 3 | Swap in a mercury pen lamp and read its five strongest lines (404.7, 435.8, 546.1, 577.0, 579.1 nm). *Safety:* Mercury lamps emit ultraviolet; keep the cover on and don't look at the bare lamp. |
| Measure the lamp's voltage and current at its terminals | 4 | Compare with the lamp's rating; filament temperature follows its resistance. *Safety:* Tungsten lamps get hot enough to burn; let them cool before handling. |

### Samples on the page

- **Lamp looks 3% cooler than rated**: [`blackbody_shift.csv`](../../data/seeded/blackbody_shift.csv). Planck's law fits, but only at about 2715 K, 3% below the lamp's rating.
- **Spectrum never reaches zero**: [`blackbody_offset.csv`](../../data/seeded/blackbody_offset.csv). The temperature is right, but the spectrum sits about 4% above zero at both ends.
- **Healthy spectrum**: [`blackbody_clean.csv`](../../data/seeded/blackbody_clean.csv). Nothing should look off: Planck's law fits at 2800 K.
- Sample result of *Record a mercury calibration lamp on the same spectrometer*: [`blackbody_shift_hg.csv`](../../data/seeded/blackbody_shift_hg.csv)

### The demo case

1. **Lamp looks 3% cooler than rated** ([`blackbody_shift.csv`](../../data/seeded/blackbody_shift.csv)): the leading cause is *Spectrometer wavelength scale shifted* at 52%, with *Lamp running below its rated temperature (supply low)* at 47%.
2. Recommended test: **Record a mercury calibration lamp on the same spectrometer** (3 min, 1.00 bits).
3. With its result ([`blackbody_shift_hg.csv`](../../data/seeded/blackbody_shift_hg.csv)): *Spectrometer wavelength scale shifted*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`blackbody/`](blackbody/)); each gives the result above. [Excel export](blackbody/excel_export.csv) · [Semicolons, decimal commas](blackbody/semicolon_decimal_comma.csv) · [Tab-separated](blackbody/tab_separated.tsv) · [UTF-16 "Unicode text"](blackbody/unicode_text.txt) · [Other column names](blackbody/other_column_names.csv)

## Atomic spectral lines (hydrogen)

Balmer lines of a hydrogen tube, to measure the Rydberg constant.

| | |
| --- | --- |
| Model | `1/λ = R(1/2² − 1/n²)` |
| Columns | `n_upper`, `wavelength_nm` (one row per reading; `#` lines are comments) |
| You enter | Accepted Rydberg constant (/m) (default 1.0967758e7); Reading precision (nm) (default 0.1) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/bench_quantum.yaml`](../../faults/bench_quantum.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `spectral_lines` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| A line from another element mistaken for a hydrogen line | Mercury's 435.8 nm line sits 1.8 nm from H-gamma at 434.0 nm | Replace the discharge tube (or note the impurity), find the true hydrogen line nearby, and refit. |
| A line assigned the wrong upper level n |  | Reassign the line (red 656 nm is n = 3, then 486, 434, 410, 397 nm) and refit. |
| Spectrometer wavelength calibration offset | A constant shift shows up as an offset the Rydberg formula can't absorb | Recalibrate with a reference lamp, or subtract the fitted offset, and quote it in the result. |
| Unknown cause (none of the above fits well) |  | Check air against vacuum wavelengths and the spectrometer's dispersion calibration. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Remeasure the odd line with a fresh hydrogen tube | 5 | Swap in a new hydrogen discharge tube and read the same line again. *Safety:* Discharge tubes run at several kilovolts; switch off before swapping and let the tube cool. |
| Calibrate the spectrometer with a reference lamp | 4 | Read the lines of a mercury or helium lamp and compare with their tabulated wavelengths. |

### Samples on the page

- **One line is off the series**: [`balmer_impurity.csv`](../../data/seeded/balmer_impurity.csv). Four lines fit the Rydberg formula, but the one taken as n = 5 is almost 2 nm out.
- **Every line a little long**: [`balmer_offset.csv`](../../data/seeded/balmer_offset.csv). Every line reads about 2 nm long, by the same amount.
- **Healthy spectrum**: [`balmer_clean.csv`](../../data/seeded/balmer_clean.csv). Nothing should look off: the Rydberg formula fits every line.
- Sample result of *Remeasure the odd line with a fresh hydrogen tube*: [`balmer_fresh_tube.csv`](../../data/seeded/balmer_fresh_tube.csv)

### The demo case

1. **One line is off the series** ([`balmer_impurity.csv`](../../data/seeded/balmer_impurity.csv)): the leading cause is *A line from another element mistaken for a hydrogen line* at 53%, with *A line assigned the wrong upper level n* at 47%.
2. Recommended test: **Remeasure the odd line with a fresh hydrogen tube** (5 min, 1.00 bits).
3. With its result ([`balmer_fresh_tube.csv`](../../data/seeded/balmer_fresh_tube.csv)): *A line from another element mistaken for a hydrogen line*, 95%, confirmed.

### Example upload files

The headline sample saved five ways ([`spectral_lines/`](spectral_lines/)); each gives the result above. [Excel export](spectral_lines/excel_export.csv) · [Semicolons, decimal commas](spectral_lines/semicolon_decimal_comma.csv) · [Tab-separated](spectral_lines/tab_separated.tsv) · [UTF-16 "Unicode text"](spectral_lines/unicode_text.txt) · [Other column names](spectral_lines/other_column_names.csv)
