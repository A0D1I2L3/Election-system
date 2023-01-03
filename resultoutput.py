import mysql.connector as broker
import matplotlib.pyplot as plt
from tkinter import *



mydb=broker.connect(host='localhost',user='root',passwd='tiger')
mycursor=mydb.cursor()

mycursor.execute("Use electionsys")
mycursor.execute("select Cndt_name from candidates group by cndt_Name order by position,vote_cnt desc;")
name=mycursor.fetchall()
mycursor.execute("select position from candidates group by cndt_Name order by position,vote_cnt desc;")
posn=mycursor.fetchall()
mycursor.execute("select vote_cnt from candidates group by cndt_Name order by position,vote_cnt desc;")
vote_cnt=mycursor.fetchall()


main_window=Tk()
main_window.geometry("400x300")
main_window.configure(background='#181818')

def bar():
    pass
def chart():
    pass

fra=Frame(main_window)
fra.pack(pady=50)
fra.configure(bg='#181818')
button=Button(fra,text="Bar Graph",command=bar,bg="white",height=2,width=10).pack(pady=5)
button=Button(fra,text="Pie Chart",command=chart,bg="white",height=2,width=10).pack()



main_window.title(" Result ")






main_window.mainloop()