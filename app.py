#python -m flask run
from importlib.resources import path
from json import dumps
import time
from flask import Flask, render_template, redirect, url_for, request, jsonify, session, make_response
import mysql.connector
import bcrypt
from database import addRankedPoints, addTurn, deleteGame, getGame, insert_user,verify_password,createNewGameJson,getGame,getAllGames,getUserPoints,editUser
import chess
import chess.engine
from Mychess import Chess

app = Flask(__name__)
app.run(debug=True)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
chessGame = Chess('player1','player2')

@app.route('/play', methods=['GET', 'POST'])     
def play():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')

    if request.args.get('gameId'):
        gameId = request.args.get('gameId')
        if request.args.get('type')  and request.args.get('turn'):
            type = request.args.get('type')
            turn = request.args.get('turn')
            game = getGame(request.args.get('gameId')) 

            if game[2] == type and game[4] == int(turn):
                return render_template('game.html')
            print("game not found")
            return redirect("/play?gameId=" + str(gameId)+"&type="+game[2]+"&turn="+str(game[4]))

        else :
            game = getGame(request.args.get('gameId'))
            return redirect("/play?gameId=" + str(gameId)+"&type="+game[2]+"&turn="+str(game[4]))
    else:
        #create new game
        print("Create a new Game")
        gameType = "player"
        if request.args.get('type') :
            gameType = request.args.get('type')
            
        gameId = newGameFunction(session['id'], gameType)
        print("gameId: ", gameId)
        return redirect("/play?gameId=" + str(gameId)+"&type="+gameType)

@app.route('/api/board', methods=['GET'])
def board():
    gameId = request.args.get('gameId')
    print("gameId DE BOARD: ", gameId)
    game = getGame(gameId)
    print("game: ", game)
    jsonFile = open(game[3], "r")
    board = jsonFile.read()
    jsonFile.close()
    return jsonify(board) 

# play piece in a game with this id
@app.route('/api/playPieces', methods=['GET'])
def playPieces():
    startPos = request.args.get('from')
    endPos = request.args.get('to')
    gameId = request.args.get('gameId')
    game = getGame(gameId)
    jsonFile = open(game[3], "r")
    board = jsonFile.read()
    jsonFile.close()
    result,board = chessGame.playPieces([int(startPos[0]),int(startPos[1])],[int(endPos[0]),int(endPos[1])],chessGame.jsonToBoard(board),game[4])
    if result :
        if(game[2] == "player"):
            turn = game[4]+1
        else :
            turn = game[4]+2
        addTurn(gameId,turn)
        jsonFile = open(game[3], "w")
        jsonFile.write(board)
        jsonFile.close()
        return "true"
    return "false"


@app.route('/api/newGame',methods=['GET'])
def newGame():
    print("YO FREROT")
    if not session.get('name') and not session.get('id'):
        "Yo frend, you need to login to create a new game"
        return jsonify(-1)
    
    if request.method == 'GET':
        if request.args.get('type') :
            gameId = newGameFunction(session['id'], request.args.get('type'))
            return jsonify(gameId)
    return jsonify(-1)

def newGameFunction(id,type) :
    path = "data/gamesJson/"
    gameId = createNewGameJson(id,type,path)
    print("game created: ", gameId)
    path = getGame(gameId)[3]
    print("path: ", path)
    board = chessGame.newGame()
    jsonFile = open(path, "w")
    jsonFile.write(board)
    jsonFile.close()
    return gameId


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] or request.form['password']) == None:
            error = 'Please fill all the fields'
            return render_template('login.html', error=error)
        result, id = verify_password(request.form['username'],request.form['password'])
        if result == True:
            session["name"] = request.form.get("username")
            session["id"] = id
            return redirect('/')
        return render_template('login.html', error=error)
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] or request.form['password'] :
           insert_user(request.form['username'], request.form['password']) 
           return redirect(url_for('login'))
        else:
            print("erreur de register")
    return render_template('register.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def menu():
    error = None
    if not session.get('name'):
        return redirect('/login')
    if request.method == 'logout':
        return redirect(url_for('sign_out'))
    return render_template('menu.html', error=error)

@app.route('/option', methods=['GET', 'POST'])
def option():
    error = None
    if not session.get('name'):
        return redirect('/login')
    return render_template('option.html')
@app.route('/sign_out')
def sign_out():
    session.pop('name')
    return redirect(url_for('login'))

@app.route('/api/checkmate')     
def checkmate():
    time.sleep(0.5)
    gameId = request.args.get('gameId')
    game = getGame(gameId)
    fen = jsonToFen(game[3])
    board = chess.Board(fen)
    if(board.is_checkmate()) :
        print("checkmate")
        if(game[4]%2 == 0):
            addRankedPoints(game[1])
        return "true"
    return "false"
    

# function get all games of a user with this id
@app.route('/allGames', methods=['GET', 'POST'])
def allGames():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')
    games = getAllGames(session['id'])
    print("games: ", games)
    return render_template('gamesBoard.html',games=games)


# fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# function read json to fen
def jsonToFen(jsonFile):
    jsonFile = open(jsonFile, "r")
    board = jsonFile.read()
    jsonFile.close()
    result = chessGame.jsonToFen(board)
    return result

# Searching Stockfish's Move
@app.route('/api/Stockfish', methods=['GET', 'POST'])
def stockfish():
    gameId = request.args.get('gameId')
    game = getGame(gameId)
    fen = jsonToFen(game[3])
    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci(
        "engines/stockfish.exe")
    move = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(move.move)

    jsonFile = open(game[3], "w")
    jsonFile.write(boardToJson(board))
    jsonFile.close()
    return "true"
    


def boardToJson(board):
    boardArr = board.__str__().replace(" ", "").splitlines()
    dictBoard = {}
    for row in range(len(boardArr)) :
        for cell in range(len(boardArr[row])) :
            if(boardArr[row][cell] != '.') :
                dictBoard[str(row) + str(cell)] = boardArr[row][cell]
    return dumps(dictBoard)

@app.route('/chooseLevel')
def chooseLevel():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')
    return render_template('chooseLevel.html')

@app.route('/deleteGames', methods=['GET', 'POST'])
def deleteGames():
    if not session.get('name'):
        return redirect('/login')
    if request.args.get('gameId'):
        gameId = request.args.get('gameId')
        deleteGame(session['id'],gameId)
        return redirect(url_for('allGames'))
    return render_template('gamesBoard.html')

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    print("profil")
    error = None
    if not session.get('name'):
        session["points"] = getUserPoints(session["name"])
        return redirect('/login')
    return render_template('profil.html', error=error)

# edit the profil with new password and check current password
@app.route('/editProfil', methods=['GET', 'POST'])
def editProfil():
    error = None
    if request.method == 'POST':
        if request.form['username'] or request.form['password'] or request.form['newpassword'] or request.form['confirmpassword'] :
            if request.form['newpassword'] == request.form['confirmpassword']:
                if verify_password(session["name"],request.form['password'])[0] == True:
                    editUser(request.form['newpassword'], request.form['username'])
                    return redirect(url_for('profil'))
                return render_template('profil.html', error=error)
            return render_template('profil.html', error=error)
    return render_template('editProfil.html', error=error)

