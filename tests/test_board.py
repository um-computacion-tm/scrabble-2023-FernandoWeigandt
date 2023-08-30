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


    # def test_cell_multiplier_word(self):
    #     word=[Cell(Tile('C',1),),Cell(Tile('A',1)),Cell(2,'word',Tile('S',2)),Cell(Tile('A',1))]
    #     value=value.calculated_value()
    #     self.assertEqual(value,10)

    # def test_cell_multiplier_both(self):
    #     word=[Cell(Tile('C',1),),Cell(Tile('A',1)),Cell(2,'word',Tile('S',2)),Cell(3,'letter',Tile('A',1))]
    #     value=value.calculated_value()
    #     self.assertEqual(value,14)

    # def test_cell_no_multiplier(self):
    #     word=[Cell(Tile('C',1),),Cell(Tile('A',1)),Cell(2,'word',Tile('S',2)),Cell(3,'letter',Tile('A',1))]
    #     value=value.calculated_value(word)
    #     self.assertEqual(value,14)
    #     word=[Cell(Tile('C',1),),Cell(Tile('A',1)),Cell(2,'word',Tile('S',2)),Cell(3,'letter',Tile('A',1)),Cell(Tile('S',2))]
    #     word.disable_multiplier()
    #     value=value.calculated_value(word)
    #     self.assertEqual(value,7)



        
    



if __name__ == '__main__':
    unittest.main()