from game.board import Board
from game.player import Player
from game.tilebag import TileBag, Tile, JokerTile
from game.scrabble_game import ScrabbleGame

class GameInterface:
    def __init__(self):
        self.board = Board()
        self.tilebag = TileBag()   
        self.players = []
        self.current_player = None

    def add_players(self):
        try:
            number_of_players = int(input('Ingrese el número de jugadores: '))
            if number_of_players > 1 and number_of_players < 4:
                for i in range(number_of_players):
                    name = input(f'Ingrese el nombre del jugador {i+1}: ')
                    self.players.append(Player(name,i+1,self.tilebag.draw_tiles(7)))
                    self.players[i].add_tiles(self.tilebag.draw_tiles(7))
            else:
                print('Ingrese un número de jugadores válido')
                self.add_players()
        except ValueError:
            print('Ingrese un número de jugadores válido')
            self.add_players()
    



    def play(self):
        print('Bienvenidos a Scrabble')
        self.add_players()
        for i in range(len(self.players)):
            self.current_player = self.players[i]
            print(f'Es el turno de {self.current_player.name}')
            print('El tablero es:')
            print(self.board.show_board())
            print(f'El jugador {self.current_player.name} tiene las siguientes fichas:')
            print(self.current_player.show_tiles())
            print('Ingrese el numero de la opción que desea realizar')
            print('1. Jugar')
            print('2. Cambiar fichas')
            print('3. Pasar turno')
            print('4. Si posee comodín, ingrese la letra que desea que represente')
            print('4. Terminar juego')
            option = str(input())
            if option == '1':
                self.play_turn()
            elif option == '2':
                self.change_tiles()
            elif option == '3':
                pass
            elif option == '4':
                self.select_letter()
            elif option == '5':
                break
            else:
                print('Ingrese una opción válida')
                self.play()
            print('Terminó el turno')
            print('Presione enter para continuar')
            input()
            
    
    def play_turn(self):
        print('Ingrese la palabra que desea jugar con sus fichas:')
        print(self.current_player.show_tiles())
        word = input()
        print('Ingrese la posición en la que desea jugar la palabra (ejemplo: 0,0)')
        position = input()
        position = position.split(',')
        location = (int(position[0]),int(position[1]))
        print('Ingrese la orientación en la que desea jugar la palabra')
        orientation = input()
        if self.board.is_empty():
            if location == (7,7) and self.board.validate_word(word):
                self.board.put_word(word,location,orientation)
                print(self.board.show_board())
            else:
                print('La primera palabra debe ser jugada en la posición 7,7')
                self.play_turn()
        else:
            if self.board.validate_word(word):
                if self.board.validate_len_of_word_in_board(word,location,orientation) and self.board.validate_crossing_words(word,location,orientation):
                    self.board.put_word(word,location,orientation)
                else:
                    print('La palabra no se puede jugar en esa posición ')
                    self.play_turn()
            else:
                print('La palabra no es válida')
                self.play_turn()

    def change_tiles(self):
        print(f'{self.current_player.name} Estas son sus fichas:')
        print(self.current_player.show_tiles())
        print('Ingrese las posicion de las fichas que desea cambiar')
        positions = input()
        positions = positions.split(',')
        positions = [int(i) for i in positions]
        self.current_player.change_tiles(positions,self.tilebag.draw_tiles(len(positions)))
        print('Se han cambiado las fichas')
        print(self.current_player.show_tiles())
        print('Presione enter para continuar')
        input()

    def select_letter(self):
        print(f'{self.current_player.name} Estas son sus fichas:')
        print(self.current_player.show_tiles())
        print('Ingrese la letra que desea que represente el comodín')
        letter = input()
        self.current_player.change_tiles([1],JokerTile(letter,0))
        print('Se ha cambiado la letra del comodín')
        print(self.current_player.show_tiles())
        print('Presione enter para continuar')
        input()

    


if __name__ == '__main__':
    game = GameInterface()
    game.play()
