from dataclasses import dataclass, field
from typing import List
from random import shuffle

@dataclass
class Card:
    value: int
    returned: bool

    def __eq__(self, other):
        return self.value == other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        return not (self >= other)
    
    def __gt__(self, other):
        return not (self <= other)

    def is_returned(self):
        return self.is_returned
    
    def switch_face(self):
        self.returned = not self.returned

@dataclass
class Deck:
    cards: List[Card] = field(default_factory=lambda: 
        [Card(v, False) for v in range(-2, -1) for _ in range(5)]
      + [Card(v, False) for v in range(-1, 13) for _ in range(10)]
      + [Card(v, False) for v in range(0,1) for _ in range(5)])

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"{self.__class__.__name__}(n={len(self)})"
    
    def initial_composition(self):
        composition = {}
        for v in range(-2, 13):
            quantity = 10 if v != -2 and v != 0 else 5 if v == -2 else 15
            composition[v] = quantity
        return composition

    def shuffle(self, n=1):
        for _ in range(n):
            shuffle(self.cards)

    def deal(self):
        card = self.cards.pop()
        return card
    
    def draw(self):
        card = self.cards.pop()
        card.switch_face()
        return card
    
    def current_composition(self):
        current_composition = {}
        for card in self.cards:
            current_composition[card.value] = current_composition.get(card.value, 0) + 1
        return current_composition
