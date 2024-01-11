from dataclasses import dataclass, field
from typing import Dict, List

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

@dataclass
class Deck:
    cards: Dict[int, list[Card]] = field(default_factory=lambda: {
        v: [Card(value=v, returned=False)] * 15 if v == 0 else [Card(value=v, returned=False)] * 5 if v == -2 else [Card(value=v, returned=False)] * 10
        for v in range(-2, 13)
    })

    def __repr__(self):
        _repr = {v: len(self.cards[v]) for v in range(-2, 13)}
        return f"Deck(cards={_repr})"

    def __len__(self):
        return sum(len(card_list) for card_list in self.cards.values())


    def shuffle(self, n):
        

