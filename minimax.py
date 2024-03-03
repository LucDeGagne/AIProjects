import random
import copy
#Team blue is positive and team red is negative
StartingBoard = [[0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0]]

test = [[1,1,-1,1,1,-1],
        [-1,-1,1,1,1,-1],
        [-1,-1,1,-1,-1,1],
        [1,-1,-1,1,-1,-1],
        [-1,1,1,1,-1,-1],
        [-1,1,1,-1,1,1]]

def generateBoard():
    temp = []
    for i in range(18):
        temp.append(1)
        temp.append(-1)
    for row in range(len(StartingBoard)):
        for col in range(len(StartingBoard[row])):
            value = temp.pop(random.randrange(0, len(temp)))
            StartingBoard[row][col] = value

def printBoard(b):
    for row in range(len(b)):
        string = "["
        for col in range(len(b[row])):
            if b[row][col] < 0:
                string = string + " R"
            elif b[row][col] > 0:
                string = string + " B"
            else:
                string = string + " _"
        string = string + " ]"
        print(string)
    print(" ")

def checkWinRed(b):
    for row in range(len(b)):
        for col in range(len(b[row])):
            if b[col][row] == 1:
                return False
    print("Red wins")
    return True

def checkWinBlue(b):
    for row in range(len(b)):
        for col in range(len(b[row])):
            if b[col][row] == -1:
                return False
    print ("Blue wins")
    return True

def Up(b, opponent, l):
    for col in range(len(b[0])):
        X = []
        Y = []
        for i in range(len(b)):
            if b[i][col] == opponent or b[i][col] == 0:
                X.append(i)
            else:
                Y.append(i)
                break
        for j in range(i+1, len(b)):
            if b[j][col] != opponent and b[j][col] != 0:
                Y.append(j)
        if len(Y) > 0:
            for k in range(len(X)):
                for h in range(len(Y)):
                    temp = []
                    temp.append(Y[h])
                    temp.append(col)
                    temp.append('U')
                    temp.append(k+1)
                    l.append(temp)
    return l


def Down(b, opponent, l):
    for col in range(len(b[0])-1, 0, -1):
        X = []
        Y = []
        for i in range(len(b)-1, 0, -1):
            if b[i][col] == opponent or b[i][col] == 0:
                X.append(i)
            else:
                Y.append(i)
                
                break
        for j in range(i-1, 0, -1):
            if b[j][col] != opponent and b[j][col] != 0:
                Y.append(j)
        if len(Y) > 0:
            for k in range(len(X)):
                for h in range(len(Y)):
                    temp = []
                    temp.append(Y[h])
                    temp.append(col)
                    temp.append('D')
                    temp.append(k+1)
                    l.append(temp)
    return l

def Left(b, opponent, l):
    for row in range(len(b)):
        X = []
        Y = []
        for i in range(len(b[row])):
            if b[row][i] == opponent or b[row][i] == 0:
                X.append(i)
            else:
                Y.append(i)
                break
        for j in range(i+1, len(b[row])):
            if b[row][j] != opponent and b[row][j] != 0:
                Y.append(j)
        if len(Y) > 0:
            for k in range(len(X)):
                for h in range(len(Y)):
                    temp = []
                    temp.append(row)
                    temp.append(Y[h])
                    temp.append('L')
                    temp.append(k+1)
                    l.append(temp)
    return l

def Right(b, opponent, l):
    for row in range(len(b)-1, 0, -1):
        X = []
        Y = []
        for i in range(len(b[0])-1, 0, -1):
            if b[row][i] == opponent or b[row][i] == 0:
                X.append(i)
            else:
                Y.append(i)
                break
        for j in range(i-1, 0, -1):
            if b[row][j] != opponent and b[row][j] != 0:
                Y.append(j)
        if len(Y) > 0:
            for k in range(len(X)):
                for h in range(len(Y)):
                    temp = []
                    temp.append(row)
                    temp.append(Y[h])
                    temp.append('R')
                    temp.append(k+1)
                    l.append(temp)
    return l

def Empty(b, opponent, l):
    for row in range(0, len(b)):
        for col in range(0, len(b[row])):
            if col > 0:
                if b[row][col] == (-1 * opponent) and b[row][col-1] == 0:
                    temp = [row, col, 'L', 1]
                    l.append(temp)
            if col < 5:
                if b[row][col] == (-1 * opponent) and b[row][col+1] == 0:
                    temp = [row, col, 'R', 1]
                    l.append(temp)
            if row > 0:
                if b[row][col] == (-1 * opponent) and b[row-1][col] == 0:
                    temp = [row, col, 'U', 1]
                    l.append(temp)
            if row < 5:
                if b[row][col] == (-1 * opponent) and b[row+1][col] == 0:
                    temp = [row, col, 'D', 1]
                    l.append(temp)
    return l

