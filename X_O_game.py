# X-O oyunu


import random

def dravBoard(board):
    print(board[7]+ '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def imputPleyerLetter():

    leter = ''

    while not (leter == 'X' or leter == 'O'):
        print('Siz "X" yoxsa "0" secirsiniz?')
        leter = input("Seciminiz? ").upper()

        if leter == 'X':
            return ['X', 'O']

        else:
            return ['O','X']

def whoGoesrFirts():

    if random.randint(0, 1) == 0:
        return 'Kampuyuter'
    else:
        return 'Insan'

def makeMove(board,letter,move):
    board[move] = letter


def isWinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or

            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or

            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    boardCopy = []

    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    return board[move] == ' '


def getPlayerMove(board):

    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Sizin novbeti gediwiniz(1-9)')
        move = input("Gediw edin: ")
    return int(move)


def chooseRandomMoveFromList(board,moveList):
    possibleMoves = []

    for i in moveList:
        if isSpaceFree(board , i):
            possibleMoves.append(i)
        if len(possibleMoves) !=0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playLetter = 'O'
    else:
        playLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)

        if isSpaceFree(boardCopy,i):
            makeMove(boardCopy, computerLetter,i)
            if isWinner(boardCopy,computerLetter):
                return  i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)

        if isSpaceFree(boardCopy,i):
            makeMove(boardCopy,playLetter,i)
            if isWinner(boardCopy,playLetter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,7,9])

    if move != None:
        return move

    if isSpaceFree(board , 5):
        return 5

    return chooseRandomMoveFromList(board,[2,4,6,8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('X-0 oyunu')

while True:
    theBoard = [' '] * 10
    playLetter,computerLetter = imputPleyerLetter()

    turn = whoGoesrFirts()
    print(''+ turn + ' birinci xod edir')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Insan':
            dravBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playLetter,move)

            if isWinner(theBoard,playLetter):
                dravBoard(theBoard)
                print('Siz qalibsiniz')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    dravBoard(theBoard)
                    print("Hec hece")
                    break
                else:
                    turn = 'Camputer'

        else:
            # camputer
            move = getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter,move)

            if isWinner(theBoard,computerLetter):
                dravBoard(theBoard)
                print("Camputer qalib geldi Siz uduzdunuz!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    dravBoard(theBoard)
                    print('Hec Hece')
                    break
                else:
                    turn = 'Insan'

    print("yeniden oynayaqmi? (he yoxsa yox)")

    if not input().lower().startswith('h'):
        break


