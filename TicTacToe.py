import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print ('Do you want to be X or O', end = ' ')
        letter = input().upper()
    if letter == 'X':
        return ['X' ,'O']
    else:
        return ['O' , 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
def playAgain():
    print ('Do you want to play again ?(yes/no)')
    return input().lower().startswith('yes')

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Provide a valid move', end=' ')
        move = input()
    #print ('move entered is' + move)
    return int(move)

def isSpaceFree(board,move):
    return board[move] == ' '

def makeMove (board,letter,move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

def isBoardFull(board):
    for i in range (1,10):
        if isSpaceFree(board,i):
            return False
    return True

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def chooseRandomMoveFromList (board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #Check Chance of Computer to Win
    for i in range (1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i
    #Block Chance of Player to Win    
    for i in range (1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    
    #Choose a Corner
    cornerList = [1,3,7,9]
    move = chooseRandomMoveFromList (board, cornerList)
    if move != None:
        return move
    #Choose Centre if available
    if isSpaceFree(board,5):
        return 5
    
    #Choose a side
    sideList = [2,4,6,8]
    move = chooseRandomMoveFromList (board, sideList)
    return move
     
print(' TIC TAC TOE KAHIN BHI HO')
print('   |   |   ')
print(' 7 | 8 | 9 ')
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' 4 | 5 | 6 ')
print('   |   |   ')
print('-----------')
print('   |   |   ')
print(' 1 | 2 | 3 ')
print('   |   |   ')

while True:
    theBoard = [' '] *10
    playerletter, computerletter = inputPlayerLetter()
    #print (playerletter, computerletter)
    turn = whoGoesFirst()
    print ('The' + turn + 'Goes First')
    gameisPlaying = True

    while gameisPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerletter,move)
            #drawBoard(theBoard)

            if isWinner(theBoard, playerletter):
                drawBoard(theBoard)
                print ('You Won')
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    print ('Its a tie')
                    break
                else:
                    turn = 'computer'
                    
        else:
            move = getComputerMove(theBoard, computerletter)
            makeMove(theBoard, computerletter, move)
        
            if isWinner(theBoard, computerletter):
                drawBoard(theBoard)
                print ('You Loose')
                gameisPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print ('Its a tie')
                    break
                else:
                    turn = 'player'
            
    if not playAgain():
        break
