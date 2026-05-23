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
        for i in range(2, 11):
            deck.append(str(i) + 'S')
            deck.append(str(i) + 'H')
            deck.append(str(i) + 'C')
            deck.append(str(i) + 'D')
        for i in range(2, 11):
            deck.append(str(i) + 'D')
            deck.append(str(i) + 'C')
            deck.append(str(i) + 'H')
            deck.append(str(i) + 'S')
        deck.append('JC')
        deck.append('JD')
        deck.append('JH')
        deck.append('JS')
        deck.append('QC')
        deck.append('QD')
        deck.append('QH')
        deck.append('QS')
        deck.append('KC')
        deck.append('KD')
        deck.append('KH')
        deck.append('KS')
        deck.append('AC')
        deck.append('AD')
        deck.append('AH')
        deck.append('AS')
        random.shuffle(deck)
        return deck


    def deal_card(self):


    def calculate_hand_value(self, hand):


    def check_winner(self, player_hand, dealer_hand):