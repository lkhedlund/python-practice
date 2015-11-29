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

# Debug flag
DEBUG_MODE = True

def debugPrint(user_input):
    if DEBUG_MODE == True:
        print("<<< %r >>>" % user_input)
    else:
        print(user_input)

# Author: James Tam
# function: displayWorld
# displayWorld(2Dlist,int,int,int)
# returns(nothing)
# Shows the current state of the world (location of Homer, the EPA agents)
def displayWorld(aMaze, articTime, currentRow):
     print()
     for r in range (0, ROWS, 1):
          for c in range (0, COLUMNS, 1):
               print(aMaze[r][c], end="")
          print()

# Author: James Tam
# function: initializeHC (hard-coded initialization)
# initializeHC(none)
# returns(2DList)

# The legacy method of initializing the game world. It's retained so students can see
# an alternative (non-file IO) method of initialization.
def initializeHC():
    count = 0
    aMaze = []
    agentLocation = []

    # Create the grid. Initialize elements to a space.
    for r in range (0, ROWS, 1):
        aMaze.append ([])
        for c in range (0, COLUMNS, 1):
            aMaze[r].append (" ")

    # Initializes the board from input file
    startPos = open('starting_board.txt', 'r')
    for line in startPos:
        aMaze[count] = line.split(",")
        count += 1

    # Create the grid to store agent's positions.
    # Two rows: row zero for agent row coordinates
    #           row one for agent column coordinates
    # Six columns: one for the six agents.
    for r in range (0, 2, 1):
       agentLocation.append ([])
       for c in range (0, AGENTS, 1):
           agentLocation[r].append (0)

    # The grid stores the (row, column ) coordinates for each agent in the
    # grid called 'aMaze".
    # There are 2 rows and 6 columns in the grid storing the agent
    # coordinates.
    # Row zero stores the row coordinates for the agents.
    # Row one stores the column coordinates for the agents.
    # Column zero stores the (row, column) pair for the first agent.
    # Column one stores the (row, column) pair for the second agent.
    # Column two stores the (row, column) pair for the third agent.
    # Column three stores the (row, column) pair for the fourth agent.
    # Column four stores the (row, column) pair for the fifth agent.
    # Column five stores the (row, column) pair for the six agent.


    # Contents of the List for the agent positions
    #            COLUMN ZERO        COLUMN ONE         COLUMN TWO         COLUMN THREE       COLUMN FOUR        COLUMN FIVE
    #  ROW ZERO  Agent 1 Row coord  Agent 2 Row coord  Agent 3 Row coord  Agent 4 Row coord  Agent 5 Row coord  Agent 6 Row coord
    #  ROW ONE   Agent 1 Col coord  Agwnt 2 Col coord  Agent 3 Col coord  Agent 4 Col coord  Agent 5 Col coord  Agent 6 Col coord

    # Col 0: Agent at position row = 8, column = 9 (position in grid "aMaze")
    agentLocation [0][0] = 8
    agentLocation [1][0] = 9

    # Col 1: Agent at position row = 13, column = 7 (position in grid "aMaze")
    agentLocation [0][1] = 13
    agentLocation [1][1] = 7

    # Col 2: Agent at position row = 13, column = 17 (position in grid "aMaze")
    agentLocation [0][2] = 13
    agentLocation [1][2] = 17

    # Col 3: Agent at position row = 14, column = 28 (position in grid "aMaze")
    agentLocation [0][3] = 14
    agentLocation [1][3] = 28

    # Col 4: Agent at position row = 15, column = 20 (position in grid "aMaze")
    agentLocation [0][4] = 15
    agentLocation [1][4] = 20

    # Col 5: Agent at position row = 16, column = 16 (position in grid "aMaze")
    agentLocation [0][5] = 16
    agentLocation [1][5] = 16

    debugPrint(agentLocation)

    return(aMaze,agentLocation)

def player_movement():
    #(F)unction:
    #(I)nput:
    #(R)eturn: homer_pos, articTime
    compass = """
        8
      4 5 6
        2"""
    print("Movement options: To move Homer, enter a number corresponding to \
a compass direction:")
    print(compass)
    print("Enter 5 to not move. Enter 0 to quit.")

    movement = input("Which direction would you like to move in: ")
    while movement not in "854620":
        print("Homer doesn't know how to move that way.")
        print(compass)
        movement = input("Please enter a new direction, or 0 to quit: ")

def agent_movement(aMaze, agentLocation):
    debugPrint(len(agentLocation))
    for r in range(len(agentLocation)):
        agent = agentLocaiton[r]



def create_building():
    pass

def create_water():
    pass

def turns_left():
    pass

def start():
    aMaze = []
    agentLocation = []
    articTime = 0
    currentRow = START_ROW
    currentColumn = START_COLUMN
    newRow = START_ROW
    newColumn = START_COLUMN
    direction = 0

    aMaze,agentLocation = initializeHC()
    agent_movement(aMaze, agentLocation)
    displayWorld(aMaze,articTime,currentRow)

start()
