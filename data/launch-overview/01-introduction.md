\pagebreak

# Introduction

![](../../patch/L12_patch.png)\ Launch 12 was the 13th launch in Portland State Aerospace Society history. At 11:15 am, July 19th, 2015 the 34 kilogram [LV2](http://psas.github.io/rockets/#LV22) rocket was launched with a commercial CTI N2501-W solid rocket motor.

The launch was very successful. We launched earlier than usual and on the first try of the countdown. We met our main goals of a safe flight to the projected altitude, and had the smoothest ground systems setup and tear down to date for PSAS.

Approximately 40 GB of video and instrument data was collected during the flight.

## Instruments

This flight contained a full stack of our flight computer with many sensors on board collecting data. We also had a secondary experimental payload.

The primary instrument of our flight computer (and any flight computer) is inertial data. Our primary Inertial Measurement Unit (IMU) was the ADIS. We also had an pressure sensor, a GPS chip and a GPS experiment.

### ADIS

The ADIS is the Analog Devices ADIS16405 9 degree of freedom IMU. This device recored X,Y,Z acceleration, rotation rate, and local magnetic field at 819.2 Hz (every 1.22 ms).

### BMP

The Bosch BMP180 is a barometric pressure and temperature sensor.

### Venus8

The Venus8 is an off-the-shelf GPS chip.

### JGPS

The JGPS experiment was an experimental board that recored the raw radio signals in the GPS L1 band straight to disk at 4 million samples per second. This should allow us to reconstruct GPS position fixes after the flight and learn a lot about operating GPS devices on rockets.


## COTS Flight Computers

We also have data from the two commercial-off-the-shelf flight computers that control the parachute deployment. They usually consist of a microcontroller, and one or more sensors. They will close a circuit when apogee is detected and later at or below a fixed altitude. This is used to fire the pyros that open either a drouge parachute or a large main parachute.

### TeleMetrium

We also have a version 1 TeleMetrium device by AltusMetrum. It has pressure, single axis acceleration, GPS and a 70 cm HAM radio for live telemetry. This is our main recovery device.

### ARTS2

The ARTS2 is a simple recovery device by Ozark Aerospace. It has a single axis accelerometer and a pressure sensor.
