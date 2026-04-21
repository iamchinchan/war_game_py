from globals import Values


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Values[rank]
