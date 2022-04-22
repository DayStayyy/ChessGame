from flask import Flask, render_template
from chess import Chess

app = Flask(__name__)
app.run(debug=True)


@app.route('/')
def hello():
    return render_template('index.html') 