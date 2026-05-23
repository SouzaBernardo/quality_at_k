
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
        new_expr = ""
        for char in self.expr:
            if char in self.left_brackets or char in self.right_brackets:
                new_expr += char
        self.expr = new_expr
    

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack:
                    return False
                opening_bracket = self.stack.pop()
                if self.left_brackets.index(opening_bracket) != self.right_brackets.index(char):
                    return False
        return len(self.stack) == 0
    