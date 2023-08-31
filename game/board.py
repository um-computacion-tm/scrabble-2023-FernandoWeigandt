from game.tilebag import Tile

class Board():
    def __init__(self,grid=None):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]

    def calculate_word_value(self, word):
        value = 0
        for cell in word:
            value += cell.calculate_value()
        for cell in word:
            if cell.multiplier_type == 'word':
                value *= cell.multiplier
                cell.multiplier = 1
        return value



class Cell:
    def __init__(self, multiplier, multiplier_type='',letter=None,active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter=None
        

    def add_letter(self, letter:Tile):
        self.letter = letter
        

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value