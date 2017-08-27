def createBoard():
    board = []
    for x in range(3):
        board.append([" ", " ", " "])
    return board

def checkWinner(board):
    for x in range(3):
        if (board[x][0] != " " and board[x][0] == board[x][1] and board[x][0] == board[x][2]):
            return True
        elif (board[0][x] != " " and board[0][x] == board[1][x] and board[0][x] == board[2][x]):
            return True
    if (board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return True
    elif (board[0][2] != " " and board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        return True
    return False

def printWin(player):
    print("Congratulations, player", player, "has won!")

def getWinner(board):
    for x in range(3):
        if (board[x][0] != " " and board[x][0] == board[x][1] and board[x][0] == board[x][2]):
            player = board[x][0]
            printWin(player)
        elif (board[0][x] != " " and board[0][x] == board[1][x] and board[0][x] == board[2][x]):
            player = board[0][x]
            printWin(player)
    if (board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        player = board[0][0]
        printWin(player)
    elif (board[0][2] != " " and board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        player = board[0][2]
        printWin(player)
        
def displayBoard(board):
    
    for x in range(3):
        print (board[x])

def getRow():
    row = input("Please enter row: ")
    while (int(row) not in range (3)):
        row = input("Error, not in range. Please enter row: ")
    return int(row)

def getColumn():
    column = input("Please enter column: ")
    while (int(column) not in range(3)):
        column = input("Error, not in range. Please enter column: ")
    return int(column)

def makeMove(board, player):
    row = getRow()
    column = getColumn()
    while (board[row][column] != " "):
        print("Sorry this space is taken, please try another spot")
        row = getRow()
        column = getColumn()
    board[row][column] = player
    return board

def initiateStart():
    userInput = input("Please enter which player to start X or O: ")
    while(userInput != 'X' and userInput != 'O'):
       userInput = input("Invalid input. Please enter which player to start X or O: ")
    if (userInput == 'X'):
        return True
    else:
        return False

def playGame():
    board = createBoard()
    player1 = "X"
    player2 = "O"
    starting = initiateStart()
    count = 0
    if (not starting):
        player1 = "O"
        player2 = "X"
    while(not checkWinner(board) and count < 9):
        if(count % 2 == 0):
            print("It is your turn player", player1, ",please make a move.")
            makeMove(board, player1)
            displayBoard(board)
        else:
            print("It is your turn player", player2, ",please make a move.")
            makeMove(board, player2)
            displayBoard(board)
        count+= 1
    if (checkWinner(board)):
        getWinner(board)
    else:
        print("The game ended in a tie.")

playGame()
