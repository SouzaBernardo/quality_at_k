from random import randint

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
        for i in range(4):
            self.nums.append(randint(1, 9))


    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [5, 6, 7, 8]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [9, 10, 11, 12]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [13, 14, 15, 16]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [5, 6, 7, 8]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [9, 10, 11, 12]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [13, 14, 15, 16]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [5, 6, 7, 8]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [9, 10, 11, 12]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [13, 14, 15, 16]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [5, 6, 7, 8]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [9, 10, 11, 12]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [13, 14, 15, 16]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [5, 6, 7, 8]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [9, 10, 11, 12]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [13, 14, 15, 16]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        [1, 2, 3, 4]
        >>> game = TwentyFourPointGame()
        >>> game.get_my_