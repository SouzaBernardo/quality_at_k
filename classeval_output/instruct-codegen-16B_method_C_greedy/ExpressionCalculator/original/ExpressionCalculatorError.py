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
        """
        expression = self.transform(expression)
        stack = deque()
        for char in expression.split():
            if self.is_operator(char):
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, char)
                stack.append(result)
            else:
                stack.append(char)
        return float(stack.pop())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        expression = expression.replace(" ", "")
        expression = expression.replace("^", "**")
        expression = expression.replace("%", "/100")
        expression = expression.replace("√", "sqrt")
        expression = expression.replace("!", "factorial")
        expression = expression.replace("π", "pi")
        expression = expression.replace("e", "exp")
        expression = expression.replace("^-1", "**-1")
        expression = expression.replace("^-2", "**-2")
        expression = expression.replace("^-3", "**-3")
        expression = expression.replace("^-4", "**-4")
        expression = expression.replace("^-5", "**-5")
        expression = expression.replace("^-6", "**-6")
        expression = expression.replace("^-7", "**-7")
        expression = expression.replace("^-8", "**-8")
        expression = expression.replace("^-9", "**-9")
        expression = expression.replace("^-10", "**-10")
        expression = expression.replace("^-11", "**-11")
        expression = expression.replace("^-12", "**-12")
        expression = expression.replace("^-13", "**-13")
        expression = expression.replace("^-14", "**-14")
        expression = expression.replace("^-15", "**-15")
        expression = expression.replace("^-16", "**-16")
        expression = expression.replace("^-17", "**-17")
        expression = expression.replace("^-18", "**-18")
        expression = expression.replace("^-19", "**-19")
        expression = expression.replace("^-20", "**-20")
        expression = expression.replace("^-21", "**-21")
        expression = expression.replace("^-22", "**-22")
        expression = expression.replace("^-23", "**-23")
        expression = expression.replace("^-24", "**-24")
        expression = expression.replace("^-25", "**-25")
        expression = expression.replace("^-26", "**-26")
        expression = expression.replace("^-27", "**-27")
        expression = expression.replace("^-28", "**-28")
        expression = expression.replace("^-29", "**-29")
        expression = expression.replace("^-30", "**-30")
        expression = expression.replace("^-31", "**-31")
        expression = expression.replace("^-32", "**-32")
        expression = expression.replace("^-33", "**-33")
        expression = expression.replace("^-34", "**-34")
        expression = expression.replace("^-35", "**-35")
        expression = expression.replace("^-36", "**-36")
        expression = expression.replace("^-37", "**-37")
        expression = expression.replace("^-38", "**-38")
        expression = expression.replace("^-39", "**-39")
        expression = expression.replace("^-40", "**-40")
        expression = expression.replace("^-41", "**-41")
        expression = expression.replace("^-42", "**-42")
        expression = expression.replace("^-43", "**-43")
        expression = expression.replace("^-44", "**-44")
        expression = expression.replace("^-45", "**-45")
        expression = expression.replace("^-46", "**-46")
        expression = expression.replace("^-47", "**-47")
        expression = expression.replace("^-48", "**-48")
        expression = expression.replace("^-49", "**-49")
        expression = expression.replace("^-50", "**-50")
        expression = expression.replace("^-51", "**-51")
        expression = expression.replace("^-52", "**-52")
        expression = expression.replace("^-53", "**-53")
        expression = expression.replace("^-54", "**-54")
        expression = expression.replace("^-55", "**-55")
        expression = expression.replace("^-56", "**-56")
        expression = expression.replace("^-57", "**-57")
        expression = expression.replace("^-58", "**-58")
        expression = expression.replace("^-59", "**-59")
        expression = expression.replace("^-60", "**-60")
        expression = expression.replace("^-61", "**-61")
        expression = expression.replace("^-62", "**-62")
        expression = expression.replace("^-63", "**-63")
        expression = expression.replace("^-64", "**-64")
        expression = expression.replace("^-65", "**-65")
        expression = expression.replace("^-66", "**-66")
        expression = expression.replace("^-67", "**-67")
        expression = expression.replace("^-68", "**-68")
        expression = expression.replace("^-69", "**-69")
        expression = expression.replace("^-70", "**-70")
        expression = expression.replace("^-71", "**-71")
        expression = expression.replace("^-72", "**-72")
        expression = expression.replace("^-73", "**-73")
        expression = expression.replace("^-74", "**-74")
        expression = expression.replace("^-75", "**-75")
        expression = expression.replace("^-76", "**-76")
        expression = expression.replace("^-77", "**-77")
        expression = expression.replace("^-78", "**-78")
        expression = expression.replace("^-79", "**-79")
        expression = expression.replace("^-80", "**-80")
        expression = expression.replace("^-81", "**-81")
        expression = expression.replace("^-82", "**-82")
        expression = expression.replace("^-83", "**-83")
        expression = expression.replace("^-84", "**-84")
        expression = expression.replace("^-85", "**-85")
        expression = expression.replace("^-86", "**-86")
        expression = expression.replace("^-87", "**-87")
        expression = expression.replace("^-88", "**-88")
        expression = expression.replace("^-89", "**-89")
        expression = expression.replace("^-90", "**-90")
        expression = expression.replace("^-91", "**-91")
        expression = expression.replace("^-92", "**-92")
        expression = expression.replace("^-93", "**-93")
        expression = expression.replace("^-94", "**-94")
        expression = expression.replace("^-95", "**-95")
        expression = expression.replace("^-96", "**-96



    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        if self.operat_priority[self.operator_dict[cur]] >= self.operat_priority[self.operator_dict[peek]]:
            return True
        else:
            return False



    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        expression = re.sub('(\d+(\s+\d+)*)','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+)*,\s+)', '\g<1>*', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re.sub('(\d+(\s+\d+))','\g<1> ', expression)
        expression = re