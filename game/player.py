
class Player:
    def __init__(self,name='',number=0,score=0,bag_tiles=None):
        self.name=name
        self.number=number
        self.score=score
        self.tiles=[]

    def add_tiles(self,tiles):
        self.tiles.extend(tiles)
