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
        self.compare(self.operat_priority[1], self.operat_priority[2])
        self.compare(self.operat_priority[2], self.operat_priority[3])
        self.compare(self.operat_priority[3], self.operat_priority[4])
        self.compare(self.operat_priority[4], self.operat_priority[5])
        self.compare(self.operat_priority[5], self.operat_priority[6])
        self.compare(self.operat_priority[6], self.operat_priority[7])
        self.compare(self.operat_priority[7], self.operat_priority[8])
        self.compare(self.operat_priority[8], self.operat_priority[9])
        self.compare(self.operat_priority[9], self.operat_priority[10])
        self.compare(self.operat_priority[10], self.operat_priority[11])
        self.compare(self.operat_priority[11], self.operat_priority[12])
        self.compare(self.operat_priority[12], self.operat_priority[13])
        self.compare(self.operat_priority[13], self.operat_priority[14])
        self.compare(self.operat_priority[14], self.operat_priority[15])
        self.compare(self.operat_priority[15], self.operat_priority[16])
        self.compare(self.operat_priority[16], self.operat_priority[17])
        self.compare(self.operat_priority[17], self.operat_priority[18])
        self.compare(self.operat_priority[18], self.operat_priority[19])
        self.compare(self.operat_priority[19], self.operat_priority[20])
        self.compare(self.operat_priority[20], self.operat_priority[21])
        self.compare(self.operat_priority[21], self.operat_priority[22])
        self.compare(self.operat_priority[22], self.operat_priority[23])
        self.compare(self.operat_priority[23], self.operat_priority[24])
        self.compare(self.operat_priority[24], self.operat_priority[25])
        self.compare(self.operat_priority[25], self.operat_priority[26])
        self.compare(self.operat_priority[26], self.operat_priority[27])
        self.compare(self.operat_priority[27], self.operat_priority[28])
        self.compare(self.operat_priority[28], self.operat_priority[29])
        self.compare(self.operat_priority[29], self.operat_priority[30])
        self.compare(self.operat_priority[30], self.operat_priority[31])
        self.compare(self.operat_priority[31], self.operat_priority[32])
        self.compare(self.operat_priority[32], self.operat_priority[33])
        self.compare(self.operat_priority[33], self.operat_priority[34])
        self.compare(self.operat_priority[34], self.operat_priority[35])
        self.compare(self.operat_priority[35], self.operat_priority[36])
        self.compare(self.operat_priority[36], self.operat_priority[37])
        self.compare(self.operat_priority[37], self.operat_priority[38])
        self.compare(self.operat_priority[38], self.operat_priority[39])
        self.compare(self.operat_priority[39], self.operat_priority[40])
        self.compare(self.operat_priority[40], self.operat_priority[41])
        self.compare(self.operat_priority[41], self.operat_priority[42])
        self.compare(self.operat_priority[42], self.operat_priority[43])
        self.compare(self.operat_priority[43], self.operat_priority[44])
        self.compare(self.operat_priority[44], self.operat_priority[45])
        self.compare(self.operat_priority[45], self.operat_priority[46])
        self.compare(self.operat_priority[46], self.operat_priority[47])
        self.compare(self.operat_priority[47], self.operat_priority[48])
        self.compare(self.operat_priority[48], self.operat_priority[49])
        self.compare(self.operat_priority[49], self.operat_priority[50])
        self.compare(self.operat_priority[50], self.operat_priority[51])
        self.compare(self.operat_priority[51], self.operat_priority[52])
        self.compare(self.operat_priority[52], self.operat_priority[53])
        self.compare(self.operat_priority[53], self.operat_priority

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
        if c in {'+', '-', '*', '/', '(', ')', '%'}:
            return True
        else:
            return False


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
            return self.compare(cur, self.operat_priority[peek])
        else:
            return self.compare(cur, self.postfix_stack.pop())


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
        elif current_op == ">>=":
            return first_value >> second_value
        elif current_op == ">>=":
            return first_value >> second_value
        elif current_op == ">>":
            return first_value >> second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":
            return first_value ** second_value
        elif current_op == "**=":
            return first_value ** second_value
        elif current_op == "**":

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
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "+")
        elif expression.startswith("-"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "-")
        elif expression.startswith("*"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "*")
        elif expression.startswith("/"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "/")
        elif expression.startswith("%"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "%")
        elif expression.startswith("**"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**")
        elif expression.startswith("**="):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=")
        elif expression.startswith("**=*"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=*")
        elif expression.startswith("**=/") or expression.startswith("**=*"):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=/")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):
            return ExpressionCalculator._calculate(expression[1:], expression[2:], "**=(")
        elif expression.startswith("**=("):