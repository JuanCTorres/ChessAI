# pip3 install python-chess
import random
from time import sleep

import chess
from src.RandomAI import RandomAI
from src.HumanPlayer import HumanPlayer
from src.MinimaxAI import MinimaxAI
from src.AlphaBetaAI import AlphaBetaAI
from src.ChessGame import ChessGame

import sys

# player1 = HumanPlayer()
# player2 = RandomAI()
# player2 = MinimaxAI(3, chess.COLORS[1]) # black
# player2 = AlphaBetaAI(5)

WHITE = 1
BLACK = 0
# player1 = MinimaxAI(2, WHITE)
# # player2 = MinimaxAI(4, BLACK)
# # player2 = IterativeMinimaxAI(3, BLACK)
# # player
# player2 = AlphaBetaAI(max_depth=4, color=BLACK, shuffle_moves=True, use_transposition=True)

# player1 = MinimaxAI(2, WHITE, shuffle_moves=False)
if __name__ == '__main__':
    random.seed(1)
    player1 = RandomAI()
    player2 = AlphaBetaAI(max_depth=3, color=BLACK, shuffle_moves=False, use_transposition=True)
    # player2 = MinimaxAI(3, BLACK)

    game = ChessGame(player1, player2)

    i = 0
    while not game.is_game_over():
        print(i)
        print('ab' if isinstance(player2, AlphaBetaAI) else 'mm')
        if i == 41:
            sleep(2)
        print(game)
        game.make_move()
        # sleep(1)
        print('------------------')
        i += 1


        # print(hash(str(game.board)))
