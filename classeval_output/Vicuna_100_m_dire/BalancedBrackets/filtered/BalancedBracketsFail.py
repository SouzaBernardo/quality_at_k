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
        self.stack = []
        for char in self.expr:
            if char in self.left_brackets or char in self.right_brackets:
                self.stack.append(char)
            elif char == "(" or char == "{" or char == "[":
                self.stack.append(char)
            else:
                self.stack.pop()

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        if not self.expr:
            return False
        for i in range(len(self.expr)-1):
            if self.left_brackets[i] not in self.expr:
                return False
            if self.right_brackets[i] not in self.expr:
                return False
        return True