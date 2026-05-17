import random
class BlackjackGame:  
    """
    This is a class representing a game of blackjack, which includes creating a deck, calculating the value of a hand, and determine the winner based on the hand values of the player and dealer.
    """

    def __init__(self):
        """
        Initialize the Blackjack Game with the attribute deck, player_hand and dealer_hand.
        While initializing deck attribute, call the create_deck method to generate.
        The deck stores 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        player_hand is a list which stores player's hand cards.
        dealer_hand is is a list which stores dealer's hand cards.
        """
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []



    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S',...].
        >>> black_jack_game = BlackjackGame()
        >>> black_jack_game.create_deck()
        ['QD', '9D', 'JC', 'QH', '2S', 'JH', '7D', '6H', '9S', '5C', '7H', 'QS', '5H',
        '6C', '7C', '3D', '10C', 'AD', '4C', '5D', 'AH', '2D', 'QC', 'KH', '9C', '9H',
        '4H', 'JS', '6S', '8H', '8C', '4S', '3H', '10H', '7S', '6D', '3C', 'KC', '3S',
        '2H', '10D', 'KS', '4D', 'AC', '10S', '2C', 'KD', '5S', 'JD', '8S', 'AS', '8D']
        """
        deck = []
        for i in range(52):
            if i == 0:
                continue
            if i == 1:
                continue
            if i == 2:
                continue
            if i == 3:
                continue
            if i == 4:
                continue
            if i == 5:
                continue
            if i == 6:
                continue
            if i == 7:
                continue
            if i == 8:
                continue
            if i == 9:
                continue
            if i == 10:
                continue
            if i == 11:
                continue
            if i == 12:
                continue
            if i == 13:
                continue
            if i == 14:
                continue
            if i == 15:
                continue
            if i == 16:
                continue
            if i == 17:
                continue
            if i == 18:
                continue
            if i == 19:
                continue
            if i == 20:
                continue
            if i == 21:
                continue
            if i == 22:
                continue
            if i == 23:
                continue
            if i == 24:
                continue
            if i == 25:
                continue
            if i == 26:
                continue
            if i == 27:
                continue
            if i == 28:
                continue
            if i == 29:
                continue
            if i == 30:
                continue
            if i == 31:
                continue
            if i == 32:
                continue
            if i == 33:
                continue
            if i == 34:
                continue
            if i == 35:
                continue
            if i == 36:
                continue
            if i == 37:
                continue
            if i == 38:
                continue
            if i == 39:
                continue
            if i