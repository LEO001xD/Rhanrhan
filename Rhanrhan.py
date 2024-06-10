#นภัสกรณ์ โพธิ์หล้า 
#gui ร้านอาหารตามสั่ง
from tkinter import *
from tkinter import messagebox

#set 
root = Tk()
root.title("Rharntamsung")
root.geometry("843x720")
#==========================================================================================================================================
#Title
frame_title = Frame(width=1200,height=100,relief=RAISED)
frame_title.pack(side=TOP)
title=Label(frame_title,text="Cooked to order dish",font=('arial',40,"bold"),relief=RAISED,bd=13,bg="light goldenrod",fg="mediumpurple3",padx=145)
title.grid(row=0,column=0)
#==========================================================================================================================================
#background
frame_back = Frame(width=1200,height=600,relief=RAISED,bd=9,bg="salmon")
frame_back.pack()
#==========================================================================================================================================
#MENU
frame_MENU = Frame(frame_back,width=400,height=800,relief=RAISED,bd=9,bg="#FFBF93")
frame_MENU.pack(side=LEFT)
menu=Label(frame_MENU,text="MENU",font=('arial',20,"bold"),relief=RAISED,bd=5,bg="sea green",fg="white",padx=160)
menu.grid(row=0,column=0)

#==========================================================================================================================================
#variable kraw praw
varkraprawmoo=IntVar()
checkkraprawmoo=IntVar()
varkraprawmoo.set("0")

varkraprawgai=IntVar()
checkkraprawgai=IntVar()
varkraprawgai.set("0")

varkraprawmookrob=IntVar()
checkkraprawmookrob=IntVar()
varkraprawmookrob.set("0")
def chkbt_kpm():#moo
    if checkkraprawmoo.get() == 1:
        kraprawmoo.configure(state=NORMAL)
        varkraprawmoo.set("")
    elif checkkraprawmoo.get() == 0:
        kraprawmoo.configure(state=DISABLED)
        varkraprawmoo.set("0")

def chkbt_kpg():#gaI
    if checkkraprawgai.get() == 1:
        kraprawgai.configure(state=NORMAL)
        varkraprawgai.set("")
    elif checkkraprawgai.get() == 0:
        kraprawgai.configure(state=DISABLED)
        varkraprawgai.set("0")

def chkbt_kpmk():#mookrob
    if checkkraprawmookrob.get() == 1:
        kraprawmookrob.configure(state=NORMAL)
        varkraprawmookrob.set("")
    elif checkkraprawmookrob.get() == 0:
        kraprawmookrob.configure(state=DISABLED)
        varkraprawmookrob.set("0")

