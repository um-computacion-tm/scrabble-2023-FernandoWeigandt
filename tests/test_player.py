import unittest
from game.player import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player=Player('Fernando',0,0)
        self.assertEqual(player.name,'Fernando')
        self.assertEqual(player.score,0)
        self.assertEqual(player.tiles,[])
        self.assertEqual(player.number,0)

    def test_give_tiles(self):
        player=Player('Fernando',0,0)
        player.give_tiles(['A','B','C'])
        self.assertEqual(player.tiles,['A','B','C'])
        