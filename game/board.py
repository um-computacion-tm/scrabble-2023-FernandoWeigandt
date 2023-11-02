from game.tilebag import Tile
from game.cell import Cell
from pyrae import dle
from game.player import Player
from diccionario import DATA

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


    def validate_word(self, word):
        dle.set_log_level(log_level='CRITICAL')
        flag=dle.search_by_word(word)
        if word.lower() not in flag.title:
            return False
        else:
            return True
        
        
    def validate_crossing_words(self, word, location, orientation):
        for i, letter in enumerate(word):
            row, col = (location[0], location[1] + i) if orientation == True else (location[0] + i, location[1])
            cell = self.grid[row][col]
            if cell.letter is not None and cell.letter != letter:
                return True
        return False
           

    def show_board(self):
        view = '       \n     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O  \n'
        for i in range(len(self.grid)):
            view += f'  {i}  ' if i <= 9 else f'  {i} '
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
            view += '\n' 
        return view

        
    def put_word(self,word,pos,horizontal):
        j=0
        for i in range(len(word)):
            cell = self.grid[pos[0]][pos[1]+i+j] if horizontal else self.grid[pos[0]+i+j][pos[1]]
            while cell.letter:
                j+=1
                cell = self.grid[pos[0]][pos[1]+i+j] if horizontal else self.grid[pos[0]+i+j][pos[1]]
            cell.letter = word[i]


    def remove_accent(self, word):
        word = word.replace('Á','A')
        word = word.replace('É','E')
        word = word.replace('Í','I')
        word = word.replace('Ó','O')
        word = word.replace('Ú','U')
        return word
    
    def get_word_without_intersections(self,word,pos,horizontal):
        result = ''
        for i in range(len(word)):
            cell = self.grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].letter
            if not cell:
                result += word[i]
        return result
        
