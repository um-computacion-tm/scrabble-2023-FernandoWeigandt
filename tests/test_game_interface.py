import unittest
from unittest.mock import patch
from game.cli.game_interface import main

class TestGameInterface(unittest.TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_main(self, mock_input):
        main()
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_input.call_args, (('How many players? ',),))
        self.assertEqual(mock_input.call_args_list, [(('How many players? ',),)])
        self
if __name__ == '__main__':
    unittest.main()
    
