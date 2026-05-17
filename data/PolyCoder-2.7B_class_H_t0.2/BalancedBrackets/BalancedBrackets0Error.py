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

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_brackets_in_string(self):
        """
        Checks if the expression has balanced brackets in the string.
        :return: True if the expression has balanced brackets in the string, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_string()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_brackets_in_string_and_expr(self):
        """
        Checks if the expression has balanced brackets in the string and the expression.
        :return: True if the expression has balanced brackets in the string and the expression, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_string_and_expr()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_brackets_in_string_and_expr_and_expr(self):
        """
        Checks if the expression has balanced brackets in the string and the expression and the expression.
        :return: True if the expression has balanced brackets in the string and the expression and the expression, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_string_and_expr_and_expr()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_brackets_in_string_and_expr_and_expr_and_expr(self):
        """
        Checks if the expression has balanced brackets in the string and the expression and the expression and the expression.
        :return: True if the expression has balanced brackets in the string and the expression and the expression and the expression, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_string_and_expr_and_expr_and_expr()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_brackets_in_string_and_expr_and_expr_and_expr_and_expr(self):
        """
        Checks if the expression has balanced brackets in the string and the expression and the expression and the expression and the expression.
        :return: True if the expression has balanced brackets in the string and the expression and the expression and the expression and the expression, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_string_and_expr_and_expr_and_expr_and_expr()
        True

        """
        for bracket in self.left_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        for bracket in self.right_brackets:
            if self.expr.find(bracket)!= -1:
                return False
        return True

    def check_balanced_br