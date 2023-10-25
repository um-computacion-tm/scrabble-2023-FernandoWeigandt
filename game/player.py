
class Player:
    def __init__(self,name='',number=0,score=0,bag_tiles=None):
        self.name=name
        self.number=number
        self.score=score
        self.tiles=[]

    def add_tiles(self,tiles):
        self.tiles.extend(tiles)
    
    def show_tiles(self):
        tiles=[]
        for tile in self.tiles:
            tiles.append(tile.letter)
        return tiles
    
    def remove_tiles(self,tiles):
        for tile in tiles:
            self.tiles.remove(tile)

    def has_tiles(self,word):
        for letter in word:
            if letter.upper() not in self.show_tiles():
                return False
        return True