# Mechanics

7 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Mechanics*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Simple pendulum](#simple-pendulum) | teaching lab | `T = 2π√(L/g)` | Repeat three lengths released from 5° or less | [Excel](pendulum/excel_export.csv) · [Semicolons](pendulum/semicolon_decimal_comma.csv) · [Tabs](pendulum/tab_separated.tsv) · [UTF-16](pendulum/unicode_text.txt) · [Renamed](pendulum/other_column_names.csv) |
| [Hooke's law spring](#hookes-law-spring) | teaching lab | `F = mg = k·x` | Weigh the hanger and add its mass to every load | [Excel](hooke/excel_export.csv) · [Semicolons](hooke/semicolon_decimal_comma.csv) · [Tabs](hooke/tab_separated.tsv) · [UTF-16](hooke/unicode_text.txt) · [Renamed](hooke/other_column_names.csv) |
| [Viscosity by Stokes' law (falling ball)](#viscosity-by-stokes-law-falling-ball) | teaching lab | `v = 2r²g(ρ_s − ρ_l) / 9η, corrected for the tube wall` | Read the glycerol's temperature with a thermometer in the tube | [Excel](stokes_viscosity/excel_export.csv) · [Semicolons](stokes_viscosity/semicolon_decimal_comma.csv) · [Tabs](stokes_viscosity/tab_separated.tsv) · [UTF-16](stokes_viscosity/unicode_text.txt) · [Renamed](stokes_viscosity/other_column_names.csv) |
| [Kater's reversible pendulum](#katers-reversible-pendulum) | teaching lab | `T₁ = T₂ = T at the crossing,  g = 4π² L / T²` | Read the swing amplitude on a protractor behind the bar | [Excel](kater_pendulum/excel_export.csv) · [Semicolons](kater_pendulum/semicolon_decimal_comma.csv) · [Tabs](kater_pendulum/tab_separated.tsv) · [UTF-16](kater_pendulum/unicode_text.txt) · [Renamed](kater_pendulum/other_column_names.csv) |
| [Cavendish torsion balance](#cavendish-torsion-balance-graduate) | graduate | `G = 2π² L r² θ / (M T²) ÷ (1 − β),  θ = ΔS / 4D` | Measure the mirror-to-scale distance with a steel tape | [Excel](cavendish/excel_export.csv) · [Semicolons](cavendish/semicolon_decimal_comma.csv) · [Tabs](cavendish/tab_separated.tsv) · [UTF-16](cavendish/unicode_text.txt) · [Renamed](cavendish/other_column_names.csv) |
| [Driven damped oscillator (resonance)](#driven-damped-oscillator-resonance) | teaching lab | `A = a ω₀² / √((ω₀² − ω²)² + (γω)²)` | Time 20 crank turns with a stopwatch at three dial settings | [Excel](driven_oscillator/excel_export.csv) · [Semicolons](driven_oscillator/semicolon_decimal_comma.csv) · [Tabs](driven_oscillator/tab_separated.tsv) · [UTF-16](driven_oscillator/unicode_text.txt) · [Renamed](driven_oscillator/other_column_names.csv) |
| [Boyle's law (syringe and pressure sensor)](#boyles-law-syringe-and-pressure-sensor) | teaching lab | `p (V + V₀) = nRT` | Measure the connecting tube's length and bore | [Excel](boyle_gas/excel_export.csv) · [Semicolons](boyle_gas/semicolon_decimal_comma.csv) · [Tabs](boyle_gas/tab_separated.tsv) · [UTF-16](boyle_gas/unicode_text.txt) · [Renamed](boyle_gas/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Simple pendulum

Period against length, to measure g.

| | |
| --- | --- |
| Model | `T = 2π√(L/g)` |
| Columns | `length_m`, `period_s` (one row per reading; `#` lines are comments) |
| You enter | Expected g (m/s²) (default 9.81) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `pendulum` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Too large a release angle | From 30° every period is about 1.7% long, so g comes out about 3% low | Release from 5° or less, or apply the finite-amplitude correction, and retime. |
| Timer running fast or slow |  | Check the timer against a reference clock and correct every period by the ratio, or time with a light gate. |
| Length measured to the top of the bob, not its centre | A 2 cm bob radius shows up as a 2 cm intercept on the T² against L plot | Measure the length to the centre of the bob, or take g from the slope of T² against L, which ignores the offset. |
| Miscounted swings |  | Time 20 swings with a second person counting aloud, or use a light gate, and retime the odd lengths. |
| Unknown cause (none of the above fits well) |  | Retime each length three times from a small release angle and look at the spread. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat three lengths released from 5° or less | 4 | Pull the bob aside by no more than a tenth of the string length and time 10 swings at three lengths. |
| Check the timer against a phone clock over five minutes | 6 | Start both together, stop both after five minutes and compare. |
| Measure the bob's diameter with callipers | 2 | Add the bob's radius to every length, then refit. |

### Samples on the page

- **g comes out 3% low**: [`pendulum_large_amp.csv`](../../data/seeded/pendulum_large_amp.csv). T² against L is a straight line through the origin, but its slope gives g about 3% below 9.81 m/s².
- **T² line misses the origin**: [`pendulum_length_offset.csv`](../../data/seeded/pendulum_length_offset.csv). The slope gives the right g, but the T² line doesn't pass through the origin.
- **Healthy measurement**: [`pendulum_clean.csv`](../../data/seeded/pendulum_clean.csv). Nothing should look off: g matches and the line goes through the origin.
- Sample result of *Repeat three lengths released from 5° or less*: [`pendulum_large_amp_small.csv`](../../data/seeded/pendulum_large_amp_small.csv)

### The demo case

1. **g comes out 3% low** ([`pendulum_large_amp.csv`](../../data/seeded/pendulum_large_amp.csv)): the leading cause is *Too large a release angle* at 54%, with *Timer running fast or slow* at 45%.
2. Recommended test: **Repeat three lengths released from 5° or less** (4 min, 0.99 bits).
3. With its result ([`pendulum_large_amp_small.csv`](../../data/seeded/pendulum_large_amp_small.csv)): *Too large a release angle*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`pendulum/`](pendulum/)); each gives the result above. [Excel export](pendulum/excel_export.csv) · [Semicolons, decimal commas](pendulum/semicolon_decimal_comma.csv) · [Tab-separated](pendulum/tab_separated.tsv) · [UTF-16 "Unicode text"](pendulum/unicode_text.txt) · [Other column names](pendulum/other_column_names.csv)

## Hooke's law spring

Extension against hanging mass, to measure the spring constant.

| | |
| --- | --- |
| Model | `F = mg = k·x` |
| Columns | `mass_kg`, `extension_m` (one row per reading; `#` lines are comments) |
| You enter | Expected spring constant (N/m) (default 25) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `hooke` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Hanger's mass left out of the loads | A 50 g hanger shows up as about −0.49 N of force at zero extension | Weigh the hanger, add its mass to every load, and refit. |
| Ruler zero read in the wrong place |  | Read the pointer with only the hanger attached and measure every extension from that point. |
| Spring loaded past its elastic limit |  | Replace the overstretched spring and keep loads within the linear range of the new one. |
| A spring with a different constant than expected |  | Check the spring's label or part number and use the right expected k, or swap in the intended spring. |
| Unknown cause (none of the above fits well) |  | Load and unload a fresh spring, reading the pointer both ways, and compare the two runs. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Weigh the hanger and add its mass to every load | 2 | Put the empty hanger on a balance, add its mass to each load and refit. |
| Read the pointer with only the hanger attached and call that zero | 3 | Remove all masses, let the hanger settle and read the pointer at eye level. |
| Unload the spring and check it returns to its original length | 2 | Remove every mass and read the pointer again. |

### Samples on the page

- **Force line misses the origin**: [`hooke_hanger.csv`](../../data/seeded/hooke_hanger.csv). The slope gives the expected spring constant, but the force line misses the origin by about half a newton.
- **Line bends at high loads**: [`hooke_overstretched.csv`](../../data/seeded/hooke_overstretched.csv). At low loads it looks fine, but the line bends: the spring stretches more and more at high loads.
- **Healthy spring**: [`hooke_clean.csv`](../../data/seeded/hooke_clean.csv). Nothing should look off: k matches, line through the origin.
- Sample result of *Weigh the hanger and add its mass to every load*: [`hooke_hanger_included.csv`](../../data/seeded/hooke_hanger_included.csv)

### The demo case

1. **Force line misses the origin** ([`hooke_hanger.csv`](../../data/seeded/hooke_hanger.csv)): the leading cause is *Hanger's mass left out of the loads* at 52%, with *Ruler zero read in the wrong place* at 47%.
2. Recommended test: **Weigh the hanger and add its mass to every load** (2 min, 1.03 bits).
3. With its result ([`hooke_hanger_included.csv`](../../data/seeded/hooke_hanger_included.csv)): *Hanger's mass left out of the loads*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`hooke/`](hooke/)); each gives the result above. [Excel export](hooke/excel_export.csv) · [Semicolons, decimal commas](hooke/semicolon_decimal_comma.csv) · [Tab-separated](hooke/tab_separated.tsv) · [UTF-16 "Unicode text"](hooke/unicode_text.txt) · [Other column names](hooke/other_column_names.csv)

## Viscosity by Stokes' law (falling ball)

Steel balls timed falling through glycerol; terminal velocity against r² gives the viscosity.

| | |
| --- | --- |
| Model | `v = 2r²g(ρ_s − ρ_l) / 9η, corrected for the tube wall` |
| Columns | `ball_diameter_mm`, `fall_time_s` (one row per reading; `#` lines are comments) |
| You enter | Glycerol temperature (°C) (default 20); Distance between the marks (mm) (default 300); Tube inner diameter (mm) (default 50); Ball density (kg/m³) (default 7800); Timing precision (s) (default 0.2); Micrometer reading precision (mm) (default 0.003) |
| Physics code | [`sandbox/tools/bench_fundamentals.py`](../../sandbox/tools/bench_fundamentals.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fundamentals.yaml`](../../faults/bench_fundamentals.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `stokes_viscosity` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Glycerol not at the temperature entered | Glycerol thins about 9% per °C near room temperature: at 22 °C, entered as 20 °C, η comes out 16% low | Enter the temperature measured in the glycerol itself (or let the tube settle to the room's temperature) and compare with η at that temperature. |
| Glycerol has absorbed water from the air | Glycerol is hygroscopic: each 1% of water lowers η by about 15% | Check the water content with a refractometer, replace the glycerol (keep the tube stoppered), or compare with the table for the measured concentration. |
| Ball diameters read on a micrometer that wasn't zeroed | A micrometer reading +0.05 mm with its anvils closed makes a 1 mm ball's r² 10% too large, so the smallest balls give the highest viscosity | Read the micrometer with its anvils closed, subtract that zero reading from every diameter, and refit. |
| Air bubbles clinging to the smallest balls (dropped in dry) | A bubble a few tenths of a millimetre across buoys a 1 mm ball enough to slow it by several % | Wet each ball in glycerol before dropping it, release it just below the surface, and time the small balls again. |
| Unknown cause (none of the above fits well) |  | Drop every ball down the tube's axis (a centring funnel helps), check the marks' separation, and time each ball twice. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the glycerol's temperature with a thermometer in the tube | 2 | Lower a thermometer into the glycerol and read it at several depths, waiting for each reading to settle. |
| Check the glycerol's water content on a refractometer | 5 | Put a drop of the glycerol on an Abbe refractometer; pure glycerol reads n = 1.4740 at 20 °C, and each 1% of water lowers it by about 0.0013. *Safety:* Wipe glycerol spills up straight away; a glycerol-coated floor or bench is very slippery. |
| Read the micrometer with its anvils closed | 1 | Clean the anvils, close them gently with the ratchet and read the scale; it should read 0.000 mm. |
| Wet the two smallest balls in glycerol and time them again | 6 | Dip each ball in glycerol, release it just below the surface down the tube's axis, and time it over the same marks. *Safety:* Recover the balls with a magnet on a rod, not by hand down the tube; tall glass tubes break easily when knocked. |

### Samples on the page

- **Viscosity 16% low, every ball alike**: [`stokes_warm_liquid.csv`](../../data/seeded/stokes_warm_liquid.csv). Every ball gives the same viscosity, but it is about 16% below the table value for glycerol at 20 °C.
- **Small balls give a higher viscosity**: [`stokes_micrometer_zero.csv`](../../data/seeded/stokes_micrometer_zero.csv). The smaller the ball, the higher the viscosity it gives: the small balls fall too slowly for their measured size.
- **Healthy measurement**: [`stokes_clean.csv`](../../data/seeded/stokes_clean.csv). Nothing should look off: corrected for the wall, v rises as r² and every ball gives η = 1.41 Pa·s.
- Sample result of *Read the glycerol's temperature with a thermometer in the tube*: [`stokes_warm_liquid_thermometer.csv`](../../data/seeded/stokes_warm_liquid_thermometer.csv)

### The demo case

1. **Viscosity 16% low, every ball alike** ([`stokes_warm_liquid.csv`](../../data/seeded/stokes_warm_liquid.csv)): the leading cause is *Glycerol not at the temperature entered* at 53%, with *Glycerol has absorbed water from the air* at 45%.
2. Recommended test: **Read the glycerol's temperature with a thermometer in the tube** (2 min, 1.00 bits).
3. With its result ([`stokes_warm_liquid_thermometer.csv`](../../data/seeded/stokes_warm_liquid_thermometer.csv)): *Glycerol not at the temperature entered*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`stokes_viscosity/`](stokes_viscosity/)); each gives the result above. [Excel export](stokes_viscosity/excel_export.csv) · [Semicolons, decimal commas](stokes_viscosity/semicolon_decimal_comma.csv) · [Tab-separated](stokes_viscosity/tab_separated.tsv) · [UTF-16 "Unicode text"](stokes_viscosity/unicode_text.txt) · [Other column names](stokes_viscosity/other_column_names.csv)

## Kater's reversible pendulum

Periods about two knife edges as a slider moves along the bar; where they are equal, g follows from the edges' separation alone.

| | |
| --- | --- |
| Model | `T₁ = T₂ = T at the crossing,  g = 4π² L / T²` |
| Columns | `knife_edge_mass_position_cm`, `period_1_s`, `period_2_s` (one row per reading; `#` lines are comments) |
| You enter | Knife-edge separation L (mm) (default 995); Local g, from a gravity survey (m/s²) (default 9.812); Release amplitude the periods are corrected for (°) (default 2); Swings timed for each period (default 50); Period precision (ms) (default 1); Separation reading precision (mm) (default 0.3) |
| Physics code | [`sandbox/tools/bench_mechanics.py`](../../sandbox/tools/bench_mechanics.py), fitted inside the glovebox |
| Fault library | [`faults/bench_mechanics.yaml`](../../faults/bench_mechanics.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `kater_pendulum` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Swung from a larger angle than the amplitude entered | Every period grows by about θ²/16: from 15° instead of 2° that is 0.42%, so g comes out 0.84% low | Release from 3° or less (about 6 cm of travel at the bar's lower end), or enter the amplitude you measured so the correction θ²/16 is applied, and retime at the crossing. |
| Knife-edge separation L measured wrongly | g ∝ L: measuring to the back of a knife-edge block instead of its edge puts L, and g, out by several mm in a metre (0.5% or more) | Measure L again from edge to edge (a beam compass or a steel rule and a lens on the edges themselves), enter it and recompute g; the periods don't need retiming. |
| Swings miscounted at one slider position | Counting 50 swings when 49 or 51 went by puts that period out by 2% (40 ms), far off its curve | Retime that position with a light gate (or with a partner counting aloud from zero), and keep the crossing from the curves through the other points. |
| One knife edge blunt or slipping on its plate | A rounded or chipped edge rolls instead of pivoting: the periods about that edge scatter by several ms from swing to swing, the other edge's don't | Look at both edges and their agate plates under a lens; clean or regrind the edge, seat it squarely, check the plate is level, and retime the scattered side. |
| Too few swings timed for the precision entered | Starting and stopping a stopwatch is good to about 0.05 s however long the run: over 10 swings that is 5 ms a period, against 1 ms over 50 | Time at least 50 swings for each period (or use a light gate), enter the precision that gives, and retime. |
| Unknown cause (none of the above fits well) |  | Check the bar is rigid and the masses are clamped tight, that the support doesn't sway, and retime two positions on both edges. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the swing amplitude on a protractor behind the bar | 2 | Fix a protractor or an angle scale behind the bar's lower end, release the pendulum exactly as you did for the timings, and read the amplitude on the first swing, five times. *Safety:* The bar with its brass bob weighs over 5 kg and swings with real momentum; stand clear of its path, keep your fingers away from the knife edges and the support, and stop it by hand only near the end of a swing. |
| Measure the knife-edge separation again, edge to edge | 5 | Lift the pendulum off, lay it flat on the bench and measure from one knife edge to the other with a beam compass or a steel rule and a lens, five times. *Safety:* Lift the pendulum with two people, one at each end, and lay it on a padded bench; the brass bob is heavy enough to crush fingers, and dropping it can chip a knife edge. |
| Retime every slider position with a light gate | 25 | Put a light gate at the bottom of the swing, set it to time 50 periods, and repeat the whole sweep about both edges. Add a light_gate column (1) to the file. *Safety:* Stand clear of the swinging bar while the gate runs, and move the slider only with the pendulum at rest and supported; clamp it before letting go, as a loose 1.25 kg slider can slide off the bar. |

### Samples on the page

- **g 0.8% low, smooth curves**: [`kater_amplitude.csv`](../../data/seeded/kater_amplitude.csv). Both curves are smooth and cross cleanly, but the crossing period gives g about 0.8% below the local value.
- **One period far off its curve**: [`kater_miscount.csv`](../../data/seeded/kater_miscount.csv). Eight of the periods about edge 1 lie on a smooth curve; the one at 72.5 cm sits about 40 ms below it.
- **Healthy measurement**: [`kater_clean.csv`](../../data/seeded/kater_clean.csv). Nothing should look off: the curves cross at the period that gives local g.
- Sample result of *Read the swing amplitude on a protractor behind the bar*: [`kater_amplitude_protractor.csv`](../../data/seeded/kater_amplitude_protractor.csv)

### The demo case

1. **g 0.8% low, smooth curves** ([`kater_amplitude.csv`](../../data/seeded/kater_amplitude.csv)): the leading cause is *Swung from a larger angle than the amplitude entered* at 53%, with *Knife-edge separation L measured wrongly* at 45%.
2. Recommended test: **Read the swing amplitude on a protractor behind the bar** (2 min, 0.99 bits).
3. With its result ([`kater_amplitude_protractor.csv`](../../data/seeded/kater_amplitude_protractor.csv)): *Swung from a larger angle than the amplitude entered*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`kater_pendulum/`](kater_pendulum/)); each gives the result above. [Excel export](kater_pendulum/excel_export.csv) · [Semicolons, decimal commas](kater_pendulum/semicolon_decimal_comma.csv) · [Tab-separated](kater_pendulum/tab_separated.tsv) · [UTF-16 "Unicode text"](kater_pendulum/unicode_text.txt) · [Other column names](kater_pendulum/other_column_names.csv)

## Cavendish torsion balance *(graduate)*

Laser spot on a scale after the large lead spheres are swung across; the damped swing's shift and period give the gravitational constant.

| | |
| --- | --- |
| Model | `G = 2π² L r² θ / (M T²) ÷ (1 − β),  θ = ΔS / 4D` |
| Columns | `time_s`, `beam_position_mm` (one row per reading; `#` lines are comments) |
| You enter | Mass of each large sphere M (kg) (default 1.5); Fibre axis to small sphere centre d (mm); L = 2d (default 50); Large to small sphere, centre to centre r (mm) (default 46.5); Mirror-to-scale distance D (m) (default 4.2); Spot reading precision (mm) (default 1); Precision of r and d (mm) (default 0.2) |
| Physics code | [`sandbox/tools/bench_mechanics.py`](../../sandbox/tools/bench_mechanics.py), fitted inside the glovebox |
| Fault library | [`faults/bench_mechanics.yaml`](../../faults/bench_mechanics.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `cavendish` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Mirror-to-scale distance D not what was entered | The spot moves 4θD, so G ∝ 1/D: D taken from a lab sheet after the balance was moved 30 cm puts G out by 8% | Measure D with a steel tape along the beam's path, from the mirror (not the case front) to the scale, enter it and recompute G; the run itself is fine. |
| Large spheres not against the case (centre distance r larger than assumed) | The pull falls as 1/r²: spheres 2 mm short of the case make G come out about 8% low | Turn the swivel arm until both spheres just touch the case in each position (check with a feeler gauge), or measure the real centre distance and enter it, then repeat the swing. |
| Equilibrium drifting (room temperature or fibre creep) | Half a millimetre a minute on the scale is common when the room warms or the fibre has just been loaded; it biases the shift unless it is fitted | Let the balance settle for several hours (overnight after loading the fibre), keep it away from radiators, sun and the door, and record a run with the spheres removed to check that the drift is steady; quote G from the fit with the drift term. |
| Air currents in the case (spot jittering more than the reading precision) | A draught or a warm hand near the case makes the spot wander by several mm over a minute | Close the case (check its glass windows are sealed), shield it from draughts and the heating, keep people away during the run, and repeat the swing. |
| Unknown cause (none of the above fits well) |  | Check the small spheres hang free of the case walls, the beam is level, and the fibre isn't kinked, then repeat the swing. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the mirror-to-scale distance with a steel tape | 3 | Run a steel tape along the laser's path from the balance's mirror to the scale and read it five times, keeping the tape straight and level. *Safety:* The pointer laser is class 2; don't look into the beam or its reflection off the mirror, and keep the tape's shiny blade out of the beam. Don't lean on the bench, as a knock sets the balance swinging for an hour. |
| Check that the large spheres touch the case in both positions | 5 | In each position, slide a feeler gauge between each large sphere and the case wall and record the gap (it should be zero), two spheres in two positions. *Safety:* Each lead sphere weighs 1.5 kg; swing the arm slowly and keep fingers out from between the sphere and the case. Wash your hands after touching the lead. |
| Log the spot for 40 minutes with the large spheres removed | 40 | Lift the large spheres off their arm and set them well away, then read the settled spot every 30 s for 40 minutes; with nothing pulling, any steady change is drift. *Safety:* Lift each 1.5 kg lead sphere with both hands, set it down where it can't roll off the bench, and wash your hands afterwards. Don't look into the laser beam. |

### Samples on the page

- **G 8% low, clean swing**: [`cavendish_scale_distance.csv`](../../data/seeded/cavendish_scale_distance.csv). The swing is clean and damps normally, but the shift and period give G about 8% below 6.674 × 10⁻¹¹.
- **Equilibrium creeping along the scale**: [`cavendish_drift.csv`](../../data/seeded/cavendish_drift.csv). The swing looks normal, but the level it settles to keeps moving along the scale through the whole run.
- **Healthy measurement**: [`cavendish_clean.csv`](../../data/seeded/cavendish_clean.csv). Nothing should look off: the swing settles 107 mm along the scale with a 9 minute period, giving G within its uncertainty.
- Sample result of *Measure the mirror-to-scale distance with a steel tape*: [`cavendish_scale_distance_tape.csv`](../../data/seeded/cavendish_scale_distance_tape.csv)

### The demo case

1. **G 8% low, clean swing** ([`cavendish_scale_distance.csv`](../../data/seeded/cavendish_scale_distance.csv)): the leading cause is *Mirror-to-scale distance D not what was entered* at 53%, with *Large spheres not against the case (centre distance r larger than assumed)* at 45%.
2. Recommended test: **Measure the mirror-to-scale distance with a steel tape** (3 min, 1.00 bits).
3. With its result ([`cavendish_scale_distance_tape.csv`](../../data/seeded/cavendish_scale_distance_tape.csv)): *Mirror-to-scale distance D not what was entered*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`cavendish/`](cavendish/)); each gives the result above. [Excel export](cavendish/excel_export.csv) · [Semicolons, decimal commas](cavendish/semicolon_decimal_comma.csv) · [Tab-separated](cavendish/tab_separated.tsv) · [UTF-16 "Unicode text"](cavendish/unicode_text.txt) · [Other column names](cavendish/other_column_names.csv)

## Driven damped oscillator (resonance)

Steady amplitude of a mass on a spring, driven by a motor and braked by eddy currents, against drive frequency.

| | |
| --- | --- |
| Model | `A = a ω₀² / √((ω₀² − ω²)² + (γω)²)` |
| Columns | `drive_frequency_Hz`, `amplitude_mm` (one row per reading; `#` lines are comments) |
| You enter | Natural frequency f₀ from free oscillations (Hz) (default 0.8); Damping γ from the free decay at the set current (1/s) (default 0.6); Brake magnet current set (A) (default 0.4); Amplitude reading precision (mm) (default 0.4) |
| Physics code | [`sandbox/tools/bench_mechanics.py`](../../sandbox/tools/bench_mechanics.py), fitted inside the glovebox |
| Fault library | [`faults/bench_mechanics.yaml`](../../faults/bench_mechanics.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `driven_oscillator` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Drive frequency read from the motor's dial, which is off | Motor dials are often 3–5% out (they depend on the supply and the load), which moves the whole curve along the frequency axis | Measure the drive frequency itself (time 20 crank turns, or a light gate on the crank) at every point, or correct every dial reading by the measured ratio, and refit. |
| Oscillating mass not the one f₀ was timed with (vane or slotted mass added) | f₀ ∝ 1/√m: adding 8% to the moving mass (a vane and its clamp) lowers f₀ by about 4% | Time the free oscillations again with everything that moves in place (vane, clamp, any slotted masses), enter that f₀ and the decay rate measured the same way, and compare. |
| Eddy-current brake current not the one the damping was measured at | Eddy damping goes as the current squared: 0.52 A instead of 0.40 A raises γ by about 60%, so the peak comes out lower and broader | Set the brake current on an ammeter in series with the magnet (not the supply's knob), leave it untouched through the sweep, and measure the free decay at that same current. |
| Amplitudes read before the transient had died away | The start-up motion decays as e^(−γt/2); near resonance, reading after one or two time constants leaves the amplitude 10–40% off and the points scattered | After each change of frequency wait at least five time constants (5 × 2/γ, about 17 s at γ = 0.6 /s) before reading, and reread the points near the peak. |
| Amplitude limited by an end stop at the top of the curve | Readings near resonance sit level at the stop (here the vane meeting the pole piece) while the curve through the rest rises above it | Halve the crank's throw (the curve scales with it) or move the stop out of the way, and repeat the points near resonance; until then quote f₀ and γ from the fit with the ceiling. |
| Unknown cause (none of the above fits well) |  | Check the spring isn't rubbing the guide, the vane is centred in the gap, and the crank's throw stays fixed, then repeat the sweep. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Time 20 crank turns with a stopwatch at three dial settings | 2 | At three dial settings across the sweep, time 20 turns of the motor's crank with a stopwatch and compare 20/time with what the dial says. *Safety:* Keep fingers, ties and hair clear of the motor's crank and the drive rod while it turns, and stop the motor before reaching near it. |
| Time the free oscillations with the motor stopped | 3 | Stop the motor with the crank at the middle of its throw, displace the mass by about 20 mm and time 20 free oscillations, three times, with the brake at its set current. *Safety:* Switch the motor off at its supply before touching the mass; don't stretch the spring past the end of its scale, as an overstretched spring can let the mass fall. |
| Read the brake magnet's current on a separate ammeter | 1 | Put a multimeter on its 10 A range in series with the electromagnet and take five readings with the supply as it was for the sweep. *Safety:* Turn the magnet's supply to zero before breaking its circuit; the coil is inductive and sparks if disconnected live, and its pole pieces get warm. |
| Reread the points nearest the peak after five time constants | 5 | At the four frequencies nearest the peak, read the amplitude once at the time you did before, then again after waiting at least 20 s more without touching anything. Columns drive_frequency_Hz, early_mm, settled_mm. *Safety:* Near resonance the mass moves fast and far; keep your face and hands clear of it and of the crank while you read the scale. |

### Samples on the page

- **Resonance 4% low, shape right**: [`oscillator_dial.csv`](../../data/seeded/oscillator_dial.csv). The curve has the right shape and width, but it peaks about 4% below the 0.800 Hz the free oscillations gave.
- **Top of the peak flat**: [`oscillator_end_stop.csv`](../../data/seeded/oscillator_end_stop.csv). Away from the peak the readings follow a resonance curve, but the readings around the peak are all level at about 16 mm.
- **Peak low and broad**: [`oscillator_brake.csv`](../../data/seeded/oscillator_brake.csv). The curve is a clean resonance at the right frequency, but the peak is lower and broader than the damping entered allows.
- **Healthy measurement**: [`oscillator_clean.csv`](../../data/seeded/oscillator_clean.csv). Nothing should look off: the peak sits at the free-oscillation f₀ of 0.800 Hz with γ = 0.60 /s.
- Sample result of *Time 20 crank turns with a stopwatch at three dial settings*: [`oscillator_dial_stopwatch.csv`](../../data/seeded/oscillator_dial_stopwatch.csv)

### The demo case

1. **Resonance 4% low, shape right** ([`oscillator_dial.csv`](../../data/seeded/oscillator_dial.csv)): the leading cause is *Drive frequency read from the motor's dial, which is off* at 56%, with *Oscillating mass not the one f₀ was timed with (vane or slotted mass added)* at 42%.
2. Recommended test: **Time 20 crank turns with a stopwatch at three dial settings** (2 min, 0.99 bits).
3. With its result ([`oscillator_dial_stopwatch.csv`](../../data/seeded/oscillator_dial_stopwatch.csv)): *Drive frequency read from the motor's dial, which is off*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`driven_oscillator/`](driven_oscillator/)); each gives the result above. [Excel export](driven_oscillator/excel_export.csv) · [Semicolons, decimal commas](driven_oscillator/semicolon_decimal_comma.csv) · [Tab-separated](driven_oscillator/tab_separated.tsv) · [UTF-16 "Unicode text"](driven_oscillator/unicode_text.txt) · [Other column names](driven_oscillator/other_column_names.csv)

## Boyle's law (syringe and pressure sensor)

Pressure of the air in a sealed syringe as the plunger is pushed in, with the tubing's dead volume included.

| | |
| --- | --- |
| Model | `p (V + V₀) = nRT` |
| Columns | `volume_ml`, `pressure_kPa` (one row per reading; `#` lines are comments) |
| You enter | Dead volume outside the syringe scale V₀ (ml) (default 0.5); Room pressure from the lab barometer (kPa) (default 101.3); Volume reading precision (ml) (default 0.3); Pressure reading precision (kPa) (default 0.2) |
| Physics code | [`sandbox/tools/bench_mechanics.py`](../../sandbox/tools/bench_mechanics.py), fitted inside the glovebox |
| Fault library | [`faults/bench_mechanics.yaml`](../../faults/bench_mechanics.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `boyle_gas` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Tubing volume left out of the dead volume | 40 cm of 3 mm bore tube holds 2.8 ml; left out, pV appears to fall by 8% between 60 ml and 20 ml | Add the tubing's volume (π × bore² / 4 × length) and the sensor's own to the dead volume, or shorten the tube, and refit; the readings themselves are fine. |
| Air leaking out at the plunger seal or a joint | A leak loses gas fastest at the highest pressure; losing 7% over a compression to 20 ml looks just like 2–3 ml of extra dead volume | Push the tubing fully onto the Luer fittings (a short sleeve of silicone tube helps), lightly grease the plunger seal or use a new syringe, check that the pressure holds at 20 ml, and repeat. |
| Compressed too fast, so the gas is warm when read | A quick push warms the air by several kelvin, a few per cent in p; read at once, the small volumes read high and pV appears to rise | Move the plunger slowly and wait 30 s at each volume before reading, so the gas returns to room temperature. |
| Pressure sensor zero offset | Absolute sensors drift by a few kPa between calibrations: the first reading, at room pressure, is off by the same amount as every other | Read the sensor with its port open beside the lab barometer, subtract the difference from every reading (or recalibrate the sensor), and refit. |
| Unknown cause (none of the above fits well) |  | Check the volume scale is read at the plunger seal's front edge, the sensor is set to absolute pressure, and the room temperature is steady, then repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the connecting tube's length and bore | 3 | Pull the tube off, measure its length with a rule and its bore with the inside jaws of a calliper (or from the label), four times each. *Safety:* Release the pressure (pull the tube off at atmospheric volume) before disconnecting; a syringe pushed to 20 ml holds three atmospheres and can fire the tube or plunger off. |
| Hold the plunger at 20 ml and watch the pressure for three minutes | 4 | Push to 20 ml, clamp or hold the plunger still, wait 30 s, then log the pressure every 10 s for three minutes. Columns time_s, held_pressure_kPa. *Safety:* Wear eye protection and point the syringe away from people; at three atmospheres the plunger can shoot out if your grip slips. Don't go beyond the sensor's rated pressure. |
| Reread each volume after 30 s at rest | 6 | Repeat the compression, reading the pressure as soon as the plunger stops and again after 30 s, at every volume. Columns volume_ml, pressure_at_once_kPa, pressure_after_30s_kPa. *Safety:* Wear eye protection and point the syringe away from people while it is compressed; don't exceed the sensor's rated pressure. |
| Read the sensor with its port open, beside the barometer | 1 | Disconnect the syringe so the sensor's port is open to the room, take five readings and read the lab barometer. *Safety:* Let the syringe back to its starting volume before pulling it off, so it doesn't spring back or spray anything left in the tube. |

### Samples on the page

- **pV falls as the gas is squeezed**: [`boyle_dead_volume.csv`](../../data/seeded/boyle_dead_volume.csv). The points are smooth, but p(V + V₀) falls steadily as the gas is squeezed, by about 8% at 20 ml.
- **First reading above room pressure**: [`boyle_sensor_offset.csv`](../../data/seeded/boyle_sensor_offset.csv). pV is nearly constant, but the first reading, taken with the gas at room pressure, is about 3.5 kPa above the barometer.
- **Healthy measurement**: [`boyle_clean.csv`](../../data/seeded/boyle_clean.csv). Nothing should look off: p(V + 0.5 ml) stays constant within the readings.
- Sample result of *Measure the connecting tube's length and bore*: [`boyle_dead_volume_tube.csv`](../../data/seeded/boyle_dead_volume_tube.csv)

### The demo case

1. **pV falls as the gas is squeezed** ([`boyle_dead_volume.csv`](../../data/seeded/boyle_dead_volume.csv)): the leading cause is *Tubing volume left out of the dead volume* at 53%, with *Air leaking out at the plunger seal or a joint* at 45%.
2. Recommended test: **Measure the connecting tube's length and bore** (3 min, 1.00 bits).
3. With its result ([`boyle_dead_volume_tube.csv`](../../data/seeded/boyle_dead_volume_tube.csv)): *Tubing volume left out of the dead volume*, 92%, confirmed.

### Example upload files

The headline sample saved five ways ([`boyle_gas/`](boyle_gas/)); each gives the result above. [Excel export](boyle_gas/excel_export.csv) · [Semicolons, decimal commas](boyle_gas/semicolon_decimal_comma.csv) · [Tab-separated](boyle_gas/tab_separated.tsv) · [UTF-16 "Unicode text"](boyle_gas/unicode_text.txt) · [Other column names](boyle_gas/other_column_names.csv)
