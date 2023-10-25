from game.scrabble_game import ScrabbleGame

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
        self.play()

    def add_players(self):
        try:
            number_of_players = int(input('Ingrese el número de jugadores: '))
            if number_of_players > 1 and number_of_players < 4:
                return number_of_players
            else:
                print('Ingrese un número de jugadores válido')
                self.add_players()
        except ValueError:
            print('Ingrese un número de jugadores válido')
            self.add_players()

    def play(self):
        board = self.scrabble.board
        while True:
            for i in range(len(self.scrabble.players)):
                current_player = self.scrabble.current_player
                print(f'Es el turno de {current_player.name}')
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
                if option == '1':
                    self.play_turn()
                elif option == '2':
                    self.change_tiles()
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
                    self.play()


                print('Presione enter para continuar')
                input()
                self.scrabble.next_turn()


            
    
    def play_turn(self):
        print('Ingrese la palabra que desea jugar con sus fichas o 5 para salir:')
        print(self.scrabble.current_player.show_tiles())
        word = input().lower()
        if word == '5':
            return 
        print('Ingrese la posición en la que desea jugar la palabra (ejemplo: 0,0)')
        position = input()
        position = position.split(',')
        location = (int(position[0]),int(position[1]))
        print('Ingrese la orientación en la que desea jugar la palabra')
        orientation = input()
        if self.scrabble.board.is_empty():
            if location == (7,7) and self.scrabble.board.validate_word(word) and self.scrabble.current_player.has_tiles(word):
                self.scrabble.board.put_word(word,location,orientation)
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
            if self.scrabble.board.validate_word(word):
                if self.scrabble.board.validate_len_of_word_in_board(word,location,orientation) and self.scrabble.board.validate_crossing_words(word,location,orientation):
                    self.scrabble.board.put_word(word,location,orientation)
                    print(self.scrabble.board.show_board())
                else:
                    print('La palabra no se puede jugar en esa posición ')
                    self.play_turn()
            else:
                print('La palabra no es válida')
                self.play_turn()

    def change_tiles(self):
        print(f'{self.scrabble.current_player.name} Estas son sus fichas:')
        print(self.scrabble.current_player.show_tiles())
        print('Ingrese las posicion de las fichas que desea cambiar')
        positions = input()
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

    def select_letter(self):
        print('Ingrese la letra que desea que represente el comodín')
        letter = input()
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
