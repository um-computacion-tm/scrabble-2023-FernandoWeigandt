import unittest
from game.scrabble_game import ScrabbleGame 
from game.tilebag import TileBag , Tile
from game.player import Player
from unittest.mock import patch

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


    def test_show_board(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(scrabble_game.show_board(), scrabble_game.board.__repr__)

    @patch('game.board.Board.validate_word', return_value=True)
    def test_validate_all(self,mock_validate_word):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.players[0].tiles = [Tile('C',1),Tile('A',1),Tile('S',1),Tile('A',1)]
        self.assertEqual(scrabble_game.validate_all('CASA',(7,7),True), True)

    @patch('game.board.Board.validate_word', return_value=True)
    def test_validate_initial_word(self,mock_validate_word):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.players[0].tiles = [Tile('C',1),Tile('A',1),Tile('S',1),Tile('A',1)]
        self.assertEqual(scrabble_game.validate_initial_word('CASA',(7,7),True), True)

    @patch('game.tilebag.TileBag.draw_tiles')
    def test_change_tiles(self, mock_take_tiles):
        scrabble = ScrabbleGame(2)
        initial_value = len(scrabble.tilebag.tiles)
        scrabble.current_player = scrabble.players[0]
        tileA = Tile('A',1)
        tileE = Tile('A',1)
        tileF = Tile('F',1)
        scrabble.players[0].tiles = [tileA,tileE,tileE,tileA,tileA,tileA,tileA]
        mock_take_tiles.return_value = [tileF,tileF]
        scrabble.change_tiles((2,3))
        expected = [tileA,tileF,tileF,tileA,tileA,tileA,tileA]
        self.assertEqual(scrabble.players[0].tiles, expected)
        self.assertEqual(len(scrabble.tilebag.tiles), initial_value)





if __name__ == '__main__':
    unittest.main()
