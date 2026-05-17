import random
class BlackjackGame: 
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
            elif self.player_hand[i] == 'JC':
                deck.append('JC')
            elif self.player_hand[i] == 'QH':
                deck.append('QH')
            elif self.player_hand[i] == '2C':
                deck.append('2C')
            elif self.player_hand[i] == 'KD':
                deck.append('KD')
            elif self.player_hand[i] == '5D':
                deck.append('5D')
            elif self.player_hand[i] == 'AH':
                deck.append('AH')
            elif self.player_hand[i] == '2S':
                deck.append('2S')
            elif self.player_hand[i] == 'QC':
                deck.append('QC')
            elif self.player_hand[i] == 'KH':
                deck.append('KH')
            elif self.player_hand[i] == '9S':
                deck.append('9S')
            elif self.player_hand[i] == '5S':
                deck.append('5S')
            elif self.player_hand[i] == '3C':
                deck.append('3C')
            elif self.player_hand[i] == 'AC':
                deck.append('AC')
            elif self.player_hand[i] == '4C':
                deck.append('4C')
            elif self.player_hand[i] == '5H':
                deck.append('5H')
            elif self.player_hand[i] == 'AS':
                deck.append('AS')
            elif self.player_hand[i] == '2C':
                deck.append('2C')
            elif self.player_hand[i] == 'KD':
                deck.append('KD')
            elif self.player_hand[i] == '5D':
                deck.append('5D')
            elif self.player_hand[i] == 'AH':
                deck.append('AH')
            elif self.player_hand[i] == '2S':
        

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value.
        Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """
        total_hand = hand[0]
        total_value = 0
        for i in range(1, len(hand)):
            if hand[i] == '1':
                total_value += 1
            else:
                total_value += 10
        total_hand = total_hand + total_value
        return total_hand



    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        rule:
        If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21.
        Otherwise, the winner is the one with the lower hand value.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
        'Player wins'
        """
        if len(player_hand) == len(dealer_hand):
            return 'Player wins'
        elif len(player_hand) < len(dealer_hand):
            return 'Dealer wins'
        else:
            return 'Player wins'