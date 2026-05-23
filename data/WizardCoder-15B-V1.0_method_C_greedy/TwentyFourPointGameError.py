import random
class TwentyFourPointGame: 
    def __init__(self) -> None:
        self.nums = []




    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = random.sample(range(1, 10), 4)

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        self.nums = random.sample(range(1, 10), 4)
        return self.nums

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Check if the expression contains any invalid characters
        if not all(c.isdigit() or c in ['+', '-'] for c in expression):
            return False
        # Evaluate the expression and compare to 24
        try:
            result = eval(expression)
            return result == 24
        except:
            return False

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        tokens = expression.split()
        nums = []
        for token in tokens:
            if token.isdigit():
                nums.append(int(token))
            elif token in ['+', '-', '*', '/']:
                if len(nums) < 2:
                    return False
                if token == '+':
                    nums[-2] += nums[-1]
                elif token == '-':
                    nums[-2] -= nums[-1]
                elif token == '*':
                    nums[-2] *= nums[-1]
                elif token == '/':
                    if nums[-1] == 0:
                        return False
                    nums[-2] /= nums[-1]
                nums.pop()
            else:
                return False
        return nums[0] == 24