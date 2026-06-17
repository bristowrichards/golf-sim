import random
from copy import deepcopy

# common definitions
ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Joker']
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 0, -5]
score_dict = dict(zip(ranks, scores))

# class definitions
class Card:
    '''
    This should instantiate a card with a suit and rank
    '''
    def __init__(self, rank:str, suit:str) -> None:
        self.rank = rank
        self.suit = suit

    def score(self) -> int:
        return(score_dict[self.rank])
    
    def __repr__(self) -> str:
        if self.rank != 'Joker':
            return f'{self.rank} of {self.suit}'
        else:
            return f'{self.suit} {self.rank}'
    
class Tile:
    '''
    This handles behavior of a card in front of a player
    '''
    def __init__(self, tile_pos:int, card:Card=None, known:bool=False, 
                 face_up:bool=False) -> None:
        self.tile_pos = tile_pos
        self.card = card
        self.known = known
        self.face_up = face_up
        self.is_pair = False

    def place_card(self, card:Card, deal:bool=False) -> None:
        self.card = card
        if not deal:
            self.flip_up()

    def flip_up(self) -> None:
        self.face_up = True
        self.known = True

    def peek(self, echo:bool=False) -> None:
        self.known = True
        if echo:
            print(self.card)

    def score(self, exp_value:float=5.7) -> int:
        if not self.known:
            return exp_value
        elif self.is_pair:
            return 0
        else:
            return self.card.score()

    def __repr__(self) -> str:
        if self.card is None:
            return 'EMPTY TILE'
        elif self.face_up:
            return repr(self.card)
        elif self.known:
            return f'Hidden: {repr(self.card)}'
        else:
            return 'XXXXXXXXXXXXX'

class Hand:
    '''
    This holds a grid of four Tiles, with methods to
    deal, exchange, and ultimately, score the hand
    '''
    def __init__(self) -> None:
        self.tiles = list(Tile(n) for n in range(4))

    def append(self, card:Card, deal:bool=True) -> None:
        # find index of next tile
        # I'm sure theres a less complex way to do this
        empty_tiles = list(t for t in self.tiles if t.card is None)
        next_tile_pos = empty_tiles[0].tile_pos

        # set next empty tile card to this card
        self.tiles[next_tile_pos].place_card(card, deal)

    def peek(self) -> None:
        self.tiles[0].peek()
        self.tiles[1].peek()

    def pair_handler(self) -> None:
        # count ranks
        rank_count = {r:0 for r in set(list(t.card.rank for t in self.tiles))}
        for t in self.tiles:
            t.is_pair = False
            if not t.known:
                continue
            r = t.card.rank
            rank_count[r] += 1

        for r, tally in rank_count.items():
            if tally == 4:
                for t in self.tiles:
                    t.is_pair = True
            elif tally > 1:
                pairs_candidates = list(
                    [i, t] for i, t in enumerate(self.tiles) if t.card.rank == r and t.known
                )
                pairs_candidates.sort( # return face-up first, since they are permenant
                    key = lambda x: -int(x[1].face_up)
                )
                for t in pairs_candidates[:2]: # choose the first two
                    t[1].is_pair = True

    def score(self, exp_value) -> int:
        self.pair_handler()
        score = sum(t.score(exp_value=exp_value) for t in self.tiles)
        return score
    
    def assess(self, card, exp_value, legal_actions) -> dict:
        new_card_score = card.score()
        self.pair_handler()

        hand_score_imputed = self.score(exp_value=exp_value)

        # set default options
        options = {i: hand_score_imputed for i in range(4)}

        # if hand is best, slightly prefer lowest known card
        for i in range(4):
            options[i] -= -.1 * self.tiles[i].score()

        # imagine known or unknown card replaced with draw pile
        # coupled with player swap method, which is a smell
        # limit to legal options 4-7
        for i in [j for j in range(4) if j+4 in legal_actions]:
            fake_hand = deepcopy(self)
            assert not fake_hand.tiles[i].face_up
            fake_hand.tiles[i].place_card(card)
            fake_hand.pair_handler()
            options[i+4] = fake_hand.score(exp_value=exp_value)

        # encourage exploration, a bit
        options[8] = hand_score_imputed - 1

        options = {k: round(v, 2) for k, v in options.items() if k in legal_actions}
        
        return options

    def __repr__(self) -> str:
        # should "hide" cards, show flipped state, locked state
        return repr(self.tiles)

class Deck:
    '''
    Instantiate a deck with shuffle and deal methods
    Reminder to make repr methods to show cards left
    And another method to extract list/dict at arbitrary time
    (I guess extracting Deck.deck also works. Would copy be an issue?)
    todo set seed?
    '''
    def __init__(self, shuffle:bool=True, jokers:bool=False) -> None:
        self.deck = self.new_deck(jokers=jokers)
        self.is_shuffled = False
        if shuffle:
            self.shuffle()
            self.is_shuffled = True
        self.expected_value = self._calculate_expected_value()

    def shuffle(self) -> None:
        random.shuffle(self.deck)
        self.is_shuffled = True

    def deal(self) -> Card: # should this be titled draw?
        return(self.deck.pop(0))

    def new_deck(self, jokers:bool=False) -> list[Card]:
        # not sure if this makes sense separate from init but wanted
        # ability to create it at will somehow, and separate that
        # from act of shuffling
        d = [Card(rank, suit) for rank in ranks[:-1] for suit in suits]
        if jokers:
            d.append(Card('Joker', 'Black'))
            d.append(Card('Joker', 'Red'))
        return d

    def reset(self) -> None:
        self.new_deck()
        self.shuffle()

    def _calculate_expected_value(self) -> float:
        ev = sum([c.score() for c in self.deck]) / len(self.deck)
        return ev

    def __repr__(self) -> str:
        return f'A deck of {len(self.deck)} card(s)'
    
class Discard:
    '''
    Handle discard pile (mostly handle when flipped exhaused)
    '''
    def __init__(self) -> None:
        self.pile = list()
        self.replenishable = True

    def stack(self, card:Card) -> None:
        # the non-replenish action (dealing, replacing)
        self.pile.append(card)
        self.replenishable = True

    def replenish(self, card:Card) -> None:
        self.pile.append(card)
        self.replenishable = False

    def __repr__(self) -> str:
        if len(self.pile) == 0:
            return 'Discard pile empty!'
        else:
            return (f'Discard Pile ({len(self.pile)} cards) '+
                    f'({"not " if not self.replenishable else ""}'+
                    f'replenishable): {repr(self.pile[-1])}') 

def main():
    pass

if __name__ == '__main__':
    main()