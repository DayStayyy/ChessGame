#python -m flask run
from importlib.resources import path
from flask import Flask, render_template, redirect, url_for, request, jsonify, session, make_response
import mysql.connector
import bcrypt
from database import getGame, insert_user,verify_password,createNewGame,getGame
from chess import Chess

app = Flask(__name__)
app.run(debug=True)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
chess = Chess('player1','player2')

@app.route('/play', methods=['GET', 'POST'])     
def home():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')

    if request.args.get('gameId'):
        return render_template('game.html')
    else:
        #create new game
        gameId = createNewGame(session['id'],1,"data/games/")
        return render_template('game.html',gameId=gameId)

@app.route('/api/board', methods=['GET'])
def board():
    gameId = request.args.get('gameId')
    game = getGame(gameId)
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
    if chess.playPieces([int(startPos[0]),int(startPos[1])],[int(endPos[0]),int(endPos[1])]) :
        jsonFile = open("data/board.json", "w")
        jsonFile.write(chess.getBoardJson())
        jsonFile.close()
        return "true"
    return "false"


@app.route('/api/newGame',methods=['GET'])
def newGame():
    if not session.get('name') and not session.get('id'):
        return redirect('/login')
    
    path = "data/games/"
    if request.method == 'GET':
        if request.args.get('type') :
            gameId = createNewGame(session['id'],request.args.get('type'),path)
            return jsonify(gameId)
    return jsonify(-1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        result, id = verify_password(request.form['username'],request.form['password'])
        if result == True:
            session["name"] = request.form.get("username")
            session["id"] = id
            return redirect('/menu')
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
