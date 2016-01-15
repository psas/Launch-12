"""Common data and constants from Launch 12
"""
from numpy import loadtxt, subtract, divide, multiply

# Pysical Constants
g_0 = 9.80665

# Liftoff time
t_0 = 117853569585227

# Mach at ~ km MSL, m/s
M = 330.0

# launch rail altitude
rail_alt = 1389.360

def ADIS_data():
    columns = loadtxt("../fc-data/ADIS.csv", delimiter=',', unpack=True)

    timestamp = columns[1]
    gyro_x, gyro_y, gyro_z  = columns[3:6]
    acc_x, acc_y, acc_z     = columns[6:9]
    mag_x, mag_y, mag_z     = columns[9:12]

    timestamp = subtract(timestamp, t_0)
    timestamp = divide(timestamp, 1.0e9)

    return timestamp, gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z, mag_x, mag_y, mag_z

def Venus_data():

    columns = loadtxt("../fc-data/V8A8.csv", delimiter=',', unpack=True)

    seqn = columns[0]
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
