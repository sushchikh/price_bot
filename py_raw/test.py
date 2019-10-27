import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='krot',
    passwd='1'
)

print(mydb)