kraprawmootik=Checkbutton(frame_MENU,text="Padkrapraw  moosub       ฿30  ",variable=checkkraprawmoo,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#14659C",command=chkbt_kpm)
kraprawmootik.grid(row=1,column=0,sticky=W)
kraprawmoo=Entry(frame_MENU,textvariable=varkraprawmoo,font=('arial',15,"bold"),width=5,state= DISABLED)
kraprawmoo.grid(row=1,column=0,sticky=E,padx=5)

kraprawgaitik=Checkbutton(frame_MENU,text="Padkrapraw  gai\t           ฿30  ",variable=checkkraprawgai,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#14659C",command=chkbt_kpg)
kraprawgaitik.grid(row=2,column=0,sticky=W)
kraprawgai=Entry(frame_MENU,textvariable=varkraprawgai,font=('arial',15,"bold"),width=5,state= DISABLED)
kraprawgai.grid(row=2,column=0,sticky=E,padx=5)

kraprawmookrobtik=Checkbutton(frame_MENU,text="Padkrapraw  mookrob     ฿40  ",variable=checkkraprawmookrob,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#14659C",command=chkbt_kpmk)
kraprawmookrobtik.grid(row=3,column=0,sticky=W)
kraprawmookrob=Entry(frame_MENU,textvariable=varkraprawmookrob,font=('arial',15,"bold"),width=5,state= DISABLED)
kraprawmookrob.grid(row=3,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#kaopad
varkaopadmoo=IntVar()
checkkaopadmoo=IntVar()
varkaopadmoo.set("0")

varkaopadgai=IntVar()
checkkaopadgai=IntVar()
varkaopadgai.set("0")

varkaopadpoo=IntVar()
checkkaopadpoo=IntVar()
varkaopadpoo.set("0")
def chkbt_kapm():#moo
    if checkkaopadmoo.get() == 1:
        kaopadmoo.configure(state=NORMAL)
        varkaopadmoo.set("")
    elif checkkaopadmoo.get() == 0:
        kaopadmoo.configure(state=DISABLED)
        varkaopadmoo.set("0")

def chkbt_kapg():#gaI
    if checkkaopadgai.get() == 1:
        kaopadgai.configure(state=NORMAL)
        varkaopadgai.set("")
    elif checkkaopadgai.get() == 0:
        kaopadgai.configure(state=DISABLED)
        varkaopadgai.set("0")

def chkbt_kapp():#poo
    if checkkaopadpoo.get() == 1:
        kaopadpoo.configure(state=NORMAL)
        varkaopadpoo.set("")
    elif checkkaopadpoo.get() == 0:
        kaopadpoo.configure(state=DISABLED)
        varkaopadpoo.set("0")

kaopadmootik=Checkbutton(frame_MENU,text="Kaopad  moo\t           ฿30  ",variable=checkkaopadmoo,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#AE4D16",command=chkbt_kapm)
kaopadmootik.grid(row=4,column=0,sticky=W)
kaopadmoo=Entry(frame_MENU,textvariable=varkaopadmoo,font=('arial',15,"bold"),width=5,state= DISABLED)
kaopadmoo.grid(row=4,column=0,sticky=E,padx=5)

kaopadgaitik=Checkbutton(frame_MENU,text="Kaopad  gai\t           ฿30  ",variable=checkkaopadgai,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#AE4D16",command=chkbt_kapg)
kaopadgaitik.grid(row=5,column=0,sticky=W)
kaopadgai=Entry(frame_MENU,textvariable=varkaopadgai,font=('arial',15,"bold"),width=5,state= DISABLED)
kaopadgai.grid(row=5,column=0,sticky=E,padx=5)

kaopadpootik=Checkbutton(frame_MENU,text="Kaopad  poo\t           ฿40  ",variable=checkkaopadpoo,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#AE4D16",command=chkbt_kapp)
kaopadpootik.grid(row=6,column=0,sticky=W)
kaopadpoo=Entry(frame_MENU,textvariable=varkaopadpoo,font=('arial',15,"bold"),width=5,state= DISABLED)
kaopadpoo.grid(row=6,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#tod kratiem
varmookratiem=IntVar()
checkmookratiem=IntVar()
varmookratiem.set("0")

vargaikratiem=IntVar()
checkgaikratiem=IntVar()
vargaikratiem.set("0")

def chkbt_mk():#moo
    if checkmookratiem.get() == 1:
        mookratiem.configure(state=NORMAL)
        varmookratiem.set("")
    elif checkmookratiem.get() == 0:
        mookratiem.configure(state=DISABLED)
        varmookratiem.set("0")

def chkbt_gk():#gaI
    if checkgaikratiem.get() == 1:
        gaikratiem.configure(state=NORMAL)
        vargaikratiem.set("")
    elif checkgaikratiem.get() == 0:
        gaikratiem.configure(state=DISABLED)
        vargaikratiem.set("0")

mookratiemtik=Checkbutton(frame_MENU,text="Moo  tod  Kratiem\t           ฿30  ",variable=checkmookratiem,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#056D49",command=chkbt_mk)
mookratiemtik.grid(row=7,column=0,sticky=W)
mookratiem=Entry(frame_MENU,textvariable=varmookratiem,font=('arial',15,"bold"),width=5,state= DISABLED)
mookratiem.grid(row=7,column=0,sticky=E,padx=5)

gaikratiemtik=Checkbutton(frame_MENU,text="Gai  tod  Kratiem\t           ฿30  ",variable=checkgaikratiem,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#056D49",command=chkbt_gk)
gaikratiemtik.grid(row=8,column=0,sticky=W)
gaikratiem=Entry(frame_MENU,textvariable=vargaikratiem,font=('arial',15,"bold"),width=5,state= DISABLED)
gaikratiem.grid(row=8,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#kai jiao #7E0A81
varkaijiao=IntVar()
checkkaijiao=IntVar()
varkaijiao.set("0")

varkaijiaomoo=IntVar()
checkkaijiaomoo=IntVar()
varkaijiaomoo.set("0")

varkaijiaokung=IntVar()
checkkaijiaokung=IntVar()
varkaijiaokung.set("0")

def chkbt_kj():#normal
    if checkkaijiao.get() == 1:
        kaijiao.configure(state=NORMAL)
        varkaijiao.set("")
    elif checkkaijiao.get() == 0:
        kaijiao.configure(state=DISABLED)
        varkaijiao.set("0")

def chkbt_kjms():#moo
    if checkkaijiaomoo.get() == 1:
        kaijiaomoo.configure(state=NORMAL)
        varkaijiaomoo.set("")
    elif checkkaijiaomoo.get() == 0:
        kaijiaomoo.configure(state=DISABLED)
        varkaijiaomoo.set("0")

def chkbt_kjks():#kung
    if checkkaijiaokung.get() == 1:
        kaijiaokung.configure(state=NORMAL)
        varkaijiaokung.set("")
    elif checkkaijiaokung.get() == 0:
        kaijiaokung.configure(state=DISABLED)
        varkaijiaokung.set("0")

kaijiaotik=Checkbutton(frame_MENU,text="Kai  jiao\t\t           ฿20  ",variable=checkkaijiao,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#7E0A81",command=chkbt_kj)
kaijiaotik.grid(row=9,column=0,sticky=W)
kaijiao=Entry(frame_MENU,textvariable=varkaijiao,font=('arial',15,"bold"),width=5,state= DISABLED)
kaijiao.grid(row=9,column=0,sticky=E,padx=5)

kaijiaomootik=Checkbutton(frame_MENU,text="Kai  jiao  moo  sub           ฿30  ",variable=checkkaijiaomoo,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#7E0A81",command=chkbt_kjms)
kaijiaomootik.grid(row=10,column=0,sticky=W)
kaijiaomoo=Entry(frame_MENU,textvariable=varkaijiaomoo,font=('arial',15,"bold"),width=5,state= DISABLED)
kaijiaomoo.grid(row=10,column=0,sticky=E,padx=5)

kaijiaokungtik=Checkbutton(frame_MENU,text="Kai  jiao  kung  sub          ฿35",variable=checkkaijiaokung,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#7E0A81",command=chkbt_kjks)
kaijiaokungtik.grid(row=11,column=0,sticky=W)
kaijiaokung=Entry(frame_MENU,textvariable=varkaijiaokung,font=('arial',15,"bold"),width=5,state= DISABLED)
kaijiaokung.grid(row=11,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#kai daw
varkaidaw=IntVar()
checkkaidaw=IntVar()
varkaidaw.set("0")

def chkbt_kd():#kaidaw
    if checkkaidaw.get() == 1:
        kaidaw.configure(state=NORMAL)
        varkaidaw.set("")
    elif checkkaidaw.get() == 0:
        kaidaw.configure(state=DISABLED)
        varkaidaw.set("0")

kaidawtik=Checkbutton(frame_MENU,text="Kai  daw \t \t           ฿20",variable=checkkaidaw,font=('arial',15,"bold"),bd=5,bg="#FFBF93",fg="#A03D4F",command=chkbt_kd)
kaidawtik.grid(row=12,column=0,sticky=W)
kaidaw=Entry(frame_MENU,textvariable=varkaidaw,font=('arial',15,"bold"),width=5,state= DISABLED)
kaidaw.grid(row=12,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#Frame2
frame2 = Frame(frame_back,width=400,height=611,bg="salmon")
frame2.pack(side=LEFT)

#Drinks
frame_drinks = Frame(frame2,width=400,height=300,relief=RAISED,bd=9,bg="pink")
frame_drinks.pack(side=TOP)
drink_title = Label(frame_drinks,text="DRINKS",font=("arial",20,"bold"),relief=RAISED,bd=5,bg="sea green",fg="white",padx=132)
drink_title.grid(row=0,column=0)
#==========================================================================================================================================
#cola
varcola=IntVar()
checkcola=IntVar()
varcola.set("0")

def chkbt_cola():#cola
    if checkcola.get() == 1:
        cola.configure(state=NORMAL)
        varcola.set("")
    elif checkcola.get() == 0:
        cola.configure(state=DISABLED)
        varcola.set("0")

colatik=Checkbutton(frame_drinks,text="Cola \t\t฿20",variable=checkcola,font=('arial',17,"bold"),bd=5,bg="pink",fg="#18815B",command=chkbt_cola)
colatik.grid(row=2,column=0,sticky=W)
cola=Entry(frame_drinks,textvariable=varcola,font=('arial',15,"bold"),width=5,state= DISABLED)
cola.grid(row=2,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#water
varwater=IntVar()
checkwater=IntVar()
varwater.set("0")

def chkbt_water():#water
    if checkwater.get() == 1:
        water.configure(state=NORMAL)
        varwater.set("")
    elif checkwater.get() == 0:
        water.configure(state=DISABLED)
        varwater.set("0")

watertik=Checkbutton(frame_drinks,text="Water \t\t฿10",variable=checkwater,font=('arial',17,"bold"),bd=5,bg="pink",fg="red4",command=chkbt_water)
watertik.grid(row=1,column=0,sticky=W)
water=Entry(frame_drinks,textvariable=varwater,font=('arial',15,"bold"),width=5,state= DISABLED)
water.grid(row=1,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#kekhauy
varkekhauy=IntVar()
checkkekhauy=IntVar()
varkekhauy.set("0")

def chkbt_kh():#kekhauy
    if checkkekhauy.get() == 1:
        kekhauy.configure(state=NORMAL)
        varkekhauy.set("")
    elif checkkekhauy.get() == 0:
        kekhauy.configure(state=DISABLED)
        varkekhauy.set("0")

kekhauytik=Checkbutton(frame_drinks,text="Kekhauy \t\t฿20",variable=checkkekhauy,font=('arial',17,"bold"),bd=5,bg="pink",fg="#18815B",command=chkbt_kh)
kekhauytik.grid(row=3,column=0,sticky=W)
kekhauy=Entry(frame_drinks,textvariable=varkekhauy,font=('arial',15,"bold"),width=5,state= DISABLED)
kekhauy.grid(row=3,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#green tea
vartea=IntVar()
checktea=IntVar()
vartea.set("0")

def chkbt_tea():#tea
    if checktea.get() == 1:
        tea.configure(state=NORMAL)
        vartea.set("")
    elif checktea.get() == 0:
        tea.configure(state=DISABLED)
        vartea.set("0")

teatik=Checkbutton(frame_drinks,text="Tea \t\t฿20",variable=checktea,font=('arial',17,"bold"),bd=5,bg="pink",fg="#18815B",command=chkbt_tea)
teatik.grid(row=4,column=0,sticky=W)
tea=Entry(frame_drinks,textvariable=vartea,font=('arial',15,"bold"),width=5,state= DISABLED)
tea.grid(row=4,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#orange juice
varorange=IntVar()
checkorange=IntVar()
varorange.set("0")

def chkbt_or():#tea
    if checkorange.get() == 1:
        orange.configure(state=NORMAL)
        varorange.set("")
    elif checkorange.get() == 0:
        orange.configure(state=DISABLED)
        varorange.set("0")

orangetik=Checkbutton(frame_drinks,text="Orange  Juice         ฿20",variable=checkorange,font=('arial',17,"bold"),bd=5,bg="pink",fg="red4",command=chkbt_or)
orangetik.grid(row=5,column=0,sticky=W)
orange=Entry(frame_drinks,textvariable=varorange,font=('arial',15,"bold"),width=5,state= DISABLED)
orange.grid(row=5,column=0,sticky=E,padx=5)
#==========================================================================================================================================
#bill
frame_bill = Frame(frame2,width=400,height=311,relief=RAISED,bd=9,bg="#98D0F7")
frame_bill.pack(side=BOTTOM)
#==========================================================================================================================================
#thx,cal
def cal_thx():
    food1 = varkraprawmoo.get()
    food2 = varkraprawgai.get()
    food3 = varkraprawmookrob.get()
    food4 = varkaopadmoo.get()
    food5 = varkaopadgai.get()
    food6 = varkaopadpoo.get()
    food7 = varmookratiem.get()
    food8 = vargaikratiem.get()
    food9 = varkaijiao.get()
    food10 = varkaijiaomoo.get()
    food11 = varkaijiaokung.get()
    food12 = varkaidaw.get()
    drinks1 = varwater.get()
    drinks2 = varcola.get()
    drinks3 = varkekhauy.get()
    drinks4 = vartea.get()
    drinks5 = varorange.get()
    total = (food1*30)+(food2*30)+(food3*40)+(food4*30)+(food5*30)+(food6*40)+(food7*30)+(food8*30)+(food9*20)+(food10*30)+(food11*35)+(food12*20)+(drinks1*10)+(drinks2*20)+(drinks3*20)+(drinks4*20)+(drinks5*20)
    
    total_show = Label(frame_bill,text=f"{total}.00Baht",font=("arial",18,"bold"),relief=SUNKEN,width=18,height=2,bd=9)
    total_show.grid(row=2,column=0,pady=20)

    messagebox.showinfo("THX","Thank you. Have a nice day.")
    root.destroy()

bill = Button(frame_bill,text="CHECK BILL",font=("arial",20,"bold"),relief=RAISED,bd=5,bg="red4",fg="white",cursor="circle",padx=91,command=cal_thx)
bill.grid(row=0,column=0)
#==========================================================================================================================================
#reset
def reset():
    kraprawmootik.deselect()
    kraprawgaitik.deselect()
    kraprawmookrobtik.deselect()
    kaopadmootik.deselect()
    kaopadgaitik.deselect()
    kaopadpootik.deselect()
    mookratiemtik.deselect()
    gaikratiemtik.deselect()
    kaijiaotik.deselect()
    kaijiaomootik.deselect()
    kaijiaokungtik.deselect()
    kaidawtik.deselect()
    colatik.deselect()
    watertik.deselect()
    kekhauytik.deselect()
    teatik.deselect()
    orangetik.deselect()

    kraprawmoo.configure(state = DISABLED)
    kraprawgai.configure(state = DISABLED)
    kraprawmookrob.configure(state = DISABLED)
    kaopadmoo.configure(state = DISABLED)
    kaopadgai.configure(state = DISABLED)
    kaopadpoo.configure(state = DISABLED)
    mookratiem.configure(state = DISABLED)
    gaikratiem.configure(state = DISABLED)
    kaijiao.configure(state = DISABLED)
    kaijiaomoo.configure(state = DISABLED)
    kaijiaokung.configure(state = DISABLED)
    kaidaw.configure(state = DISABLED)
    cola.configure(state = DISABLED)
    water.configure(state = DISABLED)
    kekhauy.configure(state = DISABLED)
    tea.configure(state = DISABLED)
    orange.configure(state = DISABLED)

    varkraprawmoo.set("0")
    varkraprawgai.set("0")
    varkraprawmookrob.set("0")
    varkaopadmoo.set("0")
    varkaopadgai.set("0")
    varkaopadpoo.set("0")
    varmookratiem.set("0")
    vargaikratiem.set("0")
    varkaijiao.set("0")
    varkaijiaomoo.set("0")
    varkaijiaokung.set("0")
    varkaidaw.set("0")
    varcola.set("0")
    varwater.set("0")
    varkekhauy.set("0")
    vartea.set("0")
    varorange.set("0")


re = Button(frame_bill,text="RESET",font=("arial",20,"bold"),relief=RAISED,bd=5,bg="red4",cursor="circle",fg="white",padx=130,command=reset)
re.grid(row=3,column=0)
#==========================================================================================================================================
#
total = Label(frame_bill,text="Total",font=("arial",20,"bold"),relief=SOLID,bd=2,bg="sea green",fg="white",padx=130)
total.grid(row=1,column=0,pady=10)
#==========================================================================================================================================
#show
total_show = Label(frame_bill,text="",font=("arial",18,"bold"),relief=SUNKEN,width=18,height=2,bd=9)
total_show.grid(row=2,column=0,pady=20)
#==========================================================================================================================================
#==========================================================================================================================================
#made by
by=Label(frame_MENU,text="MADE BY : NAPATSAKORN PHOLA  ",font=('arial',16),bd=9,bg="black",relief=GROOVE,fg="cyan")
by.grid(row=13,column=0)

root.mainloop()
