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


    def get_answer(self):
        """
        Get the answer of the game.
        :return: string, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer()
        >>> ret
        '4*3+6+6'
        """


    def get_answer_list(self):
        """
        Get the answer of the game as a list.
        :return: list, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_list()
        >>> ret
        [4, 3, 6, 6]
        """


    def get_answer_dict(self):
        """
        Get the answer of the game as a dictionary.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict()
        >>> ret
        {'4': 4, '3': 3, '6': 6, '6': 6}
        """


    def get_answer_dict_list(self):
        """
        Get the answer of the game as a dictionary of lists.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict_list()
        >>> ret
        {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}
        """


    def get_answer_dict_list_dict(self):
        """
        Get the answer of the game as a dictionary of lists of dictionaries.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict_list_dict()
        >>> ret
        {'4': {'4': 4, '3': 3, '6': 6, '6': 6}, '3': {'4': 4, '3': 3, '6': 6, '6': 6}, '6': {'4': 4, '3': 3, '6': 6, '6': 6}, '6': {'4': 4, '3': 3, '6': 6, '6': 6}}
        """


    def get_answer_dict_list_dict_list(self):
        """
        Get the answer of the game as a dictionary of lists of dictionaries of lists.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict_list_dict_list()
        >>> ret
        {'4': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}, '3': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}, '6': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}}
        """


    def get_answer_dict_list_dict_list_dict(self):
        """
        Get the answer of the game as a dictionary of lists of dictionaries of lists of dictionaries.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict_list_dict_list_dict()
        >>> ret
        {'4': {'4': {'4': 4, '3': 3, '6': 6, '6': 6}, '3': {'4': 4, '3': 3, '6': 6, '6': 6}, '6': {'4': 4, '3': 3, '6': 6, '6': 6}, '6': {'4': 4, '3': 3, '6': 6, '6': 6}}, '3': {'4': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}, '3': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}, '6': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}}}
        """


    def get_answer_dict_list_dict_list_dict_list(self):
        """
        Get the answer of the game as a dictionary of lists of dictionaries of lists of dictionaries of lists.
        :return: dict, the answer of the game
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.get_answer_dict_list_dict_list_dict_list()
        >>> ret
        {'4': {'4': {'4': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6, 6]}, '3': {'4': {'4': [4, 3, 6, 6], '3': [4, 3, 6, 6], '6': [4, 3, 6, 6], '6': [4, 3, 6