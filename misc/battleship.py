"""
HEADER: Battleship by Lars Hedlund
Features:
Version: 0.0
"""

from random import randint

def print_board(board):
    for row in board:
        print " ".join(row)

def create_board(total_ships):
    board = []
    board_range = 5 + total_ships # adds an extra row/column for every ship
    for x in range(board_range):
        board.append(["O"] * board_range) # prints 'O' for ocean
    return board

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def place_ships(board, total_ships):
    for ship in range(total_ships):
        ship_row = random_row(board)
        ship_col = random_col(board)
        board[ship_row][ship_col] = "S"
    return board

def main():
    #initializes the game board
    total_ships = int(raw_input("How many ships would you like to play against? "))
    board = create_board(total_ships)
    ships = place_ships(board, total_ships)
    print """
    Welcome to Battleship!
    """
    # prints the game board
    print_board(board)
    # guess checking
    for turn in range(4):
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))

        if guess_row and guess_col == "S":
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                if turn == 3:
                    print "Game Over"
        print "Turn", turn + 1
        print_board(board)

main()
