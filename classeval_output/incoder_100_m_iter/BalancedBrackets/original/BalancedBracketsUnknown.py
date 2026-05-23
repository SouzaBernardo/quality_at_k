
class BalancedBrackets:  
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr


    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
        expr = self.expr
        for char in self.left_brackets:
            expr = expr.replace(char, '')
        for char in self.right_brackets:
            expr = expr.replace(char, '')
        self.expr = expr


    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
        expr = self.expr
        left_brackets = self.left_brackets
        right_brackets = self.right_brackets
        stack = self.stack
        length = len(expr)
        count = 0
        while count < length:
            if expr[count] in left_brackets:
                stack.append(expr[count])
                count += 1
            elif expr[count] in right_brackets:
                stack.pop()
                count += 1
            else:
                count += 1
        return len(stack) == 0

