
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
    
    def take_tiles(self,word):
        word = self.split_word(word)
        tiles=[]
        for letter in word:
            for tile in self.tiles:
                if tile.letter==letter.upper():
                    tiles.append(tile)
                    self.tiles.remove(tile)
                    break
        return tiles
        
    def has_tiles(self,word):
        lectern = self.tiles.copy()
        cont=0
        word = self.split_word(word)
        for letter in word:
            for tile in lectern:
                if tile.letter == letter.upper():
                    lectern.remove(tile)
                    cont+=1
                    break
        if cont == len(word):
            return True
        else:
            return False

    
    def split_word(self,word):
        word = word.upper()
        if 'CH' in word:
            word = word.replace('CH','1')
        if 'LL' in word:
            word = word.replace('LL','2')
        if 'RR' in word:
            word = word.replace('RR','3')
        result = []
        for letter in word:
            if letter == '1':
                result.append('CH')
            elif letter == '2':
                result.append('LL')
            elif letter == '3':
                result.append('RR')
            else:
                result.append(letter)
        return result
