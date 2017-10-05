# brew install pyqt
from time import sleep

from PyQt5 import QtGui, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget
import sys
import chess, chess.svg
from src.RandomAI import RandomAI
from src.MinimaxAI import MinimaxAI
from src.ChessGame import ChessGame
from src.IterativeMinimaxAI import IterativeMinimaxAI
from src.HumanPlayer import HumanPlayer
from src.AlphaBetaAI import AlphaBetaAI

import random


class ChessGui:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.game = ChessGame(player1, player2)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.make_move)
        self.timer.start(10)

        self.display_board()

    def display_board(self):
        svgboard = chess.svg.board(self.game.board)

        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)

    def make_move(self):
        self.game.make_move()
        self.display_board()
        sleep(1)


if __name__ == "__main__":
    # random.seed(1)
    # WHITE = chess.COLORS[0]
    # BLACK = chess.COLORS[1]
    WHITE = True
    BLACK = False

    # player_ronda = RandomAI()

    # to do: gui does not work well with HumanPlayer, due to input() use on stdin conflict
    #   with event loop.

    # player1 = RandomAI()
    # player1 = MinimaxAI(3, WHITE, shuffle_moves=False)
    # player2 = AlphaBetaAI(max_depth=3, color=BLACK, shuffle_moves=True, use_transposition=False)
    # player2 = MinimaxAI(3, BLACK)
    # player2 = IterativeMinimaxAI(3, BLACK)
    # player
    # player1 = MinimaxAI(3, WHITE, shuffle_moves=False)
    player1 = RandomAI()
    player2 = AlphaBetaAI(max_depth=4, color=BLACK, shuffle_moves=True, use_transposition=False)

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)

    gui.start()

    sys.exit(gui.app.exec_())
