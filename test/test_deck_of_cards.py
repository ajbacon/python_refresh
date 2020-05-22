import unittest
import os.path
import sys

sys.path.append(os.path.abspath('.'))
from modules.deck_of_cards import Deck, Card


class DeckOfCardsTests(unittest.TestCase):
    def test_countt(self):
        deck = Deck()
        self.assertEqual(deck.count(), 52)

    def test_deal_card(self):
        deck = Deck()
        dealt = deck.deal_card()
        self.assertIsInstance(dealt, Card)
        self.assertEqual(deck.count(), 51)

    def test_deal_hand_success(self):
        deck = Deck()
        dealt = deck.deal_hand(2)
        self.assertEqual(len(dealt), 2)
        self.assertEqual(deck.count(), 50)
        self.assertIsInstance(dealt[0], Card)
        self.assertIsInstance(dealt[1], Card)

    def test_deal_hand_raise(self):
        deck = Deck()
        deck.deal_hand(52)
        self.assertRaises(ValueError, deck.deal_hand, 1)


if __name__ == "__main__":
    unittest.main()
