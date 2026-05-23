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
        # Initialize the expression calculator
        self.__init__()
    
        # Prepare the expression
        self.prepare(expression)
    
        # Get the first value and operator
        first_value = self.postfix_stack.pop()
        current_op = self.operat_priority[self.postfix_stack.pop()]
    
        # Perform the calculation
        result = self._calculate(first_value, current_op)
    
        # Transform the result
        self.transform(result)
    
        # Get the second value
        second_value = self.postfix_stack.pop()
    
        # Compare the second value with the result
        if second_value == "=" and self.compare(result, second_value) == 1:
            return result
        else:
            return None

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
    
        self.postfix_stack = [operand for operand, operator in zip(expression, expression[1:]) if operator.is_operator()]
        """
    
        operands = [operand for operand, operator in zip(expression, expression[1:]) if operator.is_operator()]
        self.postfix_stack = [operand for operand in operands]

    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True
    
        >>> expression_calculator.is_operator("*")
        True
    
        >>> expression_calculator.is_operator("-")
        True
    
        >>> expression_calculator.is_operator("/")
        True
    
        >>> expression_calculator.is_operator("(")
        True
    
        >>> expression_calculator.is_operator(")")
        True
    
        >>> expression_calculator.is_operator("%")
        True
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.is_operator("*")
        False
    
        >>> expression_calculator.



    def _calculate(self, first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        # code to implement the calculation logic
        pass

    def transform(expression):
        # Convert the infix expression to a postfix expression
        postfix_expression = convert_infix_to_postfix(expression)
    
        # Create a deque to store the postfix stack
        postfix_stack = deque()
    
        # Push the first token of the postfix expression onto the stack
        postfix_stack.append(postfix_expression.pop())
    
        # While there are still tokens left in the postfix expression
        while postfix_expression:
            # Get the next token from the postfix expression
            current_token = postfix_expression.pop()
    
            # If the next token is an operator, push the previous token onto the stack
            if current_token == '+':
                postfix_stack.append(postfix_stack.pop())
            elif current_token == '-':
                postfix_stack.append(postfix_stack.pop())
            elif current_token == '*':
                postfix_stack.append(postfix_stack.pop())
            elif current_token == '/':
                postfix_stack.append(postfix_stack.pop())
            elif current_token == '^':
                postfix_stack.append(postfix_stack.pop())
            else:
                # If the next token is a number, push it onto the stack
                postfix_stack.append(Decimal(current_token))
    
        # Convert the postfix stack to an infix expression
        infix_expression = convert_postfix_to_infix(postfix_stack)
    
        return infix_expression