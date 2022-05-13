from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk


def account():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.10, relheight=0.800, relwidth=.850)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.15, rely=0.105, relheight=0.8, relwidth=0.700)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#848884")
screen.configure(cursor="arrow")
          
sbmibtn=Button(screen,text='K:Company',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=account).place(x=20,y=10)
sbmibtn=Button(screen,text='Y:Data',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=180,y=10)
sbmibtn=Button(screen,text='Z:Exchange',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=340,y=10)
sbmibtn=Button(screen,text='G:Go To',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=600,y=10)
sbmibtn=Button(screen,text='O:Import',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=850,y=10)
sbmibtn=Button(screen,text='E;Export',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=990,y=10)
sbmibtn=Button(screen,text='M:E-mail',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1130,y=10)
sbmibtn=Button(screen,text='P:Print',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1270,y=10)
sbmibtn=Button(screen,text='F1:Help',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=1400,y=10)

global Canvas1
Canvas1 = tk.Canvas( background="#B0B0B0", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.800, relwidth=.850)
Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)


global Canvas4
Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas4.place(relx=0.01, rely=0.040, relheight=0.760, relwidth=0.650)
Label6 = Label(Canvas4,text='Name    ',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label6.place(relx=0.00, rely=0.010, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.2, rely=0.010, relheight=0.05, relwidth=0.300)
Label7 = Label(Canvas4,text='(alias)   ',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label7.place(relx=0.00, rely=0.070, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.2, rely=0.070, relheight=0.05, relwidth=0.300)
Label1 = Label(Canvas4,text='Under   :',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label1.place(relx=0.0, rely=0.250, relheight=0.05, relwidth=0.200)
Label1 = Label(Canvas4,text='Capital Account',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label1.place(relx=0.160, rely=0.250, relheight=0.05, relwidth=0.200)
Label8 = Label(Canvas4,text='Behaves like a sub-ledger',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label8.place(relx=0.0, rely=0.40, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.4, rely=0.400, relheight=0.05, relwidth=0.300)
Label3 = Label(Canvas4,text='Nett debit\credit card balance',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label3.place(relx=0.0, rely=0.460, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.4, rely=0.460, relheight=0.05, relwidth=0.300)
Label2 = Label(Canvas4,text='Used for calculation',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
Label2.place(relx=0.02, rely=0.520, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.4, rely=0.520, relheight=0.05, relwidth=0.300)
Label1 = Label(Canvas4,text='Method to allocate',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8")
Label1.place(relx=0.02, rely=0.580, relheight=0.05, relwidth=0.200)
Entry1 = Entry(Canvas4,width=28,borderwidth="3")
Entry1.place(relx=0.4, rely=0.580, relheight=0.05, relwidth=0.300)
sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(relx=0.6, rely=0.680)
sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(relx=0.8, rely=0.680)




# global Canvas2
# Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
# Canvas2.place(relx=0.330, rely=0.120, relheight=0.300, relwidth=0.350)
# Label5 = Label(Canvas2,text='List of groups',borderwidth="0", width=3, background="#3385ff",
#                                      foreground="#00254a",
#                                      font="-family {Segoe UI} -size 10 -weight bold ")
# Label5.place(relx=0, rely=0, relheight=0.3, relwidth=0.999)




global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)
screen.mainloop()
