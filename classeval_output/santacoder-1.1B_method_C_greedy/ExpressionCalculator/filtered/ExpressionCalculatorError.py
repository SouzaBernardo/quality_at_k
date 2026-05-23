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
            cur = self.postfix_stack.pop()
            if cur.isdigit():
                self.postfix_stack.append(cur)
            elif cur == "(":
                self.postfix_stack.append(cur)
            elif cur == ")":
                while self.postfix_stack and self.postfix_stack[-1]!= "(":
                    self.postfix_stack.pop()
                if self.postfix_stack:
                    self.postfix_stack.pop()
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1].isdigit():
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "()":
                while self.postfix_stack and self.postfix_stack[-1] in "()":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "+-*/":
                while self.postfix_stack and self.postfix_stack[-1] in "+-*/":
                    self.postfix_stack.pop()
                self.postfix_stack.append(cur)
            elif cur in "0123456789":
                while self.postfix_stack and self.postfix_stack[-1

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.postfix_stack = deque()
        for c in expression:
            if self.is_operator(c):
                self.postfix_stack.append(c)
            else:
                self.postfix_stack.append(c)


    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        return c in {'+', '-', '*', '/', '(', ')', '%'}


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
        if cur == "+" and peek == "-":
            return True
        elif cur == "-" and peek == "+":
            return True
        elif cur == "*" and peek == "/":
            return True
        elif cur == "/" and peek == "*":
            return True
        elif cur == "+" and peek == "*":
            return True
        elif cur == "*" and peek == "+":
            return True
        elif cur == "/" and peek == "-":
            return True
        elif cur == "-" and peek == "/":
            return True
        else:
            return False


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
            return first_value + second_value
        elif current_op == "-":
            return first_value - second_value
        elif current_op == "*":
            return first_value * second_value
        elif current_op == "/":
            return first_value / second_value
        elif current_op == "%":
            return first_value % second_value
        else:
            return first_value


    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        pass