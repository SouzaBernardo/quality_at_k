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
        

        if not expression:
            return None

        stack = []
        for token in expression.split():
            if token in self.operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.operators[token](x, y))
            else:
                stack.append(float(token))

        return stack.pop() if len(stack) == 1 else None


    def precedence(self, operator):
        
        if operator == '^':
            return 3
        elif operator == '/' or operator == '*':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return 0


    def apply_operator(self, operand_stack, operator_stack):
        
        if not operator_stack:
            return operand_stack, operator_stack

        operator = operator_stack.pop()
        operand_stack.append(self.operators[operator](operand_stack.pop(), operand_stack.pop()))

        return operand_stack, operator_stack


    def evaluate(self, expression):