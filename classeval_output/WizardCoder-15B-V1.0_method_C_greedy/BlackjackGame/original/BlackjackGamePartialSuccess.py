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
        for suit in ['H', 'D', 'C', 'S']:
            for value in range(2, 15):
                deck.append(str(value) + suit)
        deck.append('AS')
        deck.append('JS')
        deck.append('QS')
        deck.append('KS')
        deck.append('AD')
        deck.append('JD')
        deck.append('QD')
        deck.append('KD')
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
        aces = 0
        for card in hand:
            if card[0] in ['J', 'Q', 'K']:
                total_value += 10
            elif card[0] == 'A':
                aces += 1
                total_value += 11
            else:
                total_value += int(card[0])
        while total_value > 21 and aces > 0:
            total_value -= 10
            aces -= 1
        return total_value

    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        if player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        elif player_value > dealer_value:
            return 'Player wins'
        elif player_value < dealer_value:
            return 'Dealer wins'
        else:
            return 'Tie'