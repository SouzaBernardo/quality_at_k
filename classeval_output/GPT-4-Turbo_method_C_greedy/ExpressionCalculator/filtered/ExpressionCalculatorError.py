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
        self.postfix_stack.clear()
        postfix_expression = self.transform(expression)
        for char in postfix_expression:
            if not self.is_operator(char):
                self.postfix_stack.append(Decimal(char))
            else:
                second_value = self.postfix_stack.pop()
                first_value = self.postfix_stack.pop()
                result = self._calculate(first_value, second_value, char)
                self.postfix_stack.append(result)
        return float(self.postfix_stack[0])
    
    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        operators = set(['+', '-', '*', '/', '(', ')', '^'])
        postfix = deque()
        stack = deque()
        for char in expression:
            if char not in operators:  # if character is not operator append it to output
                postfix.append(char)
            else:
                if char=='(':  # else operators push it to the stack
                    stack.append('(')
                elif char==')':
                    while stack and stack[-1]!= '(':
                        postfix.append(stack.pop())
                    stack.pop()
                else:
                    # lesser priority can't be on top on higher or equal priority    
                     # so pop and put in output   
                    while stack and stack[-1]!='(' and self.compare(char,stack[-1]):
                        postfix.append(stack.pop())
                    stack.append(char)
        while stack:
            postfix.append(stack.pop())
        self.postfix_stack = list(postfix)
    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '(', ')', '%'}
    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        operators = ['+', '-', '*', '/', '%', '(', ')', '^']
        cur_priority = self.operat_priority[operators.index(cur)]
        peek_priority = self.operat_priority[operators.index(peek)]
        return cur_priority >= peek_priority
    @staticmethod
    def _calculate(first_value, second_value, current_op):
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
                raise ZeroDivisionError("Cannot divide by zero")
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value
        else:
            raise ValueError("Invalid operator")
    
    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        # Remove all spaces from the expression
        transformed_expression = expression.replace(" ", "")
        return transformed_expression