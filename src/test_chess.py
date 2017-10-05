"""
Author: Juan C. Torres, based on code by Devin Balkcom
October 2017
"""
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame

WHITE = 1
BLACK = 0

if __name__ == '__main__':
    players = [
        RandomAI(),
        AlphaBetaAI(max_depth=4, color=BLACK, shuffle_moves=True, use_transposition=False)
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
