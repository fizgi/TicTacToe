""" Test implementation class for TicTacToe game

    author: fizgi
    date: 23-Apr-2020
    python: v3.8.2
"""

import unittest
from typing import List
from functions import row_checker, col_checker, dgn_lr_checker, dgn_rl_checker


class TicTacToeTest(unittest.TestCase):
    """ test class of TicTacToe game methods """
    def test_checkers(self):
        """ testing row, column and diagonal checkers """
        board: List[List[str]] = [['X', 'O', 'X', 'X'],
                                  ['O', 'X', 'X', ' '],
                                  ['O', ' ', 'O', 'O'],
                                  ['X', ' ', 'O', 'O']]

        self.assertTrue(list(row_checker(board, 4)) == [])
        self.assertTrue(list(col_checker(board, 4)) == [])
        self.assertTrue(list(dgn_lr_checker(board, 4)) == [])
        self.assertTrue(list(dgn_rl_checker(board, 4)) == [])

        board: List[List[str]] = [['X', 'O', 'X'],
                                  ['O', 'X', 'X'],
                                  ['X', 'X', 'X']]

        self.assertTrue(list(row_checker(board, 3)) == ["'X' (Row index: 2)"])
        self.assertTrue(list(col_checker(board, 3)) == ["'X' (Col index 2)"])
        self.assertTrue(list(dgn_lr_checker(board, 3)) == ["'X' (Diagonal left to right)"])
        self.assertTrue(list(dgn_rl_checker(board, 3)) == ["'X' (Diagonal right to left)"])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
