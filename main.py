from players import Player
from cards import Deck
from game import Game


def main():
    players = [Player(id=id) for id in range(2)]
    deck    = Deck()
    game    = Game(players, deck, [])

    # Start the game : suffle deck and deal cards
    game.start()
    # Start all players : face up two cards for each player
    game.start_players()
    # Start rounds : the player having the less point start round
    game.play()

if __name__ == "__main__":
    main()
