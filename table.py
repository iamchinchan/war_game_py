from card import Card
from random import shuffle


class Table:
    def __init__(self):
        self.player1_cards: list[Card] = []
        self.player2_cards: list[Card] = []
        self.round_number = 0

    def __str__(self):
        return f"Round number: {self.round_number}"

    def __len__(self):
        return len(self.player1_cards) + len(self.player2_cards)

    def new_round(self):
        self.round_number += 1

    def add_cards(self, player1_cards: list[Card], player2_cards: list[Card]):
        self.player1_cards.extend(player1_cards)
        self.player2_cards.extend(player2_cards)

    def compare(self):
        if self.player1_cards[-1].value > self.player2_cards[-1].value:
            # player 1 won
            return "p1"
        elif self.player2_cards[-1].value > self.player1_cards[-1].value:
          # player 2 won
            return "p2"
        else:
            # Tie
            return "tie"

    def draw_table_cards(self):
        won_cards = self.player1_cards + self.player2_cards
        self.player1_cards = []
        self.player2_cards = []
        shuffle(won_cards)
        return won_cards
