"""
HEADER: Simpsons Game by Lars Hedlund
Features: (1) Basic movement is working! (2) Agent movement is working!
(3)
Bugs:
Version: 0.2
"""
from random import randint
import sys

ROWS = 20
COLUMNS = 30
AGENTS = 6

# Homer's positions
START_ROW = 1
START_COLUMN = 1

# GAME STATUS: 0 = still playing, 1 = won, 2 = froze to death,
# 3 = captured, 4 = drowned *)

# Game states
BUILDING      = "#"
EMPTY         = " "
EPA_AGENT     = "E"
HOMER         = "H"
SPRINGFIELD   = "S"
WATER         = "~"

# Movement Keys
UP = "8"
DOWN = "2"
LEFT = "4"
RIGHT = "6"
NO_MOVE = "5"
EXIT = "0"

# Debug flag
DEBUG = False

def debugPrint(description, user_input):
    if DEBUG == True:
        print("<<< %s >>>" % description)
        print("<<< %r >>>" % user_input)
        return user_input
    else:
        return user_input

def printBoard(board):
     print()
     for r in range (0, ROWS, 1):
          for c in range (0, COLUMNS, 1):
               print(board[r][c], end="")
          print()

# Author: James Tam
# function: initializeHC (hard-coded initialization)
# initializeHC(none)
# returns(2DList)
# The legacy method of initializing the game world. It's retained so students can see
# an alternative (non-file IO) method of initialization.
def initializeHC():
    count = 0
    board = []
    agentLocation = []

    # Create the grid. Initialize elements to a space.
    for r in range (0, ROWS, 1):
        board.append ([])
        for c in range (0, COLUMNS, 1):
            board[r].append (" ")

    # Initializes the board from input file
    startPos = open('starting_board.txt', 'r')
    for line in startPos:
        board[count] = line.split(",")
        count += 1
    startPos.close()

    # Create the grid to store agent's positions.
    # Two rows: row zero for agent row coordinates
    #           row one for agent column coordinates
    # Six columns: one for the six agents.
    for r in range (0, 2, 1):
       agentLocation.append ([])
       for c in range (0, AGENTS, 1):
           agentLocation[r].append (0)

    # Contents of the List for the agent positions
    #            COLUMN ZERO        COLUMN ONE         COLUMN TWO         COLUMN THREE       COLUMN FOUR        COLUMN FIVE
    #  ROW ZERO  Agent 1 Row coord  Agent 2 Row coord  Agent 3 Row coord  Agent 4 Row coord  Agent 5 Row coord  Agent 6 Row coord
    #  ROW ONE   Agent 1 Col coord  Agwnt 2 Col coord  Agent 3 Col coord  Agent 4 Col coord  Agent 5 Col coord  Agent 6 Col coord

    # Col 0: Agent at position row = 8, column = 9 (position in grid "board")
    agentLocation [0][0] = 8
    agentLocation [1][0] = 9

    # Col 1: Agent at position row = 13, column = 7 (position in grid "board")
    agentLocation [0][1] = 13
    agentLocation [1][1] = 7

    # Col 2: Agent at position row = 13, column = 17 (position in grid "board")
    agentLocation [0][2] = 13
    agentLocation [1][2] = 17

    # Col 3: Agent at position row = 14, column = 28 (position in grid "board")
    agentLocation [0][3] = 14
    agentLocation [1][3] = 28

    # Col 4: Agent at position row = 15, column = 20 (position in grid "board")
    agentLocation [0][4] = 15
    agentLocation [1][4] = 20

    # Col 5: Agent at position row = 16, column = 16 (position in grid "board")
    agentLocation [0][5] = 16
    agentLocation [1][5] = 16

    return(board,agentLocation)

def player_movement(board, currentRow, currentColumn):
    # Starting variables
    newRow = currentRow
    newColumn = currentColumn
    board[currentRow][currentColumn] = EMPTY
    # Starting text
    print("You can move using the number keys:")
    compass = """
            8
          4 5 6
            2"""
    print(compass)
    print("===================================")
    # Homer's Location
    debugPrint("Homer's Row:", currentRow)
    debugPrint("Homer's Column:", currentColumn)
    # Movement input
    movement = input("Please enter a direction: ")
    if ("-" in movement) and (DEBUG == False):
        DEBUG = True
    if (movement == UP):
        newRow = currentRow - 1
        newColumn = currentColumn
    elif (movement == DOWN):
        newRow = currentRow + 1
        newColumn = currentColumn
    elif (movement == RIGHT):
        newColumn = currentColumn + 1
        newRow = currentRow
    elif (movement == LEFT):
        newColumn = currentColumn - 1
        newRow = currentRow
    elif (movement == NO_MOVE):
        newRow = currentRow
        newColumn = currentColumn
        print("Homer did not move.")
    elif (movement == EXIT):
        exit(0)
    else:
        print("Homer cannot move in that direction")
    # Debug
    debugPrint("Homer's New Row:", newRow)
    debugPrint("Homer's New Column:", newColumn)
    debugPrint("Square type:", board[newRow][newColumn])
    # Checks for game over conditions and return values
    if (board[newRow][newColumn] == WATER):
        print(" cannot swim!")
        return currentRow, currentColumn, True
    if (board[newRow][newColumn] == BUILDING):
        print("Homer cannot walk through walls.")
        board[currentRow][currentColumn] = HOMER
        return currentRow, currentColumn, False
    else:
        board[newRow][newColumn] = HOMER
        return newRow, newColumn, False

def agent_movement(board, agentLocation, agent_num):
    # initial variables
    currentRow = agentLocation[0][agent_num]
    currentColumn = agentLocation[1][agent_num]
    movement = randint(1, 5)
    #      1
    #    2 5 3
    #      4
    # Agent's Location
    debugPrint("Agent's Row:", currentRow)
    debugPrint("Agent's Column:", currentColumn)
    # Movement input
    if (movement == 1):
        newRow = currentRow - 1
        newColumn = currentColumn
    elif (movement == 4):
        newRow = currentRow + 1
        newColumn = currentColumn
    elif (movement == 3):
        newColumn = currentColumn + 1
        newRow = currentRow
    elif (movement == 2):
        newColumn = currentColumn - 1
        newRow = currentRow
    elif (movement == 5):
        newRow = currentRow
        newColumn = currentColumn
        print("Agent did not move.")
    elif (movement == EXIT):
        exit(0)
    else:
        print("Agent cannot move in that direction")
    # Checks for game over conditions and return values
    if (board[newRow][newColumn] == WATER):
        return currentRow, currentColumn
    elif (board[newRow][newColumn] == BUILDING):
        return currentRow, currentColumn
    elif (board[newRow][newColumn] == SPRINGFIELD):
        return currentRow, currentColumn
    elif (board[newRow][newColumn] == EPA_AGENT):
        return currentRow, currentColumn
    else:
        board[currentRow][currentColumn] = EMPTY
        board[newRow][newColumn] = EPA_AGENT
        return newRow, newColumn

def turns_left():
    pass

def start():
    game_over = False
    board = []
    agentLocation = []
    articTime = 0
    currentRow = START_ROW
    currentColumn = START_COLUMN
    direction = 0

    with open("intro.txt", "r") as f:
        print(f.read())

    board, agentLocation = initializeHC()
    while not game_over:
        printBoard(board)
        currentRow, currentColumn, dead = player_movement(board, currentRow, currentColumn)
        for i in range(AGENTS):
            agent_num = i
            agentRow, agentColumn = agent_movement(board, agentLocation, agent_num)
            agentLocation[0][agent_num] = agentRow
            agentLocation[1][agent_num] = agentColumn

start()
