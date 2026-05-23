
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
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
        expr = self.expr
        expr = re.sub(r'[^({})]+', '', expr)
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
        stack = self.stack
        left_brackets = self.left_brackets
        right_brackets = self.right_brackets
        length = len(expr)
        count = 0
        
        while count < length:
            if expr[count] in left_brackets:
                stack.append(expr[count])
                count += 1
            elif expr[count] in right_brackets:
                stack.pop()
                count += 1
            else:
                count += 1
        
        if len(stack) == 0:
            return True
        else:
            return False
