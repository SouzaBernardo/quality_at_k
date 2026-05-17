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
        # Create a random deck
        deck = []
        for i in range(0, 52):
            deck.append(random.choice(self.deck))
        return deck


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
        total_hand = hand.count('1')
        total_value = 0
        for i in range(total_hand):
            total_value += hand[i]
        total_value += hand[total_hand-1]
        total_value += hand[total_hand-2]
        total_value += hand[total_hand-3]
        total_value += hand[total_hand-4]
        total_value += hand[total_hand-5]
        total_value += hand[total_hand-6]
        total_value += hand[total_hand-7]
        total_value += hand[total_hand-8]
        total_value += hand[total_hand-9]
        total_value += hand[total_hand-10]
        total_value += hand[total_hand-11]
        total_value += hand[total_hand-12]
        total_value += hand[total_hand-13]
        total_value += hand[total_hand-14]
        total_value += hand[total_hand-15]
        total_value += hand[total_hand-16]
        total_value += hand[total_hand-17]
        total_value += hand[total_hand-18]
        total_value += hand[total_hand-19]
        total_value += hand[total_hand-20]
        total_value += hand[total_hand-21]
        total_value += hand[total_hand-22]
        total_value += hand[total_hand-23]
        total_value += hand[total_hand-24]
        total_value += hand[total_hand-25]
        total_value += hand[total_hand-26]
        total_value += hand[total_hand-27]
        total_value += hand[total_hand-28]
        total_value += hand[total_hand-29]
        total_value += hand[total_hand-30]
        total_value += hand[total_hand-31]
        total_value += hand[total_hand-32]
        total_value += hand[total_hand-33]
        total_value += hand[total_hand-34]
        total_value += hand[total_hand-35]
        total_value += hand[total_hand-36]
        total_value += hand[total_hand-37]
        total_value += hand[total_hand-38]
        total_value += hand[total_hand-39]
        total_value += hand[total_hand-40]
        total_value += hand[total_hand-41]
        total_value += hand[total_hand-42]
        total_value += hand[total_hand-43]
        total_value += hand[total_hand-44]
        total_value += hand[total_hand-45]
        total_value += hand[total_hand-46]
        total_value += hand[total_hand-47]
        total_value += hand[total_hand-48]
        total_value += hand[total_hand-49]
        total_value += hand[total_hand-50]
        total_value += hand[total_hand-51]
        total_value += hand[total_hand-52]
        total_value += hand[total_hand-53]
        total_value += hand[total_hand-54]
        total_value += hand[total_hand-55]
        total_value += hand[total_hand-56]
        total_value += hand[total_hand-57]
        total_value += hand[total_hand-58]
        total_value += hand[total_hand-59]
        total_value += hand[total_hand-60]
        total_value += hand[total_hand-61]
        total_value += hand[total_hand-62]
        total_value += hand[total_hand-63]
        total_value += hand[total_hand-64]
        total_value += hand[total_hand-65]
        total_value += hand[total_hand-66]
        total_value += hand[total_hand-67]
        total_value += hand[total_hand-68]
        total_value += hand[total_hand-69

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
        if player_hand[0] == player_hand[1]:
            return 'Player wins'
        elif player_hand[0] > player_hand[1]:
            return 'Dealer wins'
        else:
            return 'Player wins'