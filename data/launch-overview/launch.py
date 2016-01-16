"""Common data and constants from Launch 12
"""
from numpy import loadtxt, subtract, divide
from math import sqrt
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


class BMP1Data(object):

    cal_AC1 = 408
    cal_AC2 = -72
    cal_AC3 = -14383
    cal_AC4 = 32741
    cal_AC5 = 32757
    cal_AC6 = 23153
    cal_B1 = 6190
    cal_B2 = 4
    cal_MB = -32767
    cal_MC = -8711
    cal_MD = 2868
    mode = 4

    def __init__(self, timestamp, pressure, temperature):
        self.time = timestamp
        self.pressure = pressure
        self.temperature = temperature

        # Fix up data
        pressures = []
        last_raw = 556878
        for i, t in enumerate(self.time):

            UT = int(self.temperature[i])
            UP = int(self.pressure[i])
            
            msb =  (UP & 0xff000000) >> (8*3)
            lsb =  (UP & 0x00ff0000) >> (8*2)
            xlsb = (UP & 0x0000ff00) >> (8*1)

            raw = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self.mode)
            #print "Data: 0x%x" % UP
            #print "MSB: 0x%x, LSB: 0x%x, xLSB: 0x%x" % (msb, lsb, xlsb)
            #print "Raw: 0x%x" % raw
            
            # dump gaps
            if abs(raw - last_raw) > 10000:
                raw = last_raw
            pressures.append(raw*(85.7/556878.0))
            last_raw = raw
            
            """
            X1 = ((UT - cal_AC6) * cal_AC5) >> 15
            X2 = (cal_MC << 11) / (X1 + cal_MD)
            
            B5 = X1 + X2
            #print 'B5 = {0}'.format(B5)
            
            # Pressure Calculations
            B6 = B5 - 4000
            #print 'B6 = {0}'.format(B6)
            
            X1 = (cal_B2 * (B6 * B6) >> 12) >> 11
            X2 = (cal_AC2 * B6) >> 11
            X3 = X1 + X2
            B3 = (((cal_AC1 * 4 + X3) << mode) + 2) / 4
            #print 'B3 = {0}'.format(B3)
            
            X1 = (cal_AC3 * B6) >> 13
            X2 = (cal_B1 * ((B6 * B6) >> 12)) >> 16
            X3 = ((X1 + X2) + 2) >> 2
            B4 = (cal_AC4 * (X3 + 32768)) >> 15
            #print 'B4 = {0}'.format(B4)
          
            B7 = (UP - B3) * (50000 >> mode)
            #print 'B7 = {0}'.format(B7)
            
            if B7 < 0x80000000:
                p = (B7 * 2) / B4
            else:
                p = (B7 / B4) * 2

            X1 = (p >> 8) * (p >> 8)
            X1 = (X1 * 3038) >> 16
            X2 = (-7357 * p) >> 16
            p = p + ((X1 + X2 + 3791) >> 4)
            """

        self.pressure = pressures
        temps = []
        for i, t in enumerate(self.time):
            UT = int(self.temperature[i])

            X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
            X2 = (self.cal_MC << 11) / (X1 + self.cal_MD)
            B5 = X1 + X2
            temp = ((B5 + 8) >> 4) / 10.0
            temps.append(temp)

        self.temperature = temps


def load_BMP1_data(source):
    columns = loadtxt(source, delimiter=',', unpack=True)
    timestamp = columns[1]
    pressure = columns[2]
    temperature = columns[3]

    timestamp = subtract(timestamp, t_0)
    timestamp = divide(timestamp, 1e9)
    return timestamp, pressure, temperature

def load_ADIS_data(source):
    columns = loadtxt(source, delimiter=',', unpack=True)

    timestamp = columns[1]
    gyro_x, gyro_y, gyro_z  = columns[3:6]
    acc_x, acc_y, acc_z     = columns[6:9]
    mag_x, mag_y, mag_z     = columns[9:12]

    timestamp = subtract(timestamp, t_0)
    timestamp = divide(timestamp, 1.0e9)

    return timestamp, gyro_x, gyro_y, gyro_z, acc_x, acc_y, acc_z, mag_x, mag_y, mag_z


class VenusData(object):

    def __init__(self, timestamp, fix_mode, num_sv, TOW, latitude, longitude, altmsl, GDOP, PDOP, HDOP, VDOP, TDOP, vel_x, vel_y, vel_z):
        self.time = timestamp
        self.fix_mode = fix_mode
        self.num_sv = num_sv
        self.TOW = TOW
        self.latitude = latitude
        self.longitude = longitude
        self.altmsl = altmsl
        self.GDOP = GDOP
        self.PDOP = PDOP
        self.HDOP = HDOP
        self.VDOP = VDOP
        self.TDOP = TDOP
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.vel_z = vel_z

        velocity = []
        for i, t in enumerate(self.time):
            v = sqrt((self.vel_x[i]*self.vel_x[i]) + (self.vel_y[i]*self.vel_y[i]) + (self.vel_z[i]*self.vel_z[i]))
            velocity.append(v)

        self.velocity = velocity

def load_Venus_data(source):

    columns = loadtxt(source, delimiter=',', unpack=True)

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
bmp1 = BMP1Data(*load_BMP1_data('../fc-data/BMP1.csv'))
venus = VenusData(*load_Venus_data('../full-flight/V8A8.csv'))
