"""
A module dedicated to playing tic tac toe with a human.
"""

from blessed import Terminal
from numpy import ravel_multi_index
import tictactoedata as data
import tictactoe

VERTICAL_SLICES = """
      {}````{}````{}
   {}    {}    {}
{}▁▁▁▁{}▁▁▁▁{}

      {}````{}````{}
   {}    {}    {}
{}▁▁▁▁{}▁▁▁▁{}

      {}````{}````{}
   {}    {}    {}
{}▁▁▁▁{}▁▁▁▁{}
"""


def zipped_x_o_value_to_character(tup):
    """
    Converts a tuple of booleans indicating placement of x or o markers, and returns a character representation.
    :param tup: A tuple of a boolean, indicating if an x is placed, a second boolean, indicating if an o is placed.
    :return:    One of three characters, 'X', 'O', or '.' the last indicating an empty spot.
    """
    x_placed, o_placed = tup
    assert not (x_placed and o_placed)
    if x_placed:
        return 'X'
    if o_placed:
        return 'O'

    return '.'


def flattened_characters(game):
    """
    Returns a flattened array of single character strings.
    :param game:    The game state to flatten into a string representation.
    :return:        A flattened array.
    """
    return list(map(zipped_x_o_value_to_character,
                    zip(game[0].flatten(), game[1].flatten())))


def game_loop():
    """
    Runs a game once until it's won.
    :return:    The game states of this game.
    """
    term = Terminal()
    current_game = data.BLANK_GAME_3D
    xs_turn = True  # True when it's X's turn, False otherwise.
    game_states = []  # A collection of game states to manipulate at the end.
    with term.fullscreen(), term.cbreak():  # We capture the full screen and don't print out input.
        while not tictactoe.game_over_3d(current_game):  # We go until the game is over.
            available_actions = tictactoe.available_spots(current_game)
            assert len(available_actions) > 0  # Otherwise, the game should be over ...
            potential_action_index = 0
            action = None
            flattened_markers = flattened_characters(current_game)
            while not action:
                drawn_symbols = flattened_markers.copy()
                potential_action = available_actions[potential_action_index]
                flattened_potential_action_index = ravel_multi_index(potential_action, (3, 3, 3))
                drawn_symbols[flattened_potential_action_index] = term.underline('-')
                print(term.home + term.clear)
                print(VERTICAL_SLICES.format(*drawn_symbols))
                print("Press left, right, up, or down to cycle between potential moves.")
                print("Press any other key to commit a move.")
                key = term.inkey()
                if key.code == term.KEY_RIGHT:  # Right means increase the index by one.
                    potential_action_index = (potential_action_index + 1) % len(available_actions)
                elif key.code == term.KEY_UP or key.code == term.KEY_DOWN:  # Up, down complex
                    current_action = available_actions[potential_action_index]
                    y_diff = 1 if key.code == term.KEY_DOWN else -1
                    closest_action = min(
                        filter(lambda coordinate: coordinate[0] == (current_action[0] + y_diff) % 3,
                               available_actions),
                        key=lambda coordinate: abs(coordinate[1] - current_action[1]) + abs(
                            coordinate[2] - current_action[2]),
                        default=None)
                    if closest_action:
                        potential_action_index = available_actions.index(closest_action)
                elif key.code == term.KEY_LEFT:  # Left means decreases the index by one.
                    potential_action_index = (potential_action_index - 1) % len(available_actions)
                else:  # Any other key means pick.
                    action = available_actions[potential_action_index]
            # Right, an action was picked so we append the previous game state and apply the update.
            game_states.append(current_game)
            current_game = current_game.copy()
            current_game[0 if xs_turn else 1][action] = True
            xs_turn = not xs_turn
        game_states.append(current_game)  # We append the winning game state.
    return game_states


if __name__ == '__main__':
    game_frames = game_loop()
    assert len(game_frames) > 0
    last_frame = game_frames[-1]
    assert tictactoe.game_over_3d(last_frame)
    print("\n")
    print('Game is over.')
    if tictactoe.has_won_3d(last_frame[0]):
        print('X has won.')
    if tictactoe.has_won_3d(last_frame[1]):
        print('O has won.')
    else:
        print('Tied.')
    print('The following game states were reached (flattened).')
    for game in game_frames:
        print(list(map(lambda boolean: int(boolean), game.flatten())))
