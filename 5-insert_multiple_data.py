import mysql.connector

# import mysql.connector
#create user 'user'@'%' identified by 'password'

mydb = mysql.connector.connect(
  host="localhost",user="abc",password="password")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute(""" insert into venom.mlbootcamp1 values(1,'Aditya','Panda','2024-02-16','sql','MachineLearning'),
(2,'Rohan','Sharma','2024-02-16','mysql','MachineLearning'),
(3,'Aditya','Rohan','2022-11-21','logging','MachineLearning')""")
mydb.commit()