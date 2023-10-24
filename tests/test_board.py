import unittest
from game.board import *


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()            
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[0]),15,)   

    def test_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty(), True)

    def test_not_empty(self):
        board = Board()
        board.grid[7][7].letter = Tile('c',1)
        board.grid[7][8].letter = Tile('a',1)
        board.grid[7][9].letter = Tile('s',2)
        board.grid[7][10].letter = Tile('a',1)
        self.assertEqual(board.is_empty(), False)

    def test_len_of_word_in_board_x(self):
        board = Board()
        word = 'facultad'
        location = (5,4)
        orientation = 'H'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    def test_len_of_word_in_board_y(self):
        board = Board()
        word = 'facultad'
        location = (5,4)
        orientation = 'V'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    def test_len_of_word_out_of_board_x(self):
        board = Board()
        word = 'facultad'
        location = (10,5)
        orientation = 'H'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    def test_len_of_word_out_of_board_y(self):
        board = Board()
        word = 'facultad'
        location = (5,10)
        orientation ='V'
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    def test_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,4)
        orientation = 'H'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (4,7)
        orientation = 'V'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_not_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (5,8)
        orientation = 'H'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (8,5)
        orientation = 'V'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_empty(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (6,7)
        orientation = 'V'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)
        

    def test_show_board(self):
        board = Board()
        result = board.show_board()
        expected = '''       
     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O  
  0  3W|   |   | 2L|   |   |   | 3W|   |   |   | 2L|   |   | 3W| 
  1    | 2W|   |   |   | 3L|   |   |   | 3L|   |   |   | 2W|   | 
  2    |   | 2W|   |   |   | 2L|   | 2L|   |   |   | 2W|   |   | 
  3  2L|   |   | 2W|   |   |   | 2L|   |   |   | 2W|   |   | 2L| 
  4    |   |   |   | 2W|   |   |   |   |   | 2W|   |   |   |   | 
  5    | 3L|   |   |   | 3L|   |   |   | 3L|   |   |   | 3L|   | 
  6    |   | 2L|   |   |   | 2L|   | 2L|   |   |   | 2L|   |   | 
  7  3W|   |   | 2L|   |   |   | 2W|   |   |   | 2L|   |   | 3W| 
  8    |   | 2L|   |   |   | 2L|   | 2L|   |   |   | 2L|   |   | 
  9    | 3L|   |   |   | 3L|   |   |   | 3L|   |   |   | 3L|   | 
  10   |   |   |   | 2W|   |   |   |   |   | 2W|   |   |   |   | 
  11 2L|   |   | 2W|   |   |   | 2L|   |   |   | 2W|   |   | 2L| 
  12   |   | 2W|   |   |   | 2L|   | 2L|   |   |   | 2W|   |   | 
  13   | 2W|   |   |   | 3L|   |   |   | 3L|   |   |   | 2W|   | 
  14 3W|   |   | 2L|   |   |   | 3W|   |   |   | 2L|   |   | 3W| 
'''
        self.maxDiff = None
        self.assertEqual(result, expected)
    

    def test_show_overlapping_words(self):
        board=Board()
        board.grid[7][7].letter = Tile('c',1)
        board.grid[7][8].letter = Tile('a',1)
        board.grid[7][9].letter = Tile('s',2)
        board.grid[7][10].letter = Tile('a',1)
        word = [Tile('s',2),Tile('a',1),Tile('c',1),Tile('a',1)]
        location = (7,7)
        orientation = 'H'
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_validate_word(self):
        board=Board()
        word = 'casa'
        self.assertEqual(board.validate_word(word),True)

    def test_validate_word_false(self):
        board=Board()
        word = 'asd'
        self.assertEqual(board.validate_word(word),False)

    def test_put_word(self):
        board=Board()
        word = 'casa'
        location = (7,7)
        orientation = 'H'
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter,'c')
        self.assertEqual(board.grid[7][8].letter,'a')
        self.assertEqual(board.grid[7][9].letter,'s')
        self.assertEqual(board.grid[7][10].letter,'a')
        

    def test_put_word_vertical(self):
        board=Board()
        word = 'facultad'
        location = (7,7)
        orientation = 'V'
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter,'f')
        self.assertEqual(board.grid[8][7].letter,'a')
        self.assertEqual(board.grid[9][7].letter,'c')
        self.assertEqual(board.grid[10][7].letter,'u')
        self.assertEqual(board.grid[11][7].letter,'l')
        self.assertEqual(board.grid[12][7].letter,'t')
        self.assertEqual(board.grid[13][7].letter,'a')
        self.assertEqual(board.grid[14][7].letter,'d')

    def test_validate_crossing_words(self):
        board=Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        board.grid[6][8].letter = Tile('L',1)
        board.grid[8][8].letter = Tile('Z',1)
        board.grid[9][8].letter = Tile('O',1)
        print(board.show_board())
        word1 = 'lazo'
        location1 = (6,8)
        orientation1 = 'V'
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),True)

    def test_validate_crossing_words_false(self):
        board=Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        word1 = 'faca'
        location1 = (5,8)
        orientation1 = 'H'
        print(board.show_board())
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),False)

    def test_remove_accent(self):
        board=Board()
        word = 'papá'
        self.assertEqual(board.remove_accent(word),'papa')

    def test_remove_accent_false(self):
        board=Board()
        word = 'papa'
        self.assertEqual(board.remove_accent(word),'papa')
    
if __name__ == '__main__':
    unittest.main()