import mysql.connector
import datetime as dt

mydb=mysql.connector.connect(
    host= "127.0.0.1",
    user = "root",
    passwd="NateSaber4669",
    database= "FoxGoatOmega"
    )

mycursor=mydb.cursor()

##mycursor.execute("CREATE DATABASE FoxGoatOmega")
##mycursor.execute("CREATE TABLE EqnStore ( Equation VARCHAR(255) , Solutions VARCHAR(255) , DateTime DATETIME);")

mycursor.execute("INSERT INTO EqnStore VALUES (%s,%s,%s);",("x**2+3*x+2","[-2.0,-1.0]",dt.datetime.now()))
mycursor.execute("DELETE FROM EqnStore WHERE Solution_Set='[-2.0,-1.0]';")
s="INSERT INTO EqnStore VALUES (%s,%s,%s);"
L=('x**2+6*x+8',"[-4.0,-2.0]",dt.datetime.now())

mycursor.execute(s,L)
##e=mycursor.fetchall()
##
##for i in e:
##    print(i)
##
##
##mydb.commit()
