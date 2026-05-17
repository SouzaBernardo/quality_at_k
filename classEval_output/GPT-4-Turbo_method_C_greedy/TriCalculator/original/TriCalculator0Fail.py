from math import pi, fabs
class TriCalculator: 
    def __init__(self):
        pass


    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        """
        x = x * (pi / 180)  # convert degrees to radians
        return self.taylor(x, 10)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        if a == 0:
            return 1
        else:
            return a * self.factorial(a-1)

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        x = x * pi / 180  # convert to radians
        sum = 0
        for i in range(n):
            term = ((-1)**i) * (x**(2*i)) / self.factorial(2*i)
            sum += term
        return sum

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x * (pi / 180)  # Convert degrees to radians
        return self.taylor(x, 10)

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        # Convert the angle to radians
        x = x * pi / 180

        # Calculate the sine and cosine of the angle using the Taylor series
        sin_x = self.taylor(x, 10)
        cos_x = self.taylor(x + pi/2, 10)

        # Return the tangent of the angle
        return sin_x / cos_x

