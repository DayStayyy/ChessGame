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
    print(username)
    mycursor = mydb.cursor()
    sql = "SELECT password FROM users WHERE pseudo = %s"
    sql_user = "SELECT pseudo FROM users"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    mycursor.execute(sql_user, )
    myresult_user = mycursor.fetchall()
    res = "".join(myresult)
    print(res)
    print(password)
    print(myresult_user)
    # if username not in myresult_user:
    #     return False
    if len(myresult) <= 0:
        return False
    if bcrypt.checkpw(password.encode('utf-8'), res.encode('utf-8')):
        return True
    return False
    