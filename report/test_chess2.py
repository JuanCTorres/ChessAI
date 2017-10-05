# pip3 install python-chess
import random
from time import sleep

import chess
from src.RandomAI import RandomAI
from src.HumanPlayer import HumanPlayer
from src.MinimaxAI import MinimaxAI
from src.AlphaBetaAI import AlphaBetaAI
from src.ChessGame import ChessGame

WHITE = 1
BLACK = 0

if __name__ == '__main__':
    random.seed(1)
    player1 = RandomAI()
    player2 = AlphaBetaAI(max_depth=3, color=BLACK, shuffle_moves=False, use_transposition=True)
    # player2 = MinimaxAI(3, BLACK)

    game = ChessGame(player1, player2)

    i = 0
    while not game.is_game_over():
        print(i)
        print(game)
        game.make_move()
        # sleep(1)
        print('------------------')
        i += 1
