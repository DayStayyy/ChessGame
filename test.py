import unittest
from Mychess import Chess


    
class MychessFunc():

    def __init__(self) -> None:
        self.createMyChess()
    
    def createMyChess(self):
        self.chessGame =  Chess('player1','player2')
        return self.chessGame


    def createChessFromJson(self):
        self.jsonGame = self.chessGame.newGame()
        return  self.jsonGame

    def testJsonToFen(self,turn):
        return self.chessGame.jsonToFen(self.jsonGame,turn)

    

    def testJsonToGame(self):
        chessFunc.createChessFromJson()
        return chessFunc.testJsonToGame()
    

chessFunc = MychessFunc()

class testMychess(unittest.TestCase):

    def testCreateMyChess(self) :
        self.assertIsNotNone(chessFunc.createMyChess())
    
    def testCreateChessFromJson(self):
        self.assertIsNotNone(chessFunc.createChessFromJson())
    
    def testJsonToFen(self):
        chessFunc.createChessFromJson()
        self.assertEqual(chessFunc.testJsonToFen(1), "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1")
        self.assertEqual(chessFunc.testJsonToFen(2), "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def jsonToGame(self):
        self.assertIsNotNone(chessFunc.testJsonToGame())
        
        

if __name__ == '__main__':
    unittest.main()