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
        
        deck = []
        for i in range(2, 11):
            deck.append(str(i) + "S")
            deck.append(str(i) + "H")
            deck.append(str(i) + "C")
            deck.append(str(i) + "D")
        for i in ["J", "Q", "K"]:
            deck.append(i + "S")
            deck.append(i + "H")
            deck.append(i + "C")
            deck.append(i + "D")
        random.shuffle(deck)
        return deck

    def deal_card(self):
        
        card = self.deck.pop()
        self.player_hand.append(card)
        self.dealer_hand.append(card)

    def show_hand(self):
        
        return "Player hand: {}\nDealer hand: {}".format(self.player_hand, self.dealer_hand)

    def show_hand_value(self):
        
        player_hand_value = self.calculate_hand_value(self.player_hand)
        dealer_hand_value = self.calculate_hand_value(self.dealer_hand)
        return "Player hand value: {}\nDealer hand value: {}".format(player_hand_value, dealer_hand_value)

    def show_winner(self):
        
        player_hand_value = self.calculate_hand_value(self.player_hand)
        dealer_hand_value = self.calculate_hand_value(self.dealer_hand)
        if player_hand_value > 21:
            return "Dealer wins!"
        elif dealer_hand_value > 21:
            return "Player wins!"
        elif player_hand_value > dealer_hand_value:
            return "Player wins!"
        elif dealer_hand_value > player_hand_value:
            return "Dealer wins!"
        else:
            return "It is a tie!"


    def calculate_hand_value(self, hand):


    def check_winner(self, player_hand, dealer_hand):