class State(object):
    def __init__(self, initBoard, initValue, initAlpha, initBeta, initMax, initMove):
        self.board = initBoard
        self.value = initValue
        self.alpha = initAlpha
        self.beta = initBeta
        self.Max = initMax
        self.move = initMove

def heur1(b):
    total = 0
    for i in range(len(b)):
        for j in range(len(b[i])):
            total = total + b[i][j]
    return total

def heur2(b, opponent):
    total = 0
    for row in range(0, len(b)):
        for col in range(0, len(b[row])):
            if col > 0:
                if b[row][col] == opponent and b[row][col-1] == opponent:
                    total = total + 1
            if col < 5:
                if b[row][col] == opponent and b[row][col+1] == opponent:
                    total = total + 1
            if row > 0:
                if b[row][col] == opponent and b[row-1][col] == opponent:
                    total = total + 1
            if row < 5:
                if b[row][col] == opponent and b[row+1][col] == opponent:
                    total = total + 1
    return total//2

def minimax1(b, player):
    ab = 0
    root = State(b, -100, -100, 100, True, [])
    Min = []
    Min = Up(root.board, (-1*player), Min)
    Min = Down(root.board, (-1*player), Min)
    Min = Left(root.board, (-1*player), Min)
    Min = Right(root.board, (-1*player), Min)
    result = []
    for i in range(len(Min)):
        depth2 = State(push(root.board, Min[i][0], Min[i][1], Min[i][2], Min[i][3]), 100, -100, 100, False, Min[i])
        if checkWinBlue(depth2.board) == True:
            return depth2.move
        if root.alpha > depth2.alpha:
            depth2.alpha = root.alpha
        H = []
        H = Up(depth2.board, player, H)
        H = Down(depth2.board, player, H)
        H = Left(depth2.board, player, H)
        H = Right(depth2.board, player, H)
        ab = ab + 1
        for j in range(len(H)):
            leaf = (-1*heur1(push(depth2.board, H[j][0], H[j][1], H[j][2], H[j][3])))
            if leaf < root.alpha:
                break
            if leaf < depth2.beta:
                depth2.value = leaf
            ab = ab + 1
        if depth2.value > root.alpha:
            root.alpha = depth2.value
            result = depth2.move
    if len(result) < 1:
        result = Empty(root.board, (-1 * player), [])
        result = result[random.randrange(len(result))]
    print("The number of nodes searched is: " + str(ab))
    return result

def minimax2(b, player):
    ab = 0
    root = State(b, -100, -100, 100, True, [])
    Min = []
    Min = Up(root.board, (-1*player), Min)
    Min = Down(root.board, (-1*player), Min)
    Min = Left(root.board, (-1*player), Min)
    Min = Right(root.board, (-1*player), Min)
    result = []
    for i in range(len(Min)):
        depth2 = State(push(root.board, Min[i][0], Min[i][1], Min[i][2], Min[i][3]), 100, -100, 100, False, Min[i])
        if checkWinBlue(depth2.board) == True:
            return depth2.move
        if root.alpha > depth2.alpha:
            depth2.alpha = root.alpha
        H = []
        H = Up(depth2.board, player, H)
        H = Down(depth2.board, player, H)
        H = Left(depth2.board, player, H)
        H = Right(depth2.board, player, H)
        ab = ab + 1
        for j in range(len(H)):
            leaf = (-1*heur2(push(depth2.board, H[j][0], H[j][1], H[j][2], H[j][3]), (-1*player)))
            if leaf < root.alpha:
                break
            if leaf < depth2.beta:
                depth2.value = leaf
            ab = ab + 1
        if depth2.value > root.alpha:
            root.alpha = depth2.value
            result = depth2.move
    if len(result) < 1:
        result = Empty(root.board, (-1 * player), [])
        if len(result) > 0:
            result = result[random.randrange(len(result))]
    print("The number of nodes searched is: " + str(ab))
    return result

