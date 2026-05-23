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
        from math import pi, fabs
        return 1 - (1 / (2 * pi) * ((x - pi) ** 2) ** (3 / 2)) ** (-2)

    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator = TriCalculator()
        >>> tricalculator.factorial(5)
        120
        """
        from math import pi, fabs
        return a * (a * (a * (a * (a * (a * (a * pi) + pi) + pi) + pi) + pi) + pi) + pi



    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        from math import pi, fabs
        return 1 / (2 * pi) * ((x - pi) ** 2) ** (0.5) - 1 / (2 * pi) * fabs((x - pi) ** 2) ** (-0.5)