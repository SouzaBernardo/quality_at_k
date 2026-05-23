class Calculator: 
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
        operand_stack = []
        operator_stack = []
    
        for char in expression:
            if char.isdigit():
                operand_stack.append(float(char))
            elif char in self.operators:
                while operator_stack and self.precedence(char) <= self.precedence(operator_stack[-1]):
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.operators[operator](operand1, operand2)
                    operand_stack.append(result)
                operator_stack.append(char)
    
        while operator_stack:
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.operators[operator](operand1, operand2)
            operand_stack.append(result)
    
        return operand_stack[-1] if operand_stack else None
    

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
        operator = operator_stack.pop()
        num2 = operand_stack.pop()
        num1 = operand_stack.pop()
        result = self.operators[operator](num1, num2)
        operand_stack.append(result)
        return operand_stack, operator_stack