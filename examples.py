import numpy as np


X = -1
O = 1
BLANK = 0

# A game of tic tac toe is a matrix of N dimensions,
# of the integer data type (same data type as the markers),
# with each axis having a length of 3,
# and all elements are either X, O, or BLANK.

# For example, here we define a blank 2D game, and a blank 3D game.
BLANK_GAME_2D = np.zeros((3, 3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~2-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

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
MIDGAME_2D = np.array([
    [O, BLANK, X],
    [BLANK, BLANK, BLANK],
    [X, BLANK, BLANK]
])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~3-Dimensional Games~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


BLANK_GAME_3D = np.zeros((3, 3, 3))

BLANK_3D_Template = np.array(
    [
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ]
    ]
)

#X dimensional win
X_WON_3D_X = np.array(
    [
        [
            [O, O, BLANK],
            [X, O, BLANK],
            [X, X, X],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ]
    ]
)

#Y dimensional win.
#X Wins through cordinates (0, 0, 0), (0, 1, 0), and (0, 2, 0)
X_WON_3D_Y = np.array(
    [
        [
            [X, BLANK, BLANK],
            [X, BLANK, O],
            [X, O, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ]
    ]
)

#Z dimensional win
##In this example, x has one on the cordinates (1, 0, 0), (1, 0, 1), and (1, 0, 2)
X_WON_3D_Z= np.array(
    [
        [
            [BLANK, X, BLANK],
            [BLANK, BLANK, BLANK],
            [O, BLANK, BLANK],
        ],
        [
            [BLANK, X, BLANK],
            [BLANK, BLANK, O],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, X, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ]
    ]
)


#X wins on XY plane
X_WON_3D_XY = np.array(
    [
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, O],
        ],
        [
            [X, BLANK, BLANK],
            [BLANK, X, BLANK],
            [BLANK, BLANK, X],
        ],
        [
            [BLANK, BLANK, BLANK],
            [O, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ]
    ]
)

#X wins on XZ plane
X_WON_3D_XZ = np.array(
    [
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, X],
        ],
        [
            [O, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, X, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, O],
            [X, BLANK, BLANK],
        ]
    ]
)

#X wins on YZ plane
X_WON_3D_YZ = np.array(
    [
        [
            [BLANK, BLANK, X],
            [BLANK, BLANK, BLANK],
            [O, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, X],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, O, BLANK],
            [BLANK, BLANK, X],
        ]
    ]
)

#X wins on XYZ plane
X_WON_3D_XYZ = np.array(
    [
        [
            [BLANK, BLANK, X],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, X, BLANK],
            [BLANK, BLANK, BLANK],
        ],
        [
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK],
            [X, BLANK, BLANK],
        ]
    ]
)



