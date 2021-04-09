"""
A module dedicated to playing tic tac toe with a human.
"""

from blessed import Terminal
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


def marker_to_symbol(marker):
    """
    Returns a string representation of a marker in a tic-tac-toe structure.
    :param marker:  The marker to convert.
    :return:        A single character string.
    """
    if marker == data.X_MARKER:
        return 'X'
    elif marker == data.O_MARKER:
        return 'O'
    else:
        return '.'


def coordinate_to_index(coordinate):
    """
    Converts a coordinate in the game matrix to the index in the vertical slice mark.
    :param coordinate:  The 3d-coordinate to convert into an index.
    :return:            An index from 0 to 26.
    """
    return coordinate[0] * 9 + coordinate[1] * 3 + coordinate[2]

if __name__ == '__main__':
    term = Terminal()
    current_game = data.BLANK_GAME_3D
    turn = True  # True when it's X's turn, False otherwise.
    game_states = []  # A collection of game states to manipulate at the end.
    with term.fullscreen(), term.cbreak():  # We capture the full screen and don't print out input.
        while not tictactoe.game_over_3d(current_game):  # We go until the game is over.
            available_actions = tictactoe.available_spots(current_game)
            assert (len(available_actions) > 0)  # Otherwise, the game should be over.
            action_index = 0
            action = None
            symbols = list(map(marker_to_symbol, current_game.flatten()))
            while not action:
                drawn_symbols = symbols.copy()
                coordinate_index = coordinate_to_index(available_actions[action_index])
                drawn_symbols[coordinate_index] = term.underline(drawn_symbols[coordinate_index])
                print(term.home + term.clear)
                print(VERTICAL_SLICES.format(*drawn_symbols))
                key = term.inkey()
                if key.code == term.KEY_RIGHT:  # Right means increase the index by one.
                    action_index = (action_index + 1) % len(available_actions)
                elif key.code == term.KEY_LEFT:  # Left means decreases the index by one.
                    action_index = (action_index - 1) % len(available_actions)
                else:  # Any other key means pick.
                    action = available_actions[action_index]
            # Right, an action was picked so we append the previous game state and apply the update.
            game_states.append(current_game)
            current_game = current_game.copy()
            current_game[action] = data.X_MARKER if turn else data.O_MARKER
            turn = not turn

    print("\n")
    print('Game is over.')
    if tictactoe.has_won_3d(current_game, data.X_MARKER):
        print('X has won.')
    elif tictactoe.has_won_3d(current_game, data.O_MARKER):
        print('O has won.')
    else:
        print('Tied.')
    print('The following game states were reached (flattened).')
    for game in game_states:
        print(game.flatten())
