"""
A module of useful functions for tic-tac-toe games
"""

# Use this as a helper function for some tedious iterations.
from itertools import product
# Use this to manipulate tic-tac-toe data.
import numpy as np
# Use this to bring in data definitions, and some examples to test on.
import tictactoedata as data


# Documentation of product function.
# "Cartesian product of input iterables.
# For example, product(A, repeat=4) means the same as product(A, A, A, A)."
# This is useful for available_spots.

# A function to give all the possible actions for players in a game.
def available_spots(game):
    """
    Returns the available spots for marks given some board as coordinate tuples.
    :param: game    Any tic-tac-toe structure.
    :return:        An iterable of available spots for marks.
    """
    return list(filter(lambda coordinate_tuple: not game[0][coordinate_tuple] 
        and not game[1][coordinate_tuple] 
        and not game[2][coordinate_tuple],
                       product(range(3), repeat=game.ndim - 1)))


def has_won_2d(board):
    """
    Returns if the tic tac toe game has been won.
    :param board:           The 2d-tic-tac-toe structure of some player's marks.
    :return:                True if there are three marks in a row, false otherwise.
    """
    # We check all the rows.
    for row in range(3):
        if np.all(board[row, :]):
            return True
    # All the columns.
    for col in range(3):
        if np.all(board[:, col]):
            return True
    # And the diagonals.
    if board[0, 0] and board[1, 1] and board[2, 2]:
        return True
    if board[2, 0] and board[1, 1] and board[0, 2]:
        return True
    # Since they don't fill own a row, column, or diagonal completely, they haven't won.
    return False


def game_over_2d(board):
    """
    Returns if the tic tac toe game is over.
    :param board:   The 2d-tic-tac-toe structure.
    :return:        True if the game is won or tied by players, False otherwise.s
    """
    if has_won_2d(board[0]):
        return True
    if has_won_2d(board[1]):
        return True
    if np.all(np.bitwise_or(board[0], board[1])):  # If all spots are either covered by X marks or O marks.
        return True

    return False


def has_won_3d(box):
    """
    Returns if the marks by a player has won the game.
    :param box:   The 3d-tic-tac-toe structure.
    :return:      True if there is a 3 in a row.
    """
    # We first slice by x coordinate.
    for z_coordinate in range(3):
        if has_won_2d(box[z_coordinate, :, :]):
            return True
    # We then slice by y coordinate.
    for y_coordinate in range(3):
        if has_won_2d(box[:, y_coordinate, :]):
            return True
    # We then slice by z coordinate.
    for x_coordinate in range(3):
        if has_won_2d(box[:, :, x_coordinate]):
            return True
    # We then check the diagonals.
    # pylint: disable=R0916
    if (
            (box[0, 0, 0] and box[1, 1, 1] and box[2, 2, 2]) or
            (box[0, 0, 2] and box[1, 1, 1] and box[2, 2, 0]) or
            (box[0, 2, 0] and box[1, 1, 1] and box[2, 0, 2]) or
            (box[2, 0, 0] and box[1, 1, 1] and box[0, 2, 2])
    ):
        return True
    return False


def game_over_3d(box):
    """
    Returns if the tic tac toe game is over.
    :param box:   The 3d-tic-tac-toe structure.
    :return:        If the game is won (true), or tied by the two players. False otherwise.
    """
    if has_won_3d(box[0]):
        return True
    if has_won_3d(box[1]):
        return True
    if has_won_3d(box[2]):
        return True
    if np.all(np.bitwise_or(box[0], box[1])):
        return True

    return False
