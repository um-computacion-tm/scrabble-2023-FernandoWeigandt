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
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,7)
        orientation = 'H'
        board.put_word(word,location,orientation)
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

    def test_put_word_horizontal_empty(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location =(7,7)
        orientation ='H'
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter.letter,Tile('c',1).letter)
        self.assertEqual(board.grid[7][8].letter.letter,Tile('a',1).letter)
        self.assertEqual(board.grid[7][9].letter.letter,Tile('s',2).letter)
        self.assertEqual(board.grid[7][10].letter.letter,Tile('a',1).letter)

    def test_put_word_vertical_empty(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,7)
        orientation = 'V'
        board.put_word(word,location,orientation)
        self.assertEqual(board.grid[7][7].letter.letter,Tile('c',1).letter)
        self.assertEqual(board.grid[8][7].letter.letter,Tile('a',1).letter)
        self.assertEqual(board.grid[9][7].letter.letter,Tile('s',2).letter)
        self.assertEqual(board.grid[10][7].letter.letter,Tile('a',1).letter)

    def test_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,4)
        orientation = 'H'
        board.put_word(word,location,orientation)
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (4,7)
        orientation = 'V'
        board.put_word(word,location,orientation)
        self.assertEqual(board.validate_init_of_game(word,location,orientation),True)

    def test_not_validate_word_in_board_horizontal(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (5,8)
        orientation = 'H'
        board.put_word(word,location,orientation)
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_validate_word_in_board_vertical(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (8,5)
        orientation = 'V'
        board.put_word(word,location,orientation)
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)

    def test_not_empty(self):
        board = Board()
        word0 = [Tile('a',1),Tile('u',1),Tile('t',2),Tile('o',1)]
        location0 = (7,7)
        orientation = 'H'
        board.put_word(word0,location0,orientation)
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (8,7)
        orientation = 'H'
        board.put_word(word,location,orientation)
        self.assertEqual(board.validate_init_of_game(word,location,orientation),False)
        
    def test_show_board(self):
        board = Board()
        board.show_board()

    def test_show_board_with_word(self):
        board = Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,7)
        orientation = 'H'
        board.put_word(word,location,orientation)
        board.show_board()

    def test_show_board_with_words(self):
        board=Board()
        word = [Tile('c',1),Tile('a',1),Tile('s',2),Tile('a',1)]
        location = (7,7)
        orientation = 'H'
        board.put_word(word,location,orientation)
        word1 = [Tile('a',1),Tile('u',1),Tile('t',2),Tile('o',1)]
        location1 = (8,7)
        orientation = 'V'
        board.put_word(word1,location1,orientation)
        board.show_board()




class TestCell(unittest.TestCase):
    
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter',)
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,'letter')
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_multiplier_letter(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter)
        self.assertEqual(cell.calculate_value(),6)


    def test_cell_multiplier_word(self):
        cell_1 = Cell(multiplier=1,multiplier_type='letter')
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type='letter')
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=3,multiplier_type='word')
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type='letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value=Board().calculate_word_value(word)
        self.assertEqual(value,15)


    def test_cell_multiplier_both(self):
        cell_1 = Cell(multiplier=2,multiplier_type='letter')
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type='letter')
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=3,multiplier_type='word')
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type='letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value=Board().calculate_word_value(word)
        self.assertEqual(value,18)

    def test_cell_multiplier_none(self):
        cell_1 = Cell(multiplier=1,multiplier_type='letter')
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,multiplier_type='letter')
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=3,multiplier_type='word')
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,multiplier_type='letter')
        cell_4.add_letter(Tile('A', 1))
        word = [cell_1, cell_2, cell_3, cell_4]
        value=Board().calculate_word_value(word)
        self.assertEqual(value,15)
        value2=Board().calculate_word_value(word)
        self.assertEqual(value2,5)


if __name__ == '__main__':
    unittest.main()