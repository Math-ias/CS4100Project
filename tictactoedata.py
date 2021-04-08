"""
This module contains data definitions and examples for games of tic-tac-toe.
"""

import numpy as np

# A tic-tac-toe mark is defined as one of the following.
# Markers will always fit within a signed byte.
X_MARKER = -1
O_MARKER = 1
BLANK_MARKER = 0

# I'll also include these short-hands for creating examples.
# Though the full name should be used in code.
X = X_MARKER
O = O_MARKER
_ = BLANK_MARKER

# A game of tic tac toe is a matrix of N dimensions,
# of the char data type (dtype=np.dtype('b')),
# with each axis having a length of 3,
# and all elements being a tic-tac-toe mark.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~2-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# A blank game.
BLANK_GAME_2D = np.zeros((3, 3), dtype=np.dtype('b'))

# We define some more complicated examples below as well, the purpose being to aid testing.
X_WON_2D = np.array([
    [O, O, _],
    [X, O, _],
    [X, X, X],
], dtype=np.dtype('b'))

O_WON_2D = np.array([
    [_, _, O],
    [X, O, X],
    [O, _, _],
], dtype=np.dtype('b'))

TIED_2D = np.array([
    [O, O, X],
    [X, X, O],
    [O, X, O],
], dtype=np.dtype('b'))

MIDGAME_2D = np.array([
    [O, _, X],
    [_, _, _],
    [X, _, _]
], dtype=np.dtype('b'))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~3-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Numpy slice access on these cubes goes indexing the planes, we might think of this as z.
# Then it indexes the rows, we might think of this as y.
# THen it indexes the columns, we might think of this as x.
BLANK_GAME_3D = np.zeros((3, 3, 3), dtype=np.dtype('b'))

# An X dimensional win. X wins along the easiest slice.
X_WON_3D_X = np.array([
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
], dtype=np.dtype('b'))

# Y dimensional win.
# X wins through coordinates (0, 0, 0), (0, 1, 0), and (0, 2, 0).
X_WON_3D_Y = np.array([
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
], dtype=np.dtype('b'))

# Z dimensional win
# X wins with the coordinates (1, 0, 0), (1, 0, 1), and (1, 0, 2).
X_WON_3D_Z = np.array([
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
], dtype=np.dtype('b'))

# X wins on the XY plane.
X_WON_3D_XY = np.array([
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
], dtype=np.dtype('b'))

# X wins on the XZ plane.
X_WON_3D_XZ = np.array([
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
], dtype=np.dtype('b'))

# X wins on the YZ plane.
X_WON_3D_YZ = np.array([
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
], dtype=np.dtype('b'))

# X wins on a diagonal through the cube.
X_WON_3D_XYZ = np.array([
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
], dtype=np.dtype('b'))
