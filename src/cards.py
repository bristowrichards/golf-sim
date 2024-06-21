import random

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
                 face_up:bool=False, locked:bool=False) -> None:
        self.tile_pos = tile_pos
        self.card = card
        self.known = known
        self.face_up = face_up
        self.locked = locked

    def place_card(self, card:Card, deal:bool=False) -> None:
        self.card = card
        if not deal:
            self.flip_up()

    def flip_up(self) -> None:
        self.face_up = True
        self.known = True
        self.locked = True

    def peek(self, echo:bool=False) -> None:
        self.known = True
        if echo:
            print(self.card)

    def __repr__(self) -> str:
        if self.card is None:
            return 'EMPTY TILE'
        elif self.face_up:
            return self.card.__repr__()
        elif self.known:
            return f'Hidden: {self.card.__repr__()}'
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

    def score(self) -> int:
        # this needs pair logic!
        score = sum(c.score() for c in self.tiles.card)
        return score

    def __repr__(self) -> str:
        # should "hide" cards, show flipped state, locked state
        return self.tiles.__repr__()


class Deck:
    '''
    Instantiate a deck with shuffle and deal methods
    Reminder to make repr methods to show cards left
    And another method to extract list/dict at arbitrary time
    (I guess extracting Deck.deck also works. Would copy be an issue?)
    todo don't give Jokers suits! 
    todo make option to exclude Jokers!
    todo set seed?
    '''
    def __init__(self, shuffle:bool=True, jokers:bool=False) -> None:
        self.deck = self.new_deck(jokers=jokers)
        self.is_shuffled = False
        if shuffle:
            self.shuffle()
            self.is_shuffled = True

    def shuffle(self) -> None:
        random.shuffle(self.deck)
        self.is_shuffled = True

    def deal(self) -> Card:
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

    def __repr__(self) -> str:
        return f'A deck of {len(self.deck)} card(s)'

def main():
    pass

if __name__ == '__main__':
    main()