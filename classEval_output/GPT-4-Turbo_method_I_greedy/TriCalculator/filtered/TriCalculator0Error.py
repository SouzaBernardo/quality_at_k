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
        x = x * (pi / 180)  # Convert to radians
        cos_approx = 0
        for i in range(10):  # Taylor Series up to 10th term
            term = ((-1)**i) * (x**(2*i)) / factorial(2*i)
            cos_approx += term
        return cos_approx

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
        x = x * (pi / 180)  # Convert to radians
        taylor_approx = 0
        for i in range(n):  # Taylor Series up to nth term
            term = ((-1)**i) * (x**(2*i)) / self.factorial(2*i)
            taylor_approx += term
        return taylor_approx
    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        x = x * (pi / 180)  # Convert to radians
        sin_approx = 0
        for i in range(10):  # Taylor Series up to 10th term
            term = ((-1)**i) * (x**(2*i + 1)) / self.factorial(2*i + 1)
            sin_approx += term
        return sin_approx
    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        x = x * (pi / 180)  # Convert to radians
        sin_approx = x
        cos_approx = 1
        for i in range(1, 10):  # Taylor Series up to 10th term
            sin_term = ((-1)**i) * (x**(2*i+1)) / self.factorial(2*i+1)
            cos_term = ((-1)**i) * (x**(2*i)) / self.factorial(2*i)
            sin_approx += sin_term
            cos_approx += cos_term
        tan_approx = sin_approx / cos_approx
        return tan_approx