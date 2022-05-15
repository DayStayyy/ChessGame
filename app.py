#python -m flask run
from flask import Flask, render_template, redirect, url_for, request, jsonify, session, make_response
import mysql.connector
import bcrypt
from database import insert_user,verify_password,getUserPoints,editUser
from chess import Chess

app = Flask(__name__)
app.run(debug=True)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
game = Chess('player1','player2')

@app.route('/', methods=['GET', 'POST'])     
def home():
    if not session.get('name'):
        return redirect('/login')
    board = game.getBoardJson()
    jsonFile = open("data/board.json", "w")
    jsonFile.write(board)
    jsonFile.close()
    return render_template('index.html') 

@app.route('/api/board', methods=['GET'])
def board():
    jsonFile = open("data/board.json", "r")
    board = jsonFile.read()
    jsonFile.close()
    return jsonify(board) 

@app.route('/api/playPieces')
def playPieces():
    startPos = request.args.get('from')
    endPos = request.args.get('to')
    if game.playPieces([int(startPos[0]),int(startPos[1])],[int(endPos[0]),int(endPos[1])]) :
        jsonFile = open("data/board.json", "w")
        jsonFile.write(game.getBoardJson())
        jsonFile.close()
        return "true"
    return "false"

@app.route('/api/reset')     
def reset():
    game = Chess('player1','player2')
    board = game.getBoardJson()
    jsonFile = open("data/board.json", "w")
    jsonFile.write(board)
    jsonFile.close()
    return "true"

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

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    session["points"] = getUserPoints(session["name"])
    error = None
    if not session.get('name'):
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

