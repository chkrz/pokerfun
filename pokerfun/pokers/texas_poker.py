from pokerfun.pokers.card import Card
from pokerfun.pokers.poker import Poker


class TexasPoker(Poker):
    def __init__(self):
        super().__init__()
        self.deck.extend([Card(suit, value) for suit in Card.suits for value in Card.values])

    def __repr__(self):
        return f'TexasPoker deck with {len(self.deck)} cards'
