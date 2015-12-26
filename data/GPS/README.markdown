# GPS Data

Files:

 - `igs18540.sp3` High quality ephemeris data of the GPS constellation during the day of the launch
 - `JGPS-@4.559925043` Gap fee raw data from a ~4.56 seconds after launch to ~34.7 seconds after launch. Includes

Ephemeris data from NOAA <http://www.ngs.noaa.gov/orbits/orbit_data.shtml>


## Dependencies

To read the published sp3 orbit data, we use GPSTk. To install GPSTk with python bindings:

Clone from github:

    $ git clone --depth 10 https://github.com/SGL-UT/GPSTk.git

Build and install with Python bindings

    $ cd GPSTk
    $ ./build.sh -eu


## Build This Document

Run all the IPython Notebooks and build report:

    $ make
