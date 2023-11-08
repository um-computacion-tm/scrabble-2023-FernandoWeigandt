from game.tilebag import Tile
from game.cell import Cell
from pyrae import dle
from game.player import Player
from diccionario import DATA

class Board():

    def __init__(self,grid=None):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]
        WORD_MULTIPLIERS = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))
        LETTER_MULTIPLIERS = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.validate_multiplier(row, col, WORD_MULTIPLIERS, LETTER_MULTIPLIERS)

    def validate_multiplier(self, row, col, WORD_MULTIPLIERS, LETTER_MULTIPLIERS):
        if (row, col) in LETTER_MULTIPLIERS:
            multiplier=3 if (row, col) in ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)) else 2
            self.grid[row][col] = Cell(multiplier, 'letter', '', True)
        elif (row, col) in WORD_MULTIPLIERS:
            multiplier = 3 if (row, col) in ((0, 0), (7, 0), (0, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14)) else 2
            self.grid[row][col] = Cell(multiplier, 'word', '', True)
        else:
            self.grid[row][col] = Cell(1, '', '', False)
    

    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
    

    def validate_init_of_game(self, word, location, orientation):
        for i in range(len(word)):
            row = location[0] if orientation else location[0] + i
            column = location[1] + i if orientation else location[1]
            if (row, column) == (7, 7):
                return True
        return False
        

    def validate_len_of_word_in_board(self, word, location, orientation):
        location_x = location[0]
        location_y = location[1]
        len_word = len(word)
        if orientation == True:
            if location_x + len_word > 15:
                return False
            else:
                return True
        else:
            if location_y + len_word > 15:
                return False
            else:
                return True

    def validate(self,word,location,orientation):
        exist = self.validate_word(word)
        enter = self.validate_len_of_word_in_board(word,location,orientation)
        is_valid = exist and enter
        if is_valid:
            if self.is_empty():
                return self.validate_init_of_game(word,location,orientation)
            else:
                return self.validate_not_empty(word,location,orientation)

    def validate_word(self, word):
        dle.set_log_level(log_level='CRITICAL')
        flag=dle.search_by_word(word)
        if word.lower() not in flag.title:
            return False
        else:
            return True

    def validate_side_cell(self, parameters, cell, index_increment):
        letter, pos, horizontal = parameters[0], parameters[1], parameters[2]
        grid, side_word, index = self.grid, letter, 1
        while cell:
            side_word += cell.letter.lower()
            index += 1
            cell = grid[pos[0]+(index*index_increment)][pos[1]].letter if horizontal else grid[pos[0]][pos[1]+(index*index_increment)].letter
        return side_word

    def check_cells(self, cells, parameters, validators):
        cell, sidecell, invertsidecell = cells[0], cells[1], cells[2]
        letter, pos, horizontal = parameters[0], parameters[1], parameters[2]
        is_valid, intersections = validators[0], validators[1]
        if cell:
            intersections += 1
            is_valid += 1 if cell.letter == letter.upper() else 0
            return [is_valid, intersections]
        elif sidecell and invertsidecell:
            side_word = self.validate_side_cell([letter, pos, horizontal], invertsidecell, -1)[::-1]
            side_word += self.validate_side_cell([letter, pos, horizontal], sidecell, 1)[1:]
        elif sidecell:
            side_word = self.validate_side_cell([letter, pos, horizontal], sidecell, 1)
        elif invertsidecell:
            side_word = self.validate_side_cell([letter, pos, horizontal], invertsidecell, -1)[::-1]
        side_word_is_valid = self.validate_word(side_word)
        if not side_word_is_valid:
            is_valid = -9999
        else:
            is_valid += 1
            intersections += 1
        return [is_valid, intersections]

    def validate_not_empty(self, word, pos, horizontal):
        intersections = 0
        is_valid = 0
        grid = self.grid
        for i in range(len(word)):
            if horizontal:
                cell = grid[pos[0]][pos[1]+i].letter
                sidecell = grid[pos[0] + 1][pos[1] + i].letter
                invertsidecell = grid[pos[0] - 1][pos[1] + i].letter
            else:
                cell = grid[pos[0]+i][pos[1]].letter
                sidecell = grid[pos[0] + i][pos[1] + 1].letter
                invertsidecell = grid[pos[0] + i][pos[1] - 1].letter
            if cell or sidecell or invertsidecell:
                location = (pos[0],pos[1]+i) if horizontal else (pos[0]+i,pos[1])
                checked = self.check_cells([cell, sidecell, invertsidecell], [word[i], location, horizontal], [is_valid, intersections])
                is_valid, intersections = checked[0], checked[1]
        return is_valid != 0 and is_valid == intersections

    def show_board(self):
        view = '       \n     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O  \n'
        for i in range(len(self.grid)):
            view += f'  {i}  ' if i <= 9 else f'  {i} '
            view = self.show_board_wrapper(view,i)
            view += '\n' 
        return view

    def show_board_wrapper(self,view,i):
        for j in range(len(self.grid[i])):
            cell = self.grid[i][j]
            if cell.letter is None:
                if cell.multiplier_type == 'word':
                    view += f'{cell.multiplier}W| '
                elif cell.multiplier_type == 'letter':
                    view += f'{cell.multiplier}L| '
                else:
                    view += '  | '
            elif len(cell.letter.letter) == 2:
                view += f'{cell.letter}| '
            else:
                view += f'{cell.letter} | '
        return view
        
    def put_word(self,word,location,orientation):
        j=0
        for i in range(len(word)):
            cell = self.grid[location[0]][location[1]+i+j] if orientation else self.grid[location[0]+i+j][location[1]]
            while cell.letter:
                j+=1
                cell = self.grid[location[0]][location[1]+i+j] if orientation else self.grid[location[0]+i+j][location[1]]
            cell.letter = word[i]


    def remove_accent(self, word):
        word = word.replace('Á','A')
        word = word.replace('É','E')
        word = word.replace('Í','I')
        word = word.replace('Ó','O')
        word = word.replace('Ú','U')
        return word
    
    def get_word_without_intersections(self,word,location,orientation):
        result = ''
        for i in range(len(word)):
            cell = self.grid[location[0] + (i if not orientation else 0)][location[1] + (i if orientation else 0)].letter
            if not cell:
                result += word[i]
        return result
        
    def calculate_word_value(self, word, location, orientation, first=True):
        word = Player().split_word(word)
        points = 0
        word_multiplier = 1
        i = 0
        for letter in word:
            cell, invert_cell, side_cell = self.get_cells(location, i, orientation)
            available = not cell.letter and first
            j = 1
            if invert_cell and invert_cell.letter and available:
                side_word, j = self.get_side_word(invert_cell, i, (orientation,True), location, letter)
                points += self.calculate_word_value(side_word, (location[0] - j + 1, location[1] + i) if orientation else (location[0] + i, location[1] - j + 1), not orientation, False)
            elif side_cell and side_cell.letter and available:
                side_word, j = self.get_side_word(side_cell, i, (orientation,False), location, letter)
                points += self.calculate_word_value(side_word, (location[0], location[1] + i) if orientation else (location[0] + i, location[1]), not orientation, False)
            letter_value = self.get_letter_value(letter)
            word_multiplier, points = self.update_multipliers(cell, letter_value, word_multiplier, points, first)
            i += 1
        points = points * word_multiplier
        return points        
    
    def get_cells(self, location, i, orientation):
        cell = self.grid[location[0] + (i if not orientation else 0)][location[1] + (i if orientation else 0)]
        invert_cell = self.grid[location[0] - i][location[1] - i] if not orientation and location[0] - i >= 0 and location[1] - i >= 0 else None
        side_cell = self.grid[location[0] - i][location[1] + i] if orientation and location[0] - i >= 0 and location[1] + i < 15 else None
        return cell, invert_cell, side_cell
    
    def get_side_word(self, cell, i, orientation, location, letter):
        word = ''
        j = 0
        while cell.tile:
            word += cell.tile.letter
            j += 1
            cell = self.grid[location[0] - j + 1][location[1] + i] if orientation[0] else self.grid[location[0] + i][location[1] - j + 1]
        word += letter
        return word, j
    
    def get_letter_value(self, letter):
        for tile in DATA:
            if letter == tile['letter']:
                return tile['value']
            
    def update_multipliers(self, cell, letter_value, word_multiplier, points, first):
        if cell.multiplier_type == 'letter':
            points += letter_value * cell.multiplier
        elif cell.multiplier_type == 'word':
            word_multiplier *= cell.multiplier
            points += letter_value
        else:
            points += letter_value
        return word_multiplier, points
    