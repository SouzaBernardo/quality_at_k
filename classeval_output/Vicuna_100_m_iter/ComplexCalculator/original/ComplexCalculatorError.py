
class ComplexCalculator:  
    """
    This is a class that implements addition, subtraction, multiplication, and division operations for complex numbers.
    """

    def __init__(self):
        pass

    @staticmethod


    def add(c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The sum of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """
        lhs = c1.real
        rhs = c2.real
        result_complex = c1.imag + c2.imag
        result_real = lhs + rhs
        return Complex(result_real, result_complex)

    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The difference of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)

        """
        lhs = c1.real
        rhs = c2.real
        result_complex = c1.imag - c2.imag
        result_real = lhs - rhs
        return Complex(result_real, result_complex)

    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The product of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.multiply(1+2j, 3+4j)
        (-5+10j)

        """
        lhs = c1.real
        rhs = c2.real
        result_complex = c1.imag * c2.imag - c1.real * c2.real
        result_real = lhs * rhs - lhs
        return Complex(result_real, result_complex)

    def divide(c1, c2):
        """
        Divides two complex numbers.
    
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The quotient of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)
    
        """
        lhs = c1.real
        rhs = c2.real
        result_complex = c1.imag / c2.imag
        result_real = lhs / rhs
        return Complex(result_real, result_complex)