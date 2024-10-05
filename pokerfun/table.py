from pokerfun.pokers.texas_poker import TexasPoker


class Table:
    def __init__(self, num_players):
        self.deck = TexasPoker()
        self.players = []
        self.pot = 0
        self.community_cards = []
        self.current_bet = 0
        self.round = 0  # 表示当前是第几轮下注
        self.dealer_position = 0

    def add_player(self, player):
        if len(self.players) >= 9:
            raise ValueError("Table is full")
        self.players.append(player)

    def start_new_hand(self):
        self.deck = TexasPoker()  # 重新洗牌
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.round = 0
        for player in self.players:
            player.hand = []
            player.current_bet = 0
            player.is_active = True

        self.dealer_position = (self.dealer_position + 1) % len(self.players)
        self.post_blinds()
        self.deal_hole_cards()

    def post_blinds(self):
        small_blind_position = (self.dealer_position + 1) % len(self.players)
        big_blind_position = (self.dealer_position + 2) % len(self.players)

        small_blind_amount = 10  # 假设小盲注为10
        big_blind_amount = 20  # 假设大盲注为20

        self.players[small_blind_position].bet(small_blind_amount)
        self.players[big_blind_position].bet(big_blind_amount)

        self.pot += small_blind_amount + big_blind_amount
        self.current_bet = big_blind_amount

    def deal_hole_cards(self):
        for player in self.players:
            player.receive_cards(self.deck.deal(2))

    def deal_flop(self):
        self.community_cards.extend(self.deck.deal(3))

    def deal_turn(self):
        self.community_cards.extend(self.deck.deal(1))

    def deal_river(self):
        self.community_cards.extend(self.deck.deal(1))

    def betting_round(self):
        for player in self.players:
            if player.is_active:
                # 简单示例：每个玩家都下注当前下注金额
                bet_amount = self.current_bet
                self.pot += player.bet(bet_amount)

    def next_round(self):
        if self.round == 0:
            self.deal_flop()
        elif self.round == 1:
            self.deal_turn()
        elif self.round == 2:
            self.deal_river()
        self.round += 1
        self.betting_round()

    def __repr__(self):
        return (f'Table with {len(self.players)} players, '
                f'Pot: {self.pot}, Community Cards: {self.community_cards}')
