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


    def check_answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer(ans)
        True
        """


    def check_answer_card(self, card_number):
        """
        Check if a given card number is a valid answer.
        :param card_number: integer, card number
        :return: bool, True if the card number is a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card(ans)
        True
        """


    def check_answer_card_list(self, card_list):
        """
        Check if a given list of cards is a valid answer.
        :param card_list: list of integers, card numbers
        :return: bool, True if the card numbers are a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card_list([4, 3, 6, 6])
        True
        """


    def check_answer_card_list_list(self, card_list_list):
        """
        Check if a given list of cards is a valid answer.
        :param card_list_list: list of integers, card numbers
        :return: bool, True if the card numbers are a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card_list_list([4, 3, 6, 6])
        True
        """


    def check_answer_card_list_list_list(self, card_list_list_list):
        """
        Check if a given list of cards is a valid answer.
        :param card_list_list_list: list of integers, card numbers
        :return: bool, True if the card numbers are a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card_list_list_list([4, 3, 6, 6])
        True
        """


    def check_answer_card_list_list_list_list(self, card_list_list_list_list):
        """
        Check if a given list of cards is a valid answer.
        :param card_list_list_list: list of integers, card numbers
        :return: bool, True if the card numbers are a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card_list_list_list_list([4, 3, 6, 6])
        True
        """


    def check_answer_card_list_list_list_list_list(self, card_list_list_list_list_list):
        """
        Check if a given list of cards is a valid answer.
        :param card_list_list_list_list: list of integers, card numbers
        :return: bool, True if the card numbers are a valid answer, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_answer_card_list_list_list_list_list([4, 3, 6, 6])
     