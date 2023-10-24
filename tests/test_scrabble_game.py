import unittest
from game.scrabble_game import ScrabbleGame 
from game.tilebag import TileBag
from game.player import Player

class TestGameInitialization(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.tilebag)

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
        self.assertEqual(scrabble_game.validate_word('facultad'), True)
        self.assertEqual(scrabble_game.validate_word('facultad1'), False)

    def test_show_board(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(scrabble_game.show_board(), scrabble_game.board.__repr__)

    def test_distribute_tiles(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.distribute_tiles()
        self.assertEqual(len(scrabble_game.players[0].tiles), 7)
        self.assertEqual(len(scrabble_game.players[1].tiles), 7)
        self.assertEqual(len(scrabble_game.players[2].tiles), 7)


if __name__ == '__main__':
    unittest.main()
