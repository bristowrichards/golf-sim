# import
import player
import cards

class Game:
    # yadda
    def __init__(self, players:list, label=None) -> None:
        assert isinstance(players, list)
        for p in players:
            assert isinstance(p, player.Player)
        self.players = players
        self.num_players = len(players) # is this necessary
        self.deck = cards.Deck()
        self.round = 1 # round in this context is one loop through players
        self.player_turn = 1 # turn is the individual player's turn
        self.label = label
        self.table = None

    def deal_hands(self) -> None:
        for i in range(4):
            for p in self.players:
                p.add_to_hand(self.deck.deal())

    def __repr__(self) -> str:
        return f'Game: round={self.round}, player_turn={self.player_turn}, label={self.label}'

def main():
    p1 = player.Player('Alice', 1)
    p2 = player.Player('Bob', 2)
    mygame = Game([p1, p2])
    
    print(mygame.deck)
    print(mygame.players[0].hand)
    print(mygame.players[1].hand)
    mygame.deal_hands()
    print(mygame.deck)
    print(mygame.players[0].hand)
    print(mygame.players[1].hand)
    

if __name__ == '__main__':
    main()
