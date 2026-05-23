
class Calculator:  
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }



    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        """
        try:
            left_operand, operator, right_operand = expression.split()
            left_operand = float(left_operand)
            right_operand = float(right_operand)
            operator_function = self.operators[operator]
            result = operator_function(left_operand, right_operand)
            return result
        except (ValueError, ZeroDivisionError):
            return None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator in ['+', '-']:
            return 1
        elif operator in ['*', '/']:
            return 2
        elif operator in ['^']:
            return 3
        else:
            return 0

