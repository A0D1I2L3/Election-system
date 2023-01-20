from tkinter import *
import mysql.connector as broker


mydb = broker.connect(host='192.168.1.62',user='chomu', password='tiger')
mycursor=mydb.cursor()
mycursor.execute("Use electionsys")

mycursor.execute("Select Cndt_Name,position from candidates")
data=mycursor.fetchall()

main_window = Tk()
main_window.title('Voter module')
main_window.geometry("1080x720")
main_window.resizable(False,False)
main_window.configure(background='#181818')
main_window.option_add("*Font", ("Consolas Bold",14))
main_window.option_add("*Background", "#181818")
main_window.option_add("*Button.Background", "White")
main_window.option_add("*Button.foreground", "Black")
main_window.option_add("*Label.foreground", "White")
main_window.option_add("*Text.foreground", "Black")
main_window.option_add("*OptionMenu.foreground", "White")
main_window.option_add("*Entry.foreground", "White")
main_window.option_add("*Radiobutton.foreground", "White")


proceed=IntVar()
value=StringVar()

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

def next_main_window(posn):
    
    main_window=Toplevel(newmain_window)
    main_window.geometry("400x300")
    
    Label(main_window,text=f"{posn}").pack(ipadx=5,ipady=5)

    for name in grouped_list:
        if name[1]==posn:
            Radiobutton(main_window,text=f"{name[0]}",variable = value,value=f"{name[0]}").pack(ipadx=5,ipady=10)
    save_button=Button(main_window,text="Save vote",command=lambda:[main_window.destroy(),vote()])
    save_button.pack()
    save_button.wait_variable(proceed)

def vote():
    votevalue=(value.get(),)
    sql='''update candidates set Vote_cnt=Vote_cnt+1 where Cndt_Name=%s'''
    mycursor.execute(sql,votevalue)
    
    global posn

    try :
        posn=posn_list[(posn_list.index(posn))+1]
        next_main_window(posn)
    except IndexError:
        pass
    
    mydb.commit()



def start():
    global newmain_window
    newmain_window=Toplevel(main_window)
    newmain_window.geometry("400x400")
    global posn

    for posn in posn_list:
        Label(newmain_window,text=f"{posn}").pack(ipadx=5,ipady=5)

        for name in grouped_list:
            if name[1]==posn:
                Radiobutton(newmain_window,text=f"{name[0]}",variable = value,value=f"{name[0]}").pack(ipadx=5,ipady=10)

        save_button=Button(newmain_window,text="Save vote",command=lambda:[newmain_window.withdraw(),vote()])
        save_button.pack()
        save_button.wait_variable(proceed)


Button(text="Start voting",command=lambda:[main_window.withdraw(),start()]).pack(pady=20)


main_window.mainloop()