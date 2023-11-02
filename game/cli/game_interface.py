from game.scrabble_game import ScrabbleGame
import os
import ipdb

class GameInterface:

    def __init__(self):
        print('Bienvenidos a Scrabble')
        self.player_count = self.add_players()
        self.scrabble = ScrabbleGame(self.player_count)
        i = 1
        for player in self.scrabble.players:
            player.name = input(f'Nombre del jugador {i}: ')
            player.add_tiles(self.scrabble.tilebag.draw_tiles(7))
            i += 1
        self.scrabble.next_turn()

    def add_players(self):
        try:
            number_of_players = int(input('Ingrese el número de jugadores: '))
            return number_of_players if (number_of_players > 1 and number_of_players) < 4 else ValueError
        except:
            print('Ingrese un número de jugadores válido')
            return self.add_players()

    def play(self):
        board = self.scrabble.board
        while True:
            for i in range(len(self.scrabble.players)):
                current_player = self.scrabble.current_player
                print(f'Es el turno de {current_player.name}')
                print(f'La Ronda es: {self.scrabble.round}')
                print('El tablero es:')
                print(board.show_board())
                print(f'El jugador {current_player.name} tiene las siguientes fichas:')
                print(current_player.show_tiles())
                print('Ingrese el numero de la opción que desea realizar')
                print('1. Jugar')
                print('2. Cambiar fichas')
                print('3. Pasar turno')
                print('4. Si posee comodín, ingrese la letra que desea que represente')
                print('5. Terminar juego')
                option = str(input())
                flag = True
                if option == '1':
                    self.play_turn()
                elif option == '2':
                    flag = self.change_tiles()
                elif option == '3':
                    pass
                elif option == '4':
                    self.select_letter()
                elif option == '5':
                    print('Gracias por jugar')
                    print('Los puntajes son:')
                    for player in self.scrabble.players:
                        print(f'{player.name}: {player.score}')
                    return
                else:
                    print('Ingrese una opción válida')
                    flag = False

                print('Presione enter para continuar')
                input()
                if flag:
                    self.scrabble.next_turn()
                os.system('clear')
                
    def play_turn(self):
        print('Ingrese la palabra que desea jugar con sus fichas o 5 para salir:')
        print(self.scrabble.current_player.show_tiles())
        word = str(input()).lower()
        if word == '5':
            return 
        print('Ingrese la coordenada de la fila')
        try:
            row = int(input())
        except:
            print('Ingrese una coordenada válida')
            self.play_turn()
        print('Ingrese la coordenada de la columna')
        try:
            column = int(input())
        except:
            print('Ingrese una coordenada válida')
            self.play_turn()
        location = (row,column)
        print('Ingrese la orientación en la que desea jugar la palabra')
        print('1. Horizontal')
        print('2. Vertical')
        orientation = input()
        orientation = orientation == '1'
        if self.scrabble.board.is_empty():
            if self.scrabble.validate_initial_word(word,location,orientation):
                word = self.scrabble.board.remove_accent(word)
                tiles = self.scrabble.current_player.take_tiles(word)
                self.scrabble.board.put_word(tiles,location,orientation)
                self.scrabble.current_player.add_tiles(self.scrabble.tilebag.draw_tiles(7-len(self.scrabble.current_player.tiles)))
                print(self.scrabble.board.show_board())

            elif self.scrabble.current_player.has_tiles(word) == False:
                print('Usted no tiene las fichas para jugar esa palabra')
                self.play_turn()
            elif self.scrabble.board.validate_word(word) == False:
                print('La palabra no es válida')
                self.play_turn()
            else:
                print('La palabra no se puede jugar en esa posición ')
                self.play_turn()
        else:
            if self.scrabble.validate_all(word,location,orientation):
                word_with_out_intersection = self.scrabble.board.get_word_without_intersections(word,location,orientation)
                word_with_out_intersection = self.scrabble.board.remove_accent(word_with_out_intersection)
                if self.scrabble.current_player.has_tiles(word_with_out_intersection):
                    tiles = self.scrabble.current_player.take_tiles(word_with_out_intersection)
                    self.scrabble.board.put_word(tiles,location,orientation)
                    self.scrabble.current_player.add_tiles(self.scrabble.tilebag.draw_tiles(7-len(self.scrabble.current_player.tiles)))
                    print(self.scrabble.board.show_board())
            elif self.scrabble.board.validate_len_of_word_in_board(word,location,orientation) == False:
                print('La palabra no se puede jugar en esa posición ')
                self.play_turn()
            else:
                print('La palabra no es válida')
                self.play_turn()
            

    def change_tiles(self):
        print(f'{self.scrabble.current_player.name} Estas son sus fichas:')
        print(self.scrabble.current_player.show_tiles())
        print('Ingrese las posicion de las fichas que desea cambiar o 8 para salir')
        positions = input()
        if positions == '8':
            return False
        positions = positions.split(',')
        positions = [int(position) for position in positions]
        new_tiles = self.scrabble.tilebag.draw_tiles(len(positions))
        old_tiles = self.scrabble.change_tiles(positions)
        self.scrabble.tilebag.put_tiles(old_tiles)
        self.scrabble.tilebag.shuffle()
        print('Se han cambiado las fichas')
        print(self.scrabble.current_player.show_tiles())
        print('Presione enter para continuar')
        input()
        return True

    def select_letter(self):
        print('Ingrese la letra que desea que represente el comodín o enter para salir')
        letter = input()
        if letter == '\n':
            return
        for tile in self.scrabble.current_player.tiles:
            if tile.letter == '_':
                tile.letter = letter.upper()
                print('Se ha cambiado la letra del comodín')
                print(self.scrabble.current_player.show_tiles())
                print('Presione enter para continuar')
                input()
                return

    


if __name__ == '__main__':
    game = GameInterface()
    game.play()
