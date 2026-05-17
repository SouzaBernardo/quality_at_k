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
        self.prepare(expression)
        self.compare(self.operat_priority[0], self.operat_priority[1])
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)
        self.calculate_postfix(expression)
        self.calculate_operat(expression)

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.prepare_postfix_stack()
        self.prepare_operat_priority()
        self.prepare_operator()
        self.prepare_expression(expression)


    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        if c == '+':
            return True
        elif c == '-':
            return False
        elif c == '*':
            return False
        elif c == '/':
            return False
        elif c == '(':
            return False
        elif c == ')':
            return False
        elif c == '%':
            return False
        else:
            return True


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
        if self.is_operator(peek):
            return True
        if self.is_operator(cur):
            return False
        if self.is_operator(peek) and self.is_operator(cur):
            return self.compare(cur, peek)
        if self.is_operator(cur):
            return self.compare(cur, peek)
        return self.compare(peek, cur)


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
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value
        elif current_op == ">>>=":
            return first_value >> second_value
        elif current_op == ">>>" or current_op == ">>":
            return first_value >> second_value


    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        if expression.startswith("+"):
            return ExpressionCalculator.calculate(expression) + " " + ExpressionCalculator.calculate(expression.lstrip(" + "))
        elif expression.startswith("-"):
            return ExpressionCalculator.calculate(expression) - " " + ExpressionCalculator.calculate(expression.lstrip(" - "))
        elif expression.startswith("*"):
            return ExpressionCalculator.calculate(expression) * " " + ExpressionCalculator.calculate(expression.lstrip(" * "))
        elif expression.startswith("/"):
            return ExpressionCalculator.calculate(expression) / " " + ExpressionCalculator.calculate(expression.lstrip(" / "))
        elif expression.startswith("%"):
            return ExpressionCalculator.calculate(expression) % " " + ExpressionCalculator.calculate(expression.lstrip(" % "))
        elif expression.startswith("!"):
            return ExpressionCalculator.calculate(expression)! " " + ExpressionCalculator.calculate(expression.lstrip("! "))
        elif expression.startswith("~"):
            return ExpressionCalculator.calculate(expression) ~ " " + ExpressionCalculator.calculate(expression.lstrip(" ~ "))
        elif expression.startswith("!~"):
            return ExpressionCalculator.calculate(expression)!~ " " + ExpressionCalculator.calculate(expression.lstrip("!~ "))
        elif expression.startswith("!~!"):
            return ExpressionCalculator.calculate(expression)!! " " + ExpressionCalculator.calculate(expression.lstrip("!~! "))
        elif expression.startswith("!~!~"):
            return ExpressionCalculator.calculate(expression)!!~ " " + ExpressionCalculator.calculate(expression.lstrip("!~!~ "))
        elif expression.startswith("!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~! "))
        elif expression.startswith("!~!~!~"):
            return ExpressionCalculator.calculate(expression)!!~!~ " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~ "))
        elif expression.startswith("!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~! "))
        elif expression.startswith("!~!~!~!~"):
            return ExpressionCalculator.calculate(expression)!!~!~!~ " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~ "))
        elif expression.startswith("!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~ "))
        elif expression.startswith("!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~!~!~!~!~! " " + ExpressionCalculator.calculate(expression.lstrip("!~!~!~!~!~! "))
        elif expression.startswith("!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!"):
            return ExpressionCalculator.calculate(expression)!!~!~!~!~!~!~!~