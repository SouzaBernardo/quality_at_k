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
        x = fabs(x) % 360
        if x == 0:
            return 1.0
        elif x == 180:
            return -1.0
        else:
            sinx = self.sin(x)
            return sinx / (1.0 + sinx)



    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        """
        x = x / 180 * pi
        result = 1.0
        for i in range(1, n+1):
            result -= (x ** i) / factorial(i)
        return result

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        """
        x = x / 180 * pi
        result = 0.0
        for i in range(1, 100):
            result += self.taylor(x, i) / factorial(i)
        return result