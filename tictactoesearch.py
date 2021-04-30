"""
A module to run search algorithms on a game of tic tac toe.
"""

from functools import lru_cache
import tictactoe
from tictactoedata import X_TAKEN_CENTER_CENTER_3D
import numpy as np
from hashlib import sha1


class TicTacToeWrapper:
    """
    A lite wrapper class to define hashable behavior for caching.
    """

    def __init__(self, data):
        self.data = data
        # This method copied from https://stackoverflow.com/a/5173201
        self.hash = int(sha1(data.view(np.bool)).hexdigest(), 16)

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return np.all(self.data == other.data)


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


def play(wrapper, action, turn):
    """
    Play a coordinate action in tic tac toe given a game and the marker to place.
    :param wrapper: The TicTacToeWrapper to copy and place the marker in.
    :param action:  The coordinate tuple to play.
    :param turn:    A boolean indicating if it's x's turn (True) or not (False).
    :return:        A new wrapped TicTacToeWrapper.
    """
    new_copy = np.copy(wrapper.data)
    new_copy[0 if turn else 1][action] = True
    return TicTacToeWrapper(new_copy)


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
    else:
        return min_max_value_helper(wrapper, turn)


def possible_actions(wrapper):
    """
    Returns all the possible actions.
    :param wrapper: The TicTacToeWrapper to evaluate possible actions for.
    """
    return tictactoe.available_spots(wrapper.data)


@lru_cache(maxsize=None)
def min_max_value_helper(wrapper, turn):
    """
    Recursively finds the min, max, value of a certain wrapped game, exits early on utility.
    :param wrapper: The TicTacToeWrapper to evaluate with a value.
    :param turn:    A boolean indicating if it's x's turn (True) or not (False).
    :return:        The end result utility of this wrapped game of tic tac toe after applying min max.
    """
    successors = list(map(lambda action: play(wrapper, action, turn),
                          possible_actions(wrapper)))
    successor_utilities = map(lambda successor: utility(successor), successors)

    # We exit early based on utility if we can.
    if turn and 1 in successor_utilities:
        return 1
    if not turn and -1 in successor_utilities:
        return -1

    successor_values = map(lambda successor: min_max_value_helper(successor, not turn), successors)
    found_tie = False

    for successor_value in successor_values:
        if successor_value == 0:
            found_tie = True
        if turn and successor_value == 1:
            return 1
        if not turn and successor_value == -1:
            return -1

    if found_tie:
        return 0
    if turn and not found_tie:
        return -1
    if not turn and not found_tie:
        return 1


def min_max_action(wrapper, turn):
    """
    Returns the best action in tic tac toe given a game and the current turn.
    :param wrapper: The TicTacToeWrapper to search.
    :param turn:    A boolean indicating if it's x's turn (True) or not (False).
    :return:        The best action for the player indicated by the turn flag.
                    All actions if there isn't any.
    """
    actions = possible_actions(wrapper)
    tying_action = None
    for action in actions:
        successor = play(wrapper, action)
        value = min_max_value(successor, turn)
        if turn and value == 1:
            return action
        if not turn and value == -1:
            return action
        if value == 0:
            tying_action = action

    if tying_action is not None:
        return tying_action
    else:
        return actions


if __name__ == '__main__':
    print(min_max_value(TicTacToeWrapper(X_TAKEN_CENTER_CENTER_3D), False))
