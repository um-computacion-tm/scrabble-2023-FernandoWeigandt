from game.tilebag import Tile
from game.cell import Cell
from pyrae import dle
from game.cell import Cell

class Board():
    def __init__(self,grid=None):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]
        self.assign_multipliers()
        
    def assign_multipliers(self):
        WORD_MULTIPLIERS = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))
        LETTER_MULTIPLIERS = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if (row, col) in LETTER_MULTIPLIERS:
                    if (row, col) in ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)):
                        multiplier = 2
                    else:
                        multiplier = 3
                    self.grid[row][col] = Cell(multiplier, 'letter', '', True)
                elif (row, col) in WORD_MULTIPLIERS:
                    if (row, col) in ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14)):
                        multiplier = 2
                    else:
                        multiplier = 3
                    self.grid[row][col] = Cell(multiplier, 'word', '', True)
                else:
                    self.grid[row][col] = Cell(1, '', '', False)


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
                view += '  ' + str(i+1) + '  '
            else:
                view += '  ' + str(i+1) + ' '
            for j in range(len(self.grid[i])):
                if self.grid[i][j].letter is None:
                    if self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 3:
                        view += '3W| '
                    elif self.grid[i][j].multiplier_type == 'word' and self.grid[i][j].multiplier == 2:
                        view += '2W| '
                    elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 3:
                        view += '3L| '
                    elif self.grid[i][j].multiplier_type == 'letter' and self.grid[i][j].multiplier == 2:
                        view += '2L| '
                    else:
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



