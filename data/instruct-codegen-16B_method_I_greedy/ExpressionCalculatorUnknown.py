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
        """
        expression = expression.replace(" ", "")
        expression = re.sub(r'(\d+(?:\.\d*)?[*/+-^])', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-zA-Z]))(?= )', r' \1 ', expression)
        expression = re.sub(r'(?<= )(?:(\d+(?:\.\d*)?[*/+-^])|(?:[a-

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '
        """

        """

        """

        """

        """