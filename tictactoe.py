# This file contains data definitions,
# useful functions for tic-tac-toe games,
# and tests for those useful functions as asserts.

# We use numpy for its definition of matrices. The slice syntax is invaluable.
import numpy as np
# In order to define expected outputs easily, I don't want to write our coordinates manually.
from itertools import product

# A tic-tac-toe mark is defined as one of the following.
X = -1
O = 1
BLANK = 0

# A game of tic tac toe is a matrix of N dimensions,
# of the integer data type (same data type as the markers),
# with each axis having a length of 3,
# and all elements are either X, O, or BLANK.

# For example, here we define a blank 2D game, and a blank 3D game.
BLANK_GAME_2D = np.zeros((3, 3), dtype=type(X))
BLANK_GAME_3D = np.zeros((3, 3, 3), dtype=type(X))
# We define some more complicated examples below as well, the purpose being to aid testing.
X_WON_2D = np.array([
    [O, O, O],
    [X, O, BLANK],
    [X, X, X],
])
O_WON_2D = np.array([
    [BLANK, BLANK, O],
    [X, O, X],
    [O, BLANK, BLANK],
])
TIED_2D = np.array([
    [O, O, X],
    [X, X, O],
    [O, X, O],
])


# A function to give all the possible actions for players in the game.
def available_spots_3d(box):
    """
    Returns the available cubes for marks given some board as coordinate tuples.
    :param: box   The 3d-tic-tac-toe structure.
    :return:    An iterable of available cubes for marks.
    """
    to_return = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if box[x][y][z] == BLANK:
                    to_return.append((x, y, z))
    return to_return


# Documentation of product function.
# "Cartesian product of input iterables.
# For example, product(A, repeat=4) means the same as product(A, A, A, A)."

# In our case, we use the product of the range [0,3) three times. It comes to us as a tuple, perfect!
# We run a small test on our one example, all the coordinates should be returned.
assert (set(available_spots_3d(BLANK_GAME_3D)) == set(product(range(3), repeat=3)))


# A helper function to determine if a player has won a 2D-game-slice of tic-tac-toe.
def has_won_2d(board, player_mark):
    """
    Returns if the tic tac toe game has been won.
    :param board:   The 2d-tic-tac-toe structure.
    :param player_mark:  The mark to identify the player by.
    :return:    True if the player has won the game, false otherwise.
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

# We test our function against our four examples.
assert (has_won_2d(BLANK_GAME_2D, X) == False)
assert (has_won_2d(X_WON_2D, X) == True)
assert (has_won_2d(O_WON_2D, X) == False)


# A helper function to determine if a 2D-game-slice of tic-tac-toe is over.
def game_over_2d(board):
    """
    Returns if the tic tac toe game is over.
    :param board:   The 2d-tic-tac-toe structure.
    :return:        If the game is won (true), or tied by the two players. False otherwise.
    """
    if has_won_2d(board, X):
        return True
    elif has_won_2d(board, O):
        return True
    elif np.all(board != BLANK):
        return True


def game_over_3d(box):
    """
    Returns if the tic tac toe game is over.
    :param box:   The 3d-tic-tac-toe structure.
    :return:        If the game is won (true), or tied by the two players. False otherwise.
    """


def has_won_3d(box, player_mark):
    """
    Returns if the given player (identified by some mark) has won the game.
    :param box:   The 3d-tic-tac-toe structure.
    :param player_mark:  The mark to identify the player by.
    :return:    True if the player has won the game, false otherwise.
    """
    # We first slice by x coordinate.
    # We then slice by y coordinate.
    # We then slice by z coordinate.
    # We then check the diagonals.
