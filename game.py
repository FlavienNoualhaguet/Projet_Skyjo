from dataclasses import dataclass, field
from typing import List

from cards import Card, Deck
from players import Player

@dataclass
class Game:
    players: List[Player]
    deck: Deck
    defausse: List[Card]
    
    def start(self):
        # Shuffle deck
        num_shuffle = len(self.players)
        self.deck.shuffle(num_shuffle)
        # Draw card
        for _ in range(12):
            for player in self.players:
                player.deal_cards(deck=self.deck, num_cards=1)

    def start_players(self):
        for player in self.players:
            player.start()