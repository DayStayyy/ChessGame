from json import dumps, loads
import copy
from re import S

class Chess :
    def __init__(self,player1,player2) :
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
        self.playerPieceList = [['r','n','b','q','k','p'],['R','N','B','Q','K','P']]
        
    def newGame(self) :
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.board[0][0] = 'r'
        self.board[0][1] = 'n'
        self.board[0][2] = 'b'
        self.board[0][3] = 'q'
        self.board[0][4] = 'k'
        self.board[0][5] = 'b'
        self.board[0][6] = 'n'
        self.board[0][7] = 'r'
        self.board[1][0] = 'p'
        self.board[1][1] = 'p'
        self.board[1][2] = 'p'
        self.board[1][3] = 'p'
        self.board[1][4] = 'p'
        self.board[1][5] = 'p'
        self.board[1][6] = 'p'
        self.board[1][7] = 'p'
        self.board[6][0] = 'P'
        self.board[6][1] = 'P'
        self.board[6][2] = 'P'
        self.board[6][3] = 'P'
        self.board[6][4] = 'P'
        self.board[6][5] = 'P'
        self.board[6][6] = 'P'
        self.board[6][7] = 'P'
        self.board[7][0] = 'R'
        self.board[7][1] = 'N'
        self.board[7][2] = 'B'
        self.board[7][3] = 'Q'
        self.board[7][4] = 'K'
        self.board[7][5] = 'B'
        self.board[7][6] = 'N'
        self.board[7][7] = 'R'
        self.turn = 1
        return  self.boardToJson()



    def isValidMove(self,positionStart,positionEnd) :
        print(self.board[positionStart[0]][positionStart[1]])
        print(self.playerPieceList[self.turn%2])
        if self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][5] :
            if positionEnd[0] == positionStart[0] + (2 if self.turn%2 == 0  else -2) and positionEnd[1] == positionStart[1] and self.board[positionEnd[0]][positionEnd[1]] == ' ' and self.board[positionStart[0] + (1 if self.turn%2 == 0  else -1)][positionStart[1]] == ' ' and positionStart[0] == (1 if self.turn%2 == 0  else 6) :
                return True
            elif positionEnd[0] == positionStart[0] + (1 if self.turn%2 == 0  else -1) and positionEnd[1] == positionStart[1] and self.board[positionEnd[0]][positionEnd[1]] == ' ':
                return True
            elif positionEnd[0] == positionStart[0] + (1 if self.turn%2 == 0  else -1) and (positionEnd[1] == positionStart[1] + 1 or positionEnd[1] == positionStart[1] - 1) and self.board[positionEnd[0]][positionEnd[1]] != ' ' and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                return True
            return False            
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][0] :
            if positionStart[0] == positionEnd[0] and positionStart[1] != positionEnd[1] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                testEnd = positionEnd[1]
                testStart = positionStart[1]
                testEnd += (1 if testEnd < testStart else -1) 
                while testEnd != testStart :
                    if self.board[positionEnd[0]][testEnd] != ' ' :
                        return False
                    testEnd += (1 if testEnd < testStart else -1) 
                return True 
            elif positionStart[1] == positionEnd[1] and positionStart[0] != positionEnd[0] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                testEnd = positionEnd[0]
                testStart = positionStart[0]
                testEnd += (1 if testEnd < testStart else -1)
                while testEnd != testStart :
                    if self.board[testEnd][positionEnd[1]] != ' ' :
                        return False
                    testEnd += (1 if testEnd < testStart else -1)
                return True
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][1] :
            if self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                if positionStart[0] + 1 == positionEnd[0] and positionStart[1] + 2 == positionEnd[1]:
                    return True
                elif positionStart[0] - 1 == positionEnd[0] and positionStart[1] + 2 == positionEnd[1]:
                    return True
                elif positionStart[0] + 1 == positionEnd[0] and positionStart[1] - 2 == positionEnd[1]:
                    return True
                elif positionStart[0] - 1 == positionEnd[0] and positionStart[1] - 2 == positionEnd[1]:
                    return True
                elif positionStart[0] + 2 == positionEnd[0] and positionStart[1] + 1 == positionEnd[1]:
                    return True
                elif positionStart[0] - 2 == positionEnd[0] and positionStart[1] + 1 == positionEnd[1]:
                    return True
                elif positionStart[0] + 2 == positionEnd[0] and positionStart[1] - 1 == positionEnd[1]:
                    return True
                elif positionStart[0] - 2 == positionEnd[0] and positionStart[1] - 1 == positionEnd[1]:
                    return True
            return False
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][2] :
            if positionStart[1] != positionEnd[1] and positionStart[0] != positionEnd[0] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2] and ((positionStart[0] - positionEnd[0]) if (positionStart[0] - positionEnd[0]) > 0 else (positionStart[0] - positionEnd[0])*-1)  == ((positionStart[1] - positionEnd[1]) if (positionStart[1] - positionEnd[1]) > 0 else (positionStart[1] - positionEnd[1])*-1)  :
                testEnd0 = positionEnd[0]
                testEnd1 = positionEnd[1]
                testEnd0 += (1 if testEnd0 < positionStart[0] else -1)
                testEnd1 += (1 if testEnd1 < positionStart[1] else -1)
                while positionStart[0] != testEnd0 and positionStart[1] != testEnd1  :
                    if self.board[testEnd0][testEnd1] != ' ' :
                        print(self.board[testEnd0][testEnd1])
                        return False
                    testEnd0 += (1 if testEnd0 < positionStart[0] else -1)
                    testEnd1 += (1 if testEnd1 < positionStart[1] else -1)
                return True
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][3] :
            if positionStart[0] == positionEnd[0] and positionStart[1] != positionEnd[1] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                testEnd = positionEnd[1]
                testStart = positionStart[1]
                testEnd += (1 if testEnd < testStart else -1) 
                while testEnd != testStart :
                    if self.board[positionEnd[0]][testEnd] != ' ' :
                        return False
                    testEnd += (1 if testEnd < testStart else -1) 
                return True 
            elif positionStart[1] == positionEnd[1] and positionStart[0] != positionEnd[0] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                testEnd = positionEnd[0]
                testStart = positionStart[0]
                testEnd += (1 if testEnd < testStart else -1)
                while testEnd != testStart :
                    if self.board[testEnd][positionEnd[1]] != ' ' :
                        return False
                    testEnd += (1 if testEnd < testStart else -1)
                return True
            elif positionStart[1] != positionEnd[1] and positionStart[0] != positionEnd[0] and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2] and ((positionStart[0] - positionEnd[0]) if (positionStart[0] - positionEnd[0]) > 0 else (positionStart[0] - positionEnd[0])*-1)  == ((positionStart[1] - positionEnd[1]) if (positionStart[1] - positionEnd[1]) > 0 else (positionStart[1] - positionEnd[1])*-1)  :
                testEnd0 = positionEnd[0]
                testEnd1 = positionEnd[1]
                testEnd0 += (1 if testEnd0 < positionStart[0] else -1)
                testEnd1 += (1 if testEnd1 < positionStart[1] else -1)
                while positionStart[0] != testEnd0 and positionStart[1] != testEnd1  :
                    if self.board[testEnd0][testEnd1] != ' ' :
                        print(self.board[testEnd0][testEnd1])
                        return False
                    testEnd0 += (1 if testEnd0 < positionStart[0] else -1)
                    testEnd1 += (1 if testEnd1 < positionStart[1] else -1)
                return True
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][4] :
            if self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                if positionStart[0] == positionEnd[0] :
                    if positionStart[1] == positionEnd[1] + (1 if positionStart[1] > positionEnd[1] else -1) :
                        return True
                elif positionStart[1] == positionEnd[1]  :
                    if positionStart[0] == positionEnd[0] + (1 if positionStart[0] > positionEnd[0] else -1) :
                        return True
                elif positionStart[0] == positionEnd[0] + (1 if positionStart[0] > positionEnd[0] else -1) and positionStart[1] == positionEnd[1] + (1 if positionStart[1] > positionEnd[1] else -1) :
                    return True
            return False  
                

    def playPieces(self,positionStart,positionEnd,board,turn):
        self.turn = turn
        self.board = board
        if(self.isValidMove(positionStart,positionEnd)):
            print("Valid Move")
            checkBoard = copy.deepcopy(self.board)
            checkBoard[positionEnd[0]][positionEnd[1]] = checkBoard[positionStart[0]][positionStart[1]]
            checkBoard[positionStart[0]][positionStart[1]] = ' '
            if self.isCheck(checkBoard) :
                print("Valid check")
                self.board = checkBoard
                self.turn += 1
                return True, self.boardToJson()
            print("Invalid check")
            return False, self.board
        print("Invalid Move")
        return False, self.board


    def affBoard(self) :
        print("   ",['0', '1', '2', '3', '4', '5', '6', '7'])
        for i in range(8) :
            print(i, " ",self.board[i])
    def affBoardTest(self,board) :
        print("   ",['0', '1', '2', '3', '4', '5', '6', '7'])
        for i in range(8) :
            print(i, " ",board[i])
    def isGameOver(self) :
        if self.turn == 64 :
            return True
        return False
    
    def kingPos(self,checkBoard) :
        self.affBoardTest(checkBoard)
        for i in range(len(checkBoard)) :
            for j in range(len(checkBoard[i])) :
                if checkBoard[i][j] == self.playerPieceList[self.turn%2][4] :
                    return [i,j]
    
    def isCheck(self,checkBoard) :
        kingPosition = self.kingPos(checkBoard)
        testLeft = kingPosition[0]
        testRight = kingPosition[0]
        while testLeft > 0 :
            testLeft -= 1
            if checkBoard[testLeft][kingPosition[1]] != ' ' :
                if checkBoard[testLeft][kingPosition[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testLeft][kingPosition[1]] in "QRqr"  : 
                    return False
                elif abs(testLeft-kingPosition[0]) == 1 and checkBoard[testLeft][kingPosition[1]] in "Kk" :
                    return False
                else :
                    break
        while testRight < 7 :
            testRight += 1
            if checkBoard[testRight][kingPosition[1]] != ' ' :
                if checkBoard[testRight][kingPosition[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testRight][kingPosition[1]] in "QRqr" :
                    return False
                elif  abs(testRight-kingPosition[0]) == 1 and checkBoard[testRight][kingPosition[1]] in "Kk" :
                    return False
                else :
                    break
    
    
        testUp = kingPosition[1]
        testDown = kingPosition[1]

        while testUp > 0 :
            testUp -= 1
            if checkBoard[kingPosition[0]][testUp] != ' ' :
                if checkBoard[kingPosition[0]][testUp] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[kingPosition[0]][testUp] in "QRqr"  :
                    return False
                elif abs(testUp-kingPosition[1]) == 1  and checkBoard[kingPosition[0]][testUp] in "Kk" :
                    return False
                else :
                    break
        while testDown < 7 :
            testDown += 1
            if checkBoard[kingPosition[0]][testDown] != ' ' :
                if checkBoard[kingPosition[0]][testDown] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[kingPosition[0]][testDown] in "QRqr"  :
                    return False
                elif abs(testDown-kingPosition[1]) == 1 and checkBoard[kingPosition[0]][testDown] in "Kk" :
                    return False
                else :
                    break

        testUpLeft = kingPosition.copy()
        testUpRight = kingPosition.copy()
        testDownLeft = kingPosition.copy()
        testDownRight = kingPosition.copy()
        while testUpLeft[0] > 0 and testUpLeft[1] > 0 :
            testUpLeft[0] -= 1
            testUpLeft[1] -= 1
            if checkBoard[testUpLeft[0]][testUpLeft[1]] != ' ' :
                if checkBoard[testUpLeft[0]][testUpLeft[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testUpLeft[0]][testUpLeft[1]] in "QBqb"  :
                    return False
                elif abs(testUpLeft[0]-kingPosition[0]) and abs(testUpLeft[1]-kingPosition[1]) and checkBoard[testUpLeft[0]][testUpLeft[1]] in "Kk" :
                    return False
                else :
                    break
        while testUpRight[0] > 0 and testUpRight[1] < 7 :
            testUpRight[0] -= 1
            testUpRight[1] += 1
            if checkBoard[testUpRight[0]][testUpRight[1]] != ' ' :
                if checkBoard[testUpRight[0]][testUpRight[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testUpRight[0]][testUpRight[1]] in "QBqb" :
                    return False
                elif abs(testUpRight[0]-kingPosition[0]) and abs(testUpRight[1]-kingPosition[1]) and checkBoard[testUpRight[0]][testUpRight[1]] in "Kk" :
                    return False
                else :
                    break
        while testDownLeft[0] < 7 and testDownLeft[1] > 0 :
            testDownLeft[0] += 1
            testDownLeft[1] -= 1
            if checkBoard[testDownLeft[0]][testDownLeft[1]] != ' ' :
                if checkBoard[testDownLeft[0]][testDownLeft[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testDownLeft[0]][testDownLeft[1]] in "QBqb"  :
                    return False
                elif  abs(testDownLeft[0]-kingPosition[0]) and abs(testDownLeft[1]-kingPosition[1]) and checkBoard[testDownLeft[0]][testDownLeft[1]] in "Kk" :
                    return False
                else :
                    break
        while testDownRight[0] < 7 and testDownRight[1] < 7 :
            testDownRight[0] += 1
            testDownRight[1] += 1
            if checkBoard[testDownRight[0]][testDownRight[1]] != ' ' :
                if checkBoard[testDownRight[0]][testDownRight[1]] in self.playerPieceList[self.turn%2] :
                    break
                elif checkBoard[testDownRight[0]][testDownRight[1]] in "QBqb" :
                    return False
                elif abs(testDownRight[0]-kingPosition[0]) and abs(testDownRight[1]-kingPosition[1]) and checkBoard[testDownRight[0]][testDownRight[1]] in "Kk" :
                    return False
                else :
                    break        
        
        return True
    

    def isCheckMate(self) :
        checkBoard = copy.deepcopy(self.board)
        for i in range(0,8) :
            for j in range(0,8) :
                if checkBoard[i][j] == self.playerPieceList[self.turn%2][4] :
                    if self.isCheck(checkBoard) :
                        return False
                    else :
                        for k in range(0,8) :
                            for l in range(0,8) :
                                if checkBoard[k][l] == self.playerPieceList[self.turn%2][4] :
                                    checkBoard[k][l] = ' '
                                    for m in range(-1,2) :
                                        for n in range(-1,2) :
                                            if k+m < 0 or k+m > 7 or l+n < 0 or l+n > 7 :
                                                continue
                                            elif checkBoard[k+m][l+n] == ' ' or checkBoard[k+m][l+n] not in self.playerPieceList[self.turn%2] :
                                                lastValue = checkBoard[k+m][l+n]
                                                checkBoard[k+m][l+n] = self.playerPieceList[self.turn%2][4]
                                                if self.isCheck(checkBoard) :
                                                    checkBoard[k][l] = ' '
                                                    checkBoard[k+m][l+n] = lastValue
                                                    return False
                                                else :
                                                    checkBoard[k][l] = ' '
                                                    checkBoard[k+m][l+n] = lastValue
                                                    continue
                                    return True
        return True


    def play(self) :
        start = (input("Enter the position of the piece you want to move : " ))
        end = (input("Enter the position you want to move the piece to : " ))
        if self.playPieces([int(start[0]),int(start[1])],[int(end[0]),int(end[1])]) :
            self.affBoard()
            self.play()
        else :
            print("Invalid move")
            self.play()

    def boardToJson(self) :
        dictBoard = {}
        for row in range(len(self.board)) :
            for cell in range(len(self.board[row])) :
                if(self.board[row][cell] != ' ') :
                    dictBoard[str(row) + str(cell)] = self.board[row][cell]
        return dumps(dictBoard)

    def jsonToBoard(self,jsonBoard) :
        self.board = [[' ' for i in range(8)] for j in range(8)]
        dictBoard = loads(jsonBoard)
        for key in dictBoard :
            self.board[int(key[0])][int(key[1])] = dictBoard[key]
        self.affBoard()
        return self.board

    # fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    def jsonToFen(self,jsonBoard) :
        self.jsonToBoard(jsonBoard)
        fen = ""
        for i in range(len(self.board)) :
            count = 0
            for j in range(len(self.board[i])) :
                if self.board[i][j] == ' ' :
                    count += 1
                else :
                    if count != 0 :
                        fen += str(count)
                        count = 0
                    fen += self.board[i][j]
            if count != 0 :
                fen += str(count)
            if i != 7 :
                fen += "/"
        fen += " "
        fen += "b" if self.turn%2 == 0 else "w"
        fen += " KQkq "
        fen += "- "
        fen += "0"
        fen += " "
        fen += "1"
        return fen


# test = Chess('player1','player2')
# test.affBoard()
# test.play()
# test.getBoardJson()