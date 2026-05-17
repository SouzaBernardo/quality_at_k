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
        if expression == "":
            return 0.0
        if expression[0] == "(":
            return self.calculate_subtraction(expression)
        if expression[0] == ")":
            return self.calculate_multiplication(expression)
        if expression[0] == "+":
            return self.calculate_addition(expression)
        if expression[0] == "-":
            return self.calculate_subtraction(expression)
        if expression[0] == "*":
            return self.calculate_multiplication(expression)
        if expression[0] == "/":
            return self.calculate_division(expression)
        if expression[0] == "%":
            return self.calculate_modulo(expression)
        if expression[0] == "**":
            return self.calculate_power(expression)
        if expression[0] == "==":
            return self.calculate_equality(expression)
        if expression[0] == "!=":
            return self.calculate_inequality(expression)
        if expression[0] == "<":
            return self.calculate_less_than(expression)
        if expression[0] == ">":
            return self.calculate_greater_than(expression)
        if expression[0] == "<=":
            return self.calculate_less_than_or_equal(expression)
        if expression[0] == ">=":
            return self.calculate_greater_than_or_equal(expression)
        if expression[0] == "in":
            return self.calculate_in(expression)
        if expression[0] == "not in":
            return self.calculate_not_in(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is":
            return self.calculate_is(expression)
        if expression[0] == "is not":
            return self.calculate_is_not(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is not in":
            return self.calculate_is_not_in(expression)
        if expression[0] == "is":
       









