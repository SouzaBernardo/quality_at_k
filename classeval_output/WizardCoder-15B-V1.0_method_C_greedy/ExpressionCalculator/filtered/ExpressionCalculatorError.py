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
        """
        # Prepare the postfix expression
        postfix_expression = self.prepare(expression)
        # Calculate the result of the postfix expression
        self.postfix_stack = deque()
        for c in postfix_expression:
            if self.is_operator(c):
                second_value = self.postfix_stack.pop()
                first_value = self.postfix_stack.pop()
                result = self._calculate(first_value, second_value, c)
                self.postfix_stack.append(result)
            else:
                self.postfix_stack.append(float(c))
        return self.postfix_stack.pop()

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        :return: list, the postfix expression
        """
        # Remove all spaces from the expression
        expression = expression.replace(" ", "")
        # Convert the infix expression to postfix notation
        postfix_expression = []
        operator_stack = deque()
        for char in expression:
            if self.is_operator(char):
                while (operator_stack and self.compare(char, operator_stack[-1]) == 1):
                    postfix_expression.append(operator_stack.pop())
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1]!= '(':
                    postfix_expression.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            else:
                postfix_expression.append(char)
        while operator_stack:
            postfix_expression.append(operator_stack.pop())
        self.postfix_stack = postfix_expression
        return postfix_expression

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
        """
        if cur == "(" or cur == ")":
            return False
        if peek == "(" or peek == ")":
            return True
        return self.operat_priority[self.OPERATORS.index(cur)] >= self.operat_priority[self.OPERATORS.index(peek)]