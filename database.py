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
    mycursor = mydb.cursor()
    hashedpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql = "INSERT INTO users (pseudo, password) VALUES (%s, %s)"
    val = (username, hashedpassword)
    mycursor.execute(sql, val)
    mydb.commit()



# function to check password in database and return boolean
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
    
