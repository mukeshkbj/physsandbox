# Optics: example upload files

9 experiments. Each folder holds that experiment's headline sample saved five ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file gives the result listed for its experiment; *Other column names* does once you match its columns on the page.

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

[All areas](../README.md)

## Laser and photodetector alignment

`laser_alignment` · model `V = V_d + V_p e^(−2(x−x₀)²/w²)` · columns `position_mm`, `detector_voltage_mV`

Made from the sample **Peak is off-centre** ([`data/seeded/laser_misaligned.csv`](../../data/seeded/laser_misaligned.csv)).

- *The bench:* Photodetector scanned across a laser beam (1 mm radius) from −3 to +3 mm in 0.25 mm steps.
- *What looks off:* The beam profile has the right height and width, but its peak sits about 0.85 mm off centre.

**Expected result:** Detector or beam steering misaligned, 64% as the leading cause (with the page's defaults: Beam should be at (mm) = 0; Expected peak (mV) = 600; Beam radius (mm) = 1).

Files: [Excel export](laser_alignment/excel_export.csv) · [Semicolons, decimal commas](laser_alignment/semicolon_decimal_comma.csv) · [Tab-separated](laser_alignment/tab_separated.tsv) · [UTF-16 "Unicode text"](laser_alignment/unicode_text.txt) · [Other column names](laser_alignment/other_column_names.csv)

## Malus's law polariser

`malus` · model `I = I₀ cos²θ` · columns `angle_deg`, `intensity`

Made from the sample **Never goes dark** ([`data/seeded/malus_poor_extinction.csv`](../../data/seeded/malus_poor_extinction.csv)).

- *The bench:* Light through two polarisers as the analyser turns from 0° to 180° in 10° steps.
- *What looks off:* The cos² curve has the right shape, but it never reaches dark: at 90° about 8% of the light is still there.

**Expected result:** Room light reaching the detector, 58% as the leading cause (with the page's defaults: Angle of maximum (°) = 0).

Files: [Excel export](malus/excel_export.csv) · [Semicolons, decimal commas](malus/semicolon_decimal_comma.csv) · [Tab-separated](malus/tab_separated.tsv) · [UTF-16 "Unicode text"](malus/unicode_text.txt) · [Other column names](malus/other_column_names.csv)

## Beer-Lambert absorption

`beer_lambert` · model `I = I₀ e^(−αx)` · columns `thickness_cm`, `transmitted_intensity`

Made from the sample **Intensity levels off above zero** ([`data/seeded/beer_stray_light.csv`](../../data/seeded/beer_stray_light.csv)).

- *The bench:* Transmitted intensity through 0–5 cm of absorber in 0.5 cm steps.
- *What looks off:* The curve falls off exponentially but levels out at about 12% instead of heading to zero.

**Expected result:** Room light leaking into the detector, 60% as the leading cause (with the page's defaults: Absorption coefficient (1/cm) = 0.5; Unattenuated intensity = 1).

Files: [Excel export](beer_lambert/excel_export.csv) · [Semicolons, decimal commas](beer_lambert/semicolon_decimal_comma.csv) · [Tab-separated](beer_lambert/tab_separated.tsv) · [UTF-16 "Unicode text"](beer_lambert/unicode_text.txt) · [Other column names](beer_lambert/other_column_names.csv)

## Diffraction grating

`grating` · model `d sin θ = mλ` · columns `order_m`, `angle_deg`

Made from the sample **Wavelength comes out 17% short** ([`data/seeded/grating_wrong_spec.csv`](../../data/seeded/grating_wrong_spec.csv)).

- *The bench:* Diffraction angles of a 532 nm green laser through a grating labelled 600 lines/mm, orders −3 to +3.
- *What looks off:* The pattern is symmetric, but the angles give a wavelength about 17% shorter than 532 nm.

**Expected result:** A grating with a different line density than assumed, 52% as the leading cause (with the page's defaults: Grating (lines/mm) = 600; Laser wavelength (nm) = 532).

Files: [Excel export](grating/excel_export.csv) · [Semicolons, decimal commas](grating/semicolon_decimal_comma.csv) · [Tab-separated](grating/tab_separated.tsv) · [UTF-16 "Unicode text"](grating/unicode_text.txt) · [Other column names](grating/other_column_names.csv)

## Faraday rotation

`faraday_rotation` · graduate · model `θ = V·B·L` · columns `field_mT`, `rotation_deg`

Made from the sample **Verdet constant 11% low** ([`data/seeded/faraday_rot_nonuniform.csv`](../../data/seeded/faraday_rot_nonuniform.csv)).

- *The bench:* The same rod, coil, laser and probe.
- *What looks off:* A straight line through zero, but its slope gives a Verdet constant about 11% low.

**Expected result:** Field not uniform along the rod (rod off-centre or sticking out of the coil), 53% as the leading cause (with the page's defaults: Verdet constant of the glass at your wavelength (rad/(T·m)) = 23; Rod length L (mm) = 100; Rotation reading precision (°) = 0.05; Gaussmeter precision (mT) = 0.2).

Files: [Excel export](faraday_rotation/excel_export.csv) · [Semicolons, decimal commas](faraday_rotation/semicolon_decimal_comma.csv) · [Tab-separated](faraday_rotation/tab_separated.tsv) · [UTF-16 "Unicode text"](faraday_rotation/unicode_text.txt) · [Other column names](faraday_rotation/other_column_names.csv)

## Michelson interferometer

`michelson` · model `N = 2d/λ` · columns `micrometer_um`, `fringes`

Made from the sample **Wavelength 3% long, line straight** ([`data/seeded/michelson_miscount.csv`](../../data/seeded/michelson_miscount.csv)).

- *The bench:* The same interferometer, counting 300 fringes and noting the reading every 20.
- *What looks off:* The points lie on a straight line, but its slope gives a wavelength about 3% longer than the laser's 632.8 nm.

**Expected result:** Fringes slipping past uncounted (turning too fast), 57% as the leading cause (with the page's defaults: Laser wavelength (nm) = 632.8; Micrometer reading precision (µm) = 0.2).

Files: [Excel export](michelson/excel_export.csv) · [Semicolons, decimal commas](michelson/semicolon_decimal_comma.csv) · [Tab-separated](michelson/tab_separated.tsv) · [UTF-16 "Unicode text"](michelson/unicode_text.txt) · [Other column names](michelson/other_column_names.csv)

## Young's double slit

`young_double_slit` · model `y_m = m λ L / d` · columns `order_m`, `position_mm`

Made from the sample **Wavelength 8% low, line straight** ([`data/seeded/young_screen_distance.csv`](../../data/seeded/young_screen_distance.csv)).

- *The bench:* The same laser and slide, orders −5 to +5, with L entered as 2.000 m.
- *What looks off:* The fringes lie on a good straight line, but its slope gives a wavelength about 8% below the laser's 632.8 nm.

**Expected result:** Slit-to-screen distance L measured from the wrong point (the laser or the slide holder, not the slits), 53% as the leading cause (with the page's defaults: Laser wavelength (nm) = 632.8; Slit separation d (mm) = 0.25; Slit-to-screen distance L (m) = 2; Fringe position reading precision (mm) = 0.3).

Files: [Excel export](young_double_slit/excel_export.csv) · [Semicolons, decimal commas](young_double_slit/semicolon_decimal_comma.csv) · [Tab-separated](young_double_slit/tab_separated.tsv) · [UTF-16 "Unicode text"](young_double_slit/unicode_text.txt) · [Other column names](young_double_slit/other_column_names.csv)

## Focal length of a thin lens

`thin_lens` · model `1/u + 1/v = 1/f` · columns `object_distance_cm`, `image_distance_cm`

Made from the sample **Straight line, but its slope isn't −1** ([`data/seeded/lens_holder_edge.csv`](../../data/seeded/lens_holder_edge.csv)).

- *The bench:* The same lens, bench and screen, u read at the lens holder's index mark.
- *What looks off:* The points lie on a good straight line, but its slope is about −1.25 instead of −1.

**Expected result:** Lens position read at the holder's index mark, which is off the lens itself, 56% as the leading cause (with the page's defaults: Focal length marked on the lens (cm) = 10; Object distance reading precision (cm) = 0.1; Image position precision, judging the focus (cm) = 0.2).

Files: [Excel export](thin_lens/excel_export.csv) · [Semicolons, decimal commas](thin_lens/semicolon_decimal_comma.csv) · [Tab-separated](thin_lens/tab_separated.tsv) · [UTF-16 "Unicode text"](thin_lens/unicode_text.txt) · [Other column names](thin_lens/other_column_names.csv)

## Brewster's angle (Fresnel reflection)

`brewster` · model `R_p = |r_p|²,  tan θ_B = n` · columns `incidence_angle_deg`, `reflected_power_uW`

Made from the sample **Minimum doesn't reach zero** ([`data/seeded/brewster_polariser.csv`](../../data/seeded/brewster_polariser.csv)).

- *The bench:* The same laser, polariser, plate and detector.
- *What looks off:* The minimum is at 56.6° as expected, but it bottoms out at about 1.2 µW instead of almost nothing.

**Expected result:** Polariser not set exactly for p (some s-polarised light in the beam), 56% as the leading cause (with the page's defaults: Refractive index of the glass at the laser's wavelength = 1.515; Incident power, measured with the same meter (µW) = 1000; Power reading precision, absolute (µW) = 0.1; Power reading precision, relative (%) = 1; Angle reading precision (°) = 0.2).

Files: [Excel export](brewster/excel_export.csv) · [Semicolons, decimal commas](brewster/semicolon_decimal_comma.csv) · [Tab-separated](brewster/tab_separated.tsv) · [UTF-16 "Unicode text"](brewster/unicode_text.txt) · [Other column names](brewster/other_column_names.csv)
