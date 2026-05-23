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
        if x < 0:
            raise ValueError("The input x must be non-negative")
        x = fabs(x)
        n = int(math.log(x) / math.log(2))
        return 2**n * (1 - (x**2)**(2**n)) / (1 - (x**2)**(2**n-1))


    def factorial(self, a):

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if x == 0:
            return 1
        if n == 1:
            return 1 - x**2 / (2 * (1 - x**2)**2)
        else:
            return 1 - x**2 / (2 * (1 - x**2)**2) + x**2 / (2 * (1 - x**2)**3) - x**4 / (24 * (1 - x**2)**4) + ...

    def sin(self, x):

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        if x < -1 or x > 1:
            raise ValueError("x must be between -1 and 1")
        x = fabs(x)
        return 1 - x**2 / (2 * n + 1) / 2
