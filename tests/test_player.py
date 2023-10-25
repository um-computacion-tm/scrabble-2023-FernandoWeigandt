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

    def test_show_tiles(self):
        player=Player('Fernando',0,0,TileBag())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        self.assertEqual(player.show_tiles(),['A','B','C'])

    def test_remove_tiles(self):
        player=Player('Fernando',0,0,TileBag())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        player.remove_tiles([player.tiles[0],player.tiles[1]])
        self.assertEqual(len(player.tiles),1)
        self.assertEqual(player.tiles[0].letter,'C')

    def test_has_tiles(self):
        player=Player('Fernando',0,0,TileBag())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.add_tiles(tiles)
        self.assertTrue(player.has_tiles('ABC'))
        self.assertFalse(player.has_tiles('ABD'))

