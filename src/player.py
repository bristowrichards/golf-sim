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
                 forgetfulness:float=0) -> None:
        self.name = name
        self.pos = pos
        self.hand = cards.Hand()
        self.strategy = strategy # encoding strategy
        self.risk_penalty = risk_penalty
        self.knowledge_bonus = knowledge_bonus
        self.forgetfulness = forgetfulness # encoding forgetfulness
    
    def add_to_hand(self, card) -> None:
        assert isinstance(card, cards.Card)
        self.hand.append(card)

    def play_basic(self, state) -> int:
        # placeholder for having per-strategy play logic
        pass

    def play(self, state) -> int:
        # I'm thinking that for this, the player will return a value
        # between 1-9, 1-4 being flip cards 1-4, 5-8 being
        # exchange discard card for cards 1-4, and 9 being flip new
        # card onto discard card (if available)
        pass

    def display_hand(self) -> None:
        print(self._hand_str())

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
