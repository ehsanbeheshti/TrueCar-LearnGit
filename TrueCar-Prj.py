import mysql.connector
import requests
import json
from bs4 import BeautifulSoup

Check_flag = False
db_user ='admin'
db_pass = 'Aa123456!@#$%^'
db_name = 'truecar20'
db_table1 = 'TrueCar'

########################## ADD to DB
def addToDB (db_user,db_pass,db_name,name,address,price,mileage):
    mydb_test = mysql.connector.connect(
        host="localhost",
        user=db_user,
        password=db_pass,
        database=db_name
    )
    mycursor_test = mydb_test.cursor()
    mycursor_test.execute(("USE "+db_name))
    ADD = "INSERT INTO TrueCar  VALUES (%s ,%s , %s, %s)"
    B = (name, address , price, mileage)
    mycursor_test.execute(ADD , B)
    mydb_test.commit()

########################## CREAT DB -->number Test truecar6
def creatDB (db_user,db_pass,db_name):
    mydb_test = mysql.connector.connect(
        host="localhost",
        user=db_user,
        password=db_pass,
        #database="maktab_test"
        )
    mycursor_test = mydb_test.cursor()
    mycursor_test.execute(("CREATE DATABASE "+ db_name))
    mycursor_test.execute(("USE "+db_name))
    mycursor_test.execute("CREATE TABLE TrueCar (Name VARCHAR(30),address VARCHAR(30), Price VARCHAR(20) , Mileage VARCHAR(20)) ;")

########################## SELECT from DB -->number Test truecar6
def selectDB (db_user,db_pass,db_name,db_table1):
    mydb_test = mysql.connector.connect(
        host="localhost",
        user=db_user,
        password=db_pass,
        database=db_name
        )
    mycursor_test = mydb_test.cursor()
    mycursor_test.execute("SELECT * FROM "+ db_table1 + ";")
    myresult = mycursor_test.fetchall()
    for x in myresult:
        print (x)



print('****We Will Start with DB informatio so ****')
db_user = input("Pleas Enter your database Username:")
db_pass = input("Pleas Enter your database Password:")
db_name = input("Pleas Enter your database name:")
creatDB (db_user,db_pass,db_name)
addToDB (db_user,db_pass,db_name,'ferari','sankhoze','test' , 'test')
addToDB (db_user,db_pass,db_name,'ferari2','sankhoze2','test2' , 'test2')
addToDB (db_user,db_pass,db_name,'ferari3','sankhoze3','test3' , 'test3')
addToDB (db_user,db_pass,db_name,'ferari4','sankhoze4','test4' , 'test4')

selectDB (db_user,db_pass,db_name,db_table1)

print('change')
