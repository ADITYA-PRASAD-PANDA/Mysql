import mysql.connector

# import mysql.connector
#create user 'user'@'%' identified by 'password'

mydb = mysql.connector.connect(
  host="localhost",user="abc",password="password")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute(" select firstname,lastname,class from venom.mlbootcamp1 where studentid between 2 and 3 ")
for i in mycursor:
    print(i)