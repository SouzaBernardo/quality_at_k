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
        from math import pi, fabs
        return pi / 2 - fabs(self.taylor(x, 1) / self.factorial(x))

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        from math import pi, fabs
        n = a ** 0.5
        return pi * (1 + pi ** 2) ** n * fabs(a ** n)