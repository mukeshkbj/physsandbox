# Example upload files

Every experiment's headline measurement (51 experiments in 10 areas of physics), saved the ways real files arrive. Upload any of them on the [live demo](https://192-248-159-149.sslip.io/), or pick them on the page under the samples (*Same measurement, other file formats*). Every file except *Other column names* gives exactly the sample's result, and that one does once you match its columns on the page.

Made by [`data/make_examples.py`](../data/make_examples.py) from `data/seeded/`; [`eval/check_parsing.py`](../eval/check_parsing.py) checks that every file gives the sample's result.

## The five formats

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## By area

| Area | Experiments |
| --- | --- |
| [Electricity](electricity/README.md) | Low-resistance measurement, RC charging curve, Diode I–V curve, Series RLC resonance |
| [Signals](signals/README.md) | Oscilloscope trace |
| [Magnetism](magnetism/README.md) | Helmholtz coil calibration, Faraday's law of induction, Hall effect, Magnetic hysteresis (B–H loop), e/m of the electron (fine-beam tube), Electron spin resonance (DPPH), Pulsed NMR spin echo |
| [Optics](optics/README.md) | Laser and photodetector alignment, Malus's law polariser, Beer-Lambert absorption, Diffraction grating, Faraday rotation, Michelson interferometer, Young's double slit, Focal length of a thin lens, Brewster's angle (Fresnel reflection) |
| [Heat](heat/README.md) | Newton's law of cooling, Stefan–Boltzmann law (lamp filament), Thermal conductivity (Lee's disc), Thermocouple calibration (type K) |
| [Mechanics](mechanics/README.md) | Simple pendulum, Hooke's law spring, Viscosity by Stokes' law (falling ball), Kater's reversible pendulum, Cavendish torsion balance, Driven damped oscillator (resonance), Boyle's law (syringe and pressure sensor) |
| [Waves & sound](waves/README.md) | Speed of sound (resonance tube) |
| [Quantum](quantum/README.md) | Electron diffraction (de Broglie), Zeeman effect (cadmium red line), Millikan oil drop, Photoelectric effect (h/e), Franck–Hertz experiment (mercury), Optical pumping of rubidium, Planck's constant from LEDs, Quantum tunnelling simulation, Blackbody radiation, Atomic spectral lines (hydrogen) |
| [Nuclear & particle](nuclear/README.md) | Gamma-ray attenuation in lead, Muon lifetime, Radioactive decay (Geiger–Müller), Rutherford scattering (alphas on gold), Compton scattering |
| [Condensed matter](condensed/README.md) | X-ray Bragg diffraction (NaCl), Superconducting transition, Band gap of germanium |
