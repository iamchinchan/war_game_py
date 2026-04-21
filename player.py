from card import Card

# I consider the leftmost elements in card as Top card for playing and right most as bottom of player's and cards where more card weill be added during the game


class Player:
    def __init__(self, name):
        self.naame = name
        self.hand_cards = []

    def add_cards(self, played_cards: list[Card]):
        self.hand_cards.extend(played_cards)

    def draw_cards(self, number_of_cards):
        if len(self.hand_cards) >= number_of_cards:
            drawn_cards = self.hand_cards[:number_of_cards]
            del self.hand_cards[:number_of_cards]
            return (True, drawn_cards)
        else:
            drawn_cards = self.hand_cards
            self.hand_cards = []
            return (False, drawn_cards)
