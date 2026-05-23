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
        try:
            tokens = expression.split()
            result = float(tokens[0])  # Initialize result with the first number
    
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                operand = float(tokens[i+1])
    
                if operator in self.operators:
                    result = self.operators[operator](result, operand)
                else:
                    raise ValueError("Invalid operator: {}".format(operator))
    
            return result
    
        except (IndexError, ValueError, ZeroDivisionError) as e:
            print("Error occurred during calculation:", e)
            return None
    

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator == '^':
            return 3
        elif operator in ['/', '*']:
            return 2
        elif operator in ['+', '-']:
            return 1
        else:
            return 0
    

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, and store the result at the top of the operand stack
        :param operand_stack: list, stack of operands
        :param operator_stack: list, stack of operators
        :return: tuple, updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
    
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
    
        return operand_stack, operator_stack