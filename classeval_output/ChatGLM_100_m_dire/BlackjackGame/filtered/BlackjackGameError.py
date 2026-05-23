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
        return ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'A2', 'A9', 'B2', 'B9',
               'C2', 'C9', 'D2', 'D9', 'E2', 'E9', 'F2', 'F9', 'G2', 'G9', 'H2', 'H9',
               'I2', 'I9', 'J2', 'J9', 'K2', 'K9', 'L2', 'L9', 'M2', 'M9', 'N2', 'N9',
               'O2', 'O9', 'P2', 'P9', 'Q2', 'Q9', 'R2', 'R9', 'S2', 'S9', 'T2', 'T9',
               'U2', 'U9', 'V2', 'V9', 'W2', 'W9', 'X2', 'X9', 'Y2', 'Y9', 'Z2', 'Z9',
               'A10', 'A10.2', 'A10.9', 'B10.2', 'B10.9', 'C10.2', 'C10.9', 'D10.2',
               'D10.9', 'E10.2', 'E10.9', 'F10.2', 'F10.9', 'G10.2', 'G10.9', 'H10.2',
               'H10.9', 'I10.2', 'I10.9', 'J10.2', 'J10.9', 'K10.2', 'K10.9', 'L10.2',
               'L10.9', 'M10.2', 'M10.9', 'N10.2', 'N10.9', 'O10.2', 'O10.9', 'P10.2',
               'P10.9', 'Q10.2', 'Q10.9', 'R10.2', 'R10.9', 'S10.2', 'S10.9', 'T10.2',
               'T10.9', 'U10.2', 'U10.9', 'V10.2', 'V10.9', 'W10.2', 'W10.9', 'X10.2',
               'X10.9', 'Y10.2', 'Y10.9', 'Z10.2', 'Z10.9', 'A10.10', 'A10.10.2', 'A10.10.9',
               'B10.10.2', 'B10.10.9', 'C10.10.2', 'C10.10.9', 'D10.10.2', 'D10.10.9',
               'E10.10.2', 'E10.10.9', 'F10.10.2', 'F10.10.9', 'G10.10.2', 'G10.10.9',
               'H10.10.2', 'H10.10.9', 'I10.10.2', 'I10.10.9', 'J10.10.2', 'J10.10.9',
               'K10.10.2', 'K10.10.9', 'L10.10.2', 'L10.10.9', 'M10.10.2', 'M10.10.



    def check_winner(self, player_hand, dealer_hand):
        """
        Determines the winner of a game by comparing the hand values of the player and dealer.
        rule:
        If both players have hand values that are equal to or less than 21, the winner is the one whose hand value is closer to 21.
         Otherwise, the winner is the one with the lower hand value.
        :param player_hand: list
        :param dealer_hand: list
        :return: the result of the game, only two certain str: 'Dealer wins' or 'Player wins'
        """
        if player_hand[0] == dealer_hand[0] and player_hand[-1] <= 21 and dealer_hand[-1] <= 21:
            return 'Dealer wins'
        elif player_hand[0] < dealer_hand[0] and player_hand[-1] > 21 and dealer_hand[-1] < 21:
            return 'Player wins'
        else:
            return 'Unknown'