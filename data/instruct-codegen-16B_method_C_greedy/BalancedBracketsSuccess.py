class BalancedBrackets: 
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
        """
        self.expr = "".join(c for c in self.expr if c in self.left_brackets + self.right_brackets)

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for bracket in self.expr:
            if bracket in self.left_brackets:
                self.stack.append(bracket)
            elif bracket in self.right_brackets:
                if not self.stack or self.right_brackets.index(bracket)!= self.left_brackets.index(self.stack.pop()):
                    return False
        return not self.stack