"""
Author: Juan C. Torres, based on code by Devin Balkcom
October 2017
"""
from time import sleep
from src.RandomAI import RandomAI
from src.HumanPlayer import HumanPlayer
from src.MinimaxAI import MinimaxAI
from src.AlphaBetaAI import AlphaBetaAI
from src.ChessGame import ChessGame

import sys

WHITE = 1
BLACK = 0
# player1 = MinimaxAI(2, WHITE)
# # player2 = MinimaxAI(4, BLACK)
# # player2 = IterativeMinimaxAI(3, BLACK)
# # player
# player2 = AlphaBetaAI(max_depth=4, color=BLACK, shuffle_moves=True, use_transposition=True)

if __name__ == '__main__':
    players = [
        MinimaxAI(3, WHITE, shuffle_moves=False),
        AlphaBetaAI(max_depth=3, color=BLACK, shuffle_moves=True, use_transposition=False)
    ]

    # game = ChessGame(player1, player2)
    game = ChessGame(*players)

    i = 0
    while not game.is_game_over():
        print('Turn: %d' % i)
        print(game)
        game.make_move()
        print('------------------')
        i += 1
    print('GAME OVER')
