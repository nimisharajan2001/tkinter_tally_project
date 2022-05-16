from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk

def Stock_Query():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.110, relwidth=0.250)
    Label6 = Label(Canvas4,text='Name of item',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.400)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)


    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.142, relheight=0.300, relwidth=0.290)
    Label5 = Label(Canvas2,text='List of stock items',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.2, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Stock1',borderwidth="0",background="#fff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Stocks).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Stock2',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Stocks).place(relx=0,y=98,relwidth=0.250)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Selected_Stocks():
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    selected_groups_frame.place(x=0,y=0,width=1300,height=650)
    
    f1=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
    f1.place(x=0,y=0,width=1160,height=130)     

    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=0,y=130,width=580,height=20)
    #l1=Label(f14,text="Purchases",font=("times new roman",8,"bold"),bg="white",fg="black",borderwidth=5)
    #l1.place(x=100,y=0,anchor="nw")

    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f11.place(x=0,y=150,width=580,height=20)

    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=0,y=170,width=580,height=20)

    f13=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f13.place(x=0,y=190,width=580,height=190)

    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=0,y=380,width=580,height=20)

    f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f15.place(x=0,y=400,width=580,height=20)

    f16=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f16.place(x=0,y=420,width=580,height=178)
   
    f2=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f2.place(x=580,y=130,width=580,height=20)

    f21=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f21.place(x=580,y=150,width=580,height=20)

    f22=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f22.place(x=580,y=170,width=580,height=20)

    f23=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f23.place(x=580,y=190,width=580,height=190)

    f24=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f24.place(x=580,y=380,width=580,height=20)

    f25=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f25.place(x=580,y=400,width=580,height=20)

    f26=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f26.place(x=580,y=420,width=580,height=178)
   
    
    
def Movement_Analysis():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas5
    Canvas5 = tk.Canvas(background="#fff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas5.place(relx=0.680, rely=0.3, relheight=0.38, relwidth=0.150)
    Label5 = Label(Canvas5,text='Movement Analysis',borderwidth="0", width=3, background="#3385ff",
                                  foreground="#fff",
                                  font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.1, relwidth=0.999)
    btn2=Button(Canvas5,text='Stock Group Analysis',borderwidth="0",background="#fff",
                                    foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=58,relwidth=1)
    btn2=Button(Canvas5,text='Stock Category Analysis',borderwidth="0",background="#fff",
                                    foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=78,relwidth=1)
    btn2=Button(Canvas5,text='Stock item Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=98,relwidth=1)
    btn2=Button(Canvas5,text='Group Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Group_Analysis).place(relx=0,y=148,relwidth=1)
    btn2=Button(Canvas5,text='Ledger Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Ledger_Analysis).place(relx=0,y=168,relwidth=1)
    btn2=Button(Canvas5,text='Transfer Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Transfer_Analysis).place(relx=0,y=208,relwidth=1)
    btn2=Button(Canvas5,text='Quit',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=248,relwidth=1)
    
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)



def Group_Analysis():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.110, relwidth=0.250)
    Label6 = Label(Canvas4,text='Name of group',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.400)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)


    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.142, relheight=0.300, relwidth=0.290)
    Label5 = Label(Canvas2,text='List of groups',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.2, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Group1',borderwidth="0",background="#fff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=selected_groups).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Group2',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=selected_groups).place(relx=0,y=98,relwidth=0.250)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)


