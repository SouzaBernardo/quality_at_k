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
        return self.sin(x + pi / 2)

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
        """
        if x == 0:
            return 1
        else:
            cos_x = 0
            for i in range(n):
                cos_x += (-1) ** i * (x / (2 * i + 1)) ** (2 * n) / self.factorial(2 * i + 1)
            return cos_x

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        if x == 0:
            return 0
        elif x == 90:
            return 1
        elif x == 180:
            return 0
        elif x == 270:
            return -1
        else:
            sign = 1
            if x < 0:
                sign = -1
                x = fabs(x)
            elif x > 180:
                x = 360 - x
            elif x > 90:
                sign = -1
                x = 180 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 135:
                sign = -1
                x = 270 - x
            elif x > 225:
                x = 360 - x
            elif x > 315:
                sign = -1
                x = 45 - x
            elif x > 360:
                x = 360 - x
            elif x > 45:
                x = 90 - x
            elif x > 

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        return self.sin(x) / self.cos(x)