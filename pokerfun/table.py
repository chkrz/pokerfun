from pokerfun.pokers.texas_poker import TexasPoker


class Table:
    def __init__(self, max_num_players):
        self.max_num_players = max_num_players
        self.deck = TexasPoker()
        self.players = []
        self.pot = 0
        self.community_cards = []
        self.current_bet = 0
        self.round = 0  # 表示当前是第几轮下注
        self.dealer_position = 0
        self.current_stage = 'Pre-Flop'

    def play_hand(self):
        self.start_new_hand()
        self.betting_round()

        self.current_stage = 'Flop'
        self.next_round()
        self.betting_round()

        self.current_stage = 'Turn'
        self.next_round()
        self.betting_round()

        self.current_stage = 'River'
        self.next_round()
        self.betting_round()

        self.determine_winner()

    def add_player(self, player):
        if len(self.players) > self.max_num_players:
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
        self.current_stage = 'Pre-Flop'

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
                # player做行动
                # 到底需要什么info作为参数传入
                player.act(self.current_bet)

    def next_round(self):
        if self.round == 0:
            self.deal_flop()
        elif self.round == 1:
            self.deal_turn()
        elif self.round == 2:
            self.deal_river()
        self.round += 1
        self.betting_round()

    def determine_winner(self):
        # 最后给到的其实应该是active的人的ranks {0: , 1: , ...}
        pass
        # 不如直接返回 [[(), ()],[(), ()]]

    def distribute_pot(self, ranks):
        total_bet = 0
        for player in self.players:
            if player.is_active:
                total_bet += player.total_bet
        unit_bet_amount = self.pot/total_bet

        # 本质上是更高梯队的人 可以按照投入 分配低梯队的人的钱
        # 更高梯队的人，钱投入少的部分先claim, 平分
        level_amounts = []
        for i, rank in enumerate(level_amounts):
            level_count = len(rank)
            distributed = 0
            # 代表同一层上一轮已经分了的钱的数量
            current_amount = 0
            for ap in rank:
                ap[0] -= current_amount
                totals = 0
                if ap[0] == 0:
                    pass

                elif i + 1 >= len(level_amounts):
                    ap[1].balance += ap[0]
                    ap[0] = 0
                else:
                    for rank_ in level_amounts[i+1]:
                        for ap_ in rank_:
                            if ap_[0] <= ap[0]:
                                totals += ap_[0]
                                ap_[0] = 0
                            else:
                                ap_[0] -= ap[0]
                                totals += ap[0]
                    # 此时已经知道第一层可以claim的总量了
                    distributed += totals / level_count
                    ap[1].balance += distributed
                    current_amount += ap[0]

    def __repr__(self):
        return (f'Table with {len(self.players)} players, '
                f'Pot: {self.pot}, Community Cards: {self.community_cards}')
