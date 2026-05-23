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
        cards = []
        for i in range(4):
            cards.append(random.randint(1, 9))
        return cards