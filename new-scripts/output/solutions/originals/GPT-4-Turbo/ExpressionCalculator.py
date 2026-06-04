```python
from collections import deque
import decimal

class ExpressionCalculator:
    def __init__(self):
        self.postfix_stack = deque()
        self.operat_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0, ')': 0}

    def calculate(self, expression):
        self.prepare(expression)
        while self.postfix_stack:
            current = self.postfix_stack.popleft()
            if not self.is_operator(current):
                self.postfix_stack.appendleft(decimal.Decimal(current))
            else:
                second_value = self.postfix_stack.popleft()
                first_value = self.postfix_stack.popleft()
                self.postfix_stack.appendleft(self._calculate(first_value, second_value, current))
        return float(self.postfix_stack[0])

    def prepare(self, expression):
        expression = self.transform(expression)
        operator_stack = deque()
        for char in expression:
            if not self.is_operator(char):
                self.postfix_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while operator_stack and self.compare(char, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(char)
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())

    @staticmethod
    def is_operator(c):
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        return self.operat_priority[cur] <= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value

    @staticmethod
    def transform(expression):
        return expression.replace(" ", "")
```
This code defines a class `ExpressionCalculator` that can perform calculations with basic arithmetic operations. The `calculate` method is the main method that takes an expression as input and returns the calculated result. The `prepare` method transforms the infix expression to postfix notation. The `is_operator` method checks if a character is an operator. The `compare` method compares the precedence of two operators. The `_calculate` method performs the mathematical calculation based on the given operands and operator. The `transform` method removes spaces from the expression.