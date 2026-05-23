
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
        current_operand = ''
        for char in expression:
            if char.isdigit() or char == '.':
                current_operand += char
            elif char in self.operators:
                while len(operator_stack) > 0 and self.precedence(char) <= self.precedence(operator_stack[-1]):
                    if not self.apply_operator(operand_stack, operator_stack):
                        return None
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while len(operator_stack) > 0 and operator_stack[-1]!= '(':
                    if not self.apply_operator(operand_stack, operator_stack):
                        return None
                if len(operator_stack) == 0 or operator_stack[-1]!= '(':
                    return None
                operator_stack.pop()
            elif char =='':
                continue
            else:
                return None
        while len(operator_stack) > 0:
            if not self.apply_operator(operand_stack, operator_stack):
                return None
        if len(operand_stack)!= 1:
            return None
        return operand_stack[0]


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

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        if len(operator_stack) < 1:
            return operand_stack, operator_stack
        operator = operator_stack.pop()
        if len(operand_stack) < 2:
            return operand_stack, operator_stack
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        return operand_stack, operator_stack