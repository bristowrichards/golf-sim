# import
import player
import cards

class Game:
    # yadda
    def __init__(self, players:list, id=None) -> None:
        assert isinstance(players, list)
        for p in enumerate(players):
            assert isinstance(p[1], player.Player)
            assert len(p) <= 3 # max 4 players for now
            p[1]._assign_pos(p[0]) # assign player position from enumerate order
        self.players = players
        self.num_players = len(players) # is this necessary
        self.deck = cards.Deck()
        self.discard = cards.Discard()
        self.round = 0 # round in this context is one loop through players
        self.player_turn = 0 # turn is the individual player's turn
        self.id = id

    def deal_hands(self) -> None:
        for i in range(4):
            for p in self.players:
                p.add_to_hand(self.deck.deal())

    def start_game(self) -> None:
        self.deal_hands()
        for p in self.players:
            p.peek()
        self._flip()
    
    def _flip(self) -> None:
        self.discard.stack(self.deck.deal())

    def __repr__(self) -> str:
        return (f'Game: round={self.round}, player_turn={self.player_turn} '+
                f'({self.players[self.player_turn].name}), id={self.id}')

def main():
    pass

if __name__ == '__main__':
    main()
