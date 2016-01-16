"""Common data and constants from Launch 12
"""
from numpy import loadtxt, subtract, divide
from scipy.signal import butter, lfilter

# Pysical Constants
g_0 = 9.80665

# Liftoff time
t_0 = 117853569585227

# Mach at ~ km MSL, m/s
M = 330.0

# launch rail altitude
rail_alt = 1389.360


class ADISData(object):
    """Store ADIS Data"""

    fs = 819.2

    def __init__(self, timestamp, gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z, mag_x, mag_y, mag_z):
        self.time = timestamp
        self.gyro_x, self.gyro_y, self.gyro_z = gyro_x, gyro_y, gyro_z
        self.acc_x, acc_y, acc_z = acc_x, acc_y, acc_z
        self.mag_x, mag_y, mag_z = mag_x, mag_y, mag_z

        # Low pass for display
        # Filter requirements.
        order = 6
        cutoff = 20   # desired cutoff frequency of the filter, Hz
        nyq = 0.5 * self.fs
        normal_cutoff = cutoff / nyq

        # Get the filter coefficients so we can check its frequency response.
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        self.acc_x_filter = lfilter(b, a, self.acc_x)


def load_ADIS_data(source):
    columns = loadtxt(source, delimiter=',', unpack=True)

    timestamp = columns[1]
    gyro_x, gyro_y, gyro_z  = columns[3:6]
    acc_x, acc_y, acc_z     = columns[6:9]
    mag_x, mag_y, mag_z     = columns[9:12]

    timestamp = subtract(timestamp, t_0)
    timestamp = divide(timestamp, 1.0e9)

    return timestamp, gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z, mag_x, mag_y, mag_z


def Venus_data():

    columns = loadtxt("../fc-data/V8A8.csv", delimiter=',', unpack=True)

    timestamp = columns[1]
    fix_mode = columns[2]
    num_sv = columns[3]
    TOW = columns[5]
    latitude = columns[6]
    longitude = columns[7]
    altmsl = columns[9]
    GDOP = columns[10]
    PDOP = columns[1]
    HDOP = columns[13]
    VDOP = columns[14]
    TDOP = columns[15]
    vel_x = columns[18]
    vel_y = columns[19]
    vel_z = columns[20]

    timestamp = subtract(timestamp, t_0)
    timestamp = divide(timestamp, 1e9)

    return timestamp, fix_mode, num_sv, TOW, latitude, longitude, altmsl, GDOP, PDOP, HDOP, VDOP, TDOP, vel_x, vel_y, vel_z


def cached_altitude():
    columns = loadtxt("uncalibrated_integrated_altitude.csv", delimiter=',', unpack=True)
    alt_time = columns[0]
    imualt   = columns[1]

    return alt_time, imualt


def cached_velocity():
    columns = loadtxt("uncalibrated_integrated_velocity.csv", delimiter=',', unpack=True)
    vel_time = columns[0]
    imuvel   = columns[1]

    return vel_time, imuvel


# Load data!
adis = ADISData(*load_ADIS_data('../fc-data/ADIS.csv'))
