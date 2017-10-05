# ChessAI

This AI will play chess against you or another AI opponent.

## Requirements
* PyQt5
* python-chess
* Python >= 3.5

## How to run

`python3 src/test_chess.py` or `python3 src/gui_chess.py`.

These both show matches of an alpha-beta AI playing against a random AI. 
## Notes
If you wish to change the type of 
AI or play against the AI, use `AlphaBetaAI`, `MinimaxAI`, `IterativeMinimaxAI`, or `HumanPlayer`. Check each file for 
their respective constructors, and do not use `AIPlayer`, since this class is only used to be inherited by one of the 
previously mentioned AI classes.