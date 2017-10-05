"""
Author: Juan C. Torres
October 2017
"""
from src.AIPlayer import AIPlayer
import chess


class MinimaxAI(AIPlayer):
    def __init__(self, max_depth, color, shuffle_moves=False, use_transposition=False):
        super().__init__(max_depth=max_depth, color=color, use_transposition=use_transposition,
                         shuffle_moves=shuffle_moves)
        self.minimax_calls = 0
        self.utility_value = -float('inf')

    def choose_move(self, board: chess.Board) -> chess.Move:
        self.minimax_calls = 0
        self.utility_value = 0
        move = self.minimax_decision(board, 0)
        print('%s-Maximum depth reached: %d' % (self.color_string(), self.max_depth_reached))
        # calls to min_value and max_value, combined
        print('%s-Minimax calls: %d' % (self.color_string(), self.minimax_calls))
        return move

    def minimax_decision(self, board: chess.Board, depth: int) -> chess.Move:
        possible_move_list = []
        for action in self.get_possible_moves(board):
            board.push(action)
            possible_move_list.append((action, self.min_value(board, depth + 1)))
            board.pop()
        # using key=... allows max to act like argmax
        action, score = max(possible_move_list, key=lambda action_and_val: action_and_val[1])
        self.utility_value = score
        print('Best move score: %d' % score)
        return action

    def max_value(self, board: chess.Board, depth) -> int:
        """
        Return the maximum value of the possible states explored from this node
        """
        # Update the max depth reached
        self.max_depth_reached = max(self.max_depth_reached, depth)
        self.minimax_calls += 1
        if self.terminal_test(board, depth):
            return self.get_heuristic_score(board)
        val = float('-inf')
        for action in board.legal_moves:
            board.push(action)
            val = max(val, self.min_value(board, depth + 1))
            board.pop()
        return val

    def min_value(self, board: chess.Board, depth) -> int:
        """
        Return the minimum value of the possible states explored from this node
        """
        # Update the max depth reached
        self.max_depth_reached = max(self.max_depth_reached, depth)
        self.minimax_calls += 1
        if self.terminal_test(board, depth):
            return self.get_heuristic_score(board)
        val = float('inf')
        for action in self.get_possible_moves(board):
            board.push(action)
            val = min(val, self.max_value(board, depth + 1))
            board.pop()
        return val
