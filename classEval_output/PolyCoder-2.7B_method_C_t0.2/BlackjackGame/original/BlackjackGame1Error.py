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
            elif self.player_hand[i] == '9S':
                deck.append('9S')
            elif self.player_hand[i] == '5C':
                deck.append('5C')
            elif self.player_hand[i] == '7C':
                deck.append('7C')
            elif self.player_hand[i] == '3D':
                deck.append('3D')
            elif self.player_hand[i] == '10C':
                deck.append('10C')
            elif self.player_hand[i] == '5D':
                deck.append('5D')
            elif self.player_hand[i] == 'AH':
                deck.append('AH')
            elif self.player_hand[i] == '2D':
                deck.append('2D')
            elif self.player_hand[i] == 'KC':
                deck.append('KC')
            elif self.player_hand[i] == '3S':
                deck.append('3S')
            elif self.player_hand[i] == '2H':
                deck.append('2H')
            elif self.player_hand[i] == '10H':
                deck.append('10H')
            elif self.player_hand[i] == '7S':
                deck.append('7S')
            elif self.player_hand[i] == '6D':
                deck.append('6D')
            elif self.player_hand[i] == '3C':
                deck.append('3C')
            elif self.player_hand[i] == 'JD':
                deck.append('JD')
            elif self.player_hand[i] == '8S':
                deck.append('8S')
            elif self.player_hand[i] == 'AS':
                deck.append('AS')
            elif self.player_hand[i] == '8D':
                deck.append('8D')
            elif self.player_hand[i] == '4S':
                deck.append('4S')
            elif self.player_hand[i] == 'JS':
                deck.append('JS')
            elif self.player_hand[i] == '6H

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
        if len(hand) == 0:
            return 0
        if len(hand) == 1:
            return hand[0]
        if len(hand) == 2:
            return hand[0] + hand[1]
        if len(hand) == 3:
            return hand[0] + hand[1] + hand[2]
        if len(hand) == 4:
            return hand[0] + hand[1] + hand[2] + hand[3]
        if len(hand) == 5:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4]
        if len(hand) == 6:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5]
        if len(hand) == 7:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6]
        if len(hand) == 8:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7]
        if len(hand) == 9:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8]
        if len(hand) == 10:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9]
        if len(hand) == 11:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10]
        if len(hand) == 12:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11]
        if len(hand) == 13:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12]
        if len(hand) == 14:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12] + hand[13]
        if len(hand) == 15:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12] + hand[13] + hand[14]
        if len(hand) == 16:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12] + hand[13] + hand[14] + hand[15]
        if len(hand) == 17:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12] + hand[13] + hand[14] + hand[15] + hand[16]
        if len(hand) == 18:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5] + hand[6] + hand[7] + hand[8] + hand[9] + hand[10] + hand[11] + hand[12] + hand[13] + hand[14] + hand[15] + hand[16] + hand[17]
        if len(hand) == 19:
            return hand[0] + hand[1] + hand[2] + hand[3] + hand[4] + hand[5]

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
        if player_hand[0] == dealer_hand[0]:
            return 'Player wins'
        elif player_hand[0] > dealer_hand[0]:
            return 'Dealer wins'
        else:
            return 'Player wins'
