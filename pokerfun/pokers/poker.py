import random

from pokerfun.pokers.card import Card


class Poker:
    def __init__(self):
        self.deck = [Card(suit, value) for suit in Card.suits for value in Card.values]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        if num_cards > len(self.deck):
            raise ValueError("Not enough cards in the deck to deal")
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def __repr__(self):
        return f'Poker deck with {len(self.deck)} cards'
