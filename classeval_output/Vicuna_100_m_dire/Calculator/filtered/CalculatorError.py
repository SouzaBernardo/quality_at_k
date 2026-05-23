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

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('+')
            1
        >>> calculator.precedence('^')
            3
        >>> calculator.precedence('/')
            2
        >>> calculator.precedence('*')
            2
        >>> calculator.precedence('-')
            3
        >>> calculator.precedence('

    def apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        operand1 = operand_stack.pop()
        operand2 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        operator_stack.append(operand1)
        operator_stack.append(operand2)