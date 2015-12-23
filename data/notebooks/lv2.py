"""Canard Aerodynamics
"""
from math import sin, cos, radians, exp, degrees, sqrt, fabs
import threading
import struct
import socket
import time

# Define PSAS wing:
k_p = 2.45
k_v = 3.2
Cl_base = 3.2
fin_area = 1.13e-3  # m^2
fin_arm = 0.085     # m

# Define LV2.3 Mass properties
I_0 = 0.086         # m^2 kg
I_1 = 0.077         # m^2 kg
burn_time = 5.6     # motor burn time in seconds

# store last fin angle
current_alpha = 0

# TICKS to fin angle 
PWM_TICKS_MAX = 56000
PWM_TICKS_MIN =  0
PWM_US_MAX = 3333
PWM_US_MIN =  0

MAX_SERVO_POSITION_US = 1900
MIN_SERVO_POSITION_US = 1100

MAX_SERVO_POSITION_TICKS = ( MAX_SERVO_POSITION_US * PWM_TICKS_MAX / PWM_US_MAX )
MIN_SERVO_POSITION_TICKS = ( MIN_SERVO_POSITION_US * PWM_TICKS_MAX / PWM_US_MAX )

MAX_CANARD_ANGLE = 15.0
MIN_CANARD_ANGLE = -15.0

PWM_TICKS_PER_DEGREE = (MAX_SERVO_POSITION_TICKS - MIN_SERVO_POSITION_TICKS) / (MAX_CANARD_ANGLE - MIN_CANARD_ANGLE)
PWM_TICKS_CENTER = MIN_SERVO_POSITION_TICKS - PWM_TICKS_PER_DEGREE * MIN_CANARD_ANGLE

def rho(alt):
    """Very basic exponential atmosphere model.

    :param alt: MSL altitude in meters
    :returns air density:
    """

    return 1.2250 * exp((-9.80665 * 0.0289644 * alt)/(8.31432*288.15))


def Izz(t):
    """Mass moment of inertia in the roll axis of the rocket. This changes as
    a function of time because the rocket motor burns and removes mass.
    """

    I = I_0

    if t <= 0:
        I = I_0
    if t < burn_time:
        I = I_0 + (I_1-I_0)*t/5.6
    else:
        I = I_1

    return I


def C_L(a, v):
    """Find C_L for a given speed and angle of attack

    :param float a: Angle of attack, alpha in degrees
    :param float v: velocity, v in m/s
    :returns float C_L (dimensionless):

    """

    # math is in radians
    a = radians(a)

    # Subsonic case
    def _subsonic():
        sina = sin(a)
        cosa = cos(a)
        cl = k_p*sina*cosa*cosa
        cl += k_v*cosa*sina*sina
        return cl

    # Supersonic case
    def _supersonic():
        cl = a*Cl_base
        return cl

    if v <= 265:
        return _subsonic()
    elif v < 330:
        # Intepolate between super and subsonic
        y0 = _subsonic()
        y1 = _supersonic()
        x0 = 265
        x1 = 330
        cl = y0 + (y1-y0)*(v - x0)/(x1-x0)
        return cl
    else:
        return _supersonic()


def lift(a, v, alt):
    """Compute the lift of one fin at an angle of
    attack, velocity, and altitdue

    :param float a: Angle of attack in degrees
    :param float v: velocity in m/s
    :param float alt: altitude MSL in meters
    :returns float lift in Newtons:

    """
    # lift
    l = 0.5*C_L(a, v)*rho(alt)*v*v*fin_area

    if(a < 0):
        return -l
    else:
        return l


def angular_accel(a, x, v, t):
    """Compute angular accelation for a single point

    :param a: Fin alpha (degrees)
    :param x: altitude (meters, MSL)
    :param v: air velocity (m/s)
    :param t: time since launch (seconds)
    :returns float angular acceleration in degrees/s^2:

    """

    aa = degrees((4*lift(a, v, x)*fin_arm)/Izz(t))

    if a < 0:
        return -aa
    return aa


def estimate_alpha(set_aa, x, v, t):
    """Return an estimated fin angle of attack for to
    achieve the required angular acceleration.

    :param aa: Angular acceleration to compute alpha for (degrees/s/s)
    :param x: Altitude (meters, MSL)
    :param v: Air velocity (m/s)
    :param t: Time (seconds since launch)
    :returns fin angle:

    """

    # obvious cases (and avoid divide by 0):
    if fabs(set_aa) < 1 or v < 1:
        return 0

    aa = fabs(radians(set_aa))

    # Fit Constants
    af = 0.0006
    bf = 0.045

    I = Izz(t)
    rd = rho(x)

    def _subsonic():
        alpha = sqrt(fabs(2*aa*I*af)/(rd*v*v*fin_area*fin_arm) + bf*bf) - bf
        alpha = alpha / (2*af)
        return alpha

    def _supersonic():
        alpha = (aa*I)/(2*rd*v*v*fin_area*fin_arm*Cl_base)
        return degrees(alpha)

    output = 0
    if v <= 265:
        output =  _subsonic()
    elif v < 330:
        # Intepolate between super and subsonic
        y0 = _subsonic()
        y1 = _supersonic()
        x0 = 265
        x1 = 330
        cl = y0 + (y1-y0)*(v - x0)/(x1-x0)
        output =  cl
    else:
        output =  _supersonic()

    if set_aa < 0:
        return -output
    return output


def servo(alpha, t):
    """Outputs canard fin position when requested by the flight computer

    :param alpha: requested canard angle in degrees
    :param t:     current time in seconds
    :returns actual canard angle in degrees:

    """

    global current_alpha

    t_ms = int(round(t * 1000))  # convert time to ms

    # servo only responds every 3.3ms
    if (t_ms % 3) == 0:
        current_alpha = alpha

    # clamp the output to only +/- 15deg
    if current_alpha > 15:
        current_alpha = 15
    if current_alpha < -15:
        current_alpha = -15

    return current_alpha


class Servo(threading.Thread):

    def __init__(self, q):
        from psas_packet import io, messages

        threading.Thread.__init__(self)
        self._stop = threading.Event()
        self.daemon = True
        self.queue = q

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 35003))
        self.sock.settimeout(0.5)
        self.net = io.Network(self.sock)

        self.decode = messages

    def run(self):
        while (not self._stop.is_set()):
            self.read()

    def stop(self):
        """Stop thread"""
        self._stop.set()
        self.join()
        self.sock.close()

    def read(self):
        SEQN = self.decode.MESSAGES['SEQN']
        st = struct.Struct("!HB")

        try:
            buff, addr = self.sock.recvfrom(1500)
        except socket.timeout:
            return

        timestamp = time.time()

        h = []
        for c in buff:
            h.append(str(hex(ord(c))))

        seqno = SEQN.decode(buff[:SEQN.size])
        buff = buff[SEQN.size:]
        tics, en = st.unpack(buff)

        tics = tics - PWM_TICKS_CENTER
        degrees = tics / PWM_TICKS_PER_DEGREE
        self.queue.put(degrees)
