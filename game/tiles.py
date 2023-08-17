import random

class TooMuchTiles (Exception):
    pass

class TooMuchTilesPut(Exception):
    pass

TOTALTILES=98

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class TileBag:
    def __init__(self):
        self.tiles =  [
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1),
            Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1),
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),
            Tile('G', 2), Tile('G', 2), 
            Tile('B', 3), Tile('B', 3),
            Tile('C', 3), Tile('C', 3), Tile('C', 3), Tile('C', 3),
            Tile('M', 3), Tile('M', 3),
            Tile('P', 3), Tile('P', 3),
            Tile('F', 4),
            Tile('H', 4), Tile('H', 4),
            Tile('V', 4),
            Tile('Y', 4),
            Tile('CH', 5),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('LL', 8),
            Tile('Ñ', 8),
            Tile('RR', 8),
            Tile('X', 8),
            Tile('Z', 10)
        ]
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
            print('Sacaste mas fichas de las que habian')
            return tile_drawn

    def put_tiles(self,tiles:list):
        try:
            if len(tiles)+len(self.tiles)<=TOTALTILES:
                self.tiles.extend(tiles)
            else:
                raise TooMuchTilesPut
        except TooMuchTilesPut:
            print('La bolsa esta llena o hay fichas de mas')

    def tiles_remaining(self):
        return len(self.tiles)

