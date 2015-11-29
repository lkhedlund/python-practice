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
