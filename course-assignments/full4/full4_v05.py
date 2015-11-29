"""
HEADER: Simpsons Game by Lars Hedlund
Features: (1) Testing "find player"
Bugs:
Version: 0.5
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
# 3 = captured, 4 = drowned

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

def debugPrint(user_input):
    if DEBUG == True:
        print("<<<", user_input, ">>>")

def printBoard(board):
     print()
     for r in range (0, ROWS, 1):
          for c in range (0, COLUMNS, 1):
               print(board[r][c], end="")
          print()

def initialize_world(board, agentLocation):
    count = 0
    # Create the grid. Initialize elements to a space.
    for r in range(ROWS):
        board.append([])
        for c in range(COLUMNS):
            board[r].append(str())

    # Initializes the board from input file
    if DEBUG == True:
        file = input("Which file would you like to load for testing: ")
        with open(file, 'r') as start:
            for line in start:
                new_line = line.rstrip("\n")
                board[count] = list(new_line)
                count += 1
    else:
        with open('starting_board.txt', 'r') as start:
            for line in start:
                new_line = line.rstrip("\n")
                board[count] = list(new_line)
                count += 1

    # Author of code below: James Tam
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
    distraction_prob = randint(0,100)
    distracted = False
    global DEBUG

    # Starting text
    print("You can move using the number keys:")
    compass = """
            8
          4 5 6
            2"""
    print(compass)
    print("To skip a turn, type 5. To exit, type 0.")
    # Movement input
    movement = input("Please enter a direction: ")
    # Set debug mode
    if ("-" in movement) and (DEBUG == False):
        DEBUG = True
        movement = movement[1]
    elif ("-" in movement) and (DEBUG == True):
        DEBUG = False
        movement = movement[1]
    else:
        pass
    # Probability of being distracted
    if (0 < distraction_prob < 25):
        distracted = True
    # Movement Directions
    if (distracted == True) and (movement in (UP,DOWN,LEFT,RIGHT)):
        newRow = currentRow
        newColumn = currentColumn
        print("Homer becomes distracted and refuses to move.")
    elif (movement == UP):
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
    elif (movement in "1379"):
        print("Homer doesn't know how to move that way.")
    elif (movement == EXIT):
        exit(0)
    else:
        error("pc", "player_movement()")
    # Debug
    debugPrint("Homer's (r/c): (%r/%r)" % (newRow, newColumn))
    debugPrint("Square type: %r" % board[newRow][newColumn])
    debugPrint("Distraction number generated: %r" % distraction_prob)
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
    # Flag for agent movement
    can_move = False
    # Agent's Location
    debugPrint("Agent %i (r/c): (%r/%r)" % (agent_num, currentRow, currentColumn))
    # Movement input
    while can_move == False:
        movement = randint(1, 5)
        #      1
        #    2 5 3
        #      4
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
        elif (movement == EXIT):
            exit(0)
        else:
            error("npc", "agent_movement()")
        # Checks for game over conditions and return values
        if (board[newRow][newColumn] in (WATER,BUILDING,SPRINGFIELD,EPA_AGENT)):
            can_move = False
        else:
            can_move = True
            board[currentRow][currentColumn] = EMPTY
            board[newRow][newColumn] = EPA_AGENT
            return newRow, newColumn

def freezing_time(articTime):
    time_left = 10 - articTime
    print("Time in Alaska: %i days" % articTime)
    print("Time to leave before freezing: %i days" % time_left)

def error(code, function):
    print("Critical Error in function: %s" % function)
    if code == "npc":
        print("Agent move value caused an unknown error.")
    elif code == "pc":
        print("Homer's move value caused an unknown error.")
    elif code == "time":
        print("Artic time value caused an unknown error.")
    else:
        print("Exiting the program.")
        exit(0)
    print("Exiting the program.")
    exit(0)

def surrounding_space(board):
    currentRow, currentColumn = find_char(board, HOMER)
    debugPrint("Homer's (r/c): (%r/%r)" % (currentRow, currentColumn))

    sqrN = board[currentRow - 1][currentColumn]
    sqrNE = board[currentRow - 1][currentColumn + 1]
    sqrNW = board[currentRow - 1][currentColumn - 1]
    sqrS = board[currentRow + 1][currentColumn]
    sqrSE = board[currentRow + 1][currentColumn + 1]
    sqrSW = board[currentRow + 1][currentColumn - 1]
    sqrW = board[currentRow][currentColumn - 1]
    sqrE = board[currentRow][currentColumn + 1]
    # Return surrounding squares
    debugPrint("""
    Surrounding space:
         %r %r %r
         %r     %r
         %r %r %r
    """ % (sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE))
    #return sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE
    if "E" in (sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE):
        return True
    else:
        return False

def find_char(board, char):
    for r, columns in enumerate(board):
        for c, square in enumerate(columns):
            if (square == char):
                return r, c
            else:
                pass

def start():
    board = []
    agentLocation = []
    currentRow = START_ROW
    currentColumn = START_COLUMN
    articTime = 0
    global DEBUG

    debug_mode = input("Start in debug mode? (y/n): ")
    if debug_mode == "y":
        DEBUG = True
    else:
        DEBUG = False

    # Start game and print starting board
    with open("intro.txt", "r") as intro:
        print(intro.read())
    board, agentLocation = initialize_world(board, agentLocation)
    freezing_time(articTime)
    printBoard(board)
    print("%r" % agentLocation)

    # Movement and game over conditions
    game_over = surrounding_space(board)
    while not game_over:
        # Agent and player movement
        currentRow, currentColumn, dead = player_movement(board, currentRow, currentColumn)
        for i in range(AGENTS):
            agent_num = i
            agentRow, agentColumn = agent_movement(board, agentLocation, agent_num)
            agentLocation[0][agent_num] = agentRow
            agentLocation[1][agent_num] = agentColumn
        # Tracking time
        print("===================================")
        if (currentRow < 6):
            articTime += 1
            freezing_time(articTime)
        elif (currentRow >= 6):
            articTime = 0
        else:
            error("time", "start()")
        # Game over and print board

        game_over = surrounding_space(board)
        printBoard(board)

start()
