import random
from diccionario import DATA

class TooMuchTiles (Exception):
    pass

class TooMuchTilesPut(Exception):
    pass

class EmptyTiles(Exception):
    pass

TOTALTILES=100

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class JokerTile(Tile):
    
    def __init__(self, letter, value):
        super().__init__(letter, value)


    def chooseLetter(self,letter_joker):
        for i in DATA:
            if i['letter']==letter_joker.upper():
                self.letter=letter_joker.upper()
                self.value=i['value']
                break
        else:
            raise EmptyTiles    

class TileBag:
    def __init__(self):
        self.tiles=[]
        for i in DATA:
            for j in range(i.get('quantity')):
                self.tiles.append(Tile(i.get("letter"),i.get("value")))
        random.shuffle(self.tiles)
 
    def draw_tiles(self,cantidad):
        tile_drawn=[]
        try:
            if cantidad>len(self.tiles):
                raise TooMuchTiles
            else:
                for i in range(cantidad):
                    tile_drawn.append(self.tiles.pop())
                return tile_drawn
        except TooMuchTiles:
            return tile_drawn

    def put_tiles(self,tiles:list):
        try:
            if len(tiles)+len(self.tiles)<=TOTALTILES:
                self.tiles.extend(tiles)
            else:
                raise TooMuchTilesPut
        except TooMuchTilesPut:
            return TooMuchTilesPut

    def tiles_remaining(self):
        return len(self.tiles)