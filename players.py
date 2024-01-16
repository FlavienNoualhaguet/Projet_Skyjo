from random import randint
from typing import List
from cards import Card, Deck

class Player:
    def __init__(self, id: int):
        self.id = id
        self.hand: List[Card] = []  # Player's hand, initially empty
        self.points = 0  # Player's points, initially 0

    def __eq__(self, other):
        return self.points == other.points
    
    def __le__(self, other):
        return self.points <= other.points

    def __ge__(self, other):
        return self.points >= other.points

    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        return not (self >= other)
    
    def __gt__(self, other):
        return not (self <= other)
    
    def deal_cards(self, deck: Deck, num_cards: int = 1):
        """Deal a specified number of cards from the deck."""
        deal_cards = []
        for _ in range(num_cards):
            card = deck.deal()
            deal_cards.append(card)
        self.hand.extend(deal_cards)

    def show_hand(self):
        """Display the player's current hand."""
        return f"{self.id}'s Hand: {[str(card) for card in self.hand]}"

    def count_points(self):
        """Count and update the player's points based on the cards in hand."""
        self.points = sum([card.value if card.returned else 0 for card in self.hand])
        return self.points
    
    def count_returned_card(self):
        returned_cards = [c for c in self.hand if c.is_returned()]
        return len(returned_cards)
    
    def start(self):
        for i in range(2): self.hand[i].switch_face()