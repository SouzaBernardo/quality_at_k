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
        # Convert the postfix expression to a list
        postfix_list = expression.split()

        # Initialize the operand stack
        operand_stack = deque()

        # Iterate through the list
        for token in postfix_list:
            # If the token is a number, push it to the operand stack
            if token.isdigit():
                operand_stack.append(float(token))
            # If the token is an operator,
            elif self.is_operator(token):
                # Pop two operands from the operand stack
                second_value = operand_stack.pop()
                first_value = operand_stack.pop()
                # Perform the operation on the two operands and push the result back to the operand stack
                result = self._calculate(first_value, second_value, token)
                operand_stack.append(result)
            # If the token is an operand,
            else:
                operand_stack.append(token)

        # The final result is the top element in the operand stack
        return operand_stack.pop()


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.postfix_stack = deque(self.transform(expression))





    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        Decimal('5')

        """
        if current_op == '+':
            return Decimal(first_value) + Decimal(second_value)
        elif current_op == '-':
            return Decimal(first_value) - Decimal(second_value)
        elif current_op == '*':
            return Decimal(first_value) * Decimal(second_value)
        elif current_op == '/':
            return Decimal(first_value) / Decimal(second_value)
        elif current_op == '%':
            return Decimal(first_value) % Decimal(second_value)