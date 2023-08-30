import unittest
from game.player import *
from game.tilebag import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player=Player('Fernando',0,0,TileBag())
        self.assertEqual(player.name,'Fernando')
        self.assertEqual(player.score,0)
        self.assertEqual(player.number,0)
        self.assertEqual(len(player.tiles),7)
        