from math import pi, fabs
class TriCalculator: 
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
        return 1.0 - (1.0 - x) * (1.0 - x)


    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        if a < 0:
            return 0
        elif a == 0:
            return 1
        else:
            return a * self.factorial(a - 1)


    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return x * self.taylor(x, n - 1) / (n * self.factorial(n))


    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        return 0.5 * (1 + cos(x * pi / 180))


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        return 1.0 / (1.0 + x * x)
