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
        return self.taylor(x, 10)


    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        result = 1
        for i in range(1, a+1):
            result *= i
        return result
    

    def taylor(self, x, n):
        """
        Finding the n-order Taylor expansion value of cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
        x_rad = x / 180 * pi
        result = 0.0
        sign = 1

        for i in range(0, n+1):
            term = sign * (x_rad**(2*i)) / self.factorial(2*i)
            result += term
            sign *= -1

        return result


    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x * pi / 180  # Convert degrees to radians
        result = 0
        for i in range(10):  # Use 10 terms in the Taylor series approximation
            term = ((-1) ** i) * (x ** (2 * i + 1)) / self.factorial(2 * i + 1)
            result += term
        return result


    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        return self.sin(x) / self.cos(x)