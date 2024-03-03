import copy

StartingBoard = [[2,2,1,1,1,2,2],
                 [2,1,1,1,1,1,2],
                 [1,1,1,0,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [2,1,1,1,1,1,2],
                 [2,2,1,1,1,2,2]]

test = [[2,2,0,0,0,2,2],[2,0,0,0,0,0,2],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[2,0,0,0,0,0,2],[2,2,0,0,0,2,2]]

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
    for row in range(len(board)):
        for col in range(0,len(board[row])-2):
            if board[row][col] == 0:
                if board[row][col+1] == 1 and board[row][col+2] == 1:
                    list.append([[row, col+2],[row, col]])

def CheckCenter(board):
    cost = 0
    for i in range(2,5):
        for j in range(2, 5):
            cost = cost + board[i][j]
    return (9 - cost)

def CheckSymmetry(b):
    counter = 0
    state1 = [b[0][2],b[1][1],b[1][2],b[2][0],b[2][1],b[2][2]]
    state2 = [b[0][4],b[1][5],b[1][4],b[2][6],b[2][5],b[2][4]]
    state3 = [b[6][2],b[5][1],b[5][2],b[4][0],b[4][1],b[4][2]]
    state4 = [b[6][4],b[5][5],b[5][4],b[4][6],b[4][5],b[4][4]]
    for i in range(len(state1)):
        if(state1[i] == state2[i]):
               counter = counter + 1
        if(state1[i] == state3[i]):
               counter = counter + 1
        if(state1[i] == state4[i]):
               counter = counter + 1
        if(state2[i] == state3[i]):
               counter = counter + 1
        if(state2[i] == state4[i]):
               counter = counter + 1
        if(state3[i] == state4[i]):
               counter = counter + 1
    return counter
        
def CombinedHeuristic(b):
    h1 = (CheckCenter(b)/9)
    h2 = (CheckSymmetry(b)/36)
    avg = (h1 + h2) *100
    return int(avg)

def IsSame (board1, board2):
    for row in range(len(board1)):
        for col in range(len(board1)):
            if (board1[row][col] != board2[row][col]):
                    return False
    return True

def prioritize(queue, state):
    if (len(queue) != 0):
        for i in range(len(queue)):
            if (state.getF() < queue[i].getF()):
                queue.insert(i, state)
                return queue
    queue.append(state)
    return queue

class State(object):
    def __init__(self, initBoard, initG, initH):
        self.board = initBoard
        self.g = initG
        self.h = initH
        self.f = initH+initG
    def getBoard(self):
        return self.board
    def getG(self):
        return self.g
    def getH(self):
        return self.h
    def getF(self):
        return self.f

def AStar(root):
    PQ = []
    abc = 0
    TraveledBoards = []
    PQ.append(State(root, 0, CheckCenter(root)))
    TraveledBoards.append(root)
    while (len(PQ) > 0 and checkWin(PQ[0].getBoard())!=True) :
        movesList = []
        Up(PQ[0].getBoard(), movesList)
        Down(PQ[0].getBoard(), movesList)
        Left(PQ[0].getBoard(), movesList)
        Right(PQ[0].getBoard(), movesList)
        current = PQ.pop(0)
        abc+=1
        if len(movesList) > 0:
            for i in movesList:
                tempBoard = move(i, current.getBoard())
                check = False
                for x in TraveledBoards:
                    if (IsSame(x, tempBoard)):
                        check = True
                if(check == False):
                    TraveledBoards.append(tempBoard)
                    tempState = State(tempBoard, current.getF(), CheckCenter(current.getBoard()))
                    #tempState = State(tempBoard, current.getF(), CheckSymmetry(current.getBoard()))
                    #tempState = State(tempBoard, current.getF(), CombinedHeuristic(current.getBoard()))
                    PQ = prioritize(PQ, tempState)
    #printBoard(PQ[0].getBoard())
    print(abc)

AStar(DFSboard)
