from tkinter import *
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

#adding widgets 
main_window.title("Election system")
Label1=Label(main_window,text="Election 2023").pack(side=TOP)

proceed=IntVar()
value=StringVar()
d={}

def bar():
    global newWindow
    newWindow=Toplevel(main_window)
    newWindow.geometry("400x400")
    global posn
    
    names=[]
    votes=[]


    for posn in posn_list:
        
        for name in grouped_list:
            names.append(name[0])
            votes.append(name[2])

            fig = plt.figure(figsize = (10, 5))
 
            # creating the bar plot
            plt.bar(names, votes, color ='maroon')

            plt.xlabel("Names of candidates")
            plt.ylabel("No. of votes ")
            plt.title(f"{posn}")
            plt.show()
            

        

        
        
        save_button=Button(newWindow,text="Save vote",command=lambda:[newWindow.withdraw()])
        save_button.pack()
        save_button.wait_variable(proceed)


Button(text="Bar graph",command=lambda:[main_window.withdraw(),bar()]).pack(anchor=CENTER)
Button(text="Pie graph",command=lambda:[main_window.withdraw(),pie()]).pack(anchor=CENTER)



        


main_window.mainloop()


