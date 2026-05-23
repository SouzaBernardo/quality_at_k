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
        self.clear_expr()  # Clear the expression of non-bracket characters
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)  # Push opening brackets onto the stack
            elif char in self.right_brackets:
                if not self.stack:  # If stack is empty and a closing bracket is encountered, brackets are not balanced
                    return False
                opening_bracket = self.stack.pop()  # Pop the last opening bracket from the stack
                if self.left_brackets.index(opening_bracket) != self.right_brackets.index(char):
                    return False  # If the closing bracket doesn't match the last opening bracket, brackets are not balanced
        return len(self.stack) == 0  # If stack is empty, brackets are balanced