def create_group():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="white", relief="ridge",selectbackground="white", selectforeground="white")
    Canvas4.place(relx=0.01, rely=0.040, relheight=0.760, relwidth=0.650)
    Label6 = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label6.place(relx=0.00, rely=0.010, relheight=0.05, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.010, relheight=0.05, relwidth=0.300)
    Label7 = Label(Canvas4,text='(alias)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label7.place(relx=0.00, rely=0.070, relheight=0.05, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.070, relheight=0.05, relwidth=0.300)
    Label1 = Label(Canvas4,text='Under   :',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.250, relheight=0.05, relwidth=0.200)
    options_list = ["Group1", "Group2","Group3","Group4"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.250, relheight=0.05, relwidth=0.300)

    
    Label8 = Label(Canvas4,text='Behaves like a sub-ledger',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label8.place(relx=0.0, rely=0.400, relheight=0.05, relwidth=0.200)
    options_list = ["Yes", "No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.400, relheight=0.05, relwidth=0.300)

    Label3 = Label(Canvas4,text='Nett debit\credit card balance',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label3.place(relx=0.0, rely=0.460, relheight=0.05, relwidth=0.200)
    options_list = ["Yes", "No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.460, relheight=0.05, relwidth=0.300)

    Label2 = Label(Canvas4,text='Used for calculation',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label2.place(relx=0.02, rely=0.520, relheight=0.05, relwidth=0.200)
    options_list = ["Yes", "No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.520, relheight=0.05, relwidth=0.300)

    Label1 = Label(Canvas4,text='Method to allocate',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8")
    Label1.place(relx=0.02, rely=0.580, relheight=0.05, relwidth=0.200)
    options_list = ["Not Applicable", "Appropriate by Qty","Appropriate by Value"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.580, relheight=0.05, relwidth=0.300)

    sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(relx=0.6, rely=0.680)
    sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=Group_Analysis).place(relx=0.8, rely=0.680)


    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def selected_groups():
        global selected_groups_frame
        selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_groups_frame.place(x=0,y=0,width=1300,height=650)

        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=3,ipadx=208)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),fg="black",bg="white",borderwidth=0,relief=GROOVE,width=20,height=7)
        l1f1.pack(fill=X,pady=2,padx=2)
        f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=610,y=0,width=680,height=80)
        l1f2=Label(f12,text="Group Name",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=270,y=10,anchor="center")
        l1f3=Label(f12,text="Company Name",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=270,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=270,y=50,anchor="center")

        f13=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f13.place(x=0,y=145,width=607,height=420)
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt1.place(x=0,y=0,anchor="nw")
        f13bt2=Button(f13,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt2.place(x=0,y=30,anchor="nw")
        f13bt3=Button(f13,text="3",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt3.place(x=0,y=60,anchor="nw")
        f13bt4=Button(f13,text="4",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt4.place(x=0,y=90,anchor="nw")

        f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=609,y=83,width=273,height=58)
        l1f5=Label(f14,text="Purchases",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=100,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=80,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=180,y=30,anchor="nw")

        f15=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=883,y=83,width=275,height=58)
        l2f5=Label(f15,text="Sales",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=100,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=80,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=180,y=30,anchor="nw")

        f16=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f16.place(x=610,y=145,width=273,height=420)
        l3f6=Label(f16,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f6.place(x=0,y=0,anchor="nw")
        l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f7.place(x=80,y=0,anchor="nw")
        l3f8=Label(f16,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f8.place(x=180,y=0,anchor="nw")
        

        f17=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f17.place(x=883,y=145,width=275,height=420)
        l4f6=Label(f17,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f6.place(x=0,y=0,anchor="nw")
        l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f7.place(x=80,y=0,anchor="nw")
        l4f8=Label(f17,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f8.place(x=180,y=0,anchor="nw")


       
        f18=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=565,width=607,height=30)
        l5f6=Label(f18,text="Grand Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=0,y=0,anchor="nw")

        f19=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f19.place(x=610,y=565,width=273,height=30)
        l6f6=Label(f19,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f20.place(x=883,y=565,width=275,height=30)
        l7f6=Label(f20,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")

def Ledger_Analysis():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.110, relwidth=0.250)
    Label6 = Label(Canvas4,text='Name of Ledger',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.400)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)


    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.142, relheight=0.300, relwidth=0.290)
    Label5 = Label(Canvas2,text='List of Ledgers',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.2, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Ledger1',borderwidth="0",background="#fff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Ledgers).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Ledger2',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Ledgers).place(relx=0,y=98,relwidth=0.250)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Selected_Ledgers():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f11=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=3,ipadx=208)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),fg="black",bg="white",borderwidth=0,relief=GROOVE,width=20,height=7)
        l1f1.pack(fill=X,pady=2,padx=2)
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=610,y=0,width=680,height=80)
        l1f2=Label(f12,text="Ledger Name",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=270,y=10,anchor="center")
        l1f3=Label(f12,text="Company Name",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=270,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=270,y=50,anchor="center")

        f13=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f13.place(x=0,y=145,width=607,height=420)
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt1.place(x=0,y=0,anchor="nw")
        f13bt2=Button(f13,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt2.place(x=0,y=30,anchor="nw")
        f13bt3=Button(f13,text="3",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt3.place(x=0,y=60,anchor="nw")
        f13bt4=Button(f13,text="4",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt4.place(x=0,y=90,anchor="nw")

        f14=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=609,y=83,width=273,height=58)
        l1f5=Label(f14,text="Purchases",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=100,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=80,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=180,y=30,anchor="nw")

        f15=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=883,y=83,width=275,height=58)
        l2f5=Label(f15,text="Sales",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=100,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=80,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=180,y=30,anchor="nw")

        f16=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f16.place(x=610,y=145,width=273,height=420)
        l3f6=Label(f16,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f6.place(x=0,y=0,anchor="nw")
        l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f7.place(x=80,y=0,anchor="nw")
        l3f8=Label(f16,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f8.place(x=180,y=0,anchor="nw")
        
        f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f17.place(x=883,y=145,width=275,height=420)
        l4f6=Label(f17,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f6.place(x=0,y=0,anchor="nw")
        l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f7.place(x=80,y=0,anchor="nw")
        l4f8=Label(f17,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f8.place(x=180,y=0,anchor="nw")
      
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=565,width=607,height=30)
        l5f6=Label(f18,text="Grand Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=0,y=0,anchor="nw")

        f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f19.place(x=610,y=565,width=273,height=30)
        l6f6=Label(f19,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f20.place(x=883,y=565,width=275,height=30)
        l7f6=Label(f20,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")

def Transfer_Analysis():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.110, relwidth=0.250)
    Label6 = Label(Canvas4,text='Name of Voucher',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.400)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)


    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.142, relheight=0.300, relwidth=0.290)
    Label5 = Label(Canvas2,text='List of Voucher Types',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.2, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#fff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Stock Journal',borderwidth="0",background="#fff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Stock_Journal).place(relx=0,y=58,relwidth=0.250)
    
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Stock_Journal():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f11=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=3,ipadx=208)
        l1f1=Label(f11,text="Perticulars",font=("times new roman",12,"bold"),fg="black",bg="white",borderwidth=0,relief=GROOVE,width=20,height=7)
        l1f1.pack(fill=X,pady=2,padx=2)
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=610,y=0,width=680,height=80)
        l1f2=Label(f12,text="Stock Journal",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=270,y=10,anchor="center")
        l1f3=Label(f12,text="Company Name",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f3.place(x=270,y=30,anchor="center")
        l1f4=Label(f12,text="FOR 1-APR-20",font=("times new roman",9,"bold"),bg="white",fg="black")
        l1f4.place(x=270,y=50,anchor="center")

        f13=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f13.place(x=0,y=145,width=607,height=420)
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt1.place(x=0,y=0,anchor="nw")
        f13bt2=Button(f13,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt2.place(x=0,y=30,anchor="nw")
        f13bt3=Button(f13,text="3",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt3.place(x=0,y=60,anchor="nw")
        f13bt4=Button(f13,text="4",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0)
        f13bt4.place(x=0,y=90,anchor="nw")

        f14=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
        f14.place(x=609,y=83,width=273,height=58)
        l1f5=Label(f14,text="Goods In(Production)",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l1f5.place(x=60,y=0,anchor="nw")
        l1f6=Label(f14,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f6.place(x=0,y=30,anchor="nw")
        l1f7=Label(f14,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f7.place(x=80,y=30,anchor="nw")
        l1f8=Label(f14,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l1f8.place(x=180,y=30,anchor="nw")

        f15=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=1)
        f15.place(x=883,y=83,width=275,height=58)
        l2f5=Label(f15,text="Goods Out(Consumption)",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l2f5.place(x=40,y=0,anchor="nw")
        l2f6=Label(f15,text="Quantity",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f6.place(x=0,y=30,anchor="nw")
        l2f7=Label(f15,text="Eff.Rate",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f7.place(x=80,y=30,anchor="nw")
        l2f8=Label(f15,text="Value",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=0)
        l2f8.place(x=180,y=30,anchor="nw")

        f16=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f16.place(x=610,y=145,width=273,height=420)
        l3f6=Label(f16,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f6.place(x=0,y=0,anchor="nw")
        l3f7=Label(f16,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f7.place(x=80,y=0,anchor="nw")
        l3f8=Label(f16,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l3f8.place(x=180,y=0,anchor="nw")
        
        f17=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f17.place(x=883,y=145,width=275,height=420)
        l4f6=Label(f17,text="5 BTL",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f6.place(x=0,y=0,anchor="nw")
        l4f7=Label(f17,text="10",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f7.place(x=80,y=0,anchor="nw")
        l4f8=Label(f17,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l4f8.place(x=180,y=0,anchor="nw")
      
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=565,width=607,height=30)
        l5f6=Label(f18,text="Grand Total",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=0,y=0,anchor="nw")

        f19=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f19.place(x=610,y=565,width=273,height=30)
        l6f6=Label(f19,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l6f6.place(x=0,y=0,anchor="nw")

        f20=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f20.place(x=883,y=565,width=275,height=30)
        l7f6=Label(f20,text="50",font=("times new roman",12,"bold"),bg="white",fg="black",borderwidth=0)
        l7f6.place(x=0,y=0,anchor="nw")

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
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(x=20,y=10)
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
Label5 = Label(Canvas1,text='Gateway of Tally',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)



global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)

global Canvas4
Canvas4 = tk.Canvas(background="#fff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas4.place(relx=0.680, rely=0.3, relheight=0.35, relwidth=0.150)
Label5 = Label(Canvas4,text='Statements of Inventory',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.1, relwidth=0.999)
btn2=Button(Canvas4,text='STock Query',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Stock_Query).place(relx=0,y=68,relwidth=1)
btn2=Button(Canvas4,text='Movement Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Movement_Analysis).place(relx=0,y=108,relwidth=1)
btn2=Button(Canvas4,text='Ageing Analysis',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Selected_Ledgers).place(relx=0,y=138,relwidth=1)
btn2=Button(Canvas4,text='Cost Estimation',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Group_Analysis).place(relx=0,y=178,relwidth=1)
btn2=Button(Canvas4,text='Quit',borderwidth="0",background="#fff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=218,relwidth=1)



screen.mainloop()
