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
        self.postfix_stack = deque()
        self.postfix_stack.append(expression)
        while self.postfix_stack:
            token = self.postfix_stack.pop()
            if token.isdigit():
                self.postfix_stack.append(token)
            elif token == "(":
                self.postfix_stack.append(token)
            elif token == ")":
                while self.postfix_stack and self.postfix_stack[-1]!= "(":
                    self.postfix_stack.pop()
                if self.postfix_stack:
                    self.postfix_stack.pop()
            elif token in "+-*/":
                while self.postfix_stack and self.operat_priority[self.postfix_stack[-1]] >= self.operat_priority[token]:
                    self.postfix_stack.pop()
                self.postfix_stack.append(token)
            elif token == " ":
                pass
            else:
                raise ValueError("Invalid expression")
        return self.postfix_stack.pop()


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.postfix_stack = deque()
        for token in expression:
            if token.isdigit():
                self.postfix_stack.append(token)
            elif token == "(":
                self.postfix_stack.append(token)
            elif token == ")":
                while self.postfix_stack and self.postfix_stack[-1]!= "(":
                    self.postfix_stack.pop()
                if self.postfix_stack:
                    self.postfix_stack.pop()
            elif token in "+-*/":
                while self.postfix_stack and self.operat_priority[self.postfix_stack[-1]] >= self.operat_priority[token]:
                    self.postfix_stack.pop()
                self.postfix_stack.append(token)
            elif token == " ":
                pass
            else:
                raise ValueError("Invalid expression")



    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        return c in "+-*/()"



    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
        return self.operat_priority[cur] >= self.operat_priority[peek]




    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0

        """
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
            raise ValueError("Invalid operator")




    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)", r" \1 ", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?", r" \1 \2 ", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?([a-zA-Z%])", r" \1 \2 \3", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?([a-zA-Z%])([a-zA-Z%])", r" \1 \2 \3 \4", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])", r" \1 \2 \3 \4 \5", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])", r" \1 \2 \3 \4 \5 \6", expression)
        expression = re.sub(r"([0-9]+\.[0-9]*|[0-9]+)(e[+-]?[0-9]+)?([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])([a-zA-Z%])