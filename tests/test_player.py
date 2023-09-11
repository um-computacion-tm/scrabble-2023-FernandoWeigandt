import unittest
from game.player import *
from game.tilebag import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player=Player('Fernando',0,0,TileBag())
        self.assertEqual(player.name,'Fernando')
        self.assertEqual(player.score,0)
        self.assertEqual(player.number,0)
        self.assertEqual(len(player.tiles),0)
    
    def test_add_tiles(self):
        player=Player('Fernando',0,0,TileBag())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        self.assertEqual(len(player.tiles),3)
        self.assertEqual(player.tiles[0].letter,'A')
        self.assertEqual(player.tiles[1].letter,'B')
        self.assertEqual(player.tiles[2].letter,'C')

    def test_change_tiles(self):
        player=Player('Fernando',0,0,TileBag())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        player.change_tiles([1,2],[Tile('D',1),Tile('E',1)])
        self.assertEqual(len(player.tiles),3)
        self.assertEqual(player.tiles[0].letter,'D')
        self.assertEqual(player.tiles[1].letter,'E')
        self.assertEqual(player.tiles[2].letter,'C')