def randomMove(b, player):
    choice = []
    choice = Up(b, (-1*player), choice)
    choice = Down(b, (-1*player), choice)
    choice = Left(b, (-1*player), choice)
    choice = Right(b, (-1*player), choice)
    choice = Empty(b, (-1 * player), choice)
    if len(choice) > 0:
        return choice[random.randrange(0, len(choice))]
    else:
        return []

def playerMove():
    location = input("Please choose a move by identifying a row and column for the square you would like to move,separated by a space:\n")
    location = location.strip()
    row = int(location[0])
    col = int(location[2])
    direction = input("Please input direction ie Up, Down, Left or Right:\n")
    direction = direction.strip()
    direction = direction[0].upper()
    amount = input("Please insert by how many squares you'd like to move:\n")
    amount = int(amount.strip())
    return [row, col, direction, amount]

def push(oldBoard, row, col, direction, start):
    b = copy.deepcopy(oldBoard)
    zero = 0
    if direction == 'U':
        if start == 5:
            b[0][col] = b[row][col]
            for i in range(1, len(b)):
                b[i][col] = 0
        else:
            for i in range(row, row-start-1, -1):
                if b[i][col] == 0:
                    for j in range(i, row):
                        b[j][col] = b[j+1][col]
                    b[row][col] = 0
                    zero = zero + 1
            start = start - zero
            row = row - zero
            while start > 0:
                for i in range(row-start-1, row, 1):
                    b[i][col] = b[i+1][col]
                b[row][col] = 0
                start = start - 1
                row = row - 1
    if direction == 'D':
        if start == 5:
            b[5][col] = b[row][col]
            for i in range(0, len(b)-1):
                b[i][col] = 0
        else:
            for i in range(row, row+start+1):
                if b[i][col] == 0:
                    for j in range(i, row, -1):
                        b[j][col] = b[j-1][col]
                    b[row][col] = 0
                    zero = zero + 1
            start = start - zero
            row = row + zero
            while start > 0:
                for i in range(row+start, row, -1):
                    b[i][col] = b[i-1][col]
                b[row][col] = 0
                start = start - 1
                row = row + 1
    if direction == 'L':
        if start == 5:
            b[row][0] = b[row][col]
            for i in range(1, len(b[row])):
                b[row][i] = 0
        else:
            for i in range(col, col-start-1, -1):
                if b[row][i] == 0:
                    for j in range(i, col):
                        b[row][j] = b[row][j+1]
                    b[row][col] = 0
                    zero = zero + 1
            start = start - zero
            col = col - zero
            while start > 0:
                for i in range(col-start-1, col, 1):
                    b[row][i] = b[row][i+1]
                b[row][col] = 0
                start = start - 1
                col = col - 1
    if direction == 'R':
        if start == 5:
            b[row][5] = b[row][0]
            for i in range(0, len(b)-1):
                b[row][i] = 0
        else:
            for i in range(col, col+start+1):
                if b[row][i] == 0:
                    for j in range(i, col, -1):
                        b[row][j] = b[row][j-1]
                    b[row][col] = 0
                    zero = zero + 1
            start = start - zero
            col = col + zero
            while start > 0:
                for i in range(col+start, col, -1):
                    b[row][i] = b[row][i-1]
                b[row][col] = 0
                start = start - 1
                col = col + 1
    return b

generateBoard()
#Blue starts
#printBoard(test)
#m = Up(test, 1, [])
printBoard(StartingBoard)
m = minimax1(StartingBoard, 1)
newBoard = push(StartingBoard, m[0], m[1], m[2], m[3])
print("Blue player moves space at row "+str(m[0])+" and col "+str(m[1])+" "+str(m[2])+" by "+str(m[3])+" squares.")
printBoard(newBoard)

while True:
    m = playerMove()
    #m = minimax2(newBoard, -1)
    if len(m) > 0:
        newBoard = push(newBoard, m[0], m[1], m[2], m[3])
        print("Red player moves space at row "+str(m[0])+" and col "+str(m[1])+" "+str(m[2])+" by "+str(m[3])+" squares.")
        printBoard(newBoard)
        if checkWinRed(newBoard) == True or checkWinBlue(newBoard) == True:
            break
    m = minimax1(newBoard, 1)
    if len(m) > 0:
        newBoard = push(newBoard, m[0], m[1], m[2], m[3])
        print("Blue player moves space at row "+str(m[0])+" and col "+str(m[1])+" "+str(m[2])+" by "+str(m[3])+" squares.")
        printBoard(newBoard)
        if checkWinBlue(newBoard) == True or checkWinRed(newBoard) == True:
            break