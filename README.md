# PhysSandbox

**A glovebox for AI-written science code.**

Chemists handle hazardous material through a glovebox: they can work on it, but it can never touch them. PhysSandbox does the same for the code an AI writes about your experiment. Every calculation, including code a model wrote after reading your file, runs in a sealed gVisor box with no network that is destroyed after each job, and every job leaves a signed receipt of the walls it actually had, measured from inside the box and checked again by the host.

What runs inside the glovebox is a physics troubleshooter. Upload a measurement from any of 51 bench experiments, first-year to graduate level, that came out wrong; PhysSandbox finds the likely cause and tells you which bench test to run next.

Built for the **Vultr Agent Rush Hackathon** (lablab.ai), Challenge 1: *Blast Radius Zero*.

**Live demo:** [192-248-159-149.sslip.io](https://192-248-159-149.sslip.io/) — press *Take the 90-second tour*. Running on a Vultr Cloud Compute VM with gVisor and Vultr Serverless Inference.

## Why it matters

- In physics teaching labs, "nothing works the first time": 14 of 20 electronics lab instructors interviewed said so in effect ([Dounas-Frazer & Lewandowski](https://arxiv.org/pdf/1606.05389)). In quantum-optics teaching labs, alignment can take weeks before any signal appears ([Borish & Lewandowski 2023](https://arxiv.org/pdf/2211.09595)).
- Researchers already paste data into chatbots, but a chatbot can't run physics, and unpublished data shouldn't leave the lab. Uploaded files can also carry instructions aimed at the AI (prompt injection).
- No product we found diagnoses why a physics bench measurement is off. AI-for-science money is going to discovery labs, and instrument copilots answer questions about the tool, not the experiment.

## Who pays

- **First buyer: university physics departments**, for their teaching labs. One department licence covers every bench and every student. The anchor is lab-teaching software such as Labster, from $5,000 a year per institution ([Labster](https://www.labster.com/platform-overview)). Our pricing is a hypothesis to test with instructors, not a validated number.
- **Why containment is what they pay for:** university guidance tells researchers not to put unpublished or confidential research data into generative AI tools (for example [Michigan State University](https://tech.msu.edu/news/2023/08/new-university-guidance-on-generative-ai-use) and the [University of Rochester](https://www.rochester.edu/university-research/updated-advisory-guidance-on-the-use-of-generative-ai-in-research)). The same applies to teaching labs: a student's lab data and write-up are coursework the university must protect as a student record (FERPA in the US, GDPR in the UK and EU), and the graduate advanced-lab and research-bench experiments here (NMR, superconductors, Compton, muon lifetime) produce unpublished data. A glovebox with no network, run in the department's own cloud account, plus a signed record of every job, is what lets a department say yes to AI in the lab at all. The troubleshooting is what students and instructors see: fewer "it doesn't work" queues and practice in the expert habit of predict, measure, compare and test.
- **Next: R&D test benches.** In a vendor-sponsored survey of 305 R&D engineers, 97% reported project delays from test-equipment problems, with misconfiguration and lost calibration the leading causes ([Microwave Journal](https://microwavejournal.com/articles/34478-keysight-survey-reveals-true-cost-delay-from-test-equipment-misconfiguration-maintenance-and-training-issues)).
- **Your own files, not just ours.** Upload any CSV: if its columns have other names (`Current (A)`, `V_mV`), the page asks which is which and renames the header in the browser; the numbers are sent exactly as recorded.
- **The platform underneath is not physics-specific.** The glovebox, receipts and signed notebook work for any AI-written science code; each new field is a fault library and a set of analyses (YAML plus Python).

## The experiment bench

51 real teaching-lab and research-bench experiments across 10 areas of physics, from first-year labs to graduate advanced labs. Each has its own physics model (fitted inside the glovebox), a fault library of the things that really go wrong on that bench with a concrete fix for each, and bench tests chosen by information per minute. Every demo case is built so the first measurement is genuinely ambiguous between two causes, and one quick bench test tells them apart.

<!-- bench:start -->

Each area has its own folder and README in [`experiments/`](experiments/README.md) with every experiment in full: the model and columns, the faults it tells apart with a fix for each, the bench tests it can recommend, the samples, and the demo case run end to end. The example files are that experiment's headline sample in five real-world formats (Excel export, semicolons with decimal commas, tab-separated, UTF-16 "Unicode text", renamed columns); each gives the same result.

### [Electricity](experiments/electricity/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Low-resistance measurement](experiments/electricity/README.md#low-resistance-measurement) | `V = I·R` | Read the voltmeter at zero current, leads on the sample, then shorted at the meter | [folder](experiments/electricity/resistance_4wire/): [Excel](experiments/electricity/resistance_4wire/excel_export.csv) · [Semicolons](experiments/electricity/resistance_4wire/semicolon_decimal_comma.csv) · [Tabs](experiments/electricity/resistance_4wire/tab_separated.tsv) · [UTF-16](experiments/electricity/resistance_4wire/unicode_text.txt) · [Renamed](experiments/electricity/resistance_4wire/other_column_names.csv) |
| [RC charging curve](experiments/electricity/README.md#rc-charging-curve) | `V = V₀(1 − e^(−t/RC))` | Repeat the measurement with a x10 (10 MΩ) probe | [folder](experiments/electricity/rc_charging/): [Excel](experiments/electricity/rc_charging/excel_export.csv) · [Semicolons](experiments/electricity/rc_charging/semicolon_decimal_comma.csv) · [Tabs](experiments/electricity/rc_charging/tab_separated.tsv) · [UTF-16](experiments/electricity/rc_charging/unicode_text.txt) · [Renamed](experiments/electricity/rc_charging/other_column_names.csv) |
| [Diode I–V curve](experiments/electricity/README.md#diode-iv-curve) | `V = nV_T ln(I/I_s) + I·R_s` | Move the voltmeter leads onto the diode's own legs | [folder](experiments/electricity/diode/): [Excel](experiments/electricity/diode/excel_export.csv) · [Semicolons](experiments/electricity/diode/semicolon_decimal_comma.csv) · [Tabs](experiments/electricity/diode/tab_separated.tsv) · [UTF-16](experiments/electricity/diode/unicode_text.txt) · [Renamed](experiments/electricity/diode/other_column_names.csv) |
| [Series RLC resonance](experiments/electricity/README.md#series-rlc-resonance) | `V_R = V R / √((R + R_L)² + (ωL − 1/ωC)²)` | Watch the circuit's input on CH1 through the sweep | [folder](experiments/electricity/rlc_resonance/): [Excel](experiments/electricity/rlc_resonance/excel_export.csv) · [Semicolons](experiments/electricity/rlc_resonance/semicolon_decimal_comma.csv) · [Tabs](experiments/electricity/rlc_resonance/tab_separated.tsv) · [UTF-16](experiments/electricity/rlc_resonance/unicode_text.txt) · [Renamed](experiments/electricity/rlc_resonance/other_column_names.csv) |

### [Signals](experiments/signals/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Oscilloscope trace](experiments/signals/README.md#oscilloscope-trace) | `spectrum of V(t)` | Connect all instruments to one ground point and re-record | [folder](experiments/signals/waveform/): [Excel](experiments/signals/waveform/excel_export.csv) · [Semicolons](experiments/signals/waveform/semicolon_decimal_comma.csv) · [Tabs](experiments/signals/waveform/tab_separated.tsv) · [UTF-16](experiments/signals/waveform/unicode_text.txt) · [Renamed](experiments/signals/waveform/other_column_names.csv) |

### [Magnetism](experiments/magnetism/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Helmholtz coil calibration](experiments/magnetism/README.md#helmholtz-coil-calibration) | `B = (4/5)^(3/2) μ₀NI/R` | Read the probe at zero current, in the open and inside a zero-gauss chamber | [folder](experiments/magnetism/helmholtz/): [Excel](experiments/magnetism/helmholtz/excel_export.csv) · [Semicolons](experiments/magnetism/helmholtz/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/helmholtz/tab_separated.tsv) · [UTF-16](experiments/magnetism/helmholtz/unicode_text.txt) · [Renamed](experiments/magnetism/helmholtz/other_column_names.csv) |
| [Faraday's law of induction](experiments/magnetism/README.md#faradays-law-of-induction) | `ε = −N dΦ/dt` | Hold the magnet still, then short the amplifier input | [folder](experiments/magnetism/faraday/): [Excel](experiments/magnetism/faraday/excel_export.csv) · [Semicolons](experiments/magnetism/faraday/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/faraday/tab_separated.tsv) · [UTF-16](experiments/magnetism/faraday/unicode_text.txt) · [Renamed](experiments/magnetism/faraday/other_column_names.csv) |
| [Hall effect](experiments/magnetism/README.md#hall-effect) | `V_H = IB / (n e t)` | Repeat with the magnetic field reversed | [folder](experiments/magnetism/hall/): [Excel](experiments/magnetism/hall/excel_export.csv) · [Semicolons](experiments/magnetism/hall/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/hall/tab_separated.tsv) · [UTF-16](experiments/magnetism/hall/unicode_text.txt) · [Renamed](experiments/magnetism/hall/other_column_names.csv) |
| [Magnetic hysteresis (B–H loop)](experiments/magnetism/README.md#magnetic-hysteresis-bh-loop) | `H = N₁I/ℓ,  B = Φ/(N₂A)` | Compare the search coil with a freshly wound 10-turn coil | [folder](experiments/magnetism/hysteresis/): [Excel](experiments/magnetism/hysteresis/excel_export.csv) · [Semicolons](experiments/magnetism/hysteresis/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/hysteresis/tab_separated.tsv) · [UTF-16](experiments/magnetism/hysteresis/unicode_text.txt) · [Renamed](experiments/magnetism/hysteresis/other_column_names.csv) |
| [e/m of the electron (fine-beam tube)](experiments/magnetism/README.md#em-of-the-electron-fine-beam-tube) | `e/m = 2V/(B r)²,  B = (4/5)^(3/2) μ₀NI/R` | Re-read the diameters on a mirror scale | [folder](experiments/magnetism/e_over_m/): [Excel](experiments/magnetism/e_over_m/excel_export.csv) · [Semicolons](experiments/magnetism/e_over_m/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/e_over_m/tab_separated.tsv) · [UTF-16](experiments/magnetism/e_over_m/unicode_text.txt) · [Renamed](experiments/magnetism/e_over_m/other_column_names.csv) |
| [Electron spin resonance (DPPH)](experiments/magnetism/README.md#electron-spin-resonance-dpph-graduate) *(graduate)* | `h f = g μ_B B` | Reverse the field and read the resonances again | [folder](experiments/magnetism/esr/): [Excel](experiments/magnetism/esr/excel_export.csv) · [Semicolons](experiments/magnetism/esr/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/esr/tab_separated.tsv) · [UTF-16](experiments/magnetism/esr/unicode_text.txt) · [Renamed](experiments/magnetism/esr/other_column_names.csv) |
| [Pulsed NMR spin echo](experiments/magnetism/README.md#pulsed-nmr-spin-echo-graduate) *(graduate)* | `A(2τ) = A₀ e^(−2τ/T₂)` | Run a nutation sweep (FID amplitude against pulse length) | [folder](experiments/magnetism/nmr_echo/): [Excel](experiments/magnetism/nmr_echo/excel_export.csv) · [Semicolons](experiments/magnetism/nmr_echo/semicolon_decimal_comma.csv) · [Tabs](experiments/magnetism/nmr_echo/tab_separated.tsv) · [UTF-16](experiments/magnetism/nmr_echo/unicode_text.txt) · [Renamed](experiments/magnetism/nmr_echo/other_column_names.csv) |

### [Optics](experiments/optics/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Laser and photodetector alignment](experiments/optics/README.md#laser-and-photodetector-alignment) | `V = V_d + V_p e^(−2(x−x₀)²/w²)` | Repeat the scan after the laser has warmed up for 15 minutes | [folder](experiments/optics/laser_alignment/): [Excel](experiments/optics/laser_alignment/excel_export.csv) · [Semicolons](experiments/optics/laser_alignment/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/laser_alignment/tab_separated.tsv) · [UTF-16](experiments/optics/laser_alignment/unicode_text.txt) · [Renamed](experiments/optics/laser_alignment/other_column_names.csv) |
| [Malus's law polariser](experiments/optics/README.md#maluss-law-polariser) | `I = I₀ cos²θ` | Read the detector at the crossed position, then with the laser beam blocked | [folder](experiments/optics/malus/): [Excel](experiments/optics/malus/excel_export.csv) · [Semicolons](experiments/optics/malus/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/malus/tab_separated.tsv) · [UTF-16](experiments/optics/malus/unicode_text.txt) · [Renamed](experiments/optics/malus/other_column_names.csv) |
| [Beer-Lambert absorption](experiments/optics/README.md#beer-lambert-absorption) | `I = I₀ e^(−αx)` | Repeat the scan with the room lights off and the lid closed | [folder](experiments/optics/beer_lambert/): [Excel](experiments/optics/beer_lambert/excel_export.csv) · [Semicolons](experiments/optics/beer_lambert/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/beer_lambert/tab_separated.tsv) · [UTF-16](experiments/optics/beer_lambert/unicode_text.txt) · [Renamed](experiments/optics/beer_lambert/other_column_names.csv) |
| [Diffraction grating](experiments/optics/README.md#diffraction-grating) | `d sin θ = mλ` | Repeat with a source of known wavelength (HeNe 632.8 nm) | [folder](experiments/optics/grating/): [Excel](experiments/optics/grating/excel_export.csv) · [Semicolons](experiments/optics/grating/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/grating/tab_separated.tsv) · [UTF-16](experiments/optics/grating/unicode_text.txt) · [Renamed](experiments/optics/grating/other_column_names.csv) |
| [Faraday rotation](experiments/optics/README.md#faraday-rotation-graduate) *(graduate)* | `θ = V·B·L` | Map the field along the rod with the Hall probe | [folder](experiments/optics/faraday_rotation/): [Excel](experiments/optics/faraday_rotation/excel_export.csv) · [Semicolons](experiments/optics/faraday_rotation/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/faraday_rotation/tab_separated.tsv) · [UTF-16](experiments/optics/faraday_rotation/unicode_text.txt) · [Renamed](experiments/optics/faraday_rotation/other_column_names.csv) |
| [Michelson interferometer](experiments/optics/README.md#michelson-interferometer) | `N = 2d/λ` | Count the same travel again, slowly, turning one way only | [folder](experiments/optics/michelson/): [Excel](experiments/optics/michelson/excel_export.csv) · [Semicolons](experiments/optics/michelson/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/michelson/tab_separated.tsv) · [UTF-16](experiments/optics/michelson/unicode_text.txt) · [Renamed](experiments/optics/michelson/other_column_names.csv) |
| [Young's double slit](experiments/optics/README.md#youngs-double-slit) | `y_m = m λ L / d` | Measure the slit-to-screen distance again with a steel tape, from the slide itself | [folder](experiments/optics/young_double_slit/): [Excel](experiments/optics/young_double_slit/excel_export.csv) · [Semicolons](experiments/optics/young_double_slit/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/young_double_slit/tab_separated.tsv) · [UTF-16](experiments/optics/young_double_slit/unicode_text.txt) · [Renamed](experiments/optics/young_double_slit/other_column_names.csv) |
| [Focal length of a thin lens](experiments/optics/README.md#focal-length-of-a-thin-lens) | `1/u + 1/v = 1/f` | Check the holder's index mark against the lens itself | [folder](experiments/optics/thin_lens/): [Excel](experiments/optics/thin_lens/excel_export.csv) · [Semicolons](experiments/optics/thin_lens/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/thin_lens/tab_separated.tsv) · [UTF-16](experiments/optics/thin_lens/unicode_text.txt) · [Renamed](experiments/optics/thin_lens/other_column_names.csv) |
| [Brewster's angle (Fresnel reflection)](experiments/optics/README.md#brewsters-angle-fresnel-reflection) | `R_p = \|r_p\|²,  tan θ_B = n` | At the minimum, turn the polariser either side of its setting | [folder](experiments/optics/brewster/): [Excel](experiments/optics/brewster/excel_export.csv) · [Semicolons](experiments/optics/brewster/semicolon_decimal_comma.csv) · [Tabs](experiments/optics/brewster/tab_separated.tsv) · [UTF-16](experiments/optics/brewster/unicode_text.txt) · [Renamed](experiments/optics/brewster/other_column_names.csv) |

### [Heat](experiments/heat/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Newton's law of cooling](experiments/heat/README.md#newtons-law-of-cooling) | `T = T_room + ΔT e^(−t/τ)` | Put the thermocouple in an ice-water bath for two minutes | [folder](experiments/heat/cooling/): [Excel](experiments/heat/cooling/excel_export.csv) · [Semicolons](experiments/heat/cooling/semicolon_decimal_comma.csv) · [Tabs](experiments/heat/cooling/tab_separated.tsv) · [UTF-16](experiments/heat/cooling/unicode_text.txt) · [Renamed](experiments/heat/cooling/other_column_names.csv) |
| [Stefan–Boltzmann law (lamp filament)](experiments/heat/README.md#stefanboltzmann-law-lamp-filament) | `P = εσA T⁴,  R/R₀ = (T/T₀)^1.209` | Read the ammeter with the lamp circuit open | [folder](experiments/heat/stefan_lamp/): [Excel](experiments/heat/stefan_lamp/excel_export.csv) · [Semicolons](experiments/heat/stefan_lamp/semicolon_decimal_comma.csv) · [Tabs](experiments/heat/stefan_lamp/tab_separated.tsv) · [UTF-16](experiments/heat/stefan_lamp/unicode_text.txt) · [Renamed](experiments/heat/stefan_lamp/other_column_names.csv) |
| [Thermal conductivity (Lee's disc)](experiments/heat/README.md#thermal-conductivity-lees-disc) | `k = m c (dT/dt)\|T₂ · x / (A (T₁ − T₂))` | Read both thermometers side by side in the steam chamber | [folder](experiments/heat/lees_disc/): [Excel](experiments/heat/lees_disc/excel_export.csv) · [Semicolons](experiments/heat/lees_disc/semicolon_decimal_comma.csv) · [Tabs](experiments/heat/lees_disc/tab_separated.tsv) · [UTF-16](experiments/heat/lees_disc/unicode_text.txt) · [Renamed](experiments/heat/lees_disc/other_column_names.csv) |
| [Thermocouple calibration (type K)](experiments/heat/README.md#thermocouple-calibration-type-k) | `emf = S(T − T_ref) + q(T − T_ref)²,  S ≈ 41 µV/K` | Read a thermometer in the reference flask | [folder](experiments/heat/thermocouple/): [Excel](experiments/heat/thermocouple/excel_export.csv) · [Semicolons](experiments/heat/thermocouple/semicolon_decimal_comma.csv) · [Tabs](experiments/heat/thermocouple/tab_separated.tsv) · [UTF-16](experiments/heat/thermocouple/unicode_text.txt) · [Renamed](experiments/heat/thermocouple/other_column_names.csv) |

### [Mechanics](experiments/mechanics/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Simple pendulum](experiments/mechanics/README.md#simple-pendulum) | `T = 2π√(L/g)` | Repeat three lengths released from 5° or less | [folder](experiments/mechanics/pendulum/): [Excel](experiments/mechanics/pendulum/excel_export.csv) · [Semicolons](experiments/mechanics/pendulum/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/pendulum/tab_separated.tsv) · [UTF-16](experiments/mechanics/pendulum/unicode_text.txt) · [Renamed](experiments/mechanics/pendulum/other_column_names.csv) |
| [Hooke's law spring](experiments/mechanics/README.md#hookes-law-spring) | `F = mg = k·x` | Weigh the hanger and add its mass to every load | [folder](experiments/mechanics/hooke/): [Excel](experiments/mechanics/hooke/excel_export.csv) · [Semicolons](experiments/mechanics/hooke/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/hooke/tab_separated.tsv) · [UTF-16](experiments/mechanics/hooke/unicode_text.txt) · [Renamed](experiments/mechanics/hooke/other_column_names.csv) |
| [Viscosity by Stokes' law (falling ball)](experiments/mechanics/README.md#viscosity-by-stokes-law-falling-ball) | `v = 2r²g(ρ_s − ρ_l) / 9η, corrected for the tube wall` | Read the glycerol's temperature with a thermometer in the tube | [folder](experiments/mechanics/stokes_viscosity/): [Excel](experiments/mechanics/stokes_viscosity/excel_export.csv) · [Semicolons](experiments/mechanics/stokes_viscosity/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/stokes_viscosity/tab_separated.tsv) · [UTF-16](experiments/mechanics/stokes_viscosity/unicode_text.txt) · [Renamed](experiments/mechanics/stokes_viscosity/other_column_names.csv) |
| [Kater's reversible pendulum](experiments/mechanics/README.md#katers-reversible-pendulum) | `T₁ = T₂ = T at the crossing,  g = 4π² L / T²` | Read the swing amplitude on a protractor behind the bar | [folder](experiments/mechanics/kater_pendulum/): [Excel](experiments/mechanics/kater_pendulum/excel_export.csv) · [Semicolons](experiments/mechanics/kater_pendulum/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/kater_pendulum/tab_separated.tsv) · [UTF-16](experiments/mechanics/kater_pendulum/unicode_text.txt) · [Renamed](experiments/mechanics/kater_pendulum/other_column_names.csv) |
| [Cavendish torsion balance](experiments/mechanics/README.md#cavendish-torsion-balance-graduate) *(graduate)* | `G = 2π² L r² θ / (M T²) ÷ (1 − β),  θ = ΔS / 4D` | Measure the mirror-to-scale distance with a steel tape | [folder](experiments/mechanics/cavendish/): [Excel](experiments/mechanics/cavendish/excel_export.csv) · [Semicolons](experiments/mechanics/cavendish/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/cavendish/tab_separated.tsv) · [UTF-16](experiments/mechanics/cavendish/unicode_text.txt) · [Renamed](experiments/mechanics/cavendish/other_column_names.csv) |
| [Driven damped oscillator (resonance)](experiments/mechanics/README.md#driven-damped-oscillator-resonance) | `A = a ω₀² / √((ω₀² − ω²)² + (γω)²)` | Time 20 crank turns with a stopwatch at three dial settings | [folder](experiments/mechanics/driven_oscillator/): [Excel](experiments/mechanics/driven_oscillator/excel_export.csv) · [Semicolons](experiments/mechanics/driven_oscillator/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/driven_oscillator/tab_separated.tsv) · [UTF-16](experiments/mechanics/driven_oscillator/unicode_text.txt) · [Renamed](experiments/mechanics/driven_oscillator/other_column_names.csv) |
| [Boyle's law (syringe and pressure sensor)](experiments/mechanics/README.md#boyles-law-syringe-and-pressure-sensor) | `p (V + V₀) = nRT` | Measure the connecting tube's length and bore | [folder](experiments/mechanics/boyle_gas/): [Excel](experiments/mechanics/boyle_gas/excel_export.csv) · [Semicolons](experiments/mechanics/boyle_gas/semicolon_decimal_comma.csv) · [Tabs](experiments/mechanics/boyle_gas/tab_separated.tsv) · [UTF-16](experiments/mechanics/boyle_gas/unicode_text.txt) · [Renamed](experiments/mechanics/boyle_gas/other_column_names.csv) |

### [Waves & sound](experiments/waves/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Speed of sound (resonance tube)](experiments/waves/README.md#speed-of-sound-resonance-tube) | `L + e = v/4f, e ≈ 0.3 D` | Read the air temperature inside the tube | [folder](experiments/waves/resonance_tube/): [Excel](experiments/waves/resonance_tube/excel_export.csv) · [Semicolons](experiments/waves/resonance_tube/semicolon_decimal_comma.csv) · [Tabs](experiments/waves/resonance_tube/tab_separated.tsv) · [UTF-16](experiments/waves/resonance_tube/unicode_text.txt) · [Renamed](experiments/waves/resonance_tube/other_column_names.csv) |

### [Quantum](experiments/quantum/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Electron diffraction (de Broglie)](experiments/quantum/README.md#electron-diffraction-de-broglie) | `λ = h/√(2meV),  2d sin θ = λ,  D = 2L tan 2θ` | Measure the foil-to-screen distance with a rule | [folder](experiments/quantum/electron_diffraction/): [Excel](experiments/quantum/electron_diffraction/excel_export.csv) · [Semicolons](experiments/quantum/electron_diffraction/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/electron_diffraction/tab_separated.tsv) · [UTF-16](experiments/quantum/electron_diffraction/unicode_text.txt) · [Renamed](experiments/quantum/electron_diffraction/other_column_names.csv) |
| [Zeeman effect (cadmium red line)](experiments/quantum/README.md#zeeman-effect-cadmium-red-line-graduate) *(graduate)* | `Δν̃ = 2μ_B B/hc = (1/2nt)·δ/Δ` | Measure the field in the gap with a calibrated gaussmeter | [folder](experiments/quantum/zeeman/): [Excel](experiments/quantum/zeeman/excel_export.csv) · [Semicolons](experiments/quantum/zeeman/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/zeeman/tab_separated.tsv) · [UTF-16](experiments/quantum/zeeman/unicode_text.txt) · [Renamed](experiments/quantum/zeeman/other_column_names.csv) |
| [Millikan oil drop](experiments/quantum/README.md#millikan-oil-drop) | `q = n·e` | Measure the plate spacing with callipers | [folder](experiments/quantum/millikan/): [Excel](experiments/quantum/millikan/excel_export.csv) · [Semicolons](experiments/quantum/millikan/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/millikan/tab_separated.tsv) · [UTF-16](experiments/quantum/millikan/unicode_text.txt) · [Renamed](experiments/quantum/millikan/other_column_names.csv) |
| [Photoelectric effect (h/e)](experiments/quantum/README.md#photoelectric-effect-he) | `eV_s = hf − φ` | Mask the anode so only the cathode is lit, and reread every line | [folder](experiments/quantum/photoelectric/): [Excel](experiments/quantum/photoelectric/excel_export.csv) · [Semicolons](experiments/quantum/photoelectric/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/photoelectric/tab_separated.tsv) · [UTF-16](experiments/quantum/photoelectric/unicode_text.txt) · [Renamed](experiments/quantum/photoelectric/other_column_names.csv) |
| [Franck–Hertz experiment (mercury)](experiments/quantum/README.md#franckhertz-experiment-mercury) | `peaks at V = V_c + n·E₁/e` | Read the oven thermometer for a few minutes | [folder](experiments/quantum/franck_hertz/): [Excel](experiments/quantum/franck_hertz/excel_export.csv) · [Semicolons](experiments/quantum/franck_hertz/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/franck_hertz/tab_separated.tsv) · [UTF-16](experiments/quantum/franck_hertz/unicode_text.txt) · [Renamed](experiments/quantum/franck_hertz/other_column_names.csv) |
| [Optical pumping of rubidium](experiments/quantum/README.md#optical-pumping-of-rubidium-graduate) *(graduate)* | `hf = g_F μ_B \|k·I + B₀\|` | Read the coil current on a calibrated ammeter in series | [folder](experiments/quantum/optical_pumping/): [Excel](experiments/quantum/optical_pumping/excel_export.csv) · [Semicolons](experiments/quantum/optical_pumping/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/optical_pumping/tab_separated.tsv) · [UTF-16](experiments/quantum/optical_pumping/unicode_text.txt) · [Renamed](experiments/quantum/optical_pumping/other_column_names.csv) |
| [Planck's constant from LEDs](experiments/quantum/README.md#plancks-constant-from-leds) | `eV = hf − φ` | Read one LED's turn-on voltage on a calibrated reference meter too | [folder](experiments/quantum/planck_led/): [Excel](experiments/quantum/planck_led/excel_export.csv) · [Semicolons](experiments/quantum/planck_led/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/planck_led/tab_separated.tsv) · [UTF-16](experiments/quantum/planck_led/unicode_text.txt) · [Renamed](experiments/quantum/planck_led/other_column_names.csv) |
| [Quantum tunnelling simulation](experiments/quantum/README.md#quantum-tunnelling-simulation) | `T ≈ e^(−2κa), κ = √(2m(V₀−E))/ħ` | Rerun the simulation at a second energy (0.25 eV) | [folder](experiments/quantum/tunnelling/): [Excel](experiments/quantum/tunnelling/excel_export.csv) · [Semicolons](experiments/quantum/tunnelling/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/tunnelling/tab_separated.tsv) · [UTF-16](experiments/quantum/tunnelling/unicode_text.txt) · [Renamed](experiments/quantum/tunnelling/other_column_names.csv) |
| [Blackbody radiation](experiments/quantum/README.md#blackbody-radiation) | `B(λ,T) ∝ λ⁻⁵ / (e^(hc/λkT) − 1)` | Record a mercury calibration lamp on the same spectrometer | [folder](experiments/quantum/blackbody/): [Excel](experiments/quantum/blackbody/excel_export.csv) · [Semicolons](experiments/quantum/blackbody/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/blackbody/tab_separated.tsv) · [UTF-16](experiments/quantum/blackbody/unicode_text.txt) · [Renamed](experiments/quantum/blackbody/other_column_names.csv) |
| [Atomic spectral lines (hydrogen)](experiments/quantum/README.md#atomic-spectral-lines-hydrogen) | `1/λ = R(1/2² − 1/n²)` | Remeasure the odd line with a fresh hydrogen tube | [folder](experiments/quantum/spectral_lines/): [Excel](experiments/quantum/spectral_lines/excel_export.csv) · [Semicolons](experiments/quantum/spectral_lines/semicolon_decimal_comma.csv) · [Tabs](experiments/quantum/spectral_lines/tab_separated.tsv) · [UTF-16](experiments/quantum/spectral_lines/unicode_text.txt) · [Renamed](experiments/quantum/spectral_lines/other_column_names.csv) |

### [Nuclear & particle](experiments/nuclear/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [Gamma-ray attenuation in lead](experiments/nuclear/README.md#gamma-ray-attenuation-in-lead) | `N = N₀ e^(−μx),  μ = (μ/ρ)·ρ` | Count with the source removed | [folder](experiments/nuclear/gamma_attenuation/): [Excel](experiments/nuclear/gamma_attenuation/excel_export.csv) · [Semicolons](experiments/nuclear/gamma_attenuation/semicolon_decimal_comma.csv) · [Tabs](experiments/nuclear/gamma_attenuation/tab_separated.tsv) · [UTF-16](experiments/nuclear/gamma_attenuation/unicode_text.txt) · [Renamed](experiments/nuclear/gamma_attenuation/other_column_names.csv) |
| [Muon lifetime](experiments/nuclear/README.md#muon-lifetime-graduate) *(graduate)* | `N(t) = A e^(−t/τ) + B` | Read the singles rate with the detector open, then under a black cloth | [folder](experiments/nuclear/muon_lifetime/): [Excel](experiments/nuclear/muon_lifetime/excel_export.csv) · [Semicolons](experiments/nuclear/muon_lifetime/semicolon_decimal_comma.csv) · [Tabs](experiments/nuclear/muon_lifetime/tab_separated.tsv) · [UTF-16](experiments/nuclear/muon_lifetime/unicode_text.txt) · [Renamed](experiments/nuclear/muon_lifetime/other_column_names.csv) |
| [Radioactive decay (Geiger–Müller)](experiments/nuclear/README.md#radioactive-decay-geigermüller) | `N = N₀ e^(−λt) + B, t½ = ln 2 / λ` | Remove the source and count the room background | [folder](experiments/nuclear/radioactive_decay/): [Excel](experiments/nuclear/radioactive_decay/excel_export.csv) · [Semicolons](experiments/nuclear/radioactive_decay/semicolon_decimal_comma.csv) · [Tabs](experiments/nuclear/radioactive_decay/tab_separated.tsv) · [UTF-16](experiments/nuclear/radioactive_decay/unicode_text.txt) · [Renamed](experiments/nuclear/radioactive_decay/other_column_names.csv) |
| [Rutherford scattering (alphas on gold)](experiments/nuclear/README.md#rutherford-scattering-alphas-on-gold-graduate) *(graduate)* | `N(θ) ∝ 1/sin⁴(θ/2)` | Count at equal angles on both sides of the beam | [folder](experiments/nuclear/rutherford/): [Excel](experiments/nuclear/rutherford/excel_export.csv) · [Semicolons](experiments/nuclear/rutherford/semicolon_decimal_comma.csv) · [Tabs](experiments/nuclear/rutherford/tab_separated.tsv) · [UTF-16](experiments/nuclear/rutherford/unicode_text.txt) · [Renamed](experiments/nuclear/rutherford/other_column_names.csv) |
| [Compton scattering](experiments/nuclear/README.md#compton-scattering-graduate) *(graduate)* | `E′ = E / (1 + (E/m_e c²)(1 − cos θ))` | Read known calibration lines with the same MCA settings | [folder](experiments/nuclear/compton/): [Excel](experiments/nuclear/compton/excel_export.csv) · [Semicolons](experiments/nuclear/compton/semicolon_decimal_comma.csv) · [Tabs](experiments/nuclear/compton/tab_separated.tsv) · [UTF-16](experiments/nuclear/compton/unicode_text.txt) · [Renamed](experiments/nuclear/compton/other_column_names.csv) |

### [Condensed matter](experiments/condensed/README.md)

| Experiment | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- |
| [X-ray Bragg diffraction (NaCl)](experiments/condensed/README.md#x-ray-bragg-diffraction-nacl-graduate) *(graduate)* | `nλ = 2d sin θ` | Scan the detector through the direct beam with the crystal removed | [folder](experiments/condensed/bragg_xray/): [Excel](experiments/condensed/bragg_xray/excel_export.csv) · [Semicolons](experiments/condensed/bragg_xray/semicolon_decimal_comma.csv) · [Tabs](experiments/condensed/bragg_xray/tab_separated.tsv) · [UTF-16](experiments/condensed/bragg_xray/unicode_text.txt) · [Renamed](experiments/condensed/bragg_xray/other_column_names.csv) |
| [Superconducting transition](experiments/condensed/README.md#superconducting-transition-graduate) *(graduate)* | `R(T) = R_n(T) / (1 + e^(−(T−Tc)/w))` | Record a warming sweep as well and compare it with the cooling sweep | [folder](experiments/condensed/sc_transition/): [Excel](experiments/condensed/sc_transition/excel_export.csv) · [Semicolons](experiments/condensed/sc_transition/semicolon_decimal_comma.csv) · [Tabs](experiments/condensed/sc_transition/tab_separated.tsv) · [UTF-16](experiments/condensed/sc_transition/unicode_text.txt) · [Renamed](experiments/condensed/sc_transition/other_column_names.csv) |
| [Band gap of germanium](experiments/condensed/README.md#band-gap-of-germanium-graduate) *(graduate)* | `R ∝ T^(−3/2) e^(Eg/2kT)` | Keep logging as the oven cools back down | [folder](experiments/condensed/band_gap/): [Excel](experiments/condensed/band_gap/excel_export.csv) · [Semicolons](experiments/condensed/band_gap/semicolon_decimal_comma.csv) · [Tabs](experiments/condensed/band_gap/tab_separated.tsv) · [UTF-16](experiments/condensed/band_gap/unicode_text.txt) · [Renamed](experiments/condensed/band_gap/other_column_names.csv) |

<!-- bench:end -->

The Helmholtz, laser-alignment, Faraday and Beer-Lambert experiments, and their CSV formats, come from the team's first prototype by [@mtalha05-phy](https://github.com/mtalha05-phy); his datasets run unchanged here, and his self-heating resistor dataset is part of the evaluation.

## What's new

1. **A closed troubleshooting loop.** PhysSandbox ranks the likely causes, picks the bench test with the most information per minute, then folds in only the *outcome* of the test you ran. On the demo data the leading cause goes from 64% to 92% and is confirmed.
2. **An agent whose code we assume is hostile.** A model on Vultr Serverless Inference writes Python to answer your questions. A static scan highlights risky lines, but nothing relies on it: the glovebox is the safeguard.
3. **Containment receipts that don't take the code's word for it.** Every job probes its own walls (kernel, network interfaces, DNS, outbound connections, disk, user, visible secrets) *before any untrusted code runs* and writes that first; agent code is mounted read-only but not yet executed. Agent code then runs in a separate child process; the runner itself is made non-dumpable, so the child can't reach into the runner's report through `/proc` (it can reach the tracer's copy of its own output, which the runner already treats as the code's word, and the tracer records the attempt). The child can shape its own output but not the probe, and only short text fields of its output are kept (no payloads, capped length); the host also reads at most 2 MB from any container. The host then checks the container's real configuration and exit state with `docker inspect` (runtime, network mode, read-only root, memory, process and CPU limits, capabilities, privilege flags, user, devices, mounts, no-exec scratch, OOM kill). Kills (memory, time) come only from Docker's record and the host's timer. What the code *tried* (reach the internet, write outside scratch space, read files it may not, start programs, signal other processes) comes from a **system-call tracer**: the runner starts `strace` on the child before the code exists, so wrapping an attempt in `try/except` hides nothing; the receipt says which source it used (`attempts_observed_by`). The wall that stopped each attempt is the part the host verifies. The **Forge its own receipt** button runs code that prints a fake all-green receipt and tries to write into the runner's report; it can't succeed by design, and the attempt is flagged.
4. **A lab notebook you can check without trusting us.** Receipts are hash-chained and each one is signed with Ed25519, as are the notebook's start (a genesis record with its creation time) and a head record (count and last hash) rewritten on each append. The public key is published at `/api/ledger/public-key` and pinned in this repository (`notebook/ed25519-public-key.pem`, key `cd5618512f391bda`), so anyone can check every signature with a short standalone script, `tools/verify_receipts.py`, instead of taking the server's word. Stripping signatures, editing an entry and rebuilding the hashes, or deleting entries off the end all fail. **Tamper with a copy** shows it: it edits a copy of the notebook the way an attacker without the private key would, and the check catches it. Rolling the notebook back to an older copy, or wiping it, can't be caught from the notebook alone; the signed head in every downloaded record catches it from outside ([threat model](#the-lab-notebook-check-it-yourself)).
5. **An agent that repairs its own code, sealed.** If the model's script fails in the box, the sandbox's error goes back to the model and it tries again (up to three attempts, each in a fresh container with its own receipt).

## Try it in 90 seconds

Open the demo and press **Take the 90-second tour**. It walks through a real investigation (resistor reads high → offset found → bench test → cause confirmed), a break-out attempt stopped by the network wall, a poisoned file whose hidden instruction reaches the model and is contained, and the tamper check on the lab notebook. Every step runs live in the sandbox.

**Try your own kind of file.** Under the samples, *Same measurement, other file formats* loads that experiment's headline sample saved the ways real files arrive: an Excel export (byte-order mark, padded comment lines, an empty row of commas), semicolons with decimal commas, tab-separated, Excel's UTF-16 "Unicode text", and one with the column names a person would type (`Current (A)`), which the page asks you to match. Each has a download link, and all 255 are in [`experiments/`](experiments/README.md), in each experiment's folder next to its documentation; every one gives the result that experiment's README lists.

Every investigation can be downloaded as a **PDF report** in one click: the outcome, the fix for the confirmed cause, and for every step the data chart with its fit, the measured values with uncertainties, the likely causes, the recommended test with how to do it and its safety note, plus each sandbox receipt with its signature. The browser sends only the steps' receipt hashes: the server builds the PDF from its own stored result of each step, whose SHA-256 is sealed inside that step's signed receipt, and only for the browser session that ran it. A made-up result, a real receipt from another job, or a stored result edited on disk is refused. The PDF also carries its own evidence as an attached file: each step's signed receipt and the exact result it was built from, so anyone can check a report offline, without the server, with `python tools/verify_report.py report.pdf notebook/ed25519-public-key.pem`. It checks every signature, every result against the hash sealed in its receipt, the order of the steps, and that the page text still shows the signed explanation, then prints the signed numbers to compare with the tables. A markdown record is available too; it ends with the lab notebook's signed head, to keep.

Adding an experiment group needs no edits to existing code: a physics module (`sandbox/tools/bench_<group>.py`), a fault library (`faults/bench_<group>.yaml`), a catalogue file (`app/catalog.d/<group>.yaml`), a data generator (`data/gen_<group>.py`) and its evaluation cases (`data/manifest.d/<group>.yaml`). Nine groups (33 of the 51 experiments) were added that way, built in parallel.

## The glovebox (Blast Radius Zero)

Every job, physics or agent code, runs in a fresh container with:

| Wall | Setting |
| --- | --- |
| Kernel | gVisor (`runsc`): system calls hit a user-space kernel, not the host |
| Network | `--network none`: no interface except loopback, no DNS, no outbound connections |
| Disk | read-only root, 64 MB `noexec` scratch, input mounted read-only |
| Resources | 512 MB memory, 1 CPU, 64 processes, 30 s wall clock |
| Identity | uid 65534 (nobody), all capabilities dropped, `no-new-privileges` |
| Secrets | no host environment passed in; API keys stay outside |

The model never sees raw rows by default, only column names and ranges. When its code fails, the repair loop sends back only the exception's type and line number, never the message or output, because a failed parse can echo a line of the file. Turn on "Let the agent read the raw file" with the poisoned sample and the hidden instruction reaches the model. The tour does this with the live model first: in our tests `deepseek-v4.1-flash` on Vultr ignored the instruction and wrote clean code. We don't rely on that: the **red team** switch substitutes a fixed script, the code a fooled model would write (read the file, send it to an outside server), and the glovebox runs it anyway. That script is a template, not model output, and the UI labels it as such. The network wall blocks it and lights up red.

**Try to break out** buttons run real attacks inside the box: send data to the internet (blocked), use all the memory (killed at 512 MB), read secrets and tamper with the tools (nothing to read, read-only disk), and forge its own containment receipt (ignored and flagged).

The public demo is also protected from its visitors: at most two sandboxes run at once (jobs run in worker threads, so one slow job never freezes the site), uploads are capped at 1 MB, and each visitor has a request limit, tightest on the endpoints that spend inference credit.

**Development mode** (`SANDBOX_MODE=local`, for working on the physics) has no isolation, so it refuses the break-out demos and agent-written code outright, and every receipt, record and report made in it says "not isolated".

**Nothing the code writes reaches anyone else.** The public containment log (`/api/containment-log`) and the public receipts hold only text the host wrote itself and counts: when a job fails, the log says which exception it raised, never its message, and the tracer's view of what the code tried is reduced to counts. The paths, addresses and messages the code chose go back only to the person who ran the job. (An independent review found that an earlier version logged the first 200 characters of the error, which hostile code could fill with the data; that channel is closed.)

**Known limits.** The tracer runs inside the box as the same user as the code, so the code could kill it; that kill is itself recorded, and a tracer that stops early is reported as tampering. Fully host-side tracing (gVisor's `runsc --strace` on the VM) would remove even that. The app runs as root on the VM because it drives Docker, and Docker access is root-equivalent; the boundary we rely on is gVisor plus the container flags, and the signing key and inference key live on the same VM. Running the sandboxes on a separate Vultr instance in a private network is the next step.

## The lab notebook: check it yourself

Every job's receipt goes into the lab notebook (`receipts.jsonl`, one JSON record per line):

- **Genesis** (`seq` 0, `kind: "genesis"`): written when the notebook is created, with its start time and a random notebook id. Receipt #1 chains to it.
- **Receipts** (`seq` 1, 2, …): hashes of the job's input, code and output, the walls measured inside the box and checked by the host, the outcome, and `prev`, the hash of the record before it.
- **Head** (`kind: "head"`, its own file, rewritten on every append): `count`, `last_hash`, and the genesis record's hash, time and id.

Every record carries three more fields:

| Field | What it is |
| --- | --- |
| `hash` | SHA-256 of the record's canonical JSON: every field except `hash` and `sig`, keys sorted, no spaces (`json.dumps(sort_keys=True, separators=(",", ":"))`), 64 hex characters |
| `key_id` | the first 16 hex characters of SHA-256 of the raw 32-byte public key; it is inside the hashed part, so it is signed too |
| `sig` | Ed25519 signature over the ASCII text of `hash`, hex-encoded (128 characters) |

The live demo's notebook key is `cd5618512f391bda` (SHA-256 of the raw key `cd5618512f391bda1f6ce328cc125f500eac759bfaf7375f53d35b786929deb4`); its public key is committed at `notebook/ed25519-public-key.pem`, so a key served by the host can be compared with one fixed in git history. The private key is made on first use at `~/.physsandbox/ledger_ed25519.pem` (mode 0600, outside the repository and every sandbox; `LEDGER_SIGNING_KEY_FILE` moves it). The public key is at `GET /api/ledger/public-key` (JSON with the PEM and `key_id`; add `?format=pem` for the bare PEM).

To check the notebook without trusting the server (Python 3.8+ and `pip install cryptography`, nothing else):

```bash
curl -s 'https://HOST/api/ledger?limit=100' -o export.json
curl -s 'https://HOST/api/ledger/public-key?format=pem' -o notebook.pem
python tools/verify_receipts.py export.json notebook.pem
# Later: has anything changed since the head you kept?
python tools/verify_receipts.py export.json notebook.pem --expect-head physsandbox-record.md
```

The script recomputes every hash, checks every signature and link from the genesis record through the receipts to the head, and ignores the server's own verdict in the export. It exits 0 if everything checks out, 1 if it finds tampering, a rollback or a wipe, and 2 if the export doesn't cover the check. `--expect-head` takes any head you saved earlier: a downloaded investigation record (`.md`), a saved `/api/status` or `/api/ledger` response, a head record on its own, or `COUNT:HASH`. An export holds the latest 100 receipts; to compare with an older head, export from it with `/api/ledger?start=COUNT&limit=100`.

**Threat model: what is caught, and what needs a copy of the head kept elsewhere.**

| What someone does to the notebook | Caught? |
| --- | --- |
| Edits a receipt | Yes: it no longer matches its hash |
| Edits a receipt and rebuilds every hash after it | Yes: the signatures no longer match, and only the private key can make new ones |
| Strips the signatures | Yes: unsigned records are rejected |
| Deletes receipts off the end | Yes: the signed head records how many there were |
| Deletes or edits the head | Yes. The next job then starts a new notebook (the old files are archived beside it, not deleted), with a new start time |
| Restores an older copy of both files (rollback) | **Not from the notebook alone**: an older notebook is still a valid notebook, and "Check for tampering" says intact. Caught with an earlier head kept elsewhere: the count went down, or receipt #count no longer has that head's hash |
| Deletes both files (wipe) | The next job starts a new notebook with a new start time, shown as "Notebook started …" in the Lab notebook panel. With an earlier head, the script reports a different notebook |
| Replaces the signing key | Every old signature fails, and the new notebook's `key_id` differs from the one in your saved record and public key |
| Gets root on the VM and reads the private key | Can sign a new history. An earlier head kept elsewhere still catches any change to the receipts up to it, because its hash covers all of them; receipts after it rest on trusting the server |

So the notebook proves on its own that nothing in it was edited, removed or added out of order; to prove it was not rolled back or replaced, you need a head from earlier. Every downloaded investigation record ends with the signed head at the time of download (the record's own receipts are in the chain behind it), and `/api/status` and `/api/ledger` include it as `head_record`. Keep one where the server can't reach it, for example in your email.

**Notebook history.** The live notebook started on 5 November 2026 at 20:42 UTC, when the demo moved from HMAC receipts (which only the server can check) to Ed25519. The earlier HMAC notebook was moved aside on the VM, not deleted, which is why the containment log shows jobs from before that time. `deploy/update.sh fresh` starts a new notebook the same way; we record every such restart here, and snapshots of the signed head are committed under `notebook/`, so a later rollback past a committed head can be caught by anyone with `--expect-head`.

## Vultr services used

| Service | Role |
| --- | --- |
| **Vultr Cloud Compute** | One VM (London) runs the web app, the agent loop, gVisor and every sandboxed job |
| **Vultr Serverless Inference** | OpenAI-compatible model that writes the analysis code and the plain-language explanation |

## Architecture

```
Browser ──upload──▶ FastAPI app (Vultr VM)
                      │  schema summary only (no raw rows by default)
                      ├──────────────▶ Vultr Serverless Inference ── code + wording
                      │
                      ├─ run job ─▶ ┌─ gVisor container, no network, read-only ─┐
                      │             │ runner.py: probe walls ▸ run physics/code   │
                      │             └─────────────── destroyed ──────────────────┘
                      ├─ rank causes (fault library, Bayes) ▸ next test (bits/min)
                      └─ receipt ▸ hash-chained lab notebook ▸ containment log
```

## Evaluation on seeded faults

`python eval/run_eval.py` replays the whole troubleshooting loop on 289 cases with known faults (`data/manifest.yaml` and `data/manifest.d/`): for every experiment, a healthy run, its common faults, and the follow-up result of the recommended test. It reports the first measurement and the follow-ups separately:

- **First measurement, fault cases: 109/109** name the true cause first, across all 51 experiments.
- **After the recommended test: 51/51** confirm the true cause (above 90%).
- **No false alarms: 51/51** healthy datasets come back "no fault found", with no test suggested.
- **When the odds point the wrong way: 39/39.** In the ambiguous demos the data alone favour the more common of two faults. Partner cases seed the *less* common one instead (one for each of the first 39 experiments): the tool must rank it second, recommend the test that separates the two, and put it first once the test result is in. All 39 do; 29 are already confirmed above 90%, and the other 10 lead and get a second test.
- **Not tuned to one lucky dataset**: `eval/run_seeds.sh` regenerates every dataset with ten other random seeds and replays the whole evaluation for each. All ten pass: 2,890 of 2,890 cases correct. (An earlier run caught one miss, a 3.6-sigma fluctuation past a too-tight Beer-Lambert threshold; the threshold now follows the same 4/5-sigma rule as the rest.)
- **Real files, not just tidy ones**: `eval/check_parsing.py` rewrites every one of the 289 seeded files (all 51 experiments) the ways real files arrive: Windows line endings and a byte-order mark, a spreadsheet export (comment lines padded with commas, an empty row of only commas, trailing empty columns), quoted column names, semicolon-separated with decimal commas, tab- and space-separated, UTF-16, stray blank lines. It also checks the 255 example upload files in `experiments/`. All 2,567 files give exactly the same result as the originals. A user's Faraday file with an empty spreadsheet row above the header (which an earlier version misread) is now one of the evaluation cases, and its one odd reading is now named as a fault of its own ("one reading far off the rest").
- **The diagnosis can't be steered by the file**: the physics parser skips comment lines and the model plays no part in the diagnosis, so the poisoned file gets the same result as its clean twin. An injected instruction can only reach the agent box, where the glovebox contains whatever the model writes.

How the demo cases are built: in each demo the two leading faults predict the same first measurement, by design, so the first split simply reflects their priors (how often each happens on that bench, set by hand); the recommended test is the one whose outcomes the two faults predict differently. That is the situation the tool is for: data that can't separate two causes, and one quick test that can.

The likelihoods in the fault libraries (`faults/*.yaml`) are hand-set from bench experience, not calibrated on data, so the percentages show how strongly the evidence points within that model, not measured frequencies. To check the rules aren't tuned to one lucky dataset, `eval/run_seeds.sh` regenerates every dataset with ten other random seeds (results above). Because the data come from the same models the tool fits, this shows the loop is self-consistent and robust to noise, not that the fault rules match real benches; that needs real lab data.

These are synthetic datasets we generated with known faults (`data/generate*.py`, `data/gen_*.py`), so the evaluation shows the loop works end to end, not accuracy on real lab data. The four prototype CSVs from @mtalha05-phy run unchanged. Real-bench data from teaching labs is the next evaluation.

## Run it

**On a Vultr VM (Ubuntu 24.04), full containment:**

```bash
git clone https://github.com/mukeshkbj/physsandbox.git && cd physsandbox
cp .env.example .env    # add your Vultr Inference API key and model
sudo bash deploy/setup_vultr.sh
sudo bash deploy/enable_https.sh   # HTTPS via Caddy and an sslip.io name, no domain needed
```

**Locally, no isolation (development only):**

```bash
pip install -r requirements.txt && python data/generate.py
SANDBOX_MODE=local uvicorn app.main:app --reload
```

## Repository layout

```
app/        web app: sandbox runner, agent, ranking, receipts ledger, explanation, safety, PDF report;
            catalog.yaml and catalog.d/*.yaml describe the experiment bench the interface is built from
sandbox/    job image: runner.py (probe, system-call tracer, run), physics models (analyze.py, experiments.py, bench_*.py), break-out demos
faults/     fault libraries, next-test catalogue and a fix for every fault (YAML; bench_<group>.yaml per experiment group)
data/       seeded dataset generators (generate*.py, gen_*.py) and ground truth (manifest.yaml, manifest.d/)
experiments/ the bench by area of physics: a README per area (models, faults and fixes, tests, demo case) and each
            experiment's example upload files in five formats (written by data/make_experiments.py)
eval/       evaluation of the full troubleshooting loop
static/     single-page interface
tools/      verify_receipts.py: checks a lab notebook export with its public key, without trusting the server;
            verify_report.py: checks a downloaded PDF report offline from the evidence attached to it
notebook/   the live demo's pinned Ed25519 public key and committed snapshots of the signed head
deploy/     Vultr VM setup script and in-place update script
```

## Safety

Bench recommendations come from a fixed test catalogue with safety notes (never lift a safety earth; laser changes need your laser safety officer). Model text is checked against forbidden advice before it is shown.

## License

MIT
