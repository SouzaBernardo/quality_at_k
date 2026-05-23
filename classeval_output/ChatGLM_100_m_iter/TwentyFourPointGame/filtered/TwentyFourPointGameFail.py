import random
class TwentyFourPointGame:  
    """
    This ia a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

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
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [2, 7, 1, 8]
        """
        return [self._generate_cards() for _ in range(4)]

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
        # Generate four random numbers between 1 and 9 for the cards
        nums = [random.randint(1, 9) for _ in range(4)]
        
        # Check if the expression can evaluate to 24
        if expression in [f"4*{nums[0]}+{nums[1]}+{nums[2]}", f"{nums[0]}*{nums[1]}-{nums[2]}", f"{nums[0]}*{nums[1]}*{nums[2]}", f"{nums[0]}*{nums[1]}*{nums[2]}*{nums[3]}"]:
            return True
        else:
            return False

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Generate four random numbers between 1 and 9 for the cards
        nums = [random.randint(1, 9) for _ in range(4)]
        
        # Check if the expression can evaluate to 24
        if expression in [f"4*{nums[0]}+{nums[1]}+{nums[2]}", f"{nums[0]}*{nums[1]}-{nums[2]}", f"{nums[0]}*{nums[1]}*{nums[2]}", f"{nums[0]}*{nums[1]}*{nums[2]}*{nums[3]}"]:
            return True
        else:
            return False