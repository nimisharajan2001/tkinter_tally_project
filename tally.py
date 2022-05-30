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
    Label6 = Label(Canvas1,text='Select Stock Item',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a", anchor='nw',
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)
   
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                        foreground="#00254a",anchor='n',
                                        font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of item',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.400)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)


    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of stock items',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Create_Stock).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Stock1',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Stocks).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Stock2',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Stocks).place(relx=0,y=98,relwidth=0.250)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Create_Stock():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="white", relief="ridge",selectbackground="white", selectforeground="white")
    Canvas4.place(relx=0.01, rely=0.040, relheight=0.760, relwidth=0.650)
    Label6 = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label6.place(relx=0.00, rely=0.010, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.010, relheight=0.04, relwidth=0.300)
    Label7 = Label(Canvas4,text='(alias)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label7.place(relx=0.00, rely=0.070, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.070, relheight=0.04, relwidth=0.300)
    
    Label8 = Label(Canvas4,text='Under',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label8.place(relx=0.0, rely=0.310, relheight=0.04, relwidth=0.200)
    options_list = ["Primary","Group1", "Group2", "Group3", "Group4"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.2, rely=0.310, relheight=0.04, relwidth=0.250)

    Label9 = Label(Canvas4,text='Units',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.370, relheight=0.04, relwidth=0.200)
    options_list = ["Not Applicable","Unit1"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.2, rely=0.370, relheight=0.04, relwidth=0.250)

    Label0 = Label(Canvas4,text='Statutory Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 10 -weight bold")
    Label0.place(relx=0.480, rely=0.300, relheight=0.04, relwidth=0.200)
    Lab = Label(Canvas4,text='GST Applicable',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab.place(relx=0.480, rely=0.380, relheight=0.04, relwidth=0.200)
    options_list = ["Applicable","Not Applicable", "Undefined"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.680, rely=0.380, relheight=0.04, relwidth=0.250)
    Lab1 = Label(Canvas4,text='Set/Alter GST deetails',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.480, rely=0.440, relheight=0.04, relwidth=0.200)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.680, rely=0.440, relheight=0.04, relwidth=0.250)
    Lab1 = Label(Canvas4,text='Type of supply',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.480, rely=0.500, relheight=0.04, relwidth=0.200)
    options_list = ["Goods","Services"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.680, rely=0.500, relheight=0.04, relwidth=0.250)
    Lab2 = Label(Canvas4,text='Rate of Duty(eg 5)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab2.place(relx=0.480, rely=0.560, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.680, rely=0.560, relheight=0.04, relwidth=0.250)
    

    sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(relx=0.6, rely=0.720)
    sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=Stock_Query).place(relx=0.8, rely=0.720)
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Selected_Stocks():
    global selected_groups_frame
    selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
    selected_groups_frame.place(x=0,y=0,width=1300,height=650)
    
    f1=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
    f1.place(x=0,y=0,width=1160,height=130)
    l1f2=Label(f1,text="Name",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=0,y=0)
    l1f2=Label(f1,text=": Product",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=120,y=0)
    l1=Label(f1,text="Group",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l1.place(x=0,y=20)
    l1=Label(f1,text=": Primary",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1.place(x=120,y=20)
    l1f3=Label(f1,text="Clossing Balance",font=("times new roman",9),bg="white",fg="black")
    l1f3.place(x=0,y=40)
    l1f3=Label(f1,text=" :",font=("times new roman",9,"bold"),bg="white",fg="black")
    l1f3.place(x=120,y=40)
    f3=Label(f1,text="Cost Price",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    f3.place(x=0,y=60)
    f3=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    f3.place(x=120,y=60)
    f4=Label(f1,text="Costing Method",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    f4.place(x=0,y=80)
    f4=Label(f1,text=": Default",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    f4.place(x=120,y=80)
    f4=Label(f1,text="Standard Cost",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    f4.place(x=0,y=100)
    f4=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    f4.place(x=120,y=100)

    l1f2=Label(f1,text="Part No",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=600,y=0)
    l1f2=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l1f2.place(x=740,y=0)
    l3=Label(f1,text="Category",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l3.place(x=600,y=20)
    l3=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l3.place(x=740,y=20)
    l4=Label(f1,text="Clossing Value",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l4.place(x=600,y=40)
    l4=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l4.place(x=740,y=40)
    l5=Label(f1,text="Standard selling price",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l5.place(x=600,y=60)
    l5=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l5.place(x=740,y=60)
    l5=Label(f1,text="Market valuation method",font=("times new roman",9),bg="white",fg="black",borderwidth=5)
    l5.place(x=600,y=80)
    l5=Label(f1,text=":",font=("times new roman",9,"bold"),bg="white",fg="black",borderwidth=5)
    l5.place(x=740,y=80)


    f14=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f14.place(x=0,y=120,width=580,height=25)
    l2=Label(f14,text="Purchases",font=("times new roman",7,"bold"),bg="white",fg="black",borderwidth=5)
    l2.place(x=250,y=0)
    
    f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f11.place(x=0,y=155,width=580,height=25)

    f12=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=1)
    f12.place(x=0,y=175,width=580,height=20)

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
    Canvas5 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas5.place(relx=0.680, rely=0.3, relheight=0.38, relwidth=0.150)
    Label5 = Label(Canvas5,text='Movement Analysis',borderwidth="0", width=3, background="#3385ff",
                                  foreground="#fff",
                                  font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.1, relwidth=0.999)
    btn2=Button(Canvas5,text='Stock Group Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                    foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=58,relwidth=1)
    btn2=Button(Canvas5,text='Stock Category Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                    foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=78,relwidth=1)
    btn2=Button(Canvas5,text='Stock item Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=98,relwidth=1)
    btn2=Button(Canvas5,text='Group Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Group_Analysis).place(relx=0,y=148,relwidth=1)
    btn2=Button(Canvas5,text='Ledger Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Ledger_Analysis).place(relx=0,y=168,relwidth=1)
    btn2=Button(Canvas5,text='Transfer Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Transfer_Analysis).place(relx=0,y=208,relwidth=1)
    btn2=Button(Canvas5,text='Quit',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
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
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of group',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.500)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of groups',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Group1',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=selected_groups).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Group2',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
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
    cmb.place(relx=0.2, rely=0.250, relheight=0.05, relwidth=0.300)

    
    Label8 = Label(Canvas4,text='Group behaves like a sub-ledger',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label8.place(relx=0.0, rely=0.400, relheight=0.05, relwidth=0.350)
    options_list = ["Yes", "No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.400, relheight=0.05, relwidth=0.300)

    Label3 = Label(Canvas4,text='Nett Debit\Credit Balance for Reporting',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label3.place(relx=0.0, rely=0.460, relheight=0.05, relwidth=0.400)
    options_list = ["Yes", "No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.4, rely=0.460, relheight=0.05, relwidth=0.300)

    Label2 = Label(Canvas4,text='Used for calculation(for examples:taxes,discounts)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label2.place(relx=0.02, rely=0.520, relheight=0.05, relwidth=0.400)
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
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0,command=Selected_groups_row)
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

def Selected_groups_row():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=0,y=0,width=1170,height=130)
        f2=Label(f12,text="Purchases",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=820,y=0)

        f2=Label(f12,text="Date",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=420,y=60)
        f2=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=500,y=60)
        
        l1f2=Label(f12,text="No",font=("times new roman",10),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=0,y=20)
        l1=Label(f12,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        l1.place(x=120,y=20)
        l1f3=Label(f12,text="Date:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=40)
        f3=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=40)
        l1f3=Label(f12,text="Supplier invoice no:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=60)
        f3=Label(f12,text="W",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=60)
        l1f3=Label(f12,text="Party ledger A/c:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=80)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=80)
        l1f3=Label(f12,text="Current Balance:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=100)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=100)
        
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=130,width=1170,height=30)
        l5f6=Label(f18,text="Name of item",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=100,y=0)
        f6=Label(f18,text="Quantity",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=860,y=0)
        f6=Label(f18,text="Rate",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=930,y=0)
        f61=Label(f18,text="Cost",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f61.place(x=1000,y=0)
        f62=Label(f18,text="Amount",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f62.place(x=1070,y=0)


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
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of Ledger',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.500)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of Ledgers',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Create_Ledger).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Ledger1',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Ledgers).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Ledger2',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Ledgers).place(relx=0,y=98,relwidth=0.250)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Create_Ledger():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="white", relief="ridge",selectbackground="white", selectforeground="white")
    Canvas4.place(relx=0.01, rely=0.040, relheight=0.920, relwidth=0.850)
    Label6 = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label6.place(relx=0.00, rely=0.010, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.010, relheight=0.04, relwidth=0.220)
    Label7 = Label(Canvas4,text='(alias)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label7.place(relx=0.00, rely=0.050, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.050, relheight=0.04, relwidth=0.220)
    
    Label8 = Label(Canvas4,text='Under',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label8.place(relx=0.0, rely=0.220, relheight=0.04, relwidth=0.200)
    options_list = ["Primary","Group1", "Group2", "Group3", "Group4"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.25, rely=0.220, relheight=0.04, relwidth=0.220)

    Label5 = Label(Canvas4,text='Bank Account Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 10 -weight bold")
    Label5.place(relx=0.060, rely=0.300, relheight=0.04, relwidth=0.200)

    Label9 = Label(Canvas4,text='A\c Holders Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.370, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.370, relheight=0.04, relwidth=0.220)

    Label9 = Label(Canvas4,text='A\c No',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.420, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.420, relheight=0.04, relwidth=0.220)

    Label9 = Label(Canvas4,text='IFS Code',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.470, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.470, relheight=0.04, relwidth=0.220)

    Label9 = Label(Canvas4,text='SWIFT Code',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.520, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.520, relheight=0.04, relwidth=0.220)

    Lab = Label(Canvas4,text='Bank Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab.place(relx=0.0, rely=0.570, relheight=0.04, relwidth=0.200)
    options_list = ["Not Applicable", "Bank1","Bank2"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.25, rely=0.570, relheight=0.04, relwidth=0.220)

    Label9 = Label(Canvas4,text='Bank Branch',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label9.place(relx=0.0, rely=0.620, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.620, relheight=0.04, relwidth=0.220)

    Label5 = Label(Canvas4,text='Bank Configuration',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 10 -weight bold")
    Label5.place(relx=0.040, rely=0.670, relheight=0.04, relwidth=0.200)

    Lab1 = Label(Canvas4,text='Set/Alter range for Cheque Books',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.0, rely=0.720, relheight=0.04, relwidth=0.200)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.25, rely=0.720, relheight=0.04, relwidth=0.220)

    Lab1 = Label(Canvas4,text='Enable Cheque Printing',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.0, rely=0.770, relheight=0.04, relwidth=0.200)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.25, rely=0.770, relheight=0.04, relwidth=0.220)

    Lab1 = Label(Canvas4,text='Set/Alter Cheque Printing Configuration' ,borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.0, rely=0.820, relheight=0.04, relwidth=0.220)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.25, rely=0.820, relheight=0.04, relwidth=0.220)
    
    Label0 = Label(Canvas4,text='Mailing Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 10 -weight bold")
    Label0.place(relx=0.480, rely=0.300, relheight=0.04, relwidth=0.200)
    Lab = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab.place(relx=0.480, rely=0.380, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.680, rely=0.380, relheight=0.04, relwidth=0.250)

    Lab = Label(Canvas4,text='Address',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab.place(relx=0.480, rely=0.430, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.680, rely=0.430, relheight=0.04, relwidth=0.250)
    
    
    Lab1 = Label(Canvas4,text='State',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.480, rely=0.530, relheight=0.04, relwidth=0.200)
    options_list = ["Not Applicable","State1","State2","State3"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.680, rely=0.530, relheight=0.04, relwidth=0.250)

    Lab1 = Label(Canvas4,text='Country',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab1.place(relx=0.480, rely=0.580, relheight=0.04, relwidth=0.200)
    options_list = ["Not Applicable","Country1","Country2","Country3"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.680, rely=0.580, relheight=0.04, relwidth=0.250)
    
    Lab2 = Label(Canvas4,text='Pincode',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab2.place(relx=0.480, rely=0.630, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.680, rely=0.630, relheight=0.04, relwidth=0.250)
     
    Label0 = Label(Canvas4,text='Tax Registration Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 10 -weight bold")
    Label0.place(relx=0.480, rely=0.700, relheight=0.04, relwidth=0.200)
    Lab2 = Label(Canvas4,text='GSTIN/UIN',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Lab2.place(relx=0.480, rely=0.780, relheight=0.04, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.680, rely=0.780, relheight=0.04, relwidth=0.250)
    
    sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ").place(relx=0.6, rely=0.890)
    sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=10,font="-family {Segoe UI} -size 12 -weight bold ",command=Ledger_Analysis).place(relx=0.8, rely=0.890)
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
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0,command=Selected_ledgers_row)
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

def Selected_ledgers_row():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=0,y=0,width=1170,height=130)
        f2=Label(f12,text="Purchases",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=820,y=0)

        f2=Label(f12,text="Date",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=420,y=60)
        f2=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=500,y=60)
        
        l1f2=Label(f12,text="No",font=("times new roman",10),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=0,y=20)
        l1=Label(f12,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        l1.place(x=120,y=20)
        l1f3=Label(f12,text="Date:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=40)
        f3=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=40)
        l1f3=Label(f12,text="Supplier invoice no:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=60)
        f3=Label(f12,text="W",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=60)
        l1f3=Label(f12,text="Party ledger A/c:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=80)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=80)
        l1f3=Label(f12,text="Current Balance:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=100)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=100)
        
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=130,width=1170,height=30)
        l5f6=Label(f18,text="Name of item",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=100,y=0)
        f6=Label(f18,text="Quantity",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=860,y=0)
        f6=Label(f18,text="Rate",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=930,y=0)
        f61=Label(f18,text="Cost",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f61.place(x=1000,y=0)
        f62=Label(f18,text="Amount",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f62.place(x=1070,y=0)


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
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of Voucher',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.20, rely=0.20, relheight=0.30, relwidth=0.600)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of Voucher Types',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Create_Ledger).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Stock Journal',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Stock_Journal).place(relx=0,y=58,relwidth=0.350)
    
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
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0,command=Selected_transfers_row)
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

def Selected_transfers_row():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=0,y=0,width=1170,height=130)
        f2=Label(f12,text="Sales",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=820,y=0)

        f2=Label(f12,text="Date",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=420,y=60)
        f2=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=500,y=60)
        
        l1f2=Label(f12,text="No",font=("times new roman",10),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=0,y=20)
        l1=Label(f12,text="2",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        l1.place(x=120,y=20)
        l1f3=Label(f12,text="Date:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=40)
        f3=Label(f12,text="1-Apr-22",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=40)
        l1f3=Label(f12,text="Supplier invoice no:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=60)
        f3=Label(f12,text="W",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=60)
        l1f3=Label(f12,text="Party ledger A/c:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=80)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=80)
        l1f3=Label(f12,text="Current Balance:",font=("times new roman",10),bg="white",fg="black")
        l1f3.place(x=0,y=100)
        f3=Label(f12,text="",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=120,y=100)
        
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=130,width=1170,height=30)
        l5f6=Label(f18,text="Name of item",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=100,y=0)
        f6=Label(f18,text="Quantity",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=860,y=0)
        f6=Label(f18,text="Rate",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=930,y=0)
        f61=Label(f18,text="Cost",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f61.place(x=1000,y=0)
        f62=Label(f18,text="Amount",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f62.place(x=1070,y=0)

def Ageing_Analysis():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of group',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.500)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of Stock Groups',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_age_group).place(relx=0.6,y=38,relwidth=0.350)
    btn1=Button(Canvas2,text='Stock1',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=selected_age_groups).place(relx=0,y=58,relwidth=0.250)
    btn2=Button(Canvas2,text='Stock2',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=selected_age_groups).place(relx=0,y=98,relwidth=0.250)
   
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def create_age_group():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="white", relief="ridge",selectbackground="white", selectforeground="white")
    Canvas4.place(relx=0.01, rely=0.040, relheight=0.460, relwidth=0.450)
    Label6 = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label6.place(relx=0.00, rely=0.010, relheight=0.07, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.010, relheight=0.07, relwidth=0.350)
    Label7 = Label(Canvas4,text='(alias)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label7.place(relx=0.00, rely=0.080, relheight=0.07, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.080, relheight=0.07, relwidth=0.350)
    Label1 = Label(Canvas4,text='Under',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.260, relheight=0.07, relwidth=0.200)
    options_list = ["Primary","Group1", "Group2","Group3","Group4"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.2, rely=0.260, relheight=0.07, relwidth=0.350)
    
    Label1 = Label(Canvas4,text='Should quantities of items to be added',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.450, relheight=0.07, relwidth=0.400)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.5, rely=0.450, relheight=0.07, relwidth=0.350)

    Label1 = Label(Canvas4,text='Set/Alter GST Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.550, relheight=0.07, relwidth=0.400)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.5, rely=0.550, relheight=0.07, relwidth=0.350)
   

    sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=8,font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.6, rely=0.720)
    sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=8,font="-family {Segoe UI} -size 10 -weight bold ",command=Ageing_Analysis).place(relx=0.8, rely=0.720)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def selected_age_groups():
        global selected_groups_frame
        selected_groups_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_groups_frame.place(x=0,y=0,width=1300,height=650)
        #f5=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        #f5.grid(row=1,column=0,columnspan=3,ipadx=208)
        #l1f1=Label(f5,text="Perticulars",font=("times new roman",12,"bold"),fg="black",bg="white",borderwidth=0,relief=GROOVE,width=20,height=7)
        #l1f1.pack(fill=X,pady=2,padx=2)
        
        f11=Frame(selected_groups_frame,bg="white",relief=RAISED,bd=2)
        f11.grid(row=1,column=0,columnspan=6,ipadx=485)
        l1f1=Label(f11,text="It's Under:",font=("times new roman",12,"bold"),fg="black",bg="white",borderwidth=0,relief=GROOVE,width=20,height=7)
        l1f1.pack(fill=X,pady=0,padx=0,anchor="nw")
        #l1f1.place(x=0,y=0,anchor="nw")
       
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

def Cost_Estimation():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)
    Label5 = Label(Canvas1,text='Company name',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas4.place(relx=0.380, rely=0.0300, relheight=0.100, relwidth=0.180)
    Label6 = Label(Canvas4,text='Name of group',borderwidth="0", width=7, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label6.place(relx=0.25, rely=0.20, relheight=0.30, relwidth=0.500)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.25, rely=0.60, relheight=0.30, relwidth=0.500)

    global Canvas2
    Canvas2 = tk.Canvas(Canvas1, background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas2.place(relx=0.360, rely=0.120, relheight=0.900, relwidth=0.220)
    Label5 = Label(Canvas2,text='List of Stock Groups',borderwidth="0", width=3, background="#3385ff",
                                    foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
    Label5.place(relx=0, rely=0, relheight=0.04, relwidth=0.999)
    btn=Button(Canvas2,text='Create',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=create_cost_estimation).place(relx=0.6,y=30,relwidth=0.350)
    btn1=Button(Canvas2,text='Group1',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                   foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Estimations).place(relx=0,y=50,relwidth=0.250)
    btn2=Button(Canvas2,text='Group2',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=9,font="-family {Segoe UI} -size 10 ",command=Selected_Estimations).place(relx=0,y=70,relwidth=0.250)
   
    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def create_cost_estimation():
    global Canvas1
    Canvas1 = tk.Canvas( background="#B0B0B0", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas1.place(relx=0, rely=0.070, relheight=0.800, relwidth=.850)

    global Canvas4
    Canvas4 = tk.Canvas(Canvas1, background="#ffffff", insertbackground="white", relief="ridge",selectbackground="white", selectforeground="white")
    Canvas4.place(relx=0.01, rely=0.040, relheight=0.460, relwidth=0.450)
    Label6 = Label(Canvas4,text='Name',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label6.place(relx=0.00, rely=0.010, relheight=0.07, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.010, relheight=0.07, relwidth=0.350)
    Label7 = Label(Canvas4,text='(alias)',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label7.place(relx=0.00, rely=0.080, relheight=0.07, relwidth=0.200)
    Entry1 = Entry(Canvas4,width=28,borderwidth="3")
    Entry1.place(relx=0.2, rely=0.080, relheight=0.07, relwidth=0.350)
    Label1 = Label(Canvas4,text='Under',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.260, relheight=0.07, relwidth=0.200)
    options_list = ["Primary","Group1", "Group2","Group3","Group4"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.2, rely=0.260, relheight=0.07, relwidth=0.350)
    
    Label1 = Label(Canvas4,text='Should quantities of items to be added',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.450, relheight=0.07, relwidth=0.400)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.5, rely=0.450, relheight=0.07, relwidth=0.350)

    Label1 = Label(Canvas4,text='Set/Alter GST Details',borderwidth="0", width=7, background="white",foreground="#00254a",
        font="-family {Segoe UI} -size 8 ")
    Label1.place(relx=0.0, rely=0.550, relheight=0.07, relwidth=0.400)
    options_list = ["Yes","No"]
    cmb=ttk.Combobox(Canvas4,values=options_list,font=("times new roman",10))
    cmb.place(relx=0.5, rely=0.550, relheight=0.07, relwidth=0.350)

    sbmibtn=Button(Canvas4,text='Save',borderwidth="0",background="#023047",
                                     foreground="white",width=8,font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.6, rely=0.720)
    sbmibtn=Button(Canvas4,text='Exit',borderwidth="0",background="#023047",
                                     foreground="white",width=8,font="-family {Segoe UI} -size 10 -weight bold ",command=Cost_Estimation).place(relx=0.8, rely=0.720)

    global Canvas3
    Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
    Canvas3.place(relx=0.850, rely=0.100, relheight=0.8, relwidth=0.150)

def Selected_Estimations():
        global selected_ledgers_frame
        selected_ledgers_frame=Frame(Canvas1,bg="white",relief=RAISED,bd=2)
        selected_ledgers_frame.place(x=0,y=0,width=1300,height=650)
        
        f12=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f12.place(x=0,y=0,width=1170,height=80)
        f2=Label(f12,text="as at 1-Apr-22",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        f2.place(x=1050,y=5)
        l1f2=Label(f12,text="Items Under:",font=("times new roman",11),bg="white",fg="black",borderwidth=5)
        l1f2.place(x=0,y=5)
        l1=Label(f12,text="Group",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        l1.place(x=100,y=5)
        l1f3=Label(f12,text="BoM Type:",font=("times new roman",11),bg="white",fg="black")
        l1f3.place(x=0,y=30)
        f3=Label(f12,text="Default",font=("times new roman",11,"bold"),bg="white",fg="black",borderwidth=5)
        f3.place(x=100,y=30)
        
        f18=Frame(selected_ledgers_frame,bg="white",relief=RAISED,bd=2)
        f18.place(x=0,y=80,width=1170,height=30)
        l5f6=Label(f18,text="Particulars",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        l5f6.place(x=100,y=0)
        f6=Label(f18,text="Qty",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f6.place(x=930,y=0)
        f61=Label(f18,text="Cost",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f61.place(x=1000,y=0)
        f62=Label(f18,text="Amount",font=("times new roman",10),bg="white",fg="black",borderwidth=0)
        f62.place(x=1070,y=0)


def purchases_sales():
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
        f13bt1=Button(f13,text="1",font=("times new roman",10,"bold"),bg="white",fg="black",borderwidth=0,command=Selected_groups_row)
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
                                     foreground="#00254a", anchor='w',
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)



global Canvas3
Canvas3 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.8, relwidth=0.150)

global Canvas4
Canvas4 = tk.Canvas(background="#e6ffff", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas4.place(relx=0.680, rely=0.3, relheight=0.35, relwidth=0.150)
Label5 = Label(Canvas4,text='Statements of Inventory',borderwidth="0", width=3, background="#3385ff",
                                     foreground="#fff",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.1, relwidth=0.999)
btn2=Button(Canvas4,text='STock Query',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Stock_Query).place(relx=0,y=68,relwidth=1)
btn2=Button(Canvas4,text='Movement Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Movement_Analysis).place(relx=0,y=108,relwidth=1)
btn2=Button(Canvas4,text='Ageing Analysis',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Ageing_Analysis).place(relx=0,y=138,relwidth=1)
btn2=Button(Canvas4,text='COst Estimation',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ",command=Cost_Estimation).place(relx=0,y=178,relwidth=1)
btn2=Button(Canvas4,text='Quit',borderwidth="0",background="#e6ffff",activebackground="#e6ffff",
                                     foreground="black",width=100,font="-family {Segoe UI} -size 10 ").place(relx=0,y=218,relwidth=1)



screen.mainloop()
