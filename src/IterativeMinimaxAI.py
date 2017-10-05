"""
Author: Juan C. Torres
October 2017
"""
import chess
from time import sleep
from MinimaxAI import MinimaxAI


class IterativeMinimaxAI(MinimaxAI):
    def __init__(self, max_depth, color, shuffle_moves=False, use_transposition=False):
        super().__init__(max_depth=max_depth, color=color, shuffle_moves=shuffle_moves,
                         use_transposition=use_transposition)

    def choose_move(self, board: chess.Board):
        move_best = None
        for i in range(1, self.max_depth + 1):
            minimax_search = MinimaxAI(i, self.color_own, self.shuffle_moves,
                                       use_transposition=self.use_transposition)
            move = minimax_search.choose_move(board)
            utility_val = minimax_search.utility_value
            move_best = move
        return move_best
