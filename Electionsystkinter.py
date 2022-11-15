from tkinter import *

main_window=Tk()
'''widgets are added here '''

main_window.title("Election system")
main_window.geometry("200x300")

Label(main_window,text="Election 2023",bg = "red").grid()



Label(main_window,text="President").grid()
Radiobutton(main_window,text="Bruce wayne",value="Bw").grid()
Radiobutton(main_window,text="Matt Murdock",value="Mm").grid()

Label(main_window,text="Vice president").grid()
Radiobutton(main_window,text="Virat Kohli",value="Vk").grid()
Radiobutton(main_window,text="MS Dhoni",value="MSD").grid()

button=Button(main_window,text='Vote',width=25).grid()




main_window.mainloop()
