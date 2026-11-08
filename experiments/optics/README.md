# Optics

9 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Optics*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Laser and photodetector alignment](#laser-and-photodetector-alignment) | teaching lab | `V = V_d + V_p e^(−2(x−x₀)²/w²)` | Repeat the scan after the laser has warmed up for 15 minutes | [Excel](laser_alignment/excel_export.csv) · [Semicolons](laser_alignment/semicolon_decimal_comma.csv) · [Tabs](laser_alignment/tab_separated.tsv) · [UTF-16](laser_alignment/unicode_text.txt) · [Renamed](laser_alignment/other_column_names.csv) |
| [Malus's law polariser](#maluss-law-polariser) | teaching lab | `I = I₀ cos²θ` | Read the detector at the crossed position, then with the laser beam blocked | [Excel](malus/excel_export.csv) · [Semicolons](malus/semicolon_decimal_comma.csv) · [Tabs](malus/tab_separated.tsv) · [UTF-16](malus/unicode_text.txt) · [Renamed](malus/other_column_names.csv) |
| [Beer-Lambert absorption](#beer-lambert-absorption) | teaching lab | `I = I₀ e^(−αx)` | Repeat the scan with the room lights off and the lid closed | [Excel](beer_lambert/excel_export.csv) · [Semicolons](beer_lambert/semicolon_decimal_comma.csv) · [Tabs](beer_lambert/tab_separated.tsv) · [UTF-16](beer_lambert/unicode_text.txt) · [Renamed](beer_lambert/other_column_names.csv) |
| [Diffraction grating](#diffraction-grating) | teaching lab | `d sin θ = mλ` | Repeat with a source of known wavelength (HeNe 632.8 nm) | [Excel](grating/excel_export.csv) · [Semicolons](grating/semicolon_decimal_comma.csv) · [Tabs](grating/tab_separated.tsv) · [UTF-16](grating/unicode_text.txt) · [Renamed](grating/other_column_names.csv) |
| [Faraday rotation](#faraday-rotation-graduate) | graduate | `θ = V·B·L` | Map the field along the rod with the Hall probe | [Excel](faraday_rotation/excel_export.csv) · [Semicolons](faraday_rotation/semicolon_decimal_comma.csv) · [Tabs](faraday_rotation/tab_separated.tsv) · [UTF-16](faraday_rotation/unicode_text.txt) · [Renamed](faraday_rotation/other_column_names.csv) |
| [Michelson interferometer](#michelson-interferometer) | teaching lab | `N = 2d/λ` | Count the same travel again, slowly, turning one way only | [Excel](michelson/excel_export.csv) · [Semicolons](michelson/semicolon_decimal_comma.csv) · [Tabs](michelson/tab_separated.tsv) · [UTF-16](michelson/unicode_text.txt) · [Renamed](michelson/other_column_names.csv) |
| [Young's double slit](#youngs-double-slit) | teaching lab | `y_m = m λ L / d` | Measure the slit-to-screen distance again with a steel tape, from the slide itself | [Excel](young_double_slit/excel_export.csv) · [Semicolons](young_double_slit/semicolon_decimal_comma.csv) · [Tabs](young_double_slit/tab_separated.tsv) · [UTF-16](young_double_slit/unicode_text.txt) · [Renamed](young_double_slit/other_column_names.csv) |
| [Focal length of a thin lens](#focal-length-of-a-thin-lens) | teaching lab | `1/u + 1/v = 1/f` | Check the holder's index mark against the lens itself | [Excel](thin_lens/excel_export.csv) · [Semicolons](thin_lens/semicolon_decimal_comma.csv) · [Tabs](thin_lens/tab_separated.tsv) · [UTF-16](thin_lens/unicode_text.txt) · [Renamed](thin_lens/other_column_names.csv) |
| [Brewster's angle (Fresnel reflection)](#brewsters-angle-fresnel-reflection) | teaching lab | `R_p = \|r_p\|²,  tan θ_B = n` | At the minimum, turn the polariser either side of its setting | [Excel](brewster/excel_export.csv) · [Semicolons](brewster/semicolon_decimal_comma.csv) · [Tabs](brewster/tab_separated.tsv) · [UTF-16](brewster/unicode_text.txt) · [Renamed](brewster/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Laser and photodetector alignment

Detector scanned across a Gaussian beam.

| | |
| --- | --- |
| Model | `V = V_d + V_p e^(−2(x−x₀)²/w²)` |
| Columns | `position_mm`, `detector_voltage_mV` (one row per reading; `#` lines are comments) |
| You enter | Beam should be at (mm) (default 0); Expected peak (mV) (default 600); Beam radius (mm) (default 1) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `laser_alignment` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Detector or beam steering misaligned |  | Re-centre the beam on the detector with the steering mirrors, at low power and with eyewear on, then rescan. |
| Laser pointing drift during warm-up | Diode and HeNe lasers can drift tens of µrad in the first 15–30 min | Let the laser warm up for 15 to 30 minutes before scanning, and recheck the beam centre at the end of the run. |
| Low laser power or a dirty optic in the path |  | Clean or replace the dirty optic and check the output on a power meter; if the laser itself is low, report it to whoever looks after it. |
| Photodetector saturating at the beam centre |  | Add a neutral-density filter or lower the detector gain so the peak sits well below the detector's maximum, then rescan. |
| Unknown cause (none of the above fits well) |  | Re-centre the beam and detector, rescan slowly, and look at the residuals around the peak. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat the scan after the laser has warmed up for 15 minutes | 5 | Leave the laser on for 15 minutes, then scan the detector across the beam again with the same steps. *Safety:* Keep beam paths below eye level and wear the eyewear your laser safety officer specifies. |
| Measure the beam power with an optical power meter | 5 | Put a power meter right after the laser, then just before the detector, and compare with the laser's rated power. |
| Add a neutral-density filter and rescan | 5 | Put an ND1 filter in front of the detector; a saturated profile becomes Gaussian again. |

### Samples on the page

- **Peak is off-centre**: [`laser_misaligned.csv`](../../data/seeded/laser_misaligned.csv). The beam profile has the right height and width, but its peak sits about 0.85 mm off centre.
- **Peak far too low**: [`laser_low_power.csv`](../../data/seeded/laser_low_power.csv). The peak is centred and the right width, but only about 180 mV high instead of about 600 mV.
- **Well aligned**: [`laser_clean.csv`](../../data/seeded/laser_clean.csv). Nothing should look off: centred, right height and width.
- Sample result of *Repeat the scan after the laser has warmed up for 15 minutes*: [`laser_misaligned_rescan.csv`](../../data/seeded/laser_misaligned_rescan.csv)

### The demo case

1. **Peak is off-centre** ([`laser_misaligned.csv`](../../data/seeded/laser_misaligned.csv)): the leading cause is *Detector or beam steering misaligned* at 64%, with *Laser pointing drift during warm-up* at 33%.
2. Recommended test: **Repeat the scan after the laser has warmed up for 15 minutes** (5 min, 0.92 bits).
3. With its result ([`laser_misaligned_rescan.csv`](../../data/seeded/laser_misaligned_rescan.csv)): *Detector or beam steering misaligned*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`laser_alignment/`](laser_alignment/)); each gives the result above. [Excel export](laser_alignment/excel_export.csv) · [Semicolons, decimal commas](laser_alignment/semicolon_decimal_comma.csv) · [Tab-separated](laser_alignment/tab_separated.tsv) · [UTF-16 "Unicode text"](laser_alignment/unicode_text.txt) · [Other column names](laser_alignment/other_column_names.csv)

## Malus's law polariser

Transmission through two polarisers against analyser angle.

| | |
| --- | --- |
| Model | `I = I₀ cos²θ` |
| Columns | `angle_deg`, `intensity` (one row per reading; `#` lines are comments) |
| You enter | Angle of maximum (°) (default 0) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `malus` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Room light reaching the detector |  | Shield the detector from room light (lights off or a tube over the detector), or subtract the beam-blocked reading. |
| Worn or low-extinction polariser | Sheet polarisers: 100:1 to 1000:1; a worn one can drop below 20:1 | Replace the worn polariser with one of known extinction ratio and rescan. |
| Analyser scale not zeroed to the polariser axis |  | Find the transmission minimum by hand, re-zero the analyser scale 90° from it, and refit. |
| Unknown cause (none of the above fits well) |  | Rescan with fresh polarisers and the detector shielded, and compare the two scans. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the detector at the crossed position, then with the laser beam blocked | 2 | Set the analyser to the minimum, record the reading, then block the laser before the first polariser and record again. *Safety:* Block the beam with a beam block or card, never with your hand. |
| Swap in a new polariser and rescan | 5 | Replace the analyser with a fresh sheet polariser and scan 0–180° again. |
| Find the transmission minimum by hand and read the scale | 2 | Rotate the analyser slowly to the darkest point; it should read 90° if the scale is zeroed. |

### Samples on the page

- **Never goes dark**: [`malus_poor_extinction.csv`](../../data/seeded/malus_poor_extinction.csv). The cos² curve has the right shape, but it never reaches dark: at 90° about 8% of the light is still there.
- **Maximum isn't at 0°**: [`malus_angle_offset.csv`](../../data/seeded/malus_angle_offset.csv). The curve goes fully dark, but the brightest point is at about 12° instead of 0°.
- **Healthy polarisers**: [`malus_clean.csv`](../../data/seeded/malus_clean.csv). Nothing should look off: maximum at 0°, dark at 90°.
- Sample result of *Read the detector at the crossed position, then with the laser beam blocked*: [`malus_poor_extinction_blocked.csv`](../../data/seeded/malus_poor_extinction_blocked.csv)

### The demo case

1. **Never goes dark** ([`malus_poor_extinction.csv`](../../data/seeded/malus_poor_extinction.csv)): the leading cause is *Room light reaching the detector* at 58%, with *Worn or low-extinction polariser* at 41%.
2. Recommended test: **Read the detector at the crossed position, then with the laser beam blocked** (2 min, 1.07 bits).
3. With its result ([`malus_poor_extinction_blocked.csv`](../../data/seeded/malus_poor_extinction_blocked.csv)): *Room light reaching the detector*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`malus/`](malus/)); each gives the result above. [Excel export](malus/excel_export.csv) · [Semicolons, decimal commas](malus/semicolon_decimal_comma.csv) · [Tab-separated](malus/tab_separated.tsv) · [UTF-16 "Unicode text"](malus/unicode_text.txt) · [Other column names](malus/other_column_names.csv)

## Beer-Lambert absorption

Transmitted light through samples of increasing thickness.

| | |
| --- | --- |
| Model | `I = I₀ e^(−αx)` |
| Columns | `thickness_cm`, `transmitted_intensity` (one row per reading; `#` lines are comments) |
| You enter | Absorption coefficient (1/cm) (default 0.5); Unattenuated intensity (default 1) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `beer_lambert` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Room light leaking into the detector |  | Close the enclosure lid, switch off the room lights or shroud the detector, and rescan. |
| Detector dark-current or amplifier offset |  | Read the detector with the beam blocked and subtract that dark level from every point before fitting. |
| Sample concentration higher than labelled |  | Remake the solution by weighing the solute, or check it against a standard, and refit with the true concentration. |
| Cuvette path length different from assumed |  | Measure the cuvette or slab thickness with calipers and refit with the measured path length. |
| Unknown cause (none of the above fits well) |  | Rescan with a fresh sample and a reference absorbance standard, and compare the two. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat the scan with the room lights off and the lid closed | 5 | Close the sample-compartment lid, switch off the room lights, and repeat the same thicknesses. |
| Measure the cuvette or slab thickness with calipers | 3 | Check each sample's optical path length against the value used in the analysis. |
| Measure a reference absorbance standard | 10 | A certified neutral-density or holmium filter has a known absorbance; it checks the instrument, not the sample. |

### Samples on the page

- **Intensity levels off above zero**: [`beer_stray_light.csv`](../../data/seeded/beer_stray_light.csv). The curve falls off exponentially but levels out at about 12% instead of heading to zero.
- **Absorbs twice as fast as expected**: [`beer_high_alpha.csv`](../../data/seeded/beer_high_alpha.csv). The curve heads to zero, but falls about twice as fast as the expected α = 0.5 /cm.
- **Healthy absorption**: [`beer_clean.csv`](../../data/seeded/beer_clean.csv). Nothing should look off: α matches and the light heads to zero.
- Sample result of *Repeat the scan with the room lights off and the lid closed*: [`beer_stray_light_enclosed.csv`](../../data/seeded/beer_stray_light_enclosed.csv)

### The demo case

1. **Intensity levels off above zero** ([`beer_stray_light.csv`](../../data/seeded/beer_stray_light.csv)): the leading cause is *Room light leaking into the detector* at 60%, with *Detector dark-current or amplifier offset* at 38%.
2. Recommended test: **Repeat the scan with the room lights off and the lid closed** (5 min, 1.06 bits).
3. With its result ([`beer_stray_light_enclosed.csv`](../../data/seeded/beer_stray_light_enclosed.csv)): *Room light leaking into the detector*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`beer_lambert/`](beer_lambert/)); each gives the result above. [Excel export](beer_lambert/excel_export.csv) · [Semicolons, decimal commas](beer_lambert/semicolon_decimal_comma.csv) · [Tab-separated](beer_lambert/tab_separated.tsv) · [UTF-16 "Unicode text"](beer_lambert/unicode_text.txt) · [Other column names](beer_lambert/other_column_names.csv)

## Diffraction grating

Diffraction angles of a laser through a grating, orders −3 to +3.

| | |
| --- | --- |
| Model | `d sin θ = mλ` |
| Columns | `order_m`, `angle_deg` (one row per reading; `#` lines are comments) |
| You enter | Grating (lines/mm) (default 600); Laser wavelength (nm) (default 532) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `grating` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Spectrometer angle zero misread | Orders on one side read high and on the other low by the same angle | Re-zero the vernier on the straight-through beam, or average the left and right angles for each order, and refit. |
| A grating with a different line density than assumed | A 500 lines/mm grating read as 600 lines/mm makes every wavelength 17% short | Read the line density off the grating's mount, or calibrate it with a HeNe line, and refit with the right value. |
| A laser wavelength different from its label |  | Calibrate the spectrometer with a known reference line and quote the measured laser wavelength, not the label. |
| Unknown cause (none of the above fits well) |  | Repeat with a HeNe reference line, reading orders on both sides, and compare the angles. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Repeat with a source of known wavelength (HeNe 632.8 nm) | 4 | Swap in a helium-neon laser or a sodium lamp and measure orders −3 to +3 with the same grating. *Safety:* Laser changes need your laser safety officer's procedure; never view the beam directly. |
| Re-zero the spectrometer on the straight-through beam | 2 | Set the telescope on the zeroth order and read the vernier; that is your zero. |

### Samples on the page

- **Wavelength comes out 17% short**: [`grating_wrong_spec.csv`](../../data/seeded/grating_wrong_spec.csv). The pattern is symmetric, but the angles give a wavelength about 17% shorter than 532 nm.
- **Orders lopsided left to right**: [`grating_zero_offset.csv`](../../data/seeded/grating_zero_offset.csv). The wavelength is right, but every order on one side reads high and on the other side low.
- **Healthy measurement**: [`grating_clean.csv`](../../data/seeded/grating_clean.csv). Nothing should look off: wavelength matches, pattern symmetric.
- Sample result of *Repeat with a source of known wavelength (HeNe 632.8 nm)*: [`grating_wrong_spec_ref.csv`](../../data/seeded/grating_wrong_spec_ref.csv)

### The demo case

1. **Wavelength comes out 17% short** ([`grating_wrong_spec.csv`](../../data/seeded/grating_wrong_spec.csv)): the leading cause is *A grating with a different line density than assumed* at 52%, with *A laser wavelength different from its label* at 46%.
2. Recommended test: **Repeat with a source of known wavelength (HeNe 632.8 nm)** (4 min, 1.00 bits).
3. With its result ([`grating_wrong_spec_ref.csv`](../../data/seeded/grating_wrong_spec_ref.csv)): *A grating with a different line density than assumed*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`grating/`](grating/)); each gives the result above. [Excel export](grating/excel_export.csv) · [Semicolons, decimal commas](grating/semicolon_decimal_comma.csv) · [Tab-separated](grating/tab_separated.tsv) · [UTF-16 "Unicode text"](grating/unicode_text.txt) · [Other column names](grating/other_column_names.csv)

## Faraday rotation *(graduate)*

Rotation of a laser's polarisation in a glass rod against the magnetic field along it, to measure the Verdet constant.

| | |
| --- | --- |
| Model | `θ = V·B·L` |
| Columns | `field_mT`, `rotation_deg` (one row per reading; `#` lines are comments) |
| You enter | Verdet constant of the glass at your wavelength (rad/(T·m)) (default 23); Rod length L (mm) (default 100); Rotation reading precision (°) (default 0.05); Gaussmeter precision (mT) (default 0.2) |
| Physics code | [`sandbox/tools/bench_advanced.py`](../../sandbox/tools/bench_advanced.py), fitted inside the glovebox |
| Fault library | [`faults/bench_advanced.yaml`](../../faults/bench_advanced.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `faraday_rotation` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Field not uniform along the rod (rod off-centre or sticking out of the coil) | A 100 mm rod slid 5 cm along a 200 mm coil sees a field about 10% below the centre reading | Centre the rod in the coil and repeat, or use the field averaged along the rod (from the field map) in place of the centre reading, and refit. |
| Field reading high or low (Hall probe or gaussmeter calibration) | An uncalibrated Hall probe can read 5–10% off | Calibrate the gaussmeter in a reference magnet (or against a calibrated probe), rescale the field readings, and refit. |
| Analyser zero misread (extinction at zero field set wrong) | Extinction found on one side of a shallow minimum is easily 0.3–1° off | Switch the field off, find extinction again by bracketing the minimum from both sides, and subtract that angle from every reading. |
| Gaussmeter not zeroed (field reads non-zero at zero current) | A probe zeroed near the coil or in the lab's field can read a few mT at zero current | Zero the probe in its zero-gauss chamber, subtract the offset from every field reading, and refit. |
| Unknown cause (none of the above fits well) |  | Check the laser's wavelength and polarisation, and repeat a few fields in random order with the field reversed. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Map the field along the rod with the Hall probe | 4 | Hold the current at the run's top setting and step the probe through the bore in 10 mm steps from one end of the rod to the other. The field the rod sees is the average along its length. *Safety:* The coil gets hot at high current; don't touch the winding, and turn the current down before unplugging it (it is inductive and can arc). Block the laser beam while your hands are near the bore. |
| Check the gaussmeter in a reference magnet | 6 | Fetch the calibrated reference magnet (or a second, calibrated probe) and compare the gaussmeter's reading with its stated field. *Safety:* Keep the reference magnet away from watches, cards and the coil; strong magnets can pinch fingers when they snap to steel. |
| Switch the field off and find extinction again | 2 | With no current in the coil, bracket the transmission minimum by approaching it from both sides and take the midpoint. Compare it with the zero you used. *Safety:* Keep the laser beam below eye level and never look along it, even through the analyser. Follow your laser safety officer's rules for the laser's class. |
| Read the gaussmeter in its zero-gauss chamber | 2 | Put the probe in the zero-gauss chamber and read it. It should read 0.0 mT. *Safety:* The Hall probe's tip is fragile; slide it in without bending it. |

### Samples on the page

- **Verdet constant 11% low**: [`faraday_rot_nonuniform.csv`](../../data/seeded/faraday_rot_nonuniform.csv). A straight line through zero, but its slope gives a Verdet constant about 11% low.
- **Rotation not zero at zero field**: [`faraday_rot_zero_offset.csv`](../../data/seeded/faraday_rot_zero_offset.csv). The slope gives the expected Verdet constant, but the line crosses zero field at about +0.5° instead of 0°.
- **Healthy measurement**: [`faraday_rot_clean.csv`](../../data/seeded/faraday_rot_clean.csv). Nothing should look off: a straight line through zero with V = 23 rad/(T·m).
- Sample result of *Map the field along the rod with the Hall probe*: [`faraday_rot_nonuniform_map.csv`](../../data/seeded/faraday_rot_nonuniform_map.csv)

### The demo case

1. **Verdet constant 11% low** ([`faraday_rot_nonuniform.csv`](../../data/seeded/faraday_rot_nonuniform.csv)): the leading cause is *Field not uniform along the rod (rod off-centre or sticking out of the coil)* at 53%, with *Field reading high or low (Hall probe or gaussmeter calibration)* at 45%.
2. Recommended test: **Map the field along the rod with the Hall probe** (4 min, 0.99 bits).
3. With its result ([`faraday_rot_nonuniform_map.csv`](../../data/seeded/faraday_rot_nonuniform_map.csv)): *Field not uniform along the rod (rod off-centre or sticking out of the coil)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`faraday_rotation/`](faraday_rotation/)); each gives the result above. [Excel export](faraday_rotation/excel_export.csv) · [Semicolons, decimal commas](faraday_rotation/semicolon_decimal_comma.csv) · [Tab-separated](faraday_rotation/tab_separated.tsv) · [UTF-16 "Unicode text"](faraday_rotation/unicode_text.txt) · [Other column names](faraday_rotation/other_column_names.csv)

