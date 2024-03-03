import copy

StartingBoard = [[2,2,1,1,1,2,2],[2,1,1,1,1,1,2],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[2,1,1,1,1,1,2],[2,2,1,1,1,2,2]]

test = [[2,2,0,0,0,2,2],
        [2,0,0,0,0,0,2],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,1,0,0,0,0],
        [2,0,0,0,0,0,2],
        [2,2,0,0,0,2,2]]

DFSboard = [[2,2,0,0,0,2,2],
            [2,0,0,0,0,1,2],
            [1,1,0,0,1,0,0],
            [1,1,1,0,1,0,0],
            [1,0,0,1,1,0,0],
            [2,0,0,0,1,1,2],
            [2,2,0,0,1,2,2]]

def printBoard(board):
    for value in board:
        print(value)
        
def checkWin(board):
    counter=0
    for row in board:
        for value in row:
            if value < 2:
                counter = counter+value
    if counter == 1:
        print("Win.")
        return True
    else:
        #print (str(counter) + " pegs remaining")
        return False

def move(list, board):
    newBoard = copy.deepcopy(board)
    newBoard[list[0][0]][list[0][1]]=0
    newBoard[list[1][0]][list[1][1]]=1
    avgX = (list[0][0]+list[1][0])//2
    avgY = (list[0][1]+list[1][1])//2
    newBoard[avgX][avgY]=0
    return newBoard

def Up(board, list):
    for row in range(2, len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                if board[row-1][col] == 1 and board[row-2][col] == 1:
                    list.append([[row-2, col],[row, col]])

def Down(board, list):
    for row in range(0,len(board)-2):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                if board[row+1][col] == 1 and board[row+2][col] == 1:
                    list.append([[row+2, col],[row, col]])

def Left(board, list):
    for row in range(len(StartingBoard)):
        for col in range(2,len(board[row])):
            if board[row][col] == 0:
                if board[row][col-1] == 1 and board[row][col-2] == 1:
                    list.append([[row, col-2],[row, col]])

def Right(board, list):
    for row in range(len(StartingBoard)):
        for col in range(0,len(board[row])-2):
            if board[row][col] == 0:
                if board[row][col+1] == 1 and board[row][col+2] == 1:
                    list.append([[row, col+2],[row, col]])


def DFS(stack):
    while (len(stack) > 0 and checkWin(stack[len(stack)-1])!=True) :
        play = stack.pop()
        movesList = []
        #printBoard(play)
        Up(play, movesList)
        Down(play, movesList)
        Left(play, movesList)
        Right(play, movesList)
        if len(movesList) > 0:
            for i in movesList:
                temp = move(i, play)
                stack.append(temp)
    printBoard(stack[len(stack)-1])
    
                    
queue = [StartingBoard]
stack = [DFSboard]
dvs = [test]
DFS(stack)