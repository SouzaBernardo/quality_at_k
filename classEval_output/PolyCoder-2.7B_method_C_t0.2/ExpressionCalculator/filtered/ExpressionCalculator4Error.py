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
        return self.calculate_result()


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
            return self._calculate(cur, peek, self.calculate(peek))
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
            return self.calculate(first_value + second_value)
        elif current_op == "-":
            return self.calculate(first_value - second_value)
        elif current_op == "*":
            return self.calculate(first_value * second_value)
        elif current_op == "/":
            return self.calculate(first_value / second_value)
        elif current_op == "**":
            return self.calculate(first_value ** second_value)
        elif current_op == "%":
            return self.calculate(first_value % second_value)
        elif current_op == ">>":
            return self.calculate(first_value >> second_value)
        elif current_op == "<<":
            return self.calculate(first_value << second_value)
        elif current_op == "&":
            return self.calculate(first_value & second_value)
        elif current_op == "^":
            return self.calculate(first_value ^ second_value)
        elif current_op == ">>":
            return self.calculate(first_value >> second_value)
        elif current_op == "<<":
            return self.calculate(first_value << second_value)
        elif current_op == ">>":
            return self.calculate(first_value >> second_value)
        elif current_op == "==":
            return self.calculate(first_value == second_value)
        elif current_op == "!=":
            return self.calculate(first_value!= second_value)
        elif current_op == ">=":
            return self.calculate(first_value >= second_value)
        elif current_op == "<=":
            return self.calculate(first_value <= second_value)
        elif current_op == "<":
            return self.calculate(first_value < second_value)
        elif current_op == ">":
            return self.calculate(first_value > second_value)
        elif current_op == "in":
            return self.calculate(first_value in second_value)
        elif current_op == "not in":
            return self.calculate(first_value not in second_value)
        elif current_op == "is":
            return self.calculate(first_value is second_value)
        elif current_op == "is not":
            return self.calculate(first_value is not second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not":
            return self.calculate(first_value is not second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
            return self.calculate(first_value is not in second_value)
        elif current_op == "is not in":
     

    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        if expression == "":
            return ""
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):
            expression = expression[1:]
        if expression.endswith(")"):
            expression = expression[:-1]
        if expression.startswith("("):