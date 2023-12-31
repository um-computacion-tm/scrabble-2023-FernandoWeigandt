import unittest
from game.board import Board
from game.cell import Cell
from game.tilebag import Tile

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

    def test_cell_multiplayer_none(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter)
        self.assertEqual(cell.calculate_value(),3)