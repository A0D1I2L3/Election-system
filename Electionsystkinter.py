from tkinter import *
import mysql.connector as broker

mydb = broker.connect(host='192.168.1.62',user='root',port=3306, password='tiger')
mycursor=mydb.cursor()
mycursor.execute("Use electionsys")
mycursor.execute("Select position from candidates")
positions=mycursor.fetchall()

main_window=Tk()
main_window.geometry("300x200")
'''widgets are added here '''

main_window.title("Election system")
Label1=Label(main_window,text="Election 2023").pack(side=TOP)

mycursor.execute("Select Cndt_Name from candidates")
names=mycursor.fetchall()

for i in positions:
    for position in list(i):

        Label2=Label(main_window,text=f"{str(position)}").pack(ipadx=10,ipady=20)

        for k in names:
            for name in list(k):
                button=Radiobutton(main_window,text=f"{str(name)}",value="jj").pack(ipadx=8,ipady=2)














main_window.mainloop()


