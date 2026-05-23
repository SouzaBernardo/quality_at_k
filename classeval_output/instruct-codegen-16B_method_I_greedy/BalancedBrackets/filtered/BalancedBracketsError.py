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

    def check_balanced_brackets(expr):
        stack = []
        left_brackets = ["(", "{", "["]
        right_brackets = [")", "}", "]"]
        for char in expr:
            if char in left_brackets:
                stack.append(char)
            elif char in right_brackets:
                if not stack or right_brackets.index(char)!= left_brackets.index(stack.pop()):
                    return False
        return not stack