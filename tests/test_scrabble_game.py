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

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player , scrabble_game.players[0])

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player , scrabble_game.players[1])

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual (scrabble_game.current_player, scrabble_game.players[0])
    
    def test_validate_word(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertTrue(scrabble_game.validate_word('hola'))
        self.assertFalse(scrabble_game.validate_word(''))


class TestGameEnd(unittest.TestCase):
    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertFalse(scrabble_game.end_game())
        scrabble_game.bag_tiles=[]
        self.assertTrue(scrabble_game.end_game())


if __name__ == '__main__':
    unittest.main()
