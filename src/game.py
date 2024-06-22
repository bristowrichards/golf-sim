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

    def setup_game(self) -> None:
        self.deal_hands()
        for p in self.players:
            p.peek()
        self._flip()
    
    def next_player_go(self) -> None:
        p = self.players[self.player_turn]
        action = p.select_action(self)
        self._action_handler(action)

    def play(self) -> None:
        self.setup_game()
        while self.round < 4:
            self.next_player_go()
            self._increment_turn()
        else:
            self._end_game()
        pass
    
    def _increment_turn(self) -> None:
        if self.player_turn == len(self.players) - 1:
            self.player_turn = 0
            self.round += 1
        else:
            self.player_turn += 1    

    def _action_handler(self, player_action:int) -> None:
        p = self.players[self.player_turn]
        if player_action == 8:
            self._flip()
            self.next_player_go() # recursive but 8 won't be legal
        elif player_action in range(4):
            p.flip_up(player_action)
        else:
            self._card_exchange(p, player_action % 4)

    def _card_exchange(self, player:player.Player, tile_id:int) -> None:
        card_to_player = self.discard.pile[-1]
        card_from_player = player.swap_cards(card_to_player, tile_id) # does swap
        self.discard.stack(card_from_player)

    def _end_game(self) -> None:
        print('\n\n-------- Game Over! --------\n\n')
        for p in self.players:
            p.display_hand()
            p.display_score()
    
    def _flip(self) -> None:
        self.discard.stack(self.deck.deal())
    
    def _replenish(self) -> None:
        self.discard.replenish(self.deck.deal())

    def __repr__(self) -> str:
        game_str = (f'\nGame: round={self.round}, player_turn={self.player_turn} '+
                f'({self.players[self.player_turn].name}), id={self.id}')
        discard_str = ''
        if len(self.discard.pile) > 0:
            discard_str = f', Discard showing=[{self.discard.pile[-1]}]'
        return game_str + discard_str

def main():
    p1 = player.Player('Alice')
    p2 = player.Player('Bob')
    # p3 = player.Player('Charlie')
    mygame = Game([p1, p2])

    print(mygame)

    mygame.play()

if __name__ == '__main__':
    main()
