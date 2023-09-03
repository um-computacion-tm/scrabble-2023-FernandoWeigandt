import unittest
from game.scrabble_game import ScrabbleGame 
from game.tilebag import TileBag
from game.player import Player

class TestGameInitialization(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

class TestGameEnd(unittest.TestCase):
    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertFalse(scrabble_game.end_game())
        scrabble_game.bag_tiles=[]
        self.assertTrue(scrabble_game.end_game())


if __name__ == '__main__':
    unittest.main()
