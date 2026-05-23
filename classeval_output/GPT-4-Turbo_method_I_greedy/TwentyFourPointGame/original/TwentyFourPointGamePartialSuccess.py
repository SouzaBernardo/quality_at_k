import random
class TwentyFourPointGame: 
    def __init__(self) -> None:
        self.nums = []



    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        self._generate_cards()
        return self.nums
    
    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Check if all numbers in the expression are in the player's cards
        for num in self.nums:
            if str(num) not in expression:
                return False
    
        # Evaluate the expression and check if it equals 24
        try:
            if eval(expression) == 24:
                return True
            else:
                return False
        except:
            return False
    
    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        # Evaluate the expression and check if it equals 24
        try:
            if eval(expression) == 24:
                return True
            else:
                return False
        except:
            return False
    
