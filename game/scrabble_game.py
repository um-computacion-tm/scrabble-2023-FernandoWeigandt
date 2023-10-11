from game.board import Board
from game.player import Player
from game.tilebag import TileBag



class ScrabbleGame:

    def __init__(self, players_count):
        self.board = Board()
        self.tilebag = TileBag()
        self.players = [Player(number=number) for number in range(players_count)]
        self.current_player = None

    # def play(self, word, location, orientation):
    #     self.validate_word(word)
    #     self.board.put_word(word, location, orientation)
    #     total = Board().calculate_word_value(word)
    #     self.players[self.current_player].score += total
    #     self.next_turn()

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player)+1
            self.current_player=self.players[index]   
    
    def distribute_tiles(self):
        for player in self.players:
            player.add_tiles(self.tilebag.draw_tiles(7))

    def validate_word(self, word):
        return self.board.validate_word(word)
        
    def show_board(self):
        return self.board.__repr__
    
    def show_player_tiles(self):
        return self.current_player.show_tiles()

    def end_game(self):
        if  self.tilebag == []:
            return True
        else:
            return False
        
    