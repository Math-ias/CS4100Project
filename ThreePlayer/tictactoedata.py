import numpy as np

X = 0
O = 1
R = 2
_ = -1


def reshape(arr):
    """
    A function to reshape a D-dimensional array of numbers into a D+1-dimensional array of boolean values.
    :param arr: The game array to convert.
    :return:    A new array with one dimension being for what mark it is.
    """
    return np.array([arr == X, arr == O, arr == R], dtype=bool)


#BLANK_GAME_3D = np.zeros((2, 3, 3, 3), dtype=bool)

# An X dimensional win. X wins along the easiest slice.

BLANK_GAME_3D = reshape(np.array([
    [
        [_, _, _],
        [_, _, _],
        [_, _, _],
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


X_WON_3D_X = reshape(np.array([
    [
        [O, O, _],
        [X, O, _],
        [X, X, R],
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

# print(X_WON_3D_X)