import unittest
from tetris_problem import Tetris
class TestTetrisMethods(unittest.TestCase):
    def test_tetris_constructor(self):
        tetris = Tetris()
        self.assertEqual(tetris)
    def test_completed_tetris(self):
        tetris = Tetris()
        tetris.board = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        tetris.remove_completed_rows(1,3)
        self.assertEqual(len(tetris.board), 2)