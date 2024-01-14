# Import module unittest de python
import unittest

# Import de la fonction test
from unitarytest import run

# Imports des classes, fonctions à tester
from cards import Card, Deck
from players import Player
from game import Game

#-------------------------------
#---------- Test Card ----------
#-------------------------------
class TestCard(unittest.TestCase):

    def test_attributes(self):
        # Create an instance of MyClass
        card = Card(value=5, returned=True)
        
        # Get all attributes
        attributes = vars(card)
        
        # Assert that all attributes exist
        for attr, val in attributes.items():
            self.assertTrue(hasattr(card, attr))

            # Assert that my_attribute is initialized to the expected value
            if attr == "value": self.assertEqual(card.value, val)
            if attr == "returned": self.assertEqual(card.returned, val)

    def test_repr(self):
        card1 = Card(5, returned=True)
        card2 = Card(5, returned=False)

        expected_card_one = "Card(5)"
        expected_card_two = "Card(--)"

        result_one = repr(card1)
        result_two = repr(card2)

        self.assertEqual(result_one, expected_card_one, msg="Card returned True")
        self.assertEqual(result_two, expected_card_two, msg = "Card returned False")


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

    def test_switch_face(self):
        card = Card(value=5, returned=False)
        card.switch_face()
        self.assertTrue(card.is_returned())

#-------------------------------
#---------- Test Deck ----------
#-------------------------------
class TestDeck(unittest.TestCase):

    def test_attributes(self):
        # Create an instance of MyClass
        deck = Deck()
        
        # Get all attributes
        attributes = vars(deck)
        
        # Assert that all attributes exist
        for attr, val in attributes.items():
            self.assertTrue(hasattr(deck, attr))

            # Assert that my_attribute is initialized to the expected value
            if attr == "cards": self.assertEqual(deck.cards, val)
            
    def test_len(self):
        deck = Deck()
        # Assert that the deck contains 150 cards
        self.assertEqual(len(deck), 150)

    def test_repr(self):
        deck = Deck()
        result = repr(deck)
        expected_result = "Deck(n=150)"

        # Assert that the deck representation shows 150 cards
        self.assertEqual(result, expected_result)

    def test_initial_composition(self):
        deck = Deck()
        composition = deck.initial_composition()
        
        # Assert there are 15 possible values
        current_length    = len(composition)
        execpected_length = 15
        self.assertEqual(current_length, execpected_length)
        
        # Assert there are correct number for each value
        for k, v in composition.items():
            if k == -2:
                self.assertEqual(v, 5)
            elif k == 0:
                self.assertEqual(v, 15)
            else:
                self.assertEqual(v, 10)

    def test_shuffle(self):
        deck1=Deck()
        deck2=Deck()

        # Assert that the original decks are equal
        self.assertEqual(deck1, deck2)

        # Shuffle one of the decks
        deck1.shuffle()

        # Assert that the shuffled deck is not equal to the original deck
        self.assertNotEqual(deck1, deck2)

        # Sort both lists of cards and assert that they are equal (if they contain the same cards)
        deck1.cards.sort()
        deck2.cards.sort()
        
        self.assertEqual(deck1, deck2)

    def test_deal(self):
        deck = Deck()
        num_cards_before = len(deck)
    
        card = deck.deal()
        num_cards_after = len(deck)
        
        self.assertEqual(num_cards_after, num_cards_before - 1)

    def test_draw(self):
        deck = Deck()
        num_cards_before = len(deck)

        card = deck.draw()
        num_cards_after = len(deck)

        self.assertEqual(num_cards_after, num_cards_before - 1)
        self.assertTrue(card.is_returned())

    def test_current_composition(self):
        deck = Deck()
        
        init_compo = deck.initial_composition()
        current_compo_before = deck.current_composition()
        
        # Assert equality of composition at beggining
        self.assertDictEqual(current_compo_before, init_compo)

        # Take a card
        card = deck.draw()
        v = card.value
        current_compo_after = deck.current_composition()

        self.assertEqual(current_compo_after[v], current_compo_before[v]-1)

