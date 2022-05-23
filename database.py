from json import load
from dotenv import load_dotenv
import os
import mysql.connector
import bcrypt

load_dotenv()
DATABASE_HOST=os.getenv('DATABASE_HOST')
DATABASE_PORT=os.getenv('DATABASE_PORT')
DATABASE_ROOT_PASSWORD=os.getenv('DATABASE_ROOT_PASSWORD')
DATABASE_USER=os.getenv('DATABASE_USER')
DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
DATABASE_NAME=os.getenv('DATABASE_NAME')

connection_string_params = {
"host": DATABASE_HOST,
"user": DATABASE_USER,
"password": DATABASE_PASSWORD,
"db": DATABASE_NAME
}

mydb = mysql.connector.connect(
    **connection_string_params
)
print(mydb) 

def insert_user(username, password):
    mycursor = mydb.cursor()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = "INSERT INTO users (pseudo, password) VALUES (%s, %s)"
    val = (username, hashedpassword)
    mycursor.execute(sql, val)
    mydb.commit()

def createNewGameJson(playerId,type,path) :
    print("path: ", path)
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (playerId,type,path) VALUES (%s, %s, %s)"
    val = (playerId, type, path)
    mycursor.execute(sql, val)
    mydb.commit()
    # get the id of the game just created
    sql = "SELECT gameId FROM games WHERE playerId = %s"
    val = (playerId, )
    mycursor.execute(sql, val)
    # get last myresult
    myresult = mycursor.fetchall()[-1]
    # modify path to add the id of the game
    print("myresult: ", myresult)
    path = path + str(myresult[0]) + ".json"
    sql = "UPDATE games SET path = %s WHERE gameId = %s"
    val = (path, myresult[0])
    mycursor.execute(sql, val)
    mydb.commit()
    return myresult[0]
def editUser(username, password):
    mycursor = mydb.cursor()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = "UPDATE users SET password = %s WHERE pseudo = %s"
    val = (hashedpassword, username)
    mycursor.execute(sql, val)
    mydb.commit()

def createNewGamePng(playerId,type,path) :
    print("path: ", path)
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (playerId,type,path) VALUES (%s, %s, %s)"
    val = (playerId, type, path)
    mycursor.execute(sql, val)
    mydb.commit()
    # get the id of the game just created
    sql = "SELECT gameId FROM games WHERE playerId = %s"
    val = (playerId, )
    mycursor.execute(sql, val)
    # get last myresult
    myresult = mycursor.fetchall()[-1]
    # modify path to add the id of the game
    print("myresult: ", myresult)
    path = path + str(myresult[0]) + ".png"
    sql = "UPDATE games SET path = %s WHERE gameId = %s"
    val = (path, myresult[0])
    mycursor.execute(sql, val)
    mydb.commit()
    return myresult[0]

# function to check if user exists and password is correct and return the id of the user
def verify_password(username, password):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE pseudo = %s"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    print(myresult)
    if myresult is not None :
        if bcrypt.checkpw(password.encode('utf-8'), myresult[2].encode('utf-8')):
            return True, myresult[0]
    return False, -1


def getGame(gameId):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM games WHERE gameId = %s"
    val = (gameId, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult

def getAllGames(userId) :
    mycursor = mydb.cursor()
    sql = "SELECT * FROM games WHERE playerId = %s"
    val = (userId, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def addTurn(gameId, turn):
    mycursor = mydb.cursor()
    sql = "UPDATE games SET turn = %s WHERE gameId = %s"
    val = (turn, gameId)
    mycursor.execute(sql, val)
    mydb.commit()

def deleteGame(userId, gameId) :
    mycursor = mydb.cursor()
    sql = "DELETE FROM games WHERE playerId = %s AND gameId = %s"
    val = (userId, gameId)
    mycursor.execute(sql, val)
    
def getUserPoints(username):
    mycursor = mydb.cursor()
    sql = "SELECT rankedpoints FROM users WHERE pseudo = %s"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    res = str(myresult[0])
    return res

def editProfil(username, password):
    mycursor = mydb.cursor()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = "INSERT INTO users (pseudo, password) VALUES (%s)"
    val = (username, )
    mycursor.execute(sql, val)
    mydb.commit()

def addRankedPoints(userId) :
    mycursor = mydb.cursor()
    sql = "UPDATE users SET rankedPoints = rankedPoints + 10 WHERE user_id = %s"
    val = (userId, )
    mycursor.execute(sql, val)
    mydb.commit()