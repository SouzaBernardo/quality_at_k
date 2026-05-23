import random
class TwentyFourPointGame:  
    """
    This ia a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

    def __init__(self) -> None:
        self.nums = []




    def _generate_cards(self):
        
        self.nums = [random.randint(1, 9) for _ in range(4)]




    def _check_expression(self, expression):


    def get_my_cards(self):


    def answer(self, expression):


    def evaluate_expression(self, expression):
