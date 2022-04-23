from flask import Flask, render_template, request, jsonify
from chess import Chess

app = Flask(__name__)
app.run(debug=True)

game = Chess('player1','player2')

@app.route('/')
def home():
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