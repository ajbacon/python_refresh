import unittest
import os.path
import sys

sys.path.append(os.path.abspath('.'))
from modules.deck_of_cards import Deck, Card


class DeckOfCardsTests(unittest.TestCase):
    def test_countt(self):
        deck = Deck()
        self.assertEqual(deck.count(), 52)


if __name__ == "__main__":
    unittest.main()
