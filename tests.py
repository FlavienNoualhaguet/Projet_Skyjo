# Import module unittest de python
import unittest

# Import de la fonction test
from unitarytest import run

# Imports des classes, fonctions à tester
from cards import Card, Deck

#-------------------------------
#---------- Test Card ----------
#-------------------------------
class TestCard(unittest.TestCase):

    def test_eq(self):
        card1 = Card(value=5, returned=True)
        card2 = Card(value=5, returned=False)
        self.assertEqual(card1, card2)

    def test_lt(self):
        card1 = Card(value=5, returned=True)
        card2 = Card(value=7, returned=False)
        self.assertLess(card1, card2)
        self.assertFalse(card2 < card1)

    def test_gt(self):
        card1 = Card(value=5, returned=True)
        card2 = Card(value=7, returned=False)
        self.assertGreater(card2, card1)
        self.assertFalse(card1 > card2)

    def test_le(self):
        card1 = Card(value=5, returned=True)
        card2 = Card(value=7, returned=False)
        self.assertLessEqual(card1, card2)
        self.assertFalse(card2 <= card1)

    def test_ge(self):
        card1 = Card(value=5, returned=True)
        card2 = Card(value=7, returned=False)
        self.assertGreaterEqual(card2, card1)
        self.assertFalse(card1 >= card2)

    def test_is_returned(self):
        card = Card(value=5, returned=True)
        self.assertTrue(card.is_returned())
        self.assertFalse(not card.is_returned())


#-------------------------------
#---------- Test Card ----------
#-------------------------------
class TestDeck(unittest.TestCase):

    def test_repr(self):
        deck = Deck()
        result = repr(deck)
        expected_result = "Deck(cards={-2: 5, -1: 10, 0: 15, 1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10, 10: 10, 11: 10, 12: 10})"
        self.assertEqual(result, expected_result)
    
    def test_len(self):
        deck = Deck()
        self.assertEqual(len(deck), 150)



#-------------------------------
#---------- MAIN PART ----------
#-------------------------------
def main():
    objs = [TestCard, TestDeck]
    run(objs)

if __name__ == "__main__":
    main()