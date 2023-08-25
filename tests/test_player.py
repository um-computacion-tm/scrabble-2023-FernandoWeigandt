import unittest
from game.player import *


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player=Player('Fernando',0)
        self.assertEqual(player.name,'Fernando')
        self.assertEqual(player.score,0)
        self.assertEqual(player.tiles,[])
