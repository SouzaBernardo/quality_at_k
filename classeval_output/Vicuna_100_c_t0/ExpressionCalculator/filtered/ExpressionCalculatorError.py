class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

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
        stack = []
        for char in expression:
            if char == '+':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, '+')
                self.push(stack, result)
            elif char == '-':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, '-')
                self.push(stack, result)
            elif char == '*':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, '*')
                self.push(stack, result)
            elif char == '/':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, '/')
                self.push(stack, result)
            elif char == '(':
                op1 = self.pop_and_push(stack)
                self.push(stack, op1)
            elif char == ')':
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, ')')
                self.push(stack, result)
            elif char == '=':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                result = self._calculate(op1, op2, '=')
                self.push(stack, result)
            else:
                self.push(stack, char)

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        stack = []
        for char in expression:
            if char == '+':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                self._calculate(op1, op2, '+')
            elif char == '-':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                self._calculate(op1, op2, '-')
            elif char == '*':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                self._calculate(op1, op2, '*')
            elif char == '/':
                op1 = self.pop_and_push(stack)
                op2 = self.pop_and_push(stack)
                self._calculate(op1, op2, '/')
            elif char == '(':
                op1 = self.pop_and_push(stack)
                self.push(stack, op1)
            elif char == ')':
                op2 = self.pop_and_push(stack)