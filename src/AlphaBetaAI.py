"""
Author: Juan C. Torres
October 2017
"""
from time import sleep

import chess
from math import inf
from src.AIPlayer import AIPlayer


class AlphaBetaAI(AIPlayer):
    def __init__(self, max_depth, color, shuffle_moves=False, use_transposition=False):
        super().__init__(max_depth=max_depth, color=color, use_transposition=use_transposition,
                         shuffle_moves=shuffle_moves)
        self.minimax_calls = 0

    def choose_move(self, board: chess.Board):
        self.minimax_calls = 0
        self.max_depth_reached = 0
        res = self.alpha_beta_search_with_transposition(board, 0)
        print('%s-Maximum depth reached: %d' % (self.color_string(), self.max_depth_reached))
        # calls to min_value and max_value, combined
        print('%s-Minimax calls: %d' % (self.color_string(), self.minimax_calls))
        return res

    def alpha_beta_search_with_transposition(self, board: chess.Board, depth) -> chess.Move:
        """
        Top level function for alpha-beta pruning.
        """
        possible_move_list = []
        for move in self.get_possible_moves(board):  # move re-ordering happens here, if specified
            # Simulate move
            board.push(move)
            # Calculate the score for this move
            if self.use_transposition:
                hashable_board = self.get_hashable_board(board)
                if hashable_board in self.transposition_table:
                    print('Board found!')
                    score = self.transposition_table[hashable_board]
                else:
                    score = self.min_value(board, depth + 1, -inf, inf)
                    self.transposition_table[str(board)] = score
            else:
                score = self.min_value(board, depth + 1, -inf, inf)
            possible_move_list.append((move, score))
            # Done calculating score for this move. Undo!
            board.pop()
        best_move, best_score = max(possible_move_list, key=lambda move_and_score: move_and_score[1])
        print('Best move score: %d' % best_score)
        return best_move

    def min_value(self, board, depth, alpha, beta) -> int:
        """
        Get the value of the WORST state for this AI from the successor nodes. In
        other words, get the best state for the opponent. Notice this method returns
        a numerical value, not a move.
        """
        self.minimax_calls += 1
        if self.terminal_test(board, depth):
            return self.get_heuristic_score(board)
        if depth > self.max_depth_reached:
            self.max_depth_reached = depth

        val = float('inf')
        for action in self.get_possible_moves(board):
            board.push(action)
            # Calculate score of this action
            if self.use_transposition:  # check if score previously calculated or calculate now
                hashable_board = self.get_hashable_board(board)
                if hashable_board in self.transposition_table:
                    print('Board found!')
                    new_val = self.transposition_table[hashable_board]
                else:
                    print('Board missing. Finding its value!')
                    new_val = self.max_value(board, depth + 1, alpha, beta)
                    self.transposition_table[hashable_board] = new_val
            else:  # calculate score every time
                new_val = self.max_value(board, depth + 1, alpha, beta)
            val = min(val, new_val)
            # Done calculating score. Undo move
            board.pop()
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val

    def max_value(self, board, depth, alpha, beta) -> int:
        """
        Get the value of the BEST state for this AI from the successor nodes.
        Notice this method returns a numerical value, not a move.
        """
        self.minimax_calls += 1
        if depth > self.max_depth_reached:
            self.max_depth_reached = depth

        if self.terminal_test(board, depth):
            return self.get_heuristic_score(board)
        val = float('-inf')
        legal_moves = self.get_possible_moves(board)
        for action in legal_moves:
            board.push(action)
            if self.use_transposition:
                hashable_board = self.get_hashable_board(board)
                if hashable_board in self.transposition_table:
                    print('Found board in transposition table!')
                    new_val = self.transposition_table[hashable_board]
                else:
                    new_val = self.min_value(board, depth + 1, alpha, beta)
                    self.transposition_table[hashable_board] = new_val
            else:
                new_val = self.min_value(board, depth + 1, alpha, beta)
            val = max(val, new_val)
            board.pop()
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val
