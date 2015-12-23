class PIDController:
    """A simple PID Controller
    """

    def __init__(self, p, i, d):
        self.kP = p
        self.kI = i
        self.kD = d
        self.target = 0
        self.lastError = 0
        self.integrator = 0
        self.integrator_max = 100
        self.integrator_min = -100

    def setTarget(self, newTarget):
        """Set the target (set point) for the PID to track
        """

        self.target = newTarget
        self.integrator = 0

    def step(self, currentValue):
        """Calculates the error and derives a desired output value.
        """

        # determine the error by simply looking at the difference between
        # current value and target value.
        error = self.target - currentValue

        # Build the output by summing the contributions of the
        # proportional, integral, and derivative models.
        proportional = self.kP * error
        integral = self.kI * self.integrator
        derivative = self.kD * (error - self.lastError)

        # clamp the integrator!
        if integral > self.integrator_max:
            integral = self.integrator_max
        elif integral < self.integrator_min:
            integral = self.integrator_min

        output = proportional + integral + derivative

        # Remember the error for the derivative model
        self.lastError = error

        # Add the error to the integral model
        self.integrator += error

        return output, proportional, integral, derivative
