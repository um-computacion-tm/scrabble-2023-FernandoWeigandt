from game.board import Board
from game.player import Player
from game.tilebag import TileBag



class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = TileBag()
        self.players = []
        self.current_player = None
        for number in range(players_count):
            self.players.append(Player(number=number))

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player)+1
            self.current_player=self.players[index]   
    
    def validate_word(self, word, location, orientation):
        self.board.validate_len_of_word_in_board(self, word, location, orientation)

    def end_game(self):
        if  self.bag_tiles == []:
            return True
        else:
            return False
        
    