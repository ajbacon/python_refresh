import unittest
import os.path
import sys

sys.path.append(os.path.abspath('.'))
from modules.deck_of_cards import Deck, Card


class DeckOfCardsTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_countt(self):
        self.assertEqual(self.deck.count(), 52)

    def test_deal_card(self):
        dealt = self.deck.deal_card()
        self.assertIsInstance(dealt, Card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand_success(self):
        dealt = self.deck.deal_hand(2)
        self.assertEqual(len(dealt), 2)
        self.assertEqual(self.deck.count(), 50)
        self.assertIsInstance(dealt[0], Card)
        self.assertIsInstance(dealt[1], Card)

    def test_deal_hand_raise(self):
        self.deck.deal_hand(52)
        self.assertRaises(ValueError, self.deck.deal_hand, 1)


if __name__ == "__main__":
    unittest.main()
