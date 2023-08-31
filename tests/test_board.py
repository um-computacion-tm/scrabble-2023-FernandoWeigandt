import unittest
from game.board import *


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()            
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[0]),15,)        


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
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_multiplier_letter(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
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