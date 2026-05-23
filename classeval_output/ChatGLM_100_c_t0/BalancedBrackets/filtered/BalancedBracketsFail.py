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
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for char in self.expr:
            if char in self.left_brackets or char in self.right_brackets:
                self.expr = char
                break
        return self.expr

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        if len(self.stack) < 2:
            return False
        for char in self.stack[1:]:
            if char in self.left_brackets or char in self.right_brackets:
                return False
        return True