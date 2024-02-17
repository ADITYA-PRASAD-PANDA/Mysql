import mysql.connector

# import mysql.connector
#create user 'user'@'%' identified by 'password'

mydb = mysql.connector.connect(
  host="localhost",user="abc",password="password")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute(" select * from venom.mlbootcamp1 ")

for i in mycursor:
    print(i)