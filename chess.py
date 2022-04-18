class chess :
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
        self.playerPieceList = [['R','N','B','Q','K','B','N','R','P'],['r','n','b','q','k','b','n','r','p']]
        
    
    def playPieces(self,positionStart,positionEnd):
        print(positionStart," ",positionEnd)
        if self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][8] :
            if positionEnd[0] == positionStart[0] + 2 and positionEnd[1] == positionStart[1] and self.board[positionEnd[0]][positionEnd[1]] == ' ' and self.board[positionStart[0] + 1][positionStart[1]] == ' ' and positionStart[0] == (1 if self.turn%2 == 0  else 6) :
                self.board[positionStart[0]][positionStart[1]] = ' '
                self.board[positionEnd[0]][positionEnd[1]] = self.playerPieceList[self.turn%2][8]
                self.turn += 1
                return True
            elif positionEnd[0] == positionStart[0] + 1 and positionEnd[1] == positionStart[1] and self.board[positionEnd[0]][positionEnd[1]] == ' ':
                    self.board[positionEnd[0]][positionEnd[1]] = self.playerPieceList[self.turn%2][8]
                    self.board[positionStart[0]][positionStart[1]] = ' '
                    self.turn = 1
                    return True
            elif positionEnd[0] == positionStart[0] + 1 and (positionEnd[1] == positionStart[1] + 1 or positionEnd[1] == positionStart[1] - 1) and self.board[positionEnd[0]][positionEnd[1]] != ' ' and self.board[positionEnd[0]][positionEnd[1]] not in self.playerPieceList[self.turn%2]:
                self.board[positionEnd[0]][positionEnd[1]] = self.playerPieceList[self.turn%2][8]
                self.board[positionStart[0]][positionStart[1]] = ' '
                self.turn = 1
                return True
            print("Invalid move")
            return False            
        elif self.board[positionStart[0]][positionStart[1]] == self.playerPieceList[self.turn%2][7] :
            pass


    def affBoard(self) :
        for i in range(8) :
            print(i, " ",self.board[i])

    def play(self) :
        start = (input("Enter the position of the piece you want to move : " ))
        end = (input("Enter the position you want to move the piece to : " ))
        if self.playPieces([int(start[0]),int(start[1])],[int(end[0]),int(end[1])]) :
            self.affBoard()
        else :
            self.play()


test = chess('player1','player2')
test.affBoard()
test.play()