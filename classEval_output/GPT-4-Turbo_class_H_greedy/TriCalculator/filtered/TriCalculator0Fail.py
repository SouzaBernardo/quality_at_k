from math import pi, fabs

class TriCalculator:
    """
    The class allows to calculate trigonometric values, including cosine, sine, and tangent, using Taylor series approximations.
    """

    def __init__(self):
        pass

    def cos(self, x):
        """
        Calculate the cos value of the x-degree angle
        :param x:float
        :return:float
        """
        x = x * (pi / 180)  # convert to radians
        sum = 0.0
        term = 1.0
        for i in range(1, 100):
            sum += term
            term *= -x * x / (2 * i * (2 * i - 1))
        return sum

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
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
        """
        x = x * (pi / 180)  # convert to radians
        sum = 0.0
        term = 1.0
        for i in range(1, n+1):
            sum += term
            term *= -x * x / (2 * i * (2 * i - 1))
        return sum

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        return self.cos(90 - x)

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        """
        return self.sin(x) / self.cos(x)