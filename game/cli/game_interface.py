from game.board import Board
from game.player import Player
from game.tilebag import TileBag, Tile, JokerTile

class GameInterface:
    def __init__(self):
        self.board = Board()
        self.tilebag = TileBag()
        self.players = []
        self.current_player = None

    def add_players(self):
        try:
            number_of_players = int(input('Ingrese el número de jugadores: '))
            for i in range(number_of_players):
                name = input(f'Ingrese el nombre del jugador {i+1}: ')
                self.players.append(Player(name,i+1,self.tilebag.draw_tiles(7)))
        except ValueError:
            print('Ingrese un número de jugadores válido')
            self.add_players()
    



    def play(self):
        print('Bienvenidos a Scrabble')
        self.add_players()
        for i in range(len(self.players)):
            self.current_player = self.players[i]
            print(f'Es el turno de {self.current_player.name}')
            self.current_player.show_tiles()
            print('Ingrese el numero de la opción que desea realizar')
            print('1. Jugar')
            print('2. Cambiar fichas')
            print('3. Terminar turno')
            option = input()
            if option == '1':
                self.play_turn()
            elif option == '2':
                self.change_tiles()
            elif option == '3':
                pass
            else:
                print('Ingrese una opción válida')
                self.play()
            self.board.show_board()
            self.current_player.show_tiles()
            print('Terminó el turno')
            print('Presione enter para continuar')
            input()
    
    def play_turn(self):
        print('Ingrese la palabra que desea jugar')
        word = input()
        print('Ingrese la posición en la que desea jugar la palabra (ejemplo: 00)')
        position = input()
        location = (int(position[0]),int(position[1]))
        print('Ingrese la orientación en la que desea jugar la palabra')
        orientation = input()
        if self.board.is_empty():
            if location == (7,7) and self.board.validate_word(word):
                self.board.put_word(word,location,orientation)
                self.current_player.remove_tiles(word)
        else:
            if self.board.validate_word(word):
                if self.board.validate_word_place_board(word,location,orientation):
                    self.board.put_word(word,location,orientation)
                    self.current_player.remove_tiles(word)
                else:
                    print('La palabra no se puede jugar en esa posición')
            else:
                print('La palabra no es válida')
                self.play_turn()

    def change_tiles(self):
        print('Ingrese las fichas que desea cambiar (ejemplo: A,B,C)')
        tiles = input()
        tiles = tiles.split(',')
        for tile in tiles:
            if tile in self.current_player.tiles:
                self.tilebag.put_tile(self.current_player.remove_tile(tile))
        self.current_player.add_tiles(self.tilebag.draw_tiles(len(tiles)))
        print('Se han cambiado las fichas')
        self.current_player.show_tiles()
        print('Presione enter para continuar')
        input()

if __name__ == '__main__':
    game = GameInterface()
    game.play()
