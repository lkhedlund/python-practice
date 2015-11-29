# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Simpsons Game
AUTHOR: Lars Hedlund
CURRENT FEATURES: (1) Debug modes written and set; (2) initialize
world pulls from file to load locations; (3) Player movement working;
(4) Agent movement working (5) Game states (i.e. win, lose, freeze, caught);
(6) Error messages set (7)
BUGS: None!
Version: 0.6
"""

from random import randint
import sys

ROWS = 20
COLUMNS = 30
AGENTS = 6

# Characters and spaces
BUILDING      = "#"
EMPTY         = " "
EPA_AGENT     = "E"
HOMER         = "H"
SPRINGFIELD   = "S"
WATER         = "~"

# Movement Keys
UP = 8
DOWN = 2
LEFT = 4
RIGHT = 6
NO_MOVE = 5
EXIT = 0

# Debug flag
DEBUG = False

def debugPrint(user_input):
    if DEBUG == True:
        print("<<<", user_input, ">>>")

def printBoard(board):
    print("==========GAME BOARD==========")
    for r in range (0, ROWS, 1):
        for c in range (0, COLUMNS, 1):
            print(board[r][c], end="")
        print()

def initialize_world():
    board = []
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

    return(board)

def find_char(board, char):
    # initial variable
    location = []
    # create two rows, one for row and one for column
    for i in range(2):
        location.append([])
    for r, columns in enumerate(board):
        for c, square in enumerate(columns):
            if (square == char):
                debugPrint("find_char() function:")
                debugPrint("Finding %r" % char)
                debugPrint("Location (r/c): (%r/%r)" % (r,c))
                location[0].append(r)
                location[1].append(c)
                debugPrint("%r" % location)
            else:
                pass
    return location

def player_movement(board, homerLocation):
    # Starting variables
    currentRow = homerLocation[0][0]
    currentColumn = homerLocation[1][0]
    board[currentRow][currentColumn] = EMPTY
    distraction_prob = randint(0,100)
    distracted = False
    valid_input = False
    global DEBUG
    # debug print
    debugPrint("player_movement() function:")
    debugPrint("Homer's location (r/c): (%r/%r)" % (currentRow, currentColumn))
    # Starting text
    print("You can move using the number keys:")
    compass = """
            8
          4 5 6
            2"""
    print(compass)
    print("To skip a turn, type 5. To exit, type 0.")
    # Movement input
    while valid_input == False:
        movement = int(input("Please enter a direction: "))
        # Set debug mode
        if (movement < 0) and (DEBUG == False):
            DEBUG = True
            movement = abs(movement)
        elif (movement < 0) and (DEBUG == True):
            DEBUG = False
            movement = abs(movement)
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
            valid_input = True
        elif (movement == UP):
            newRow = currentRow - 1
            newColumn = currentColumn
            valid_input = True
        elif (movement == DOWN):
            newRow = currentRow + 1
            newColumn = currentColumn
            valid_input = True
        elif (movement == RIGHT):
            newColumn = currentColumn + 1
            newRow = currentRow
            valid_input = True
        elif (movement == LEFT):
            newColumn = currentColumn - 1
            newRow = currentRow
            valid_input = True
        elif (movement == NO_MOVE):
            newRow = currentRow
            newColumn = currentColumn
            print("Homer did not move.")
            valid_input = True
        elif (str(movement) in "1379"):
            newRow = currentRow
            newColumn = currentColumn
            print("Homer doesn't know how to move that way.")
            valid_input = True
        elif (movement > 9):
            print("Invalid input. Please try again.")
            valid_input = False
        elif (movement == EXIT):
            game_over("quit")
        else:
            error("pc", "player_movement()")
    # Debug
    debugPrint("Homer's new (r/c): (%r/%r)" % (newRow, newColumn))
    debugPrint("Square type: %r" % board[newRow][newColumn])
    debugPrint("Distraction number generated: %r" % distraction_prob)
    # If it makes it this far, the input is valid
    valid_input = True
    # Checks for game over conditions and return values
    if (board[newRow][newColumn] == WATER):
        game_over("drowned")
    elif (board[newRow][newColumn] == SPRINGFIELD):
        game_over("win")
    if (board[newRow][newColumn] == BUILDING) or (board[newRow][newColumn] == EPA_AGENT):
        print("Homer's personal bubble won't let him enter an occupied space.")
        board[currentRow][currentColumn] = HOMER
        return currentRow, currentColumn
    else:
        board[newRow][newColumn] = HOMER
        return newRow, newColumn

def agent_movement(board, agentLocation, agent_num):
    # initial variables
    currentRow = agentLocation[0][agent_num]
    currentColumn = agentLocation[1][agent_num]
    # Flag for agent movement
    can_move = False
    # debug printing
    debugPrint("agent_movement() function:")
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
    # Debug printing
    debugPrint("freezing_time() function:")
    debugPrint("Time left in artic: %r" % time_left)
    # Time left conditions
    if time_left == 0:
        game_over("freeze")
    else:
        print("==============================")
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
    elif code == "game over":
        print("Game over value caused an unknown error.")
    else:
        print("Exiting the program.")
        exit(0)
    print("Exiting the program.")
    exit(0)

def surrounding_space(board, playerLocation):
    currentRow = playerLocation[0][0]
    currentColumn = playerLocation[1][0]
    # debug printing
    debugPrint("surrounding_space() function:")
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
    if EPA_AGENT in (sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE):
        game_over("captured")
    else:
        return False

def game_over(reason):
    print("""
