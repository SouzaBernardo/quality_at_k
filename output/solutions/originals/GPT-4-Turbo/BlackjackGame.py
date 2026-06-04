```python
import random
class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        suits = ['S', 'H', 'D', 'C']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [rank + suit for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card[0] in 'JQK':
                value += 10
            elif card[0] == 'A':
                value += 11
                aces += 1
            else:
                value += int(card[:-1])
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        if player_value > 21:
            if dealer_value > 21:
                return 'Dealer wins'
            else:
                return 'Player wins'
        else:
            if dealer_value > 21 or dealer_value < player_value:
                return 'Player wins'
            else:
                return 'Dealer wins'
```