"""
HEADER: Text Game
AUTHOR: Lars Hedlund

MAIN FEATURES:
(1) Create board (2) Move player (3) Move Moblin (4) Capture Player

TO BE IMPLEMENTED:
(1) Game Over (2) Intro (3) Import maps

BUGS: None known
VERSION: 0.0

ABOUT:
Small text adventure in the style of 'brogue' where you guide a
character (L) to the goal (V) without getting caught by the Moblin
(M). This game was a quick conceptual demo I created for a course
assignment in CPSC 231. As such, I may not write a complete version.
"""

from random import randint
import sys

DEBUG_MODE = False

# Game board
board = []

# Movement keys
UP = "W"
DOWN = "S"
LEFT = "A"
RIGHT = "D"
NO_MOVE = "Q"
EXIT = "E"

# Tiles and characters
PLAYER = "L"
VILLAGE = "V"
MOBLIN = "M"
WATER = "~"
EMPTY = " "
ROCKS = "#"

# Board size
BOARD_WIDTH = 20
BOARD_HEIGHT = 20

# Edges
U_EDGE = 0
B_EDGE = BOARD_HEIGHT - 1
L_EDGE = 0
R_EDGE = BOARD_WIDTH - 1

def print_board(board):
    for r in range(BOARD_WIDTH):
        for c in range(BOARD_HEIGHT):
            print(board[r][c], end="")

def initialize_game(board):
    # Create board
    for r in range(BOARD_WIDTH):
        board.append([])
        for c in range(BOARD_HEIGHT):
            board[r].append(" ")
    # Link's Location
    currentRow = int(BOARD_HEIGHT - 2)
    currentCol = int(BOARD_WIDTH / 2)
    board[currentRow][currentCol] = PLAYER
    # Village Location
    board[0][0] = VILLAGE
    # Moblin Location
    moblinR = 1
    moblinC = BOARD_WIDTH - 2
    board[moblinR][moblinC] = MOBLIN
    # Water locations
    for i in range(BOARD_HEIGHT):
        board[i][BOARD_WIDTH - 1] = WATER
    # Returned values
    return currentRow, currentCol, moblinR, moblinC

def game_over(reason, board):
    print_board(board)
    print(reason)
    print("Game over.")
    exit(0)

def surrounding_space(charR, charC):
    if charR == U_EDGE:
        sqr_up = "TOP EDGE"
        sqr_down = board[charR + 1][charC]
        sqr_left = board[charR][charC - 1]
        sqr_right = board[charR][charC + 1]
    elif charR == B_EDGE:
        sqr_up = board[charR - 1][charC]
        sqr_down = "BOTTOM EDGE"
        sqr_left = board[charR][charC - 1]
        sqr_right = board[charR][charC + 1]
    elif charC == L_EDGE:
        sqr_up = board[charR - 1][charC]
        sqr_down = board[charR + 1][charC]
        sqr_left = "LEFT EDGE"
        sqr_right = board[charR][charC + 1]
    elif charC == R_EDGE:
        sqr_up = board[charR - 1][charC]
        sqr_down = board[charR + 1][charC]
        sqr_left = board[charR][charC - 1]
        sqr_right = "RIGHT EDGE"
    else:
        sqr_up = board[charR - 1][charC]
        sqr_down = board[charR + 1][charC]
        sqr_left = board[charR][charC - 1]
        sqr_right = board[charR][charC + 1]
    # Return surrounding squares
    return sqr_up, sqr_down, sqr_left, sqr_right

def player_movement(char_name, board, currentRow, currentCol):
    # Starting variables
    newRow = currentRow
    newCol = currentCol
    board[currentRow][currentCol] = EMPTY
    # Starting text
    print("You can move using the letter keys:")
    compass = """
            W
          A   D
            S"""
    print(compass)
    print("===================================")
    # Movement input
    movement = input("Please enter a direction: ")
    if (movement == UP):
        newRow = currentRow - 1
        newCol = currentCol
    elif (movement == DOWN):
        newRow = currentRow + 1
        newCol = currentCol
    elif (movement == RIGHT):
        newCol = currentCol + 1
        newRow = currentRow
    elif (movement == LEFT):
        newCol = currentCol - 1
        newRow = currentRow
    elif (movement == NO_MOVE):
        newRow = currentRow
        newCol = currentCol
        print("%s did not move." % char_name)
    elif (movement == EXIT):
        exit(0)
    # Player inputs an invalid number
    else:
        print("%s cannot move in that direction"  % char_name)
    # Checks for game over conditions and return values
    if (board[newRow][newCol] == WATER):
        print("%s cannot swim!" % char_name)
        return currentRow, currentCol
    if (board[newRow][newCol] == BUILDING):
        print("%s cannot walk through rocks." % char_name)
        return currentRow, currentCol
    else:
        board[newRow][newCol] = PLAYER
        return newRow, newCol

def moblin_movement(board, moblinR, moblinC):
    movement = randint(1, 5)
    #      1
    #    2 5 3
    #      4
    # Surrounding spaces
    sqr_up, sqr_down, sqr_left, sqr_right = surrounding_space(moblinR, moblinC)
    # space conditions
    if WATER in (sqr_up, sqr_down, sqr_left, sqr_right):
        movement = 2
    # Moblin movement
    if (movement == 1) and (moblinR > U_EDGE):
        board[moblinR][moblinC] = GRASS
        moblinR -= 1
        board[moblinR][moblinC] = MOBLIN
    elif (movement == 4) and (moblinR < B_EDGE):
        board[moblinR][moblinC] = GRASS
        moblinR += 1
        board[moblinR][moblinC] = MOBLIN
    elif (movement == 3) and (moblinC < R_EDGE):
        board[moblinR][moblinC] = GRASS
        moblinC += 1
        board[moblinR][moblinC] = MOBLIN
    elif (movement == 2) and (moblinC > L_EDGE):
        board[moblinR][moblinC] = GRASS
        moblinC -= 1
        board[moblinR][moblinC] = MOBLIN
    # Player doesn't move any squares
    elif (movement == 5):
        pass
    else:
        print("Moblin stays put.")
    # Returns the new values, or the same values if unchanged
    return moblinR, moblinC


def main(board):
    game_over = False
    currentRow, currentCol, moblinR, moblinC = initialize_game(board)
    print_board(board)
    # Moving Link
    while not game_over:
        print_board(board)
        currentRow, currentCol = player_movement(board, currentRow, currentCol)
        moblinR, moblinC = moblin_movement(board, moblinR, moblinC)

main(board)
