"""
Author: Juan C. Torres, based on code by Devin Balkcom
October 2017
"""
from src.RandomAI import RandomAI
from src.HumanPlayer import HumanPlayer
from src.MinimaxAI import MinimaxAI
from src.AlphaBetaAI import AlphaBetaAI
from src.ChessGame import ChessGame

WHITE = 1
BLACK = 0

if __name__ == '__main__':
    players = [
        MinimaxAI(3, WHITE, shuffle_moves=False),
        AlphaBetaAI(max_depth=3, color=BLACK, shuffle_moves=True, use_transposition=False)
    ]

    game = ChessGame(*players)

    i = 0
    while not game.is_game_over():
        print('Turn: %d' % i)
        print(game)
        game.make_move()
        print('------------------')
        i += 1
    print('GAME OVER')
