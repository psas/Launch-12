# Raw GPS Data From Launch 12

Files:

 - `igs18540.sp3` High quality ephemeris data of the GPS constellation during the day of the launch[1]
 - `JGPS@-32.041913222` Raw IQ data from approximately 32 seconds before launch to 4.6 seconds after launch. This includes sitting on the launch rail to liftoff and most of the motor burn.
 - `JGPS@04.559925043` Raw IQ data from approximately 4.6 seconds after launch to 34.7 seconds after launch. This is most of the flight from just before motor burnout to apogee

[1]: Ephemeris data from NOAA <http://www.ngs.noaa.gov/orbits/orbit_data.shtml>

**Note** The GPS data is almost complete, but not quite. There is a gap of about 1 ms between the two files. We believe the data in each file to be contiguous.


## Raw IQ Format

We used the Maxim MAX2769 GPS RF front-end chip at 4.092 MHz sampling rate, using 2 bit ADC (sign/magnitude).

This is stored 2 bits I, 2 bits Q, continuously in the file.

Example code that would read from `stdin` and convert to floating point representation

```c
#include <stdint.h>
#include <stdio.h>

/* Utility to convert bits to a float */
static float sign_magnitude(unsigned sign, unsigned magnitude)
{
	float value = magnitude ? 1 : 1.0/3.0;
	return sign ? -value : value;
}

int main(void)
{
    while(1)
    {
        // Grab one byte
        uint8_t buf;
        if(fread(&buf, sizeof(uint8_t), 1, stdin) != 1)
            break;

        // Read a nibble
        unsigned int j;
        for(j = 0; j < 2; ++j)
        {
            /* Each nibble contains, in order from MSB to LSB:
             * - real part followed by imaginary part
             * - older sample followed by newer sample */
            unsigned imag  = (buf >> (8 - j * 4 - 1)) & 1;
            unsigned isign = (buf >> (8 - j * 4 - 2)) & 1;
            unsigned qmag  = (buf >> (8 - j * 4 - 3)) & 1;
            unsigned qsign = (buf >> (8 - j * 4 - 4)) & 1;

            // Convert sample to an array (I, Q)
            float sample[2] = {
				sign_magnitude(isign, imag),
				sign_magnitude(qsign, qmag),
			};

            /* Do something with data here! */
        }
    }
    return 0;
}
```

See our [GPS](https://github.com/psas/gps) repo for code that does things with this raw data.
