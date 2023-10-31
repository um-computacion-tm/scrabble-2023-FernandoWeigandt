from game.board import Board
from game.player import Player
from game.tilebag import TileBag



class ScrabbleGame:

    def __init__(self, players_count):
        self.board = Board()
        self.tilebag = TileBag()
        self.players = [Player(number=number) for number in range(players_count)]
        self.current_player = None
        self.round = 0

    def next_turn(self):
        self.round += 1
        if self.current_player == None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player)+1
            self.current_player=self.players[index]   
    
    def validate_all(self, word,location,orientation):
        if self.board.validate_word(word) and self.board.validate_len_of_word_in_board(word,location,orientation):
            return True
        
    def validate_initial_word(self, word,location,orientation):
        if self.board.validate_word(word) and self.board.validate_len_of_word_in_board(word,location,orientation) and self.board.is_empty() and self.current_player.has_tiles(word) and self.board.validate_init_of_game(word,location,orientation):
            return True
        
    def show_board(self):
        return self.board.__repr__
    
    def change_tiles(self, old_tiles_index=[]):
        new_tiles=self.tilebag.draw_tiles(len(old_tiles_index))
        old_tiles = []
        for i in old_tiles_index:
            old_tiles.append(self.current_player.tiles[i-1])
            self.current_player.tiles[i-1] = new_tiles.pop(0)
        self.tilebag.put_tiles(old_tiles)
        return old_tiles
    