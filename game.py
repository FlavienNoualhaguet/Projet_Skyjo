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

    def play(self):
        # Starting player is the one having the less points
        i_player_starting, _ = min(enumerate(self.players), 
                                 key=lambda x: x[1].count_points())
        return i_player_starting