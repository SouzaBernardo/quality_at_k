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
        # Calculate the cos value
        cos_val = 0
        x_deg = x * pi / 180
        n = 10
        for n in range(1, n + 1):
            cos_val += ((-1)**n)*(x_deg**(2*n))/factorial(2*n)
        return cos_val





    def sin(self, x):
        """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.sin(30)
        0.5
        """
        # Calculate the sin value
        sin_val = 0
        x_deg = x * pi / 180
        n = 10
        for n in range(1, n + 1):
            sin_val += ((-1)**n)*(x_deg**(2*n+1))/factorial(2*n+1)
        return sin_val




    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.tan(45)
        1.6
        """
        # Calculate the tan value
        tan_val = 0
        x_deg = x * pi / 180
        n = 10
        for n in range(1, n + 1):
            tan_val += ((-1)**n)*(x_deg**(2*n))/factorial(2*n)
        return tan_val

    def tan(self, x):
        """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.tan(45)
        1.0
        """
        # Calculate the tan value
        tan_val = 0
        x_deg = x * pi / 180
        n = 10
        for n in range(1, n + 1):
            tan_val += ((-1)**n)*(x_deg**(2*n))/factorial(2*n)
        return tan_val