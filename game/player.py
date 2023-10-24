
class Player:
    def __init__(self,name='',number=0,score=0,bag_tiles=None):
        self.name=name
        self.number=number
        self.score=score
        self.tiles=[]

    def add_tiles(self,tiles):
        self.tiles.extend(tiles)

    def change_tiles(self,player_old_tiles_index=[],player_new_tiles=[]):
        tiles_to_change=[]
        for tile_index in range (len(player_old_tiles_index)):
            tiles_to_change.append(self.tiles[player_old_tiles_index[tile_index]-1])
            self.tiles[player_old_tiles_index[tile_index]-1]=player_new_tiles[player_old_tiles_index[tile_index]-1]
        return tiles_to_change
    
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