import re
from collections import deque
from decimal import Decimal
class ExpressionCalculator: 
    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]



    def calculate(self, expression):


    def prepare(self, expression):
        
        expression = self.transform(expression)
        for c in expression:
            if self.is_operator(c):
                while len(self.postfix_stack) > 0 and self.compare(c, self.postfix_stack[-1]):
                    self.postfix_stack.pop()
                self.postfix_stack.append(c)
            else:
                self.postfix_stack.append(c)


@staticmethod
    def is_operator(c):


    def compare(self, cur, peek):


@staticmethod
    def _calculate(first_value, second_value, current_op):


@staticmethod
    def transform(expression):
        
        return re.sub(r"\s+", "", expression)
