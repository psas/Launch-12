
# Magnetometer

The magnetic field sensor in the rocket is sensitive, but because the Earth's field is so weak it's easily overwhelmed by local effects (metal screws, magnetic fields from nearby wires, etc.). In order to get good orientation data we need to undo these local effects.

Before the flight we moved the rocket around in every direction to recored the magnetic field offset in each direction.

## Field Strength

First check, let's average the magnitude of the field and compare to what NOAA says it should have been for our location.

From [NOAA's magnetic field calculator](https://www.ngdc.noaa.gov/geomag/magfield.shtml)


 - Model Used: `WMM2015`
 - Latitude: `43.79613280° N`
 - Longitude: `120.65175340° W`
 - Elevation: `1390.0 m Mean Sea Level`

| Date | Declination (+E/-W) | Inclination (+D/-U) | Horizontal Intensity | North Comp (+N/-S) | East Comp (+E/-W) | Vertical Comp (+D/-U) | Total Field |
| ---- | ------------------- | ------------------- | -------------------- | ------------------ | -------------------- | --------------------- | ----------- | 
| 2015-07-17   | 14.7990° | 66.5386° | 20,754.1 nT | 20,065.7 nT | 5,301.2 nT | 47,819.4 nT | 52,129.0 nT | 
| Uncertainty  |    0.36° |    0.22° |      133 nT |      138 nT |      89 nT |      165 nT | 152 nT      |



Our average total field strength measured 58.95 μT, compared to NOAA's 52.129 ± 0.152 μT.



We can also run a time series of the data and see how it changes. The total field strength shouldn't change, even as we move the rocket around.




![](magnetometer_files/magnetometer_3_0.png)


It does change, because we have a big offset in some direction. The other way to look at this is a 3D plot of all the values. They _should_ land on a sphere, but instead it's an elongated ellipsoid.




![](magnetometer_files/magnetometer_5_0.png)


## Correction

The calibration takes two parts, moving the center of the magnetometer back to 0, and fixing the elongation.



Center offset (Hard Iron): `(11.275, 2.400, 1.975)`

Ellipsoid Correction Matrix (Soft Iron):

    |  0.87201  -0.12879  -0.28422 |
    | -0.12879   1.51323  -0.04663 |
    | -0.28422  -0.04663   1.44352 |







![](magnetometer_files/magnetometer_8_0.png)





![](magnetometer_files/magnetometer_9_0.png)


## Correcting The Flight Data

Using the above correction matrix we can fix the data from the flight.






![](magnetometer_files/magnetometer_12_0.png)





![](magnetometer_files/magnetometer_13_0.png)



