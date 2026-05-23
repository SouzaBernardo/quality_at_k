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
        result = 0.0
        expression = expression.replace(" + ", "").replace(" * ", "").replace(" / ", "")
        expression = re.sub(r"\s+", "", expression)
        expression = expression.replace(" ", "")
        expression = expression.replace("^", "")
        expression = expression.replace("$", "")
        expression = expression.replace("(", "").replace(")", "").replace(" ", "")
        expression = expression.replace("(", "").replace(")", "").replace(" ", "")
         Operat_priority = self.operat_priority
        current_op = expression[0]
        if current_op in [0, 3, 2, 1, -1, 1, 0, 2]:
            result = self.prepare(expression)
        elif current_op == 1:
            result = self._calculate(expression[1], expression[2], current_op)
        elif current_op == -1:
            result = self._calculate(expression[1], expression[2], Operat_priority[current_op])
        elif current_op == 2:
            result = self._calculate(expression[1], expression[2], Operat_priority[current_op])
        else:
            result = self._calculate(expression[1], expression[2], Operat_priority[current_op])
        return result

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        # Add the operator to the front of the expression
        operator = re.compile(r'\w+').search(expression)
        if operator:
            expression = expression[:operator.start()] + operator + expression[operator.start():]

        # Remove any whitespace before and after the operator
        operator_str = operator.group()
        expression = re.sub(r'\s+', '', expression)

        # Add the operator to the postfix stack
        postfix_stack.append(operator_str)

        # Calculate the result
        result = expression.replace('+', '+').replace('*', '*').replace('/', '/')
        result = Decimal(result)

        # Calculate the priority of the operator
        priority = [int(x) for x in re.findall(r'\d+', operator_str)]
        priority.sort()
        operator_priority = sorted(priority, key=lambda x: x[0], reverse=True)

        # Add the result and operator priority to the postfix stack
        postfix_stack.append(result)
        postfix_stack.append(operator_priority[0])







    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
    
        """
        # Step 1: Identify the infix operator and its priority
        operator, priority = re.search("([+-])\s*\d+\s*(\d+\.\d+)?", expression), re.finditer(r"\d+\s*(\d+\.\d+)?", expression)
        if operator:
            # Step 2: Calculate the left and right operands
            left_value, right_value = expression.split(" + ")
            if left_value:
                left_value = Decimal(left_value)
            if right_value:
                right_value = Decimal(right_value)
            # Step 3: Perform the operator's operation on the operands
            result = operator(left_value, right_value)
            # Step 4: Rewrite the expression using the operator's priority and operands
            expression = f"{operator.group(1)}({left_value})({result})"
        else:
            # Step 4: Rewrite the expression using the operator's priority and operands
            expression = f"{priority.group(0)}({operator.group(1)})" + expression
        return expression