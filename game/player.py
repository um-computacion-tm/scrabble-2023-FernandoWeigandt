
class Player:
    def __init__(self,name,number,score):
        self.name=name
        self.number=number
        self.score=score
        self.tiles=[]

    def give_tiles(self,tiles):
        self.tiles.extend(tiles)
'''
    def change_tiles_given(self,tilebag):
        for i in self.tiles:
            tilebag.put_tiles([i])
        self.tiles=[]
        self.give_tiles(tilebag.draw_tiles(7))
        
'''    
            
        