import unittest
from game.tiles import *



class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestTileBag(unittest.TestCase):
    def test_tilebag(self):
        tilebag = TileBag()
        self.assertEqual(tilebag.tiles_remaining(), TOTALTILES)

    def test_draw_tiles(self):
        tilebag = TileBag()
        tilebag.draw_tiles(7)
        self.assertEqual(tilebag.tiles_remaining(), TOTALTILES-7)
        
    def test_draw_too_much_tiles(self):
        tilebag= TileBag()
        self.assertEqual(tilebag.draw_tiles(TOTALTILES+1),[])
        
    def test_put_tiles(self):
        tilebag=TileBag()
        taken=tilebag.draw_tiles(6)
        tilebag.put_tiles([taken[0], taken[5], taken[2]])
        self.assertEqual(tilebag.tiles_remaining(),TOTALTILES-3)

    def test_put_too_much_tiles(self):
        tilebag=TileBag()
        tilebag.put_tiles([Tile('A',1)])
        self.assertEqual(tilebag.tiles_remaining(),TOTALTILES)
        

    def test_Joker(self):
        tilebag=TileBag()
        tilebag.draw_tiles(7)
        tilebag.put_tiles([JokerTile('A',1)])
        self.assertEqual(tilebag.tiles_remaining(),TOTALTILES-6)

    def test_Joker_chooseLetter(self):
        tilebag=TileBag()





if __name__ == '__main__':
    unittest.main()