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
        if self.is_operator(expression):
            return self.calculate_operator(expression)
        elif self.is_operator(expression.lower()):
            return self.calculate_operator(expression.lower())
        elif self.is_operator(expression.upper()):
            return self.calculate_operator(expression.upper())
        elif self.is_operator(expression.add()):
            return self.calculate_operator(expression.add())
        elif self.is_operator(expression.subtract()):
            return self.calculate_operator(expression.subtract())
        elif self.is_operator(expression.multiply()):
            return self.calculate_operator(expression.multiply())
        elif self.is_operator(expression.divide()):
            return self.calculate_operator(expression.divide())
        elif self.is_operator(expression.modulo()):
            return self.calculate_operator(expression.modulo())
        elif self.is_operator(expression.and_()):
            return self.calculate_operator(expression.and_())
        elif self.is_operator(expression.or_()):
            return self.calculate_operator(expression.or_())
        elif self.is_operator(expression.xor_()):
            return self.calculate_operator(expression.xor_())
        elif self.is_operator(expression.left_shift()):
            return self.calculate_operator(expression.left_shift())
        elif self.is_operator(expression.right_shift()):
            return self.calculate_operator(expression.right_shift())
        elif self.is_operator(expression.left_add()):
            return self.calculate_operator(expression.left_add())
        elif self.is_operator(expression.right_add()):
            return self.calculate_operator(expression.right_add())
        elif self.is_operator(expression.left_subtract()):
            return self.calculate_operator(expression.left_subtract())
        elif self.is_operator(expression.right_subtract()):
            return self.calculate_operator(expression.right_subtract())
        elif self.is_operator(expression.left_multiply()):
            return self.calculate_operator(expression.left_multiply())
        elif self.is_operator(expression.right_multiply()):
            return self.calculate_operator(expression.right_multiply())
        elif self.is_operator(expression.left_divide()):
            return self.calculate_operator(expression.left_divide())
        elif self.is_operator(expression.right_divide()):
            return self.calculate_operator(expression.right_divide())
        elif self.is_operator(expression.left_modulo()):
            return self.calculate_operator(expression.left_modulo())
        elif self.is_operator(expression.right_modulo()):
            return self.calculate_operator(expression.right_modulo())
        elif self.is_operator(expression.left_and()):
            return self.calculate_operator(expression.left_and())
        elif self.is_operator(expression.right_and()):
            return self.calculate_operator(expression.right_and())
        elif self.is_operator(expression.left_or()):
            return self.calculate_operator(expression.left_or())
        elif self.is_operator(expression.right_or()):
            return self.calculate_operator(expression.right_or())
        elif self.is_operator(expression.left_xor()):
            return self.calculate_operator(expression.left_xor())
        elif self.is_operator(expression.right_xor()):
            return self.calculate_operator(expression.right_xor())
        elif self.is_operator(expression.left_left_shift()):
            return self.calculate_operator(expression.left_left_shift())
        elif self.is_operator(expression.right_left_shift()):
            return self.calculate_operator(expression.right_left_shift())
        elif self.is_operator(expression.left_right_shift()):
            return self.calculate_operator(expression.left_right_shift())
        elif self.is_operator(expression.right_right_shift()):
            return self.calculate_operator(expression.right_right_shift())
        elif self.is_operator(expression.left_left_add()):
            return self.calculate_operator(expression.left_left_add())
        elif self.is_operator(expression.right_left_add()):
            return self.calculate_operator(expression.right_left_add())
        elif self.is_operator(expression.left_right_add()):
         

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.prepare_postfix(expression)


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
        if self.is_operator(peek):
            return True
        elif self.is_operator(cur):
            return False
        elif self.is_operator(peek) and self.is_operator(cur):
            return self.compare(cur, peek)
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
        if not expression:
            return ""
        if expression[0] == "+":
            return expression[1:]
        if expression[0] == "-":
            return expression[1:]
        if expression[0] == "*":
            return expression[1:]
        if expression[0] == "/":
            return expression[1:]
        if expression[0] == "^":
            return expression[1:]
        if expression[0] == "**":
            return expression[1:]
        if expression[0] == "==":
            return expression[1:]
        if expression[0] == "!=":
            return expression[1:]
        if expression[0] == ">=":
            return expression[1:]
        if expression[0] == "<=":
            return expression[1:]
        if expression[0] == ">=":
            return expression[1:]
        if expression[0] == "<":
            return expression[1:]
        if expression[0] == "in":
            return expression[1:]
        if expression[0] == "not in":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not in":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]
        if expression[0] == "is":
            return expression[1:]
        if expression[0] == "is not":
            return expression[1:]