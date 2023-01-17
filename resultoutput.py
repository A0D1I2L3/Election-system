from tkinter import *
from tkinter import ttk

import mysql.connector as broker
import matplotlib.pyplot as plt


mydb = broker.connect(host='192.168.1.62',user='chomu', password='tiger')
mycursor=mydb.cursor()
mycursor.execute("Use electionsys")



#candiate name , positions are fetched from sql
mycursor.execute("Select Cndt_Name,position,vote_cnt from candidates")
data=mycursor.fetchall()

#positions are added to separate list
posn_list=[]
grouped_list=[]
for i in data:
    if i[1] not in posn_list:
        posn_list.append(i[1])

#candidate name,posn are grouped based on position
for j in posn_list:
    for k in data:
        if k[1]==j:
            grouped_list.append(k)


#tkinter starts here
#initialising tkinter
main_window=Tk()
main_window.geometry("400x300")
main_window.configure(background='#181818')
#adding widgets 

fra=Frame(main_window)
fra.pack(pady=50)
fra.configure(bg='#181818')




main_window.title(" Result ")

proceed=IntVar()
value=StringVar()
d={}

def selector():
    fnctn=pie_button.cget('text')
    fnctn1=bar_button.cget('text')

    global newWindow
    newWindow=Toplevel(main_window)
    newWindow.geometry("400x400")
    newWindow.configure(background='#181818')
    fra=Frame(newWindow)
    fra.pack(pady=50)
    fra.configure(bg='#181818')

    global posn
    if fnctn=="Pie chart":
        for posn in posn_list:
            b=Button(newWindow,text=f"{posn}",command=pi)
            b.pack(padx=5,pady=5)
    if fnctn1=="Bar graph":
        for posn in posn_list:
            b=Button(newWindow,text=f"{posn}",command=bar)
            b.pack(padx=5,pady=5)

    
    




def bar():
    
    
    names=[]
    votes=[]


    for posn in posn_list:
        
        for name in grouped_list:
            if name[1]==posn:
                names.append(name[0])
                votes.append(name[2])

            
        fig = plt.figure(figsize = (10, 5))
        plt.bar(names, votes, color ='maroon')
        plt.xlabel("Names of candidates")
        plt.ylabel("No. of votes ")
        plt.title(f"{posn}")
        plt.show()      

        button=Button(text="next")  



def pie():
    pass


bar_button=Button(fra,text="Bar graph",command=lambda:[main_window.withdraw(),selector()],bg="white",height=2,width=10)
bar_button.pack(pady=5)
pie_button=Button(fra,text="Pie chart",command=lambda:[main_window.withdraw(),selector()],bg="white",height=2,width=10)
pie_button.pack(pady=5)





        


main_window.mainloop()


