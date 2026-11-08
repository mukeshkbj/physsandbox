# Condensed matter

3 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Condensed matter*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [X-ray Bragg diffraction (NaCl)](#x-ray-bragg-diffraction-nacl-graduate) | graduate | `nλ = 2d sin θ` | Scan the detector through the direct beam with the crystal removed | [Excel](bragg_xray/excel_export.csv) · [Semicolons](bragg_xray/semicolon_decimal_comma.csv) · [Tabs](bragg_xray/tab_separated.tsv) · [UTF-16](bragg_xray/unicode_text.txt) · [Renamed](bragg_xray/other_column_names.csv) |
| [Superconducting transition](#superconducting-transition-graduate) | graduate | `R(T) = R_n(T) / (1 + e^(−(T−Tc)/w))` | Record a warming sweep as well and compare it with the cooling sweep | [Excel](sc_transition/excel_export.csv) · [Semicolons](sc_transition/semicolon_decimal_comma.csv) · [Tabs](sc_transition/tab_separated.tsv) · [UTF-16](sc_transition/unicode_text.txt) · [Renamed](sc_transition/other_column_names.csv) |
| [Band gap of germanium](#band-gap-of-germanium-graduate) | graduate | `R ∝ T^(−3/2) e^(Eg/2kT)` | Keep logging as the oven cools back down | [Excel](band_gap/excel_export.csv) · [Semicolons](band_gap/semicolon_decimal_comma.csv) · [Tabs](band_gap/tab_separated.tsv) · [UTF-16](band_gap/unicode_text.txt) · [Renamed](band_gap/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## X-ray Bragg diffraction (NaCl) *(graduate)*

Angles of the Mo Kα Bragg peaks from an NaCl crystal, orders 1 to 4, to measure its lattice spacing.

| | |
| --- | --- |
| Model | `nλ = 2d sin θ` |
| Columns | `order_n`, `angle_deg` (one row per reading; `#` lines are comments) |
| You enter | X-ray wavelength, Mo Kα (pm) (default 71.07); NaCl (200) spacing d (pm) (default 282); Peak angle precision (°) (default 0.05); Mo Kβ wavelength (pm) (default 63.26) |
| Physics code | [`sandbox/tools/bench_fields.py`](../../sandbox/tools/bench_fields.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fields.yaml`](../../faults/bench_fields.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `bragg_xray` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Goniometer zero misset (every angle read from a wrong zero) | A zero 0.5° off makes d from the first order about 7% small but from the fourth only 1.5% small, so the orders disagree | Set the goniometer zero on the direct beam (detector peak at 0°, crystal parallel to the beam), or subtract the fitted zero from every angle, and refit. |
| Crystal not at the 2:1 coupled position (turned in its holder) | A crystal turned 0.5° in its holder shifts every peak by 0.5° and lowers it, as the reflected beam lands off the centre of the detector slit | Reclamp the crystal flat against its holder's stop, set the crystal zero with the detector on a known peak (rocking curve), and repeat the scan in coupled mode. |
| Kβ peak taken for Kα at one order | Mo Kβ (63.3 pm) sits just below each Kα peak; at the third order it is 2.5° lower | At that order, take the stronger, higher-angle peak of the pair (the one that stays with the zirconium filter in), and refit. |
| Wrong crystal in the holder (not NaCl) | A LiF crystal (d = 201.4 pm) in the NaCl box gives a d 29% small, consistent from order to order | Fit the labelled NaCl crystal (or use the d of the crystal that was in) and repeat the scan. |
| Unknown cause (none of the above fits well) |  | Check the anode (Mo or Cu) against the wavelength used, the crystal face against the holder, and repeat the scan in coupled mode. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Scan the detector through the direct beam with the crystal removed | 5 | Take the crystal out, put the attenuator in, turn the emission current to its lowest setting and scan the detector alone from −1.5° to +3° in 0.1° steps. The beam should peak at 0°; a goniometer zero error δ puts it at 2δ on the detector scale. *Safety:* The X-ray tube sits in an interlocked lead-glass enclosure. Change the crystal only with the high voltage off, close the door before switching on, and never defeat or bridge the interlocks. Keep the emission current at its minimum while the detector looks into the direct beam. |
| Rock the crystal with the detector parked on a peak | 8 | Park the detector on the second-order peak, then turn the crystal alone through ±1.5° about half the detector angle in 0.1° steps. With the coupling right the crystal peaks at half the detector angle. *Safety:* Run it with the enclosure door closed and the interlocks working; never defeat or bridge them, and switch the high voltage off before opening the door. |
| Repeat two orders on the reference NaCl crystal | 10 | Measure the first two orders on the crystal used, then, with the high voltage off, swap in the lab's labelled reference NaCl crystal and measure the same two orders without touching the goniometer zero. *Safety:* Switch the high voltage off and open the door only then; never defeat the interlocks. Hold crystals by their edges (NaCl is brittle and dissolves in sweat; LiF is toxic if swallowed), and wash your hands afterwards. |
| Count at the odd peak with and without the zirconium filter | 4 | Set the crystal and detector on the peak that sits off the line and count five times without the filter, then five times with the zirconium filter in the beam. Zr passes about half of the Mo Kα but only a few per cent of the Kβ. *Safety:* Fit the filter only with the high voltage off and the door open, close the door before switching on, and never defeat or bridge the interlocks. |

### Samples on the page

- **The orders disagree on d**: [`bragg_zero_offset.csv`](../../data/seeded/bragg_zero_offset.csv). d comes out small from the first order and closer to 282 pm from the fourth: the orders disagree.
- **Third order off the curve**: [`bragg_kbeta.csv`](../../data/seeded/bragg_kbeta.csv). Three orders give d = 282.0 pm, but the third-order peak sits well below the curve through them.
- **d 29% small**: [`bragg_lif.csv`](../../data/seeded/bragg_lif.csv). All four orders agree with one another, but on a d about 29% below 282.0 pm.
- **Healthy measurement**: [`bragg_clean.csv`](../../data/seeded/bragg_clean.csv). Nothing should look off: every order gives d = 282.0 pm.
- Sample result of *Scan the detector through the direct beam with the crystal removed*: [`bragg_zero_offset_direct_beam.csv`](../../data/seeded/bragg_zero_offset_direct_beam.csv)

### The demo case

1. **The orders disagree on d** ([`bragg_zero_offset.csv`](../../data/seeded/bragg_zero_offset.csv)): the leading cause is *Goniometer zero misset (every angle read from a wrong zero)* at 53%, with *Crystal not at the 2:1 coupled position (turned in its holder)* at 45%.
2. Recommended test: **Scan the detector through the direct beam with the crystal removed** (5 min, 0.99 bits).
3. With its result ([`bragg_zero_offset_direct_beam.csv`](../../data/seeded/bragg_zero_offset_direct_beam.csv)): *Goniometer zero misset (every angle read from a wrong zero)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`bragg_xray/`](bragg_xray/)); each gives the result above. [Excel export](bragg_xray/excel_export.csv) · [Semicolons, decimal commas](bragg_xray/semicolon_decimal_comma.csv) · [Tab-separated](bragg_xray/tab_separated.tsv) · [UTF-16 "Unicode text"](bragg_xray/unicode_text.txt) · [Other column names](bragg_xray/other_column_names.csv)

## Superconducting transition *(graduate)*

Four-probe resistance of a YBCO pellet against temperature, to find Tc and the transition width.

| | |
| --- | --- |
| Model | `R(T) = R_n(T) / (1 + e^(−(T−Tc)/w))` |
| Columns | `temperature_K`, `resistance_mOhm` (one row per reading; `#` lines are comments) |
| You enter | Expected Tc (K) (default 92); Expected 10–90% width (K) (default 1); Reading precision (mΩ) (default 0.01) |
| Physics code | [`sandbox/tools/bench_graduate.py`](../../sandbox/tools/bench_graduate.py), fitted inside the glovebox |
| Fault library | [`faults/bench_graduate.yaml`](../../faults/bench_graduate.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `sc_transition` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Thermometer not at the sample's temperature (lag or gradient) | Sweeping at 2 K/min with the sensor on the cold stage can put the reading 1–2 K off the sample | Mount the thermometer on the sample block with grease, sweep slower (under 0.5 K/min), and quote Tc as the mean of the cooling and warming sweeps. |
| Measuring current too high (near the critical current) | Near Jc the transition moves down by a kelvin or more and broadens | Drop the current tenfold (use a lock-in or a nanovoltmeter to keep the signal) and repeat the sweep. |
| Sample degraded (oxygen loss lowers Tc) |  | Re-anneal the pellet in flowing oxygen (or use a fresh one) and store it dry. |
| Thermal EMF at the voltage contacts (resistance never reaches zero) | A few microvolts of thermocouple voltage at the contacts reads as 0.01–0.1 mΩ | Average readings with the current forward and reversed (or use AC with a lock-in), and keep the leads' joints at one temperature. |
| Unknown cause (none of the above fits well) |  | Check the four contacts' resistances and the thermometer calibration at 77 K in liquid nitrogen. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Record a warming sweep as well and compare it with the cooling sweep | 15 | Lift the probe just out of the liquid nitrogen and log R and T as it warms through 110 K at the same rate. If the sample lags the thermometer, its transition appears at a higher thermometer reading on warming and a lower one on cooling. *Safety:* Liquid nitrogen causes cold burns; wear cryogenic gloves and a face shield, and never seal a dewar. Use it only in a ventilated room, as boil-off can displace the oxygen in a closed one. |
| Repeat the sweep at a tenth of the current | 25 | Drop the current from 100 mA to 10 mA and sweep again, averaging more readings per point to keep the noise down. *Safety:* Liquid nitrogen causes cold burns; wear cryogenic gloves and a face shield, and never seal a dewar. Use it only in a ventilated room, as boil-off can displace the oxygen in a closed one. |
| Read the voltage below Tc with the current forward and reversed | 3 | Hold the sample at 80 K and read the voltage at +100 mA and −100 mA. A thermal EMF keeps its sign; a real resistance flips with the current. *Safety:* Liquid nitrogen causes cold burns; wear cryogenic gloves and never seal a dewar. |

### Samples on the page

- **Transition low and broad**: [`sc_lag.csv`](../../data/seeded/sc_lag.csv). The resistance drops to zero, but about 1.5 K low and spread over more than 2 K.
- **Resistance never reaches zero**: [`sc_thermal_emf.csv`](../../data/seeded/sc_thermal_emf.csv). The transition is sharp and at 92 K, but below it the resistance stays at about 0.06 mΩ instead of zero.
- **Healthy transition**: [`sc_clean.csv`](../../data/seeded/sc_clean.csv). Nothing should look off: a sharp drop to zero at 92 K.
- Sample result of *Record a warming sweep as well and compare it with the cooling sweep*: [`sc_lag_warming.csv`](../../data/seeded/sc_lag_warming.csv)

### The demo case

1. **Transition low and broad** ([`sc_lag.csv`](../../data/seeded/sc_lag.csv)): the leading cause is *Thermometer not at the sample's temperature (lag or gradient)* at 54%, with *Measuring current too high (near the critical current)* at 46%.
2. Recommended test: **Record a warming sweep as well and compare it with the cooling sweep** (15 min, 0.99 bits).
3. With its result ([`sc_lag_warming.csv`](../../data/seeded/sc_lag_warming.csv)): *Thermometer not at the sample's temperature (lag or gradient)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`sc_transition/`](sc_transition/)); each gives the result above. [Excel export](sc_transition/excel_export.csv) · [Semicolons, decimal commas](sc_transition/semicolon_decimal_comma.csv) · [Tab-separated](sc_transition/tab_separated.tsv) · [UTF-16 "Unicode text"](sc_transition/unicode_text.txt) · [Other column names](sc_transition/other_column_names.csv)

## Band gap of germanium *(graduate)*

Resistance of an undoped germanium bar against temperature in its intrinsic range, to measure the band gap.

| | |
| --- | --- |
| Model | `R ∝ T^(−3/2) e^(Eg/2kT)` |
| Columns | `temperature_K`, `resistance_ohm` (one row per reading; `#` lines are comments) |
| You enter | Expected band gap (eV): Ge 0.67, Si 1.12 (default 0.67); Resistance reading precision (%) (default 0.5); Temperature reading precision (K) (default 0.5) |
| Physics code | [`sandbox/tools/bench_optics2.py`](../../sandbox/tools/bench_optics2.py), fitted inside the glovebox |
| Fault library | [`faults/bench_optics2.yaml`](../../faults/bench_optics2.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `band_gap` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Sample lagging the oven's thermometer while it heats | Heating at 10 K/min with the bar on its board two minutes behind the thermometer puts the sample 20 K cooler than the reading, and Eg comes out about 9% high | Heat more slowly (2 K/min or less) or hold each temperature until R stops changing, put the thermometer against the sample's board, and quote Eg from the mean of a heating and a cooling sweep. |
| Oven thermometer reading high (two-wire lead resistance or calibration) | A Pt100 read two-wire adds 2.6 K for every ohm of lead, and an uncalibrated sensor can be several kelvin out; reading 20 K high makes Eg about 9% high, just like a lag | Read the Pt100 four-wire, or calibrate the oven thermometer against a reference thermometer at two steady temperatures and correct every reading, then refit. |
| Readings taken below the intrinsic region (impurity carriers at the cold end) | In 'undoped' germanium the residual impurities still supply carriers below about 320–340 K, so R stops rising as fast on cooling and the cold end bends below the line | Fit only the straight, hot part of the plot (above the bend), or take readings further up, and quote Eg from that range. |
| Sample current too high (the bar heats itself) | 20 mA through the bar (190 Ω at 340 K) puts 76 mW into it, enough to warm it a few kelvin at the cold end, where R is largest; the cold end bends down and Eg comes out low | Turn the current down until halving it no longer changes R (1 mA or less for this bar), then repeat the sweep. |
| Contacts degraded (a resistance in series with the bar) | 3 Ω of bad solder joints is under 2% of the reading at 340 K (190 Ω) but over a third at 450 K (8 Ω), so the hot end flattens and Eg comes out 10–15% low | Measure four-terminal (current through the end contacts, voltage across the inner pair) or remake the contacts, then repeat the hot end. |
| Unknown cause (none of the above fits well) |  | Check the sample's identity (germanium or silicon) and its rated temperature, the current source's setting, and repeat the sweep slowly. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Keep logging as the oven cools back down | 10 | After the heating sweep, ramp the oven down at a similar rate and read R at the same thermometer readings on the way down, logging a cooling column (0 heating, 1 cooling). A sample lagging the thermometer sits on opposite sides of it going up and coming down. *Safety:* The oven and the sample board reach 180 °C. Don't touch them or the leads' clips while hot, let the board cool before handling it, and keep below the sample's rated temperature. |
| Compare the oven thermometer with a calibrated one at a steady temperature | 15 | Hold the oven at 400 K with a calibrated thermometer against the sample's board, wait until both readings stop drifting (about ten minutes), then take six readings of each. *Safety:* The oven is at 127 °C during the check; put the reference probe in with the oven's tongs or holder, not your fingers, and close the lid before reading. |
| Repeat the three coldest temperatures at half the current | 6 | At the three coldest temperatures, read R at the run's current and again at half of it, letting each reading settle, and log the current in a current_mA column. *Safety:* The oven and board are hot; change the current at the source, not by unclipping leads, and keep the bar below its rated temperature (an intrinsic semiconductor's falling R lets a high current run away). |
| Read the hot end four-terminal as well | 5 | At the four hottest temperatures, read R across the end (current) contacts as in the run and across the inner (voltage) contacts, at the same current, logging both. *Safety:* The board is at up to 180 °C at the hot end; move the voltage clips with insulated tweezers or let it cool first. |

### Samples on the page

- **Band gap 9% high**: [`bandgap_lag.csv`](../../data/seeded/bandgap_lag.csv). The plot is a straight line, but its slope gives a band gap about 9% above 0.67 eV.
- **Line bends over at the hot end**: [`bandgap_contacts.csv`](../../data/seeded/bandgap_contacts.csv). The cold end looks right, but the line bends over towards the hot end and its slope gives a band gap about 13% low.
- **Healthy measurement**: [`bandgap_clean.csv`](../../data/seeded/bandgap_clean.csv). Nothing should look off: ln(R·T^3/2) against 1/T is a straight line whose slope gives Eg of about 0.66 eV.
- Sample result of *Keep logging as the oven cools back down*: [`bandgap_lag_cooling.csv`](../../data/seeded/bandgap_lag_cooling.csv)

### The demo case

1. **Band gap 9% high** ([`bandgap_lag.csv`](../../data/seeded/bandgap_lag.csv)): the leading cause is *Sample lagging the oven's thermometer while it heats* at 56%, with *Oven thermometer reading high (two-wire lead resistance or calibration)* at 42%.
2. Recommended test: **Keep logging as the oven cools back down** (10 min, 0.99 bits).
3. With its result ([`bandgap_lag_cooling.csv`](../../data/seeded/bandgap_lag_cooling.csv)): *Sample lagging the oven's thermometer while it heats*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`band_gap/`](band_gap/)); each gives the result above. [Excel export](band_gap/excel_export.csv) · [Semicolons, decimal commas](band_gap/semicolon_decimal_comma.csv) · [Tab-separated](band_gap/tab_separated.tsv) · [UTF-16 "Unicode text"](band_gap/unicode_text.txt) · [Other column names](band_gap/other_column_names.csv)
