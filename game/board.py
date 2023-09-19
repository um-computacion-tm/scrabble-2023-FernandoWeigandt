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
        
    
    def put_word(self,word,location, orientation):
        location_x = location[0]
        location_y = location[1]
        if orientation == 'V':
            for i in range(len(word)):
                self.grid[location_x+i][location_y].add_letter(word[i])
        else:
            for i in range(len(word)):
                self.grid[location_x][location_y+i].add_letter(word[i])

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


    def show_board(self):
        print('')
        columnas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        print("  ".join(columnas))
        print('-----------------------------------------------')
        filas  = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
        for i in range(15):
            print(filas[i], end='|  ')
            for j in range(15):
                if self.grid[i][j].letter is None:
                    print('-', end='  ')
                else:
                    print(self.grid[i][j].letter.letter.upper(), end=' ')
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