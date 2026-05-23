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
        deck = []
        for suit in ['H', 'C', 'D', 'S']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                deck.append(rank + suit)
        deck = sorted(deck)
        return deck

    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
            40
        """
        total_value = 0
        for card in hand:
            if card.isdigit():
                total_value += int(card)
            else:
                if total_value > 21:
                    if 'A' in card:
                        total_value = 1
                    else:
                        total_value = 11
                else:
                    total_value = 11
        return total_value

    def check_winner(player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
        'Player wins'
        """
        total_value_player = self.calculate_hand_value(player_hand)
        total_value_dealer = self.calculate_hand_value(dealer_hand)
    
        if total_value_player > total_value_dealer:
            return "Player wins"
        elif total_value_player < total_value_dealer:
            return "Dealer wins"
        else:
            if 'A' in player_hand and 'A' in dealer_hand:
                return "Tie"
            else:
                return "Dealer wins"