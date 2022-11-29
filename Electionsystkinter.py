from tkinter import *
import mysql.connector as broker

mydb = broker.connect(host='192.168.1.62',user='chomu', password='tiger')
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
main_window.geometry("400x300")

#adding widgets 
main_window.title("Election system")
Label1=Label(main_window,text="Election 2023").pack(side=TOP)

proceed=IntVar()
value=StringVar()

def next_window(posn):
    
    Window=Toplevel(newWindow)
    Window.geometry("400x300")
    Label(Window,text=f"{posn}").pack(ipadx=5,ipady=5)

    for name in grouped_list:
        if name[1]==posn:
            Radiobutton(Window,text=f"{name[0]}",variable = value,value=f"{name[0]}").pack(ipadx=5,ipady=10)
    save_button=Button(Window,text="Save vote",command=lambda:[Window.destroy(),vote()])
    save_button.pack()
    save_button.wait_variable(proceed)

def vote():
    votevalue=(value.get(),)
    print(votevalue)
    sql='''update candidates set Vote_cnt=Vote_cnt+1 where Cndt_Name=%s'''
    mycursor.execute(sql,votevalue)
    
    global posn

    try :
        posn=posn_list[(posn_list.index(posn))+1]
        next_window(posn)
    except IndexError:
        pass
    
    mydb.commit()



def start():
    global newWindow
    newWindow=Toplevel(main_window)
    newWindow.geometry("400x400")
    global posn

    for posn in posn_list:
        Label(newWindow,text=f"{posn}").pack(ipadx=5,ipady=5)

        for name in grouped_list:
            if name[1]==posn:
                Radiobutton(newWindow,text=f"{name[0]}",variable = value,value=f"{name[0]}").pack(ipadx=5,ipady=10)

        save_button=Button(newWindow,text="Save vote",command=lambda:[newWindow.withdraw(),vote()])
        save_button.pack()
        save_button.wait_variable(proceed)


Button(text="Start voting",command=lambda:[main_window.withdraw(),start()]).pack(anchor=CENTER)


        


main_window.mainloop()


