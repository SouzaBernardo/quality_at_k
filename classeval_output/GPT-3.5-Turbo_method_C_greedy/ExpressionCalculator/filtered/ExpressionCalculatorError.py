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





    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        self.postfix_stack = deque()
        operator_stack = deque()
        expression = re.sub(r'\s+', '', expression)  # Remove whitespace from the expression
    
        i = 0
        while i < len(expression):
            if expression[i].isdigit():  # If the character is a digit, add it to the postfix stack
                num = ''
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                self.postfix_stack.append(num)
            elif self.is_operator(expression[i]):  # If the character is an operator
                while operator_stack and self.compare(expression[i], operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(expression[i])
                i += 1
            else:
                i += 1
    
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())
    
        return self.postfix_stack
    

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        operators = ['+', '-', '*', '/', '(', ')', '%']
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
        first_value = Decimal(first_value)
        second_value = Decimal(second_value)
        
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
        return re.sub(r'\s+', '', expression)