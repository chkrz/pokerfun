import random

from pokerfun.player import Player
from pokerfun.table import Table


class Game:
    def __init__(self, player_names, starting_balance):
        self.players = [Player(name, starting_balance) for name in player_names]
        self.table = Table(len(self.players))
        for player in self.players:
            self.table.add_player(player)
        self.current_stage = 'Pre-Flop'
        self.winner = None

    def add_player(self, player):
        self.players.append(player)
        self.table.add_player(player)

    def play_hand(self):
        self.table.start_new_hand()
        self.betting_round()

        self.current_stage = 'Flop'
        self.table.next_round()
        self.betting_round()

        self.current_stage = 'Turn'
        self.table.next_round()
        self.betting_round()

        self.current_stage = 'River'
        self.table.next_round()
        self.betting_round()

        self.determine_winner()

    def betting_round(self):
        for player in self.table.players:
            if player.is_active:
                # 调用player做操作
                # 必要的信息有 1. call 跟平, game需要记录当轮已投入, 还差多少跟平
                #
                bet_amount = self.table.current_bet
                self.table.pot += player.bet(bet_amount)
                player.fold()

    def determine_winner(self):
        # 简化胜利者确定逻辑：随机选择一个还在游戏中的玩家
        active_players = [player for player in self.table.players if player.is_active]
        if active_players:
            self.winner = random.choice(active_players)
            self.winner.balance += self.table.pot
            print(f'{self.winner.name} wins the pot of {self.table.pot}')
        else:
            print('No active players left.')

    def __repr__(self):
        return (f'Game with {len(self.players)} players, '
                f'Current Stage: {self.current_stage}, '
                f'Pot: {self.table.pot}, '
                f'Community Cards: {self.table.community_cards}')
