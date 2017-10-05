import chess
import random
from time import sleep


class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)
        print("Random AI recommending move " + str(move))
        sleep(1)  # I'm thinking so hard.
        return move

