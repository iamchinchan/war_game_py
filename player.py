from card import Card

# I consider the leftmost elements in card as Top card for playing and right most as bottom of player's and cards where more card weill be added during the game


class Player:
    def __init__(self, name):
        self.name = name
        self.hand_cards = []

    def get_name(self):
        return self.name

    def add_card(self, card: Card):
        self.hand_cards.append(card)

    def add_won_cards(self, played_cards: list[Card]):
        self.hand_cards.extend(played_cards)

    def __len__(self):
        return len(self.hand_cards)

    def has_sufficient_war_cards(self, number_of_cards_in_war):
        return len(self.hand_cards) >= number_of_cards_in_war

    def draw_cards(self, number_of_cards):
        if len(self.hand_cards) >= number_of_cards:
            drawn_cards = self.hand_cards[:number_of_cards]
            del self.hand_cards[:number_of_cards]
            return (drawn_cards)
        else:
            # wont ever come here according to game logic but added this just for safety
            return []
        # [] is also a falsy value
