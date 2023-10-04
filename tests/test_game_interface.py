# import unittest
# from unittest.mock import patch
# from game.cli.game_interface import main

# class TestGameInterface(unittest.TestCase):

#     @patch('game.cli.game_interface.ScrabbleGame')
#     @patch('game.cli.game_interface.input')
#     def test_main(self, mock_input, mock_scrabble_game):
#         mock_input.side_effect = ['2', 'word', '1', '1', 'V']
#         main()
#         self.assertEqual(mock_scrabble_game.call_count, 0)
#         self.assertEqual(mock_scrabble_game.return_value.next_turn.call_count, 1)
#         self.assertEqual(mock_scrabble_game.return_value.current_player, mock_scrabble_game.return_value.players[0])
#         self.assertEqual(mock_scrabble_game.return_value.validate_word.call_count, 1)
#         self.assertEqual(mock_scrabble_game.return_value.end_game.call_count, 1)






# if __name__ == '__main__':
#     unittest.main()

