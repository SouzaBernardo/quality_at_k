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
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        deck = []
        for i in range(2):
            for j in range(2):
                deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
        deck.append(random.randint(1, 11))
       

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
                if 'A' in card:
                    if 'A' not in hand:
                        if total_value > 21:
                            total_value = 21
                        else:
                            total_value = 1
                else:
                    if '1' in card:
                        if '1' not in hand:
                            total_value = 1
                        else:
                            total_value += 1
        return total_value

    def check_winner(player_hand, dealer_hand):
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