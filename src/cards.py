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
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def score(self) -> int:
        return(score_dict[self.rank])
    
    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

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
    def __init__(self, shuffle=True) -> None:
        self.deck = self.new_deck()
        self.is_shuffled = False
        if shuffle:
            self.shuffle()
            self.is_shuffled = True

    def shuffle(self) -> None:
        random.shuffle(self.deck)
        self.is_shuffled = True

    def deal(self) -> Card:
        return(self.deck.pop(0))

    def new_deck(self) -> list[Card]:
        # not sure if this makes sense separate from init but wanted
        # ability to create it at will somehow, and separate that
        # from act of shuffling
        return([Card(rank, suit) for rank in ranks for suit in suits])

    def reset(self) -> None:
        self.new_deck()
        self.shuffle()

    def __repr__(self) -> str:
        return f'A deck of {len(self.deck)} card(s)'

def main():
    mydeck = Deck()
    print(mydeck.deal())

if __name__ == '__main__':
    main()