from unittest.mock import patch
from game.cli.game_interface import *
import unittest

class TestGameInterface(unittest.TestCase):

    @patch('game.cli.game_interface.GameInterface.add_players', return_value=2)
    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    @patch('game.cli.game_interface.GameInterface.play', return_value='')
    def test_init(self, mock_add_players, mocked_input, mock_play):
        game_interface = GameInterface()
        self.assertEqual(len(game_interface.scrabble.players), 2)
        self.assertEqual(game_interface.scrabble.players[0].name, 'Player 1')
        self.assertEqual(game_interface.scrabble.players[1].name, 'Player 2')
        self.assertEqual(len(game_interface.scrabble.players[0].tiles), 7)
        self.assertEqual(len(game_interface.scrabble.players[1].tiles), 7)
        self.assertEqual(len(game_interface.scrabble.tilebag.tiles), 100-14)
        self.assertEqual(game_interface.scrabble.current_player, game_interface.scrabble.players[0])

    @patch('builtins.input', side_effect=['2','1', '2'])
    @patch('game.cli.game_interface.GameInterface.play', return_value='')
    def test_add_players(self, mocked_input, mock_play):
        game_interface = GameInterface()
        self.assertEqual(len(game_interface.scrabble.players), 2)



