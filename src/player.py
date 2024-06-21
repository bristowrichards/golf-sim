import cards

# the dimensions of choice seem to be:
# 1. valuation of unknown cards
# 2. tolerance for risk
# 3. bonus for keeping known cards
# 4. 'forgetfulness'
# 5. strategically denying cards that other players need (tbd...)
# strategies: 'basic'
# choices: 'flip', 

class Player:
    def __init__(self, name:str, pos:int = 0, strategy:str='basic', 
                 risk_penalty:float=0, knowledge_bonus:float=0, 
                 forgetfulness:float=0, controlled:bool = False) -> None:
        self.name = name
        self.pos = pos
        self.hand = cards.Hand()
        self.strategy = strategy # encoding strategy
        self.risk_penalty = risk_penalty
        self.knowledge_bonus = knowledge_bonus
        self.forgetfulness = forgetfulness # encoding forgetfulness
        self.controlled = controlled
    
    def add_to_hand(self, card) -> None:
        assert isinstance(card, cards.Card)
        self.hand.append(card)

    # def play_basic(self, game) -> int:
    #     # placeholder for having per-strategy play logic
    #     pass

    def swap_cards(self, incoming_card:cards.Card, tile_id:int) -> cards.Card:
        '''
        If player selects a swap card action (actions 4-7), this handles
        putting the card from the discard object into their tiles, while
        preparing their current tile card as a to-be-discarded object
        handled by the action handler in the Game object
        '''
        selected_tile = self.hand.tiles[tile_id]
        assert not selected_tile.locked
        outgoing_card = selected_tile.card # temp to not overwrite!
        selected_tile.card = incoming_card # player gets new card
        return(outgoing_card) # function returns outgoing card, which game handles


    def select_action(self, game) -> int:
        '''
        Allow player agent to intake information (of some format in the state) 
        and output some decision in the format of an int
        There are up to 16 choices a player can make: flip one of the four 
        tiles (0-3), exchange the discard card with one of the four tiles (4-7),
        or replenish the discard pile and take either of the preceding 8 
        actions (8-15). For simplicity, I plan to keep actions 0-7, then assign
        the 8 action to be replenish, so that the player can iterate through the
        first 8 actions.
        '''
        # at first, player will simply flip each tile sequentially with no strategy
        print(game) # just to debug
        self.hand.tiles[game.round].flip_up() # player will flip each round sequentially
        self.display_hand()

    def display_hand(self) -> None:
        print(self._hand_str())

    def display_score(self) -> None:
        print(f'{self.__repr__()}\'s score: {self._score()}')

    def peek(self) -> None:
        self.hand.peek()

    def _hand_str(self) -> str:
        return f'{self.__repr__()}\'s hand: {self.hand.__repr__()}'

    def _assign_pos(self, pos) -> None:
        self.pos = pos

    def _score(self) -> int:
        return(self.hand.score())

    def __repr__(self) -> str:
        return f'{self.name} (p{self.pos})'

def main():
    pass

if __name__ == '__main__':
    main()