class TestPlayer(unittest.TestCase):

    def test_attributes(self):
        # Create an instance of MyClass
        player = Player(id=1)
        
        # Get all attributes
        attributes = vars(player)
        
        # Assert that all attributes exist
        for attr, val in attributes.items():
            self.assertTrue(hasattr(player, attr))

            # Assert that my_attribute is initialized to the expected value
            if attr == "id": self.assertEqual(player.id, 1)
            if attr == "hand": self.assertListEqual(player.hand, [])
            if attr == "points": self.assertEqual(player.points, 0)

    def test_deal_cards(self):
        player = Player(id=1)

        # Assert empty hand when instanciated
        self.assertListEqual(player.hand, [])

        # Take 12 cards
        num_cards_expected = 12
        deck = Deck()
        player.deal_cards(deck=deck, num_cards=num_cards_expected)
        
        num_cards_result = len(player.hand)
        # Assert player's hand has 12 cards

        self.assertEqual(num_cards_result, num_cards_expected)

        # Assert all card in hand are not returned
        for card in player.hand:
            self.assertFalse(card.is_returned())


    def test_show_hand(self):
        player = Player(id=1)
        
        result = player.show_hand()
        expected_result = "1's Hand: []"

        self.assertEqual(result, expected_result)

    def test_count_points(self):
        player = Player(id=1)
        
        # Assert points at beggining
        expected_points = 0
        result = player.count_points()
        self.assertEqual(result, expected_points, msg="Init point")

        # Assert points when cards on hand
        deck = Deck()
        player.deal_cards(deck, num_cards=6)

        expected_points = 0
        result = player.count_points()
        self.assertEqual(result, expected_points, msg="Dealing 6 cards")

        player.hand[-1].switch_face()
        expected_points = 12
        result = player.count_points()
        self.assertEqual(result, expected_points, msg="Dealing 6 cards and switch the last one")

    def test_eq(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 15
        player2.points = 15

        self.assertEqual(player1, player2)

    def test_le(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertLessEqual(player1, player2)
        self.assertFalse(player2 <= player1)

    def test_ge(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertGreaterEqual(player2, player1)
        self.assertFalse(player1 >= player2)

    def test_lt(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertLess(player1, player2)
        self.assertFalse(player2 < player1)

    def test_gt(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertGreater(player2, player1)
        self.assertFalse(player1 > player2)

    def test_lt(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertLess(player1, player2)
        self.assertFalse(player2 < player1)

    def test_ne(self):
        player1=Player(id=1)
        player2=Player(id=2)

        player1.points = 10
        player2.points = 15

        self.assertNotEqual(player1, player2)
        self.assertTrue(player1 != player2)
        self.assertFalse(player1 == player2)

    def test_count_returned_card(self):
        player = Player(id=1)
        deck   = Deck()
        player.deal_cards(deck, 12)

        # Assert 0 card are returned when dealed
        expected_returned_card = 0
        result_num_returned_card = player.count_returned_card()

        self.assertEqual(result_num_returned_card, expected_returned_card)

        # Assert 4 cards are returned when switch face         
        for i in range(4):
            player.hand[i].switch_face()
        
        expected_returned_card = 4
        result_num_returned_card = player.count_returned_card()

        self.assertEqual(result_num_returned_card, expected_returned_card)


    def test_start(self):
        player = Player(id=1)
        player.deal_cards(Deck(), 12)

        excepted_returned_card = 0
        result_num_returned_card = player.count_returned_card()

        self.assertEqual(result_num_returned_card, excepted_returned_card)

        # Assert player.start() returned 2 cards
        player.start()
        excepted_returned_card = 2
        result_num_returned_card = player.count_returned_card()

        self.assertEqual(result_num_returned_card, excepted_returned_card)

class TestGame(unittest.TestCase):


    def test_attributes(self):
        players = [Player(id=i) for i in range(2)]
        deck    = Deck()
        defausse = []
        num_cards_before = len(deck)

        game = Game(players=players, deck=deck, defausse=defausse)

        attributes = vars(game)

        for attr, val in attributes.items():
            if attr == "players": self.assertListEqual(game.players, val)
            if attr == "deck": self.assertEqual(game.deck, val)
            if attr == "defausse": self.assertEqual(game.defausse, val)


    def test_start(self):
        players = [Player(id=i) for i in range(2)]
        deck    = Deck()
        defausse = []
        num_cards_before = len(deck)
        
        game = Game(players=players, deck=deck, defausse=defausse)

        game.start()

        # Assert each player has 12 cards in hand all returned false
        expected_num_cards_hand = 12
        for p in players:
            result_num_cards_hand   = len(p.hand)
            self.assertEqual(result_num_cards_hand, expected_num_cards_hand)

            # Assert all card in hand are not returned
            for c in p.hand:
                self.assertFalse(c.is_returned())

        # Assert there are left cards in deck
        num_players = len(players)

        expected_num_cards_draw = expected_num_cards_hand * num_players
        result_num_cards_deck = len(deck)
        
        self.assertEqual(result_num_cards_deck, num_cards_before - expected_num_cards_draw)

    def test_start_players(self):
        players = [Player(id=i) for i in range(2)]
        deck = Deck()
        defausse = []

        # Initialise game and start game
        game = Game(players, deck, defausse)
        game.start()

        # Start each player
        game.start_players()

        expected_returned_card = 2
        for player in players:
            result_num_returned_card = player.count_returned_card()
            self.assertEqual(result_num_returned_card, expected_returned_card)


    def test_play(self):
        players = [Player(id=i**2) for i in range(2,4)]
        deck    = Deck()
        game    = Game(players, deck, [])

        game.start()
        game.start_players()
        
        for (i ,player) in enumerate(players):
            print(player.show_hand())
        print(game.play())
        
#-------------------------------
#---------- MAIN PART ----------
#-------------------------------
def main():
    objs = [TestCard, TestDeck, TestPlayer, TestGame]
    run(objs)

if __name__ == "__main__":
    main()