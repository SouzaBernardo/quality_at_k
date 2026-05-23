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
        self.nums = [random.randint(1, 9) for _ in range(4)]
        return self.nums

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            # Evaluate the expression
            result = eval(expression)
            # Check if the result is 24
            if result == 24:
                return True
            else:
                return False
        except Exception as e:
            # If there is any error in the expression, return False
            return False
    
    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            result = eval(expression)
            return result == 24
        except Exception as e:
            print(f"Invalid expression: {e}")
            return False