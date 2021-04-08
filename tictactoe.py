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
    return filter(lambda coordinate_tuple: game[coordinate_tuple] == data.BLANK_MARKER,
                  product(range(3), repeat=game.ndim))


def has_won_2d(board, player_mark):
    """
    Returns if the tic tac toe game has been won.
    :param board:       The 2d-tic-tac-toe structure.
    :param player_mark: The mark to identify the player by.
    :return:            True if the player has won the game, false otherwise.
    """
    # We check all the rows.
    for row in range(3):
        if np.all(board[row, :] == player_mark):
            return True
    # All the columns.
    for col in range(3):
        if np.all(board[:, col] == player_mark):
            return True
    # And the diagonals.
    if board[0, 0] == player_mark and board[1, 1] == player_mark and board[2, 2] == player_mark:
        return True
    if board[2, 0] == player_mark and board[1, 1] == player_mark and board[0, 2] == player_mark:
        return True
    # Since they don't fill own a row, column, or diagonal completely, they haven't won.
    return False


def game_over_2d(board):
    """
    Returns if the tic tac toe game is over.
    :param board:   The 2d-tic-tac-toe structure.
    :return:        True if the game is won or tied by players, False otherwise.s
    """
    if has_won_2d(board, data.X):
        return True
    if has_won_2d(board, data.O):
        return True
    if np.all(board != data.BLANK_MARKER):
        return True

    return False


def has_won_3d(box, player_mark):
    """
    Returns if the given player (identified by some mark) has won the game.
    :param box:   The 3d-tic-tac-toe structure.
    :param player_mark:  The mark to identify the player by.
    :return:    True if the player has won the game, false otherwise.
    """
    # We first slice by x coordinate.
    for z_coordinate in range(3):
        if has_won_2d(box[z_coordinate, :, :], player_mark):
            return True
    # We then slice by y coordinate.
    for y_coordinate in range(3):
        if has_won_2d(box[:, y_coordinate, :], player_mark):
            return True
    # We then slice by z coordinate.
    for x_coordinate in range(3):
        if has_won_2d(box[:, :, x_coordinate], player_mark):
            return True
    # We then check the diagonals.
    # pylint: disable=R0916
    if (  # Parenthesis let me put these coordinates together a little more visually.
            box[0, 0, 0] == player_mark and
            box[1, 1, 1] == player_mark and
            box[2, 2, 2] == player_mark
    ) or (
            box[0, 0, 2] == player_mark and
            box[1, 1, 1] == player_mark and
            box[2, 2, 0] == player_mark
    ) or (
            box[0, 2, 0] == player_mark and
            box[1, 1, 1] == player_mark and
            box[2, 0, 2] == player_mark
    ) or (
            box[2, 0, 0] == player_mark and
            box[1, 1, 1] == player_mark and
            box[0, 2, 2] == player_mark
    ):
        return True
    return False


def game_over_3d(box):
    """
    Returns if the tic tac toe game is over.
    :param box:   The 3d-tic-tac-toe structure.
    :return:        If the game is won (true), or tied by the two players. False otherwise.
    """
    if has_won_3d(box, data.X_MARKER):
        return True
    if has_won_3d(box, data.O_MARKER):
        return True
    if np.all(box != data.BLANK_MARKER):
        return True

    return False
