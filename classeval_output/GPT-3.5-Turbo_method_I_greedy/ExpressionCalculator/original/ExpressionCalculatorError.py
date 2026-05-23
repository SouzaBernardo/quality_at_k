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
        tokens = expression.split()
        stack = []
    
        for token in tokens:
            if token.isdigit():
                stack.append(Decimal(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
    
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                elif token == '/':
                    result = num1 / num2
                elif token == '%':
                    result = num1 % num2
    
                stack.append(result)
    
        return float(stack.pop())
    

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        operators = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
            '%': 1,
        }
        output_queue = []
        operator_stack = []
    
        tokens = re.findall(r'\d+|\+|\-|\*|\/|\%', expression)
    
        for token in tokens:
            if token.isdigit():
                output_queue.append(token)
            elif token in operators:
                while operator_stack and operators[token] <= operators[operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
    
        while operator_stack:
            output_queue.append(operator_stack.pop())
    
        self.postfix_stack = deque(output_queue)
    

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        return c in operators
    

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        cur_index = self.operat_priority.index(cur)
        peek_index = self.operat_priority.index(peek)
        
        return cur_index >= peek_index
    

@staticmethod
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
        if current_op == '+':
            result = Decimal(first_value) + Decimal(second_value)
        elif current_op == '-':
            result = Decimal(first_value) - Decimal(second_value)
        elif current_op == '*':
            result = Decimal(first_value) * Decimal(second_value)
        elif current_op == '/':
            result = Decimal(first_value) / Decimal(second_value)
        elif current_op == '%':
            result = Decimal(first_value) % Decimal(second_value)

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
        transformed_expression = re.sub(r'\s', '', expression)
        return transformed_expression
    