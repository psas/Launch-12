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
