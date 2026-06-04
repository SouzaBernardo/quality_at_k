Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class BalancedBrackets in the following code.
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

### Response:The class `BalancedBrackets` is already implemented and complete. The only thing that needs to be added is the `clear_expr` method. Here's the updated code:

```python
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
        self.expr = ''.join(filter(lambda x: x in self.left_brackets + self.right_brackets, self.expr))

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True
        """
        self.clear_expr()
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack:
                    return False
                if self.right_brackets.index(char)!= self.left_brackets.index(self.stack.pop()):
                    return False
        return not self.stack
```

The `clear_expr` method uses the `filter` function to remove all characters that are not brackets from the expression. The `check_balanced_brackets` method first calls `clear_expr` to remove any characters that are not brackets. It then iterates through the expression and checks if each character is a left bracket or a right bracket. If it is a left bracket, it is added to the stack. If it is a right bracket, it is popped from the stack and compared to the corresponding left bracket. If they do not match, the expression is not balanced. If the stack is empty at the end of the iteration, the expression is balanced.