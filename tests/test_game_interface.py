# from unittest.mock import patch
# from game.cli.game_interface import GameInterface
# import unittest

# class TestGameInterface(unittest.TestCase):

#     @patch('builtins.input', side_effect=['2', 'player1', 'player2', '5'])
#     def test_add_players(self, mock_input):
#         game_interface = GameInterface()
#         self.assertEqual(game_interface.player_count, 2)

#     @patch('builtins.input', side_effect=['2', 'player1', 'player2', '5'])
#     def test_play(self, mock_input):
#         game_interface = GameInterface()
#         with patch.object(game_interface.scrabble, 'next_turn') as mock_next_turn:
#             game_interface.play()
#             self.assertEqual(mock_next_turn.call_count, 3)

#     @patch('builtins.input', side_effect=['word', '0,0', 'horizontal', '5'])
#     def test_play_turn(self, mock_input):
#         game_interface = GameInterface()
#         game_interface.scrabble.current_player.add_tiles(['w', 'o', 'r', 'd', 'e', 'r', 's'])
#         with patch.object(game_interface.scrabble.board, 'show_board') as mock_show_board:
#             with patch.object(game_interface.scrabble.board, 'put_word') as mock_put_word:
#                 game_interface.play_turn()
#                 self.assertEqual(mock_show_board.call_count, 2)
#                 self.assertEqual(mock_put_word.call_count, 0)

#     @patch('builtins.input', side_effect=['0,1', '2,1', '4,1'])
#     def test_change_tiles(self, mock_input):
#         game_interface = GameInterface()
#         game_interface.scrabble.current_player.add_tiles(['w', 'o', 'r', 'd', 'e', 'r', 's'])
#         with patch.object(game_interface.scrabble.tilebag, 'draw_tiles') as mock_draw_tiles:
#             with patch.object(game_interface.scrabble.tilebag, 'put_tiles') as mock_put_tiles:
#                 with patch.object(game_interface.scrabble.tilebag, 'shuffle') as mock_shuffle:
#                     game_interface.change_tiles()
#                     self.assertEqual(mock_draw_tiles.call_count, 1)
#                     self.assertEqual(mock_put_tiles.call_count, 1)
#                     self.assertEqual(mock_shuffle.call_count, 1)

#     @patch('builtins.input', side_effect=['V'])
#     def test_select_letter(self, mock_input):
#         game_interface = GameInterface()
#         game_interface.scrabble.current_player.add_tiles(['w', 'o', 'r', 'd', 'e', 'r', '_'])
#         game_interface.select_letter()
#         self.assertEqual(game_interface.scrabble.current_player.tiles[-1].letter, 'V')

#     @patch('builtins.input', side_effect=['2', 'player1', 'player2', '5'])
#     def test_add_players_invalid_input(self, mock_input):
#         game_interface = GameInterface()
#         with patch('builtins.print') as mock_print:
#             with patch.object(game_interface, 'add_players', return_value=None) as mock_add_players:
#                 game_interface.__init__()
#                 self.assertEqual(mock_add_players.call_count, 2)
#                 self.assertEqual(mock_print.call_count, 2)

#     @patch('builtins.input', side_effect=['word', '0,0', 'horizontal', '5'])
#     def test_play_turn_invalid_input(self, mock_input):
#         game_interface = GameInterface()
#         game_interface.scrabble.current_player.add_tiles(['w', 'o', 'r', 'd', 'e', 'r', 's'])
#         with patch.object(game_interface.scrabble.board, 'show_board') as mock_show_board:
#             with patch.object(game_interface.scrabble.board, 'put_word') as mock_put_word:
#                 with patch('builtins.print') as mock_print:
#                     game_interface.play_turn()
#                     self.assertEqual(mock_show_board.call_count, 2)
#                     self.assertEqual(mock_put_word.call_count, 0)
#                     self.assertEqual(mock_print.call_count, 1)

#     @patch('builtins.input', side_effect=['0,1', '2,1', '4,1'])
#     def test_change_tiles_invalid_input(self, mock_input):
#         game_interface = GameInterface()
#         game_interface.scrabble.current_player.add_tiles(['w', 'o', 'r', 'd', 'e', 'r', 's'])
#         with patch.object(game_interface.scrabble.tilebag, 'draw_tiles') as mock_draw_tiles:
#             with patch.object(game_interface.scrabble.tilebag, 'put_tiles') as mock_put_tiles:
#                 with patch.object(game_interface.scrabble.tilebag, 'shuffle') as mock_shuffle:
#                     with patch('builtins.print') as mock_print:
#                         game_interface.change_tiles()
#                         self.assertEqual(mock_draw_tiles.call_count, 1)
#                         self.assertEqual(mock_put_tiles.call_count, 1)
#                         self.assertEqual(mock_shuffle.call_count, 1)
#                         self.assertEqual(mock_print.call_count, 1)


# if __name__ == '__main__':
#     unittest.main()