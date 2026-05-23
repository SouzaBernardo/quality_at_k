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
        self.postfix_stack = []
        tokens = re.findall(r'[-+*/()]|\d+(\.\d+)?', expression)
        for token in tokens:
            if token.isdigit():
                self.postfix_stack.append(float(token))
            else:
                self.postfix_stack.append(token)
        self.postfix_notation(self.postfix_stack)
        return self.postfix_stack.pop()

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        self.postfix_stack = []
        output_queue = deque()
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        for token in re.findall(r'[-+*/()]|\d+(\.\d+)?', expression):
            if token.isdigit():
                output_queue.append(float(token))
            elif token in operators:
                while self.postfix_stack and self.postfix_stack[-1]!= '(' and operators[token] <= operators[self.postfix_stack[-1]]:
                    output_queue.append(self.postfix_stack.pop())
                self.postfix_stack.append(token)
            elif token == '(':
                self.postfix_stack.append(token)
            elif token == ')':
                while self.postfix_stack[-1]!= '(':
                    output_queue.append(self.postfix_stack.pop())
                self.postfix_stack.pop()
        while self.postfix_stack:
            output_queue.append(self.postfix_stack.pop())
        self.postfix_stack = list(output_queue)







    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        expression = expression.replace(' ', '')
        operators = {'+':'+ ', '-':'- ', '*':'* ', '/':'/ ', '%':'% '}
        for operator in operators:
            expression = expression.replace(operator, operators[operator])
        return expression