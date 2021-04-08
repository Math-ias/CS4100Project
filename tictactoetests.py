"""
A collection of unit-tests for tictactoe.py.
"""

# Something provided in Python 3. Neat!
import unittest
# The functions we are testing are from this module.
import tictactoe
# The data and examples necessary to test this function are from here.
import tictactoedata as data
# A useful function for generating data.
from itertools import product


# Sets are used in these tests to avoid order comparison.
class TestAvailableSpots(unittest.TestCase):
    """
    A test case for the tictactoe.available_spots function.
    """

    def test_blank(self):
        """
        Blank games should return all the coordinates.
        """
        self.assertEqual(set(tictactoe.available_spots(data.BLANK_GAME_2D)), set(product(range(3), repeat=2)))
        self.assertEqual(set(tictactoe.available_spots(data.BLANK_GAME_3D)), set(product(range(3), repeat=3)))

    def test_finished(self):
        """
        Finished games should return no coordinates.
        """
        self.assertEqual(set(tictactoe.available_spots(data.TIED_2D)), set())

    def test_midgame(self):
        """
        In-progress games should return SOME coordinates.
        """
        # This is prone to break if the example changes.
        # Other example names are descriptive enough to ensure compat.
        self.assertEqual(set(tictactoe.available_spots(data.MIDGAME_2D)),
                          {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)})


class TestHasWon2D(unittest.TestCase):
    """
    A test case for the tictactoe.has_won_2d function.
    """

    def test_in_progress_games(self):
        """
        Neither player should win a game in progress.
        """
        # No one should win a blank game.
        self.assertFalse(tictactoe.has_won_2d(data.BLANK_GAME_2D, data.X_MARKER))
        self.assertFalse(tictactoe.has_won_2d(data.BLANK_GAME_2D, data.O_MARKER))
        # No one should win a game we marked as only being midgame.
        self.assertFalse(tictactoe.has_won_2d(data.MIDGAME_2D, data.X_MARKER))
        self.assertFalse(tictactoe.has_won_2d(data.MIDGAME_2D, data.O_MARKER))

    def test_games_won(self):
        """
        Only the player we designed as winning a game should win a game.
        """
        # Only X should win the X_WON board.
        self.assertTrue(tictactoe.has_won_2d(data.X_WON_2D, data.X_MARKER))
        self.assertFalse(tictactoe.has_won_2d(data.X_WON_2D, data.O_MARKER))
        # Only O should win the O_WON board.
        self.assertTrue(tictactoe.has_won_2d(data.O_WON_2D, data.O_MARKER))
        self.assertFalse(tictactoe.has_won_2d(data.O_WON_2D, data.X_MARKER))

    def test_tied_games(self):
        """
        No one should win a tied game.
        """
        self.assertFalse(tictactoe.has_won_2d(data.TIED_2D, data.X_MARKER))
        self.assertFalse(tictactoe.has_won_2d(data.TIED_2D, data.O_MARKER))


class TestGameOver2D(unittest.TestCase):
    """
    A test case for the tictactoe.game_over_2d function.
    """

    def test_in_progress_games(self):
        """
        An in-progress game should not be over.
        """
        # A blank game is in-progress and not over.
        self.assertFalse(tictactoe.game_over_2d(data.BLANK_GAME_2D))
        # An in-progress game is not over either.
        self.assertFalse(tictactoe.game_over_2d(data.MIDGAME_2D))

    def test_finished_games(self):
        """
        Games won by a player OR tied should be over.
        """
        # X has won, therefore the game is over.
        self.assertTrue(tictactoe.game_over_2d(data.X_WON_2D))
        # O has won, therefore the game is over.
        self.assertTrue(tictactoe.game_over_2d(data.O_WON_2D))
        # The game is tied, therefore the game is over.
        self.assertTrue(tictactoe.game_over_2d(data.TIED_2D))


class TestHasWon3D(unittest.TestCase):
    """
    A test case for the tictactoe.has_won_3d function.
    """

    def test_in_progress_games(self):
        """
        In progress games are not won by either player.
        """
        # Neither player should win a blank game.
        self.assertFalse(tictactoe.has_won_3d(data.BLANK_GAME_3D, data.X_MARKER))
        self.assertFalse(tictactoe.has_won_3d(data.BLANK_GAME_3D, data.O_MARKER))

    def test_won_games(self):
        """
        Only players we designated as winning should win their games.
        """
        # X should win along one axis easily.
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_X, data.X_MARKER))
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_Y, data.X_MARKER))
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_Z, data.X_MARKER))
        # O should lose along those axes easily.
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_X, data.O_MARKER))
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_Y, data.O_MARKER))
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_Z, data.O_MARKER))
        # X should win when it has three in a row in a 2D slice.
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_XY, data.X_MARKER))
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_XZ, data.X_MARKER))
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_YZ, data.X_MARKER))
        # O should therefore lose when X wins in those slices.
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_XY, data.O_MARKER))
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_XZ, data.O_MARKER))
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_YZ, data.O_MARKER))
        # X should win across 3-dimensional diagonals.
        self.assertTrue(tictactoe.has_won_3d(data.X_WON_3D_XYZ, data.X_MARKER))
        # And O should lose these.
        self.assertFalse(tictactoe.has_won_3d(data.X_WON_3D_XYZ, data.O_MARKER))


if __name__ == '__main__':
    unittest.main()
