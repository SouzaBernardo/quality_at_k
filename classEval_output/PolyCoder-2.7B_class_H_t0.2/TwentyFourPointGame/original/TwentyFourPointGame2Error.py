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


    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()

        """


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


    def evaluate_expression_random(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression_random(ans)
        True
        """


    def add_card(self, card):
        """
        Add a card to the game.
        :param card: integer, card to add
        :return: None
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.add_card(1)
        >>> game.nums
        [4, 3, 6, 6]
        """


    def remove_card(self, card):
        """
        Remove a card from the game.
        :param card: integer, card to remove
        :return: None
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.remove_card(1)
        >>> game.nums
        []
        """


    def get_card(self, card):
        """
        Get a card from the game.
        :param card: integer, card to get
        :return: integer, card number
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.get_card(1)
        4
        >>> game.get_card(2)
        3
        >>> game.get_card(3)
        6
        >>> game.get_card(4)
        6
        """


    def get_card_random(self, card):
        """
        Get a card from the game.
        :param card: integer, card to get
        :return: integer, card number
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.get_card_random(1)
        4
        >>> game.get_card_random(2)
        3
        >>> game.get_card_random(3)
        6
        >>> game.get_card_random(4)
        6
        """


    def get_cards(self):
        """
        Get a list of all the cards in the game.
        :return: list of integers, all the cards in the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.get_cards()
        [4, 3, 6, 6]
        """


    def get_card_count(self):
        """
        Get the number of cards in the game.
        :return: integer, the number of cards in the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.get_card_count()
        3
        """


    def get_card_count_random(self):
        """
        Get the number of cards in the game.
        :return: integer, the number of cards in the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> game.get_card_count_random()
        3
        """


    def get_card_count_random_random(self):
        """
        Get the number of cards in the game.
        :return: integer, the number of cards in the game
      