==========GAME OVER==========
    """)
    if reason == "win":
        print("Homer made it back to Springfield!")
        print("You won the game! Congratulations!")
    elif reason == "freeze":
        print("The artic cold is too much for Homer.")
        print("He freezes into a delicate ice statue.")
        print("You lose the game.")
    elif reason == "captured":
        print("The EPA agents have caught Homer!")
        print("They take him off to be 'processed'.")
        print("You lose the game.")
    elif reason == "drowned":
        print("Homer cannot swim!")
        print("Bubbles pop on the surface of the water until none remain.")
        print("You lose the game.")
    elif reason == "quit":
        print("You quit the game.")
        print("Homer's fate remains unknown.")
        print("Please play again some day!")
    else:
        error("game over", "game_over()")
    print("""
==========Credits=============
The Simpsons: copyright, Fox
Homer ASCII art: copyright, http://textart4u.blogspot.ca/2012/03/simpsons-text-art-ascii-art.html
Game Design: copyright, James Tam
Game Code and implementation: copyright, Lars Hedlund
==============================
    THANK YOU FOR PLAYING!
==============================
    """)
    exit(0)

def start():
    articTime = 0
    global DEBUG

    # Start in debug mode using command line
    for arg in sys.argv:
        if arg == "DEBUG":
            debugPrint("Starting in DEBUG mode:")
            DEBUG = True
        else:
            DEBUG = False

    # Start game and print starting board
    with open("intro.txt", "r") as intro:
        print(intro.read())
    # initialize various lists
    board = initialize_world()
    playerLocation = find_char(board, HOMER)
    agentLocation = find_char(board, EPA_AGENT)
    freezing_time(articTime)
    printBoard(board)

    # Movement and game over conditions
    game_over = surrounding_space(board, playerLocation)
    while not game_over:
        # Agent and player movement
        currentRow, currentColumn = player_movement(board, playerLocation)
        playerLocation[0][0] = currentRow
        playerLocation[1][0] = currentColumn
        for i in range(AGENTS):
            agent_num = i
            agentRow, agentColumn = agent_movement(board, agentLocation, agent_num)
            agentLocation[0][agent_num] = agentRow
            agentLocation[1][agent_num] = agentColumn
        # Tracking time
        if (currentRow < 6):
            articTime += 1
            freezing_time(articTime)
        elif (currentRow >= 6):
            articTime = 0
        else:
            error("time", "start()")
        # Game over and print board
        game_over = surrounding_space(board, playerLocation)
        printBoard(board)

start()
