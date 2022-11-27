from tkinter import *
import mysql.connector as broker

mydb = broker.connect(host='192.168.1.3',user='chomu', password='tiger')
mycursor=mydb.cursor()
mycursor.execute("Use electionsys")



#candiate name , positions are fetched from sql
mycursor.execute("Select Cndt_Name,position from candidates")
data=mycursor.fetchall()
print(data)

#positions are added to separate list
posn_list=[]
grouped_list=[]
for i in data:
    if i[1] not in posn_list:
        posn_list.append(i[1])
print(posn_list)

#candidate name,posn are grouped based on position
for j in posn_list:
    for k in data:
        if k[1]==j:
            grouped_list.append(k)
print(grouped_list)


#tkinter starts here
#initialising tkinter
main_window=Tk()
main_window.geometry("300x200")

#adding widgets 
main_window.title("Election system")
Label1=Label(main_window,text="Election 2023").pack(side=TOP)


def save():
    print('hehe')
    proceed.set(1)
    
proceed=IntVar()
for posn in posn_list:
    Label(text=f"{posn}").pack(ipadx=5,ipady=5)
    for name in grouped_list:
        print(name[1])
        if name[1]==posn:
            Radiobutton(text=f"{name[0]}",value=f"{name[0]}").pack(ipadx=5,ipady=10)

    button=Button(text="Cast this vote",command=save)
    button.pack(side=BOTTOM)
    proceed.set(None)
    button.wait_variable(proceed)


main_window.mainloop()


