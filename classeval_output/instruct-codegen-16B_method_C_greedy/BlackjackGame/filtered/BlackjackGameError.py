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
        """
        deck = []
        for suit in ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
            '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
            'JD', 'QD', 'KD', 'AD',
            '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
            'AH', 'JH', 'QH', 'KH',
            'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
            'KC', 'QC', 'AC']:
            for value in range(2, 11):
                deck.append(suit + str(value))
        random.shuffle(deck)
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
        """
        total_value = 0
        aces_count = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                total_value += 10
            elif card == 'A':
                aces_count += 1
            else:
                total_value += int(card)
        for _ in range(aces_count):
            if total_value > 21:
                total_value -= 10
            else:
                break
        return total_value

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
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        if player_value > dealer_value:
            return 'Player wins'
        elif player_value < dealer_value:
            return 'Dealer wins'
        else:
            return 'Draw'