## Michelson interferometer

Fringes counted against mirror travel on the micrometer, to measure the laser wavelength.

| | |
| --- | --- |
| Model | `N = 2d/λ` |
| Columns | `micrometer_um`, `fringes` (one row per reading; `#` lines are comments) |
| You enter | Laser wavelength (nm) (default 632.8); Micrometer reading precision (µm) (default 0.2) |
| Physics code | [`sandbox/tools/bench_classical.py`](../../sandbox/tools/bench_classical.py), fitted inside the glovebox |
| Fault library | [`faults/bench_classical.yaml`](../../faults/bench_classical.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `michelson` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Fringes slipping past uncounted (turning too fast) | Missing one fringe in 30 makes the wavelength come out about 3% long | Turn the micrometer slowly enough to count every fringe (or count with a photodiode and counter), recount the travel and refit. |
| Micrometer-to-mirror lever ratio out of calibration | A lever ratio 4% off makes every wavelength 4% off, on a perfectly straight line | Calibrate the micrometer against a dial gauge (or a laser of known wavelength) and correct every reading by the measured ratio. |
| Backlash in the mirror screw (dead travel after reversing) | Winding back to the start leaves a few µm of slack: several fringes' worth of travel before the mirror moves | Turn past the starting point and come back to it in the counting direction before zeroing, so the slack is already taken up, then recount. |
| Unknown cause (none of the above fits well) |  | Check the alignment (fringes should be concentric and centred) and the mounting of the moving mirror, then repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Count the same travel again, slowly, turning one way only | 6 | Turn past the start and come back to it, zero the micrometer, then count the same 300 fringes slowly, noting the reading every 20. *Safety:* The laser is Class 2 or 3R. Never look into the direct beam or its reflections from the mirrors; watch the fringes on the screen, and keep watches and rings out of the beam. |
| Read the mirror's real travel with a dial gauge | 12 | Clamp a 1 µm dial gauge against the moving mirror's carriage and compare it with the micrometer over the same travel. *Safety:* Switch the laser off or block it at the source while you mount the gauge near the mirrors. |

### Samples on the page

- **Wavelength 3% long, line straight**: [`michelson_miscount.csv`](../../data/seeded/michelson_miscount.csv). The points lie on a straight line, but its slope gives a wavelength about 3% longer than the laser's 632.8 nm.
- **First reading off the line**: [`michelson_backlash.csv`](../../data/seeded/michelson_backlash.csv). The starting reading sits well off the line through all the others, which run parallel to the expected line.
- **Healthy measurement**: [`michelson_clean.csv`](../../data/seeded/michelson_clean.csv). Nothing should look off: the slope gives 632.8 nm.
- Sample result of *Count the same travel again, slowly, turning one way only*: [`michelson_miscount_recount.csv`](../../data/seeded/michelson_miscount_recount.csv)

### The demo case

1. **Wavelength 3% long, line straight** ([`michelson_miscount.csv`](../../data/seeded/michelson_miscount.csv)): the leading cause is *Fringes slipping past uncounted (turning too fast)* at 57%, with *Micrometer-to-mirror lever ratio out of calibration* at 41%.
2. Recommended test: **Count the same travel again, slowly, turning one way only** (6 min, 0.98 bits).
3. With its result ([`michelson_miscount_recount.csv`](../../data/seeded/michelson_miscount_recount.csv)): *Fringes slipping past uncounted (turning too fast)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`michelson/`](michelson/)); each gives the result above. [Excel export](michelson/excel_export.csv) · [Semicolons, decimal commas](michelson/semicolon_decimal_comma.csv) · [Tab-separated](michelson/tab_separated.tsv) · [UTF-16 "Unicode text"](michelson/unicode_text.txt) · [Other column names](michelson/other_column_names.csv)

