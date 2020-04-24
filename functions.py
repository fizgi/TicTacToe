""" Functions for TicTacToe game

    author: fizgi
    date: 23-Apr-2020
    python: v3.8.2
"""

import random
from typing import List


def initializer():
    """ initialize the game values """
    size: int = int(input("Enter a number for the board size: "))
    board: List[List[str]] = [[random.choice(["X", "O", " "]) for x in range(size)] for y in
                              range(size)]
    return size, board


def print_board(board):
    """ print the board """
    for row in board:
        print(row)


def row_checker(board, size):
    """ check rows if there is a winning combination """
    for i in range(size):
        for j in range(1, size):
            if board[i][0] != board[i][j]:
                break
        else:
            yield f"'{board[i][j]}' (Row index: {i})"


def col_checker(board, size):
    """ check columns if there is a winning combination """
    for i in range(size):
        for j in range(1, size):
            if board[0][i] != board[j][i]:
                break
        else:
            yield f"'{board[j][i]}' (Col index {i})"


def dgn_lr_checker(board, size):
    """ check diagonal left to right if there is a winning combination """
    for i in range(0, size):
        if board[0][0] != board[i][i]:
            break
    else:
        yield f"'{board[0][0]}' (Diagonal left to right)"


def dgn_rl_checker(board, size):
    """ check diagonal right to left if there is a winning combination """
    for i, j in zip(range(0, size), reversed(range(0, size))):
        if board[0][size - 1] != board[i][j]:
            break
    else:
        yield f"'{board[0][size - 1]}' (Diagonal right to left)"


def result(winner_list):
    """ print the result """
    try:
        print(f"\n\033[4mWinner!! : {winner_list[0]}\033[0m")
        if len(winner_list) > 1:
            print(f"\n\033[1mThe other winning combination(s):\033[0m")
            for winner in winner_list[1:]:
                print(winner)
        else:
            print(f"\n\033[1mNo other winning combination.\033[0m")

    except IndexError:
        print("\nNo winner!")
