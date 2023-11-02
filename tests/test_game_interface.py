from unittest.mock import patch
from game.cli.game_interface import *
import unittest
import ipdb, io, sys

class TestGameInterface(unittest.TestCase):

    @patch('game.cli.game_interface.GameInterface.add_players', return_value=2)
    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    @patch('game.cli.game_interface.GameInterface.play', return_value='')
    def test_init(self, mock_add_players, mocked_input, mock_play):
        output_buffet = io.StringIO()
        sys.stdout = output_buffet
        game_interface = GameInterface()
        sys.stdout = sys.__stdout__
        output_buffet.close()
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
        output_buffet = io.StringIO()
        sys.stdout = output_buffet
        game_interface = GameInterface()
        sys.stdout = sys.__stdout__
        output_buffet.close()
        self.assertEqual(len(game_interface.scrabble.players), 2)

    @patch('builtins.input', side_effect=['a',2,'a','b'])
    def test_add_players_invalid(self,mock_input):
        output_buffet = io.StringIO()
        sys.stdout = output_buffet
        game_interface = GameInterface()
        sys.stdout = sys.__stdout__
        output_buffet.close()

    @patch('builtins.input', side_effect=[2,'a','b',1,'\n',5])
    def test_play_play_turn(self,mock_input):
        output_buffet = io.StringIO()
        sys.stdout = output_buffet
        game_interface = GameInterface()
        with patch.object(game_interface, 'play_turn') as mock_play_turn:
            # ipdb.set_trace()
            game_interface.play()
            mock_play_turn.assert_called_once()
        sys.stdout = sys.__stdout__
        output_buffet.close()

    @patch('builtins.input', side_effect=[2,'a','b',2,'\n',5])
    def test_play_play_turn(self,mock_input):
        output_buffet = io.StringIO()
        sys.stdout = output_buffet
        game_interface = GameInterface()
        with patch.object(game_interface, 'change_tiles') as mock_change_tiles:
            game_interface.play()
            mock_change_tiles.assert_called_once()
        sys.stdout = sys.__stdout__
        output_buffet.close()

    
    # @patch('builtins.input', side_effect=[2,'a','b',4,'\n',5])
    # def test_play_play_turn(self,mock_input):
    #     game_interface = GameInterface()
    #     with patch.object(game_interface, 'select_letter') as mock_select_letter:
    #         game_interface.play()
    #         mock_select_letter.assert_called_once()

    # @patch('builtins.input', side_effect=['a',2,'a','b',1,5,'\n',2,'8','\n',3,'\n',4,'\n','\n','t','\n',5])
    # def test_play(self,mock_input):
    #     game_interface = GameInterface()
    #     game_interface.play()
