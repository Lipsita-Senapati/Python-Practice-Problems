from tkinter import *
w=Tk()
def create():
    from random import sample
    n =sample(range(10),6)
    L1.configure(text=n[0])
    L2.configure(text=n[1])
    L3.configure(text=n[2])
    L4.configure(text=n[3])
    L5.configure(text=n[4])
    L6.configure(text=n[5])


def reset():
    from random import sample
    n =sample(range(10),6)
    L1.configure(text="...")
    L2.configure(text="...")
    L3.configure(text="...")
    L4.configure(text="...")
    L5.configure(text="...")
    L6.configure(text="...")

###design the componentss
img = PhotoImage(file=r"C:\Users\ASUS\Desktop\lottery.png")
Limg = Label(w,image=img)
L1 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)
L2 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)
L3 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)
L4 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)
L5 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)
L6 = Label(w,relief='solid',text="...",font=("arial",20,"bold"),width=2)

B1 = Button(w,command=create,text="Get Your Lucky No.",font=("arial",20,"bold"))
B2 = Button(w,command=reset,text="Reset",font=("arial",20,"bold"))

Limg.grid(row=1,column=1,rowspan=2)
L1.grid(row=1,column=2)
L2.grid(row=1,column=3)
L3.grid(row=1,column=4)
L4.grid(row=1,column=5)
L5.grid(row=1,column=6)
L6.grid(row=1,column=7)

B1.grid(row=2,column=2,columnspan=4)

B2.grid(row=2,column=6,columnspan=2)

w.mainloop()
