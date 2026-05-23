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


    def get_my_cards_and_evaluate_expression(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards, and evaluate the expression.
        :return: list of integers, representing the player's cards and the expression's result
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]
        expression = "4*3+6+6"
        result = self.answer(expression)
        return result, result


    def generate_cards_and_evaluate_expression(self):
        """
        Generate four random numbers between 1 and 9, evaluate the expression, and return the result.
        :return: tuple of integers, representing the player's cards and the expression's result
        """
        result, expression = self.generate_cards_and_evaluate_expression()
        return result