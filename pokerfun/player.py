class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []
        self.current_bet = 0
        self.is_active = True  # 表示玩家是否在当前牌局中

    def act(self, info):
        # 根据牌桌信息，来决定策略
        # 先随机
        actions = ["bet", "fold", "allin"]
        prob = [0.45, 0.45, 0.1]

    def check(self):
        pass

    def call(self):
        pass

    def raise_(self):
        pass

    def bet(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance to bet")
        self.balance -= amount
        self.current_bet += amount
        return amount

    def fold(self):
        self.is_active = False
        self.hand = []

    def allin(self):
        self.current_bet += self.balance
        self.balance = 0

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def __repr__(self):
        return f'Player({self.name}, Balance: {self.balance}, Hand: {self.hand})'
