# import

# the dimensions of choice seem to be:
# 1. valuation of unknown cards
# 2. tolerance for risk
# 3. bonus for keeping known cards
# 4. 'forgetfulness'
# 5. strategically denying cards that other players need (tbd...)
# strategies: 'basic'
# choices: 'flip', 

class Player:
    def __init__(self, name, pos, strategy='basic', risk_penalty=0, 
                 knowledge_bonus=0, forgetfulness=0) -> None:
        self.name = name
        self.pos = pos
        self.strategy = strategy # encoding strategy
        self.risk_penalty = risk_penalty
        self.knowledge_bonus = knowledge_bonus
        self.forgetfulness = forgetfulness # encoding forgetfulness

    def play_basic(self, state) -> str:
        # placeholder for having per-strategy play logic
        pass

    def play(self, state) -> str:
        pass

    def __repr__(self) -> str:
        return f'{self.name} is player {self.pos}'
