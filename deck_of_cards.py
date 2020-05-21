

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


card = Card("A", "Clubs")
print(card)
deck = Deck()
