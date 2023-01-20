from tkinter import *
import mysql.connector as broker
from tkinter import messagebox
import matplotlib.pyplot as plt
import random


mydb = broker.connect(host='localhost',user='root', password='tiger')
mycursor=mydb.cursor()


main_window = Tk()
main_window.title('ADMIN_CONTROL')
main_window.geometry("1080x720")
main_window.resizable(False,False)
main_window.configure(background='#181818')
main_window.option_add("*Font", ("Consolas Bold",14))
main_window.option_add("*Background", "#181818")
main_window.option_add("*Button.Background", "#404040")
main_window.option_add("*Button.foreground", "White")
main_window.option_add("*Label.foreground", "White")
main_window.option_add("*Text.foreground", "White")
main_window.option_add("*OptionMenu.foreground", "White")
main_window.option_add("*Entry.foreground", "White")


fra=Frame(main_window)
fra.pack(pady=50)

Label1=Label(fra,text="Election 2023",font=("Queental", 70)).pack()



Button(fra,text="Create posts",command=lambda:[creation()]).pack(padx=5,pady=10)
Button(fra,text="View result ",command=lambda:[result()]).pack(padx=5,pady=10)
Button(fra,text=" Delete all data",command=lambda:[delete()],bg="red").pack(padx=5,pady=10)
Button(fra,text=" Exit",command=main_window.destroy).pack(padx=5,pady=10)



posn=StringVar()
name=StringVar()

def creation():
    global newwindow

    newwindow=Toplevel()
    newwindow.title("Creator")
    newwindow.geometry('480x480')
    frame=Frame(newwindow)
    frame.pack(padx=10,pady=10,ipadx=10)   



    name_post_l = Label(master=frame , text="NAME OF THE POST").pack(pady = 10)
    Cd_posn=Entry(frame,textvariable=posn)
    Cd_posn.pack()


    name_post_name = Label(master=frame , text="NAME OF THE CANDIDATE").pack(pady = 10)
    Cd_name=Entry(frame,textvariable=name)
    Cd_name.pack()




    Button(frame,text="Add candidate",command=lambda:[add()]).pack(anchor=CENTER)
    Button(frame,text="Next position ",command=lambda:[nextpos()]).pack(anchor=CENTER)

    Button(frame,text="Close ",command=lambda:[newwindow_destroy()]).pack(anchor=CENTER)





    def add():
        

        mycursor.execute("Create database IF NOT EXISTS Electionsys")
        mycursor.execute("use Electionsys")   

        mycursor.execute("create table IF NOT EXISTS candidates(Cndt_Name char(20) unique,Position char(20),Vote_cnt int(3) default 0)")
         
        PositionName=posn.get()
        candidateName=name.get()

        if candidateName!="" or PositionName!="":
            sql='''Insert into candidates(Cndt_Name,Position) values(%s,%s)'''
        else:
            messagebox.showerror("Error","Candidate/Position name cannot be empty ")
            
        data=(candidateName,PositionName)
        try:
            mycursor.execute(sql,data)
        except broker.errors.IntegrityError:
            messagebox.showerror("Error",f"Candidate {candidateName} already exists" )



        mydb.commit()

        Cd_name.delete(0, END)
    def nextpos():
        Cd_posn.delete(0, END)
        Cd_name.delete(0, END)



def result():

    def rand(l):
        col=[]
        for i in range(l):
            color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
            col.append(color)
        return col

        

    mycursor.execute("use Electionsys")  
    mycursor.execute("Select Cndt_Name,position,vote_cnt from candidates")
    data=mycursor.fetchall()
    posn_list=[]
    grouped_list=[]
    for i in data:
        if i[1] not in posn_list:
            posn_list.append(i[1])

    for j in posn_list:
        for k in data:
            if k[1]==j:
                grouped_list.append(k)


    
    
    global newwindow

    newwindow=Toplevel()
    newwindow.geometry('480x480')
    frame=Frame(newwindow)
    frame.pack(padx=10,pady=10,ipadx=10)   




    newwindow.title(" Result ")

    proceed=IntVar()
    value=StringVar()
    d={}

        


    def bar_plotter():
        global newmain_window
        newmain_window=Toplevel(newwindow)
        newmain_window.geometry("400x400")
        newmain_window.configure(bg='#181818')

        
        def bar(posn):

            
                    

            names=[]
            votes=[]
            for name in grouped_list:
                if name[1]==posn:
                    names.append(name[0])
                    votes.append(name[2])   
            fig = plt.figure(figsize = (10, 5))
            plt.barh(names, votes)            
            plt.xlabel("Names of candidates")
            plt.ylabel("No. of votes ")
            plt.title(posn)
            for index, value in enumerate(votes):
                    plt.text(value, index,
                            str(value))

            plt.show()      
        
        
        button_dict={}
        fra=Frame(newmain_window)
        fra.pack(pady=50)
        fra.configure(bg='#181818')


        for i in range(len(posn_list)):
            def func(x=i):
                return bar(posn_list[x])
            
            
            button_dict[i]=Button(newmain_window, text=posn_list[i], command=func,height=2,width=10).pack(pady=5)
            

    def pie_plotter():
        global newmain_window
        newmain_window=Toplevel(main_window)
        newmain_window.geometry("400x400")
        
        newmain_window.configure(bg='#181818')

        def pie(posn):
            
            names=[]
            votes=[]
            
            for name in grouped_list:
                if name[1]==posn:
                    if name[2]!=0:
                        names.append(name[0])
                        votes.append(name[2]) 
            l=len(names)
            colV=rand(l)
            plt.pie(votes, startangle = 90,counterclock=False, shadow=True,autopct='%.1f%%',colors=colV)
            plt.title(posn)

            

            plt.legend(names,loc='upper left', frameon=False)
            plt.show()

        fra=Frame(newmain_window)
        fra.pack(pady=50)
        fra.configure(bg='#181818')

        button_dict={}
        for i in range(len(posn_list)):
            def func(x=i):
                return pie(posn_list[x])
            
            
            button_dict[i]=Button(newmain_window, text=posn_list[i], command=func,height=2,width=10).pack(pady=5)

        


    bar_button=Button(frame,text="Bar graph",command=lambda:[bar_plotter()],height=2,width=10)
    bar_button.pack(pady=5)
    pie_button=Button(frame,text="Pie chart",command=lambda:[pie_plotter()],height=2,width=10)
    pie_button.pack(pady=5)

def delete():
    answer=messagebox.askyesno(title="Confirmation",message="Are you sure you want to delete all Data (this cant be recovered)")
    if answer==True:
        main_window.destroy()
        mycursor.execute("Drop database Electionsys")
        
    else:
        pass
    
def newwindow_destroy():
    newwindow.destroy()


cred =Frame(main_window)
cred.pack(padx=10,pady=10,side=BOTTOM)
credit=Label(cred,text='''Project Done By: Adil Haneef M.K, Athul Krishna, Sreerag Unni N
                             \n KENDRIYA VIDYALAYA KALPETTA
                                        \nYear : 2022-2023''')
credit.pack(side='right',anchor='e')

main_window.mainloop()