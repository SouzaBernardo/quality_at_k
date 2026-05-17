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


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """


    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """


    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """


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


    @staticmethod
    def get_postfix_stack(expression):
        """
        Get the postfix expression stack
        :param expression: string, the infix expression to be transformed
        :return: string, the postfix expression stack
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_postfix_stack("2 + 3 * 4")
        ['2', '3', '4', '*', '+']

        """


    @staticmethod
    def get_operator(expression):
        """
        Get the operator from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: string, the operator
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_operator("+")
        '+'

        """


    @staticmethod
    def get_operator_priority(expression):
        """
        Get the operator priority from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: int, the operator priority
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_operator_priority("+")
        1

        """


    @staticmethod
    def get_operator_priority_by_operator(expression):
        """
        Get the operator priority from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: int, the operator priority
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_operator_priority_by_operator("+")
        2

        """


    @staticmethod
    def get_operator_priority_by_operator_and_operator(expression):
        """
        Get the operator priority from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: int, the operator priority
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_operator_priority_by_operator_and_operator("+")
        3

        """


    @staticmethod
    def get_operator_priority_by_operator_and_operator_and_operator(expression):
        """
        Get the operator priority from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: int, the operator priority
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.get_operator_priority_by_operator_and_operator_and_operator("+")
        4

        """


    @staticmethod
    def get_operator_priority_by_operator_and_operator_and_operator_and_operator(expression):
        """
        Get the operator priority from the postfix expression
        :param expression: string, the infix expression to be transformed
        :return: int,