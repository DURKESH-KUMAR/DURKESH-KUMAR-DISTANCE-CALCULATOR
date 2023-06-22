from tkinter import *


import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your distance calculator will open sooner please wait ")

x.runAndWait()
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("python index.py")
lbl=Button(root,text="DISTANCE CALCULATOR",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)
def display():
    import os
    os.system("python time_1.py")

btns=Button(root,text="TIME",command=display)
btns.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btns.pack(side=LEFT,padx=10)
img=PhotoImage(file="core.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()

lbl2=Label(root,text="ENTER THE FILE NAME:")
lbl2.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl2.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",20,"bold"))
entry.pack(padx=10,pady=20)
def graph():
    v=entry.get()
    w=str(v)+".txt"

    x=open(w,"r")

    y=x.read()
    print(y)
    print(type(y))
    n=[]
    for i in y:
        if i==",":
            continue
        b=int(i)
        n.append(b)

    import matplotlib.pyplot as plt
    plt.plot(n)
    plt.xlabel("distance")
    plt.ylabel("time")
    plt.title("DISTANCE CALCULATOR")
    plt.show()
    
    
    
    import matplotlib.pyplot as plt
    plt.plot(a)
    plt.xlabel("distance")
    plt.ylabel("time")
    plt.show()
    
btn=Button(root,text="GRAPH",command=graph)
btn.config(font=("callibri",20,"bold italic"),bg="green",fg="black")
btn.pack(padx=20,pady=20)

root.mainloop()
