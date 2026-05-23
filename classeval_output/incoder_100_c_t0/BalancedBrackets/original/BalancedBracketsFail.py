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
        for char in self.left_brackets:
            if char in expr:
                self.stack.append(char)
                expr = expr.replace(char, '')
            else:
                if len(expr) > 0:
                    return False
                else:
                    return True
        for char in self.right_brackets:
            if char in expr:
                self.stack.pop()
                expr = expr.replace(char, '')
            else:
                if len(expr) > 0:
                    return False
                else:
                    return True
        if len(expr) > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

<|/ file |>
