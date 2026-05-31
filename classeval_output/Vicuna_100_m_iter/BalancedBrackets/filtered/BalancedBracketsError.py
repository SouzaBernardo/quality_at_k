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
        self.stack = []
        for i in range(len(self.expr) - 1):
            if self.expr[i] not in self.left_brackets and self.expr[i] not in self.right_brackets:
                self.stack.append(self.expr[i])
            elif self.expr[i] in self.left_brackets:
                self.stack.append(self.left_brackets.pop(0))
            elif self.expr[i] in self.right_brackets:
                self.stack.append(self.right_brackets.pop(0))
        self.expr = ''.join(self.stack)

    def check_balanced_brackets(self):
        if len(self.stack) == 0:
            return True
        if len(self.stack) == 1:
            return True
        for i in range(len(self.stack) - 1):
            if self.stack[i] == "(" or self.stack[i] == "{" or self.stack[i] == "[":
                return False
        return True