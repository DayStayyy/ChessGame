from json import dumps

class Chess :
    def __init__(self,player1,player2) :
        self.player1 = player1
        self.player2 = player2
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.board[0][0] = 'R'
        self.board[0][1] = 'N'
        self.board[0][2] = 'B'
        self.board[0][3] = 'Q'
        self.board[0][4] = 'K'
        self.board[0][5] = 'B'
        self.board[0][6] = 'N'
        self.board[0][7] = 'R'
        self.board[1][0] = 'P'
        self.board[1][1] = 'P'
        self.board[1][2] = 'P'
        self.board[1][3] = 'P'
        self.board[1][4] = 'P'
        self.board[1][5] = 'P'
        self.board[1][6] = 'P'
        self.board[1][7] = 'P'
        self.board[7][0] = 'r'
        self.board[7][1] = 'n'
        self.board[7][2] = 'b'
        self.board[7][3] = 'q'
        self.board[7][4] = 'k'
        self.board[7][5] = 'b'
        self.board[7][6] = 'n'
        self.board[7][7] = 'r'
        self.board[6][0] = 'p'
        self.board[6][1] = 'p'
        self.board[6][2] = 'p'
        self.board[6][3] = 'p'
        self.board[6][4] = 'p'
        self.board[6][5] = 'p'
        self.board[6][6] = 'p'
        self.board[6][7] = 'p'
        self.turn = 0
        self.playerPieceList = [['R','N','B','Q','K','P'],['r','n','b','q','k','p']]
        
    def isValidMove(self,positionStart,positionEnd) :
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
                if positionStart[0] == positionEnd[0] and positionStart[1] == positionEnd[1] + (1 if positionStart[1] < positionEnd[1] else -1) :
                    return True
                elif positionStart[0] == positionEnd[0] + (1 if positionStart[1] < positionEnd[1] else -1) and positionStart[1] == positionEnd[1] :
                    return True
                elif positionStart[0] == positionEnd[0] + (1 if positionStart[1] < positionEnd[1] else -1) and positionStart[1] == positionEnd[1] + (1 if positionStart[1] < positionEnd[1] else -1) :
                    return True
            return False  
                

    def playPieces(self,positionStart,positionEnd):
        if(self.isValidMove(positionStart,positionEnd)):
            self.board[positionEnd[0]][positionEnd[1]] = self.board[positionStart[0]][positionStart[1]]
            self.board[positionStart[0]][positionStart[1]] = ' '
            self.turn += 1
            return True
        return False


    def affBoard(self) :
        print("   ",['0', '1', '2', '3', '4', '5', '6', '7'])
        for i in range(8) :
            print(i, " ",self.board[i])

    def play(self) :
        start = (input("Enter the position of the piece you want to move : " ))
        end = (input("Enter the position you want to move the piece to : " ))
        if self.playPieces([int(start[0]),int(start[1])],[int(end[0]),int(end[1])]) :
            self.affBoard()
            self.play()
        else :
            print("Invalid move")
            self.play()

    def getBoardJson(self) :
        dictBoard = {}
        for row in range(len(self.board)) :
            for cell in range(len(self.board[row])) :
                if(self.board[row][cell] != ' ') :
                    dictBoard[str(row) + str(cell)] = self.board[row][cell]
        return dumps(dictBoard)

# test = Chess('player1','player2')
# test.affBoard()
# test.play()
# test.getBoardJson()