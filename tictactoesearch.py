"""
A module to run search algorithms on a game of tic tac toe.
"""

from functools import lru_cache
import tictactoe
from tictactoedata import GAME_2
import numpy as np
from hashlib import sha1


class TicTacToeWrapper:
    """
    A lite wrapper class to define hashable behavior for caching.
    """

    def __init__(self, data):
        self.data = data
        # This method copied from https://stackoverflow.com/a/5173201
        self.hash = int(sha1(data.view(np.uint8)).hexdigest(), 16)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return np.all(self.data == other.data)


@lru_cache(maxsize=None)
def utility(wrapper):
    """
    Defines the utility for a X of a board of TicTacToe.
    :param wrapper: The TicTacToeWrapper to evaluate for utility.
    :return:        The utility of tic tac toe if terminal, else None.
    """
    if tictactoe.has_won_3d(wrapper.data[0]):
        return 1
    elif tictactoe.has_won_3d(wrapper.data[1]):
        return -1
    elif tictactoe.game_over_3d(wrapper.data):
        return 0
    else:
        return None


def play(wrapper, action, index):
    """
    Play a coordinate action in tic tac toe given a game and the marker to place.
    :param wrapper: The TicTacToeWrapper to copy and place the marker in.
    :param action:  The coordinate tuple to play.
    :param index:   The index of the marker to place.
    :return:        A new wrapped TicTacToeWrapper.
    """
    assert (len(action) == wrapper.data.ndim - 1)
    new_copy = np.copy(wrapper.data)
    new_copy[index][action] = True
    return TicTacToeWrapper(new_copy)


@lru_cache(maxsize=None)
def min_max_value(wrapper, turn):
    """
    Recursively finds the min, max, value of a certain wrapped game.
    :param wrapper: The TicTacToeWrapper to evaluate with a value.
    :param turn:    A boolean indicating if it's x's turn (True) or not (False).
    :return:        The end result utility of this wrapped game of tic tac toe after applying min max.
    """
    game_state_utility = utility(wrapper)
    if game_state_utility is not None:
        return game_state_utility
    successors = map(lambda action: play(wrapper, action, 0 if turn else 1),
                     tictactoe.available_spots(wrapper.data))
    seen_zero = False
    for successor_utility in map(lambda successor: min_max_value(successor, not turn),
                                 successors):
        if turn and successor_utility == 1:
            return 1
        if not turn and successor_utility == -1:
            return -1
        if successor_utility == 0:
            seen_zero = True
    if seen_zero:  # If we didn't return out early then zero, if seen, will be our greatest or smallest value.
        return 0
    else:  # Otherwise, we return the minimum of what we saw.
        return -1 if turn else 1


if __name__ == '__main__':
    print(min_max_value(TicTacToeWrapper(GAME_2[-2]), True))
