from game.scrabble_game import ScrabbleGame
from game.board import Board
from game.tilebag import Tile


def main():
    print("Welcome to Scrabble!")
    while True:
        try:
            player_count = int(input("How many players? "))
            if player_count <= 1 or player_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Please enter a number between 2 and 4")
            scrabble_game = ScrabbleGame(players_count=player_count)
            print('Number of playes: ', len(scrabble_game.players))
            scrabble_game.next_turn()
            print('Current player: ', scrabble_game.current_player)
            word= input("Enter a word: ")
            location_x = input("Enter x coordinate: ")
            location_y = input("Enter y coordinate: ")
            location = [location_x, location_y]
            orientation = input("Enter orientation (V/H): ")

def print_board(board):
    print('                  TABLERO\n')
    print(' '*8,end='')
    for i in 'ABCDEFGHIJKLMNL':
        print(f'{i}',end=' ')
    print()
    for row in range(len(board)):
        if row+1 < 10:
           print(f'  {row+1}  | ', end=' ')
        else:
            print(f' {row+1}  | ', end=' ')
        for column in range(len(board[row])):
            if not(board[row][column].letter is None):
                print(f'{board[row][column].letter.letter}', end=' ')
            else:
                print('_',end=' ')
        print()
    print()
       
if __name__ == '__main__':
    main()
