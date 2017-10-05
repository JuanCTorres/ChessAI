"""
Author: Juan C. Torres
October 2017
"""
import chess
from typing import List


class AIPlayer:
    piece_score_list = [0, 1, 3, 3, 5, 9, 1000]
    WHITE = 1
    BLACK = 0

    def __init__(self, max_depth, color, use_transposition=False, shuffle_moves=False):
        self.max_depth = max_depth
        self.color_own = color
        self.color_opponent = abs(color - 1)
        self.use_transposition = use_transposition
        self.transposition_table = {}
        self.shuffle_moves = shuffle_moves
        self.max_depth_reached = 0

    def color_string(self):
        return 'WHITE' if self.color_own else 'BLACK'

    def get_heuristic_score(self, board: chess.Board):
        """
        Heuristic evaluation function. Returns the value of the board
        for _THIS_ AI.
        """
        score_own = sum([
            len(board.pieces(piece, self.color_own)) * self.piece_score_list[piece] for piece in
            chess.PIECE_TYPES
        ])
        score_opponent = sum([
            len(board.pieces(piece, self.color_opponent)) * self.piece_score_list[piece] for piece in
            chess.PIECE_TYPES
        ])
        checkmate_score = 0
        if board.is_checkmate():  # depending on whose turn it is, checkmate is a good or bad thing
            # simulate the king having been captured by adding/subtracting its value
            if board.turn == self.color_opponent:
                checkmate_score = self.piece_score_list[len(self.piece_score_list) - 1]
            else:
                checkmate_score = -self.piece_score_list[len(self.piece_score_list) - 1]

        return score_own - score_opponent + checkmate_score

    def terminal_test(self, board: chess.Board, depth):
        """
        Should we stop the search?
        """
        return depth == self.max_depth or board.is_game_over()

    @staticmethod
    def get_hashable_board(board):
        return str(board)

    def get_possible_moves(self, board: chess.Board) -> List[chess.Move]:
        """
        Get a list of moves to consider
        """
        legal_moves = list(board.legal_moves)
        if self.shuffle_moves:
            legal_move_and_priority_list = [(move, self.get_move_priority(board, move)) for move in legal_moves]
            # sorts in ascending value by default; the opposite of what we want!
            legal_move_and_priority_list.sort(key=lambda move_and_priority: move_and_priority[1], reverse=True)
            move_list_sorted = [move for move, priority in legal_move_and_priority_list]
            return move_list_sorted
        else:
            return legal_moves

    def get_move_priority(self, board: chess.Board, move: chess.Move):
        if board.is_capture(move):
            return 5
        move_str = str(move)
        row_from = int(move_str[1])
        row_to = int(move_str[3])
        # do I move forward?
        if board.turn and row_to > row_from:  # white
            return 2
        elif not board.turn and row_to < row_from:  # black
            return 2
        return 0
