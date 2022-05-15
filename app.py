#python -m flask run
from importlib.resources import path
from flask import Flask, render_template, redirect, url_for, request, jsonify, session, make_response
import mysql.connector
import bcrypt
from database import getGame, insert_user,verify_password,createNewGame,getGame,getAllGames
from chess import Chess

app = Flask(__name__)
app.run(debug=True)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
chess = Chess('player1','player2')

@app.route('/play', methods=['GET', 'POST'])     
def play():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')

    if request.args.get('gameId'):
        return render_template('game.html')
    else:
        #create new game
        print("Create a new Game")
        gameId = newGameFunction(session['id'], 1)
        print("gameId: ", gameId)
        return redirect("/play?gameId=" + str(gameId))

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
    result,board = chess.playPieces([int(startPos[0]),int(startPos[1])],[int(endPos[0]),int(endPos[1])],chess.jsonToBoard(board))
    if result :
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
    
    path = "data/games/"
    if request.method == 'GET':
        if request.args.get('type') :
            gameId = createNewGame(session['id'],request.args.get('type'),path)
            print("game created: ", gameId)
            path = getGame(gameId)[3]
            print("path: ", path)
            board = chess.newGame(path)
            jsonFile = open(path, "w")
            jsonFile.write(board)
            jsonFile.close()
            return jsonify(gameId)
    return jsonify(-1)

def newGameFunction(id,type) :
    path = "data/games/"
    gameId = createNewGame(id,type,path)
    print("game created: ", gameId)
    path = getGame(gameId)[3]
    print("path: ", path)
    board = chess.newGame()
    jsonFile = open(path, "w")
    jsonFile.write(board)
    jsonFile.close()
    return gameId


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
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
    if request.method == 'POST':
        return redirect(url_for('home'))
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
    if(chess.isCheckMate()) :
        print("checkmate")
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