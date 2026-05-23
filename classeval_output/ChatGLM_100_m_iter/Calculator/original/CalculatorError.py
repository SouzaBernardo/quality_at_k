
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
        :return:If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        try:
            result = self.operators[expression][0](self.operators[expression][1], self.operators[expression][2])
            return result
        except Exception as e:
            return None



    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        if len(operator_stack) == 0:
            return operand_stack, operator_stack
        top_result, top_operator = operand_stack[0]
        bottom_result, bottom_operator = operand_stack[-1]
        operator_result = self.operators[operator_operator][0](top_result, bottom_result)
        operator_stack.append(operator_result)
         operand_stack.pop()
        return operator_stack, top_operator