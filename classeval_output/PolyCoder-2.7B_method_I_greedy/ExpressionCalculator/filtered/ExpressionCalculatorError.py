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
            return 0
        if expression[0] == "(":
            return self.calculate_expression(expression)
        if expression[0] == ")":
            return self.calculate_expression(expression)
        if expression[0] == "+":
            return self.calculate_expression(expression)
        if expression[0] == "-":
            return self.calculate_expression(expression)
        if expression[0] == "*":
            return self.calculate_expression(expression)
        if expression[0] == "/":
            return self.calculate_expression(expression)
        if expression[0] == "^":
            return self.calculate_expression(expression)
        if expression[0] == "**":
            return self.calculate_expression(expression)
        if expression[0] == "==":
            return self.calculate_expression(expression)
        if expression[0] == "!=":
            return self.calculate_expression(expression)
        if expression[0] == "<":
            return self.calculate_expression(expression)
        if expression[0] == "<=":
            return self.calculate_expression(expression)
        if expression[0] == ">":
            return self.calculate_expression(expression)
        if expression[0] == ">=":
            return self.calculate_expression(expression)
        if expression[0] == "==":
            return self.calculate_expression(expression)
        if expression[0] == "!=":
            return self.calculate_expression(expression)
        if expression[0] == "&&":
            return self.calculate_expression(expression)
        if expression[0] == "||":
            return self.calculate_expression(expression)
        if expression[0] == "**":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if expression[0] == "**=":
            return self.calculate_expression(expression)
        if