"""
A module of useful functions for tic-tac-toe games
"""

# Use this to manipulate tic-tac-toe data.
import numpy as np
# Use this as a helper function for some tedious iterations.
from itertools import product
# Use this to bring in data definitions, and some examples to test on.
import tictactoedata as data


# Documentation of product function.
# "Cartesian product of input iterables.
# For example, product(A, repeat=4) means the same as product(A, A, A, A)."
# This is useful for available_spots, AND testing examples.

# A function to give all the possible actions for players in a game.
def available_spots(game):
    """
    Returns the available spots for marks given some board as coordinate tuples.
    :param: game    Any tic-tac-toe structure.
    :return:        An iterable of available spots for marks.
    """
    return filter(lambda coordinate_tuple: game[coordinate_tuple] == data.BLANK_MARKER,
                  product(range(3), repeat=game.ndim))


# Sets are used to avoid order comparison.
assert (set(available_spots(data.BLANK_GAME_2D)) == set(product(range(3), repeat=2)))
assert (set(available_spots(data.BLANK_GAME_3D)) == set(product(range(3), repeat=3)))
# We get no available spots in this finished game.
assert (set(available_spots(data.TIED_2D)) == set())
# We get some spots in MIDGAME_2D.
# This is prone to break if the example changes.
# Other example names are descriptive enough to ensure compat.
assert (set(available_spots(data.MIDGAME_2D)) == set([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)]))


def has_won_2d(board, player_mark):
    """
    Returns if the tic tac toe game has been won.
    :param board:       The 2d-tic-tac-toe structure.
    :param player_mark: The mark to identify the player by.
    :return:            True if the player has won the game, false otherwise.
    """

    # We check all the rows.
    for row in range(3):
        if np.all(board[row:(row + 1), 0:3] == player_mark):
            return True
    # All the columns.
    for col in range(3):
        if np.all(board[0:3, col:(col + 1)] == player_mark):
            return True
    # And the diagonals.
    if board[0, 0] == player_mark and board[1, 1] == player_mark and board[2, 2] == player_mark:
        return True
    elif board[2, 0] == player_mark and board[1, 1] == player_mark and board[0, 2] == player_mark:
        return True
    # Since they don't fill own a row, column, or diagonal completely, they haven't won.
    return False


# We test our function against our examples.
# Neither player should win a blank game.
assert (not has_won_2d(data.BLANK_GAME_2D, data.X_MARKER))
assert (not has_won_2d(data.BLANK_GAME_2D, data.O_MARKER))
# Only X should win the X_WON board.
assert (has_won_2d(data.X_WON_2D, data.X_MARKER))
assert (not has_won_2d(data.X_WON_2D, data.O_MARKER))
# Only O should win the O_WON board.
assert (has_won_2d(data.O_WON_2D, data.O_MARKER))
assert (not has_won_2d(data.O_WON_2D, data.X_MARKER))
# Neither should win a tied board.
assert (not has_won_2d(data.TIED_2D, data.X_MARKER))
assert (not has_won_2d(data.TIED_2D, data.O_MARKER))
# Neither should win an in-progress-unfinished game.
assert (not has_won_2d(data.MIDGAME_2D, data.X_MARKER))
assert (not has_won_2d(data.MIDGAME_2D, data.O_MARKER))


def game_over_2d(board):
    """
    Returns if the tic tac toe game is over.
    :param board:   The 2d-tic-tac-toe structure.
    :return:        True if the game is won or tied by players, False otherwise.s
    """
    if has_won_2d(board, data.X):
        return True
    elif has_won_2d(board, data.O):
        return True
    elif np.all(board != data.BLANK_MARKER):
        return True
    else:
        return False


# We test our function against our examples.
# These tests should match the scenarios for has_won_2d.
# A blank game is in-progress and not over.
assert (not game_over_2d(data.BLANK_GAME_2D))
# X has won, therefore the game is over.
assert (game_over_2d(data.X_WON_2D))
# O has won, therefore the game is over.
assert (game_over_2d(data.O_WON_2D))
# The game is tied, therefore the game is over.
assert (game_over_2d(data.TIED_2D))
# An in-progress game is not over.
assert (not game_over_2d(data.MIDGAME_2D))


def has_won_3d(box, player_mark):
    """
    Returns if the given player (identified by some mark) has won the game.
    :param box:   The 3d-tic-tac-toe structure.
    :param player_mark:  The mark to identify the player by.
    :return:    True if the player has won the game, false otherwise.
    """
    # We first slice by x coordinate.
    for x in range(3):
        if has_won_2d(box[x:(x + 1), 0:3, 0:3], player_mark):
            return True
    # We then slice by y coordinate.
    for y in range(3):
        if has_won_2d(box[0:3, y:(y + 1), 0:3], player_mark):
            return True
    # We then slice by z coordinate.
    for z in range(3):
        if has_won_2d(box[0:3, 0:3, z:(z + 1)], player_mark):
            return True
    # We then check the diagonals.
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


assert (has_won_3d(data.X_WON_3D_X, data.X_MARKER))
assert (has_won_3d(data.X_WON_3D_Y, data.X_MARKER))
assert (has_won_3d(data.X_WON_3D_Z, data.X_MARKER))

assert (has_won_3d(data.X_WON_3D_XY, data.X_MARKER))
assert (has_won_3d(data.X_WON_3D_XZ, data.X_MARKER))
assert (has_won_3d(data.X_WON_3D_YZ, data.X_MARKER))

assert (has_won_3d(data.X_WON_3D_XYZ, data.X_MARKER))


def game_over_3d(box):
    """
    Returns if the tic tac toe game is over.
    :param box:   The 3d-tic-tac-toe structure.
    :return:        If the game is won (true), or tied by the two players. False otherwise.
    """
    if has_won_3d(box, data.X_MARKER):
        return True
    elif has_won_3d(box, data.O_MARKER):
        return True
    elif np.all(box != data.BLANK_MARKER):
        return True
    else:
        return False
