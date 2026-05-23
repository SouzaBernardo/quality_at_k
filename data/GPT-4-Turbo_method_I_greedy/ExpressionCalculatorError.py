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
        operators = set(['+', '-', '*', '/', '%'])
        postfix_expression = deque()
        operand_stack = []
    
        # Convert infix expression to postfix
        for char in expression:
            if char not in operators:  # if it's an operand, add it to the postfix expression
                postfix_expression.append(char)
            else:
                while (len(operand_stack) != 0 and operand_stack[-1] != '(' and
                       self.operat_priority[operators.index(operand_stack[-1])] >= self.operat_priority[operators.index(char)]):
                    postfix_expression.append(operand_stack.pop())
                operand_stack.append(char)
    
        while len(operand_stack) != 0:
            postfix_expression.append(operand_stack.pop())
    
        # Evaluate the postfix expression
        for char in postfix_expression:
            if char not in operators:  # if it's an operand, push it to the stack
                operand_stack.append(Decimal(char))
            else:  # if it's an operator, pop two operands, do the calculation, and push back the result
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                result = 0
                if char == '+':
                    result = operand_1 + operand_2
                elif char == '-':
                    result = operand_1 - operand_2
                elif char == '*':
                    result = operand_1 * operand_2
                elif char == '/':
                    result = operand_1 / operand_2
                elif char == '%':
                    result = operand_1 % operand_2
                operand_stack.append(result)
    
        return float(operand_stack[0])
    
    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        operators = set(['+', '-', '*', '/', '%'])
        operand_stack = []
        postfix_expression = []
    
        for char in expression:
            if char not in operators:  # if it's an operand, add it to the postfix expression
                postfix_expression.append(char)
            else:
                while (len(operand_stack) != 0 and operand_stack[-1] != '(' and
                       self.operat_priority[operators.index(operand_stack[-1])] >= self.operat_priority[operators.index(char)]):
                    postfix_expression.append(operand_stack.pop())
                operand_stack.append(char)
    
        while len(operand_stack) != 0:
            postfix_expression.append(operand_stack.pop())
    
        self.postfix_stack = postfix_expression
    
    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        operators = set(['+', '-', '*', '/', '(', ')', '%'])
        return c in operators

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        operators = ['(', ')', '+', '-', '*', '/', '%']
        return self.operat_priority[operators.index(cur)] >= self.operat_priority[operators.index(peek)]
    def _calculate(self, first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        first_value = Decimal(first_value)
        second_value = Decimal(second_value)
    
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                raise ZeroDivisionError("division by zero")
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value
        else:
            raise ValueError("Invalid operator")
    def transform(self, expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        return expression.replace(" ", "")