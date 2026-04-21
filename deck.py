from card import Card
from globals import Suits, Ranks
from random import shuffle


class Deck:
    def __init__(self):
        self.deck_cards = []
        for suit in Suits:
            for rank in Ranks:
                self.deck_cards.append(Card(suit, rank))

    def deck_shuffle(self):
        shuffle(self.deck_cards)

    def draw_one(self):
        return self.deck_cards.pop()