## Young's double slit

Positions of the bright fringes from a laser through two slits, against fringe order, to measure the wavelength.

| | |
| --- | --- |
| Model | `y_m = m λ L / d` |
| Columns | `order_m`, `position_mm` (one row per reading; `#` lines are comments) |
| You enter | Laser wavelength (nm) (default 632.8); Slit separation d (mm) (default 0.25); Slit-to-screen distance L (m) (default 2); Fringe position reading precision (mm) (default 0.3) |
| Physics code | [`sandbox/tools/bench_fundamentals.py`](../../sandbox/tools/bench_fundamentals.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fundamentals.yaml`](../../faults/bench_fundamentals.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `young_double_slit` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Slit-to-screen distance L measured from the wrong point (the laser or the slide holder, not the slits) | Measuring L from the front of the laser, 15 cm behind the slide, makes λ come out about 7.5% low, on a perfectly straight line | Measure L with a steel tape from the slits themselves to the screen, along the beam, and refit with that distance. |
| Slit separation not the value on the slide's label | Photographic and etched slides are often 5–10% off their nominal separation, which scales λ by the same amount | Measure the slit pair's centre-to-centre separation under a travelling microscope and refit with that d. |
| Fringes past the envelope's dark band numbered wrongly (a hidden order skipped, or the dark band counted as a fringe) | With slits 0.04 mm wide and 0.25 mm apart, the 6th fringe falls in the single-slit envelope's dark band; numbering on past it one out puts every outer fringe a whole spacing off the line, on both sides | Renumber the fringes beyond the dark band (the hidden order still counts; the dark band itself doesn't), or fit only the fringes inside the central envelope. |
| Unknown cause (none of the above fits well) |  | Check that the screen is square to the beam and that every mark is the centre of a bright fringe, then repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Measure the slit-to-screen distance again with a steel tape, from the slide itself | 2 | Hook a steel tape on the slide holder level with the slits and run it to the screen along the beam; take five readings. *Safety:* Switch the laser off (or block it at the aperture) while you work next to the beam path, and keep the tape's shiny blade out of the beam. |
| Measure the slit separation under a travelling microscope | 10 | Take the slide out, focus a travelling microscope on the two slits and read the centre of each slit on the vernier, three times. *Safety:* Switch the laser off before taking the slide out; never look along the beam or into its reflection from the slide. |
| Cover one slit and count the fringes inside the central envelope | 3 | Cover one slit with card and mark where the single-slit pattern's first dark bands fall on the screen, then uncover it and count the bright fringes between those marks. *Safety:* The laser is Class 2 or 3R. Never look into the beam or its reflections; watch the pattern on the screen. |

### Samples on the page

- **Wavelength 8% low, line straight**: [`young_screen_distance.csv`](../../data/seeded/young_screen_distance.csv). The fringes lie on a good straight line, but its slope gives a wavelength about 8% below the laser's 632.8 nm.
- **Outer fringes off the line**: [`young_missing_order.csv`](../../data/seeded/young_missing_order.csv). The fringes out to the 5th lie on a line; the ones numbered 6 and 7 sit a whole spacing further out, on both sides.
- **Healthy measurement**: [`young_clean.csv`](../../data/seeded/young_clean.csv). Nothing should look off: the spacing gives 632.8 nm.
- Sample result of *Measure the slit-to-screen distance again with a steel tape, from the slide itself*: [`young_screen_distance_tape.csv`](../../data/seeded/young_screen_distance_tape.csv)

### The demo case

1. **Wavelength 8% low, line straight** ([`young_screen_distance.csv`](../../data/seeded/young_screen_distance.csv)): the leading cause is *Slit-to-screen distance L measured from the wrong point (the laser or the slide holder, not the slits)* at 53%, with *Slit separation not the value on the slide's label* at 45%.
2. Recommended test: **Measure the slit-to-screen distance again with a steel tape, from the slide itself** (2 min, 0.99 bits).
3. With its result ([`young_screen_distance_tape.csv`](../../data/seeded/young_screen_distance_tape.csv)): *Slit-to-screen distance L measured from the wrong point (the laser or the slide holder, not the slits)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`young_double_slit/`](young_double_slit/)); each gives the result above. [Excel export](young_double_slit/excel_export.csv) · [Semicolons, decimal commas](young_double_slit/semicolon_decimal_comma.csv) · [Tab-separated](young_double_slit/tab_separated.tsv) · [UTF-16 "Unicode text"](young_double_slit/unicode_text.txt) · [Other column names](young_double_slit/other_column_names.csv)

## Focal length of a thin lens

Image distance against object distance for a converging lens on an optical bench, to measure its focal length.

| | |
| --- | --- |
| Model | `1/u + 1/v = 1/f` |
| Columns | `object_distance_cm`, `image_distance_cm` (one row per reading; `#` lines are comments) |
| You enter | Focal length marked on the lens (cm) (default 10); Object distance reading precision (cm) (default 0.1); Image position precision, judging the focus (cm) (default 0.2) |
| Physics code | [`sandbox/tools/bench_optics2.py`](../../sandbox/tools/bench_optics2.py), fitted inside the glovebox |
| Fault library | [`faults/bench_optics2.yaml`](../../faults/bench_optics2.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `thin_lens` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Lens position read at the holder's index mark, which is off the lens itself | An index mark 1.2 cm from the glass makes every u 1.2 cm long and every v 1.2 cm short; the slope of 1/v against 1/u becomes about −(1 + δ/f)², −1.25 for a 10 cm lens | Read u and v from the lens's own mid-plane (or add the measured index offset to every v and take it off every u), then refit. |
| Thick or compound lens (its principal planes are not at the middle of its mount) | A 1.5 cm thick plano-convex lens has both principal planes towards its curved face, about 0.5 cm off centre on average, which tilts the line by about 10% | Use Bessel's displacement method, which needs only how far the lens moves between the two sharp images and not where its middle is, or change to a thin lens. Turning the lens round and averaging the two lines also takes out most of the tilt. |
| Image judged sharp by eye in one go (the depth of focus spreads the image distances) | With a dim image on a ground-glass screen and a 3 cm aperture, the image looks sharp over about ±8% of v: ±4 cm at v = 50 cm | For each image, move the screen in until the image just blurs and out until it blurs again, and record the midpoint; a brighter object or a darker room makes the blur easier to see. |
| Wrong lens picked up (its focal length is not the one entered) | A +8 D lens (12.5 cm) looks just like a +10 D one (10 cm): f comes out 25% long on a perfectly straight line | Check the lens's marking against the set and fetch the one you meant (or enter the focal length of the lens you used), then repeat. |
| Unknown cause (none of the above fits well) |  | Check that the object is the illuminated cross-wire itself (not the lamp's front plate), that the bench scale is continuous, and repeat a few points in random order. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Check the holder's index mark against the lens itself | 2 | Slide the holder to five places along the bench and at each read the bench scale at the holder's index mark and at the lens's own mid-plane, sighting across the glass with a set square. *Safety:* The object lamp's housing gets hot enough to burn; keep your hands clear of it while you sight across the lens. Hold lenses by their mounts, as chipped glass edges cut. |
| Turn the lens round in its holder and repeat four points | 6 | Take four object distances as in the run, then turn the lens round in the same holder and take the same four again, logging a lens_reversed column (0, then 1). A thick lens's principal planes swap sides when it is turned round; a misplaced index mark does not move. *Safety:* Let the object lamp cool, or work round it, before reaching past it to the lens holder; hold the lens by its rim, as chipped glass edges cut. |
| Focus a distant object and measure f from the lens itself | 3 | Aim the lens at a window frame or a lamp at least 5 m away, focus its image on the screen and measure from the lens's mid-plane to the screen with a ruler. Repeat five times, noting the object's distance. *Safety:* Never use the Sun as the distant object. The lens focuses it to a spot that can blind you or set the screen alight; use a window frame or a lamp across the room. |

### Samples on the page

- **Straight line, but its slope isn't −1**: [`lens_holder_edge.csv`](../../data/seeded/lens_holder_edge.csv). The points lie on a good straight line, but its slope is about −1.25 instead of −1.
- **Focal length 25% long**: [`lens_wrong_lens.csv`](../../data/seeded/lens_wrong_lens.csv). A good straight line of slope −1, but its intercepts give a focal length about 25% longer than 10 cm.
- **Points scattered about the line**: [`lens_focus_by_eye.csv`](../../data/seeded/lens_focus_by_eye.csv). The slope and focal length are about right, but the points scatter about the line far more than the precision entered.
- **Healthy measurement**: [`lens_clean.csv`](../../data/seeded/lens_clean.csv). Nothing should look off: 1/v against 1/u is a straight line of slope −1, both intercepts at 1/f = 10 m⁻¹.
- Sample result of *Check the holder's index mark against the lens itself*: [`lens_holder_edge_index.csv`](../../data/seeded/lens_holder_edge_index.csv)

### The demo case

1. **Straight line, but its slope isn't −1** ([`lens_holder_edge.csv`](../../data/seeded/lens_holder_edge.csv)): the leading cause is *Lens position read at the holder's index mark, which is off the lens itself* at 56%, with *Thick or compound lens (its principal planes are not at the middle of its mount)* at 42%.
2. Recommended test: **Check the holder's index mark against the lens itself** (2 min, 0.99 bits).
3. With its result ([`lens_holder_edge_index.csv`](../../data/seeded/lens_holder_edge_index.csv)): *Lens position read at the holder's index mark, which is off the lens itself*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`thin_lens/`](thin_lens/)); each gives the result above. [Excel export](thin_lens/excel_export.csv) · [Semicolons, decimal commas](thin_lens/semicolon_decimal_comma.csv) · [Tab-separated](thin_lens/tab_separated.tsv) · [UTF-16 "Unicode text"](thin_lens/unicode_text.txt) · [Other column names](thin_lens/other_column_names.csv)

## Brewster's angle (Fresnel reflection)

Power of p-polarised laser light reflected from a glass plate against the angle of incidence, to find Brewster's angle and the glass's refractive index.

| | |
| --- | --- |
| Model | `R_p = \|r_p\|²,  tan θ_B = n` |
| Columns | `incidence_angle_deg`, `reflected_power_uW` (one row per reading; `#` lines are comments) |
| You enter | Refractive index of the glass at the laser's wavelength (default 1.515); Incident power, measured with the same meter (µW) (default 1000); Power reading precision, absolute (µW) (default 0.1); Power reading precision, relative (%) (default 1); Angle reading precision (°) (default 0.2) |
| Physics code | [`sandbox/tools/bench_optics2.py`](../../sandbox/tools/bench_optics2.py), fitted inside the glovebox |
| Fault library | [`faults/bench_optics2.yaml`](../../faults/bench_optics2.yaml) |
| Evaluation | 5 seeded cases in `data/manifest*` |
| Key | `brewster` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Polariser not set exactly for p (some s-polarised light in the beam) | A polariser 5° off p lets sin²5° = 0.8% of the light through as s, which reflects 15% at Brewster's angle: about 1.2 µW of a 1 mW beam where there should be almost none | At Brewster's angle, turn the polariser for the deepest minimum and lock it there (that is exact p), then repeat the sweep. |
| Polariser's extinction too poor (it passes some of the crossed polarisation) | An old or heat-faded sheet polariser can pass 1% of the crossed polarisation: about 1.5 µW at the minimum from a 1 mW beam, whichever way it is turned | Replace the sheet with a better polariser (a Glan–Taylor or Glan–Thompson prism, or a fresh high-extinction sheet) and repeat the sweep. |
| Rotation stage's zero not at normal incidence (every angle offset) | A stage zeroed by eye against the plate's edge is easily 1–3° out; 2° puts Brewster's angle at 58.6° and makes tan θ_B 1.64 instead of 1.515 | Find normal incidence by sending the front-face reflection straight back into the laser's exit aperture, take that reading as zero, and subtract it from every angle. |
| Glass not the type entered (its refractive index differs) | Flint (n ≈ 1.62) and crown (n ≈ 1.515) plates look alike; flint puts Brewster's angle 1.7° higher and reflects about a third more near normal incidence | Identify the glass (its label, or n measured by refraction through the plate) and enter its refractive index at the laser's wavelength. |
| Back-face reflection reaching the detector too (a second spot beside the first) | With the iris open, the spot from the plate's back face nearly doubles the reflected power at small angles; at Brewster's angle both vanish, so the minimum stays put | Close the iris in front of the detector round the front-face spot only (or use a thicker block, or a wedge, so the second spot lands well clear), then repeat. |
| Detector saturating at the brightest angles | A photodiode on too high a gain, or with too large a load resistor, reads the bright grazing-incidence beam low: 280 µW instead of 490 µW at 85° | Put a calibrated ND filter in front of the detector (or turn its gain down) for the bright angles, correct by the filter's measured transmission, and refit. |
| Reflected beam walking off the detector at large angles (plate's face off the stage's axis) | A plate face 2–3 mm off the rotation axis moves the reflected beam by up to twice that near grazing incidence, partly off a 10 mm photodiode | Move the plate so its front face sits on the stage's rotation axis (the spot then stays put on the detector as the stage turns), then repeat the large angles. |
| Unknown cause (none of the above fits well) |  | Check the incident power again with the same meter, look at the reflected spot on a card at each angle, and repeat the sweep in the opposite direction. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| At the minimum, turn the polariser either side of its setting | 3 | Leave the stage at the angle of the minimum and turn the polariser from −10° to +10° about its setting in 2° steps, reading the reflected power at each. Exact p gives the deepest minimum. *Safety:* The laser is Class 2 or 3R. Keep the beam below eye level, never look into the direct beam or its reflections off the plate, and take off watches and rings before working near it. |
| Check the polariser's extinction with a second polariser | 5 | Put a good analyser (a Glan–Taylor prism if you have one) after the polariser, read the power with it parallel, then turn it for the darkest reading. Take five readings each way, logging analyser_crossed (0, then 1). *Safety:* The laser is Class 2 or 3R; never look into the direct beam, and block it at the laser while you place the analyser. Hold prisms and polariser sheets by their mounts, as their edges are sharp. |
| Find normal incidence by sending the reflection back into the laser | 2 | Turn the stage until the reflection from the plate's front face goes straight back into the laser's exit aperture (watch the spot on a card with a hole for the beam) and read the stage. Repeat five times. *Safety:* This sends the reflection back along the beam towards you as well as the laser. Watch it on a card held beside the aperture, never by eye, and keep your head above beam height. |
| Repeat a faint and the brightest angles with an ND filter in front of the detector | 5 | At 30° and at 75°, 80° and 85°, read the power without and then with an ND 1.0 filter in front of the detector, logging nd_filter (0, then 1). A linear detector gives the same ratio at every angle; the faint angle calibrates the filter. *Safety:* The laser is Class 2 or 3R. Near grazing incidence the reflection leaves the plate almost along the bench, so keep your eyes above beam height and block stray reflections with a card. |
| Close the iris round the main spot and repeat three small angles | 3 | At 20°, 30° and 40°, read the power with the iris open, then closed down round the front-face spot only (check on a card that the second, fainter spot is blocked), logging iris_closed (0, then 1). *Safety:* The laser is Class 2 or 3R; never look into the direct beam or along the reflected one, and keep watches and rings out of the beam while you adjust the iris. |

### Samples on the page

- **Minimum doesn't reach zero**: [`brewster_polariser.csv`](../../data/seeded/brewster_polariser.csv). The minimum is at 56.6° as expected, but it bottoms out at about 1.2 µW instead of almost nothing.
- **Minimum 2° too high**: [`brewster_stage_zero.csv`](../../data/seeded/brewster_stage_zero.csv). The curve has the expected shape and depth, but its minimum is near 58.6°, which would make n = tan θ_B about 1.64.
- **Nearly twice the reflection expected**: [`brewster_ghost.csv`](../../data/seeded/brewster_ghost.csv). The minimum is at 56.6° and reaches almost nothing, but away from it the reflected power is well above Fresnel's equations, nearly twice at small angles.
- **Healthy measurement**: [`brewster_clean.csv`](../../data/seeded/brewster_clean.csv). Nothing should look off: the reflected power follows Fresnel's equations and falls to almost nothing at Brewster's angle, 56.6°.
- Sample result of *At the minimum, turn the polariser either side of its setting*: [`brewster_polariser_rotate.csv`](../../data/seeded/brewster_polariser_rotate.csv)

### The demo case

1. **Minimum doesn't reach zero** ([`brewster_polariser.csv`](../../data/seeded/brewster_polariser.csv)): the leading cause is *Polariser not set exactly for p (some s-polarised light in the beam)* at 56%, with *Polariser's extinction too poor (it passes some of the crossed polarisation)* at 42%.
2. Recommended test: **At the minimum, turn the polariser either side of its setting** (3 min, 1.06 bits).
3. With its result ([`brewster_polariser_rotate.csv`](../../data/seeded/brewster_polariser_rotate.csv)): *Polariser not set exactly for p (some s-polarised light in the beam)*, 94%, confirmed.

### Example upload files

The headline sample saved five ways ([`brewster/`](brewster/)); each gives the result above. [Excel export](brewster/excel_export.csv) · [Semicolons, decimal commas](brewster/semicolon_decimal_comma.csv) · [Tab-separated](brewster/tab_separated.tsv) · [UTF-16 "Unicode text"](brewster/unicode_text.txt) · [Other column names](brewster/other_column_names.csv)
