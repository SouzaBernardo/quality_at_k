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
        
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]
        for i in expression.split():
            if i in "+-*/%":
                self.operate(i)
            else:
                self.postfix_stack.append(Decimal(i))
        return self.postfix_stack.pop()

    def operate(self, operat):
        
        if operat == "+":
            self.postfix_stack.append(self.postfix_stack.pop() + self.postfix_stack.pop())
        elif operat == "-":
            self.postfix_stack.append(-self.postfix_stack.pop() + self.postfix_stack.pop())
        elif operat == "*":
            self.postfix_stack.append(self.postfix_stack.pop() * self.postfix_stack.pop())
        elif operat == "/":
            self.postfix_stack.append(self.postfix_stack.pop() / self.postfix_stack.pop())
        elif operat == "%":
            self.postfix_stack.append(self.postfix_stack.pop() % self.postfix_stack.pop())
        else:
            raise ValueError("Invalid operat")


    def prepare(self, expression):
        
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]
        for i in expression.split():
            if i in "+-*/%":
                self.operate(i)
            else:
                self.postfix_stack.append(Decimal(i))


@staticmethod
    def is_operator(c):
        

        return c in "+-*/%"





@staticmethod
    def _calculate(first_value, second_value, current_op):
        
        if current_op == "+":
            return Decimal(first_value) + Decimal(second_value)
        elif current_op == "-":
            return Decimal(first_value) - Decimal(second_value)
        elif current_op == "*":
            return Decimal(first_value) * Decimal(second_value)
        elif current_op == "/":
            return Decimal(first_value) / Decimal(second_value)
        elif current_op == "%":
            return Decimal(first_value) % Decimal(second_value)
        else:
            raise ValueError("Invalid operat")


@staticmethod
    def transform(expression):
        
        expression = re.sub(r"\s+", "", expression)
        expression = re.sub(r"\*\*", "^", expression)
        expression = re.sub(r"\/\/", "//", expression)
        expression = re.sub(r"\+\+", "++", expression)
        expression = re.sub(r"--", "--", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\+", "++", expression)
        expression = re.sub(r"\-\-", "--", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression)
        expression = re.sub(r"\*\=", "*=", expression)
        expression = re.sub(r"\/\=", "/=", expression)
        expression = re.sub(r"\%\=", "%=", expression)
        expression = re.sub(r"\+\=", "+=", expression)
        expression = re.sub(r"\-\=", "-=", expression
