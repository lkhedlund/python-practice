# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

"""
HEADER: Simpsons Game
AUTHOR: Lars Hedlund

MAIN FEATURES:
(1) Debug modes written and set; (2) initialize
world pulls from file to load locations; (3) Player movement working;
(4) Agent movement working (5) Game states (i.e. win, lose, freeze, caught);
(6) Error messages set; (7) Tracks time in Alaska (resets when necessary);
(8) Find the player and non-player locations when pulled from a file.
FEATURES NOT IMPLEMENTED:
does not track whether or not the player is
at the edge of the map; does not determine if a ValueError occurs in
user's input; ROWS, COLUMNS, and AGENTS cannot be changed, or
initialize_world() will be unable to read the file.

BUGS: None known
VERSION: 0.7

ABOUT:
This is a small game where the player controls Homer (H) and
tries to guide him to Springfield (S) before he either freezes, drowns,
or is caught by the EPA Agents (E). If the player makes it to Springfield,
he or she wins the game. If any of the other conditions are true (freezes,
etc), he or she loses the game.
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
    # FUNCTION: Prints debugging values to help with logic errors
    # INPUT: string
    # RETURN: none
    if DEBUG == True:
        print("<<<", user_input, ">>>")

def printBoard(board):
    # FUNCTION: Prints the game board to the console
    # INPUT: list
    # RETURN: none
    print("==========GAME BOARD==========")
    for r in range (0, ROWS, 1):
        for c in range (0, COLUMNS, 1):
            print(board[r][c], end="")
        print()

def initialize_world():
    # FUNCTION: Creates the game world
    # INPUT: none
    # RETURN: list

    # Starting variables
    board = []
    count = 0 # sets the row for each pass when inializing board
    # Create the grid. Initialize elements to a space.
    for r in range(ROWS):
        board.append([])
        for c in range(COLUMNS):
            board[r].append(str())

    # Initializes the board from input file
    if DEBUG == True: # quick way to load test files for debugging
        file = input("Which file would you like to load for testing: ") # file must end with .txt, no error checking
        with open(file, 'r') as start:
            # loops through the file and converts each line into characters
            for line in start:
                new_line = line.rstrip("\n")
                # adds each character to the row
                board[count] = list(new_line)
                count += 1
    else:
        # standard board if DEBUG mode isn't activated
        with open('data.txt', 'r') as start:
            for line in start:
                new_line = line.rstrip("\n")
                board[count] = list(new_line)
                count += 1

    return board

def find_char(board, char):
    # FUNCTION: Finds a string in a list of lists (matrix)
    # INPUT: list, string
    # RETURN: list
    # initial variables
    location = []
    # create two rows, first row holds character row coordinates
    # second row holds character column coordinates
    for i in range(2):
        location.append([])
    # moves through each row and column looking for a character
    for r, columns in enumerate(board):
        for c, square in enumerate(columns):
            # if it finds the character, it adds it to the location list
            if (square == char):
                debugPrint("find_char() function:")
                debugPrint("Finding %r" % char)
                debugPrint("Location (r/c): (%r/%r)" % (r,c))
                # first row for row coordinates
                location[0].append(r)
                # second row for column coordinates
                location[1].append(c)
                debugPrint("%r" % location)
            else:
                pass
    return location

def player_movement(board, homerLocation):
    # FUNCTION: Move the player's character
    # INPUT: list, list
    # RETURN: int, int
    # Starting variables
    currentRow = homerLocation[0][0]
    currentColumn = homerLocation[1][0]
    board[currentRow][currentColumn] = EMPTY
    # produces a number between 0-100 to determine if player is distracted
    distraction_prob = randint(0,100)
    distracted = False # distracted flag
    valid_input = False # valid input (i.e. less than 9)
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
        # Toggle debug mode
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
    # Debug print
    debugPrint("Homer's new (r/c): (%r/%r)" % (newRow, newColumn))
    debugPrint("Square type: %r" % board[newRow][newColumn])
    debugPrint("Distraction number generated: %r" % distraction_prob)
    # Checks for game over conditions and returns values or exits
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
    # FUNCTION: Move the non-player characters
    # INPUT: list, list, int
    # RETURN: int, int
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
        # agent movement is based on a randomely generated number
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
        # Checks for movement conditions and return values
        if (board[newRow][newColumn] in (WATER,BUILDING,SPRINGFIELD,EPA_AGENT)):
            can_move = False # agent cannot move onto the above spaces
        else:
            can_move = True
            board[currentRow][currentColumn] = EMPTY
            board[newRow][newColumn] = EPA_AGENT
            return newRow, newColumn

def freezing_time(articTime):
    # FUNCTION: Displays time spent in the artic
    # INPUT: int
    # RETURN: none
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
    # FUNCTION: Displays program breaking error codes
    # INPUT: string, string
    # RETURN: None
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
    # FUNCTION: Determines which spaces surround the player
    # INPUT: list, list
    # RETURN: boolean
    # intialize variables
    currentRow = playerLocation[0][0]
    currentColumn = playerLocation[1][0]
    # debug printing
    debugPrint("surrounding_space() function:")
    debugPrint("Homer's (r/c): (%r/%r)" % (currentRow, currentColumn))

    # determines what occupies each square around the player
    sqrN = board[currentRow - 1][currentColumn]
    sqrNE = board[currentRow - 1][currentColumn + 1]
    sqrNW = board[currentRow - 1][currentColumn - 1]
    sqrS = board[currentRow + 1][currentColumn]
    sqrSE = board[currentRow + 1][currentColumn + 1]
    sqrSW = board[currentRow + 1][currentColumn - 1]
    sqrW = board[currentRow][currentColumn - 1]
    sqrE = board[currentRow][currentColumn + 1]
    # Return surrounding squares if in DEBUG mode
    debugPrint("""
    Surrounding space:
         %r %r %r
         %r     %r
         %r %r %r
    """ % (sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE))
    # Ends the game if an agent is in a square near the player
    if EPA_AGENT in (sqrNW, sqrN, sqrNE, sqrW, sqrE, sqrSW, sqrS, sqrSE):
        game_over("captured")
    else:
        return False # returns false to keep movement loop in start() going

def game_over(reason):
    # FUNCTION: Prints out game over conditions and exits
    # INPUT: string
    # RETURN: None
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

def intro():
    # FUNCTION: Prints out the introduction
    # INPUT: None
    # RETURN: None
    print("""
                      ,;-.
                    ,((--\).
                   /        \\
                  |          |
                  |          |
                 (,'"`.  ,'"`.)
                 :     \/     ;
                 `.o  ,'`.  o,'
                 (|`>'`--'`<'|)            ,-,
     ,.           |/        \|         ,-./ /
   _ | \,-.       (          )        | `-'`--.
  ( `' (_/|__      \   (o   /       ,-'     ,-'
   ;         )    ,|`.  - ,'|.      `-.   ) \\
   | (    ,-'   _/ `-.`""',-' \---.   /      ;
   |     |   ,-'  \  /\  / \  |   |--/       |
   |     |_,|    / \/  \/   \/\   |          |
   |     `  \   |              \  /        ,'
   |         \  |              | /      _,'
   :          \ ,              `/------'
    `-.___,---')                `.
             ,'                   \\
=================================================
              The Simpson’s Game!
=================================================
Homer is trapped in Alaska and needs to make it
back to Springfield. There’s only one problem:
the EPA Agents are after him!

Help Homer (H) get back to Springfield (S) before
the EPA Agents (E) catch him! But don’t take too
long, or Homer will freeze in the arctic (the top
6 rows of the map)!

Homer is also prone to silly mistakes: if you
enter the water (~), you’ll freeze. Homer
might not always listen to your commands either,
so be strategic!
=================================================
    """)

def start():
    # FUNCTION: Main function
    # INPUT: None
    # RETURN: None
    # initializes variables
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
    intro()
    # initialize various lists
    board = initialize_world() # creates game board
    playerLocation = find_char(board, HOMER) # determines player's location
    agentLocation = find_char(board, EPA_AGENT) # determines non-player locations
    freezing_time(articTime) # displays time left
    printBoard(board) # prints first board

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
