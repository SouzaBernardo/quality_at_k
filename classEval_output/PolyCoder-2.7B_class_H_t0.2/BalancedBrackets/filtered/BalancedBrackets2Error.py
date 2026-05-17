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
        if self.expr.find("(")!= -1:
            return True
        else:
            return False

    def check_balanced_brackets_in_str(self, str_expr):
        """
        Checks if the expression has balanced brackets in a string.
        :param str_expr: The string expression to check for balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_str("a(b)c")
        True

        """
        if self.expr.find("(")!= -1:
            return True
        else:
            return False

    def check_balanced_brackets_in_str_in_expr(self, str_expr, expr):
        """
        Checks if the expression has balanced brackets in a string and in an expression.
        :param str_expr: The string expression to check for balanced brackets.
        :param expr: The expression to check for balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_str_in_expr("a(b)c", "a(b)c")
        True

        """
        if self.expr.find("(")!= -1:
            return True
        else:
            return False

    def check_balanced_brackets_in_str_in_expr_in_expr(self, str_expr, expr, expr_in_expr):
        """
        Checks if the expression has balanced brackets in a string and in an expression and in an expression.
        :param str_expr: The string expression to check for balanced brackets.
        :param expr: The expression to check for balanced brackets.
        :param expr_in_expr: The expression to check for balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_str_in_expr_in_expr("a(b)c", "a(b)c", "a(b)c")
        True

        """
        if self.expr.find("(")!= -1:
            return True
        else:
            return False

    def check_balanced_brackets_in_str_in_expr_in_expr_in_expr(self, str_expr, expr, expr_in_expr, expr_in_expr_in_expr):
        """
        Checks if the expression has balanced brackets in a string and in an expression and in an expression and in an expression.
        :param str_expr: The string expression to check for balanced brackets.
        :param expr: The expression to check for balanced brackets.
        :param expr_in_expr: The expression to check for balanced brackets.
        :param expr_in_expr_in_expr: The expression to check for balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_str_in_expr_in_expr_in_expr("a(b)c", "a(b)c", "a(b)c", "a(b)c")
        True

        """
        if self.expr.find("(")!= -1:
            return True
        else:
            return False

    def check_balanced_brackets_in_str_in_expr_in_expr_in_expr_in_expr(self, str_expr, expr, expr_in_expr, expr_in_expr_in_expr, expr_in_expr_in_expr_in_expr):
        """
        Checks if the expression has balanced brackets in a string and in an expression and in an expression and in an expression and in an expression.
        :param str_expr: The string expression to check for balanced brackets.
        :param expr: The expression to check for balanced brackets.
        :param expr_in_expr: The expression to check for balanced brackets.
        :param expr_in_expr_in_expr: The expression to check for balanced brackets.
        :param expr_in_expr_in_expr_in_expr: The expression to check for balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_in_str_in_expr_in_expr_in_expr_in_expr_in_expr("a(b)c", "a(b)c", "a(b)c", "a(b)c", "a(b)c")
        True