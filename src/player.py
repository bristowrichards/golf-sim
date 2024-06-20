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
    def __init__(self, name:str, pos:int, strategy:str='basic', 
                 risk_penalty:float=0, knowledge_bonus:float=0, 
                 forgetfulness:float=0) -> None:
        self.name = name
        self.pos = pos
        self.hand = list()
        self.strategy = strategy # encoding strategy
        self.risk_penalty = risk_penalty
        self.knowledge_bonus = knowledge_bonus
        self.forgetfulness = forgetfulness # encoding forgetfulness
    
    def add_to_hand(self, card) -> None:
        assert isinstance(card, cards.Card)
        assert len(self.hand) < 4
        self.hand.append(card)

    def play_basic(self, state) -> str:
        # placeholder for having per-strategy play logic
        pass

    def play(self, state) -> str:
        pass

    def __repr__(self) -> str:
        return f'{self.name} (p{self.pos})'

def main():
    pass

if __name__ == '__main__':
    main()
