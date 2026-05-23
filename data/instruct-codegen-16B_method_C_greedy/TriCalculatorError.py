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
        # Calculate the cos value
        cos_val = 0
        x_deg = x * pi / 180
        n = 10
        for i in range(n):
            cos_val += (self.taylor(x_deg, i) * (pi/180)) / (self.factorial(2*i)*(2*i+1))
        return cos_val

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
        # Initialize the sum
        s = 0
        # Calculate the sum
        for i in range(n):
            s += (-1)**i * (x**(2*i+1)) / (self.factorial(2*i+1))
        # Return the result
        return s

    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
        # check if x is in radians
        if x > pi:
            x = x - 2 * pi
        elif x < -pi:
            x = x + 2 * pi
        
        # calculate the Taylor series
        sin_value = 0.0
        for i in range(1, n + 1):
            sin_value += (-1)**i * x**(2*i) / self.factorial(2*i)
        
        # return the sine value
        return sin_value

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
        return self.taylor(x, 2)