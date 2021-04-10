"""
This module contains data definitions and examples for games of tic-tac-toe.
"""

import numpy as np

# I'll also include these short-hands for creating examples.
# Though these betray how the array's are actually laid out.
X = 0
O = 1
_ = -1


# A game of N-dimensional tic tac toe is a matrix of N + 1 dimensions,
# of the boolean data type,
# with the first axis having a length of 2,
# and subsequent axes having a length of 3.
# The first axis represents if the rest of the matrix is for the x (0) or o mark (1).

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~2-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def reshape(arr):
    """
    A function to reshape a D-dimensional array of numbers into a D+1-dimensional array of boolean values.
    :param arr: The game array to convert.
    :return:    A new array with one dimension being for what mark it is.
    """
    return np.array([arr == X, arr == O], dtype=bool)


# A blank game.
BLANK_GAME_2D = np.zeros((2, 3, 3), dtype=bool)

# We define some more complicated examples below as well, the purpose being to aid testing.
X_WON_2D = reshape(np.array([
    [O, O, _],
    [X, O, _],
    [X, X, X],
]))

O_WON_2D = reshape(np.array([
    [_, _, O],
    [X, O, X],
    [O, _, _],
]))

TIED_2D = reshape(np.array([
    [O, O, X],
    [X, X, O],
    [O, X, O],
]))

MIDGAME_2D = reshape(np.array([
    [O, _, X],
    [_, _, _],
    [X, _, _]
]))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~3-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Numpy slice access on these cubes goes indexing the marks,
# Then it indexes the planes, we might think of this as z.
# Then it indexes the rows, we might think of this as y.
# Then it indexes the columns, we might think of this as x.
BLANK_GAME_3D = np.zeros((2, 3, 3, 3), dtype=bool)

# An X dimensional win. X wins along the easiest slice.
X_WON_3D_X = reshape(np.array([
    [
        [O, O, _],
        [X, O, _],
        [X, X, X],
    ],
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]
]))

# Y dimensional win.
# X wins through coordinates (0, 0, 0), (0, 1, 0), and (0, 2, 0).
X_WON_3D_Y = reshape(np.array([
    [
        [X, _, _],
        [X, _, O],
        [X, O, _],
    ],
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]
]))

# Z dimensional win
# X wins with the coordinates (1, 0, 0), (1, 0, 1), and (1, 0, 2).
X_WON_3D_Z = reshape(np.array([
    [
        [_, X, _],
        [_, _, _],
        [O, _, _],
    ],
    [
        [_, X, _],
        [_, _, O],
        [_, _, _],
    ],
    [
        [_, X, _],
        [_, _, _],
        [_, _, _],
    ]
]))

# X wins on the XY plane.
X_WON_3D_XY = reshape(np.array([
    [
        [_, _, _],
        [_, _, _],
        [_, _, O],
    ],
    [
        [X, _, _],
        [_, X, _],
        [_, _, X],
    ],
    [
        [_, _, _],
        [O, _, _],
        [_, _, _],
    ]
]))

# X wins on the XZ plane.
X_WON_3D_XZ = reshape(np.array([
    [
        [_, _, _],
        [_, _, _],
        [_, _, X],
    ],
    [
        [O, _, _],
        [_, _, _],
        [_, X, _],
    ],
    [
        [_, _, _],
        [_, _, O],
        [X, _, _],
    ]
]))

# X wins on the YZ plane.
X_WON_3D_YZ = reshape(np.array([
    [
        [_, _, X],
        [_, _, _],
        [O, _, _],
    ],
    [
        [_, _, _],
        [_, _, X],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, O, _],
        [_, _, X],
    ]
]))

# X wins on a diagonal through the cube.
X_WON_3D_XYZ = reshape(np.array([
    [
        [_, _, X],
        [_, _, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, X, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, _, _],
        [X, _, _],
    ]
]))

# X has an initial move in the center.
X_TAKEN_CENTER_CENTER_3D = reshape(np.array([
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, X, _],
        [_, _, _],
    ],
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]
]))

reshape_lambda = lambda arr: reshape(np.array(arr).reshape((3, 3, 3)))

# The following is a game played between Mathias (X) and Jamie (O) as flattened arrays.
GAME_1 = list(
    map(reshape_lambda, [
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, O],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, X, O],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, O, _, _, _, _, _, _, _, _, _, _, _, X, O],
        [X, X, _, _, _, _, _, _, _, _, _, _, _, O, _, _, _, _, _, _, _, _, _, _, _, X, O],
        [X, X, O, _, _, _, _, _, _, _, _, _, _, O, _, _, _, _, _, _, _, _, _, _, _, X, O],
        [X, X, O, _, _, _, _, _, _, _, _, _, _, O, _, _, _, _, _, _, _, _, _, _, X, X, O],
        [X, X, O, _, _, _, _, _, _, _, _, _, O, O, _, _, _, _, _, _, _, _, _, _, X, X, O],
        [X, X, O, _, _, _, _, _, _, _, _, _, O, O, X, _, _, _, _, _, _, _, _, _, X, X, O],
        [X, X, O, _, _, _, _, _, _, _, _, _, O, O, X, _, _, _, _, _, _, _, O, _, X, X, O],
        [X, X, O, _, X, _, _, _, _, _, _, _, O, O, X, _, _, _, _, _, _, _, O, _, X, X, O],
        [X, X, O, _, X, _, _, _, _, _, _, _, O, O, X, _, _, _, O, _, _, _, O, _, X, X, O]
    ]))

# The following is another game played between Mathias and Jamie again.
GAME_2 = list(
    map(reshape_lambda, [
        [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, _, _, O],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, _, _, O],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, _, O, O],
        [_, X, _, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, X, O, O],
        [_, X, O, _, _, _, _, _, _, _, _, _, _, X, _, _, _, _, _, _, _, _, _, _, X, O, O],
        [_, X, O, _, _, _, _, _, _, _, _, _, _, X, X, _, _, _, _, _, _, _, _, _, X, O, O],
        [_, X, O, _, _, _, _, _, _, _, _, _, O, X, X, _, _, _, _, _, _, _, _, _, X, O, O],
        [_, X, O, _, _, _, _, _, _, _, _, _, O, X, X, _, _, _, _, _, _, _, X, _, X, O, O],
        [_, X, O, _, X, _, _, _, _, _, _, _, O, X, X, _, _, _, _, _, _, _, X, _, X, O, O]
    ]))
