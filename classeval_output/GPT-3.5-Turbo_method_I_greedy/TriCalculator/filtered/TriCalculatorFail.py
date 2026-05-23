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
        x = x * pi / 180  # Convert degrees to radians
        result = 1  # Initialize the result with the first term of the Taylor series

        # Calculate subsequent terms of the Taylor series
        for n in range(1, 10):
            term = (-1) ** n * (x ** (2 * n)) / (2 * n)
            result += term

        return result


    def factorial(self, a):
        """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
        result = 1  # Initialize the result with 1
    
        # Calculate the factorial using a loop
        for i in range(1, a + 1):
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
        x = x * pi / 180  # Convert degrees to radians
        cos_value = self.cos(x)  # Calculate the cosine value using the cos method
        factorial_value = self.factorial(n)  # Calculate the factorial value using the factorial method
        result = cos_value * factorial_value / (x ** n)  # Calculate the Taylor expansion value
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
        result = x  # Initialize the result with the first term of the Taylor series
    
        # Calculate subsequent terms of the Taylor series
        for n in range(1, 10):
            term = (-1) ** n * (x ** (2 * n + 1)) / self.factorial(2 * n + 1)
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
        sin_value = self.sin(x)  # Calculate the sine value using the sin method
        cos_value = self.cos(x)  # Calculate the cosine value using the cos method
        result = sin_value / cos_value  # Calculate the tangent value
        return result