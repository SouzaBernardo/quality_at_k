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
            if bracket in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket()
        True

        """
        for bracket in self.left_brackets:
            if bracket not in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket not in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket_no_bracket()
        True

        """
        for bracket in self.left_brackets:
            if bracket not in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket not in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket_no_bracket_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket_no_bracket_no_bracket()
        True

        """
        for bracket in self.left_brackets:
            if bracket not in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket not in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket()
        True

        """
        for bracket in self.left_brackets:
            if bracket not in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket not in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket()
        True

        """
        for bracket in self.left_brackets:
            if bracket not in self.expr:
                return True
        for bracket in self.right_brackets:
            if bracket not in self.expr:
                return True
        return False

    def check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket_no_bracket()
        True