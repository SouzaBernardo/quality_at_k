
class ComplexCalculator: 
    def __init__(self):
        pass

    @staticmethod


    @staticmethod
    def add(c1, c2):
        """
        Adds two complex numbers.
        :param c1: The first complex number, complex.
        :param c2: The second complex number, complex.
        :return: The sum of the two complex numbers, complex.
        """
        return c1 + c2
    

    @staticmethod
    def subtract(c1, c2):
        """
        Subtracts two complex numbers.
        :param c1: The first complex number, complex.
        :param c2: The second complex number, complex.
        :return: The difference of the two complex numbers, complex.
        """
        return c1 - c2
    

    @staticmethod
    def multiply(c1, c2):
        """
        Multiplies two complex numbers.
        :param c1: The first complex number, complex.
        :param c2: The second complex number, complex.
        :return: The product of the two complex numbers, complex.
        """
        real_part = (c1.real * c2.real) - (c1.imag * c2.imag)
        imag_part = (c1.real * c2.imag) + (c1.imag * c2.real)
        return complex(real_part, imag_part)
    

    @staticmethod
    def divide(c1, c2):
        """
        Divides two complex numbers.
        :param c1: The first complex number, complex.
        :param c2: The second complex number, complex.
        :return: The quotient of the two complex numbers, complex.
        """
        real_part = (c1.real * c2.real + c1.imag * c2.imag) / (c2.real ** 2 + c2.imag ** 2)
        imag_part = (c2.real * c1.imag - c1.real * c2.imag) / (c2.real ** 2 + c2.imag ** 2)
        return complex(real_part, imag_part)
    