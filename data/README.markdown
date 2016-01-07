# L-12 Launch Data

Raw flight computer data is in the `LAUNCH` directory. Subsystems and COTS FC data are in their respective named directories.

To unpack, make sure you have our packet decoding library installed

    $ pip install psas_packet

Then run

    $ make

to unpack the data into csv files for each instrument. You can now easily run the IPython notebooks and other analysis.

**Note about big data**. Because of file size limits, only the ~40 seconds of launch-to-apogee data is in this repository. 

To get the full data go to:

[annex.psas.pdx.edu/Launch-12/](http://annex.psas.pdx.edu/Launch-12/)

Download `flightcomputer.log` and `flightcomputer-calibration.log` to this directory and run

    $ make fullflight

## Analysis

 - [First Look](notebooks/first-look.md)
 - [Roll Control Effectiveness](notebooks/rollanalysis_part2.md)
 - [Geiger Counter](notebooks/geiger.md)
 - [Telemetry Quality](notebooks/telemetry-quality.md)
 - [COTS GPS Receiver](notebooks/venus8-gps.md)
 - [Missing Data And IMU Arrival Jitter](notebooks/seq_failure_timing_jitter.md)
