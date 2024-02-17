import mysql.connector

# import mysql.connector
#create user 'user'@'%' identified by 'password'

mydb = mysql.connector.connect(
  host="localhost",user="abc",password="password")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute(" select * from venom.mlbootcamp1 where studentid>1 and course='MachineLearning' ")

for i in mycursor:
    print(i)