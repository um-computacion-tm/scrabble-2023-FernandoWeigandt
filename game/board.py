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

    def validate_len_of_word_in_board(self, word, location, orientation):
        location_x = location[0]
        location_y = location[1]
        len_word = len(word)
        if orientation == 'H':
            if location_x + len_word > 15:
                return False
            else:
                return True
        else:
            if location_y + len_word > 15:
                return False
            else:
                return True

    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
    
    def put_word(self,word,location, orientation):
        if self.is_empty() is True:
            location_x = location[0]
            location_y = location[1]
            if orientation == 'H':
                for i in range(len(word)):
                    self.grid[location_x+i][location_y].add_letter(word[i])
            else:
                for i in range(len(word)):
                    self.grid[location_x][location_y+i].add_letter(word[i])

    def validate_init_of_game(self,word,location,orientation):
        if self.is_empty() and self.validate_len_of_word_in_board(word,location,orientation):
            for i in range (len(word)):
                if orientation =='H':
                    pos_x = location[0]+i
                    if pos_x == 7:
                        return True
                    else:
                        return False
                else:
                    pos_y = location[1]+i
                    if pos_y == 7:
                        return True
                    else:
                        return False
        else:
            return False

                    





class Cell:
    def __init__(self, multiplier, multiplier_type='',letter=None,active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter=None
        

    def add_letter(self, tile):
        self.letter = tile
        

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value