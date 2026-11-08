# Heat

4 experiments on the PhysSandbox bench. Try any of them on the [live demo](https://192-248-159-149.sslip.io/) under *Heat*. [All areas](../README.md) · [Project README](../../README.md)

| Experiment | Level | Model | Test that settles the demo case | Example files |
| --- | --- | --- | --- | --- |
| [Newton's law of cooling](#newtons-law-of-cooling) | teaching lab | `T = T_room + ΔT e^(−t/τ)` | Put the thermocouple in an ice-water bath for two minutes | [Excel](cooling/excel_export.csv) · [Semicolons](cooling/semicolon_decimal_comma.csv) · [Tabs](cooling/tab_separated.tsv) · [UTF-16](cooling/unicode_text.txt) · [Renamed](cooling/other_column_names.csv) |
| [Stefan–Boltzmann law (lamp filament)](#stefanboltzmann-law-lamp-filament) | teaching lab | `P = εσA T⁴,  R/R₀ = (T/T₀)^1.209` | Read the ammeter with the lamp circuit open | [Excel](stefan_lamp/excel_export.csv) · [Semicolons](stefan_lamp/semicolon_decimal_comma.csv) · [Tabs](stefan_lamp/tab_separated.tsv) · [UTF-16](stefan_lamp/unicode_text.txt) · [Renamed](stefan_lamp/other_column_names.csv) |
| [Thermal conductivity (Lee's disc)](#thermal-conductivity-lees-disc) | teaching lab | `k = m c (dT/dt)\|T₂ · x / (A (T₁ − T₂))` | Read both thermometers side by side in the steam chamber | [Excel](lees_disc/excel_export.csv) · [Semicolons](lees_disc/semicolon_decimal_comma.csv) · [Tabs](lees_disc/tab_separated.tsv) · [UTF-16](lees_disc/unicode_text.txt) · [Renamed](lees_disc/other_column_names.csv) |
| [Thermocouple calibration (type K)](#thermocouple-calibration-type-k) | teaching lab | `emf = S(T − T_ref) + q(T − T_ref)²,  S ≈ 41 µV/K` | Read a thermometer in the reference flask | [Excel](thermocouple/excel_export.csv) · [Semicolons](thermocouple/semicolon_decimal_comma.csv) · [Tabs](thermocouple/tab_separated.tsv) · [UTF-16](thermocouple/unicode_text.txt) · [Renamed](thermocouple/other_column_names.csv) |

Each experiment's folder holds its headline sample in five file formats:

| File | Format |
| --- | --- |
| `excel_export.csv` | **Excel export**: Byte-order mark, Windows line endings, comment lines padded with commas, an empty row of only commas above the header, a trailing empty column |
| `semicolon_decimal_comma.csv` | **Semicolons, decimal commas**: A European spreadsheet export: `;` between columns and `0,25` for 0.25 |
| `tab_separated.tsv` | **Tab-separated**: Tabs between columns, as copied out of a spreadsheet |
| `unicode_text.txt` | **UTF-16 "Unicode text"**: Excel's *Unicode text* export: UTF-16 with a byte-order mark, tab-separated |
| `other_column_names.csv` | **Other column names**: The names a person would type, units in brackets (`Current (A)`): the page asks you to match them |

## Newton's law of cooling

A hot sample cooling in air, read with a K-type thermocouple.

| | |
| --- | --- |
| Model | `T = T_room + ΔT e^(−t/τ)` |
| Columns | `time_s`, `temperature_C` (one row per reading; `#` lines are comments) |
| You enter | Room temperature (°C) (default 21); Expected time constant (s) (default 420) |
| Physics code | [`sandbox/tools/experiments.py`](../../sandbox/tools/experiments.py), fitted inside the glovebox |
| Fault library | [`faults/faults.yaml`](../../faults/faults.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `cooling` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Thermocouple cold-junction compensation error | A cold junction 2–3 °C warmer than the meter assumes shifts every reading by that much | Check the thermocouple in ice water and subtract that offset from every reading, and keep the meter's cold junction away from warm air. |
| The surroundings aren't at the room temperature you assumed |  | Measure the air temperature beside the sample with a second thermometer and use it as the room temperature in the fit. |
| Poor thermal contact between thermocouple and sample |  | Tape the junction to the sample with a dab of thermal paste and repeat the run. |
| Unknown cause (none of the above fits well) |  | Repeat with a second thermocouple on the sample and compare the two cooling curves. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Put the thermocouple in an ice-water bath for two minutes | 3 | Crushed ice topped up with water, stirred, reads 0.0 °C. Record the meter for two minutes. |
| Measure the air temperature next to the sample with a second thermometer | 5 | Place a calibrated thermometer where the sample cools, away from vents and windows. |
| Repeat with thermal paste and the junction taped to the sample | 30 | Bond the thermocouple bead to the sample with thermal paste and Kapton tape, then repeat the cooling run. *Safety:* Let the sample cool below 50 °C before handling it. |

### Samples on the page

- **Settles 2.5 °C above the room**: [`cooling_cjc_offset.csv`](../../data/seeded/cooling_cjc_offset.csv). It cools at the expected rate, but settles about 2.5 °C above the room temperature.
- **Cools far too slowly**: [`cooling_slow_contact.csv`](../../data/seeded/cooling_slow_contact.csv). It settles at room temperature, but takes more than twice as long as expected to get there.
- **Healthy cooling curve**: [`cooling_clean.csv`](../../data/seeded/cooling_clean.csv). Nothing should look off: settles at 21 °C at the expected rate.
- Sample result of *Put the thermocouple in an ice-water bath for two minutes*: [`cooling_cjc_ice_point.csv`](../../data/seeded/cooling_cjc_ice_point.csv)

### The demo case

1. **Settles 2.5 °C above the room** ([`cooling_cjc_offset.csv`](../../data/seeded/cooling_cjc_offset.csv)): the leading cause is *Thermocouple cold-junction compensation error* at 55%, with *The surroundings aren't at the room temperature you assumed* at 44%.
2. Recommended test: **Put the thermocouple in an ice-water bath for two minutes** (3 min, 0.99 bits).
3. With its result ([`cooling_cjc_ice_point.csv`](../../data/seeded/cooling_cjc_ice_point.csv)): *Thermocouple cold-junction compensation error*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`cooling/`](cooling/)); each gives the result above. [Excel export](cooling/excel_export.csv) · [Semicolons, decimal commas](cooling/semicolon_decimal_comma.csv) · [Tab-separated](cooling/tab_separated.tsv) · [UTF-16 "Unicode text"](cooling/unicode_text.txt) · [Other column names](cooling/other_column_names.csv)

## Stefan–Boltzmann law (lamp filament)

Electrical power into a tungsten filament against its temperature from its resistance, to test P ∝ T⁴.

| | |
| --- | --- |
| Model | `P = εσA T⁴,  R/R₀ = (T/T₀)^1.209` |
| Columns | `voltage_V`, `current_A` (one row per reading; `#` lines are comments) |
| You enter | Cold filament resistance R₀ (Ω) (default 1.6); Room temperature T₀ (K) (default 293); Meter precision (%) (default 0.5) |
| Physics code | [`sandbox/tools/bench_classical.py`](../../sandbox/tools/bench_classical.py), fitted inside the glovebox |
| Fault library | [`faults/bench_classical.yaml`](../../faults/bench_classical.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `stefan_lamp` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Ammeter zero not set (reads current with none flowing) | 12 mA too much on a 0.2–0.5 A lamp makes the power high and the temperature low at the cold end; the exponent falls to about 3.8 | Zero the ammeter with the circuit open (or subtract its open-circuit reading from every current) and refit. |
| Heat lost by conduction through the filament supports | Power ∝ T⁴ plus a term ∝ (T − T₀); it matters most at the cold end and pulls the exponent below 4 | Fit only the hottest points (above about 1800 K), or fit P = aT⁴ + G(T − T₀) and quote the exponent of the radiated part. |
| Voltage read at the supply, so the leads and ammeter count as lamp | 1.5 Ω of leads and ammeter makes R and P too high at the cold end; the exponent rises above 4 | Connect the voltmeter directly across the lamp's terminals (four-wire) and repeat the sweep. |
| Unknown cause (none of the above fits well) |  | Measure the cold resistance on a four-wire meter, check the room temperature and let each point settle before reading. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read the ammeter with the lamp circuit open | 2 | Switch the supply off, disconnect the lamp and take ten readings of the ammeter, which should read zero. *Safety:* Switch off the supply before rewiring; mains-powered bench supplies stay live inside, so keep their covers on. |
| Measure the radiated power directly with a thermopile | 12 | Put a thermopile radiation sensor a fixed distance from the lamp and repeat the sweep; its signal is radiation only. *Safety:* The bulb gets hot enough to burn; don't touch the glass, and let it cool before moving the sensor. |
| Move the voltmeter leads onto the lamp's own terminals | 2 | At full voltage, compare the reading at the supply with the reading across the lamp itself. *Safety:* The bulb gets hot enough to burn; keep your hands off the glass while the lamp is on. |

### Samples on the page

- **Exponent below 4, worst when cold**: [`stefan_ammeter_zero.csv`](../../data/seeded/stefan_ammeter_zero.csv). The exponent comes out about 3.8, not 4: power ÷ T⁴ climbs at the cold end, by about a fifth at the coldest point.
- **Exponent above 4**: [`stefan_supply_voltage.csv`](../../data/seeded/stefan_supply_voltage.csv). The exponent comes out about 4.3, above 4: power ÷ T⁴ falls away at the cold end.
- **Healthy measurement**: [`stefan_clean.csv`](../../data/seeded/stefan_clean.csv). Nothing should look off: power follows T⁴ over 1200–2700 K.
- Sample result of *Read the ammeter with the lamp circuit open*: [`stefan_ammeter_open.csv`](../../data/seeded/stefan_ammeter_open.csv)

### The demo case

1. **Exponent below 4, worst when cold** ([`stefan_ammeter_zero.csv`](../../data/seeded/stefan_ammeter_zero.csv)): the leading cause is *Ammeter zero not set (reads current with none flowing)* at 53%, with *Heat lost by conduction through the filament supports* at 45%.
2. Recommended test: **Read the ammeter with the lamp circuit open** (2 min, 0.99 bits).
3. With its result ([`stefan_ammeter_open.csv`](../../data/seeded/stefan_ammeter_open.csv)): *Ammeter zero not set (reads current with none flowing)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`stefan_lamp/`](stefan_lamp/)); each gives the result above. [Excel export](stefan_lamp/excel_export.csv) · [Semicolons, decimal commas](stefan_lamp/semicolon_decimal_comma.csv) · [Tab-separated](stefan_lamp/tab_separated.tsv) · [UTF-16 "Unicode text"](stefan_lamp/unicode_text.txt) · [Other column names](stefan_lamp/other_column_names.csv)

## Thermal conductivity (Lee's disc)

Steady temperatures either side of a thin poor conductor, then the brass disc's cooling curve, to measure k.

| | |
| --- | --- |
| Model | `k = m c (dT/dt)\|T₂ · x / (A (T₁ − T₂))` |
| Columns | `stage`, `time_s`, `steam_C`, `disc_C` (one row per reading; `#` lines are comments) |
| You enter | Expected conductivity k (W/m·K) (default 0.19); Sample thickness x (mm) (default 3); Disc diameter (mm) (default 110); Brass disc heat capacity m·c (J/K) (default 335); Thermometer precision (K) (default 0.1) |
| Physics code | [`sandbox/tools/bench_fundamentals.py`](../../sandbox/tools/bench_fundamentals.py), fitted inside the glovebox |
| Fault library | [`faults/bench_fundamentals.yaml`](../../faults/bench_fundamentals.yaml) |
| Evaluation | 6 seeded cases in `data/manifest*` |
| Key | `lees_disc` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| The two thermometers disagree (calibration offset between them) | T₁ − T₂ is only about 15 K, so a 1.8 K offset between the thermocouples moves k by about 11% | Read both thermometers side by side in the steam (or a stirred bath), correct one by the measured difference, and recompute T₁ − T₂. |
| Steady state not reached (disc still warming when T₂ was read) | The disc settles with a time constant of about 8 minutes; reading T₂ 1.5 K short of its final value makes k about 12% low | Log T₁ and T₂ every minute and take them only once neither has moved by 0.1 K for ten minutes, then redo the cooling run around the new T₂. |
| Disc cooled with its top face bare (sample not put back on top for the cooling run) | A bare top face roughly doubles the disc's heat loss, so k comes out 50–100% high | Repeat the cooling run with the sample (or an insulating disc like it) on top, or scale the cooling rate by the exposed areas, (r + 2h)/(2r + 2h). |
| Unknown cause (none of the above fits well) |  | Measure the sample's thickness at several points, check the contact (a smear of heat-sink paste) and repeat. |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read both thermometers side by side in the steam chamber | 3 | Take the disc thermocouple out of the brass disc, put it next to the steam-side one in the steam chamber, and read both together eight times. *Safety:* Steam scalds. Turn the steam down while you move the thermocouple, keep your hand off the chamber's vent, and handle the hot brass with tongs or gloves. |
| Log T₁ and T₂ every minute for ten more minutes | 10 | Leave the steam on and the sample in place, and note both temperatures every minute. *Safety:* Steam scalds; keep the steam generator's water topped up so it doesn't boil dry, and keep the outlet tube pointing away from people. |
| Repeat the cooling run with the sample back on top of the disc | 15 | Reheat the brass disc about 8 K above T₂, put the sample (or an identical insulating disc) on top, and log the cooling every 30 s through T₂. *Safety:* The brass disc is at 90 °C or more; move it only with tongs or heat-proof gloves. |

### Samples on the page

- **Conductivity 10% low**: [`leesdisc_thermometer_offset.csv`](../../data/seeded/leesdisc_thermometer_offset.csv). The cooling curve looks normal, but k comes out about 10% below 0.19 W/m·K.
- **Conductivity almost twice the expected**: [`leesdisc_top_bare.csv`](../../data/seeded/leesdisc_top_bare.csv). The disc cools about twice as fast as the steady state implies: k comes out almost double 0.19 W/m·K.
- **Healthy measurement**: [`leesdisc_clean.csv`](../../data/seeded/leesdisc_clean.csv). Nothing should look off: k = 0.19 W/m·K, the table value for Perspex.
- Sample result of *Read both thermometers side by side in the steam chamber*: [`leesdisc_thermometer_offset_sidebyside.csv`](../../data/seeded/leesdisc_thermometer_offset_sidebyside.csv)

### The demo case

1. **Conductivity 10% low** ([`leesdisc_thermometer_offset.csv`](../../data/seeded/leesdisc_thermometer_offset.csv)): the leading cause is *The two thermometers disagree (calibration offset between them)* at 53%, with *Steady state not reached (disc still warming when T₂ was read)* at 45%.
2. Recommended test: **Read both thermometers side by side in the steam chamber** (3 min, 0.99 bits).
3. With its result ([`leesdisc_thermometer_offset_sidebyside.csv`](../../data/seeded/leesdisc_thermometer_offset_sidebyside.csv)): *The two thermometers disagree (calibration offset between them)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`lees_disc/`](lees_disc/)); each gives the result above. [Excel export](lees_disc/excel_export.csv) · [Semicolons, decimal commas](lees_disc/semicolon_decimal_comma.csv) · [Tab-separated](lees_disc/tab_separated.tsv) · [UTF-16 "Unicode text"](lees_disc/unicode_text.txt) · [Other column names](lees_disc/other_column_names.csv)

## Thermocouple calibration (type K)

Emf of a type K thermocouple against its hot junction's temperature, reference junction in ice, to measure its Seebeck coefficient.

| | |
| --- | --- |
| Model | `emf = S(T − T_ref) + q(T − T_ref)²,  S ≈ 41 µV/K` |
| Columns | `hot_junction_C`, `emf_mV` (one row per reading; `#` lines are comments) |
| You enter | Reference junction temperature (°C) (default 0); Emf reading precision (mV) (default 0.01); Bath thermometer precision (°C) (default 0.2) |
| Physics code | [`sandbox/tools/bench_optics2.py`](../../sandbox/tools/bench_optics2.py), fitted inside the glovebox |
| Fault library | [`faults/bench_optics2.yaml`](../../faults/bench_optics2.yaml) |
| Evaluation | 4 seeded cases in `data/manifest*` |
| Key | `thermocouple` |

### What goes wrong on this bench

| Cause | Typical size | Fix |
| --- | --- | --- |
| Reference junction not at 0 °C (ice melted, or the junction out of the ice) | Each kelvin the reference sits above 0 °C takes about 39 µV off every reading; ice melted to 8 °C water makes them all 0.32 mV low | Refill the flask with crushed ice and a little water, stir, push the reference junction well down into it and check a thermometer there reads 0 °C, then repeat. |
| Voltmeter zero offset on its millivolt range | A meter not zeroed on its 200 mV range can read 0.1–0.3 mV with its input shorted, which shifts every emf by the same amount | Zero the meter with its input shorted (or subtract the shorted reading from every emf), then refit. |
| Wrong thermocouple type (a type J, iron–constantan, read as type K) | Type J gives about 54 µV/K over 25–200 °C against type K's 41, so every emf is 28–32% high and the curve's shape differs too | Identify the thermocouple from its colours and the magnet test, then fit it against its own reference table (or fetch a type K) and repeat. |
| Thermocouple legs connected the wrong way round (the emf comes out negative) | Swapping the legs at the meter or at the reference junction flips the sign: −4.1 mV at 100 °C instead of +4.1 mV | Reconnect so the magnetic (alumel, negative) leg goes through the reference junction to the meter's − terminal, then repeat. |
| Hot junction not in good thermal contact with the bath (reads low at high temperature) | A bead touching the beaker wall or barely under the oil can sit 5% of the way back towards room temperature: 9 K low at 200 °C | Tie the junction to the thermometer's bulb with fine wire, push both well under the stirred oil away from the walls, and let each reading settle before taking it. |
| Unknown cause (none of the above fits well) |  | Check the bath thermometer against the ice point and the steam point, and look for a joint of a third metal in either leg (a screw terminal or a solder joint away from the junctions). |

### Bench tests it can recommend

Chosen by expected information per minute of bench time, among the causes still in the running.

| Test | Minutes | What you do |
| --- | --- | --- |
| Read a thermometer in the reference flask | 1 | Stir the reference flask and read a thermometer held beside the reference junction, six times a few seconds apart. Crushed ice with a little water reads 0.0 °C. *Safety:* The oil bath on the hot plate reaches 200 °C. Keep the ice flask and your arms clear of it, never let water or ice get into the hot oil (it spits violently), and wear safety glasses. |
| Short the voltmeter's input and read it | 2 | Disconnect the thermocouple leads, join the meter's input terminals with a short copper wire, and take ten readings on the same range as the run. *Safety:* Lift the thermocouple out of the hot oil before unplugging it and lay it on a heat-proof mat, not on the bench or across its own leads. |
| Check the wire colours and test each leg with a magnet | 2 | Note the colours, then hold a small magnet against each leg in three places. In type K the negative leg (alumel) is pulled and the positive (chromel) is not. Log leg as +1 for the leg on the meter's + terminal and −1 for the other, and magnetic as 1 or 0. *Safety:* Test the legs only once the probe has cooled; the sheath and wires stay hot for a while after leaving 200 °C oil. |
| Push the hot junction deeper into the stirred oil and repeat the top temperatures | 5 | At the three hottest settings, read the emf as before, then with the junction tied against the thermometer bulb well under the oil (log deeper, 0 then 1), letting each reading settle. *Safety:* Oil at 200 °C burns. Move the junction with tongs or a clamp, wear heat-resistant gloves and safety glasses, and keep water away from the bath. |

### Samples on the page

- **Every emf 0.3 mV low**: [`thermocouple_ice_melted.csv`](../../data/seeded/thermocouple_ice_melted.csv). The slope matches type K, but every emf sits about 0.3 mV below the table.
- **Seebeck coefficient 30% high**: [`thermocouple_type_j.csv`](../../data/seeded/thermocouple_type_j.csv). The emf rises about 54 µV/K instead of 41, some 30% above the type K table, and doesn't quite follow its shape.
- **Healthy calibration**: [`thermocouple_clean.csv`](../../data/seeded/thermocouple_clean.csv). Nothing should look off: the emf follows the type K table, about 41 µV/K.
- Sample result of *Read a thermometer in the reference flask*: [`thermocouple_ice_melted_bath.csv`](../../data/seeded/thermocouple_ice_melted_bath.csv)

### The demo case

1. **Every emf 0.3 mV low** ([`thermocouple_ice_melted.csv`](../../data/seeded/thermocouple_ice_melted.csv)): the leading cause is *Reference junction not at 0 °C (ice melted, or the junction out of the ice)* at 56%, with *Voltmeter zero offset on its millivolt range* at 42%.
2. Recommended test: **Read a thermometer in the reference flask** (1 min, 0.99 bits).
3. With its result ([`thermocouple_ice_melted_bath.csv`](../../data/seeded/thermocouple_ice_melted_bath.csv)): *Reference junction not at 0 °C (ice melted, or the junction out of the ice)*, 93%, confirmed.

### Example upload files

The headline sample saved five ways ([`thermocouple/`](thermocouple/)); each gives the result above. [Excel export](thermocouple/excel_export.csv) · [Semicolons, decimal commas](thermocouple/semicolon_decimal_comma.csv) · [Tab-separated](thermocouple/tab_separated.tsv) · [UTF-16 "Unicode text"](thermocouple/unicode_text.txt) · [Other column names](thermocouple/other_column_names.csv)
