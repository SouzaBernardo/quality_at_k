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
        for _ in range(4):
            self.nums.append(random.randint(1, 9))

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        return self.nums

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Split the expression into individual terms
        terms = expression.split('+')
        # Evaluate each term and add them up
        total = 0
        for term in terms:
            total += eval(term)
        # Return True if the expression evaluates to 24
        return total == 24

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Split the expression into individual terms
        terms = expression.split('+')
        # Evaluate each term and add them up
        total = 0
        for term in terms:
            total += eval(term)
        # Return True if the expression evaluates to 24
        return total == 24