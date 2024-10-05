# 先跑通一轮
from pokerfun.game import Game
from pokerfun.player import Player


# player1 = Player("a", 200)
# player2 = Player("b", 200)
# player3 = Player("b", 200)

game = Game(player_names=["a", "b", "c"], starting_balance=200)
game.play_hand()

