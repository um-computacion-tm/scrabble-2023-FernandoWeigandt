import unittest
from tiles import *

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TileBag(unittest.TestCase):
    def test_tilebag(self):
        tilebag = TileBag()
        self.assertEqual(tilebag.tiles_remaining(), 0)

    def test_add_tile(self):
        tilebag = TileBag()
        tile = Tile('A', 1)
        tilebag.add_tile(tile)
        self.assertEqual(tilebag.tiles_remaining(), 1)

    def test_remove_tile(self):
        tilebag = TileBag()
        tile = Tile('A', 1)
        tilebag.add_tile(tile)
        tilebag.remove_tile(tile)
        self.assertEqual(tilebag.tiles_remaining(), 0)


if __name__ == '__main__':
    unittest.main()