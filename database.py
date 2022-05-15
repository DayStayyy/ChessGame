import os
import mysql.connector
import bcrypt 
mydb = mysql.connector.connect(
    host="localhost",
    user="benji",
    password="benji",
    database='chessgame'
)
print(mydb) 

def insert_user(username, password):
    mycursor = mydb.cursor(buffered=True)
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = "INSERT INTO users (pseudo, password) VALUES (%s, %s)"
    val = (username, hashedpassword)
    mycursor.execute(sql, val)
    mydb.commit()

def createNewGame(playerId,type,path) :
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (playerId,type,path) VALUES (%s, %s, %s)"
    val = (playerId, type, path)
    mycursor.execute(sql, val)
    mydb.commit()
    # get the id of the game just created
    sql = "SELECT id FROM games WHERE playerId = %s"
    val = (playerId, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    while myresult is not None :
        myresult = mycursor.fetchone()
    # modify path to add the id of the game
    path = path + str(myresult[0]) + ".json"
    sql = "UPDATE games SET path = %s WHERE gameId = %s"
    val = (path, myresult[0])
    mycursor.execute(sql, val)
    mydb.commit()
    return myresult[0]

# function to check if user exists and password is correct and return the id of the user
def verify_password(username, password):
    mycursor = mydb.cursor()
    sql = "SELECT user_id, password FROM users WHERE pseudo = %s"
    val = (username, )
    myresult = mycursor.execute(sql, val)
    if myresult is not None :
        if bcrypt.checkpw(password.encode('utf-8'), myresult[1]) :
            return True, myresult[0]
    return False, 0

def getGame(gameId):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM games WHERE id = %s"
    val = (gameId, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult