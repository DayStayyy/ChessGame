from flask import Flask, render_template
from chess import Chess

app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello():
    game = Chess('player1','player2')
    board = game.getBoardJson()
    jsonFile = open("data/board.json", "w")
    jsonFile.write(board)
    jsonFile.close()

    return render_template('index.html') 