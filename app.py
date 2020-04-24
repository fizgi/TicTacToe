""" A program that implements the logic for a Tic-Tac-Toe game
    on an arbitrary size square board, e.g. 4x4, 5x5, etc.

    author: fizgi
    date: 23-Apr-2020
    python: v3.8.2
"""

from typing import List
from functions import initializer, print_board, row_checker, col_checker,\
    dgn_lr_checker, dgn_rl_checker, result

size, board = initializer()
winner_list: List[str] = []

print_board(board)

winner_list.extend(list(row_checker(board, size)))
winner_list.extend(list(col_checker(board, size)))
winner_list.extend(list(dgn_lr_checker(board, size)))
winner_list.extend(list(dgn_rl_checker(board, size)))

result(winner_list)
