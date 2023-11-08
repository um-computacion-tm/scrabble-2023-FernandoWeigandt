from game.board import Board
from game.player import Player
from game.tilebag import TileBag



class ScrabbleGame:

    def __init__(self, players_count):
        self.board = Board()
        self.tilebag = TileBag()
        self.players = [Player(number=number) for number in range(players_count)]
        self.current_player = None
        self.round = 1

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.round += 1
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player)+1
            self.current_player=self.players[index]   
    
    def change_tiles(self, old_tiles_index=[]):
        new_tiles=self.tilebag.draw_tiles(len(old_tiles_index))
        old_tiles = []
        for i in old_tiles_index:
            old_tiles.append(self.current_player.tiles[i-1])
            self.current_player.tiles[i-1] = new_tiles.pop(0)
        self.tilebag.put_tiles(old_tiles)
        return old_tiles
    
    def end_game(self):
        if self.tilebag.tiles == []:
            for player in self.players:
                if player.tiles == []:
                    return True
                else:
                    return False
        elif self.players[0].surrender == 3:
            return True
        else:
            return False