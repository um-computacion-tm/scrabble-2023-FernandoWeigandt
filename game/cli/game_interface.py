# from game.scrabble_game import ScrabbleGame
# from game.board import Board
# from game.tilebag import TileBag


# def main():
#     print("Bienvenido a Scrabble!")
#     while not scrabble_game.end_game():
#         try:
#             player_count = int(input("Cuantos Jugadores? "))
#             if player_count <= 1 or player_count > 4:
#                 raise ValueError
#         except ValueError:
#             print("")
#             print("Por favor ingrese un numero entre 2 y 4")
#             scrabble_game = ScrabbleGame(players_count=player_count, board=Board(), tilebag=TileBag())
#             print('Total de jugadores: ', len(scrabble_game.players))
#             scrabble_game.next_turn()
#             print('Jugador actual: ', scrabble_game.current_player)
#             scrabble_game.show_player_tiles()
#             scrabble_game.show_board()
#             word= input("Ingrese una palabra: ")
#             location_x = input("Coloque su coordenada en x: ")
#             location_y = input("Coloque su coordenada en y: ")
#             location = [location_x, location_y]
#             orientation = input("Coloque la orientacion: ")
#             scrabble_game.validate_init_of_game(word, location, orientation)
#             scrabble_game.validate_len_of_word_in_board(word, location, orientation)
#             scrabble_game.validate_word(word)
#             scrabble_game.calculate_word_value(word)
#             scrabble_game.show_board()


