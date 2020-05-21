

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = self._create_deck()

    def _create_deck(self):
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        return [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        to_deal = min([count, num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        dealt = self.cards[-to_deal:]
        del self.cards[-to_deal:]
        # self.cards = self.cards[:-to_deal]
        print(self.cards)
        return dealt


card = Card("A", "Clubs")
print(card)
deck = Deck()
print(deck.count())
deck._deal(1)
