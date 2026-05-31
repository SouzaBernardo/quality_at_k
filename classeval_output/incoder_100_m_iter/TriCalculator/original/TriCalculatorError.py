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
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
        cos_value = math.cos(x)
        return cos_value


    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        factorial_value = math.factorial(a)
        return factorial_value


    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        taylor_value = self.factorial(n) / (self.factorial(n-1) * self.factorial(n-2) * math.factorial(n-3))
        taylor_value *= self.cos(x / 180 * pi)
        return taylor_value


    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        sin_value = math.sin(x)
        return sin_value


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        taylor_value = self.taylor(x, 3)
        tan_value = taylor_value / 2
        return tan_value

