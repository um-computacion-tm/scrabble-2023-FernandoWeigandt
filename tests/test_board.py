import unittest
from game.board import *
from unittest.mock import patch


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
        orientation = True
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    def test_len_of_word_in_board_y(self):
        board = Board()
        word = 'facultad'
        location = (5,4)
        orientation = False
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),True)

    def test_len_of_word_out_of_board_x(self):
        board = Board()
        word = 'facultad'
        location = (10,5)
        orientation = True
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    def test_len_of_word_out_of_board_y(self):
        board = Board()
        word = 'facultad'
        location = (5,10)
        orientation = False
        self.assertEqual(board.validate_len_of_word_in_board(word,location,orientation),False)

    def test_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,4)
        orientation = True
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (4,7)
        orientation = False
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_not_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (5,8)
        orientation = True
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (8,5)
        orientation = False
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_empty(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (6,7)
        orientation = False
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
    
    def test_show_board_with_word(self):
        board = Board()
        board.grid[7][7].letter = 'C'
        board.grid[7][8].letter = 'A'
        board.grid[7][9].letter = 'S'
        board.grid[7][10].letter = 'A'
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
  7  3W|   |   | 2L|   |   |   | C | A | S | A | 2L|   |   | 3W| 
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

    def test_show_board_with_word_2(self):
        board = Board()
        board.grid[7][7].letter = 'CH'
        board.grid[7][8].letter = 'O'
        board.grid[7][9].letter = 'Z'
        board.grid[7][10].letter = 'A'
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
  7  3W|   |   | 2L|   |   |   | CH| O | Z | A | 2L|   |   | 3W| 
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
        orientation = True
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    @patch('game.board.dle.search_by_word')
    def test_rae_search(self, mock_search_by_word):
        board = Board()
        valid_word = 'casa'
        mock_search_by_word.return_value.title = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        result1 = board.validate_word(valid_word)
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        invalid_word = 'uasffho'
        result2 = board.validate_word(invalid_word)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    def test_put_word(self):
        board=Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,7)
        orientation = True
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter.letter,'c')
        self.assertEqual(board.grid[7][8].letter.letter,'a')
        self.assertEqual(board.grid[7][9].letter.letter,'s')
        self.assertEqual(board.grid[7][10].letter.letter,'a')
    
    def test_put_word_vertical(self):
        board=Board()
        word = [Tile('f',1),Tile('a',1),Tile('c',2),Tile('u',1),Tile('l',1),Tile('t',1),Tile('a',1),Tile('d',1)]
        location = (7,7)
        orientation = False
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter.letter,'f')
        self.assertEqual(board.grid[8][7].letter.letter,'a')
        self.assertEqual(board.grid[9][7].letter.letter,'c')
        self.assertEqual(board.grid[10][7].letter.letter,'u')
        self.assertEqual(board.grid[11][7].letter.letter,'l')
        self.assertEqual(board.grid[12][7].letter.letter,'t')
        self.assertEqual(board.grid[13][7].letter.letter,'a')
        self.assertEqual(board.grid[14][7].letter.letter,'d')

    def test_validate_crossing_words(self):
        board=Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        board.grid[6][8].letter = Tile('L',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[8][8].letter = Tile('Z',1)
        board.grid[9][8].letter = Tile('O',1)
        word1 = 'lazo'
        location1 = (6,8)
        orientation1 = False
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),True)

    def test_validate_crossing_words_false(self):
        board=Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        word1 = 'faca'
        location1 = (5,8)
        orientation1 = True
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),False)

    def test_put_word_with_intersection(self):
        board = Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        word = [Tile('S',1)]
        location = (7,7)
        orientation = True
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter.letter,'C')
        self.assertEqual(board.grid[7][8].letter.letter,'A')
        self.assertEqual(board.grid[7][9].letter.letter,'S')
        self.assertEqual(board.grid[7][10].letter.letter,'A')
        self.assertEqual(board.grid[7][11].letter.letter,'S')

    def test_remove_accent(self):
        board=Board()
        word = 'PAPÁ'
        self.assertEqual(board.remove_accent(word),'PAPA')

    def test_remove_accent_false(self):
        board=Board()
        word = 'PAPA'
        self.assertEqual(board.remove_accent(word),'PAPA')

    def test_get_word_tithout_intersection(self):
        board=Board()
        board.grid[7][7].letter = Tile('C',1)
        board.grid[7][8].letter = Tile('A',1)
        board.grid[7][9].letter = Tile('S',2)
        board.grid[7][10].letter = Tile('A',1)
        word = 'faca'
        location = (6,8)
        orientation = False
        self.assertEqual(board.get_word_without_intersections(word,location,orientation),'fca')


if __name__ == '__main__':
    unittest.main()