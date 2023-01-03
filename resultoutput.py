import mysql.connector as broker
import matplotlib.pyplot as plt
from tkinter import *



mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()

mycursor.execute("Use electionsys")
mycursor.execute("select Cndt_name,position,vote_cnt from candidates group by cndt_Name order by position,vote_cnt desc;")
data=mycursor.fetchall()

for i in data:
    print(i)



