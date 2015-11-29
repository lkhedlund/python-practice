board = []

# initialize board
for r in range(3):
    board.append([])
    for c in range(3):
        board[r].append(str())

print("%r" % board)

# fill board
board[0] = ["E", "H", " "]
board[1] = [" ", "E", "E"]
board[2] = ["E", " ", " "]

print("%r" % board)

def load_locations(board):
    # initialize agent
    for r in range (2):
       location.append ([])
       for c in range (6):
           location[r].append (0)
    # Find starting locations of PCs and NPCs
    currentRow, currentColumn = find_char(board, HOMER)
    for i in range(AGENTS):
        agent_num = i
        agentRow, agentColumn = find_char(board, agentLocation, agent_num)
        agentLocation[0][agent_num] = agentRow
        agentLocation[1][agent_num] = agentColumn


def find_char(board, char):
    # initial variable
    location = []
    for i in range(2):
        location.append([])
    for r, columns in enumerate(board):
        for c, square in enumerate(columns):
            if (square == char):
                print(r, c)
                location[0].append(r)
                location[1].append(c)
                print("%r" % location)
            else:
                pass
    return location
find_char(board, "E")
find_char(board, "H")
