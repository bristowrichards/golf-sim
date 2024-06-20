import random

# common definitions
ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
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
        if self.face_up:
            return self.card.__repr__()
        elif self.known:
            return f'Hidden: {self.card.__repr__()}'
        else:
            return 'XXXXXXXXXXXXX'

# class Hand:
#     '''
#     This should allow four Card objects to be given attributes
#     Like position, flipped/"locked" status, and "known" status
#     (how players treat difference between known flipped and known
#     private cards I am not sure)
#     '''
#     def __init__(self) -> None:
#         self.hand = dict(
#             0 : (None, 'top left'),
#             1 : 
#         )

#     def append(self, Card) -> None:
#         pass

#     def __repr__(self) -> str:
#         # should "hide" cards, show flipped state, locked state
#         pass


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
        d = [Card(rank, suit) for rank in ranks for suit in suits]
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
    mydeck = Deck(shuffle=False, jokers=False)
    mytile = Tile(0)
    mytile.place_card(mydeck.deal(), deal=True)
    print('tile at first')
    print(mytile)
    mytile.peek()
    print(mytile)
    mytile.flip_up()
    print(mytile)

if __name__ == '__main__':
    main()