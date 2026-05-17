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


    def check_card(self, card_number):
        """
        Check if a given card number is a valid number.
        :param card_number: integer, card number
        :return: bool, True if the card number is a valid number, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_card(ans)
        True
        """


    def check_card_expression(self, expression):
        """
        Check if a given card expression is valid.
        :param expression: string, card expression
        :return: bool, True if the card expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_card_expression(ans)
        True
        """


    def check_card_expression_and_answer(self, expression):
        """
        Check if a given card expression is valid.
        :param expression: string, card expression
        :return: bool, True if the card expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_card_expression_and_answer(ans)
        True
        """


    def check_card_expression_and_answer_expression(self, expression):
        """
        Check if a given card expression is valid.
        :param expression: string, card expression
        :return: bool, True if the card expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_card_expression_and_answer_expression(ans)
        True
        """


    def check_expression(self, expression):
        """
        Check if a given mathematical expression is valid.
        :param expression: string, mathematical expression
        :return: bool, True if the expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_expression(ans)
        True
        """


    def check_expression_and_answer(self, expression):
        """
        Check if a given mathematical expression is valid.
        :param expression: string, mathematical expression
        :return: bool, True if the expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.check_expression_and_answer(ans)
        True
        """


    def check_expression_and_answer_expression(self, expression):
        """
        Check if a given mathematical expression is valid.
        :param expression: string, mathematical expression
        :return: bool, True if the expression is valid, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
    