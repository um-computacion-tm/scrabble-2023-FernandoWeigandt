from game.tilebag import Tile
from game.cell import Cell
from pyrae import dle
from game.cell import Cell

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
    

    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
    

    def validate_init_of_game(self, word, location, orientation):
                center_row, center_col = 7, 7
                if orientation == "H":
                    word_coords = [(location[0], location[1] + i) for i in range(len(word))]
                elif orientation == "V":
                    word_coords = [(location[0] + i, location[1]) for i in range(len(word))]
                for coord in word_coords:
                    if coord == (center_row, center_col):
                        return True
                return False
        

    def validate_len_of_word_in_board(self, word, location, orientation):
        if self.validate_word(word):
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


    def validate_word(self, word):
        dle.set_log_level(log_level='CRITICAL')
        flag=dle.search_by_word(word)
        if word.lower() not in flag.title:
            return False
        else:
            return True
        

    def validate_word_place_board(self, word, location, orientation):
        if self.validate_word(word):
            h_space = len(word) <= len(self.grid)-location[0]
            v_space = len(word) <= len(self.grid)-location[1]
            intersections = 0
            is_valid = 0
            if (orientation=='H' and h_space):
                for i in range(len(word)):
                    cell = self.grid[location[0]][location[1]+i].letter
                    if cell is not None:
                        intersections += 1
                        if cell.letter == word[i]:
                            is_valid += 1
            elif ((not orientation=='H') and v_space):
                for i in range(len(word)):
                    cell = self.grid[location[0]+i][location[1]].letter
                    if cell is not None:
                        intersections += 1
                        if cell.letter == word[i]:
                            is_valid += 1
            if is_valid != 0 and intersections == is_valid:
                return True
            else:
                return False    

    def __repr__(self):
        view = '       '
        col = ' ABCDEFGHIJKLMNO'
        view += '\n'
        for i in col:
            view += ' ' + i + '  '
        view += '\n'
        for i in range(len(self.grid)):
            if i < 9:
                view += ' ' + str(i+1) + ' '
            else:
                view += str(i+1) + ' '
            for j in range(len(self.grid[i])):
                if self.grid[i][j].letter is None:
                    view += '  | '
                else:
                    view += self.grid[i][j].letter.letter.upper() + ' | '
            view += '\n' 
        return view
    
    
    def put_word(self, word, location, orientation):
        if orientation == 'H':
            for i in range(len(word)):
                self.grid[location[0]][location[1]+i].letter = word[i]
        else:
            for i in range(len(word)):
                self.grid[location[0]+i][location[1]].letter = word[i]



