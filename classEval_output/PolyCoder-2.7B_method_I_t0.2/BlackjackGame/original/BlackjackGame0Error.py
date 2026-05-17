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
        for i in range(len(self.player_hand)):
            if self.player_hand[i] == 'AS':
                deck.append('AS')
            elif self.player_hand[i] == '2S':
                deck.append('2S')
            elif self.player_hand[i] == 'JH':
                deck.append('JH')
            elif self.player_hand[i] == '7D':
                deck.append('7D')
            elif self.player_hand[i] == '6H':
                deck.append('6H')
            elif self.player_hand[i] == '9D':
                deck.append('9D')
            elif self.player_hand[i] == '5D':
                deck.append('5D')
            elif self.player_hand[i] == 'AH':
                deck.append('AH')
            elif self.player_hand[i] == '2C':
                deck.append('2C')
            elif self.player_hand[i] == 'KC':
                deck.append('KC')
            elif self.player_hand[i] == '3D':
                deck.append('3D')
            elif self.player_hand[i] == '10C':
                deck.append('10C')
            elif self.player_hand[i] == 'KS':
                deck.append('KS')
            elif self.player_hand[i] == '5S':
                deck.append('5S')
            elif self.player_hand[i] == 'JD':
                deck.append('JD')
            elif self.player_hand[i] == '8S':
                deck.append('8S')
            elif self.player_hand[i] == 'AS':
                deck.append('AS')
            elif self.player_hand[i] == '2S':
                deck.append('2S')
            elif self.player_hand[i] == 'JH':
                deck.append('JH')
            elif self.player_hand[i] == '7D':
                deck.append('7D')
            elif self.player_hand[i] == '6H':
                deck.append('6H')
            elif self.player_hand[i] == '9D':
                deck.append('9D')
            elif self.player_hand[i] == '5D':
                deck.append('5D')
            elif self.player_hand[i] == 'AH':
                deck.append('AH')
            elif self.player_hand[i] == '2C':
                deck.append('2C')
            elif self.player_hand[i] == 'KC':
                deck.append('KC')
            elif self.player_hand[i] == '3D':
                deck.append('3D')
            elif self.player_hand[i] == '10C':
       



