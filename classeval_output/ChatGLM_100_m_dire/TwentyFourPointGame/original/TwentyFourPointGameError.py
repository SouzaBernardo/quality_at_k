import random
class TwentyFourPointGame: 
    def __init__(self) -> None:
        self.nums = []




    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        nums = [random.randint(1, 9) for _ in range(4)]
        self.nums = nums

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        return random.randint(1, 9)



    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
        # Evaluate the expression using a mathematical function
        result = self._calculate_expression(expression)
        
        # Check if the result is 24
        if result == 24:
            return True
        else:
            return False
        
        # Return False if the expression is not 24
        return False