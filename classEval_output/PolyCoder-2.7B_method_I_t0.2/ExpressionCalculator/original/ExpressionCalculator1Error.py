import re
from collections import deque
from decimal import Decimal
class ExpressionCalculator:  
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]



    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        if expression == "0":
            return 0.0
        elif expression == "1":
            return 1.0
        elif expression == "2":
            return 2.0
        elif expression == "3":
            return 3.0
        elif expression == "4":
            return 4.0
        elif expression == "5":
            return 5.0
        elif expression == "6":
            return 6.0
        elif expression == "7":
            return 7.0
        elif expression == "8":
            return 8.0
        elif expression == "9":
            return 9.0
        elif expression == "10":
            return 10.0
        elif expression == "11":
            return 11.0
        elif expression == "12":
            return 12.0
        elif expression == "13":
            return 13.0
        elif expression == "14":
            return 14.0
        elif expression == "15":
            return 15.0
        elif expression == "16":
            return 16.0
        elif expression == "17":
            return 17.0
        elif expression == "18":
            return 18.0
        elif expression == "19":
            return 19.0
        elif expression == "20":
            return 20.0
        elif expression == "21":
            return 21.0
        elif expression == "22":
            return 22.0
        elif expression == "23":
            return 23.0
        elif expression == "24":
            return 24.0
        elif expression == "25":
            return 25.0
        elif expression == "26":
            return 26.0
        elif expression == "27":
            return 27.0
        elif expression == "28":
            return 28.0
        elif expression == "29":
            return 29.0
        elif expression == "30":
            return 30.0
        elif expression == "31":
            return 31.0
        elif expression == "32":
            return 32.0
        elif expression == "33":
            return 33.0
        elif expression == "34":
            return 34.0
        elif expression == "35":
            return 35.0
        elif expression == "36":
            return 36.0
        elif expression == "37":
            return 37.0
        elif expression == "38":
            return 38.0
        elif expression == "39":
            return 39.0
        elif expression == "40":
            return 40.0
        elif expression == "41":
            return 41.0
        elif expression == "42":
            return 42.0
        elif expression == "43":
            return 43.0
        elif expression == "44":
            return 44.0
        elif expression == "45":
            return 45.0
        elif expression == "46":
            return 46.0
        elif expression == "47":
            return 47.0
        elif expression == "48":
            return 48.0
        elif expression == "49":
            return 49.0
        elif expression == "50":
            return 50.0
        elif expression == "51":
            return 51.0
        elif expression == "52":
            return 52.0
        elif expression == "53":
            return 53.0
        elif expression == "54":
            return 54.0
        elif expression == "55":
            return 55.0
        elif expression == "56":
            return 56.0
        elif expression == "57":
            return 57.0
        elif expression == "58":
        









