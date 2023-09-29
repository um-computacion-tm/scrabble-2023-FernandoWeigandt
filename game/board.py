from game.tilebag import Tile
from pyrae import dle 

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
        flag=dle.search_by_word(word)
        if word.lower() in flag.title:
            return True 
        else:
            return False
        

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

    def show_board(self):
        print('')
        columnas = ['   ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        print("  ".join(columnas))
        print('-------------------------------------------------')
        filas  = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
        for i in range(15):
            print(filas[i], end='|  ')
            for j in range(15):
                if self.grid[i][j].letter is None:
                    print('-', end='  ')
                else:
                    print(self.grid[i][j].letter.letter.upper(), end='  ')
            print('')
        print('')   


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
        
