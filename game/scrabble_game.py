from game.board import Board
from game.player import Player
from game.tilebag import TileBag



class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = TileBag()
        self.players = []
        for number in range(players_count):
            self.players.append(Player(number=number))

    def end_game(self):
        if  self.bag_tiles == []:
            return True
        else:
            return False
        
    