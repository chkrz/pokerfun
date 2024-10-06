import random


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []
        # 当轮的投入和这局的总投入
        self.current_bet = 0
        self.total_bet = 0
        self.is_active = True  # 表示玩家是否在当前牌局中

    def act(self, pot, bet_amount):
        # 根据牌桌信息，来决定策略
        # 先随机
        # if self.balance == 0:

        actions = ["allin", "raise_", "fold"]
        prob = ["0.05", "0.8", "0.15"]
        if bet_amount >= self.balance:
            actions = ["allin", "fold"]
            prob = [0.7, 0.3]
        elif bet_amount > self.current_bet:
            actions = ["call", "raise_", "allin", "fold"]
            prob = [0.4, 0.4, 0.05, 0.15]
        elif bet_amount == 0:
            actions = ["check", "raise_", "allin"]
            prob = [0.45, 0.45, 0.1]
        chosen_action = random.choices(actions, weights=prob, k=1)[0]
        # 确定钱

        if chosen_action == "raise_":
            amount = bet_amount + 1
        elif chosen_action == "call":
            amount = bet_amount

        if chosen_action in ["raise_", "call"]:
            getattr(self, chosen_action)(amount)
        else:
            getattr(self, chosen_action)

    def check(self):
        amount = self.bet(0)
        return amount

    def call(self, bet_amount):
        amount = self.bet(bet_amount - self.current_bet)
        return amount

    def raise_(self, amount):
        amount = self.bet(amount)
        return amount

    def bet(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance to bet")
        self.balance -= amount
        self.current_bet += amount
        return amount

    def fold(self):
        self.is_active = False
        self.hand = []
        self.current_bet = 0

    def allin(self):
        self.current_bet += self.balance
        self.balance = 0

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def __repr__(self):
        return f'Player({self.name}, Balance: {self.balance}, Hand: {self.hand})'
