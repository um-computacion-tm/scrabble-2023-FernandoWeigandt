import unittest
from game.tiles import *

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TileBag(unittest.TestCase):
    def test_tilebag(self):
        tilebag = TileBag()
        self.assertEqual(tilebag.tiles_remaining(), 100)

    def test_draw_tiles(self):
        tilebag = TileBag()
        tilebag.draw_tiles(7)
        self.assertEqual(tilebag.tiles_remaining(), 93)


if __name__ == '__main__':
    unittest.main()